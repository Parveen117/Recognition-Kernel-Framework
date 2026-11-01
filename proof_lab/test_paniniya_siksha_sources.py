from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.paniniya_siksha_sources import STHANA_SIKSA, build_certificate, canonical_bytes, certificate_sha256, prayatna_karana, prayatna_sparsa

EXPECTED = Path(__file__).with_name("PANINIYA_SIKSHA_SOURCES_EXPECTED.sha256")


class PaniniyaSikshaSourcesTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("paniniya_siksha_sources.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_verses_17_18(self) -> None:
        self.assertEqual(STHANA_SIKSA["k"], "jihvāmūla")
        self.assertEqual(STHANA_SIKSA["h"], "kaṇṭha")
        self.assertEqual(STHANA_SIKSA["v"], "danta-oṣṭha")
        self.assertEqual(prayatna_karana("e"), "vivṛta-2")
        self.assertEqual(prayatna_karana("ai"), "vivṛta-3")
        self.assertEqual(prayatna_sparsa("ś"), "nema-spṛṣṭa")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PANINIYA_SIKSHA_SOURCES_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
