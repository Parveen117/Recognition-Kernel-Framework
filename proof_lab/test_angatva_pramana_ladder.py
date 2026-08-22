from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.angatva_pramana_ladder import build_certificate, canonical_bytes, certificate_sha256, resolve

EXPECTED = Path(__file__).with_name("ANGATVA_PRAMANA_LADDER_EXPECTED.sha256")


class AngatvaPramanaLadderTests(unittest.TestCase):
    def test_delay_order(self) -> None:
        self.assertEqual(resolve([("samākhyā", "x"), ("śruti", "y")])["angin"], "y")
        self.assertTrue(resolve([("vākya", "a"), ("vākya", "b")])["vikalpa"])

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_ANGATVA_PRAMANA_LADDER_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
