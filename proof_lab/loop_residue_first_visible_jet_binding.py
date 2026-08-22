from __future__ import annotations

"""Exact certificate (theorum/57): LOOP-RESIDUE / FIRST-VISIBLE-JET BINDING.

Binds theorum/55's declared residue Gamma_mu (the Cayley commutator-loop
residual of the R-flow and the K-flow) to theorum/46's first-visible-jet seam
quotient.  Seam parameter: the flow step h.  Carrier: C_Sigma matrices
(theorum/50 scalars), Cayley steps of theorum/51.  Nothing Hilbert.

The jets are computed in the exact truncated ring  C_Sigma[h] / h^(N+1):
the Cayley step (I - hD/2)^{-1}(I + hD/2) is inverted by the terminating
geometric series of the nilpotent jet X = hD/2 (native Exp-style factorial /
geometric approximant, F00E shape), so every jet coefficient is an exact
C_Sigma matrix (theorum/45: zero arithmetic radius).

Facts certified:
 T1  Gamma(h) := loop(h) - I is a lawful theorum/46 seam observable:
     Gamma(0) = 0 (46 (2.1)), exact jets a_0 = a_1 = 0, a_2 = [D1, D2].
     Against the declared denominator B(h) = h^2 (b_2 = 1 != 0) theorum/46
     Thm 3.1 case 2 gives, entry by entry through 46's own classifier,
        Gamma (.)_S h^2 = [D1, D2]      (FINITE_SEAM_QUOTIENT),
     and for the EMK pair D1 = alpha R, D2 = iota beta K this is
     2 iota alpha beta RK (theorum/55 T3).  The 46 ladder: against h^1 the
     quotient is FINITE_QUOTIENT_ZERO, against h^3 it is DIVERGENT.
     theorum/55's "cubic scaling on a dyadic window" is replaced by an exact
     jet identity.
 T2  EXACT ORDER-3 LOOP IDENTITY (the item theorum/55 refused to claim):
        a_3 = (1/2) [D1 + D2, [D1, D2]]
     on random anti-self-dagger generators (exact), and in EMK coordinates
        a_3 = 2 alpha beta^2 R - 2 iota alpha^2 beta K.
     Consequence: the residual loop - I - h^2 a_2 - h^3 a_3 has first-visible
     order >= 4 (exact), which is what 55's dyadic ratio <= 1/6 was seeing.
 T3  Regular reparameterization (46 Thm 5.1): h = c s, c != 0 leaves the seam
     quotient invariant; the non-regular seam h = s^2 (phi'(0) = 0) changes
     the verdict against s^2 to FINITE_QUOTIENT_ZERO -- the subscript S is
     part of the type (46 Sec. 4).
 T4  GE false-residue verdict (55 T5) re-expressed in jet order: a residue is
     flow-generated iff its first-visible order is >= 2 and its order-2 jet
     is the bracket; a planted order-0 obstruction (55's unlawful
     perturbation) and a planted order-1 drift are both DIVERGENT against h^2
     under 46 -- false residue = residue visible before the bracket order.
     Commuting control: all jets zero to depth N AND exact identity loop = I
     at five rational h -- recorded as IDENTICALLY_ZERO_BY_EXACT_ALGEBRA,
     distinct from 46's INCOMPLETE_FLAT_OR_UNRESOLVED (46 Sec. 8 boundary
     respected: zero jets alone would not decide).
 T5  Jet packet corroborated against the exact rational loop of theorum/55:
     loop(h) - P_N(h) has dyadic mass ratio <= 1/2^(N+1) per halving on
     h in [1/512, 1/16] (remainder first-visible order >= N+1 witnessed).
"""

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.first_visible_jet_seam_quotient import classify_finite_jets
from proof_lab.generalized_euler_emk_dock import I2, K, R, RK, is_anti_self_dagger, loop
from proof_lab.native_seam_gap_odd_covariance import (
    Mat,
    eye,
    ftext,
    is_zero,
    m_add,
    m_scale,
    m_sub,
    mass,
    mat,
    sc,
    star,
    zeros,
)
from proof_lab.odd_channel_exchange_law import anti_self_dagger_generator

IOTA = sc(0, 1)
DEPTH = 4  # jets a_0..a_4 exact

Jet = list[Mat]  # coefficient of h^k at index k, truncated at DEPTH


