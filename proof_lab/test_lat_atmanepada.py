from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.lat_atmanepada import build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("LAT_ATMANEPADA_EXPECTED.sha256")


class LatAtmanepadaTests(unittest.TestCase):
    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_LAT_ATMANEPADA_CANDIDATE")
        self.assertEqual(payload["oracle_mismatches"], [])
        self.assertEqual(payload["forms"]["labh:3d"], "labhete")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
