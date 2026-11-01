from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.asirlin_parasmaipada_compiled import build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("ASIRLIN_PARASMAIPADA_COMPILED_EXPECTED.sha256")


class T115Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("asirlin_parasmaipada_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_ASIRLIN_PARASMAIPADA_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
