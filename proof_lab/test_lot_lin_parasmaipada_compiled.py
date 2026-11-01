from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.lot_lin_parasmaipada_compiled import BHU, LIN, LIN_STAGES, LOT, LOT_STAGES, build_certificate, canonical_bytes, certificate_sha256, lin, lot, paradigm, present_stem

EXPECTED = Path(__file__).with_name("LOT_LIN_PARASMAIPADA_COMPILED_EXPECTED.sha256")


class LotLinParasmaipadaCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("lot_lin_parasmaipada_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_forms(self) -> None:
        s = present_stem(BHU)
        self.assertEqual(paradigm(lot, s, LOT_STAGES), LOT["bhū"])
        self.assertEqual(paradigm(lin, s, LIN_STAGES), LIN["bhū"])

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_LOT_LIN_PARASMAIPADA_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
