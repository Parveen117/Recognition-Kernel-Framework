from __future__ import annotations

from pathlib import Path
import unittest

from proof_lab.native_prime_gamma_debt_source_adapter import (
    build_certificate,
    canonical_bytes,
    run_actual_weil_stage_gate,
    run_canonical_graph_adapter,
    run_decoder_and_cut_covariance,
    run_event_coordinate_covariance,
    run_null_seam_adapter_family,
    run_prime_gamma_debt_packet,
    run_robust_two_sheet_attachment_budget,
)


class NativePrimeGammaDebtSourceAdapterTests(unittest.TestCase):
    def test_prime_gamma_debt_packet(self) -> None:
        result = run_prime_gamma_debt_packet()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["diagonal_debt"], "144")
        self.assertEqual(result["source_gram"][0][0], "25")
        self.assertEqual(result["source_gram"][1][1], "81")
        self.assertEqual(result["source_gram"][2][2], "256")

    def test_canonical_graph_adapter(self) -> None:
        result = run_canonical_graph_adapter()
        self.assertTrue(all(result["checks"].values()))

    def test_null_seam_adapter_family(self) -> None:
        result = run_null_seam_adapter_family()
        self.assertTrue(all(result["checks"].values()))
        self.assertNotEqual(result["ambient_difference_energy"], "0")

    def test_decoder_and_cut_covariance(self) -> None:
        result = run_decoder_and_cut_covariance()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["decoder_burden"], "361/900")
        self.assertEqual(result["relative_reserve"], "539/900")

    def test_event_coordinate_covariance(self) -> None:
        result = run_event_coordinate_covariance()
        self.assertTrue(all(result["checks"].values()))

    def test_robust_two_sheet_attachment_budget(self) -> None:
        result = run_robust_two_sheet_attachment_budget()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["relative_reserve"], "0.1709143798342551")

    def test_actual_weil_gate(self) -> None:
        result = run_actual_weil_stage_gate()
        self.assertTrue(all(result["checks"].values()))
        self.assertTrue(result["actual_source_adapter"])
        self.assertFalse(result["actual_decoder_bound"])

    def test_combined_certificate(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_STAGE3D",
        )
        self.assertTrue(all(result["checks"].values()))

    def test_expected_certificate_hash(self) -> None:
        expected = Path(__file__).with_name(
            "NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        from hashlib import sha256

        self.assertEqual(expected, sha256(canonical_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
