from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.panini_isa import OPS, build_certificate, canonical_bytes, certificate_sha256, classify_firing, splice

EXPECTED = Path(__file__).with_name("PANINI_ISA_EXPECTED.sha256")


class T150Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("panini_isa.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_splice_and_classes(self) -> None:
        self.assertEqual(splice(list("bhav"), list("bhāv")), (2, ["a"], ["ā"]))
        seg = ("ag", "ab", "r", "it", "v", "pre", "aff")
        def st(**kw):
            d = {k: [] for k in seg} | {"flags": set(), "pit": False, "vsit": False, "gana": 1, "up_root": ""}
            return d | {k: list(v) if isinstance(v, str) else v for k, v in kw.items()}
        self.assertEqual(classify_firing(st(r="bhū"), st(r="bho"), seg), ["GUṆA"])          # 7.3.84
        self.assertEqual(classify_firing(st(r="bhū"), st(r="bhau"), seg), ["VṚDDHI"])        # 7.2.115
        self.assertEqual(classify_firing(st(r="his"), st(r="hins"), seg), ["ĀGAMA-MIT"])     # 7.1.58
        self.assertEqual(classify_firing(st(r="bhū"), st(ag="a", r="bhū"), seg), ["PRATYAYA"])   # 6.4.71's aṭ as the ag segment
        self.assertEqual(classify_firing(st(aff="ti"), st(aff="ati"), seg), ["ĀGAMA-ĀDI"])
        self.assertEqual(classify_firing(st(aff="ti"), st(aff=""), seg), ["LOPA"])          # 6.1.68
        self.assertEqual(classify_firing(st(r="as"), st(r="bhū"), seg), ["SARVĀDEŚA"])      # 2.4.52
        self.assertEqual(classify_firing(st(r="han"), st(r="hat"), seg), ["ANTYĀDEŚA"])
        self.assertEqual(classify_firing(st(r="bhū"), st(ab="bu", r="bhū"), seg), ["DVITVA"])   # 6.1.8
        self.assertEqual(classify_firing(st(r="bhav", aff="i"), st(r="bhav", aff="i", flags={"x"}), seg), ["SAṀJÑĀ"])
        self.assertEqual(classify_firing(st(v="a", aff="anti"), st(v="", aff="anti"), seg), ["LOPA"])      # 6.1.97
        self.assertEqual(classify_firing(st(v="a", pre="iy"), st(v="", pre="ey"), seg), ["SANDHI"])       # 6.1.87 at the boundary (a + iy → ey)
        self.assertEqual(classify_firing(st(r="ne"), st(r="nay"), seg), ["ANTYĀDEŚA"])                   # 6.1.78: ay for the final e (1.1.52)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PANINI_ISA_CANDIDATE")
        self.assertTrue(all(payload["checks"].values()))
        self.assertEqual(set(payload["operation_types_used"]), set(OPS))
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
