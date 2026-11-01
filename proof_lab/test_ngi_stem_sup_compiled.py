from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.ngi_stem_sup_compiled import NADI_ORACLE, build_certificate, canonical_bytes, certificate_sha256, load_entries, paradigm, trc_agent

EXPECTED = Path(__file__).with_name("NGI_STEM_SUP_COMPILED_EXPECTED.sha256")


class NgiStemSupCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("ngi_stem_sup_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_nadi_and_kartri(self) -> None:
        self.assertEqual(paradigm(("n", "a", "d", "ī")), NADI_ORACLE)
        e = load_entries()
        self.assertEqual(trc_agent("1080010", e)["feminine"], "kartrī")
        self.assertEqual(trc_agent("1050001", e)["agent"], "sotṛ")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_NGI_STEM_SUP_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