def comm(X: Mat, Y: Mat) -> Mat:
    """C_Sigma commutator [X, Y] = X*Y - Y*X (51's comm is real-only)."""
    return m_sub(star(X, Y), star(Y, X))


# ---------------------------------------------------------------- jet ring C_Sigma[h]/h^(DEPTH+1)
def j_const(M: Mat) -> Jet:
    n = len(M)
    return [M] + [zeros(n, n) for _ in range(DEPTH)]


def j_add(a: Jet, b: Jet) -> Jet:
    return [m_add(x, y) for x, y in zip(a, b)]


def j_sub(a: Jet, b: Jet) -> Jet:
    return [m_sub(x, y) for x, y in zip(a, b)]


def j_scale(c, a: Jet) -> Jet:
    return [m_scale(c, x) for x in a]


def j_mul(a: Jet, b: Jet) -> Jet:
    n = len(a[0])
    out = [zeros(n, n) for _ in range(DEPTH + 1)]
    for i in range(DEPTH + 1):
        for k in range(DEPTH + 1 - i):
            out[i + k] = m_add(out[i + k], star(a[i], b[k]))
    return out


def j_inv_one_minus(X: Jet) -> Jet:
    """(I - X)^{-1} for a jet X with zero constant term: terminating geometric series."""
    n = len(X[0])
    assert is_zero(X[0]), "geometric inverse needs zero constant term"
    acc = j_const(eye(n))
    power = j_const(eye(n))
    for _ in range(DEPTH):
        power = j_mul(power, X)
        acc = j_add(acc, power)
    return acc


def cayley_jet(D: Mat, c: Fraction = Fraction(1)) -> Jet:
    """Jets of C_h(D) = (I - hD/2)^{-1}(I + hD/2) along the seam h = c*s (in s)."""
    n = len(D)
    X = [zeros(n, n), m_scale(c / 2, D)] + [zeros(n, n) for _ in range(DEPTH - 1)]
    return j_mul(j_inv_one_minus(X), j_add(j_const(eye(n)), X))


def loop_jet(D1: Mat, D2: Mat, c: Fraction = Fraction(1)) -> Jet:
    C1, C2 = cayley_jet(D1, c), cayley_jet(D2, c)
    C1i, C2i = cayley_jet(m_scale(-1, D1), c), cayley_jet(m_scale(-1, D2), c)
    return j_mul(j_mul(j_mul(C1, C2), C1i), C2i)


def residue_jet(D1: Mat, D2: Mat, c: Fraction = Fraction(1)) -> Jet:
    """Gamma(h) = loop(h) - I as a jet: theorum/55's declared residue typed as a 46 seam observable."""
    return j_sub(loop_jet(D1, D2, c), j_const(eye(len(D1))))


def j_eval(a: Jet, h: Fraction) -> Mat:
    n = len(a[0])
    out = zeros(n, n)
    for k, M in enumerate(a):
        out = m_add(out, m_scale(h**k, M))
    return out


# ---------------------------------------------------------------- theorum/46 consumed entrywise
def denominator_jets(order: int) -> list[Fraction]:
    return [Fraction(1 if k == order else 0) for k in range(DEPTH + 1)]


def classify_residue(gamma: Jet, denom_order: int) -> dict[str, Any]:
    """Apply 46's classify_finite_jets to every (entry, rad/turn) channel of the matrix jet."""
    n = len(gamma[0])
    b = denominator_jets(denom_order)
    statuses = set()
    quotient = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            parts = []
            for ch in (0, 1):
                cls = classify_finite_jets([gamma[k][i][j][ch] for k in range(DEPTH + 1)], b)
                statuses.add(cls.status)
                parts.append(cls.quotient)
            quotient[i][j] = parts
    # an entry whose jets are all zero is classified FINITE_QUOTIENT_ZERO by 46's classifier
    # (admitted-remainder convention); the matrix verdict is the strongest non-zero status present.
    if "DIVERGENT_NO_FINITE_QUOTIENT" in statuses:
        verdict = "DIVERGENT_NO_FINITE_QUOTIENT"
        Q = None
    elif "FINITE_SEAM_QUOTIENT" in statuses:
        verdict = "FINITE_SEAM_QUOTIENT"
        Q = tuple(tuple((quotient[i][j][0], quotient[i][j][1]) for j in range(n)) for i in range(n))
    else:
        verdict = "FINITE_QUOTIENT_ZERO"
        Q = zeros(n, n)
    return {"verdict": verdict, "quotient": Q, "entry_statuses": sorted(statuses)}


