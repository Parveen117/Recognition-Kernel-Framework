from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.first_visible_jet_seam_quotient import classify_finite_jets
from proof_lab.generalized_euler_emk_dock import I2, K, R, RK, loop
from proof_lab.loop_residue_first_visible_jet_binding import (
    DEPTH,
    a3_closed_form,
    build_certificate,
    canonical_bytes,
    cayley_jet,
    certificate_sha256,
    classify_residue,
    comm,
    emk_pair,
    first_visible_order,
    j_const,
    j_eval,
    j_mul,
    loop_jet,
    residue_jet,
)
from proof_lab.native_seam_gap_odd_covariance import eye, is_zero, m_add, m_scale, m_sub, mass, sc

EXPECTED = Path(__file__).with_name("LOOP_RESIDUE_FIRST_VISIBLE_JET_BINDING_EXPECTED.sha256")


class LoopResidueFirstVisibleJetBindingTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("loop_residue_first_visible_jet_binding.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "sympy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float(", "math.cos", "math.sin"):
            self.assertNotIn(forbidden, src)

    def test_cayley_jet_matches_exact_cayley_to_depth(self) -> None:
        # jets of C_h(D) agree with the exact rational Cayley step up to O(h^(DEPTH+1))
        D = m_scale(Fraction(3), R)
        Cj = cayley_jet(D)
        from proof_lab.odd_channel_exchange_law import cayley_unitary

        m1 = mass(m_sub(cayley_unitary(D, Fraction(1, 64)), j_eval(Cj, Fraction(1, 64))))
        m2 = mass(m_sub(cayley_unitary(D, Fraction(1, 128)), j_eval(Cj, Fraction(1, 128))))
        self.assertGreater(m1, 0)
        self.assertLessEqual(m2, m1 / 2 ** (DEPTH + 1))
        self.assertEqual(j_mul(Cj, cayley_jet(m_scale(-1, D))), j_const(eye(2)))

    def test_residue_is_46_seam_observable_with_bracket_quotient(self) -> None:
        D1, D2 = emk_pair(Fraction(2), Fraction(3))
        g = residue_jet(D1, D2)
        self.assertTrue(is_zero(g[0]))  # 46 (2.1)
        self.assertEqual(first_visible_order(g), 2)
        cls = classify_residue(g, 2)
        self.assertEqual(cls["verdict"], "FINITE_SEAM_QUOTIENT")
        self.assertEqual(cls["quotient"], comm(D1, D2))
        self.assertEqual(cls["quotient"], m_scale(sc(0, 12), RK))
        self.assertEqual(classify_residue(g, 1)["verdict"], "FINITE_QUOTIENT_ZERO")
        self.assertEqual(classify_residue(g, 3)["verdict"], "DIVERGENT_NO_FINITE_QUOTIENT")

    def test_46_classifier_is_the_one_consumed(self) -> None:
        # the (1,0) rad entry of Gamma for alpha=2, beta=3 is the scalar jet [0,0,0,36,...]; vs h^3 it is 36
        D1, D2 = emk_pair(Fraction(2), Fraction(3))
        g = residue_jet(D1, D2)
        rad_10 = [g[k][1][0][0] for k in range(DEPTH + 1)]
        cls = classify_finite_jets(rad_10, [0, 0, 0, 1, 0])
        self.assertEqual(cls.status, "FINITE_SEAM_QUOTIENT")
        self.assertEqual(cls.quotient, Fraction(36))

    def test_exact_order3_identity(self) -> None:
        D1, D2 = emk_pair(Fraction(2), Fraction(3))
        g = residue_jet(D1, D2)
        self.assertEqual(g[3], a3_closed_form(D1, D2))
        self.assertEqual(g[3], m_add(m_scale(36, R), m_scale(sc(0, -24), K)))
        self.assertFalse(is_zero(g[3]))

    def test_planted_false_residue_is_divergent(self) -> None:
        D1, D2 = emk_pair(Fraction(1), Fraction(-2))
        g = residue_jet(D1, D2)
        g[1] = m_scale(sc(0, 1), I2)
        self.assertEqual(classify_residue(g, 2)["verdict"], "DIVERGENT_NO_FINITE_QUOTIENT")

    def test_commuting_generators_loop_identity_and_zero_jets(self) -> None:
        D1 = R
        Dc = m_scale(sc(0, 4), I2)
        self.assertIsNone(first_visible_order(residue_jet(D1, Dc)))
        self.assertEqual(loop(D1, Dc, Fraction(3, 7)), eye(2))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_LOOP_RESIDUE_FIRST_VISIBLE_JET_BINDING_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
