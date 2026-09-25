from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import unittest

from proof_lab.native_source_kernel_no_blindness import (
    EXPECTED_STAGE3F_HASH,
    build_certificate,
    canonical_bytes,
    run_actual_strict_odd_gate,
    run_insufficient_active_observer_control,
    run_noncoercive_strictness,
    run_zero_cut_odd_uniqueness,
)


class Stage3GTests(unittest.TestCase):
    def test_zero_cut_odd_uniqueness(self) -> None:
        result = run_zero_cut_odd_uniqueness()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["active_determinant"], "720")
        self.assertEqual(result["source_determinant"], "518400")
        self.assertEqual(result["decoder_burden"], "61/144")
        self.assertEqual(result["relative_reserve"], "83/144")
        self.assertEqual(result["cut_covariance_determinant"], "298800")

    def test_insufficient_active_observer_control(self) -> None:
        result = run_insufficient_active_observer_control()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["blind_coefficients"], ["4", "-5", "1"])
        self.assertEqual(result["third_active_detection"], "120")

    def test_noncoercive_strictness(self) -> None:
        result = run_noncoercive_strictness()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["relative_reserve"], "1/5")
        self.assertEqual(result["minimum_source_prefix"], "1/12")
        self.assertEqual(result["minimum_strict_prefix"], "1/60")

    def test_actual_gate_closes_with_verified_stage3f(self) -> None:
        result = run_actual_strict_odd_gate(
            stage3f_hash=EXPECTED_STAGE3F_HASH,
            stage3f_payload_valid=True,
        )
        self.assertTrue(all(result["checks"].values()))
        self.assertTrue(result["actual_source_kernel_injectivity"])
        self.assertTrue(result["actual_xi0_injectivity"])
        self.assertTrue(result["actual_strict_odd_positivity"])
        self.assertFalse(result["actual_odd_classical_interface"])
        self.assertFalse(result["rh_promotion_allowed"])
        self.assertEqual(result["relative_source_reserve"], "0.1709143798342551")

    def test_wrong_stage3f_hash_fails_closed(self) -> None:
        result = run_actual_strict_odd_gate(
            stage3f_hash="0" * 64,
            stage3f_payload_valid=True,
        )
        self.assertFalse(result["stage3f_hash_verified"])
        self.assertFalse(result["actual_source_kernel_injectivity"])
        self.assertFalse(result["actual_strict_odd_positivity"])

    def test_invalid_stage3f_payload_fails_closed(self) -> None:
        result = run_actual_strict_odd_gate(
            stage3f_hash=EXPECTED_STAGE3F_HASH,
            stage3f_payload_valid=False,
        )
        self.assertFalse(result["actual_source_kernel_injectivity"])
        self.assertFalse(result["actual_strict_odd_positivity"])

    def test_combined_certificate(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_NATIVE_SOURCE_KERNEL_NO_BLINDNESS_STAGE3G",
        )
        self.assertTrue(all(result["checks"].values()))

    def test_canonical_hash_fixture(self) -> None:
        expected = Path(
            "proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        actual = sha256(canonical_bytes(build_certificate())).hexdigest()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
