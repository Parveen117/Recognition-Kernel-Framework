from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pg_modal_registers_ii import replay
from proof_lab.pg_modal_registers_iii import E_P, OPTIONS, SOURCES, build_certificate, canonical_bytes, cat, certificate_sha256, written_constructors_checked

EXPECTED = Path(__file__).with_name("PG_MODAL_REGISTERS_III_EXPECTED.sha256")


class T159Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("pg_modal_registers_iii.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_constructors_sources_and_classic_forms(self) -> None:
        self.assertTrue(all(written_constructors_checked().values()))
        for root, note in OPTIONS.items():
            self.assertIn(note.split(" ")[0], SOURCES, root)
        self.assertEqual(cat({"a", "b"}, "x"), {"ax", "bx"}); self.assertEqual(cat("a", "x"), "ax"); self.assertEqual(E_P["3s"], "avītu")
        self.assertEqual(replay("dviṣ2", "loṭ", "2s", "P"), "dviḍḍhi"); self.assertEqual(replay("duh2A", "loṭ", "2s", "A"), "dhukṣva"); self.assertEqual(replay("lih2", "loṭ", "3s", "P"), "leḍhu")
        self.assertEqual(replay("yu2", "loṭ", "3s", "P"), "yautu"); self.assertEqual(replay("i2", "loṭ", "3p", "P"), "yantu"); self.assertEqual(replay("vī2", "loṭ", "3p", "P"), "viyantu")
        self.assertEqual(replay("sū2A", "liṅ", "3s", "A"), "suvīta"); self.assertEqual(replay("ric", "loṭ", "3s", "P"), "riṇaktu"); self.assertEqual(replay("kṛt", "loṭ", "2s", "P"), "kṛnddhi")
        self.assertEqual(replay("vac2", "loṭ", "2s", "P"), "vagdhi"); self.assertEqual(replay("ās2A", "loṭ", "2s", "A"), "āssva")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PG_MODAL_REGISTERS_III_CANDIDATE")
        t = payload["totals"]
        self.assertEqual((t["positions"], t["replayed"], t["agree"], t["to_adjudicate"], t["other_branch_of_an_option"]), (1457, 1043, 1043, 0, 75))
        self.assertEqual(payload["branch_rows_the_table_realises_mixed"], {})
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
