from __future__ import annotations

"""Exact certificate (theorum/62): SILENCE–VIBRATION, SŪTRA-FLOW, AWARENESS-CATEGORY
canvases on the primitive carrier (second canvas batch, Aug 23 2026).

Eleven canvases read as hints.  Six were already handled by theorum/56
(Aghora, Asato Mā projector pipeline, Aṣṭādhyāyī rewrite, Om eigenmode,
Om λ-heat, Operator-Universe tower).  What is NEW and certifiable here:

 T1  SŪTRA-FLOW ▹ (short-circuit composition) and the Aṣṭādhyāyī canvas law
     "R_i ≻ R_j  ⇒  R_i R_j = R_i":  DISPROVED on the theorum/61 sandhi
     matrices (6.1.101 ≻ 6.1.77 yet R_101 R_77 ≠ R_101).  The lawful object
     is the priority step operator P_max of theorum/61 T5 (computed: P_max
     differs from every single R_k and from every product R_i R_j).
     "Commutators detect true conflicts; vanish under confluence":
     DISPROVED by theorum/61's enabling dependencies (gam with memory is
     CONFLUENT yet [R_7.3.77, R_6.1.73] ≠ 0).  Corrected: CONFLICT
     commutators vanish under confluence; enabling commutators need not.
 T2  VIBRATION FROM SILENCE = the Euler circular system on an odd generator.
     For anti-self-dagger D with D² = −ω²I (rational ω):
        Exp(tD) = Cos(ωt)·I + Sin(ωt)·D/ω   EXACTLY in the jet ring (depth 4),
     with Cos/Sin the native factorial jets (F00E Thm 5.3 circular system,
     5.4 Pythagorean identity re-verified in jets).  The "orthogonal
     companion" ψ⊥ = Dψ₁/ω; silence = ker D (T51 T3: odd generator creates
     the odd channel from the even one).  Control: a nilpotent odd generator
     (theorum/50's D₁) has Exp(tD) = I + tD — no oscillation, two-term law
     fails; the canvas's stability criterion Ω²=−ω²I is load-bearing.
 T3  AWARENESS CATEGORY on the theorum/60 reachable graph (objects = states,
     morphisms = reductions):  a TERMINAL object exists  ⟺  the verdict is
     CONFLUENT_MOD_LEDGER (gam with memory: terminal = gacchati; without:
     two sinks, no terminal).  Initial object = root.  "Collapse morphisms
     are absorbing" = normal forms are sinks (true).  "Every morphism
     factors through silence" DISPROVED: no arrow returns to the root
     (rewrites are irreversible, as the Sūtra-flow canvas itself says).
     Abstract note: initial + terminal + "all arrows factor through the
     initial object" forces a zero object and collapses the category to a
     preorder — the A-category as written has no further structure.
 T4  OM: nothing new certifiable beyond theorum/56 B5 (even/odd commuting
     split, m-torus gap = T49 instance).  The canvases' ω₁ = "smallest
     nonzero eigenvalue of a Laplacian" has no primitive-carrier object;
     the native analogue already present is theorum/50's uniform gap ρ.
 REFUSED (no statement / classical-analytic import): Operator-Universe
     Lagrangian (awareness metric g = ⟨X|A|Y⟩, Hodge dual, Bakry–Émery);
     Om–λ spectral unification (uniform ellipticity, L², heat trace);
     Gāyatrī pipeline (M, R, S, Π undefined — only their non-commutation is
     asserted; theorum/61's enabling chain is the nearest certified shape).
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.generalized_euler_emk_dock import I2, R, is_anti_self_dagger
from proof_lab.loop_residue_first_visible_jet_binding import DEPTH, j_add, j_const, j_mul, j_scale
from proof_lab.native_seam_gap_odd_covariance import eye, is_zero, m_add, m_scale, mat, sc, star, zeros
from proof_lab.paninian_seam_calculus import GAM, SANDHI, VOWELS
from proof_lab.rewrite_rules_as_cut_module_operators import realize, sp_mul, sp_sub
from proof_lab.seam_compensated_confluence_verdict import _priority_step, explore, step, word_rules


# ---------------------------------------------------------------- T1
def t1_sutra_flow() -> dict[str, Any]:
    sandhi = [(s, f) for s, f in SANDHI]
    states = set()
    for x in VOWELS:
        for y in VOWELS:
            states |= set(explore((x, y), sandhi)["states"])
    roots = sorted(states)
    idx = {W: i for i, W in enumerate(roots)}
    n = len(roots)
    mats = {}
    for r in sandhi:
        M = {}
        for W in roots:
            W2 = step(r, W)
            M[(idx[W] if W2 is None else idx[W2], idx[W])] = (Fraction(1), Fraction(0))
        mats[r[0]] = M
    Pm = {}
    for W in roots:
        W2 = _priority_step(W, sandhi)
        Pm[(idx[W] if W2 is None else idx[W2], idx[W])] = (Fraction(1), Fraction(0))
    hi, lo = mats["6.1.101"], mats["6.1.77"]
    canvas_law = sp_mul(hi, lo, n) == hi  # "R_i > R_j => R_i R_j = R_i"
    pmax_not_single = all(Pm != M for M in mats.values())
    pmax_not_product = all(Pm != sp_mul(mats[a], mats[b], n) for a in mats for b in mats)
    # enabling commutator nonzero under confluence (gam with memory)
    Rm = realize(GAM, word_rules(True))
    C = sp_sub(sp_mul(Rm["mats"]["7.3.77"], Rm["mats"]["6.1.73"], Rm["n"]), sp_mul(Rm["mats"]["6.1.73"], Rm["mats"]["7.3.77"], Rm["n"]))
    checks = {
        "canvas_law_Ri_Rj_eq_Ri_DISPROVED_on_6_1_101_over_6_1_77": not canvas_law,
        "priority_step_operator_is_not_any_single_rule_nor_any_product": pmax_not_single and pmax_not_product,
        "confluent_gam_with_memory_has_nonzero_enabling_commutator": bool(C),
    }
    return {"checks": checks, "sandhi_states": n}


# ---------------------------------------------------------------- T2
def cos_sin_jets(omega: Fraction):
    cos = [Fraction(0)] * (DEPTH + 1)
    sin = [Fraction(0)] * (DEPTH + 1)
    fact = 1
    for k in range(DEPTH + 1):
        fact = fact * k if k else 1
        if k % 2 == 0:
            cos[k] = (-1) ** (k // 2) * omega**k / fact
        else:
            sin[k] = (-1) ** ((k - 1) // 2) * omega**k / fact
    return cos, sin


def exp_jet_matrix(D):
    n = len(D)
    u = [zeros(n, n), D] + [zeros(n, n) for _ in range(DEPTH - 1)]
    acc = j_const(eye(n))
    power = j_const(eye(n))
    fact = 1
    for k in range(1, DEPTH + 1):
        power = j_mul(power, u)
        fact *= k
        acc = j_add(acc, j_scale(Fraction(1, fact), power))
    return acc


def scalar_jet_times(coeffs, M):
    return [m_scale(c, M) for c in coeffs]


def t2_vibration_from_silence() -> dict[str, Any]:
    ok = pyth = True
    for omega in (Fraction(1), Fraction(3, 2), Fraction(5)):
        D = m_scale(omega, R)  # EMK R: R^2 = -I  ->  D^2 = -omega^2 I
        assert is_anti_self_dagger(D) and star(D, D) == m_scale(-(omega**2), I2)
        lhs = exp_jet_matrix(D)
        cos, sin = cos_sin_jets(omega)
        rhs = j_add(scalar_jet_times(cos, I2), scalar_jet_times(sin, m_scale(Fraction(1) / omega, D)))
        ok &= lhs == rhs
        # F00E 5.4 in jets: Cos^2 + Sin^2 = 1
        c2 = [sum(cos[i] * cos[k - i] for i in range(k + 1)) for k in range(DEPTH + 1)]
        s2 = [sum(sin[i] * sin[k - i] for i in range(k + 1)) for k in range(DEPTH + 1)]
        pyth &= [c + s for c, s in zip(c2, s2)] == [Fraction(1)] + [Fraction(0)] * DEPTH
    # silence = ker D; companion = D psi / omega; 2-cycle: D psi_perp = -omega psi
    omega = Fraction(2)
    D = m_scale(omega, R)
    psi1 = mat([[sc(1)], [sc(0)]])
    perp = m_scale(Fraction(1) / omega, star(D, psi1))
    two_cycle = star(D, perp) == m_scale(-omega, psi1)
    # control: nilpotent odd generator of theorum/50 -> Exp = I + tD, no oscillation
    D1 = mat([[0, sc(0, 1)], [0, 0]])
    e1 = exp_jet_matrix(D1)
    nilp = e1[0] == eye(2) and e1[1] == D1 and all(is_zero(e1[k]) for k in range(2, DEPTH + 1))
    checks = {
        "Exp_tD_equals_Cos_I_plus_Sin_D_over_omega_exact_in_jets": ok,
        "F00E_5_4_Cos2_plus_Sin2_eq_1_in_jets": pyth,
        "orthogonal_companion_two_cycle_D_psi_perp_eq_minus_omega_psi": two_cycle,
        "control_nilpotent_odd_generator_no_oscillation": nilp,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T3
def t3_awareness_category() -> dict[str, Any]:
    out = {}
    for name, rules in (("with_memory", word_rules(True)), ("without_memory", word_rules(False))):
        g = explore(GAM, rules)
        sinks = [W for W in g["states"] if not g["edges"].get(W)]
        # terminal object: unique sink reachable from every state
        reach_all = all(any(_reaches(g, W, s) for s in sinks) for W in g["states"])
        terminal = len(sinks) == 1 and reach_all
        returns_to_root = any(GAM == v for W in g["states"] for _, v in g["edges"].get(W, []))
        out[name] = {"sinks": len(sinks), "terminal_exists": terminal, "arrow_back_to_root": returns_to_root}
    checks = {
        "terminal_object_exists_iff_confluent_with_memory_yes": out["with_memory"]["terminal_exists"],
        "terminal_object_absent_without_memory_two_sinks": (not out["without_memory"]["terminal_exists"]) and out["without_memory"]["sinks"] >= 2,
        "every_morphism_factors_through_silence_DISPROVED_no_return_arrows": not out["with_memory"]["arrow_back_to_root"] and not out["without_memory"]["arrow_back_to_root"],
    }
    return {"checks": checks, "graphs": out}


def _reaches(g, a, b) -> bool:
    seen, stack = {a}, [a]
    while stack:
        u = stack.pop()
        if u == b:
            return True
        for _, v in g["edges"].get(u, []):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return False


def build_certificate() -> dict[str, Any]:
    packets = {"t1_sutra_flow": t1_sutra_flow(), "t2_vibration_from_silence": t2_vibration_from_silence(), "t3_awareness_category": t3_awareness_category()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SILENCE_VIBRATION_SUTRA_FLOW_CANDIDATE" if all(checks.values()) else "FAIL_SILENCE_VIBRATION_SUTRA_FLOW_CANDIDATE"
    return {
        "schema": "rkf.silence_vibration_sutra_flow_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Sūtra-flow: 'R_i > R_j => R_i R_j = R_i' DISPROVED; the lawful priority object is the step operator P_max (not a single rule, not a product); 'commutators vanish under confluence' DISPROVED (enabling commutator nonzero on the confluent gam carrier)",
                "Vibration from silence: for anti-self-dagger D with D^2 = -omega^2 I, Exp(tD) = Cos(omega t) I + Sin(omega t) D/omega exactly in jets (F00E circular system); companion two-cycle; nilpotent control has no oscillation",
                "Awareness category on the reachable graph: terminal object exists iff CONFLUENT_MOD_LEDGER (gam with/without memory); no arrow returns to the root, so 'every morphism factors through silence' is false",
            ],
            "NOT_claimed": [
                "OM beyond theorum/56 B5; any Laplacian eigenvalue omega_1 (no primitive-carrier object)",
                "Operator-Universe Lagrangian, Om-lambda spectral unification, Gayatri pipeline (REFUSED: undefined operators or classical analytic imports)",
                "Asato Ma beyond theorum/56 B6 (projector products)",
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
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
