from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.paninian_it_samjna_compiled import build_certificate, canonical_bytes, certificate_sha256, insert_agama, its, placement

EXPECTED = Path(__file__).with_name("PANINIAN_IT_SAMJNA_COMPILED_EXPECTED.sha256")


class PaninianItSamjnaCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("paninian_it_samjna_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_its_examples(self) -> None:
        self.assertEqual(its("śap", "pratyaya")["remaining"], "a")
        self.assertEqual(its("tas", "pratyaya", vibhakti=True)["remaining"], "tas")       # 1.3.4
        self.assertEqual(its("tas", "pratyaya", vibhakti=False)["remaining"], "ta")
        self.assertEqual(its("kan", "pratyaya", taddhita=True)["remaining"], "ka")         # ataddhite
        self.assertEqual(its("ḍukṛñ", "dhatu")["remaining"], "kṛ")                          # 1.3.5 + 1.3.3
        self.assertEqual(its("jhi", "pratyaya", vibhakti=True)["remaining"], "jhi")        # jñāpaka 7.1.3
        self.assertEqual(its("jhi", "pratyaya", vibhakti=True, jnapaka=False)["remaining"], "i")

    def test_augments(self) -> None:
        self.assertEqual(placement("tu~k"), "after")
        self.assertEqual(placement("aṭ"), "before")
        self.assertEqual("".join(insert_agama(("bh", "a", "v", "a", "t"), "nu~m")), "bhavant")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PANINIAN_IT_SAMJNA_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