def first_visible_order(gamma: Jet) -> int | None:
    for k, M in enumerate(gamma):
        if not is_zero(M):
            return k
    return None


def emk_pair(alpha: Fraction, beta: Fraction) -> tuple[Mat, Mat]:
    return m_scale(alpha, R), m_scale(sc(0, beta), K)


def mtext(M: Mat) -> list[list[str]]:
    return [[f"{ftext(x[0])}+{ftext(x[1])}i" for x in row] for row in M]


# ---------------------------------------------------------------- T1
def t1_seam_quotient_is_bracket() -> dict[str, Any]:
    rng = random.Random(57)
    ok_vanish = ok_orders = ok_quot = ok_ladder = 0
    trials = 12
    for _ in range(trials):
        alpha, beta = Fraction(rng.randint(-4, 4) or 1), Fraction(rng.randint(-4, 4) or 1)
        D1, D2 = emk_pair(alpha, beta)
        g = residue_jet(D1, D2)
        bracket = comm(D1, D2)
        ok_vanish += is_zero(g[0])  # 46 (2.1): A(0) = 0
        ok_orders += first_visible_order(g) == 2 and is_zero(g[1])
        c2 = classify_residue(g, 2)
        ok_quot += c2["verdict"] == "FINITE_SEAM_QUOTIENT" and c2["quotient"] == bracket == m_scale(sc(0, 2 * alpha * beta), RK)
        c1, c3 = classify_residue(g, 1), classify_residue(g, 3)
        ok_ladder += c1["verdict"] == "FINITE_QUOTIENT_ZERO" and c3["verdict"] == "DIVERGENT_NO_FINITE_QUOTIENT"
    # general (non-EMK) anti-self-dagger generators, n = 3
    gen_ok = 0
    for _ in range(8):
        D1, _, _ = anti_self_dagger_generator(3, rng)
        D2, _, _ = anti_self_dagger_generator(3, rng)
        assert is_anti_self_dagger(D1) and is_anti_self_dagger(D2)
        g = residue_jet(D1, D2)
        gen_ok += is_zero(g[0]) and is_zero(g[1]) and g[2] == comm(D1, D2)
    D1, D2 = emk_pair(Fraction(2), Fraction(3))
    g = residue_jet(D1, D2)
    checks = {
        "residue_vanishes_at_seam_endpoint_46_2_1": ok_vanish == trials,
        "first_visible_order_exactly_2_a0_a1_zero": ok_orders == trials,
        "seam_quotient_vs_h2_equals_bracket_2_iota_alpha_beta_RK": ok_quot == trials,
        "46_ladder_h1_zero_h3_divergent": ok_ladder == trials,
        "a2_equals_bracket_general_anti_self_dagger_n3_8_of_8": gen_ok == 8,
    }
    return {"checks": checks, "example_alpha2_beta3_a2": mtext(g[2]), "example_quotient": classify_residue(g, 2)["verdict"]}


# ---------------------------------------------------------------- T2
def a3_closed_form(D1: Mat, D2: Mat) -> Mat:
    return m_scale(Fraction(1, 2), comm(m_add(D1, D2), comm(D1, D2)))


def t2_exact_order3() -> dict[str, Any]:
    rng = random.Random(59)
    ok_gen = ok_emk = ok_order4 = 0
    for _ in range(10):
        n = rng.choice([2, 3, 4])
        D1, _, _ = anti_self_dagger_generator(n, rng)
        D2, _, _ = anti_self_dagger_generator(n, rng)
        g = residue_jet(D1, D2)
        ok_gen += g[3] == a3_closed_form(D1, D2)
    for _ in range(10):
        alpha, beta = Fraction(rng.randint(-4, 4) or 2), Fraction(rng.randint(-4, 4) or 3)
        D1, D2 = emk_pair(alpha, beta)
        g = residue_jet(D1, D2)
        emk_form = m_add(m_scale(2 * alpha * beta * beta, R), m_scale(sc(0, -2 * alpha * alpha * beta), K))
        ok_emk += g[3] == a3_closed_form(D1, D2) == emk_form
        # residual after removing a2, a3 has first-visible order >= 4 in the jet ring
        known = [zeros(2, 2), zeros(2, 2), g[2], g[3]] + [zeros(2, 2)] * (DEPTH - 3)
        ok_order4 += first_visible_order(j_sub(g, known)) in (4, None)
    D1, D2 = emk_pair(Fraction(2), Fraction(3))
    g = residue_jet(D1, D2)
    checks = {
        "a3_equals_half_bracket_of_sum_with_bracket_general_10_of_10": ok_gen == 10,
        "a3_EMK_closed_form_2ab2_R_minus_2i_a2b_K_10_of_10": ok_emk == 10,
        "residual_after_a2_a3_has_order_ge_4": ok_order4 == 10,
        "a3_nonzero_for_alpha2_beta3": not is_zero(g[3]),
    }
    return {"checks": checks, "a3_alpha2_beta3": mtext(g[3]), "a4_alpha2_beta3": mtext(g[4])}


