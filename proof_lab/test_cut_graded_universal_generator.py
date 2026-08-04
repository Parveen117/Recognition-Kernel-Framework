from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.cut_graded_universal_generator import (
    add,
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    closure_sign,
    cut_decomposition,
    cut_loop_series,
    diagonal,
    eye_sectors,
    identity,
    involution_projectors,
    is_zero,
    matmul,
    matrix,
    nilpotent_odd_flow,
    run_bilateral_flow_fixture,
    run_closure_spectrum_fixture,
    run_component_observer_fixture,
    run_cut_decomposition_fixture,
    run_cut_loop_fixture,
    run_eye_fixture,
    scale,
    sub,
)


class CutGradedUniversalGeneratorTests(unittest.TestCase):
    def test_unique_cut_even_odd_decomposition(self) -> None:
        packet = run_cut_decomposition_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_cut_block_support_is_typed(self) -> None:
        j = diagonal((1, 1, -1, -1))
        g = matrix(
            (
                (1, 0, 1, 0),
                (0, 2, 0, 1),
                (3, 0, -1, 0),
                (0, 4, 0, 1),
            )
        )
        g_even, g_odd = cut_decomposition(g, j)
        p_plus, p_minus = involution_projectors(j)
        self.assertTrue(is_zero(matmul(matmul(p_plus, g_even), p_minus)))
        self.assertTrue(is_zero(matmul(matmul(p_minus, g_even), p_plus)))
        self.assertTrue(is_zero(matmul(matmul(p_plus, g_odd), p_plus)))
        self.assertTrue(is_zero(matmul(matmul(p_minus, g_odd), p_minus)))
        self.assertEqual(add(g_even, g_odd), g)

    def test_cut_loop_extracts_memory_and_seam_curvature(self) -> None:
        packet = run_cut_loop_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_cut_loop_identity_forces_zero_even_part_at_first_order(self) -> None:
        j = diagonal((1, -1))
        g_odd = matrix(((0, 1), (0, 0)))
        loop = cut_loop_series(g_odd, j, order=2)
        self.assertEqual(loop[0], identity(2))
        self.assertTrue(is_zero(loop[1]))
        self.assertTrue(is_zero(loop[2]))

        g_with_memory = add(g_odd, diagonal((1, 0)))
        memory_loop = cut_loop_series(g_with_memory, j, order=2)
        self.assertFalse(is_zero(memory_loop[1]))

    def test_bilateral_exponential_cut_square(self) -> None:
        packet = run_bilateral_flow_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_derived_cut_join_products_are_equal(self) -> None:
        g_odd = matrix(((0, 1), (0, 0)))
        flow = nilpotent_odd_flow(g_odd, Fraction(5, 3))
        self.assertEqual(
            matmul(flow["join"], flow["cut"]),
            matmul(flow["cut"], flow["join"]),
        )
        self.assertEqual(
            sub(matmul(flow["join"], flow["join"]), matmul(flow["cut"], flow["cut"])),
            scale(4, identity(2)),
        )

    def test_periodic_and_antiperiodic_closure_are_distinguished(self) -> None:
        packet = run_closure_spectrum_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(closure_sign(Fraction(1, 2), 8), 1)
        self.assertEqual(closure_sign(Fraction(1, 8), 8), -1)
        self.assertIsNone(closure_sign(Fraction(1, 3), 8))

    def test_clock_free_eye_removes_stroboscopic_blindness(self) -> None:
        packet = run_eye_fixture()
        self.assertTrue(all(packet["checks"].values()))
        sectors = eye_sectors((Fraction(0), Fraction(1), Fraction(-1), Fraction(1, 2)))
        self.assertEqual(sectors["single_step_fixed"], (0, 1, 2))
        self.assertEqual(sectors["all_time_fixed"], (0,))
        self.assertEqual(sectors["stroboscopic_blind"], (1, 2))

    def test_component_observer_negative_control(self) -> None:
        packet = run_component_observer_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["negative_control_direct_energy"], "10")

    def test_certificate_is_deterministic_and_passes(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        self.assertEqual(
            first["status"],
            "PASS_CUT_GRADED_UNIVERSAL_GENERATOR_CANDIDATE",
        )
        self.assertTrue(all(first["checks"].values()))
        expected_path = Path(__file__).with_name(
            "CUT_GRADED_UNIVERSAL_GENERATOR_EXPECTED.sha256"
        )
        expected = expected_path.read_text(encoding="ascii").strip()
        self.assertEqual(certificate_sha256(first), expected)
        self.assertEqual(
            hashlib.sha256(canonical_bytes(first)).hexdigest(),
            expected,
        )


if __name__ == "__main__":
    unittest.main()
