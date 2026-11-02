from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.panini_kernel import build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("PANINI_KERNEL_EXPECTED.sha256")


class T142Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("panini_kernel.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_rows_and_ledger_agree(self) -> None:
        c = build_certificate()
        self.assertEqual(c["k1"]["rows_not_in_ledger"], [])
        self.assertEqual(c["k1"]["ledger_hand_coded_not_in_rows"], {})
        self.assertTrue(c["k2"]["checks"]["shared_rows_are_junction_or_tripadi_rules"])

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PANINI_KERNEL_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
