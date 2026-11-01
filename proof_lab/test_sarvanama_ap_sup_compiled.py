from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.sarvanama_ap_sup_compiled import SA, SARVA_F, build_certificate, canonical_bytes, certificate_sha256, paradigm

EXPECTED = Path(__file__).with_name("SARVANAMA_AP_SUP_COMPILED_EXPECTED.sha256")


class SarvanamaApSupCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("sarvanama_ap_sup_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_paradigms(self) -> None:
        self.assertEqual(paradigm(("s", "a", "r", "v", "a")), SARVA_F)
        self.assertEqual(paradigm(("t", "a", "d"), tyadadi=True), SA)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_SARVANAMA_AP_SUP_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
