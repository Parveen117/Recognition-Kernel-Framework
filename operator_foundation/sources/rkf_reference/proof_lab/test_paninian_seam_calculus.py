from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.paninian_seam_calculus import (
    GAM,
    NI,
    SANDHI,
    G,
    V,
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    derive,
    free_normal_forms,
    priority_normal_form,
    recognized,
)

EXPECTED = Path(__file__).with_name("PANINIAN_SEAM_CALCULUS_EXPECTED.sha256")


class PaninianSeamCalculusTests(unittest.TestCase):
    def test_no_hilbert_and_no_hardcoded_verdicts(self) -> None:
        src = Path(__file__).with_name("paninian_seam_calculus.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "float(", ": True,\n", "\": True}"):
            self.assertNotIn(forbidden, src)

    def test_vowel_semilattice(self) -> None:
        self.assertEqual((G("i"), V("i"), V(G("i")), G(V("i"))), ("e", "ai", "ai", "ai"))
        self.assertEqual(G(G("u")), G("u"))

    def test_i_plus_i_ambiguous_free_unique_under_priority(self) -> None:
        rules = [r for _, r in SANDHI]
        self.assertEqual(free_normal_forms(("i", "i"), rules), {("y", "i"), ("I",)})
        self.assertEqual(priority_normal_form(("i", "i"), SANDHI), ("I",))
        self.assertEqual(priority_normal_form(("a", "i"), SANDHI), ("e",))

    def test_canonical_derivations_and_memory_control(self) -> None:
        self.assertEqual(recognized(derive(GAM)), "gacchati")
        self.assertEqual(recognized(derive(NI)), "nayati")
        self.assertEqual(recognized(derive(GAM, carry_memory=False)), "gamati")
        self.assertEqual(recognized(derive(GAM, carry_memory=False, lopa_last=True)), "gacchati")
        self.assertEqual(recognized(derive(GAM, lopa_last=True)), "gacchati")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PANINIAN_SEAM_CALCULUS_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
