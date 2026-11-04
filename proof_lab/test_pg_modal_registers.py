from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pg_modal_registers import (OPTIONS, SOURCES, build_certificate, canonical_bytes, certificate_sha256, pg21_expand, pg21_interfaces, split_top,
                                          written_constructors_checked)

EXPECTED = Path(__file__).with_name("PG_MODAL_REGISTERS_EXPECTED.sha256")


class T156Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("pg_modal_registers.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_constructors_are_the_written_ones(self) -> None:
        self.assertTrue(all(written_constructors_checked().values()))
        s4, s5 = pg21_interfaces()
        self.assertEqual(s4["sun"], ("sunv", "sunu")); self.assertEqual(s4["āpn"], ("āpnuv", "āpnuhi")); self.assertIn("pun", s5)
        self.assertEqual(pg21_expand("U_P(sun)", s4, s5), ["sunotu", "sunutām", "sunvantu", "sunu", "sunutam", "sunuta", "sunavāni", "sunavāva", "sunavāma"])
        self.assertEqual(pg21_expand("A_P(pun)", s4, s5)[3], "punīhi"); self.assertEqual(pg21_expand("O_A(sunv)", s4, s5)[0], "sunvīta")
        self.assertEqual(split_top("a, {b, c}, d"), ["a", "{b, c}", "d"])
        for root, note in OPTIONS.items():
            self.assertIn(note.split(" ")[0], SOURCES, root)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PG_MODAL_REGISTERS_CANDIDATE")
        t = payload["totals"]
        self.assertEqual((t["positions"], t["replayed"], t["agree"], t["to_adjudicate"]), (1026, 693, 693, 0))
        self.assertEqual((t["branch_rows"], t["branch_rows_mixed"]), (8, 2))
        self.assertEqual(sorted(payload["branch_rows_the_table_realises_mixed"]), ["PG21:NM20:loṭ", "PG21:NM21:loṭ"])
        for p in ("PG20", "PG21", "PG22"):
            self.assertEqual(payload["packets"][p]["to_adjudicate"], {}, p)
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
