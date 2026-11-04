from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pg_written_replay import (ADJUDICATED, CONSTRUCTOR_ENDINGS, OUT_OF_SCOPE, SOURCES, TARGETS, athematic_tuples, build_certificate, canonical_bytes,
                                         certificate_sha256, constructor_endings_from_written, history_sequences, is_subsequence, pg19_rows, table_path)

EXPECTED = Path(__file__).with_name("PG_WRITTEN_REPLAY_EXPECTED.sha256")


class T155Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("pg_written_replay.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_pg19_register_is_read_from_the_written_files(self) -> None:
        self.assertEqual(constructor_endings_from_written(), CONSTRUCTOR_ENDINGS)
        ath = athematic_tuples()
        self.assertEqual(ath["I_P(kṛ)"][0], "karotu"); self.assertEqual(ath["I_P(kṛ)"][6], "karavāṇi"); self.assertEqual(ath["O_A(krī)"][0], "krīṇīta")
        rows = pg19_rows()
        self.assertEqual(len(rows), 58)
        self.assertEqual([r["block"] for r in rows].count("BK"), 15); self.assertEqual([r["block"] for r in rows].count("CK"), 22)
        self.assertEqual([r["block"] for r in rows].count("CP"), 13); self.assertEqual([r["block"] for r in rows].count("BP"), 4); self.assertEqual([r["block"] for r in rows].count("BH"), 4)

    def test_classic_forms_and_the_adjudicated_cell(self) -> None:
        self.assertEqual(table_path("ting", "kṛ", "loṭ", "1s", "P")[0], "karavāṇi")
        self.assertEqual(table_path("ting", "kṛ", "loṭ", "1s", "NP")[0], "kārayāṇi")
        self.assertEqual(table_path("ting", "krī", "liṅ", "3s", "A")[0], "krīṇīta")
        self.assertEqual(table_path("ting", "kṛ", "liṅ", "3p", "A")[0], "kurvīran")
        for k, v in ADJUDICATED.items():
            self.assertTrue(v["reason"].split(" ")[0] in SOURCES, k)

    def test_pg47_sequences_and_paths(self) -> None:
        seqs = history_sequences()
        self.assertEqual(len(seqs), 29)
        self.assertEqual(seqs["C05"]["written_sequence"][:1], ["7.1.9"])
        self.assertEqual(table_path("sup", "vṛkṣa", "3p", "m", ()), ("vṛkṣaiḥ", ["7.1.9", "6.1.88", "8.2.66", "8.3.15"]))
        self.assertEqual(table_path("sup", "vṛkṣa", "4p", "m", ())[1][0], "7.3.103")
        self.assertNotIn("7.3.102", table_path("sup", "vṛkṣa", "4p", "m", ())[1])
        self.assertIn("7.2.79", table_path("ting", "lū", "liṅ", "3s", "P")[1]); self.assertNotIn("7.2.79", table_path("ting", "lū", "āśīrliṅ", "3s", "A")[1])
        self.assertEqual(table_path("sup", "pañcan", "1p", "m", ()), ("pañca", ["7.1.22", "8.2.7"]))
        self.assertEqual(table_path("krt", "ās2A", "śānac"), ("āsīna", ["3.2.124", "7.2.83"]))
        self.assertTrue(is_subsequence(["a", "c"], ["a", "b", "c"])); self.assertFalse(is_subsequence(["c", "a"], ["a", "b", "c"]))
        self.assertEqual(set(seqs), {t.rstrip("b") for t in TARGETS} | set(OUT_OF_SCOPE))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PG_WRITTEN_REPLAY_CANDIDATE")
        r4 = payload["r4_pg19_register"]
        self.assertEqual((r4["positions"], r4["replayed"], r4["agree"]), (976, 706, 703))
        self.assertEqual(r4["to_adjudicate"], {})
        r5 = payload["r5_pg47_histories"]
        self.assertEqual((r5["histories"], r5["compared_count"], r5["agree"], r5["out_of_scope_count"]), (29, 12, 12, 18))
        r6 = payload["r6_written_registers"]
        self.assertEqual(r6["text_mismatch"], []); self.assertEqual(r6["not_in_pinned_edition"], []); self.assertEqual(r6["contracts"], 3796)
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
