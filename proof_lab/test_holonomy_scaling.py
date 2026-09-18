import unittest
from fractions import Fraction

from proof_lab.morphic_recognition.holonomy import (
    I, X, Y, ZERO, add, commutator, determinant_coefficients, evaluate,
    exp_upper_rational, holonomy_error_bound, identity_error_bound, matrix,
    matrix_power, multiply, nilpotent_euler_holonomy_coefficients, norm_inf,
    polynomial_multiply, scale, verify_holonomy_contract,
)


class HolonomyScalingTests(unittest.TestCase):
    def test_exact_loop_polynomial_and_determinant(self):
        p = nilpotent_euler_holonomy_coefficients(X, Y)
        self.assertEqual(p, (I, ZERO, matrix(1, 0, 0, -1),
                             matrix(0, -1, 1, 0), matrix(1, 0, 0, 0)))
        self.assertEqual(determinant_coefficients(p), (Fraction(1),))
        self.assertEqual(polynomial_multiply((I, X), (I, scale(-1, X))), (I,))

    def test_orientation_sign_is_not_interchangeable(self):
        forward = nilpotent_euler_holonomy_coefficients(X, Y)
        backward = nilpotent_euler_holonomy_coefficients(Y, X)
        self.assertEqual(forward[2], commutator(X, Y))
        self.assertEqual(backward[2], scale(-1, forward[2]))
        self.assertNotEqual(forward[2], backward[2])

    def test_commuting_nilpotent_controls(self):
        self.assertEqual(nilpotent_euler_holonomy_coefficients(X, X), (I,))
        self.assertEqual(nilpotent_euler_holonomy_coefficients(X, ZERO), (I,))
        self.assertEqual(nilpotent_euler_holonomy_coefficients(X, scale(3, X)), (I,))

    def test_remainder_bound_is_exact_at_domain_endpoint(self):
        p = nilpotent_euler_holonomy_coefficients(X, Y)
        for h in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1)):
            remainder = add(evaluate(p, h), scale(-1, add(I, scale(h*h, commutator(X, Y)))))
            self.assertEqual(norm_inf(remainder), h**3 + h**4)
            self.assertLessEqual(norm_inf(remainder), 2*h**3)
        self.assertEqual(norm_inf(remainder), 2)

    def test_wrong_scaling_exact_negative_control(self):
        p = nilpotent_euler_holonomy_coefficients(X, Y)
        actual = norm_inf(add(matrix_power(evaluate(p, Fraction(1, 8)), 8), scale(-1, I)))
        bound = identity_error_bound(Fraction(1, 8), 8, 1, 2, 1)
        self.assertLessEqual(actual, bound)
        self.assertEqual(bound, Fraction(5, 27))
        self.assertEqual(1-bound, Fraction(22, 27))

    def test_area_bound_retains_unit_area_and_decreases(self):
        previous = None
        for m in (8, 16, 32):
            h, n = Fraction(1, m), m*m
            self.assertEqual(n*h*h, 1)
            bound = holonomy_error_bound(h, n, 1, 2, 1)
            self.assertGreater(bound, 0)
            if previous is not None:
                self.assertLess(bound, previous)
            previous = bound

    def test_zero_area_and_rational_exponential_majorant(self):
        self.assertEqual(holonomy_error_bound(0, 3, 1, 2, 1), 0)
        self.assertEqual(identity_error_bound(0, 3, 1, 2, 1), 0)
        self.assertEqual(exp_upper_rational(0), 1)
        self.assertEqual(exp_upper_rational(Fraction(5, 32)), Fraction(32, 27))
        self.assertEqual(exp_upper_rational(1), 4)

    def test_invalid_hypotheses_fail_closed(self):
        for args in ((2, 1, 1, 2, 1), (-1, 1, 1, 2, 1),
                     (0, 0, 1, 2, 1), (0, 1, -1, 2, 1),
                     (0, 1, 1, -2, 1), (0, 1, 1, 2, 0),
                     (0, Fraction(1), 1, 2, 1)):
            with self.assertRaises(ValueError):
                holonomy_error_bound(*args)
        with self.assertRaises(TypeError):
            holonomy_error_bound(0.5, 4, 1, 2, 1)
        with self.assertRaises(ValueError):
            nilpotent_euler_holonomy_coefficients(I, X)
        with self.assertRaises(ValueError):
            exp_upper_rational(-1)

    def test_contract_closes_with_separate_evidence_boundary(self):
        result = verify_holonomy_contract()
        self.assertEqual(result["theorem_id"], "MR-07")
        self.assertEqual(result["status"], "RNKE_CONTRACT_VERIFIED", result)
        self.assertEqual(len(result["checks"]), 7)
        self.assertFalse(result["claim_boundary"]["formal_proof_assistant"])


if __name__ == "__main__":
    unittest.main()
