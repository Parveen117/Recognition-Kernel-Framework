from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.paninian_samjna_sound_layer import VOWELS_IAST, build_certificate, canonical_bytes, certificate_sha256, savarna_classes, tadanta_1_1_72, ti_1_1_64, upadha_1_1_65

EXPECTED = Path(__file__).with_name("PANINIAN_SAMJNA_SOUND_LAYER_EXPECTED.sha256")


class PaninianSamjnaSoundLayerTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("paninian_samjna_sound_layer.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_savarna_examples(self) -> None:
        classes = savarna_classes(VOWELS_IAST + ("k", "kh", "g", "gh", "ṅ", "ś", "h"))
        self.assertIn(frozenset({"k", "kh", "g", "gh", "ṅ"}), classes)
        self.assertIn(frozenset({"a", "ā"}), classes)
        self.assertNotIn(frozenset({"e", "ai"}), classes)

    def test_selectors(self) -> None:
        self.assertEqual(ti_1_1_64(("r", "ā", "m", "a")), ("a",))
        self.assertEqual(upadha_1_1_65(("r", "ā", "m", "a")), "m")
        self.assertTrue(tadanta_1_1_72(("n", "I"), ("i", "I", "u", "U")))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PANINIAN_SAMJNA_SOUND_LAYER_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
