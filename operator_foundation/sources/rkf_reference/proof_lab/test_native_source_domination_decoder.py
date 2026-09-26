from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import unittest

from proof_lab.native_source_domination_decoder import (
    build_certificate,
    canonical_bytes,
    run_cut_cell_envelope,
    run_exact_source_domination,
    run_first_cut_cancellation,
    run_matrix_symbol_floor,
    run_negative_controls,
    run_t21_source_domination_audit,
)


class NativeSourceDominationDecoderTests(unittest.TestCase):
    def test_exact_source_domination(self) -> None:
        result = run_exact_source_domination()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["source_envelope"], "25/36")
        self.assertEqual(result["sharp_burden"], "13/36")
        self.assertEqual(result["canonical_decoder_energy"], "13/36")

    def test_matrix_symbol_floor(self) -> None:
        result = run_matrix_symbol_floor()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["matrix_burden"], "2/3")
        self.assertEqual(result["scalar_floor_envelope"], "1")

    def test_cut_cell_envelope(self) -> None:
        result = run_cut_cell_envelope()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["beta_envelope"], "4591/27000")

    def test_first_cut_cancellation(self) -> None:
        result = run_first_cut_cancellation()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["first_cut_upper"], "1/13050")

    def test_t21_audit_fails_closed_on_common_chart(self) -> None:
        result = run_t21_source_domination_audit()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["reported_beta_upper"], "0.8290856201657449")
        self.assertFalse(result["actual_weil_promotion_allowed"])
        self.assertFalse(
            result["contract"]["exact_boundary_pairing_in_same_chart_displayed"]
        )

    def test_negative_controls(self) -> None:
        result = run_negative_controls()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["source_energy_on_blind_vector"], "0")
        self.assertEqual(result["boundary_value_on_blind_vector"], "1")

    def test_combined_and_hash(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_NATIVE_SOURCE_DOMINATION_DECODER_STAGE3B",
        )
        self.assertTrue(all(result["checks"].values()))
        expected = Path(__file__).with_name(
            "NATIVE_SOURCE_DOMINATION_DECODER_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        self.assertEqual(expected, sha256(canonical_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
