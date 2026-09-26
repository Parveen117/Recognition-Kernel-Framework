from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.prime_letter_operators import (
    build_certificate,
    canonical_bytes,
    cayley_jet_scalar,
    certificate_sha256,
    exp_jet_scalar,
    l_add,
    l_neg,
    load_f00h,
    mass1,
)
from proof_lab.loop_residue_first_visible_jet_binding import first_visible_order, j_const, j_mul, j_sub
from proof_lab.native_seam_gap_odd_covariance import eye

EXPECTED = Path(__file__).with_name("PRIME_LETTER_OPERATORS_EXPECTED.sha256")


class PrimeLetterOperatorsTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("prime_letter_operators.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float(", "math.log", "math.cos"):
            self.assertNotIn(forbidden, src)

    def test_ledger_dagger_law_and_canvas_disproof(self) -> None:
        self.assertEqual(l_add({2: 1}, l_neg({3: 1})), {2: 1, 3: -1})
        self.assertNotEqual(l_add({2: 1}, l_neg({3: 1})), l_neg({2: 1, 3: 1}))
        f = load_f00h()
        self.assertEqual(mass1(dict(f.factor_integer(97))), 1)
        self.assertEqual(mass1(dict(f.factor_integer(96))), 6)

    def test_exp_exact_and_cayley_order3(self) -> None:
        x, y = Fraction(1, 2), Fraction(3)
        self.assertEqual(j_mul(exp_jet_scalar(x), exp_jet_scalar(y)), exp_jet_scalar(x + y))
        gamma = j_sub(j_mul(j_mul(cayley_jet_scalar(x), cayley_jet_scalar(y)), cayley_jet_scalar(-(x + y))), j_const(eye(1)))
        self.assertEqual(first_visible_order(gamma), 3)
        self.assertEqual(gamma[3][0][0], (Fraction(0), x * y * (x + y) / 4))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_PRIME_LETTER_OPERATORS_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
