from __future__ import annotations

import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.canvas_operators_nativized import (
    b4_aghora,
    bindu,
    build_certificate,
    certificate_sha256,
    guna,
    lopa,
    lopa_k,
    normal_forms,
    yan,
    yan_k,
)
from proof_lab.local_to_uniform_seam_gap import is_psd_exact, matrix

EXPECTED = Path(__file__).with_name("CANVAS_OPERATORS_NATIVIZED_EXPECTED.sha256")


class CanvasOperatorsNativizedTests(unittest.TestCase):
    def test_bindu_lopa_seam_alphabet(self) -> None:
        a, b = Fraction(3), Fraction(4)
        c1 = lopa(*bindu(a, b))                 # (3/5, 0)
        self.assertEqual(c1, (Fraction(3, 5), Fraction(0)))
        c2 = lopa(*bindu(*c1))                  # (1, 0)
        self.assertEqual(c2, (Fraction(1), Fraction(0)))
        self.assertEqual(lopa(*bindu(*c2)), c2)
        self.assertNotEqual(bindu(*lopa(a, b)), c1)   # non-commutation

    def test_panini_precedence_and_blindness(self) -> None:
        self.assertNotEqual(yan(guna("aia")), guna(yan("aia")))
        self.assertEqual(len(normal_forms("aia", [guna, yan])), 2)
        self.assertEqual(lopa_k(yan_k("Kiu")), "yu")
        self.assertEqual(yan_k("iu"), "iu")
        self.assertEqual(yan_k(lopa_k("Kiu")), "iu")

    def test_aghora_refusal_is_not_vacuous(self) -> None:
        out = b4_aghora()
        self.assertGreater(out["anticommuting_count"], 1)
        self.assertTrue(out["checks"]["REFUSAL_psd_plus_anticommuting_forces_G_zero"])
        # planted: an off-diagonal symmetric G is anticommuting but NOT psd
        self.assertFalse(is_psd_exact(matrix(((0, 2), (2, 0)))))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_CANVAS_OPERATORS_NATIVIZED_CANDIDATE")
        self.assertEqual(certificate_sha256(payload), EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
