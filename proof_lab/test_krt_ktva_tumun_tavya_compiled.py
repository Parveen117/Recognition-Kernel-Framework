from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.krt_ktva_tumun_tavya_compiled import ORACLE, build_certificate, canonical_bytes, certificate_sha256, derive

EXPECTED = Path(__file__).with_name("KRT_KTVA_TUMUN_TAVYA_COMPILED_EXPECTED.sha256")


class KrtKtvaTumunTavyaCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("krt_ktva_tumun_tavya_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_forms(self) -> None:
        for a in ORACLE:
            for r in ORACLE[a]:
                self.assertEqual(derive(r, a)[0], ORACLE[a][r])

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_KRT_KTVA_TUMUN_TAVYA_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
