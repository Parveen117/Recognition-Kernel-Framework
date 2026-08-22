from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab import sup_vibhakti_resolver_ladder as t63
from proof_lab.sup_vibhakti_resolver_ladder import derive
from proof_lab.ting_lat_parasmaipada import ORACLE, RULES, build_certificate, canonical_bytes, certificate_sha256, derive_para_only, grammar_wide_domains, inputs, surface

EXPECTED = Path(__file__).with_name("TING_LAT_PARASMAIPADA_EXPECTED.sha256")


class TingLatParasmaipadaTests(unittest.TestCase):
    def test_paradigms_match_oracle(self) -> None:
        ins = inputs()
        dom = grammar_wide_domains(ins, t63)
        for code, W0 in ins.items():
            rn, c = code.split(":")
            self.assertEqual(surface(derive(W0, RULES, dom=dom)[0]), ORACLE[rn][c], code)

    def test_real_earlier_apavada(self) -> None:
        ins = inputs()
        self.assertEqual(surface(derive_para_only(ins["bhU:3p"], RULES)), "bhavAnti")
        self.assertEqual(surface(derive(ins["bhU:3p"], RULES, dom=grammar_wide_domains(ins, t63))[0]), "bhavanti")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_TING_LAT_PARASMAIPADA_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
