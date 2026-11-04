from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.ting_rule_table_engine import NASAL, SUITE, V_ORACLE, build_certificate, canonical_bytes, certificate_sha256, oracles, paradigm, W_ORACLE

EXPECTED = Path(__file__).with_name("TING_RULE_TABLE_ENGINE_EXPECTED.sha256")


class T129Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("ting_rule_table_engine.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_suite_equals_the_certified_oracles(self) -> None:
        O = oracles()
        for r, lak, cells, pada in SUITE:
            exp = W_ORACLE[(r, lak, pada)] if (r, lak, pada) in W_ORACLE else (NASAL[r][3] if r in NASAL else (V_ORACLE[(r, pada)] if (lak == "laṭ" and (r, pada) in V_ORACLE) else O[r][lak]))
            got = paradigm(r, lak, cells=cells, pada=pada)
            for c in cells:   # a set: the written line's alternatives, the table's form one of them (theorum/160)
                self.assertTrue(got[c] in exp[c] if isinstance(exp[c], set) else got[c] == exp[c], f"{r}.{lak}.{c}: {got[c]} vs {exp[c]}")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_TING_RULE_TABLE_ENGINE_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())

    def test_dhatupatha_pinned_and_read(self) -> None:
        from proof_lab.ting_rule_table_engine import DHATUPATHA, DHATUPATHA_SHA256, anudatta
        self.assertEqual(hashlib.sha256(DHATUPATHA.read_bytes()).hexdigest(), DHATUPATHA_SHA256)
        self.assertIs(anudatta("bhū", 1), False); self.assertIs(anudatta("ṇīñ", 1), True); self.assertIs(anudatta("edha~", 1), False); self.assertIs(anudatta("ḍukṛñ", 8), True)


if __name__ == "__main__":
    unittest.main()
