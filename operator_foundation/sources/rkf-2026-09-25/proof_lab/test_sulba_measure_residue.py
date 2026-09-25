from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.sulba_measure_residue import build_certificate, canonical_bytes, certificate_sha256, sqrt2_cord

EXPECTED = Path(__file__).with_name("SULBA_MEASURE_RESIDUE_EXPECTED.sha256")


class SulbaMeasureResidueTests(unittest.TestCase):
    def test_cord(self) -> None:
        self.assertEqual(sqrt2_cord(), Fraction(577, 408))

    def test_no_float_in_verdicts(self) -> None:
        src = Path(__file__).with_name("sulba_measure_residue.py").read_text(encoding="utf-8")
        self.assertNotIn("math.sqrt", src)
        self.assertEqual(src.count("float("), 1)  # display only

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_SULBA_MEASURE_RESIDUE_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
