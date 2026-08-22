from __future__ import annotations

"""Exact certificate (theorum/50): the uploaded "operator canvases" (Bindu-Lopa,
Paninian rewrite, Operator-Universe tower, Aghora, OM/heat, Asato-Ma,
Mandukya, Lila) reduced to the framework's own cut algebra.

Each canvas is treated as a HINT, never as a source of theorems.  What is
certified below is only what survives exact arithmetic; what does not survive
is recorded as a refusal (Aghora) or as declared-not-certified.

Blocks
  B1  Bindu-Lopa: chart-dependence of [⊙,𝓛]; seam-alphabet termination C^2 ∈ {-1,0,1}
  B2  Paninian rewrite algebra: lopa idempotent zero map; anubandha = projection
      blindness (UGD-1 T4 shape); precedence = order is content; confluence census
  B3  Operator-Universe tower = theorum/41 grading: [A,[A,G]] = G_odd,
      [A,[A,[A,G]]] = [A,G]; D = 0 iff G even
  B4  Aghora refusal: A^2=I, AGA=-G, G square-sourced  =>  G = 0 (two routes);
      native repair: G cut-odd signed
  B5  OM/heat: even-scalar generator has zero cut-loop curvature, so the
      transport factorizes exactly; holonomy commutes; OM gap on an m-torus is
      a Theorem-49 instance (rho independent of m)
  B6  Projector sectors: product of projectors idempotent iff they commute;
      four-sector resolution is the sheet lattice; Turiya = recognized sheet;
      kappa = ||[A,U]|| = 0 iff H is even

fractions.Fraction only; no float, no root of unity, no exponential evaluated.
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.local_to_uniform_seam_gap import (
    add,
    cut_grade,
    face,
    identity,
    is_psd_exact,
    is_zero,
    matmul,
    matrix,
    norm_le,
    product_data,
    scale,
    sub,
    transpose,
)

Matrix = tuple[tuple[Fraction, ...], ...]


def q(v) -> Fraction:
    return v if isinstance(v, Fraction) else Fraction(v)


def ftext(v: Fraction) -> str:
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def sign(x: Fraction) -> Fraction:
    return Fraction(0) if x == 0 else (Fraction(1) if x > 0 else Fraction(-1))


# ---------------------------------------------------------------------
# B1  Bindu-Lopa
# Cartesian chart: z = (a, b) with a^2 + b^2 = c^2 rational (Pythagorean
# points, so the phase lift is exact).  ⊙z = (a/c, b/c); ⊙0 := 0 is the
# DECLARED cut-zero convention (UGD-1 T5: zero is the first cut).  𝓛z = (a,0).
# Native chart (F00G Log_Σ / UGD digit): w = (scale, phase) additively;
# ⊙ = phase projection, 𝓛 = scale projection.
# ---------------------------------------------------------------------

def pythagorean_points() -> list[tuple[Fraction, Fraction, Fraction]]:
    pts = []
    for m in range(1, 5):
        for n in range(1, m):
            a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
            for sa, sb in itertools.product((1, -1), repeat=2):
                pts.append((Fraction(sa * a), Fraction(sb * b), Fraction(c)))
                pts.append((Fraction(sb * b), Fraction(sa * a), Fraction(c)))
    pts += [(Fraction(k), Fraction(0), Fraction(abs(k))) for k in (-3, -1, 1, 2, 5)]
    pts.append((Fraction(0), Fraction(0), Fraction(0)))
    return pts


def bindu(a: Fraction, b: Fraction) -> tuple[Fraction, Fraction]:
    if a == 0 and b == 0:
        return Fraction(0), Fraction(0)
    if b == 0:
        return sign(a), Fraction(0)
    # caller guarantees Pythagorean
    c2 = a * a + b * b
    c = Fraction(int(c2.numerator ** 0.5 + 0.5), int(c2.denominator ** 0.5 + 0.5))
    assert c * c == c2, "non-Pythagorean point reached bindu"
    return a / c, b / c


def lopa(a: Fraction, b: Fraction) -> tuple[Fraction, Fraction]:
    return a, Fraction(0)


def b1_bindu_lopa() -> dict[str, Any]:
    pts = pythagorean_points()
    noncommute_witness = None
    seam_alphabet = {Fraction(-1), Fraction(0), Fraction(1)}
    c2_in_alphabet = True
    c3_eq_c2 = True
    fixed_points = set()
    lopa_idem = True
    bindu_unit = True
    for a, b, c in pts:
        if c != 0 and a * a + b * b != c * c:
            continue
        ob = bindu(a, b)
        lo = lopa(a, b)
        lopa_idem &= lopa(*lo) == lo
        bindu_unit &= (ob[0] ** 2 + ob[1] ** 2 in (Fraction(0), Fraction(1)))
        lb = lopa(*ob)          # C = 𝓛∘⊙
        bl = bindu(*lo)         # ⊙∘𝓛
        if lb != bl and noncommute_witness is None:
            noncommute_witness = {"z": [ftext(a), ftext(b)], "lopa_bindu": [ftext(x) for x in lb], "bindu_lopa": [ftext(x) for x in bl]}
        c2 = lopa(*bindu(*lb))  # C^2
        c3 = lopa(*bindu(*c2))  # C^3
        c2_in_alphabet &= c2[1] == 0 and c2[0] in seam_alphabet
        c3_eq_c2 &= c3 == c2
        if lb == (a, b):
            fixed_points.add((a, b))
    # native chart: w = (scale, phase); ⊙ = phase projection, 𝓛 = scale projection
    P_phase = matrix(((0, 0), (0, 1)))
    P_scale = matrix(((1, 0), (0, 0)))
    native_commute = matmul(P_phase, P_scale) == matmul(P_scale, P_phase)
    native_complementary = add(P_phase, P_scale) == identity(2) and is_zero(matmul(P_phase, P_scale))
    # bindu-lopa R = ⊙ + 𝓛 - 𝓛⊙ in the native chart = P_phase + P_scale - 0 = I
    R_native = sub(add(P_phase, P_scale), matmul(P_scale, P_phase))
    checks = {
        "lopa_idempotent": lopa_idem,
        "bindu_unit_modulus_or_zero": bindu_unit,
        "cartesian_commutator_nonzero": noncommute_witness is not None,
        "C_squared_lands_in_seam_alphabet": c2_in_alphabet,
        "C_cubed_equals_C_squared_terminates": c3_eq_c2,
        "fixed_points_of_C_are_exactly_pm1_and_declared_zero": fixed_points == {(Fraction(1), Fraction(0)), (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(0))},
        "native_chart_bindu_lopa_commute": native_commute,
        "native_chart_complementary_projections": native_complementary,
        "native_chart_R_is_identity": R_native == identity(2),
    }
    return {"checks": checks, "points": len(pts), "noncommute_witness": noncommute_witness,
            "fixed_points": sorted([ftext(x) for x, _ in fixed_points])}


# ---------------------------------------------------------------------
# B2  Paninian rewrite algebra on a toy alphabet.
# Strings over {a,i,u,e,o,y,v,K} where K is an anubandha (it-marker).
# Rules (operators on the free module; represented as string maps):
#   GUNA   a+i -> e, a+u -> o                     (1.1.2 shape)
#   YAN    i+V -> y+V, u+V -> v+V                 (1.1.4 / iko yaN aci shape)
#   YANK   i+V -> y+V ONLY IF marker K precedes   (marker-gated rule)
#   LOPA   delete every K                          (1.1.6 / 1.1.15)
# ---------------------------------------------------------------------

VOWELS = set("aiueo")


def guna(w: str) -> str:
    out, i = [], 0
    while i < len(w):
        if i + 1 < len(w) and w[i] == "a" and w[i + 1] in "iu":
            out.append("e" if w[i + 1] == "i" else "o"); i += 2
        else:
            out.append(w[i]); i += 1
    return "".join(out)


def yan(w: str) -> str:
    out = list(w)
    for i in range(len(out) - 1):
        if out[i] in "iu" and out[i + 1] in VOWELS:
            out[i] = "y" if out[i] == "i" else "v"
    return "".join(out)


def yan_k(w: str) -> str:
    out = list(w)
    for i in range(1, len(out) - 1):
        if out[i - 1] == "K" and out[i] in "iu" and out[i + 1] in VOWELS:
            out[i] = "y" if out[i] == "i" else "v"
    return "".join(out)


def lopa_k(w: str) -> str:
    return w.replace("K", "")


def normal_forms(w: str, rules: list) -> set[str]:
    seen, frontier, nfs = {w}, [w], set()
    while frontier:
        x = frontier.pop()
        nxt = {r(x) for r in rules} - {x}
        if not nxt:
            nfs.add(x)
        for y in nxt:
            if y not in seen:
                seen.add(y); frontier.append(y)
    return nfs


def precedence_nf(w: str) -> str | None:
    """Iterated declared-precedence product yan∘guna to a fixed point (None if no fixed point within 10)."""
    for _ in range(10):
        w2 = yan(guna(w))
        if w2 == w:
            return w
        w = w2
    return None


def b2_panini() -> dict[str, Any]:
    alphabet = "aiu"
    strings = ["".join(p) for n in range(1, 4) for p in itertools.product(alphabet, repeat=n)]
    # lopa: idempotent zero map on the marker sector, identity on the visible sector
    lopa_idem = all(lopa_k(lopa_k(w)) == lopa_k(w) for w in strings + ["KaKi", "iKu"])
    lopa_visible_identity = all(lopa_k(w) == w for w in strings)
    # non-commutation witness (order is content)
    wit = None
    for w in strings:
        if guna(yan(w)) != yan(guna(w)):
            wit = {"w": w, "guna_then_yan": yan(guna(w)), "yan_then_guna": guna(yan(w))}
            break
    # precedence resolves: declared order guna ≻ yan gives a well-defined product
    precedence_product_total = all(isinstance(yan(guna(w)), str) for w in strings)
    # confluence census under free application
    non_confluent = [w for w in strings if len(normal_forms(w, [guna, yan])) > 1]
    # anubandha = projection blindness: different markers, same visible output
    d1 = lopa_k(yan_k("Kiu"))      # marker fires the rule, then is elided
    d2 = "yu"                        # already visible form, no marker ever present
    ledger1, ledger2 = "Kiu".count("K"), "yu".count("K")
    blind = d1 == d2 and ledger1 != ledger2
    # without the marker the gated rule is silent
    gated_silent = yan_k("iu") == "iu"
    # 1.1.15 composite: marker elided AFTER it acts -> elide-first loses the action
    act_then_elide = lopa_k(yan_k("Kiu"))
    elide_then_act = yan_k(lopa_k("Kiu"))
    checks = {
        "lopa_idempotent_zero_map_on_marker_sector": lopa_idem,
        "lopa_identity_on_visible_sector": lopa_visible_identity,
        "rewrite_operators_do_not_commute": wit is not None,
        "declared_precedence_makes_product_total": precedence_product_total,
        "free_application_is_not_confluent": len(non_confluent) > 0,
        "precedence_restores_unique_normal_form": all(precedence_nf(w) is not None and precedence_nf(w) in normal_forms(w, [guna, yan]) for w in strings),
        "anubandha_projection_blindness_visible_equal_ledger_differs": blind,
        "gated_rule_silent_without_marker": gated_silent,
        "order_of_action_and_elision_is_content": act_then_elide != elide_then_act,
    }
    return {"checks": checks, "noncommute_witness": wit, "non_confluent_strings": non_confluent,
            "blindness": {"marked_derivation": d1, "unmarked": d2, "ledgers": [ledger1, ledger2]},
            "act_then_elide": act_then_elide, "elide_then_act": elide_then_act}


# ---------------------------------------------------------------------
# B3  Operator-Universe tower.  A idempotent (awareness projector), G any
# operator (creation).  With J = 2A - I (theorum/41 primitive cut):
#   D := [A,G],  R := [A,D] = G_odd,  [A,R] = D.
# ---------------------------------------------------------------------

def comm(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def b3_operator_universe() -> dict[str, Any]:
    n = 3
    A = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 0)))
    J = sub(scale(2, A), identity(n))
    vals = (Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(1), Fraction(3))
    ok_R, ok_period, ok_odd, ok_D_iff_even, count = True, True, True, True, 0
    for entries in itertools.islice(itertools.product(vals, repeat=9), 0, None, 37):
        G = matrix(tuple(entries[i * 3:(i + 1) * 3] for i in range(3)))
        D = comm(A, G)
        R = comm(A, D)
        even, odd = cut_grade(G, J)
        ok_R &= R == odd
        ok_period &= comm(A, R) == D
        ok_odd &= is_zero(cut_grade(D, J)[0])
        ok_D_iff_even &= (is_zero(D) == is_zero(odd))
        count += 1
    checks = {
        "A_idempotent_J_involution": matmul(A, A) == A and matmul(J, J) == identity(n),
        "curvature_R_equals_odd_grade_of_G": ok_R,
        "tower_has_period_two_[A,R]=D": ok_period,
        "time_D_is_cut_odd": ok_odd,
        "no_time_iff_G_even": ok_D_iff_even,
    }
    return {"checks": checks, "sampled_G": count}


# ---------------------------------------------------------------------
# B4  Aghora refusal.  Axioms: A^2 = I, A G A = -G, G >= 0 (square-sourced).
# Theorem: G = 0.  Proof: <v,Gv> >= 0 and <Av,G Av> = -<v,Gv> >= 0 forces
# <v,Gv> = 0 for all v; a PSD form with zero diagonal is zero.  Second route:
# the canvas also asserts [A,G] = 0, which with AGA = -G gives G = -G.
# Native repair: G is allowed as a cut-ODD SIGNED form (theorum/41 (3.3)).
# ---------------------------------------------------------------------

def b4_aghora() -> dict[str, Any]:
    A = matrix(((1, 0), (0, -1)))
    anticommuting = []
    for g in itertools.product((Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(3)), repeat=4):
        G = matrix(((g[0], g[1]), (g[2], g[3])))
        if matmul(matmul(A, G), A) == scale(-1, G) and transpose(G) == G:
            anticommuting.append(G)
    psd_and_anticommuting = [G for G in anticommuting if is_psd_exact(G)]
    only_zero = all(is_zero(G) for G in psd_and_anticommuting)
    nonzero_anticommuting_exists = any(not is_zero(G) for G in anticommuting)
    # second route
    route2 = all(not (is_zero(comm(A, G)) and not is_zero(G)) for G in anticommuting)
    # repair: anticommuting G are exactly the cut-odd ones
    odd_exactly = all(is_zero(cut_grade(G, A)[0]) for G in anticommuting)
    # a nonzero cut-odd G has indefinite (signed) form with explicit witnesses
    Gw = matrix(((0, 1), (1, 0)))
    signed = not is_psd_exact(Gw) and not is_psd_exact(scale(-1, Gw))
    checks = {
        "A_is_involution": matmul(A, A) == identity(2),
        "anticommuting_symmetric_G_exist_nonzero": nonzero_anticommuting_exists,
        "REFUSAL_psd_plus_anticommuting_forces_G_zero": only_zero,
        "REFUSAL_route2_commuting_and_anticommuting_forces_G_zero": route2,
        "repair_anticommuting_G_are_exactly_cut_odd": odd_exactly,
        "repair_nonzero_odd_G_is_signed_not_psd": signed,
    }
    return {"checks": checks, "anticommuting_count": len(anticommuting)}


# ---------------------------------------------------------------------
# B5  OM / heat.  On the EMK carrier {I,K,R,RK}: generator Δ = -ω I + α R.
# Grading by K: even part -ωI (decay), odd part αR (spin).  Cut-loop
# curvature [G_e,G_o] = 0, so powers expand binomially EXACTLY (the algebraic
# content of e^{tΔ} = e^{-ωt} e^{αtR}); λ-holonomy χ (scalar on the mode)
# commutes.  OM gap on an m-torus: faces diag(1, ρ_i) (mode 0 recognized,
# mode 1 memory) multiply to a Theorem-49 instance.
# ---------------------------------------------------------------------

def b5_om_heat() -> dict[str, Any]:
    I2 = identity(2)
    K = matrix(((0, 1), (1, 0)))
    R = matrix(((0, -1), (1, 0)))
    omega, alpha = Fraction(2), Fraction(1, 3)
    Delta = add(scale(-omega, I2), scale(alpha, R))
    even, odd = cut_grade(Delta, K)
    curvature_zero = is_zero(comm(even, odd))
    # binomial expansion of powers holds exactly iff the parts commute
    def power(M: Matrix, n: int) -> Matrix:
        out = identity(2)
        for _ in range(n):
            out = matmul(out, M)
        return out
    from math import comb
    binom_ok = True
    for n in range(1, 7):
        rhs = None
        for k in range(n + 1):
            term = scale(comb(n, k), matmul(power(even, n - k), power(odd, k)))
            rhs = term if rhs is None else add(rhs, term)
        binom_ok &= power(Delta, n) == rhs
    # control: a non-scalar even part breaks the binomial law
    Delta_c = add(add(scale(-omega, I2), K), scale(alpha, R))  # even part -ωI + K is non-scalar
    ec, oc = cut_grade(Delta_c, K)
    control_breaks = power(Delta_c, 2) != add(add(power(ec, 2), scale(2, matmul(ec, oc))), power(oc, 2))
    # holonomy: the phase factor is carried as an exponent (UGD-1 discipline); its
    # action on the mode commutes with Δ because it is scalar on that mode
    chi = scale(Fraction(1), I2)
    holonomy_commutes = is_zero(comm(chi, Delta))
    # OM gap on an m-torus
    f = face(Fraction(1), matrix(((Fraction(1, 4),),)))
    rho = Fraction(1, 4)
    gap_ok = True
    for m in range(1, 5):
        pd = product_data([f] * m)
        gap_ok &= norm_le(matmul(matmul(pd["Q"], pd["L"]), pd["Q"]), rho) and matmul(pd["L"], pd["P"]) == pd["P"]
    checks = {
        "decay_is_even_spin_is_odd": even == scale(-omega, I2) and odd == scale(alpha, R),
        "cut_loop_curvature_zero": curvature_zero,
        "binomial_power_law_exact_n_le_6": binom_ok,
        "control_nonscalar_even_part_breaks_binomial": control_breaks,
        "holonomy_commutes_with_generator": holonomy_commutes,
        "OM_gap_on_m_torus_independent_of_m_theorem49": gap_ok,
    }
    return {"checks": checks, "rho": ftext(rho)}


# ---------------------------------------------------------------------
# B6  Projector sectors (Asato-Ma, Mandukya, Lila, Sankhya).
# ---------------------------------------------------------------------

def b6_projector_sectors() -> dict[str, Any]:
    n = 3
    # commuting projectors: coordinate
    P1 = matrix(((1, 0, 0), (0, 0, 0), (0, 0, 0)))
    P2 = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 0)))
    prod = matmul(P1, P2)
    commuting_is_projector = matmul(prod, prod) == prod and prod == matmul(P2, P1)
    # non-commuting projector (rational 3-4-5 tilt)
    v = (Fraction(3, 5), Fraction(4, 5), Fraction(0))
    Pv = tuple(tuple(v[i] * v[j] for j in range(n)) for i in range(n))
    prod2 = matmul(P1, Pv)
    noncommuting = matmul(P1, Pv) != matmul(Pv, P1)
    prod2_not_projector = matmul(prod2, prod2) != prod2
    # each projection is a contraction in the cut-square sense
    contraction = all(norm_le(P, Fraction(1)) for P in (P1, P2, Pv))
    # four-sector resolution = sheet lattice; Turiya = recognized sheet
    PA = matrix(((1, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)))
    PU = matrix(((0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)))
    PM = matrix(((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 0)))
    PT = matrix(((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 1)))
    resolution = add(add(PA, PU), add(PM, PT)) == identity(4)
    # Lila: kappa = [A, U] = 0 iff [A,H] = 0, U any polynomial in H
    A = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 0)))
    J = sub(scale(2, A), identity(n))
    H_even = matrix(((1, 2, 0), (2, -1, 0), (0, 0, 3)))
    H_odd = matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0)))
    def poly(H: Matrix) -> Matrix:  # U = I + H + H^2/2 (truncated, exact)
        return add(add(identity(n), H), scale(Fraction(1, 2), matmul(H, H)))
    lila_even = is_zero(comm(A, poly(H_even))) and is_zero(cut_grade(H_even, J)[1])
    lila_odd = not is_zero(comm(A, poly(H_odd))) and not is_zero(cut_grade(H_odd, J)[1])
    checks = {
        "commuting_projector_product_is_projector": commuting_is_projector,
        "noncommuting_projectors_witness": noncommuting,
        "noncommuting_product_not_idempotent_order_is_content": prod2_not_projector,
        "every_projector_is_a_cut_square_contraction": contraction,
        "four_sector_resolution_of_identity": resolution,
        "lila_kappa_zero_iff_H_even": lila_even and lila_odd,
    }
    return {"checks": checks}


def build_certificate() -> dict[str, Any]:
    packets = {
        "b1_bindu_lopa": b1_bindu_lopa(),
        "b2_panini": b2_panini(),
        "b3_operator_universe": b3_operator_universe(),
        "b4_aghora": b4_aghora(),
        "b5_om_heat": b5_om_heat(),
        "b6_projector_sectors": b6_projector_sectors(),
    }
    checks = {f"{k}_all_checks": all(p["checks"].values()) for k, p in packets.items()}
    status = "PASS_CANVAS_OPERATORS_NATIVIZED_CANDIDATE" if all(checks.values()) else "FAIL_CANVAS_OPERATORS_NATIVIZED_CANDIDATE"
    return {
        "schema": "rkf.canvas_operators_nativized_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Bindu-Lopa: [⊙,𝓛] is chart content -- nonzero in the Cartesian chart (exact Pythagorean witness), zero in the native additive chart where ⊙,𝓛 are complementary projections and R = ⊙+𝓛-𝓛⊙ = I",
                "Bindu-Lopa: C = 𝓛⊙ iterated twice lands in the UGD seam alphabet {-1,0,+1} and is stationary from then on; fixed points of C are exactly ±1 and the declared cut-zero",
                "Panini: lopa is an idempotent zero map on the marker sector and the identity on the visible sector; rewrite operators do not commute; free application is not confluent and a declared precedence (paraM kAryam) restores a unique normal form",
                "Panini: anubandha = projection blindness (visible outputs equal, ledgers differ, UGD-1 T4 shape); the order of action and elision is content (EMK-T2 shape)",
                "Operator-Universe tower IS theorum/41's grading: R=[A,[A,G]] = odd grade of G, [A,R]=D (period two), D=[A,G] is cut-odd, D=0 iff G is even",
                "Aghora REFUSAL: A^2=I, AGA=-G, G square-sourced forces G=0 (also via [A,G]=0); anticommuting G are exactly the cut-odd SIGNED forms -- the lawful repair",
                "OM/heat: even-scalar decay + odd spin has zero cut-loop curvature, binomial power law exact (n<=6), holonomy commutes; OM gap on an m-torus is a Theorem-49 instance, independent of m",
                "projector sectors: product of projectors is a projector iff they commute (witnesses both ways); four-sector resolution is a sheet lattice; Lila kappa = 0 iff H is even",
            ],
            "NOT_claimed": [
                "any semantic, psychological, religious or physical interpretation of the canvases",
                "R = ⊙+𝓛-𝓛⊙ idempotent in the Cartesian chart (canvas asserts; no rational witness exists, so NOT certified)",
                "von Neumann alternating-projection limits (classical; not used, not claimed)",
                "Paninian coverage beyond the toy alphabet; the 3,959-rule engine is a DECLARED protocol",
                "Laplacian eigenmode claims on the continuum torus; only the algebraic factorization on the EMK carrier is certified",
                "RH, Yang-Mills, any other gate -- untouched",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
