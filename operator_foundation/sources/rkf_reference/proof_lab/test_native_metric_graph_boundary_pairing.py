from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import unittest

from proof_lab.native_metric_graph_boundary_pairing import (
    build_certificate,
    canonical_bytes,
    run_actual_weil_adapter_gate,
    run_boundary_jet_audit,
    run_metric_graph_pairing,
    run_negative_controls,
    run_recognition_quotient_adapter,
    run_reflection_odd_pairing,
)


class NativeMetricGraphBoundaryPairingTests(unittest.TestCase):
    def test_metric_graph_pairing(self) -> None:
        result = run_metric_graph_pairing()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["graph_boundary_energy"], "7/20")
        self.assertEqual(result["source_decoder_energy"], "7/80")

    def test_reflection_odd_pairing(self) -> None:
        result = run_reflection_odd_pairing()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["odd_graph_energy"], "1/40")

    def test_recognition_quotient_adapter(self) -> None:
        result = run_recognition_quotient_adapter()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["sharp_burden"], "2/3")
        self.assertNotEqual(
            result["boundary_event_state"],
            result["quotient_equivalent_decoder"],
        )

    def test_boundary_jet_audit(self) -> None:
        result = run_boundary_jet_audit()
        self.assertTrue(all(result["checks"].values()))
        self.assertGreater(float(result["full_boundary_jet_lower"]), 0.0011)

    def test_actual_gate_fails_closed(self) -> None:
        result = run_actual_weil_adapter_gate()
        self.assertTrue(all(result["checks"].values()))
        self.assertFalse(result["actual_source_event_adapter_complete"])
        self.assertFalse(
            result["pins"][
                "source_event_analysis_factorization_through_metric_graph"
            ]
        )

    def test_negative_controls(self) -> None:
        result = run_negative_controls()
        self.assertTrue(all(result["checks"].values()))

    def test_combined_and_hash(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_STAGE3C",
        )
        self.assertTrue(all(result["checks"].values()))
        expected = Path(__file__).with_name(
            "NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_EXPECTED.sha256"
        ).read_text(encoding="ascii").strip()
        self.assertEqual(expected, sha256(canonical_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
