from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.vedanga_sources_quoted import build_certificate, canonical_bytes, certificate_sha256, daylength_rvj22, prastara_q, sqrt2_cord_q, uddishta_q

EXPECTED = Path(__file__).with_name("VEDANGA_SOURCES_QUOTED_EXPECTED.sha256")


class VedangaSourcesQuotedTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("vedanga_sources_quoted.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_quoted_rules(self) -> None:
        self.assertEqual(prastara_q(3), ["ggg", "lgg", "glg", "llg", "ggl", "lgl", "gll", "lll"])
        self.assertEqual(uddishta_q("glgl"), 11)
        self.assertEqual(sqrt2_cord_q(), Fraction(577, 408))
        self.assertEqual(daylength_rvj22(183), 18)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_VEDANGA_SOURCES_QUOTED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
