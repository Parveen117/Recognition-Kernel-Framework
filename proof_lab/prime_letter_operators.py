from __future__ import annotations

"""Exact certificate (theorum/59): PRIME LETTER OPERATORS -- the Prime Operator
canvas read on the primitive carrier (not Hilbert).

Owner's correction (Aug 23 2026): the Prime Operator canvas was refused in
theorum/58 on Hilbert-layer grounds (eigenvalues, ladder adjoints).  Like
Aghora (theorum/56 refusal -> theorum/50/51 repair), the operator has a
lawful home on the primitive carrier.  This certificate locates it.

Sources consumed (PROVED / pinned):
  F00H Thm 8.1   native fundamental theorem of arithmetic (prime-letter ledger)
  F00H Thm 11.2  native logarithmic divisor identity  sum_{d|n} Lambda(d) = log n
  F00E Thm 3.1   native Exp addition law
  T01 (RH-Framework)  residues NEGATE under dagger
  theorum/55 T1  iota*I is an ODD (A-type, turn) anti-self-dagger generator
  theorum/57     loop residue as first-visible-jet seam quotient
  Vedic repo, VRG_Letter_Root_Operator_Seed_Algebra_v1: word = ordered letter
                 product, letter phase accumulation phi(W) = sum phi(l_i),
                 letter curvature [l_i, l_j], winding memory k(W)
  (the Vedic repo contains NO prime-operator file; the Letter-Root seed
   algebra is the nearest PROVED-shape statement and is what is bound here)

Carrier: prime-letter ledger v in Z^(P) (F00H 8.1 bijection n <-> v).
Letter a_p = shift by e_p.  Dagger = negation of the ledger (T01 rule).
Formal log  l(v) = v  (no floats; UGD-M-1 prime-log lattice).

Facts certified:
 T1  Canvas A4 corrected: [a_p, a_q] = 0 exactly; a_p a_q^dagger = a_{p/q}
     (ledger e_p - e_q).  The canvas relation a_p a_q^dagger = a_{pq}^dagger is
     DISPROVED (witness p=2, q=3).  Letter curvature Omega_L = 0 for prime
     letters: the word ledger is order-free (Vedic letter algebra,
     commutative case).
 T2  Canvas A1/A2 native: irreducible  <=>  ledger mass |v|_1 = 1  (computed
     n <= 300 against F00H factorization); the "spectrum" of the generator is
     the SUPPORT of the Lambda memory channel = single-letter words (prime
     powers), and the weight carried there is the letter's own log e_p, not p.
 T3  Generator = memory of multiplication: l(mn) = l(m) + l(n) and F00H 11.2
     sum_{d|n} Lambda(d) = l(n) re-verified exactly in the formal lattice
     (n <= 300).
 T4  AGHORA PLACEMENT (the owner's point): in the unitary log chart the letter
     acts as Exp(iota t l_p); its generator iota*l_p*I is anti-self-dagger and
     turn-only (ODD, theorum/55 T1);  (a) two letters carry NO loop residue
     (jets zero to depth 4 + exact loop = I: abelian = zero exchange);
     (b) phase accumulation is EXACT under native Exp in the jet ring
     (F00E addition law, binomial) -- Exp(iota t x) Exp(iota t y) =
     Exp(iota t (x+y)) to depth 4;  (c) the rational one-step (Cayley) chart
     stores a first-visible residue at order 3:
          C(x)C(y)C(x+y)^{-1} - I  (.)_S t^3  =  iota * x y (x+y) / 4
     (theorum/46 classifier; closed form certified on random rationals) --
     the Vedic "winding memory" of letter composition is a chart artefact of
     rational stepping, absent under native Exp;  (d) central invisibility:
     transport of ANY cut square by the letter's unitary is the identity
     (C^dagger S C = S exactly) -- prime letters are invisible to every
     quadratic form; the only observable is turn accumulation.  This is why
     Hilbert eigenvalue language misfires while the operator is lawful.
 T5  NOT CLAIMED: canvas A3 (zeta as partition function, zeros), A5
     (self-reference), L1 (PNT), L2 (twin), L3 (Goldbach), L4 (entropy):
     each needs native continuation past Re > 1 (N1/N2 OPEN, WEIL-N-1).
"""

import argparse
import hashlib
import importlib.util
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.first_visible_jet_seam_quotient import classify_finite_jets
from proof_lab.generalized_euler_emk_dock import I2, is_anti_self_dagger, loop
from proof_lab.loop_residue_first_visible_jet_binding import DEPTH, cayley_jet, first_visible_order, j_add, j_const, j_mul, j_scale, j_sub, residue_jet
from proof_lab.native_seam_gap_odd_covariance import cut_square, dagger, eye, is_zero, m_scale, mat, sc, star, zeros
from proof_lab.odd_channel_exchange_law import cayley_unitary, random_operator, transport

