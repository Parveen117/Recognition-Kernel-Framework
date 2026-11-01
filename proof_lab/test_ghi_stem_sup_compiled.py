from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.ghi_stem_sup_compiled import GURU, HARI, build_certificate, canonical_bytes, certificate_sha256, paradigm

EXPECTED = Path(__file__).with_name("GHI_STEM_SUP_COMPILED_EXPECTED.sha256")


class GhiStemSupCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("ghi_stem_sup_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_hari_guru_agni(self) -> None:
        self.assertEqual(paradigm(("h", "a", "r", "i")), HARI)
        self.assertEqual(paradigm(("g", "u", "r", "u")), GURU)
        self.assertEqual(paradigm(("a", "g", "n", "i"))["3s"], "agninā")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_GHI_STEM_SUP_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
