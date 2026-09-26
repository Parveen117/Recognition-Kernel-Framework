from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.karaka_vibhakti_carrier import GAYATRI_L1, PASSIVE_L1, assign, build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("KARAKA_VIBHAKTI_CARRIER_EXPECTED.sha256")


class KarakaVibhaktiCarrierTests(unittest.TestCase):
    def test_ledger_flip(self) -> None:
        self.assertEqual(assign(GAYATRI_L1)["bhargas"]["vibhakti"], 2)
        self.assertEqual(assign(PASSIVE_L1)["bhargas"]["vibhakti"], 1)
        self.assertEqual(assign(PASSIVE_L1)["asmad"]["vibhakti"], 3)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_KARAKA_VIBHAKTI_CARRIER_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
