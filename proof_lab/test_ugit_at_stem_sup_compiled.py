from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.ugit_at_stem_sup_compiled import STEMS, build_certificate, canonical_bytes, certificate_sha256, oracle, paradigm

EXPECTED = Path(__file__).with_name("UGIT_AT_STEM_SUP_COMPILED_EXPECTED.sha256")


class UgitAtStemSupCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("ugit_at_stem_sup_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_forms(self) -> None:
        for r in STEMS:
            self.assertEqual(paradigm(r), oracle(r), r)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_UGIT_AT_STEM_SUP_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
