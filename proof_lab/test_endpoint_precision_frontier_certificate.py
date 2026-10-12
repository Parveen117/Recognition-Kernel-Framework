"""Independent arithmetic controls for SE11's finer and faster enclosure."""
import itertools
import unittest
from decimal import localcontext
from fractions import Fraction as F
from math import factorial

from proof_lab.endpoint_full_aperture_certificate import BERNOULLI, I, hurwitz_power, log_positive
from proof_lab.endpoint_precision_frontier_certificate import (
    GAMMA_TERMS, GRID, gauss24, gamma_symbol, node_error, odd_bessel, refined_constants,
)
from proof_lab.test_endpoint_prime_power_certificate import complex_product, reduced_log


def shifted_gamma(t, pi, log2):
    """Independent complex digamma expansion shifted by 2048, with its tail."""
    a, y = F(8193, 4), t/2
    inverse = (a/(a*a+y*y), -y/(a*a+y*y))
    square, power = complex_product(inverse, inverse), (F(1), F(0))
    value = reduced_log(a*a+y*y, log2)/2-inverse[0]/2-log_positive(pi)
    for k, bernoulli in enumerate(BERNOULLI, 1):
        power = complex_product(power, square)
        value = value-bernoulli*power[0]/(2*k)
    value = value-sum((F(4*k+1, 4)/(F(4*k+1, 4)**2+y*y)
                       for k in range(2048)), F(0))
    error = abs(BERNOULLI[-1])/(12*a**12)
    return value+I(-error, error)


class PrecisionFrontierTests(unittest.TestCase):
    def test_gauss24_all_degree47_moments(self):
        with localcontext() as context:
            context.prec = 90
            nodes, weights = gauss24()
            self.assertEqual(len(nodes), 24)
            self.assertTrue(all(w.lo > 0 for w in weights))
            for degree in range(48):
                value = sum((w*x**degree for x, w in zip(nodes, weights)), I(0))
                exact = F(0) if degree % 2 else F(2, degree+1)
                self.assertLessEqual(F(value.lo), exact, degree)
                self.assertGreaterEqual(F(value.hi), exact, degree)
                self.assertLess(F(value.hi)-F(value.lo), F(1, 10**60))

    def test_refined_gamma_contains_independent_shifted_expansion(self):
        with localcontext() as context:
            context.prec = 90
            pi, log2, mg = refined_constants()
            self.assertLess(F(mg.hi)-F(mg.lo), F(1, 10**37))
            zeta = [hurwitz_power(2*r+1) for r in range(1, GAMMA_TERMS+2)]
            for t in [F(0), F(32), F(96), F(160)]:
                actual = gamma_symbol(I(t), mg, zeta)
                control = shifted_gamma(t, pi, log2)
                self.assertLessEqual(actual.lo, control.lo, str(t))
                self.assertGreaterEqual(actual.hi, control.hi, str(t))
                self.assertLess(F(control.hi)-F(control.lo), F(1, 10**40))

    def test_bessel_against_exact_trigonometric_formulas_through128(self):
        with localcontext() as context:
            context.prec = 90
            for z in [F(1, 64), F(1), F(64), F(128)]:
                sine = sum(((-1)**k*z**(2*k+1)/factorial(2*k+1)
                            for k in range(400)), F(0))
                cosine = sum(((-1)**k*z**(2*k)/factorial(2*k)
                              for k in range(400)), F(0))
                sine_error, cosine_error = z**801/F(factorial(801)), z**800/F(factorial(800))
                got = odd_bessel(I(z))
                for index, (s, c) in enumerate([
                    (1/z**2, -1/z), (15/z**4-6/z**2, 1/z-15/z**3),
                ]):
                    expected = s*sine+c*cosine
                    error = abs(s)*sine_error+abs(c)*cosine_error
                    self.assertLessEqual(F(got[index].lo), expected+error)
                    self.assertGreaterEqual(F(got[index].hi), expected-error)
                    self.assertLess(F(got[index].hi)-F(got[index].lo), F(1, 10**30))

    def test_signed_gram_bound_against_exact_rational_corner_matrices(self):
        with localcontext() as context:
            context.prec = 90
            epsilon = F(1, 10**7)
            vector = [I(F(3, 5)-epsilon, F(3, 5)), I(F(4, 5)-epsilon, F(4, 5))]
            self.assertLessEqual(sum(F(v.hi)**2 for v in vector), 1)
            for sign in [-1, 1]:
                measure = I(sign*F(3, 2)-epsilon, sign*F(3, 2)+epsilon)
                integer, integers, error = node_error(measure, vector)
                mu, u = F(integer, GRID), [F(x, GRID) for x in integers]
                for weight, v0, v1 in itertools.product(
                    [F(measure.lo), F(measure.hi)],
                    [F(vector[0].lo), F(vector[0].hi)],
                    [F(vector[1].lo), F(vector[1].hi)],
                ):
                    v = [v0, v1]
                    frobenius_squared = sum((weight*v[i]*v[j]-mu*u[i]*u[j])**2
                                            for i in range(2) for j in range(2))
                    self.assertLessEqual(frobenius_squared, F(error.hi)**2)


if __name__ == '__main__':
    unittest.main()
