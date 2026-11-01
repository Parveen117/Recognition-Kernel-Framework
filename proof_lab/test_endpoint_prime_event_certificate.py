"""Independent controls for the larger SE9 Bessel range and matrix dimension."""
import unittest
from decimal import localcontext
from fractions import Fraction as F
from math import factorial

from proof_lab.endpoint_prime_event_certificate import I, N, odd_bessel, interval_ldl


class PrimeEventArithmeticTests(unittest.TestCase):
    def test_larger_bessel_recurrence_against_direct_j1_and_j3(self):
        with localcontext() as context:
            context.prec = 90
            for z in [F(1, 64), F(1), F(24), F(48)]:
                sine = sum(((-1)**k*z**(2*k+1)/factorial(2*k+1)
                            for k in range(240)), F(0))
                cosine = sum(((-1)**k*z**(2*k)/factorial(2*k)
                              for k in range(240)), F(0))
                sine_error = z**481/F(factorial(481))
                cosine_error = z**480/F(factorial(480))
                # These independent closed trigonometric formulas do not use
                # high-order seeds or the downward recurrence being checked.
                for index, (s, c) in enumerate([
                    (1/z**2, -1/z),
                    (15/z**4-6/z**2, 1/z-15/z**3),
                ]):
                    expected = s*sine+c*cosine
                    error = abs(s)*sine_error+abs(c)*cosine_error
                    got = odd_bessel(I(z))[index]
                    self.assertLessEqual(F(got.lo), expected+error)
                    self.assertGreaterEqual(F(got.hi), expected-error)
                    self.assertLess(F(got.hi)-F(got.lo), F(1, 10**55))

    def test_ldl_checks_coupling_at_the_new_last_coordinate(self):
        matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
        self.assertEqual(len(interval_ldl(matrix, F(1, 2))), N)
        matrix[0][-1] = matrix[-1][0] = 2
        with self.assertRaises(AssertionError):
            interval_ldl(matrix, F(0))


if __name__ == '__main__':
    unittest.main()
