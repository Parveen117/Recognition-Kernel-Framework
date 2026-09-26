from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.paninian_seam_calculus import GAM
from proof_lab.seam_compensated_confluence_verdict import build_certificate, canonical_bytes, certificate_sha256, verdict, word_equiv, word_rules

EXPECTED = Path(__file__).with_name("SEAM_COMPENSATED_CONFLUENCE_VERDICT_EXPECTED.sha256")


class SeamCompensatedConfluenceVerdictTests(unittest.TestCase):
    def test_no_classical_import(self) -> None:
        src = Path(__file__).with_name("seam_compensated_confluence_verdict.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "networkx", "float(", "import sympy"):
            self.assertNotIn(forbidden, src)

    def test_memory_flips_verdict(self) -> None:
        self.assertEqual(verdict(GAM, word_rules(True), word_equiv, priority=False)["verdict"], "CONFLUENT_MOD_LEDGER")
        v = verdict(GAM, word_rules(False), word_equiv, priority=False)
        self.assertEqual(v["verdict"], "NOT_CONFLUENT")
        self.assertTrue(any(set(p["pair"]) == {"1.3.9", "7.3.77"} for p in v["open"]))

    def test_open_pair_witness_and_cycle(self) -> None:
        rules = [("r1", lambda w: ("b",) if w == ("a",) else None), ("r2", lambda w: ("c",) if w == ("a",) else None)]
        v = verdict(("a",), rules, lambda x, y: x == y, priority=False)
        self.assertEqual(v["verdict"], "NOT_CONFLUENT")
        self.assertEqual(v["open"][0]["class"], "OPEN")
        cyc = [("r1", lambda w: ("b",) if w == ("a",) else None), ("r2", lambda w: ("a",) if w == ("b",) else None)]
        self.assertEqual(verdict(("a",), cyc, lambda x, y: x == y, priority=False)["verdict"], "NON_TERMINATING")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_SEAM_COMPENSATED_CONFLUENCE_VERDICT_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
