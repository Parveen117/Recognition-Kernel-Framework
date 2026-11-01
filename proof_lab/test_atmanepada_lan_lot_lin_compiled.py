from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.atmanepada_lan_lot_lin_compiled import LAN, LAN_STAGES, LIN, LIN_STAGES, LOT, LOT_STAGES, build_certificate, canonical_bytes, certificate_sha256, lan, lin, lot, paradigm

EXPECTED = Path(__file__).with_name("ATMANEPADA_LAN_LOT_LIN_COMPILED_EXPECTED.sha256")


class AtmanepadaLanLotLinCompiledTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("atmanepada_lan_lot_lin_compiled.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_forms(self) -> None:
        self.assertEqual(paradigm(lan, "edh", LAN_STAGES), LAN["edh"])
        self.assertEqual(paradigm(lot, "labh", LOT_STAGES), LOT["labh"])
        self.assertEqual(paradigm(lin, "labh", LIN_STAGES), LIN["labh"])

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_ATMANEPADA_LAN_LOT_LIN_COMPILED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