F00H = Path(__file__).resolve().parents[1] / "certificates" / "foundation" / "F00GHI_LOG_ARITHMETIC_ZETA_V0_1" / "verify.py"


def load_f00h():
    spec = importlib.util.spec_from_file_location("f00ghi_verify", F00H)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


# ---------------------------------------------------------------- prime-letter ledger
Ledger = dict[int, int]


def ledger(n: int, f) -> Ledger:
    return dict(f.factor_integer(n))


def l_add(a: Ledger, b: Ledger) -> Ledger:
    out = dict(a)
    for p, k in b.items():
        out[p] = out.get(p, 0) + k
        if out[p] == 0:
            del out[p]
    return out


def l_neg(a: Ledger) -> Ledger:  # native dagger: residues negate (T01)
    return {p: -k for p, k in a.items()}


def mass1(a: Ledger) -> int:
    return sum(abs(k) for k in a.values())


def t1_canvas_a4_corrected(f) -> dict[str, Any]:
    primes = f.primes_upto(60)
    commute = all(l_add({p: 1}, {q: 1}) == l_add({q: 1}, {p: 1}) for p in primes for q in primes)
    dagger_law = all(l_add({p: 1}, l_neg({q: 1})) == ({p: 1, q: -1} if p != q else {}) for p in primes for q in primes)
    canvas_pq = l_add({2: 1}, l_neg({3: 1})) == l_neg({2: 1, 3: 1})  # canvas claim a_p a_q^dag = a_pq^dag
    rng = random.Random(59)
    order_free = True
    for _ in range(30):
        word = [rng.choice(primes) for _ in range(6)]
        v1: Ledger = {}
        for p in word:
            v1 = l_add(v1, {p: 1})
        rng.shuffle(word)
        v2: Ledger = {}
        for p in word:
            v2 = l_add(v2, {p: 1})
        order_free &= v1 == v2
    checks = {
        "prime_letters_commute_exactly": commute,
        "a_p_a_q_dagger_equals_a_p_over_q_ledger": dagger_law,
        "canvas_a_p_a_q_dagger_equals_a_pq_dagger_DISPROVED": not canvas_pq,
        "letter_curvature_zero_word_ledger_order_free": order_free,
    }
    return {"checks": checks, "witness": {"a2_a3_dagger": l_add({2: 1}, l_neg({3: 1})), "a6_dagger": l_neg({2: 1, 3: 1})}}


def t2_irreducibility_and_spectrum(f) -> dict[str, Any]:
    N = 300
    irreducible_iff_mass1 = all((mass1(ledger(n, f)) == 1) == f.is_prime(n) for n in range(2, N + 1))
    support = [n for n in range(1, N + 1) if f.lambda_log_vector(n)]
    single_letter = [n for n in range(1, N + 1) if len(ledger(n, f)) == 1]
    weight_is_letter_log = all(f.lambda_log_vector(n) == {next(iter(ledger(n, f))): 1} for n in support)
    checks = {
        "irreducible_iff_ledger_mass_1_n_le_300": irreducible_iff_mass1,
        "generator_support_equals_single_letter_words_prime_powers": support == single_letter,
        "weight_on_support_is_letter_log_not_p": weight_is_letter_log,
    }
    return {"checks": checks, "support_count": len(support)}


def t3_generator_is_memory(f) -> dict[str, Any]:
    N = 300
    leibniz = all(ledger(m * n, f) == l_add(ledger(m, f), ledger(n, f)) for m in range(1, 40) for n in range(1, 40))
    divisor_identity = all(f.add_vectors(f.lambda_log_vector(d) for d in f.divisors(n)) == ledger(n, f) for n in range(1, N + 1))
    checks = {"formal_log_additive_over_letters": leibniz, "F00H_11_2_sum_Lambda_over_divisors_equals_log_n_le_300": divisor_identity}
    return {"checks": checks}


# ---------------------------------------------------------------- odd-sector placement (unitary log chart)
def exp_jet_scalar(x: Fraction):
    """Jets of Exp(iota t x) in C_Sigma[t]/t^(DEPTH+1): native factorial approximant (F00E shape)."""
    u = [zeros(1, 1), mat([[sc(0, x)]])] + [zeros(1, 1) for _ in range(DEPTH - 1)]
    acc = j_const(eye(1))
    power = j_const(eye(1))
    fact = 1
    for k in range(1, DEPTH + 1):
        power = j_mul(power, u)
        fact *= k
        acc = j_add(acc, j_scale(Fraction(1, fact), power))
    return acc


def cayley_jet_scalar(x: Fraction):
    return cayley_jet(mat([[sc(0, x)]]))


