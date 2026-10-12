"""Independent exact controls for the SE15 bounds; not formal verification."""
from fractions import Fraction as F
import itertools
import unittest

from proof_lab.endpoint_full_aperture_certificate import I, log_positive
from proof_lab.endpoint_global_eta_certificate import (
    BOUNDARY_CAP, ETA, MG_CAP, PRIME_CAP, integer_log,
    localization_budget, obligation, prime_mass_enclosure,
)


class GlobalEtaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mass = prime_mass_enclosure()
        cls.log2 = log_positive(2)

    def test_prime_mass_against_independent_positive_prime_power_sum(self):
        # Sieve prime powers directly. This oracle does not use zeta, the
        # alternating identity, or its logarithmic derivative.
        cutoff = 4096
        is_prime = [True]*(cutoff+1)
        is_prime[:2] = [False, False]
        lower = I(0)
        lambda_four = None
        for p in range(2, cutoff+1):
            if not is_prime[p]:
                continue
            for composite in range(p*p, cutoff+1, p):
                is_prime[composite] = False
            logarithm = integer_log(p, self.log2)
            power = p
            while power <= cutoff:
                lower = lower+logarithm/(power*power)
                if power == 4:
                    lambda_four = logarithm
                power *= p
        upper = lower+(integer_log(cutoff, self.log2)+1)/cutoff
        mass = self.mass['mass']
        self.assertLess(lower.hi, mass.lo)
        self.assertGreater(upper.lo, mass.hi)
        self.assertEqual(lambda_four.record(), self.log2.record())
        # A changed derivative sign is numerically plausible but wrong.
        wrong = self.log2-self.mass['logarithmic_sum']/self.mass['denominator']
        self.assertGreater(wrong.lo, upper.hi)

    def test_binary_log_against_rational_series_without_binary_reduction(self):
        for n in (1, 2, 3, 7, 15, 31):
            z = F(n-1, n+1)
            terms = 1800
            power, total = z, F(0)
            for j in range(terms):
                total += 2*power/(2*j+1)
                power *= z*z
            tail = 2*power/((2*terms+1)*(1-z*z))
            got = integer_log(n, self.log2)
            self.assertLessEqual(F(got.lo), total+tail)
            self.assertGreaterEqual(F(got.hi), total)
            self.assertLess(F(got.hi)-F(got.lo), F(1, 10**80))

    def test_weighted_boundary_constant_against_positive_rational_series(self):
        # Expand 1/(1-exp(-3*x)) before integration; all terms are positive.
        count = 128
        partial = sum((F(1, 3*k-1)-F(2, 3*k)+F(1, 3*k+1)
                       for k in range(1, count+1)), F(0))
        tail = F(1, 24*count*count)
        got = log_positive(3)-1
        self.assertLess(partial, F(got.lo))
        self.assertGreater(partial+tail, F(got.hi))
        self.assertLess(F(got.hi), BOUNDARY_CAP)

    def test_complex_jump_localization_retains_signed_cross_term(self):
        # Complex numbers are pairs of rationals to keep every operation exact.
        frames = ((F(1), F(0)), (F(3, 5), F(4, 5)), (F(0), F(1)))
        values = ((F(2), F(3)), (F(-1), F(4)), (F(3), F(-2)))
        def norm(z):
            return z[0]*z[0]+z[1]*z[1]
        for i, j in itertools.product(range(3), repeat=2):
            a, b = values[i], values[j]
            direct = norm((a[0]-b[0], a[1]-b[1]))
            localized = sum((norm((frames[i][k]*a[0]-frames[j][k]*b[0],
                                   frames[i][k]*a[1]-frames[j][k]*b[1]))
                             for k in range(2)), F(0))
            defect = sum(((frames[i][k]-frames[j][k])**2 for k in range(2)), F(0))
            cross = a[0]*b[0]+a[1]*b[1]
            self.assertEqual(direct, localized-defect*cross)
        self.assertNotEqual(values[0][0]*values[1][0]+values[0][1]*values[1][1], 0)

    def test_pole_localization_has_full_two_sided_cross_coefficient(self):
        frames = ((F(1), F(0)), (F(3, 5), F(4, 5)), (F(0), F(1)))
        v, f = (F(2), F(-3), F(1)), (F(1), F(2), F(-4))
        source = lambda z: -2*sum((a*b for a, b in zip(v, z)), F(0))**2
        localized = sum((source([frames[i][k]*f[i] for i in range(3)])
                         for k in range(2)), F(0))
        remainder = sum((v[i]*v[j]*f[i]*f[j]*sum(
            ((frames[i][k]-frames[j][k])**2 for k in range(2)), F(0))
            for i, j in itertools.product(range(3), repeat=2)), F(0))
        self.assertEqual(source(f), localized-remainder)
        self.assertNotEqual(source(f), localized)
        self.assertNotEqual(source(f), localized-remainder/2)

    def test_gamma_jump_normalization_against_laplace_transform(self):
        for k, xi in itertools.product(range(7), (F(1, 3), F(2), F(17))):
            a, beta = F(4*k+1, 4), F(4*k+1, 2)
            digamma_increment = (xi/2)**2/(a*(a*a+(xi/2)**2))
            # Integral exp(-beta*t)*(1-cos(xi*t)) dt.
            laplace_increment = 1/beta-beta/(beta*beta+xi*xi)
            self.assertEqual(digamma_increment, 2*laplace_increment)
            self.assertNotEqual(digamma_increment, laplace_increment)

    def test_source_polynomial_factorization_and_failed_zero_shift(self):
        for u in (F(0), F(1, 17), F(1, 2), F(16, 17), F(1)):
            direct = (ETA+(ETA-(1-ETA)*MG_CAP)*u
                      -PRIME_CAP*(1+u*u)-BOUNDARY_CAP*(1-u))
            factored = (1-u)*(ETA-PRIME_CAP-BOUNDARY_CAP+PRIME_CAP*u)
            self.assertEqual(direct, factored)
            self.assertGreaterEqual(direct, 0)
        self.assertLess(-MG_CAP-2*PRIME_CAP, 0)
        self.assertGreater(ETA-PRIME_CAP-BOUNDARY_CAP, 0)

    def test_cut_is_l2_isometry_but_need_not_be_native_isometry(self):
        # Exact graph metric I+C^T C. A coordinate partition preserves L2
        # while dropping a nonzero graph cross term: it cannot be substituted.
        f = (F(1), F(1))
        native = lambda z: z[0]**2+z[1]**2+(z[0]+z[1])**2
        self.assertEqual(sum(x*x for x in f), 2)
        self.assertEqual(native(f), 6)
        self.assertEqual(native((1, 0))+native((0, 1)), 4)
        # Positive diagonal observations do not certify the whole source.
        quadratic = lambda z: z[0]**2+4*z[0]*z[1]+z[1]**2
        self.assertGreater(quadratic((1, 0)), 0)
        self.assertGreater(quadratic((0, 1)), 0)
        self.assertLess(quadratic((1, -1)), 0)

    def test_schedule_is_conditional_and_rejects_zero_limit_as_input(self):
        for target in (F(1, 2), F(1, 1000)):
            row = obligation(target, self.log2)
            self.assertFalse(row['local_certificate_executed'])
            self.assertEqual(row['status'], 'CONDITIONAL_LOCAL_OBLIGATION')
            self.assertLessEqual(F(row['conditional_global_allowance_upper']), target)
            self.assertLessEqual(F(row['logarithmic_inner_radius'][1])+1,
                                 F(row['aperture_radius']))
        for target in (0, -1):
            with self.assertRaises(ValueError):
                obligation(target, self.log2)
        for count in (0, 1, 3):
            with self.assertRaises(ValueError):
                prime_mass_enclosure(count)
        with self.assertRaises(ValueError):
            localization_budget(1, I(0))


if __name__ == '__main__':
    unittest.main()
