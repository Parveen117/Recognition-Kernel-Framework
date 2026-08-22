from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.stem_classes_gayatri_coverage import GAYATRI_LINE_1, build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("STEM_CLASSES_GAYATRI_COVERAGE_EXPECTED.sha256")


class StemClassesGayatriCoverageTests(unittest.TestCase):
    def test_certificate_pin_and_coverage(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_STEM_CLASSES_GAYATRI_COVERAGE_CANDIDATE")
        self.assertEqual(payload["oracle_mismatches"], [])
        self.assertEqual([p for p in GAYATRI_LINE_1 if payload["gayatri_line_1"][p] != "DERIVED"], ["dhImahi"])
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
