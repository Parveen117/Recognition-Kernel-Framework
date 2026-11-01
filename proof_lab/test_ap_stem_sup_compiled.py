from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.ap_stem_sup_compiled import LATA_ORACLE, build_certificate, canonical_bytes, certificate_sha256, paradigm, tap_stem

EXPECTED = Path(__file__).with_name("AP_STEM_SUP_COMPILED_EXPECTED.sha256")


class ApStemSupCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("ap_stem_sup_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_lata(self) -> None:
        self.assertEqual(paradigm(tap_stem(("l", "a", "t", "a"))), LATA_ORACLE)
        self.assertEqual(paradigm(tap_stem(("k", "ṛ", "t", "a")))["4s"], "kṛtāyai")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_AP_STEM_SUP_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
