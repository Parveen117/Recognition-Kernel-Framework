from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.krt_ghan_lyut_nvul_satr_compiled import CASES, build_certificate, canonical_bytes, certificate_sha256, krt

EXPECTED = Path(__file__).with_name("KRT_GHAN_LYUT_NVUL_SATR_COMPILED_EXPECTED.sha256")


class KrtGhanLyutNvulSatrCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("krt_ghan_lyut_nvul_satr_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_forms(self) -> None:
        for r, a, exp in CASES:
            self.assertEqual(krt(r, a)[0], exp)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_KRT_GHAN_LYUT_NVUL_SATR_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
