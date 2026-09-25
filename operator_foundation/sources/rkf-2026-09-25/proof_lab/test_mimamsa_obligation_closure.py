from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.mimamsa_obligation_closure import build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("MIMAMSA_OBLIGATION_CLOSURE_EXPECTED.sha256")


class MimamsaObligationClosureTests(unittest.TestCase):
    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_MIMAMSA_OBLIGATION_CLOSURE_CANDIDATE")
        self.assertEqual(payload["closures"]["T4"]["K_M"], 1)
        self.assertEqual(payload["closures"]["T5_mantra_alone"]["obligations"], {})
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
