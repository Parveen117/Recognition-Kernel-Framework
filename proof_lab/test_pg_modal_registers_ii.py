from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pg_modal_registers_ii import ADJUDICATED, AUGMENT_ROWS, OPTIONS, SOURCES, build_certificate, canonical_bytes, certificate_sha256, replay

EXPECTED = Path(__file__).with_name("PG_MODAL_REGISTERS_II_EXPECTED.sha256")


class T157Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("pg_modal_registers_ii.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_sources_and_classic_forms(self) -> None:
        for root, note in OPTIONS.items():
            self.assertIn(note.split(" ")[0], SOURCES, root)
        for k, v in ADJUDICATED.items():
            self.assertIn(v["reason"].split(" ")[0], SOURCES, k)
        self.assertEqual(replay("han2", "loṭ", "2s", "P"), "jahi"); self.assertEqual(replay("brū2", "loṭ", "3s", "P"), "bravītu"); self.assertEqual(replay("śī2A", "loṭ", "3s", "A"), "śetām")
        self.assertEqual(replay("bhī3", "loṭ", "1s", "P"), "bibhayāni"); self.assertEqual(replay("hā3", "loṭ", "3p", "P"), "jahatu"); self.assertEqual(replay("mā3A", "loṭ", "3s", "A"), "mimītām")
        self.assertEqual(replay("kṛ", "luṅ", "3s", "P"), "akārṣīt"); self.assertEqual(replay("kṛ", "lṛṅ", "3s", "A"), "akariṣyata")
        self.assertEqual(replay("bhū", "luṅ", "3s", "P", AUGMENT_ROWS), "bhūt"); self.assertEqual(replay("kṛ", "laṅ", "1s", "A", AUGMENT_ROWS), "kurvi"); self.assertEqual(replay("bhū", "laṅ", "3s", "P", AUGMENT_ROWS), "bhavat")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PG_MODAL_REGISTERS_II_CANDIDATE")
        t = payload["totals"]
        self.assertEqual((t["positions"], t["replayed"] + t["replayed_under_6.4.74_augment_rows_withheld"], t["agree"], t["to_adjudicate"], t["adjudicated"]), (999, 981, 981, 0, 0))
        self.assertEqual(t["replayed_under_6.4.74_augment_rows_withheld"], 144)
        self.assertEqual(payload["adjudicated"], {})   # theorum/158: the table corrected, the ten śās cells agree
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
