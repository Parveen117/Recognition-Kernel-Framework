from __future__ import annotations

import hashlib
import random
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.native_seam_gap_odd_covariance import cut_square, dagger, energy, eye, m_scale, mat, rad_part, sc, star, turn_part
from proof_lab.odd_channel_exchange_law import (
    anti_self_dagger_generator,
    build_certificate,
    canonical_bytes,
    cayley_unitary,
    certificate_sha256,
    comm,
    inverse,
    random_operator,
    real_mat,
    transport,
)

EXPECTED = Path(__file__).with_name("ODD_CHANNEL_EXCHANGE_LAW_EXPECTED.sha256")


class OddChannelExchangeLawTests(unittest.TestCase):
    def test_exact_inverse_over_cut_complex(self) -> None:
        a = mat([[sc(1, 1), sc(0, 2)], [sc(3, 0), sc(1, -1)]])
        self.assertEqual(star(inverse(a), a), eye(2))
        with self.assertRaises(AssertionError):
            inverse(mat([[sc(1, 1), sc(2, 2)], [sc(2, 2), sc(4, 4)]]))

    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("odd_channel_exchange_law.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "is_psd", "norm_le", "transpose(", "float("):
            self.assertNotIn(forbidden, src)

    def test_exchange_law_and_planted_wrong_sign(self) -> None:
        rng = random.Random(3)
        D, B, A = anti_self_dagger_generator(3, rng)
        S = cut_square(random_operator(3, rng))
        R, T = rad_part(S), turn_part(S)
        dS = star(dagger(D), S)
        dS = tuple(tuple((x[0] + y[0], x[1] + y[1]) for x, y in zip(r1, r2)) for r1, r2 in zip(dS, star(S, D)))
        right = tuple(tuple(x + y for x, y in zip(r1, r2)) for r1, r2 in zip(comm(T, B), comm(R, A)))
        wrong = tuple(tuple(x - y for x, y in zip(r1, r2)) for r1, r2 in zip(comm(T, B), comm(R, A)))
        self.assertEqual(turn_part(dS), right)
        self.assertNotEqual(turn_part(dS), wrong)

    def test_unitarity_needs_anti_self_dagger(self) -> None:
        D, _, _ = anti_self_dagger_generator(3, random.Random(4))
        C = cayley_unitary(D, Fraction(2, 3))
        self.assertEqual(star(dagger(C), C), eye(3))
        n = 3
        Bsym = tuple(tuple(Fraction(int(i != j)) for j in range(n)) for i in range(n))
        Z = tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))
        Cbad = cayley_unitary(real_mat(Bsym, Z), Fraction(2, 3))
        self.assertNotEqual(star(dagger(Cbad), Cbad), eye(3))

    def test_energy_exchange_not_conservation_of_odd(self) -> None:
        rng = random.Random(5)
        D, _, _ = anti_self_dagger_generator(3, rng)
        S = cut_square(random_operator(3, rng))
        Sh = transport(S, cayley_unitary(D, Fraction(1, 2)))
        self.assertEqual(energy(Sh), energy(S))
        odd = lambda X: sum(x * x for row in turn_part(X) for x in row)
        self.assertNotEqual(odd(Sh), odd(S))

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_ODD_CHANNEL_EXCHANGE_LAW_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
