from __future__ import annotations

import hashlib
from pathlib import Path
import unittest

from proof_lab.cut_covariance_event_realization import (
    build_certificate,
    canonical_bytes,
    run_co_generated_packet,
    run_critical_burden_sequence,
    run_imported_boundary_negative_control,
    run_moment_transfer,
    run_target_observer_packet,
)


class CutCovarianceEventRealizationTests(unittest.TestCase):
    def test_co_generated_first_second_moments(self) -> None:
        result = run_co_generated_packet()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["least_energy_decoder_burden"], "1/6")
        self.assertEqual(result["memory_rank"], 5)

    def test_critical_burden_sequence(self) -> None:
        result = run_critical_burden_sequence()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["rows"][-1]["decoder_burden"], "10/11")
        self.assertEqual(
            result["rows"][-1]["minimum_cut_covariance_eigenvalue"],
            "1/100",
        )

    def test_target_observer(self) -> None:
        result = run_target_observer_packet()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["correct_observer_action"], "0")
        self.assertEqual(result["wrong_rank_five_action"], "81/100")

    def test_imported_boundary_negative_control(self) -> None:
        result = run_imported_boundary_negative_control()
        self.assertTrue(all(result["checks"].values()))
        self.assertNotEqual(
            result["covariance_mismatch_frobenius_square"], "0"
        )

    def test_moment_transfer(self) -> None:
        result = run_moment_transfer()
        self.assertTrue(all(result["checks"].values()))

    def test_combined_certificate(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_CUT_COVARIANCE_EVENT_REALIZATION_V0_1",
        )
        self.assertTrue(all(result["checks"].values()))

    def test_expected_certificate_hash_is_stable(self) -> None:
        expected_hash = Path(__file__).with_name(
            "CUT_COVARIANCE_EVENT_REALIZATION_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        actual_hash = hashlib.sha256(canonical_bytes()).hexdigest()
        self.assertEqual(expected_hash, actual_hash)


if __name__ == "__main__":
    unittest.main()
