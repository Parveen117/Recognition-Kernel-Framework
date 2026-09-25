from __future__ import annotations

from pathlib import Path
import unittest

from proof_lab.cut_variational_minimal_observer import (
    build_certificate,
    canonical_bytes,
    run_faithfulness_transfer_example,
    run_minimal_observer_example,
    run_source_restriction_example,
    run_variational_tail_example,
)


class CutVariationalMinimalObserverTests(unittest.TestCase):
    def test_minimal_observer(self) -> None:
        result = run_minimal_observer_example()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["memory_rank"], 5)
        self.assertEqual(result["rank_five_minimum_action"], "0")
        self.assertEqual(result["rank_four_minimum_action"], "1/25")
        self.assertEqual(result["wrong_rank_five_orientation_action"], "1/25")

    def test_source_restriction(self) -> None:
        result = run_source_restriction_example()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["collapsed_rank"], 45)
        self.assertEqual(result["target_relevant_blind_dimension"], 5)
        self.assertEqual(result["split_occurrence_determinant"], "-2592")
        self.assertEqual(result["repaired_rank"], 50)

    def test_faithfulness_transfer(self) -> None:
        result = run_faithfulness_transfer_example()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["observer_action_n"], "1/100")
        self.assertEqual(result["observer_action_m"], "1/324")
        self.assertEqual(result["observer_action_limit"], "0")

    def test_variational_tail(self) -> None:
        result = run_variational_tail_example()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(
            result["minimum_actions_by_rank"],
            {"3": "21/100", "4": "1/20", "5": "1/100", "6": "0"},
        )

    def test_combined_certificate(self) -> None:
        result = build_certificate()
        self.assertEqual(
            result["status"],
            "PASS_CUT_VARIATIONAL_MINIMAL_OBSERVER_V0_1",
        )
        self.assertTrue(all(result["checks"].values()))

    def test_expected_certificate_is_byte_stable(self) -> None:
        expected = Path(__file__).with_name(
            "CUT_VARIATIONAL_MINIMAL_OBSERVER_EXPECTED.json"
        ).read_bytes()
        self.assertEqual(expected, canonical_bytes())


if __name__ == "__main__":
    unittest.main()
