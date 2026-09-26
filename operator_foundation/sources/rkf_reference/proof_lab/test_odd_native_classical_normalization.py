from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import unittest

from proof_lab import odd_native_classical_normalization as stage


class Stage3HTests(unittest.TestCase):
    def test_correlation_interface(self) -> None:
        result = stage.run_correlation_interface()
        self.assertTrue(all(result["checks"].values()))

    def test_termwise_explicit_formula_interface(self) -> None:
        result = stage.run_termwise_explicit_formula_interface()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["native_completed_form"], result["explicit_distribution_side"])

    def test_odd_boundary_reduction(self) -> None:
        result = stage.run_odd_boundary_reduction()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["cross_boundary"], result["cross_negative_rank_one"])

    def test_log_mellin_unitary_interface(self) -> None:
        result = stage.run_log_mellin_unitary_interface()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["multiplicative_completed_form"], result["logarithmic_completed_form"])

    def test_fourier_reflection_hermitian(self) -> None:
        result = stage.run_fourier_sign_reflection_hermitian()
        self.assertTrue(all(result["checks"].values()))

    def test_core_density(self) -> None:
        result = stage.run_core_density_calibration()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["completed_weighted_norm"], "2/7")

    def test_actual_normalization_gate(self) -> None:
        result = stage.build_certificate()
        gate = result["actual_normalization_gate"]
        self.assertEqual(result["status"], "PASS_ODD_NATIVE_CLASSICAL_NORMALIZATION_STAGE3H")
        self.assertTrue(gate["actual_odd_native_classical_interface"])
        self.assertFalse(gate["classical_zero_sum_rederived"])
        self.assertFalse(gate["odd_weil_implication_consumed"])
        self.assertFalse(gate["rh_promotion_allowed"])

    def test_stage3g_payload_validator(self) -> None:
        payload = {
            "status": stage.STAGE3G_STATUS,
            "actual_strict_odd_gate": {
                "stage3f_hash_verified": True,
                "actual_source_kernel_injectivity": True,
                "actual_xi0_injectivity": True,
                "actual_strict_odd_positivity": True,
                "actual_cut_covariance_injectivity": True,
                "actual_odd_classical_interface": False,
                "rh_promotion_allowed": False,
            },
        }
        self.assertTrue(stage.validate_stage3g_payload(payload))
        payload["actual_strict_odd_gate"]["actual_strict_odd_positivity"] = False
        self.assertFalse(stage.validate_stage3g_payload(payload))

    def test_wrong_stage3g_hash_fails_closed(self) -> None:
        result = stage.build_certificate(stage3g_hash="0" * 64)
        self.assertEqual(result["status"], "FAIL_ODD_NATIVE_CLASSICAL_NORMALIZATION_STAGE3H")
        self.assertFalse(result["actual_normalization_gate"]["stage3g_hash_verified"])

    def test_canonical_hash_fixture(self) -> None:
        expected = Path(
            "proof_lab/ODD_NATIVE_CLASSICAL_NORMALIZATION_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        actual = sha256(stage.canonical_bytes(stage.build_certificate())).hexdigest()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