# ---------------------------------------------------------------- T3
def t3_reparameterization() -> dict[str, Any]:
    D1, D2 = emk_pair(Fraction(2), Fraction(3))
    q_ref = classify_residue(residue_jet(D1, D2), 2)["quotient"]
    ok = 0
    for c in (Fraction(2), Fraction(-1, 3), Fraction(7, 5)):
        g_s = residue_jet(D1, D2, c)  # seam h = c s, jets in s
        # 46 Thm 5.1: leading coefficients scale by c^2 on both sides; quotient against (c s)^2 is unchanged
        cls = classify_residue(g_s, 2)
        quotient_vs_h2 = tuple(tuple((x[0] / (c * c), x[1] / (c * c)) for x in row) for row in cls["quotient"])
        ok += cls["verdict"] == "FINITE_SEAM_QUOTIENT" and quotient_vs_h2 == q_ref and g_s[2] == m_scale(c * c, comm(D1, D2))
    # non-regular seam h = s^2: Gamma(s^2) has first-visible order 4 in s
    g2 = residue_jet(D1, D2)
    g_sq = [zeros(2, 2)] * (DEPTH + 1)
    for k, M in enumerate(g2):
        if 2 * k <= DEPTH:
            g_sq[2 * k] = M
    cls_sq = classify_residue(g_sq, 2)
    checks = {
        "regular_reparameterization_invariance_3_of_3_46_thm_5_1": ok == 3,
        "non_regular_seam_h_eq_s2_changes_verdict_to_zero": cls_sq["verdict"] == "FINITE_QUOTIENT_ZERO" and first_visible_order(g_sq) == 4,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T4
def t4_false_residue_by_jet_order() -> dict[str, Any]:
    D1, D2 = emk_pair(Fraction(1), Fraction(-2))
    g = residue_jet(D1, D2)
    lawful = classify_residue(g, 2)
    # planted order-0 obstruction (55 T5's unlawful perturbation shape)
    plant0 = j_add(g, j_const(mat([[sc(1, 0), 0], [0, sc(-1, 0)]])))
    # planted order-1 drift: an extra generator entering at first order
    drift = [zeros(2, 2), m_scale(IOTA, I2)] + [zeros(2, 2)] * (DEPTH - 1)
    plant1 = j_add(g, drift)
    c0, c1 = classify_residue(plant0, 2), classify_residue(plant1, 2)
    # commuting control: alpha R with iota gamma I
    Dc = m_scale(sc(0, Fraction(5)), I2)
    gc = residue_jet(D1, Dc)
    jets_zero = first_visible_order(gc) is None
    exact_identity = all(loop(D1, Dc, h) == eye(2) for h in (Fraction(1, 2), Fraction(1, 3), Fraction(2, 7), Fraction(-3, 4), Fraction(5)))
    commuting_status = "IDENTICALLY_ZERO_BY_EXACT_ALGEBRA" if (jets_zero and exact_identity) else "INCOMPLETE_FLAT_OR_UNRESOLVED"
    checks = {
        "lawful_residue_first_visible_order_2_quotient_is_bracket": lawful["verdict"] == "FINITE_SEAM_QUOTIENT" and lawful["quotient"] == comm(D1, D2),
        "planted_order0_obstruction_DIVERGENT_vs_h2": c0["verdict"] == "DIVERGENT_NO_FINITE_QUOTIENT" and first_visible_order(plant0) == 0,
        "planted_order1_drift_DIVERGENT_vs_h2": c1["verdict"] == "DIVERGENT_NO_FINITE_QUOTIENT" and first_visible_order(plant1) == 1,
        "commuting_control_identically_zero_by_exact_algebra": commuting_status == "IDENTICALLY_ZERO_BY_EXACT_ALGEBRA",
    }
    return {"checks": checks, "commuting_status": commuting_status, "rule": "flow-generated residue <=> first-visible order >= 2 and a_2 = [D1,D2]; false residue = visible before the bracket order"}


# ---------------------------------------------------------------- T5
def t5_corroborate_against_exact_loop() -> dict[str, Any]:
    D1, D2 = emk_pair(Fraction(2), Fraction(3))
    g = loop_jet(D1, D2)
    masses = []
    for k in range(4, 10):
        h = Fraction(1, 2**k)
        masses.append(mass(m_sub(loop(D1, D2, h), j_eval(g, h))))
    ratio_ok = all(masses[i + 1] <= masses[i] / 2 ** (DEPTH + 1) for i in range(len(masses) - 1)) and masses[0] > 0
    # jets of C(D) and C(-D) are mutually inverse in the jet ring (Cayley involution, exact)
    C, Ci = cayley_jet(D1), cayley_jet(m_scale(-1, D1))
    inv_ok = j_mul(C, Ci) == j_const(eye(2))
    checks = {
        "exact_loop_minus_jet_polynomial_halves_by_2_pow_5_on_dyadic_window": ratio_ok,
        "cayley_jets_of_D_and_minus_D_mutually_inverse": inv_ok,
    }
    return {"checks": checks, "remainder_masses": [ftext(m) for m in masses]}


def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_seam_quotient_is_bracket": t1_seam_quotient_is_bracket(),
        "t2_exact_order3": t2_exact_order3(),
        "t3_reparameterization": t3_reparameterization(),
        "t4_false_residue_by_jet_order": t4_false_residue_by_jet_order(),
        "t5_corroborate_against_exact_loop": t5_corroborate_against_exact_loop(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_LOOP_RESIDUE_FIRST_VISIBLE_JET_BINDING_CANDIDATE" if all(checks.values()) else "FAIL_LOOP_RESIDUE_FIRST_VISIBLE_JET_BINDING_CANDIDATE"
    return {
        "schema": "rkf.loop_residue_first_visible_jet_binding_candidate.v1",
        "status": status,
        "consumes": {
            "theorum/46": "first-visible-jet seam quotient classification (classify_finite_jets), Thm 3.1, Thm 5.1, Sec. 8 boundary",
            "theorum/55": "Cayley commutator loop of R-flow and K-flow; Gamma_mu declared residue; T5 false-residue verdict",
            "theorum/51": "Cayley step and anti-self-dagger generators",
            "theorum/45": "exact rational jets carry zero arithmetic radius",
        },
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Gamma(h) = loop(h) - I is a theorum/46 seam observable with first-visible order exactly 2 and Gamma (.)_S h^2 = [D1,D2] (= 2 iota alpha beta RK on the EMK pair), through 46's own classifier entrywise",
                "EXACT ORDER-3 LOOP IDENTITY: a_3 = (1/2)[D1 + D2, [D1, D2]]; EMK form 2 alpha beta^2 R - 2 iota alpha^2 beta K; residual after a_2, a_3 has order >= 4",
                "the seam quotient is invariant under regular reparameterization h = c s (46 Thm 5.1) and the non-regular seam h = s^2 changes the verdict (S is part of the type)",
                "GE false residue = residue visible before jet order 2: planted order-0 and order-1 residues are DIVERGENT against h^2; lawful residue's order-2 jet is the bracket",
                "commuting generators: jets zero to depth 4 AND exact identity loop = I at five rational h (IDENTICALLY_ZERO_BY_EXACT_ALGEBRA, not 46's INCOMPLETE)",
                "jet packet corroborated against theorum/55's exact rational loop on the dyadic window [1/512, 1/16]",
            ],
            "NOT_claimed": [
                "a closed form for a_4 or any all-orders (BCH-type) series -- only jets to depth 4 are computed, and only a_2, a_3 have certified closed forms",
                "seam-invariance across genuinely different seams (46's own boundary): only the step seam h and its regular reparameterizations are covered",
                "that Gamma_mu of de4 has no component beyond the loop residue -- the binding types the loop residual as THE 46-resolvable part of the declared residue; any further declared term remains declared",
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
