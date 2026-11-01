from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pingala_chandas_pratyaya import build_certificate, canonical_bytes, certificate_sha256, nashta, prastara, uddishta

EXPECTED = Path(__file__).with_name("PINGALA_CHANDAS_PRATYAYA_EXPECTED.sha256")


class PingalaChandasPratyayaTests(unittest.TestCase):
    def test_inverse(self) -> None:
        for r, p in enumerate(prastara(6), start=1):
            self.assertEqual(nashta(6, r), p)
            self.assertEqual(uddishta(p), r)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PINGALA_CHANDAS_PRATYAYA_CANDIDATE")
        self.assertEqual([p["count"] for p in payload["gayatri_padas_as_written"]], [7, 8, 8])
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
