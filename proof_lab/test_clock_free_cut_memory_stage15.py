from __future__ import annotations

from pathlib import Path
import unittest

from proof_lab.clock_free_cut_memory_stage15_examples import (
    build_certificate,
    madhava_smriti_example,
    morphic_stabilization_example,
    recognition_complete_limit_example,
    recovered_middle_example,
    shadow_recognition_cauchy_example,
)
from proof_lab.write_stage15_certificate import canonical_bytes


class Stage15Tests(unittest.TestCase):
    def test_recovered_middle(self) -> None:
        result = recovered_middle_example()
        self.assertTrue(all(result["checks"].values()))
        self.assertTrue(result["shadow_equal"])
        self.assertFalse(result["raw_recovered"])
        self.assertTrue(result["aligned_recovered"])

    def test_shadow_vs_recognition_cauchy(self) -> None:
        result = shadow_recognition_cauchy_example()
        self.assertTrue(all(result["checks"].values()))
        self.assertTrue(result["shadow_cauchy"])
        self.assertFalse(result["raw_recognition_cauchy"])

    def test_madhava_smriti(self) -> None:
        result = madhava_smriti_example()
        self.assertTrue(all(result["checks"].values()))

    def test_morphic_stabilization(self) -> None:
        result = morphic_stabilization_example()
        self.assertTrue(all(result["checks"].values()))

    def test_recognition_complete_limit(self) -> None:
        result = recognition_complete_limit_example()
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["limit_relative_gap"], "19/100")
        self.assertEqual(result["outward_top_n"], result["exact_limit_top"])

    def test_combined(self) -> None:
        result = build_certificate()
        self.assertEqual(result["status"], "PASS_CLOCK_FREE_CUT_MEMORY_STAGE15")
        self.assertTrue(all(result["checks"].values()))

    def test_expected_certificate_is_byte_stable(self) -> None:
        expected_path = Path(__file__).with_name(
            "CLOCK_FREE_CUT_MEMORY_STAGE15_EXPECTED.json"
        )
        self.assertEqual(expected_path.read_bytes(), canonical_bytes())


if __name__ == "__main__":
    unittest.main()
