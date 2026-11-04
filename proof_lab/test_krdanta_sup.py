from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.krdanta_sup import STRI, build_certificate, canonical_bytes, certificate_sha256, declension, feminine

EXPECTED = Path(__file__).with_name("KRDANTA_SUP_EXPECTED.sha256")


class T153Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("krdanta_sup.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_feminine_stems(self) -> None:
        self.assertEqual(feminine("bhūta", "kta")[0], "bhūtā")
        self.assertEqual(feminine("bhūtavat", "ktavatu")[0], "bhūtavatī")
        self.assertEqual(feminine("bhavat", "śatṛ", True)[0], "bhavantī")
        self.assertEqual(feminine("adat", "śatṛ", False)[0], "adatī")
        self.assertEqual(feminine("kartṛ", "tṛc")[0], "kartrī")
        self.assertEqual(feminine("kāraka", "ṇvul")[0], "kārikā")
        self.assertEqual(len(STRI), 5)

    def test_classic_padas(self) -> None:
        for (r, a, g, c), exp in {("bhū", "kta", "m", "1s"): "bhūtaḥ", ("bhū", "kta", "f", "1s"): "bhūtā", ("bhū", "kta", "n", "1p"): "bhūtāni", ("bhū", "ktavatu", "m", "1s"): "bhūtavān",
                                  ("bhū", "ktavatu", "n", "1p"): "bhūtavanti", ("bhū", "ktavatu", "f", "7s"): "bhūtavatyām", ("kṛ", "tṛc", "m", "1s"): "kartā", ("kṛ", "tṛc", "m", "2p"): "kartṝn",
                                  ("kṛ", "tṛc", "f", "1s"): "kartrī", ("bhū", "śatṛ", "m", "1s"): "bhavan", ("bhū", "śatṛ", "m", "3s"): "bhavatā", ("bhū", "śatṛ", "n", "1d"): "bhavantī",
                                  ("ad", "śatṛ", "f", "1s"): "adatī", ("dā", "śatṛ", "m", "1s"): "dadat", ("kṣubh9", "śatṛ", "m", "1s"): "kṣubhnan", ("edh", "śānac", "f", "1s"): "edhamānā",
                                  ("kṛ", "śānac", "m", "1s"): "kurvāṇaḥ", ("pac", "ṇvul", "m", "1s"): "pācakaḥ", ("bhū", "tavya", "n", "1s"): "bhavitavyam"}.items():
            self.assertEqual(declension(r, a, g, c)[0], exp, (r, a, g, c))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_KRDANTA_SUP_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
