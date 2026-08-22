from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pada_to_line_external_sandhi import build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("PADA_TO_LINE_EXTERNAL_SANDHI_EXPECTED.sha256")


class PadaToLineExternalSandhiTests(unittest.TestCase):
    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PADA_TO_LINE_EXTERNAL_SANDHI_CANDIDATE")
        self.assertEqual(payload["lines"]["line1"], "tat savitur vareNyaM bhargo devasya dhImahi")
        self.assertEqual(payload["lines"]["line2"], "dhiyo yo naH pracodayAt")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
