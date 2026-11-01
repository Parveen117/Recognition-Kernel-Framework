from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.tripadi_nishtha_compiled import TRIPADI, build_certificate, canonical_bytes, certificate_sha256, load_entries, nishtha

EXPECTED = Path(__file__).with_name("TRIPADI_NISHTHA_COMPILED_EXPECTED.sha256")


class TripadiNishthaCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("tripadi_nishtha_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_nouns_and_order(self) -> None:
        e = load_entries()
        self.assertEqual(nishtha("1011130", e)["output"], "labdha")
        self.assertEqual(nishtha("1011130", e, list(reversed(TRIPADI)))["output"], "labhdha")
        self.assertEqual(nishtha("1060001", e)["output"], "tunna")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_TRIPADI_NISHTHA_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
