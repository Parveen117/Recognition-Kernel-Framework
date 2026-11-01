from __future__ import annotations

import hashlib
import itertools
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.generalized_euler_emk_dock import I2, R
from proof_lab.native_seam_gap_odd_covariance import dagger, star
from proof_lab.shaiva_sources_nativized import (
    SIX,
    TOKENS,
    USED,
    _atoms,
    _interval_order_exists,
    _six_sets,
    build_certificate,
    canonical_bytes,
    certificate_sha256,
    omega_bilinear,
    path_memory,
    pratyahara,
)

EXPECTED = Path(__file__).with_name("SHAIVA_SOURCES_NATIVIZED_EXPECTED.sha256")


class ShaivaSourcesNativizedTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("shaiva_sources_nativized.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_maheshvara_intervals(self) -> None:
        # 1.1.71 on the fourteen sūtras: the classical sets, read off the token order
        self.assertEqual(pratyahara("i", 1), ("i", "u", "ṛ", "ḷ"))
        self.assertEqual(pratyahara("a", 3), ("a", "i", "u", "ṛ", "ḷ", "e", "o", "ai", "au"))
        self.assertEqual(pratyahara("y", 5), ("y", "v", "r", "l"))
        self.assertEqual(pratyahara("ś", 12), ("ś", "ṣ", "s"))
        self.assertEqual(len(TOKENS), 43)
        self.assertEqual(TOKENS.count("h"), 2)
        self.assertEqual(len(USED), 42)

    def test_repeated_h_is_necessary(self) -> None:
        one_h = _six_sets(split_h=False)
        atoms = _atoms(sorted(set(TOKENS)), one_h)
        self.assertEqual(len(atoms), 6)
        self.assertFalse(_interval_order_exists(atoms, one_h))
        two_h = _six_sets(split_h=True)
        atoms2 = _atoms(sorted((set(TOKENS) - {"h"}) | {"h1", "h2"}), two_h)
        self.assertTrue(_interval_order_exists(atoms2, two_h))
        self.assertEqual(SIX, ["ac", "aṭ", "yaṇ", "yar", "val", "hal"])

    def test_spanda_turn_group(self) -> None:
        R2 = star(R, R)
        self.assertEqual(star(R2, R2), I2)
        self.assertNotEqual(R2, I2)
        self.assertEqual(star(R2, R), dagger(R))

    def test_recognition_defect_is_the_turn_part(self) -> None:
        B = ((1, 3), (-2, 2))
        A = tuple(tuple(Fraction(B[i][k] - B[k][i], 2) for k in range(2)) for i in range(2))
        gens = [(1, 0), (0, 1), (1, 1)]
        for ms in itertools.combinations_with_replacement(gens, 3):
            perms = sorted(set(itertools.permutations(ms)))
            for g, e in itertools.combinations(perms, 2):
                dB = path_memory(lambda b, a: omega_bilinear(B, b, a), list(g))[0] - path_memory(lambda b, a: omega_bilinear(B, b, a), list(e))[0]
                dA = path_memory(lambda b, a: omega_bilinear(A, b, a), list(g))[0] - path_memory(lambda b, a: omega_bilinear(A, b, a), list(e))[0]
                self.assertEqual(dB, dA)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_SHAIVA_SOURCES_NATIVIZED_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
