from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from proof_lab.pg_replay import OPTIONS, SOURCES, build_certificate, canonical_bytes, certificate_sha256, same

EXPECTED = Path(__file__).with_name("PG_REPLAY_EXPECTED.sha256")


class T154Tests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("pg_replay.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_options_are_quoted(self) -> None:
        for lid, note in OPTIONS.items():
            self.assertIn(note.split(" ")[0], SOURCES, lid)
        self.assertTrue(same("haṁsi", "haṃsi")); self.assertFalse(same("hanti", "hansi"))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PG_REPLAY_CANDIDATE")
        self.assertEqual(payload["rules"]["not_in_pinned_edition"], [])
        self.assertEqual(payload["rules"]["text_mismatch"], [])
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
