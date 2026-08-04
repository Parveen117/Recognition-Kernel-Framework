from __future__ import annotations

from pathlib import Path
import unittest

from proof_lab.native_weil_cut_event_cogeneration import (
    build_certificate,
    canonical_hash,
    run_fail_closed_rh_contract,
    run_finite_cogeneration,
    run_refinement_orientation_gate,
    run_shift_refinement_identity,
    run_t21_scalar_ledger,
)


class NativeWeilCutEventCogenerationTests(unittest.TestCase):
    def test_finite_cogeneration(self) -> None:
        packet = run_finite_cogeneration()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["decoder_burden"], "3/4")
        self.assertEqual(
            packet["cut_covariance"],
            [["4", "0"], ["0", "4"]],
        )

    def test_shift_refinement(self) -> None:
        packet = run_shift_refinement_identity()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(packet["beta_zero"], "3/4")

    def test_orientation_gate(self) -> None:
        packet = run_refinement_orientation_gate()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(
            packet["coherent"]["burden"],
            packet["opposite_orientation"]["burden"],
        )
        self.assertNotEqual(
            packet["coherent"]["boundary"],
            packet["opposite_orientation"]["boundary"],
        )

    def test_t21_scalar_ledger(self) -> None:
        packet = run_t21_scalar_ledger()
        self.assertTrue(all(packet["checks"].values()))
        self.assertEqual(
            packet["reported_beta_zero_upper"],
            "0.8290856201657449",
        )
        self.assertEqual(
            packet["threshold_reserve_lower"],
            "0.1709143798342551",
        )

    def test_rh_contract_fails_closed(self) -> None:
        packet = run_fail_closed_rh_contract()
        self.assertTrue(all(packet["checks"].values()))
        self.assertFalse(packet["terminal_promotion_allowed"])
        self.assertEqual(
            packet["status"],
            "OPEN_NATIVE_WEIL_EVENT_ORIENTATION",
        )

    def test_combined(self) -> None:
        packet = build_certificate()
        self.assertEqual(
            packet["status"],
            "PASS_NATIVE_WEIL_CUT_EVENT_COGENERATION_STAGE3A",
        )
        self.assertTrue(all(packet["checks"].values()))

    def test_expected_hash(self) -> None:
        expected = Path(__file__).with_name(
            "NATIVE_WEIL_CUT_EVENT_COGENERATION_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        self.assertEqual(expected, canonical_hash())


if __name__ == "__main__":
    unittest.main()
