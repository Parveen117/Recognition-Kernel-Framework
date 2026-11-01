"""Independent exact controls for SE16's signed-return source certificate."""
from fractions import Fraction as F
import itertools
import unittest

from proof_lab.endpoint_full_aperture_certificate import I, log_positive, sqrt_integer
from proof_lab.endpoint_global_eta_certificate import integer_log
from proof_lab.endpoint_signed_return_certificate import (
    ETA, FLOOR, MG_CAP, NATIVE_FLOOR, comparison_cell, gamma_row,
    prime_catalogue, prime_row_upper,
)


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


class SignedReturnTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = prime_catalogue()

    def test_positive_prime_mass_contains_independent_alternating_enclosure(self):
        # This oracle differentiates the alternating Dirichlet identity at
        # s=5/2; the production mass uses a positive prime-power sieve.
        count, log2 = 1024, log_positive(2)
        e, d = I(0), I(0)
        for n in range(1, count+1):
            coefficient = F((-1)**(n-1), n*n)/sqrt_integer(n)
            e = e+coefficient
            d = d+coefficient*integer_log(n, log2)
        rem = I(1)/((count+1)**2*sqrt_integer(count+1))
        e = e+I(0, rem.hi)
        d = d+I(0, (rem*integer_log(count+1, log2)).hi)
        exact = log2/(2*sqrt_integer(2)-1)+d/e
        self.assertLess(self.cat['mass'].lo, exact.lo)
        self.assertGreater(self.cat['mass'].hi, exact.hi)
        wrong_sign = log2/(2*sqrt_integer(2)-1)-d/e
        self.assertGreater(wrong_sign.lo, self.cat['mass'].hi)

    def test_catalogue_against_trial_division_prime_power_definition(self):
        for n in range(2, 160):
            factors, remaining, p = [], n, 2
            while p*p <= remaining:
                if remaining % p == 0:
                    factors.append(p)
                    while remaining % p == 0:
                        remaining //= p
                p += 1
            if remaining > 1:
                factors.append(remaining)
            value = self.cat['weights'][n]
            if len(factors) == 1:
                independent = log_positive(factors[0], count=1800)
                self.assertLessEqual(value.lo, independent.hi)
                self.assertGreaterEqual(value.hi, independent.lo)
            else:
                self.assertEqual(value.record(), ['0', '0'])

    def test_prime_breakpoint_is_counted_once_with_its_complete_peak(self):
        # Synthetic one-event catalogue at n=4 with rational weight one.
        limit = 16
        prefix = [I(0 if n < 4 else 8) for n in range(limit+1)]
        suffix = [I(F(1, 32) if n < 4 else 0) for n in range(limit+1)]
        peaks = [I(F(1, 8) if n == 4 else 0) for n in range(limit+1)]
        cat = dict(limit=limit, prefix=prefix, suffix=suffix, peaks=peaks,
                   mass=I(F(1, 32)), tail=I(0))
        left, right = F(49, 100), F(51, 100)
        upper = prime_row_upper(left, right, cat)
        exact_upper = right**6/F(32)+F(1, 8)
        self.assertLessEqual(F(upper.lo), exact_upper)
        self.assertGreaterEqual(F(upper.hi), exact_upper)
        for j in range(49, 52):
            z = F(j, 100)
            direct = z**6/F(32)+min(8*z**6, 1/(32*z*z))
            self.assertGreaterEqual(F(upper.hi), direct)
        double_counted = right**6*(F(8)+F(1, 32))+F(1, 32)/left**2
        self.assertGreater(double_counted, 2*F(upper.hi)-F(1, 100))

    def test_odd_folding_retains_the_opposite_side_kernel(self):
        # x_i=2*i*log(2), so the two exponential kernels are rational.
        values = {1: (F(1), F(2)), 2: (F(-3), F(1)), 3: (F(2), F(-1))}
        for beta_twice in (1, 5):
            full = F(0)
            for i, j in itertools.product((-3, -2, -1, 1, 2, 3), repeat=2):
                a = tuple((1 if i > 0 else -1)*v for v in values[abs(i)])
                b = tuple((1 if j > 0 else -1)*v for v in values[abs(j)])
                kernel = F(1, 2**(3*abs(i)+3*abs(j)+beta_twice*abs(i-j)))
                full += kernel*dot(a, b)
            folded = F(0)
            for i, j in itertools.product((1, 2, 3), repeat=2):
                kernel = F(1, 2**(3*i+3*j))*(F(1, 2**(beta_twice*abs(i-j)))
                                                     -F(1, 2**(beta_twice*(i+j))))
                folded += 2*kernel*dot(values[i], values[j])
            self.assertEqual(full, folded)

    def test_weighted_row_defect_is_exact_for_complex_readings(self):
        kernel = [[F(2), F(3), F(1)], [F(3), F(1), F(4)], [F(1), F(4), F(5)]]
        weight = [F(1), F(1, 2), F(1, 7)]
        values = [(F(1), F(2)), (F(-3), F(1)), (F(2), F(-1))]
        direct = sum((kernel[i][j]*dot(values[i], values[j])
                      for i, j in itertools.product(range(3), repeat=2)), F(0))
        row = [sum((kernel[i][j]*weight[j] for j in range(3)), F(0))/weight[i]
               for i in range(3)]
        diagonal = sum((row[i]*dot(values[i], values[i]) for i in range(3)), F(0))
        residual = F(0)
        for i, j in itertools.product(range(3), repeat=2):
            delta = tuple(values[i][k]/weight[i]-values[j][k]/weight[j] for k in range(2))
            residual += kernel[i][j]*weight[i]*weight[j]*dot(delta, delta)/2
        self.assertEqual(diagonal-direct, residual)
        self.assertGreater(residual, 0)
        self.assertNotEqual(diagonal-direct, residual/2)

    def test_gamma_rows_against_three_separately_integrated_pieces(self):
        # Integrate the intervals (0,x), (x,infinity), and the reflected
        # kernel separately. At x=2*k*log(2) all exponentials are rational.
        for k in (1, 2, 4):
            z, total = F(1, 2**k), F(0)
            for beta in (F(1, 2), F(5, 2)):
                eb = z**int(2*beta)
                ec = z**4
                piece_left = (eb-ec)/(2-beta)
                piece_right = ec/(2+beta)
                reflected = eb/(2+beta)
                total += z**2*(piece_left+piece_right-reflected)
            self.assertEqual(total, gamma_row(z))
            self.assertGreater(gamma_row(z, False), total)

    def test_native_floor_and_implied_shift_use_the_graph_metric(self):
        self.assertEqual(NATIVE_FLOOR, F(1, 1845))
        self.assertEqual(ETA-NATIVE_FLOOR, F(25441, 36900))
        for physical, positive_gamma in itertools.product((F(0), F(1, 7), F(3)), repeat=2):
            lower = FLOOR*physical+2*ETA*positive_gamma
            native_upper = (2+MG_CAP)*physical+2*positive_gamma
            self.assertGreaterEqual(lower, NATIVE_FLOOR*native_upper)

    def test_retained_reflection_passes_and_erased_comparison_fails(self):
        z = 1/sqrt_integer(3)
        lower = comparison_cell(F(z.lo), F(z.hi), self.cat)
        self.assertGreater(lower.lo, I(FLOOR).hi)
        # Direct prime formula exactly at exp(x)=3, independent of cell logic.
        prime = (self.cat['prefix'][3]+self.cat['mass'])/27+3*(
            self.cat['suffix'][3]+I(0, self.cat['tail'].hi))
        diagonal = ETA-F(1, 10)+(ETA-(1-ETA)*(MG_CAP-F(24, 5))+F(1, 10))/27
        erased = diagonal-(1-ETA)*gamma_row(z, False)-prime
        self.assertLess(erased.hi, 0)


if __name__ == '__main__':
    unittest.main()
