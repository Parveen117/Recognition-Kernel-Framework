from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.krt_rule_table_engine import IDS, RULES, SOURCES, build_certificate, canonical_bytes, certificate_sha256, derive, norm_id

EXPECTED = Path(__file__).with_name("KRT_RULE_TABLE_ENGINE_EXPECTED.sha256")


class T151Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("krt_rule_table_engine.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_every_row_is_a_quoted_sutra(self) -> None:
        for n in IDS:
            self.assertIn(norm_id(n), SOURCES, n)
        self.assertEqual(len(IDS), len(set(IDS)))
        self.assertEqual(len(RULES), len(IDS))

    def test_classic_forms(self) -> None:
        for (r, a), exp in {("bhū", "kta"): "bhūta", ("bhū", "tumun"): "bhavitum", ("bhū", "ṇvul"): "bhāvaka", ("kṛ", "kta"): "kṛta", ("kṛ", "tṛc"): "kartṛ", ("kṛ", "anīya"): "karaṇīya",
                            ("gam", "kta"): "gata", ("gam", "tavya"): "gantavya", ("dā", "kta"): "datta", ("dhā", "kta"): "hita", ("labh", "kta"): "labdha", ("bhid", "kta"): "bhinna",
                            ("lih2", "kta"): "līḍha", ("duh2", "kta"): "dugdha", ("vac2", "kta"): "ukta", ("svap2", "kta"): "supta", ("grah9", "kta"): "gṛhīta", ("pac", "ṇvul"): "pācaka",
                            ("han2", "ṇvul"): "ghātaka", ("śī2A", "kta"): "śayita", ("cur", "kta"): "corita", ("cur", "tumun"): "corayitum", ("kṝ9", "kta"): "kīrṇa", ("pṝ3", "kta"): "pūrta",
                            ("nī", "ṇvul"): "nāyaka", ("div", "kta"): "dyūta", ("hā3", "kta"): "hīna", ("as", "kta"): "bhūta", ("jāgṛ2", "ṇvul"): "jāgaraka",
                            ("bhū", "śatṛ"): "bhavat", ("kṛ", "śatṛ"): "kurvat", ("kṛ", "śānac"): "kurvāṇa", ("han2", "śatṛ"): "ghnat", ("as", "śatṛ"): "sat", ("hu", "śatṛ"): "juhvat",
                            ("krī", "śānac"): "krīṇāna", ("edh", "śānac"): "edhamāna", ("śī2A", "śānac"): "śayāna", ("ās2A", "śānac"): "āsīna", ("bhā2", "śatṛ"): "bhāt"}.items():
            self.assertEqual(derive(r, a)[0], exp, (r, a))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_KRT_RULE_TABLE_ENGINE_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
