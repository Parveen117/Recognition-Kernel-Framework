"""Independent checks for SE10's larger integration and frequency ranges."""
import unittest
from decimal import localcontext
from fractions import Fraction as F
from math import factorial

from proof_lab.endpoint_full_aperture_certificate import (
    BERNOULLI, I, constants, hurwitz_power, log_positive,
)
from proof_lab.endpoint_prime_power_certificate import (
    GAMMA_TERMS, SCALE, T, gauss20, gamma_symbol, odd_bessel,
)


def complex_product(left, right):
    a, b = left
    c, d = right
    return a*c-b*d, a*d+b*c


def reduced_log(x, log2):
    exponent = 0
    while x >= 2:
        x /= 2
        exponent += 1
    return log_positive(x)+exponent*log2


def independent_digamma_real(t, pi, log2):
    """Shifted complex Euler--Maclaurin; no Gamma-ground constant is used.

    psi(z)=log(z)-1/(2z)-sum B_2k/(2k*z**(2k))+R after shifting by 128.
    Periodic Bernoulli gives |R|<=|B12|/(12*Re(z)**12).
    All complex powers below are exact rational pairs.
    """
    a, y = F(513, 4), t/2
    inv = (a/(a*a+y*y), -y/(a*a+y*y))
    inverse_square = complex_product(inv, inv)
    power = (F(1), F(0))
    value = reduced_log(a*a+y*y, log2)/2-inv[0]/2-log_positive(pi)
    for k, bernoulli in enumerate(BERNOULLI, 1):
        power = complex_product(power, inverse_square)
        value = value-bernoulli*power[0]/(2*k)
    value = value-sum((F(4*k+1, 4)/(F(4*k+1, 4)**2+y*y)
                       for k in range(128)), F(0))
    error = abs(BERNOULLI[-1])/(12*a**12)
    return value+I(-error, error)


class PrimePowerArithmeticTests(unittest.TestCase):
    def test_gauss20_encloses_all_degree_39_moments(self):
        with localcontext() as context:
            context.prec = 90
            nodes, weights = gauss20()
            self.assertEqual(len(nodes), 20)
            self.assertTrue(all(w.lo > 0 for w in weights))
            for degree in range(40):
                moment = sum((w*x**degree for x, w in zip(nodes, weights)), I(0))
                exact = F(0) if degree % 2 else F(2, degree+1)
                self.assertLessEqual(F(moment.lo), exact, degree)
                self.assertGreaterEqual(F(moment.hi), exact, degree)
                self.assertLess(F(moment.hi)-F(moment.lo), F(1, 10**60))

    def test_gamma_contains_independent_shifted_complex_expansion(self):
        with localcontext() as context:
            context.prec = 90
            pi, log2, mg = constants()
            zeta = [hurwitz_power(2*r+1) for r in range(1, GAMMA_TERMS+2)]
            for t in [F(0), F(24), F(96), F(T)/SCALE]:
                actual = gamma_symbol(I(t), mg, zeta)
                control = independent_digamma_real(t, pi, log2)
                self.assertLessEqual(actual.lo, control.lo, str(t))
                self.assertGreaterEqual(actual.hi, control.hi, str(t))
                self.assertLess(F(control.hi)-F(control.lo), F(1, 10**25))

    def test_bessel_seeds_against_direct_j1_j3_through_96(self):
        with localcontext() as context:
            context.prec = 90
            for z in [F(1, 64), F(1), F(48), F(96)]:
                sine = sum(((-1)**k*z**(2*k+1)/factorial(2*k+1)
                            for k in range(360)), F(0))
                cosine = sum(((-1)**k*z**(2*k)/factorial(2*k)
                              for k in range(360)), F(0))
                sine_error = z**721/F(factorial(721))
                cosine_error = z**720/F(factorial(720))
                got = odd_bessel(I(z))
                for index, (s, c) in enumerate([
                    (1/z**2, -1/z),
                    (15/z**4-6/z**2, 1/z-15/z**3),
                ]):
                    expected = s*sine+c*cosine
                    error = abs(s)*sine_error+abs(c)*cosine_error
                    self.assertLessEqual(F(got[index].lo), expected+error)
                    self.assertGreaterEqual(F(got[index].hi), expected-error)
                    # At z=96, interval recurrence cancellation costs about
                    # forty of the ninety working digits. Formula containment
                    # is the correctness check; this width guard still leaves
                    # over thirty digits beyond the required matrix accuracy.
                    self.assertLess(F(got[index].hi)-F(got[index].lo), F(1, 10**45), str(z))


if __name__ == '__main__':
    unittest.main()
