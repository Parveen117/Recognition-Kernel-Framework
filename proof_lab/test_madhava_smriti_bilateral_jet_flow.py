from __future__ import annotations

import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.madhava_smriti_bilateral_jet_flow import (
    build_certificate,
    canonical_fixture,
    certificate_sha256,
    classify_madhava_smriti,
    correction_window,
    is_zero,
    power,
    run_bilateral_smriti_fixture,
    run_correction_smriti_gauge_fixture,
    run_fail_closed_fixture,
    run_madhava_refinement_fixture,
    run_refinement_cocycle_fixture,
)


class MadhavaSmritiBilateralJetFlowTests(unittest.TestCase):
    def test_madhava_refinement_and_tail_transfer(self) -> None:
        packet = run_madhava_refinement_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["tail_energy"][-1], "0")
        self.assertNotEqual(packet["tail_energy"][0], "0")

    def test_bilateral_smriti_and_parity(self) -> None:
        packet = run_bilateral_smriti_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertNotEqual(packet["wrong_cut_defect"], [["0"] * 5])

    def test_refinement_cocycle(self) -> None:
        packet = run_refinement_cocycle_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["direct_seam"], [["0"] * 5])
        self.assertNotEqual(packet["corrupt_seam"], [["0"] * 5])

    def test_correction_smriti_gauge(self) -> None:
        packet = run_correction_smriti_gauge_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["coupled_defect"], [["0"] * 5])
        self.assertEqual(packet["uncoupled_defect"], packet["gauge"])

    def test_fail_closed_states(self) -> None:
        packet = run_fail_closed_fixture()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(
            classify_madhava_smriti(
                closure_zero=True,
                bilateral_zero=True,
                tail_typed=True,
                tail_zero=False,
                burden=Fraction(1, 4),
            ),
            "MEMORY_CLOSED",
        )

    def test_nilpotent_fixture_and_empty_correction(self) -> None:
        _, g, observer = canonical_fixture()
        self.assertTrue(is_zero(power(g, 5)))
        self.assertEqual(
            correction_window(observer, g, Fraction(2, 3), 1, 0),
            ((Fraction(0),) * 5,),
        )

    def test_certificate_is_deterministic_and_hash_stable(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        self.assertEqual(
            first["status"],
            "PASS_MADHAVA_SMRITI_BILATERAL_JET_FLOW_CLOSURE_CANDIDATE",
        )
        expected = (
            Path(__file__)
            .with_name("MADHAVA_SMRITI_BILATERAL_JET_FLOW_EXPECTED.sha256")
            .read_text(encoding="utf-8")
            .strip()
        )
        self.assertEqual(certificate_sha256(first), expected)


if __name__ == "__main__":
    unittest.main()
