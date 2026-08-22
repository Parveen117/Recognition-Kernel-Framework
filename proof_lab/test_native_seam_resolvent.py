from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.native_seam_gap_odd_covariance import eye, mass, mat, sc, star
from proof_lab.native_seam_resolvent import (
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    charpoly,
    det,
    inverse,
    lam_I_minus,
    partial_resolvent,
    poly_eval,
    q_ratio,
    tail_budget,
)

EXPECTED = Path(__file__).with_name("NATIVE_SEAM_RESOLVENT_EXPECTED.sha256")


class NativeSeamResolventTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("native_seam_resolvent.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float("):
            self.assertNotIn(forbidden, src)

    def test_charpoly_is_det_lambda_minus_L(self) -> None:
        L = mat([[sc(1, 1), sc(2, 0)], [sc(0, 1), sc(-1, 0)]])
        cp = charpoly(L)
        for lam in (sc(0), sc(1, 1), sc(Fraction(3, 2), -2)):
            self.assertEqual(poly_eval(cp, lam), det(lam_I_minus(L, lam)))

    def test_tail_budget_fails_closed(self) -> None:
        L = mat([[sc(1, 0), sc(0, 1)], [sc(0, 0), sc(1, 0)]])
        lam = sc(4, 1)
        q = q_ratio(L, lam)
        self.assertLess(q, 1)
        Rex = inverse(lam_I_minus(L, lam))
        self.assertEqual(star(lam_I_minus(L, lam), Rex), eye(2))
        for N in range(5):
            self.assertLessEqual(mass(tuple(tuple((x[0] - y[0], x[1] - y[1]) for x, y in zip(r1, r2)) for r1, r2 in zip(Rex, partial_resolvent(L, lam, N)))), tail_budget(L, lam, N, q))
        # a budget declared with too-small q must be violated at N = 0
        tight = tail_budget(L, lam, 0, q / 4)
        self.assertGreater(mass(tuple(tuple((x[0] - y[0], x[1] - y[1]) for x, y in zip(r1, r2)) for r1, r2 in zip(Rex, partial_resolvent(L, lam, 0)))), tight)

    def test_singular_exactly_at_recognized_value(self) -> None:
        L = mat([[sc(4, 0), 0, 0], [0, sc(1, Fraction(1, 2)), sc(0, 1)], [0, 0, sc(1, 0)]])
        self.assertEqual(det(lam_I_minus(L, sc(4, 0))), (Fraction(0), Fraction(0)))
        self.assertNotEqual(det(lam_I_minus(L, sc(3, 0))), (Fraction(0), Fraction(0)))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_NATIVE_SEAM_RESOLVENT_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
