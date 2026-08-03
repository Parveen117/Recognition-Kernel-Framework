from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import unittest

from proof_lab.native_two_sheet_compatibility_attachment import (
    build_certificate,
    canonical_bytes,
    run_actual_attachment_gate,
    run_compatibility_transfer,
    run_robust_t21_budget,
    run_strip_boundary_kernel,
    run_zero_cut_support_gate,
)


class NativeTwoSheetCompatibilityAttachmentTests(unittest.TestCase):
    def test_strip_boundary_kernel(self) -> None:
        result = run_strip_boundary_kernel()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["evaluation_kernel_mass"], "3/4")

    def test_compatibility_transfer(self) -> None:
        result = run_compatibility_transfer()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["actual_source_burden"], "397/5184")

    def test_zero_cut_support(self) -> None:
        result = run_zero_cut_support_gate()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["support_burden"], "97/1296")

    def test_robust_t21_budget(self) -> None:
        result = run_robust_t21_budget()
        self.assertTrue(all(result["checks"].values()))

    def test_actual_boundary_attachment_closed(self) -> None:
        result = run_actual_attachment_gate()
        self.assertTrue(all(result["checks"].values()))
        self.assertTrue(result["actual_two_sheet_boundary_attachment"])
        self.assertFalse(result["actual_compatibility_transfer"])
        self.assertFalse(result["actual_source_domination"])
        self.assertFalse(result["actual_decoder_bound"])

    def test_combined_status(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_STAGE3E",
        )
        self.assertTrue(all(result["checks"].values()))

    def test_canonical_hash_fixture(self) -> None:
        expected_path = Path(__file__).with_name(
            "NATIVE_TWO_SHEET_COMPATIBILITY_ATTACHMENT_EXPECTED.sha256"
        )
        expected = expected_path.read_text(encoding="ascii").strip()
        actual = sha256(canonical_bytes(build_certificate())).hexdigest()
        self.assertEqual(actual, expected)

    def test_negative_kernel_boundary_is_not_promoted(self) -> None:
        result = run_zero_cut_support_gate()
        self.assertTrue(result["checks"]["kernel_boundary_is_rejected"])


if __name__ == "__main__":
    unittest.main()