def t4_aghora_placement() -> dict[str, Any]:
    rng = random.Random(61)
    odd_generator = all(is_anti_self_dagger(m_scale(sc(0, Fraction(rng.randint(1, 9), rng.randint(1, 9))), I2)) for _ in range(10))
    turn_only = all(all(e[0] == 0 for row in m_scale(sc(0, Fraction(k)), I2) for e in row) for k in range(1, 6))
    # (a) no loop residue between two letters
    no_loop = True
    for _ in range(6):
        x, y = (Fraction(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(2))
        D1, D2 = m_scale(sc(0, x), I2), m_scale(sc(0, y), I2)
        no_loop &= first_visible_order(residue_jet(D1, D2)) is None and loop(D1, D2, Fraction(1, 3)) == eye(2)
    # (b) Exp phase accumulation exact in jets; (c) Cayley residue at order 3 with closed form
    exp_exact = cayley_residue_form = True
    example = None
    for _ in range(8):
        x, y = (Fraction(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(2))
        ex, ey, exy = exp_jet_scalar(x), exp_jet_scalar(y), exp_jet_scalar(x + y)
        exp_exact &= j_mul(ex, ey) == exy
        cx, cy, cxy_inv = cayley_jet_scalar(x), cayley_jet_scalar(y), cayley_jet_scalar(-(x + y))
        gamma = j_sub(j_mul(j_mul(cx, cy), cxy_inv), j_const(eye(1)))
        jets_turn = [g[0][0][1] for g in gamma]
        jets_rad = [g[0][0][0] for g in gamma]
        cls = classify_finite_jets(jets_turn, [0, 0, 0, 1, 0])
        cls_rad = classify_finite_jets(jets_rad, [0, 0, 0, 1, 0])
        cayley_residue_form &= cls.status == "FINITE_SEAM_QUOTIENT" and cls.quotient == x * y * (x + y) / 4 and cls_rad.status == "FINITE_QUOTIENT_ZERO" and first_visible_order(gamma) == 3
        example = example or {"x": str(x), "y": str(y), "a3_turn": str(cls.quotient)}
    # (d) central invisibility on cut squares
    invisible = True
    for _ in range(8):
        S = cut_square(random_operator(3, rng))
        U = cayley_unitary(m_scale(sc(0, Fraction(rng.randint(1, 7), rng.randint(1, 4))), eye(3)), Fraction(1, 2))
        invisible &= transport(S, U) == S and star(dagger(U), U) == eye(3)
    checks = {
        "letter_generator_iota_x_I_anti_self_dagger_turn_only_ODD": odd_generator and turn_only,
        "two_letters_zero_loop_residue_abelian": no_loop,
        "native_Exp_phase_accumulation_exact_in_jets_F00E": exp_exact,
        "cayley_chart_residue_order3_quotient_iota_xy_x_plus_y_over_4": cayley_residue_form,
        "letter_unitary_transport_is_identity_on_every_cut_square": invisible,
    }
    return {"checks": checks, "cayley_residue_example": example}


def build_certificate() -> dict[str, Any]:
    f = load_f00h()
    packets = {
        "t1_canvas_a4_corrected": t1_canvas_a4_corrected(f),
        "t2_irreducibility_and_spectrum": t2_irreducibility_and_spectrum(f),
        "t3_generator_is_memory": t3_generator_is_memory(f),
        "t4_aghora_placement": t4_aghora_placement(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PRIME_LETTER_OPERATORS_CANDIDATE" if all(checks.values()) else "FAIL_PRIME_LETTER_OPERATORS_CANDIDATE"
    return {
        "schema": "rkf.prime_letter_operators_candidate.v1",
        "status": status,
        "f00h_verify_sha256": hashlib.sha256(F00H.read_bytes()).hexdigest(),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "prime letters commute; a_p a_q^dagger = a_{p/q}; the canvas's a_{pq}^dagger DISPROVED; word ledger order-free (letter curvature zero)",
                "irreducible <=> ledger mass 1 (n<=300, F00H); generator support = Lambda support = prime powers; weight there is the letter log",
                "formal log additive; F00H 11.2 divisor identity re-verified in the formal lattice",
                "letter generator iota*x*I is ODD (anti-self-dagger, turn-only); two letters have zero loop residue; Exp phase accumulation exact in jets; Cayley chart residue (.)_S t^3 = iota xy(x+y)/4; letter unitary acts trivially on every cut square",
            ],
            "NOT_claimed": [
                "canvas A3 (zeta partition function / zeros), A5 (self-reference), L1 PNT, L2 twin primes, L3 Goldbach, L4 gap entropy -- all need native continuation (N1/N2 OPEN)",
                "any statement about primes beyond n<=300 except where F00H theorems are cited",
                "that the Vedic repo contains a prime-operator statement (it does not; the Letter-Root seed algebra is what is bound)",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    body = canonical_bytes(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
