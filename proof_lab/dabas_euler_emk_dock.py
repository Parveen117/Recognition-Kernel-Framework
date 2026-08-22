from __future__ import annotations

"""Exact certificate (theorum/55): DABAS-EULER / EMK DOCK.

Binds three previously "same shape, dock open" items:
  (a) theorum/51's exchange law  <->  the EMK/Dabas-Euler RK transport
      (nabla^{RK} = nabla + alpha R + beta K + Gamma, de4 Sec. 4);
  (b) the EMK bracket [R,K] = 2RK (mixed RK channel)  <->  the commutator
      loop of the two flows (RST-1 T4 shape);
  (c) EMK-1's determinant identity det M = Delta_par + Delta_perp  <->
      theorum/53's flow invariant det S.

Carrier: the EMK 2x2 real primitives of theorum/48 (I, K, R, RK) embedded in
C_Sigma (turn-free), plus iota-multiples.  Verdicts: mass/energy, exact
algebra.  Nothing Hilbert.

Facts certified:
 T1  anti-self-dagger generators inside the EMK span:  R is a pure EVEN
     (B-type, real antisymmetric) generator;  iota*I, iota*K, iota*RK are pure
     ODD (A-type, turn-symmetric) generators;  K, RK, I themselves are NOT
     anti-self-dagger (not flow generators).  The dagger grading and the
     J_E := K grading of theorum/48 are DIFFERENT gradings (R: K-odd but
     dagger-even; iota K: K-even but dagger-odd) -- certified as a separation,
     not identified.
 T2  DOCK (a): for the DE connection generator D = alpha R + iota beta K the
     exchange law reads  rad <- alpha[R_S, R] + beta[K, T],
     turn <- alpha[T, R] + beta[R_S, K]:  the DE "lawful phase rotation"
     alpha R acts by commutator inside each channel, the DE "seam transport"
     beta K (carrying turn) EXCHANGES channels.  Exact on random cut squares.
 T3  DOCK (b): [alpha R, iota beta K] = 2 iota alpha beta RK exactly (EMK
     bracket), and the Cayley commutator loop of the two flows has residual
     loop - I - h^2 [D1,D2] with mass scaling cubically on dyadic h
     (ratio <= 1/6 per halving for h <= 1/16; BUILD NOTE: h = 1/2..1/8 with generator mass ~3 is not in the
     asymptotic range and was refused by the first draft's check -- the
     certified window is h in [1/512, 1/16]) -- the RK mixed channel IS the leading loop
     residue of composing R-flow and K-flow.  Commuting control: alpha R vs
     iota gamma I gives loop = I exactly.
 T4  DOCK (c): for M = aI + bK + cR + dRK (real), det(M^dagger M) = (Delta_par
     + Delta_perp)^2 exactly; under the R-flow M -> M C_h(R) the total
     Delta_par + Delta_perp is exactly invariant while Delta_par and Delta_perp
     individually EXCHANGE (rational rotation, no trigonometry): EMK-1's two
     channels are an exchange pair and their sum is theorum/53's invariant.
 T5  DE false-residue prevention (de4 Sec. 5) as an executable verdict: for a
     transition S -> S' the DE residue is S' - transport_{alpha,beta}(S);
     a lawful transition has residue exactly 0 under its declared (alpha,
     beta), nonzero under any other grid pair; an unlawful transition has
     nonzero residue for EVERY grid pair (open obstruction).
"""

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.native_seam_gap_odd_covariance import (
    F0,
    F1,
    Mat,
    cut_square,
    dagger,
    eye,
    ftext,
    is_zero,
    m_add,
    m_scale,
    m_sub,
    mass,
    mat,
    rad_part,
    sc,
    star,
    turn_part,
)
from proof_lab.native_seam_resolvent import det
from proof_lab.odd_channel_exchange_law import cayley_unitary, comm, inverse, random_operator, real_add, transport

I2 = mat([[1, 0], [0, 1]])
K = mat([[0, 1], [1, 0]])
R = mat([[0, -1], [1, 0]])
RK = star(R, K)
IOTA = sc(0, 1)


def emk(a, b, c, d) -> Mat:
    return m_add(m_add(m_scale(a, I2), m_scale(b, K)), m_add(m_scale(c, R), m_scale(d, RK)))


def real_of(M: Mat):
    return rad_part(M)


def is_anti_self_dagger(D: Mat) -> bool:
    return dagger(D) == m_scale(-1, D)


