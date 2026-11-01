from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.nirukta_nama_akhyatajani import build_certificate, canonical_bytes, certificate_sha256, kta_pratipadika

EXPECTED = Path(__file__).with_name("NIRUKTA_NAMA_AKHYATAJANI_EXPECTED.sha256")


class NiruktaNamaAkhyatajaniTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("nirukta_nama_akhyatajani.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_kta_pratipadikas(self) -> None:
        self.assertEqual(kta_pratipadika("gam")["pratipadika"], "gata")
        self.assertEqual(kta_pratipadika("bhū")["pratipadika"], "bhūta")
        self.assertEqual(kta_pratipadika("kṛ")["pratipadika"], "kṛta")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_NIRUKTA_NAMA_AKHYATAJANI_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
