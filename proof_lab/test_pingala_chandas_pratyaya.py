from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pingala_chandas_pratyaya import build_certificate, canonical_bytes, certificate_sha256, meru, nashta, prastara, sankhya, uddishta

EXPECTED = Path(__file__).with_name("PINGALA_CHANDAS_PRATYAYA_EXPECTED.sha256")


class PingalaChandasPratyayaTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("pingala_chandas_pratyaya.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_pratyayas(self) -> None:
        self.assertEqual(prastara(3), ["ggg", "lgg", "glg", "llg", "ggl", "lgl", "gll", "lll"])
        self.assertEqual(nashta(4, 11), "glgl")
        self.assertEqual(uddishta("glgl"), 11)
        self.assertEqual(sankhya(10)[0], 1024)
        self.assertEqual(meru(4), [1, 4, 6, 4, 1])

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PINGALA_CHANDAS_PRATYAYA_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
