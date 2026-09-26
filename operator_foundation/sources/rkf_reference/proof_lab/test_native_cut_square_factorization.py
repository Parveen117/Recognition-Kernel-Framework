from __future__ import annotations

import hashlib
import random
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.native_cut_square_factorization import build_certificate, canonical_bytes, certificate_sha256, ldl_native, quad, reconstruct
from proof_lab.native_seam_gap_odd_covariance import cut_square, mat, sc, turn_part
from proof_lab.odd_channel_exchange_law import random_operator

EXPECTED = Path(__file__).with_name("NATIVE_CUT_SQUARE_FACTORIZATION_EXPECTED.sha256")


class NativeCutSquareFactorizationTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("native_cut_square_factorization.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float(", "sqrt"):
            self.assertNotIn(forbidden, src)

    def test_factorization_exact_and_weights_turn_free(self) -> None:
        S = cut_square(random_operator(4, random.Random(2)))
        fac = ldl_native(S)
        self.assertEqual(reconstruct(fac), S)
        self.assertTrue(all(fac["Dg"][i][i][1] == 0 and fac["Dg"][i][i][0] >= 0 for i in range(4)))

    def test_not_self_dagger_refused(self) -> None:
        with self.assertRaises(AssertionError):
            ldl_native(mat([[sc(1, 0), sc(1, 0)], [sc(0, 0), sc(1, 0)]]))

    def test_negative_witness_is_exact(self) -> None:
        T = mat([[sc(0, 0), sc(1, 0)], [sc(1, 0), sc(0, 0)]])
        # zero pivot with nonzero row: not a cut square, must be refused rather than silently passed
        with self.assertRaises(AssertionError):
            ldl_native(T)
        T2 = mat([[sc(1, 0), sc(3, 0)], [sc(3, 0), sc(1, 0)]])
        fac = ldl_native(T2)
        self.assertTrue(any(w < 0 for w in fac["weights"]))
        self.assertLess(quad(T2, fac["witness"])[0], 0)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_NATIVE_CUT_SQUARE_FACTORIZATION_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
