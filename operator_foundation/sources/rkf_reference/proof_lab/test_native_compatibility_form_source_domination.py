from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import unittest

from proof_lab.native_compatibility_form_source_domination import (
    build_certificate,
    canonical_bytes,
    run_actual_form_attachment_gate,
    run_cellwise_cut_profile,
    run_form_range_nonattained_model,
    run_recognition_class_representatives,
    run_t21_attachment_audit,
    run_two_sheet_loewner_symbol,
)


class Stage3FTests(unittest.TestCase):
    def test_form_range_nonattained_model(self) -> None:
        result = run_form_range_nonattained_model()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["decoder_burden_limit"], "1/4")
        self.assertEqual(result["formal_source_inverse_prefix_energy"], "32/25")

    def test_two_sheet_loewner_symbol(self) -> None:
        result = run_two_sheet_loewner_symbol()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["total_burden"], "419/7200")

    def test_recognition_class_representatives(self) -> None:
        result = run_recognition_class_representatives()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["minimum_class_burden"], "2/3")

    def test_cellwise_cut_profile(self) -> None:
        result = run_cellwise_cut_profile()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["beta_upper"], "41/400")

    def test_t21_attachment_audit(self) -> None:
        result = run_t21_attachment_audit()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["reported_beta_upper"], "0.8290856201657449")
        self.assertEqual(result["relative_reserve"], "0.1709143798342551")

    def test_actual_form_attachment_gate(self) -> None:
        result = run_actual_form_attachment_gate()
        self.assertTrue(all(result["checks"].values()))
        self.assertTrue(result["actual_form_range_transfer"])
        self.assertTrue(result["actual_source_domination"])
        self.assertTrue(result["actual_decoder_bound"])
        self.assertTrue(result["actual_cut_covariance"])
        self.assertFalse(result["actual_strict_odd_positivity"])
        self.assertFalse(result["ambient_compatibility_range_required"])

    def test_combined_certificate(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_STAGE3F",
        )
        self.assertTrue(all(result["checks"].values()))

    def test_canonical_hash_fixture(self) -> None:
        expected = Path(
            "proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        actual = sha256(canonical_bytes(build_certificate())).hexdigest()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
