from __future__ import annotations

import hashlib
import itertools
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.infinite_face_recognition_completion import build_certificate, canonical_bytes, certificate_sha256, geometric_faces, normalized_face, word_mass

EXPECTED = Path(__file__).with_name("INFINITE_FACE_RECOGNITION_COMPLETION_EXPECTED.sha256")


class InfiniteFaceTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("infinite_face_recognition_completion.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float(", "math.exp"):
            self.assertNotIn(forbidden, src)

    def test_geometric_faces_have_declared_mu(self) -> None:
        faces = geometric_faces(Fraction(1, 3), Fraction(1, 2), 5)
        self.assertEqual([fc["mu"] for fc in faces], [Fraction(1, 3) * Fraction(1, 2) ** i for i in range(1, 6)])

    def test_word_mass_is_product_and_memory_words_bounded(self) -> None:
        faces = geometric_faces(Fraction(1, 2), Fraction(1, 2), 4)
        rho = max(fc["mu"] for fc in faces)
        for w in itertools.product((1, -1), repeat=4):
            if any(s == -1 for s in w):
                self.assertLessEqual(word_mass(faces, w), rho)
        self.assertEqual(word_mass(faces, (1, 1, 1, 1)), Fraction(1))

    def test_constant_mu_increments_diverge(self) -> None:
        rho = Fraction(1, 2)
        incs = [((1 + rho) ** n) * rho for n in range(1, 8)]
        self.assertTrue(all(b > a for a, b in zip(incs, incs[1:])))
        self.assertGreater(incs[-1], 1)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_INFINITE_FACE_RECOGNITION_COMPLETION_CANDIDATE")
        self.assertIn("NOT APPLICABLE", payload["theorum_28_section_11_ledger"]["4_target_faithfulness_residual"])
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
