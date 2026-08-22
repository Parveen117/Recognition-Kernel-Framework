from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.native_seam_gap_odd_covariance import (
    build_certificate,
    canonical_bytes,
    cayley_step,
    certificate_sha256,
    cut_square,
    dagger,
    energy,
    face_hypotheses,
    flip_orientation,
    instance_faces,
    kron,
    mass,
    mat,
    rad_part,
    real_kron,
    real_sub,
    sc,
    star,
    turn_part,
)

EXPECTED = Path(__file__).with_name("NATIVE_SEAM_GAP_ODD_COVARIANCE_EXPECTED.sha256")


class NativeSeamGapOddCovarianceTests(unittest.TestCase):
    def test_scalar_carrier_is_cut_complex(self) -> None:
        iota = mat([[sc(0, 1)]])
        self.assertEqual(star(iota, iota), mat([[sc(-1, 0)]]))
        self.assertEqual(dagger(iota), mat([[sc(0, -1)]]))
        self.assertEqual(energy(iota), Fraction(1))
        self.assertEqual(mass(iota), Fraction(1))

    def test_no_hilbert_verdict_anywhere(self) -> None:
        src = Path(__file__).with_name("native_seam_gap_odd_covariance.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float("):
            self.assertNotIn(forbidden, src)

    def test_h2_mass_fails_closed(self) -> None:
        fc = instance_faces()[0]  # memory mass 5/4, f0 = 4
        self.assertTrue(face_hypotheses(fc, Fraction(1, 2))["H2_mass_contraction"])
        self.assertFalse(face_hypotheses(fc, Fraction(1, 4))["H2_mass_contraction"])

    def test_flow_generated_smoothing(self) -> None:
        D = mat([[0, sc(0, 1)], [0, 0]])
        C = cayley_step(D, Fraction(1, 2))
        self.assertEqual(C, mat([[1, sc(0, Fraction(1, 2))], [0, 1]]))  # D^2 = 0 -> C_h = I + hD
        with self.assertRaises(AssertionError):
            cayley_step(mat([[1, 0], [0, 1]]), Fraction(1))

    def test_even_feedback_is_negative_and_nonzero(self) -> None:
        fa, fb = instance_faces()[:2]
        Sa, Sb = cut_square(fa["L"]), cut_square(fb["L"])
        Sab = cut_square(kron(fa["L"], fb["L"]))
        tt = real_kron(turn_part(Sa), turn_part(Sb))
        minus = real_sub(real_kron(rad_part(Sa), rad_part(Sb)), tt)
        self.assertEqual(rad_part(Sab), minus)
        plus = tuple(tuple(x + 2 * y for x, y in zip(r1, r2)) for r1, r2 in zip(minus, tt))
        self.assertNotEqual(rad_part(Sab), plus)

    def test_orientation_covariance(self) -> None:
        fa = instance_faces()[0]
        S, Sf = cut_square(fa["L"]), cut_square(flip_orientation(fa["L"]))
        self.assertEqual(rad_part(S), rad_part(Sf))
        self.assertEqual(turn_part(S), tuple(tuple(-x for x in row) for row in turn_part(Sf)))
        self.assertTrue(any(x != 0 for row in turn_part(S) for x in row))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_NATIVE_SEAM_GAP_ODD_COVARIANCE_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