# ---------------------------------------------------------------- T1
def t1_generators() -> dict[str, Any]:
    iK, iRK, iI = m_scale(IOTA, K), m_scale(IOTA, RK), m_scale(IOTA, I2)
    # K-grading of theorum/48: conjugation by K
    kgrade = lambda X: star(star(K, X), K) == X
    checks = {
        "EMK_relations": star(K, K) == I2 and star(R, R) == m_scale(-1, I2) and star(R, K) == m_scale(-1, star(K, R)),
        "R_is_anti_self_dagger_even_B_type": is_anti_self_dagger(R) and all(x[1] == 0 for row in R for x in row),
        "iota_I_iota_K_iota_RK_anti_self_dagger_odd_A_type": all(is_anti_self_dagger(X) and all(x[0] == 0 for row in X for x in row) for X in (iI, iK, iRK)),
        "K_RK_I_not_flow_generators": not any(is_anti_self_dagger(X) for X in (K, RK, I2)),
        "gradings_differ_R_is_K_odd_but_dagger_even": (not kgrade(R)) and is_anti_self_dagger(R),
        "gradings_differ_iotaK_is_K_even_but_dagger_odd": kgrade(iK) and all(x[0] == 0 for row in iK for x in row),
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T2
def t2_dock_exchange() -> dict[str, Any]:
    rng = random.Random(55)
    ok = 0
    for _ in range(15):
        alpha, beta = Fraction(rng.randint(-3, 3)), Fraction(rng.randint(-3, 3))
        D = m_add(m_scale(alpha, R), m_scale(sc(0, beta), K))
        assert is_anti_self_dagger(D)
        S = cut_square(random_operator(2, rng))
        RS, T = rad_part(S), turn_part(S)
        dS = m_add(star(dagger(D), S), star(S, D))
        Rr, Kr = real_of(R), real_of(K)
        sc_ = lambda c, X: tuple(tuple(c * x for x in row) for row in X)
        pred_rad = real_add(sc_(alpha, comm(RS, Rr)), sc_(beta, comm(Kr, T)))
        pred_turn = real_add(sc_(alpha, comm(T, Rr)), sc_(beta, comm(RS, Kr)))
        ok += rad_part(dS) == pred_rad and turn_part(dS) == pred_turn
    return {"checks": {"DE_connection_generator_obeys_exchange_law_15_of_15": ok == 15}, "reading": "alpha R: commutator inside each channel; beta K (with turn): exchange between channels"}


# ---------------------------------------------------------------- T3
def loop(D1: Mat, D2: Mat, h: Fraction) -> Mat:
    C1, C2 = cayley_unitary(D1, h), cayley_unitary(D2, h)
    return star(star(star(C1, C2), inverse(C1)), inverse(C2))


def t3_dock_bracket() -> dict[str, Any]:
    alpha, beta = Fraction(2), Fraction(3)
    D1 = m_scale(alpha, R)
    D2 = m_scale(sc(0, beta), K)
    bracket = m_sub(star(D1, D2), star(D2, D1))
    emk_bracket = bracket == m_scale(sc(0, 2 * alpha * beta), RK)
    masses = []
    for k in range(4, 10):
        h = Fraction(1, 2**k)
        res = m_sub(m_sub(loop(D1, D2, h), eye(2)), m_scale(h * h, bracket))
        masses.append(mass(res))
    cubic = all(masses[i + 1] <= masses[i] / 6 for i in range(len(masses) - 1)) and masses[0] > 0
    # leading term check: (loop - I)/h^2 -> bracket: mass(loop - I - h^2 bracket) << mass(h^2 bracket)
    h = Fraction(1, 256)
    leading = mass(m_sub(m_sub(loop(D1, D2, h), eye(2)), m_scale(h * h, bracket))) < mass(m_scale(h * h, bracket)) / 10
    commuting = loop(D1, m_scale(sc(0, Fraction(5)), I2), Fraction(1, 2)) == eye(2)
    checks = {
        "bracket_equals_2_iota_alpha_beta_RK_EMK": emk_bracket,
        "loop_residual_scales_cubically_on_dyadic_h": cubic,
        "RK_channel_is_leading_loop_residue": leading,
        "commuting_control_loop_identity": commuting,
    }
    return {"checks": checks, "residual_masses": [ftext(m) for m in masses]}


# ---------------------------------------------------------------- T4
def t4_dock_determinant() -> dict[str, Any]:
    rng = random.Random(57)
    ok = inv = exch = 0
    for _ in range(15):
        a, b, c, d = (Fraction(rng.randint(-3, 3)) for _ in range(4))
        M = emk(a, b, c, d)
        dpar, dperp = a * a - b * b, c * c - d * d
        S = cut_square(M)
        ok += det(S) == sc((dpar + dperp) ** 2)
        h = Fraction(rng.randint(1, 3), rng.randint(1, 4))
        Mh = star(M, cayley_unitary(R, h))  # rational rotation, no trigonometry
        # read off new EMK coordinates: M = [[a-d, b-c],[b+c, a+d]]
        a2 = (Mh[0][0][0] + Mh[1][1][0]) / 2
        d2 = (Mh[1][1][0] - Mh[0][0][0]) / 2
        b2 = (Mh[0][1][0] + Mh[1][0][0]) / 2
        c2 = (Mh[1][0][0] - Mh[0][1][0]) / 2
        assert emk(a2, b2, c2, d2) == Mh
        dpar2, dperp2 = a2 * a2 - b2 * b2, c2 * c2 - d2 * d2
        inv += dpar2 + dperp2 == dpar + dperp and det(cut_square(Mh)) == det(S)
        exch += dpar2 != dpar
    checks = {
        "det_S_equals_total_channel_squared_15_of_15": ok == 15,
        "total_channel_invariant_under_R_flow_15_of_15": inv == 15,
        "individual_channels_exchange_under_R_flow": exch > 0,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T5
def t5_false_residue() -> dict[str, Any]:
    rng = random.Random(58)
    S = cut_square(random_operator(2, rng))
    h = Fraction(1, 2)
    grid = [(Fraction(a), Fraction(b)) for a in range(-2, 3) for b in range(-2, 3)]
    gen = lambda a, b: m_add(m_scale(a, R), m_scale(sc(0, b), K))
    alpha, beta = Fraction(1), Fraction(-2)
    S_lawful = transport(S, cayley_unitary(gen(alpha, beta), h))
    residue = lambda Sp, a, b: m_sub(Sp, transport(S, cayley_unitary(gen(a, b), h)))
    closed = is_zero(residue(S_lawful, alpha, beta))
    others_open = all(not is_zero(residue(S_lawful, a, b)) for a, b in grid if (a, b) != (alpha, beta))
    # unlawful transition: add a non-transport perturbation
    S_unlawful = m_add(S_lawful, mat([[sc(1, 0), 0], [0, sc(-1, 0)]]))
    open_all = all(not is_zero(residue(S_unlawful, a, b)) for a, b in grid)
    checks = {
        "lawful_transition_residue_zero_under_declared_pair": closed,
        "same_transition_open_under_every_other_grid_pair": others_open,
        "unlawful_transition_open_under_every_grid_pair": open_all,
    }
    return {"checks": checks}


def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_generators": t1_generators(),
        "t2_dock_exchange": t2_dock_exchange(),
        "t3_dock_bracket": t3_dock_bracket(),
        "t4_dock_determinant": t4_dock_determinant(),
        "t5_false_residue": t5_false_residue(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_DABAS_EULER_EMK_DOCK_CANDIDATE" if all(checks.values()) else "FAIL_DABAS_EULER_EMK_DOCK_CANDIDATE"
    return {
        "schema": "rkf.dabas_euler_emk_dock_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "R is the even (B-type) flow generator of the EMK span; iota I, iota K, iota RK are the odd (A-type) ones; K, RK, I are not flow generators; dagger grading and theorum/48's K-grading certified DIFFERENT",
                "DOCK (a): the DE connection generator alpha R + iota beta K obeys theorum/51's exchange law with alpha R = commutator inside channels and beta K = channel exchange",
                "DOCK (b): [alpha R, iota beta K] = 2 iota alpha beta RK (EMK bracket) and it is the leading h^2 residue of the Cayley commutator loop (cubic residual on dyadic h; commuting control exact)",
                "DOCK (c): det(M^dagger M) = (Delta_par + Delta_perp)^2; under the rational R-flow the total is invariant and the two EMK channels exchange",
                "DE false-residue prevention executable: lawful transition closed under its declared pair only; unlawful transition open under every pair",
            ],
            "NOT_claimed": [
                "an exact order-3 identity for the loop residual (only cubic scaling on dyadic h is certified)",
                "that the EMK 2x2 carrier is the only or the physical realization of the DE connection (de4's Gamma_mu term is declared residue, not modelled)",
                "any claim about Dabas-Euler measurement statistics, Born recoverability, or devices (de.tex Sec. 7-9)",
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
