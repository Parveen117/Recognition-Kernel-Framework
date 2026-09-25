from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.local_to_uniform_seam_gap import (
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    cut_grade,
    face,
    face_hypotheses,
    heterogeneous_faces,
    is_psd_exact,
    is_zero,
    matmul,
    matrix,
    norm_le,
    product_data,
    scale,
    sheet_projector,
    t2_uniform_gap,
    t7_controls,
)

EXPECTED = Path(__file__).with_name("LOCAL_TO_UNIFORM_SEAM_GAP_EXPECTED.sha256")


class LocalToUniformSeamGapTests(unittest.TestCase):
    def test_exact_psd_and_norm_certifier(self) -> None:
        self.assertFalse(is_psd_exact(matrix(((1, 2), (2, 1)))))
        self.assertTrue(is_psd_exact(matrix(((0, 0), (0, 1)))))
        self.assertFalse(is_psd_exact(matrix(((0, 1), (1, 1)))))
        b = matrix(((Fraction(1), Fraction(1, 2)), (Fraction(0), Fraction(1))))
        # ||b||^2 = (9 + sqrt(17))/8 ~ 1.640; 5/4 must be rejected, 13/10 accepted
        self.assertFalse(norm_le(b, Fraction(5, 4)))
        self.assertTrue(norm_le(b, Fraction(13, 10)))

    def test_face_hypotheses_fail_closed(self) -> None:
        fc, W, lam = heterogeneous_faces()[0]
        good = face_hypotheses(fc, W, lam)
        self.assertTrue(all(v for v in good.values() if isinstance(v, bool)))
        # planted negative: halve the admitted contraction -> H2 must fail
        bad = face_hypotheses(fc, W, lam / 2)
        self.assertFalse(bad["H2_memory_contraction_certified"])

    def test_uniform_gap_rejects_planted_smaller_rho(self) -> None:
        faces = [fc for fc, _, _ in heterogeneous_faces()[:3]]
        ok = t2_uniform_gap(faces, Fraction(3, 8))
        self.assertTrue(all(ok["checks"].values()))
        # the binding face has rho = 3/8 with ||B|| > 1.28 > 5/4: rho = 5/16 must be refused
        bad = t2_uniform_gap(faces, Fraction(5, 16))
        self.assertFalse(bad["checks"]["memory_sheet_contraction_certified_on_full_product"])

    def test_sheet_law_is_a_product_law(self) -> None:
        f1 = face(Fraction(3), matrix(((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1, 2)))))
        f2 = face(Fraction(2), matrix(((Fraction(1, 2),),)))
        pd = product_data([f1, f2])
        minus_minus = sheet_projector([f1, f2], (-1, -1))
        block = matmul(matmul(minus_minus, pd["L"]), minus_minus)
        # rho^2 f0^m = (1/3)^2 * 6 = 2/3 ; the block's top diagonal value is 1*1/2 = 1/2 <= 2/3
        self.assertTrue(norm_le(block, Fraction(2, 3)))
        self.assertFalse(norm_le(block, Fraction(1, 3)))

    def test_leaking_face_is_not_even(self) -> None:
        leak = {"L": matrix(((2, 1), (0, Fraction(1, 2)))), "J": matrix(((1, 0), (0, -1))), "f0": Fraction(2)}
        even, odd = cut_grade(leak["L"], leak["J"])
        self.assertFalse(is_zero(odd))
        self.assertTrue(all(t7_controls()["checks"].values()))

    def test_certificate_status_and_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_LOCAL_TO_UNIFORM_SEAM_GAP_CANDIDATE")
        self.assertTrue(all(payload["checks"].values()))
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
