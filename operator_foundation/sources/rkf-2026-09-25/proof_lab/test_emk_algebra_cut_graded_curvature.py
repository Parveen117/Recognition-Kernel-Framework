from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.emk_algebra_cut_graded_curvature import (
    I2,
    K,
    R,
    RK,
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    commutator,
    cut_grade,
    general_closed_form,
    involution_and_grading,
    is_zero,
    matmul,
    negative_controls,
    primitive_relations,
    representative_curvature,
    scale,
)


class EmkAlgebraCutGradedCurvatureTests(unittest.TestCase):
    def test_primitive_relations(self) -> None:
        packet = primitive_relations()
        self.assertTrue(all(packet["checks"].values()))

    def test_K_is_its_own_involution(self) -> None:
        self.assertEqual(matmul(K, K), I2)

    def test_R_squares_to_minus_identity(self) -> None:
        self.assertEqual(matmul(R, R), scale(-1, I2))

    def test_involution_and_grading_matches_EMK2(self) -> None:
        packet = involution_and_grading()
        self.assertTrue(all(packet["checks"].values()))

    def test_cut_grade_of_R_under_K_is_purely_odd(self) -> None:
        even, odd = cut_grade(R, K)
        self.assertTrue(is_zero(even))
        self.assertEqual(odd, R)

    def test_cut_grade_of_K_under_K_is_purely_even(self) -> None:
        even, odd = cut_grade(K, K)
        self.assertTrue(is_zero(odd))
        self.assertEqual(even, K)

    def test_representative_curvature_closed_form(self) -> None:
        packet = representative_curvature()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(commutator(K, R), scale(-2, RK))

    def test_general_closed_form_holds_on_a_new_random_sample(self) -> None:
        # independent spot-check beyond the certificate's own grid
        for a, b, c, d in [
            (Fraction(2), Fraction(-3), Fraction(1, 2), Fraction(5)),
            (Fraction(0), Fraction(7), Fraction(-2), Fraction(-2)),
            (Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4)),
        ]:
            g_e = (a, b)
            g_o = (c, d)
            from proof_lab.emk_algebra_cut_graded_curvature import add, matrix

            G_e = add(scale(a, I2), scale(b, K))
            G_o = add(scale(c, R), scale(d, RK))
            lhs = commutator(G_e, G_o)
            rhs = scale(-2 * b, add(scale(d, R), scale(c, RK)))
            self.assertEqual(lhs, rhs, (g_e, g_o))

    def test_general_closed_form_packet(self) -> None:
        packet = general_closed_form()
        self.assertTrue(all(packet["checks"].values()))
        self.assertGreaterEqual(packet["sampled_points"], 100)
        self.assertEqual(packet["mismatches"], 0)

    def test_negative_controls(self) -> None:
        packet = negative_controls()
        self.assertTrue(all(packet["checks"].values()))

    def test_zero_odd_gives_zero_curvature(self) -> None:
        from proof_lab.emk_algebra_cut_graded_curvature import zero

        self.assertEqual(commutator(K, zero(2, 2)), zero(2, 2))

    def test_certificate_is_deterministic_and_passes(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        self.assertEqual(
            first["status"],
            "PASS_EMK_ALGEBRA_CUT_GRADED_CURVATURE_CANDIDATE",
        )
        self.assertTrue(all(first["checks"].values()))
        expected_path = Path(__file__).with_name(
            "EMK_ALGEBRA_CUT_GRADED_CURVATURE_EXPECTED.sha256"
        )
        expected = expected_path.read_text(encoding="ascii").strip()
        self.assertEqual(certificate_sha256(first), expected)
        self.assertEqual(
            hashlib.sha256(canonical_bytes(first)).hexdigest(),
            expected,
        )


if __name__ == "__main__":
    unittest.main()
