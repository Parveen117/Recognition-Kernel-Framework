from __future__ import annotations

import unittest

from proof_lab.ladder_audit_50_59 import build_certificate


class LadderAuditTests(unittest.TestCase):
    def test_all_planted_negatives_rejected_and_rederivations_agree(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_LADDER_AUDIT_50_59")
        self.assertGreaterEqual(payload["summary"]["cert_defects"], 4)

    def test_fixed_pins_are_live(self) -> None:
        import hashlib
        from pathlib import Path

        from proof_lab import canvas_operators_nativized, infinite_face_recognition_completion, native_seam_resolvent, paninian_seam_calculus

        for mod, name in ((canvas_operators_nativized, "CANVAS_OPERATORS_NATIVIZED"), (infinite_face_recognition_completion, "INFINITE_FACE_RECOGNITION_COMPLETION"), (native_seam_resolvent, "NATIVE_SEAM_RESOLVENT"), (paninian_seam_calculus, "PANINIAN_SEAM_CALCULUS")):
            digest = hashlib.sha256(mod.canonical_bytes(mod.build_certificate())).hexdigest()
            self.assertEqual(digest, Path(__file__).with_name(f"{name}_EXPECTED.sha256").read_text().strip())


if __name__ == "__main__":
    unittest.main()
