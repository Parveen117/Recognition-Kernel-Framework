from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.sup_vibhakti_resolver_ladder import ORACLE, RULES, build_certificate, canonical_bytes, certificate_sha256, derive, inputs, paradigm_domains, surface

EXPECTED = Path(__file__).with_name("SUP_VIBHAKTI_RESOLVER_LADDER_EXPECTED.sha256")


class SupVibhaktiResolverLadderTests(unittest.TestCase):
    def test_paradigm_matches_oracle(self) -> None:
        dom = paradigm_domains(RULES)
        for code, W0 in inputs().items():
            self.assertEqual(surface(derive(W0, RULES, dom=dom)[0]), ORACLE[code], code)

    def test_memory_control_breaks_3s(self) -> None:
        dom = paradigm_domains(RULES, carry=False)
        self.assertNotEqual(surface(derive(inputs()["3s"], RULES, carry=False, dom=dom)[0]), "rAmeNa")

    def test_no_hilbert_no_float(self) -> None:
        src = Path(__file__).with_name("sup_vibhakti_resolver_ladder.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "float(", ": True,\n"):
            self.assertNotIn(forbidden, src)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_SUP_VIBHAKTI_RESOLVER_LADDER_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
