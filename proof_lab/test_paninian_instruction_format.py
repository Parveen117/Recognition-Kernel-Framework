from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.paninian_instruction_format import (
    GUNA_SET,
    SANDHI_RECORDS,
    VRDDHI_SET,
    antaratama,
    antaratama_winners,
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    compile_sandhi,
    rapara_1_1_51,
    scu_of,
)

EXPECTED = Path(__file__).with_name("PANINIAN_INSTRUCTION_FORMAT_EXPECTED.sha256")


class PaninianInstructionFormatTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("paninian_instruction_format.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_compiled_sandhi_examples(self) -> None:
        rules = {rec["sid"]: compile_sandhi(rec) for rec in SANDHI_RECORDS}
        self.assertEqual(rules["6.1.77"](("i", "a")), ("y", "a"))  # iti + api -> ityapi
        self.assertEqual(rules["6.1.77"](("I", "a")), ("y", "a"))  # nadī + ā : 1.1.69 savarṇa
        self.assertEqual(rules["6.1.78"](("e", "a")), ("ay", "a"))
        self.assertEqual(rules["6.1.87"](("a", "i")), ("e",))  # 6.1.84 ekādeśa
        self.assertEqual(rules["6.1.87"](("A", "U")), ("o",))
        self.assertEqual(rules["6.1.88"](("a", "e")), ("ai",))
        self.assertEqual(rules["6.1.101"](("i", "I")), ("I",))
        self.assertIsNone(rules["6.1.101"](("i", "u")))
        self.assertIsNone(rules["6.1.77"](("e", "a")))

    def test_antaratama_and_rapara(self) -> None:
        self.assertEqual(antaratama("i", GUNA_SET), "e")
        self.assertEqual(antaratama("u", GUNA_SET), "o")
        self.assertEqual(rapara_1_1_51("R", antaratama("R", GUNA_SET)), "ar")
        self.assertEqual(antaratama("e", VRDDHI_SET), "ai")
        self.assertEqual(len(antaratama_winners("L", ("y", "v", "r", "l"))), 1)

    def test_scutva_from_the_manner_grid(self) -> None:
        self.assertEqual(scu_of("t"), "c")
        self.assertEqual(scu_of("dh"), "jh")
        self.assertEqual(scu_of("s"), "S")

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PANINIAN_INSTRUCTION_FORMAT_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
