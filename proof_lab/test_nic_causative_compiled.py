from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.nic_causative_compiled import ROOTS, build_certificate, canonical_bytes, certificate_sha256, forms_for, oracle

EXPECTED = Path(__file__).with_name("NIC_CAUSATIVE_COMPILED_EXPECTED.sha256")


class NicCausativeCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("nic_causative_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_forms(self) -> None:
        for r in ROOTS:
            self.assertEqual(forms_for(r), oracle(r), r)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_NIC_CAUSATIVE_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
