import unittest
from fractions import Fraction

from proof_lab.first_visible_jet_seam_quotient import (
    RawDivisionByZero,
    STATUS,
    build_certificate,
    classify_finite_jets,
    first_visible_order,
    quotient_enclosure_radius,
    quotient_interval,
    raw_divide,
    reparameterized_leading,
)


class FirstVisibleJetSeamQuotientTests(unittest.TestCase):
    def test_raw_one_over_zero_rejected(self):
        with self.assertRaises(RawDivisionByZero):
            raw_divide(Fraction(1), Fraction(0))

    def test_raw_zero_over_zero_rejected(self):
        with self.assertRaises(RawDivisionByZero):
            raw_divide(Fraction(0), Fraction(0))

    def test_first_visible_order(self):
        self.assertEqual(first_visible_order([0, 0, Fraction(3, 7)]), 2)
        self.assertIsNone(first_visible_order([0, 0, 0]))

    def test_equal_order_seam_quotient(self):
        result = classify_finite_jets([0, 0, 2], [0, 0, 4])
        self.assertEqual(result.status, "FINITE_SEAM_QUOTIENT")
        self.assertEqual(result.quotient, Fraction(1, 2))

    def test_numerator_higher_order_tends_to_zero(self):
        result = classify_finite_jets([0, 0, 3], [0, 5])
        self.assertEqual(result.status, "FINITE_QUOTIENT_ZERO")
        self.assertEqual(result.quotient, 0)

    def test_denominator_higher_order_diverges(self):
        result = classify_finite_jets([0, 3], [0, 0, 5])
        self.assertEqual(result.status, "DIVERGENT_NO_FINITE_QUOTIENT")
        self.assertIsNone(result.quotient)

    def test_flat_finite_jets_are_incomplete(self):
        result = classify_finite_jets([0, 0, 0], [0, 0, 0])
        self.assertEqual(result.status, "INCOMPLETE_FLAT_OR_UNRESOLVED")

    def test_flat_denominator_is_incomplete_even_if_numerator_visible(self):
        result = classify_finite_jets([0, 1], [0, 0, 0])
        self.assertEqual(result.status, "INCOMPLETE_FLAT_OR_UNRESOLVED")

    def test_regular_reparameterization_preserves_ratio(self):
        a, b, r, c = Fraction(7, 3), Fraction(5, 2), 3, Fraction(-4, 3)
        ap = reparameterized_leading(a, r, c)
        bp = reparameterized_leading(b, r, c)
        self.assertEqual(ap / bp, a / b)

    def test_singular_reparameterization_rejected(self):
        with self.assertRaises(ValueError):
            reparameterized_leading(Fraction(1), 2, Fraction(0))

    def test_denominator_separation_is_required(self):
        with self.assertRaises(ValueError):
            quotient_enclosure_radius(
                Fraction(1), Fraction(1, 100), Fraction(0), Fraction(1, 100)
            )

    def test_negative_remainder_rejected(self):
        with self.assertRaises(ValueError):
            quotient_enclosure_radius(
                Fraction(1), Fraction(2), Fraction(-1, 100), Fraction(0)
            )

    def test_exact_quotient_enclosure_radius(self):
        radius = quotient_enclosure_radius(
            Fraction(3, 2),
            Fraction(2),
            Fraction(1, 100),
            Fraction(1, 50),
        )
        self.assertEqual(radius, Fraction(5, 396))

    def test_quotient_interval_contains_leading_ratio(self):
        lo, hi = quotient_interval(
            Fraction(3, 2),
            Fraction(2),
            Fraction(1, 100),
            Fraction(1, 50),
        )
        self.assertEqual(lo, Fraction(73, 99))
        self.assertEqual(hi, Fraction(151, 198))
        self.assertLessEqual(lo, Fraction(3, 4))
        self.assertLessEqual(Fraction(3, 4), hi)

    def test_exact_cancellation_example(self):
        result = classify_finite_jets([0, 0, Fraction(-9, 5)], [0, 0, Fraction(6, 7)])
        self.assertEqual(result.quotient, Fraction(-21, 10))

    def test_certificate_passes(self):
        result = build_certificate()
        self.assertEqual(result["status"], STATUS)
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["pinned_examples"]["quotient_radius"], "5/396")


if __name__ == "__main__":
    unittest.main()
