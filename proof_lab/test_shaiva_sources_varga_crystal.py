from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.shaiva_sources_nativized import TOKENS, compose, omega_bilinear
from proof_lab.shaiva_sources_varga_crystal import MANNER, VARGAS, _sets_under, build_certificate, canonical_bytes, certificate_sha256

EXPECTED = Path(__file__).with_name("SHAIVA_SOURCES_VARGA_CRYSTAL_EXPECTED.sha256")


class ShaivaSourcesVargaCrystalTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("shaiva_sources_varga_crystal.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_grid_is_a_bijection(self) -> None:
        stops = [s for row in MANNER.values() for s in row]
        self.assertEqual(len(stops), 25)
        self.assertEqual(set(stops), {s for col in VARGAS.values() for s in col})
        for col in VARGAS.values():
            self.assertEqual(len(set(col) & set(stops)), 5)

    def test_swapping_j_and_b_changes_jas(self) -> None:
        order = list(TOKENS)
        i, k = order.index("j"), order.index("b")
        order[i], order[k] = order[k], order[i]
        self.assertNotEqual(_sets_under(order), _sets_under(TOKENS))

    def test_symmetric_cocycle_is_a_coboundary(self) -> None:
        S = ((2, 1), (1, 4))
        alpha = lambda a: omega_bilinear(S, a, a) / 2
        for a in [(1, 0), (0, 1), (2, 3)]:
            for b in [(1, 1), (3, 0), (0, 2)]:
                self.assertEqual(omega_bilinear(S, b, a), alpha(compose(b, a)) - alpha(b) - alpha(a))
        self.assertEqual(alpha((1, 1)), Fraction(4))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_SHAIVA_SOURCES_VARGA_CRYSTAL_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
