from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.dabas_euler_emk_dock import I2, K, R, RK, build_certificate, canonical_bytes, certificate_sha256, emk, is_anti_self_dagger, loop
from proof_lab.native_seam_gap_odd_covariance import eye, m_scale, sc, star
from proof_lab.native_seam_resolvent import det
from proof_lab.native_seam_gap_odd_covariance import cut_square

EXPECTED = Path(__file__).with_name("DABAS_EULER_EMK_DOCK_EXPECTED.sha256")


class DabasEulerEmkDockTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("dabas_euler_emk_dock.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float(", "math.cos", "math.sin"):
            self.assertNotIn(forbidden, src)

    def test_emk_relations_and_generator_types(self) -> None:
        self.assertEqual(star(R, R), m_scale(-1, I2))
        self.assertEqual(star(K, K), I2)
        self.assertTrue(is_anti_self_dagger(R))
        self.assertFalse(is_anti_self_dagger(K))
        self.assertTrue(is_anti_self_dagger(m_scale(sc(0, 1), K)))

    def test_determinant_identity_is_squared_total(self) -> None:
        M = emk(Fraction(2), Fraction(1), Fraction(3), Fraction(-1))
        self.assertEqual(det(cut_square(M)), sc((4 - 1 + 9 - 1) ** 2))

    def test_commuting_loop_is_identity_and_noncommuting_is_not(self) -> None:
        self.assertEqual(loop(R, m_scale(sc(0, 2), I2), Fraction(1, 2)), eye(2))
        self.assertNotEqual(loop(R, m_scale(sc(0, 2), K), Fraction(1, 2)), eye(2))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_DABAS_EULER_EMK_DOCK_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
