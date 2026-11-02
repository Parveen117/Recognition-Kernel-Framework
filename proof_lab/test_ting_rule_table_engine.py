from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.ting_rule_table_engine import NASAL, SUITE, V_ORACLE, build_certificate, canonical_bytes, certificate_sha256, oracles, paradigm

EXPECTED = Path(__file__).with_name("TING_RULE_TABLE_ENGINE_EXPECTED.sha256")


class T129Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("ting_rule_table_engine.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_suite_equals_the_certified_oracles(self) -> None:
        O = oracles()
        for r, lak, cells, pada in SUITE:
            exp = NASAL[r][3] if r in NASAL else (V_ORACLE[(r, pada)] if (lak == "laṭ" and (r, pada) in V_ORACLE) else O[r][lak])
            self.assertEqual(paradigm(r, lak, cells=cells, pada=pada), exp, f"{r}.{lak}")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_TING_RULE_TABLE_ENGINE_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
