from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.nirukta_dhatupatha_nama import build_certificate, canonical_bytes, certificate_sha256, kta_from_entry, load_entries

EXPECTED = Path(__file__).with_name("NIRUKTA_DHATUPATHA_NAMA_EXPECTED.sha256")


class NiruktaDhatupathaNamaTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("nirukta_dhatupatha_nama.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_entries(self) -> None:
        e = load_entries()
        self.assertEqual(kta_from_entry("1050001", e["1050001"])["pratipadika"], "suta")    # ṣuñ: 6.1.64
        self.assertEqual(kta_from_entry("1080001", e["1080001"])["pratipadika"], "tata")    # tanu~: 6.4.37
        self.assertEqual(kta_from_entry("1090001", e["1090001"])["pratipadika"], "krīta")   # ḍukrīñ: 1.3.5

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_NIRUKTA_DHATUPATHA_NAMA_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
