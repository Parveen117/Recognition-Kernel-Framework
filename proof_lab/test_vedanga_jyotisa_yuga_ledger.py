from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.vedanga_jyotisa_yuga_ledger import build_certificate, canonical_bytes, certificate_sha256, daylight, wind_phase

EXPECTED = Path(__file__).with_name("VEDANGA_JYOTISA_YUGA_LEDGER_EXPECTED.sha256")


class VedangaJyotisaYugaLedgerTests(unittest.TestCase):
    def test_basic(self) -> None:
        self.assertEqual(wind_phase(Fraction(1830), Fraction(1830, 62)), (62, Fraction(0)))
        self.assertEqual(daylight(183), 18)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_VEDANGA_JYOTISA_YUGA_LEDGER_CANDIDATE")
        self.assertEqual(payload["five_year_residue_days"], "-1830/31")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
