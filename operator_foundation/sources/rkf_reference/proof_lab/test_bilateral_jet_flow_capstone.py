from __future__ import annotations

import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.bilateral_jet_flow_capstone import (
    build_certificate,
    canonical_fixture,
    certificate_sha256,
    classify_capstone,
    finite_jet_observer,
    jet_layers,
    jet_reconstruction,
    nilpotent_exponential,
    run_bilateral_flow_fixture,
    run_curvature_response_fixture,
    run_fail_closed_fixture,
    run_jet_reconstruction_fixture,
    run_recognition_repair_fixture,
)
from proof_lab.cut_graded_universal_generator import (
    add,
    identity,
    is_zero,
    matmul,
    scale,
    sub,
)


class BilateralJetFlowCapstoneTests(unittest.TestCase):
    def test_bilateral_flow_and_cut_square(self) -> None:
        packet = run_bilateral_flow_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_wrong_cut_negative_control(self) -> None:
        packet = run_bilateral_flow_fixture()
        self.assertNotEqual(
            packet["wrong_cut_defect"],
            [["0"] * 4 for _ in range(4)],
        )

    def test_jet_parity_and_exact_reconstruction(self) -> None:
        packet = run_jet_reconstruction_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(
            packet["third_order_remainder"],
            [["0", "0", "0", "0"]],
        )
        self.assertNotEqual(
            packet["second_order_remainder"],
            [["0", "0", "0", "0"]],
        )

    def test_direct_fixture_reconstruction(self) -> None:
        _, g, observer = canonical_fixture()
        t = Fraction(2, 3)
        u = nilpotent_exponential(g, t, 4)
        reconstructed = jet_reconstruction(observer, g, t, 3)
        self.assertEqual(reconstructed, matmul(observer, u))
        self.assertEqual(len(jet_layers(observer, g, 3)), 4)

    def test_observer_kernel_monotonicity_and_target_repair(self) -> None:
        packet = run_recognition_repair_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["ranks"], [1, 2, 3, 4])
        self.assertEqual(packet["classification"], "HIGHER_LAYER_REPAIR")

    def test_full_jet_observer_is_identity(self) -> None:
        _, g, observer = canonical_fixture()
        self.assertEqual(
            finite_jet_observer(observer, g, 3),
            identity(4),
        )

    def test_curvature_is_consumed_by_observer(self) -> None:
        packet = run_curvature_response_fixture()
        self.assertTrue(all(packet["checks"].values()))

    def test_fail_closed_classification(self) -> None:
        packet = run_fail_closed_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(
            classify_capstone(
                closure_defect_zero=False,
                target_blind=False,
                repaired_by_higher_layer=False,
                burden=Fraction(1, 4),
            ),
            "OPEN_SEAM",
        )

    def test_exact_cut_square_directly(self) -> None:
        _, g, _ = canonical_fixture()
        t = Fraction(5, 7)
        up = nilpotent_exponential(g, t, 4)
        um = nilpotent_exponential(g, -t, 4)
        join = add(up, um)
        cut = sub(up, um)
        self.assertEqual(
            sub(matmul(join, join), matmul(cut, cut)),
            scale(4, identity(4)),
        )
        self.assertTrue(
            is_zero(sub(matmul(join, cut), matmul(cut, join)))
        )

    def test_certificate_is_deterministic_and_passing(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        self.assertEqual(
            first["status"],
            "PASS_BILATERAL_JET_FLOW_CAPSTONE_CANDIDATE",
        )
        actual = certificate_sha256(first)
        self.assertEqual(actual, certificate_sha256(second))
        expected = (
            Path(__file__)
            .with_name("BILATERAL_JET_FLOW_CAPSTONE_EXPECTED.sha256")
            .read_text(encoding="utf-8")
            .strip()
        )
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
