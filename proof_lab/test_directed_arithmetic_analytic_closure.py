import unittest
from fractions import Fraction

from proof_lab.directed_arithmetic_analytic_closure import (
    Ball,
    STATUS,
    build_certificate,
    fraction_from_decimal_token,
    promote_upper,
)


class DirectedArithmeticAnalyticClosureTests(unittest.TestCase):
    def test_decimal_tokens_are_exact(self):
        self.assertEqual(fraction_from_decimal_token("0.1"), Fraction(1, 10))
        self.assertEqual(fraction_from_decimal_token("0.7"), Fraction(7, 10))
        self.assertEqual(fraction_from_decimal_token("0.8"), Fraction(4, 5))
        self.assertEqual(
            fraction_from_decimal_token("0.1") + fraction_from_decimal_token("0.7"),
            fraction_from_decimal_token("0.8"),
        )

    def test_scientific_notation_is_exact(self):
        self.assertEqual(fraction_from_decimal_token("-12.3400e-3"), Fraction(-617, 50000))

    def test_zero_radius_ball_is_exact_embedding(self):
        q = Fraction(17, 23)
        self.assertTrue(Ball(q, Fraction(0)).contains(q))

    def test_negative_radius_rejected(self):
        with self.assertRaises(ValueError):
            Ball(Fraction(0), Fraction(-1, 10))

    def test_strict_threshold_pass(self):
        self.assertEqual(
            promote_upper(Fraction(7, 10), Fraction(1, 100), Fraction(1, 100), Fraction(4, 5)),
            "PASS",
        )

    def test_exact_threshold_is_boundary(self):
        self.assertEqual(
            promote_upper(Fraction(7, 10), Fraction(1, 20), Fraction(1, 20), Fraction(4, 5)),
            "BOUNDARY",
        )

    def test_outward_threshold_failure(self):
        self.assertEqual(
            promote_upper(Fraction(3, 4), Fraction(1, 20), Fraction(1, 100), Fraction(4, 5)),
            "FAIL",
        )

    def test_independent_balls_must_overlap_for_same_target(self):
        a = Ball(Fraction(1, 2), Fraction(1, 100))
        b = Ball(Fraction(101, 200), Fraction(1, 100))
        self.assertTrue(a.overlaps(b))

    def test_disjoint_ball_negative_control(self):
        a = Ball(Fraction(1, 2), Fraction(1, 1000))
        b = Ball(Fraction(51, 100), Fraction(1, 1000))
        self.assertFalse(a.overlaps(b))

    def test_three_ledger_refinement_identity(self):
        F = Fraction(1)
        M0, H0 = Fraction(3, 5), Fraction(59, 100)
        M1, H1 = Fraction(4, 5), Fraction(79, 100)
        A0, A1 = M0 - H0, M1 - H1
        T0, T1 = F - M0, F - M1
        self.assertEqual((H1 - H0) + (A1 - A0) + (T1 - T0), 0)

    def test_certificate_passes(self):
        result = build_certificate()
        self.assertEqual(result["status"], STATUS)
        self.assertTrue(all(result["checks"].values()))


if __name__ == "__main__":
    unittest.main()
