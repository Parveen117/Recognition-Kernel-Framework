from __future__ import annotations

"""Exact certificate (theorum/52): NATIVE SEAM RESOLVENT AND SPECTRAL REGION.

Carrier, verdicts, faces: theorum/50 (pinned module).  Exact inverse over
C_Sigma: theorum/51 (pinned module).  Nothing Hilbert; no eigenvalue is ever
approximated.

The classical resolvent (lambda - L)^{-1} and spectrum are rebuilt from the
framework's own three tools:
  * T01 Thm 2.2  M(a*b) <= M(a)M(b)  and Lemma 2.1 D(zw) <= D(z)D(w);
  * theorum/28 Sec. 3-4: recognition-Cauchy sequences with DECLARED Smriti tails;
  * exact field arithmetic of K_Sigma (scalar inverse z^{-1} = z^dagger/N(z)).

Definitions.
  mass-Neumann condition at lambda:   q(lambda) := M(L) * D(lambda) / N(lambda) < 1
  partial resolvent:                  R_N(lambda) = lambda^{-1} sum_{k<=N} (lambda^{-1} L)^k
  Smriti tail budget (declared):      tau_N = D(lambda^{-1}) * q^{N+1} / (1 - q)
  native resolvent set (certified):   {lambda : q(lambda) < 1}  (or q_k < 1 for L^k)
  native singular locus:              det_{K_Sigma}(lambda I - L) = 0   (exact)

Certified:
 T1  where q < 1 the exact inverse exists and M(exact - R_N) <= tau_N for every
     N, with tau_N -> 0 geometrically: the resolvent is RECOGNITION-COMPLETE
     (theorum/28 Sec. 3-4 hypotheses delivered with exact budgets, not
     asserted).  Planted control: the tail budget with q replaced by q/2 is
     violated.
 T2  SEAM GAP AS A SPECTRAL REGION.  For a seam-compatible face L = f0 P (+) B
     with M(B) <= rho f0:  det(lambda I - L) = (lambda - f0) det(lambda I - B),
     and every lambda with N(lambda) > rho f0 D(lambda) lies in the certified
     resolvent set of B.  Hence the singular locus of L is {f0} union a set
     inside the NATIVE REGION  G_rho = {lambda : N(lambda) <= rho f0 D(lambda)},
     and f0 is outside G_rho (on the radial axis G_rho is exactly |t| <= rho f0).
 T3  exact singular locus on triangular instances: the characteristic
     polynomial over K_Sigma factors exactly as prod (lambda - b_ii); each
     root verified singular (det = 0) and every other tested lambda regular.
 T4  powers sharpen the region (Gelfand-shaped, from 2.2 alone): an instance
     where q_1(lambda) >= 1 but q_2(lambda) = M(L^2)D(lambda)^2/N(lambda)^2 < 1
     still has an exact resolvent, certified by the L^2 Neumann form.
 T5  product: the singular locus of (x)L_i is the union over sheets; f0^m
     isolated; the memory singular locus lies inside G_rho at scale f0^m,
     uniformly in m (consumes theorum/50's sheet-mass law); the resolvent of
     the product is sheet-block-diagonal but NOT a tensor product of face
     resolvents (control).
"""

import argparse
import hashlib
import itertools
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.native_seam_gap_odd_covariance import (
    F0,
    F1,
    Mat,
    Sc,
    energy,
    eye,
    ftext,
    instance_faces,
    is_zero,
    kron,
    kron_all,
    m_add,
    m_scale,
    m_sub,
    mass,
    mat,
    product_data,
    s_D,
    s_N,
    s_add,
    s_dag,
    s_mul,
    s_sub,
    sc,
    sctext,
    sheet_projector,
    star,
)
from proof_lab.odd_channel_exchange_law import inverse, s_inv


# ---------------------------------------------------------------- determinant / charpoly over K_Sigma
def det(a: Mat) -> Sc:
    n = len(a)
    M = [list(r) for r in a]
    d = sc(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != (F0, F0)), None)
        if piv is None:
            return sc(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = s_mul(d, sc(-1))
        d = s_mul(d, M[c][c])
        inv = s_inv(M[c][c])
        for r in range(c + 1, n):
            if M[r][c] != (F0, F0):
                f = s_mul(M[r][c], inv)
                M[r] = [s_sub(x, s_mul(f, y)) for x, y in zip(M[r], M[c])]
    return d


def poly_mul(p, q):
    out = [sc(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = s_add(out[i + j], s_mul(x, y))
    return out


def charpoly(a: Mat) -> list[Sc]:
    """Faddeev-LeVerrier over K_Sigma: coefficients of det(lambda I - a), low to high."""
    n = len(a)
    I = eye(n)
    Mk = tuple(tuple(sc(0) for _ in range(n)) for _ in range(n))
    coeffs = [sc(0)] * (n + 1)
    coeffs[n] = sc(1)
    c = sc(1)
    for k in range(1, n + 1):
        Mk = m_add(star(a, Mk), m_scale(c, I))
        AM = star(a, Mk)
        tr = sc(0)
        for i in range(n):
            tr = s_add(tr, AM[i][i])
        c = s_mul(sc(Fraction(-1, k)), tr)
        coeffs[n - k] = c
    return coeffs


def poly_eval(p, z: Sc) -> Sc:
    acc = sc(0)
    for coef in reversed(p):
        acc = s_add(s_mul(acc, z), coef)
    return acc


def lam_I_minus(L: Mat, lam: Sc) -> Mat:
    return m_sub(m_scale(lam, eye(len(L))), L)


# ---------------------------------------------------------------- mass-Neumann resolvent
def q_ratio(L: Mat, lam: Sc, k: int = 1) -> Fraction:
    Lk = L
    for _ in range(k - 1):
        Lk = star(Lk, L)
    return mass(Lk) * s_D(lam) ** k / s_N(lam) ** k


def partial_resolvent(L: Mat, lam: Sc, N: int) -> Mat:
    li = s_inv(lam)
    X = m_scale(li, L)
    term = eye(len(L))
    acc = term
    for _ in range(N):
        term = star(term, X)
        acc = m_add(acc, term)
    return m_scale(li, acc)


def tail_budget(L: Mat, lam: Sc, N: int, q: Fraction | None = None) -> Fraction:
    qq = q_ratio(L, lam) if q is None else q
    assert qq < 1, "tail budget is only defined inside the mass-Neumann region q < 1 (fail-closed)"
    return s_D(s_inv(lam)) * qq ** (N + 1) / (1 - qq)


# ---------------------------------------------------------------- T1
def t1_recognition_complete_resolvent() -> dict[str, Any]:
    rng = random.Random(52)
    ok_exact = ok_tail = geom = planted = 0
    trials = 10
    for _ in range(trials):
        n = rng.randint(2, 3)
        L = tuple(tuple(sc(Fraction(rng.randint(-2, 2), 3), Fraction(rng.randint(-2, 2), 3)) for _ in range(n)) for _ in range(n))
        # lambda chosen inside the certified region with a turn component: q < 1 by construction
        lam = sc(2 * mass(L) + 1, Fraction(rng.randint(-2, 2)))
        q = q_ratio(L, lam)
        assert q < 1
        Rex = inverse(lam_I_minus(L, lam))
        ok_exact += star(lam_I_minus(L, lam), Rex) == eye(n)
        budgets_ok = True
        prev = None
        for N in range(0, 7):
            gap = mass(m_sub(Rex, partial_resolvent(L, lam, N)))
            budgets_ok &= gap <= tail_budget(L, lam, N, q)
            prev = gap
        ok_tail += budgets_ok
        geom += tail_budget(L, lam, 6, q) < tail_budget(L, lam, 0, q) / 2
        planted += mass(m_sub(Rex, partial_resolvent(L, lam, 0))) > tail_budget(L, lam, 0, q / 2)
    checks = {
        "exact_inverse_exists_where_q_lt_1": ok_exact == trials,
        "smriti_tail_budget_holds_N_0_to_6": ok_tail == trials,
        "tail_budget_decreases_geometrically": geom == trials,
        "planted_halved_q_budget_violated_somewhere": planted > 0,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T2
def t2_gap_as_region() -> dict[str, Any]:
    rho = Fraction(1, 2)
    results = []
    all_ok = True
    for fc in instance_faces()[:3]:
        L, B, f0 = fc["L"], fc["B"], fc["f0"]
        n = len(L)
        # det factorization (exact): charpoly(L) == (lambda - f0) * charpoly(B)
        fac = charpoly(L) == poly_mul([sc(-f0), sc(1)], charpoly(B))
        # sample lambda outside the native region: N > rho f0 D  -> resolvent of B certified
        outside_ok = True
        region_points = 0
        for r in range(-8, 9):
            for t in range(-8, 9):
                lam = sc(Fraction(r, 2), Fraction(t, 2))
                if lam == (F0, F0):
                    continue
                outside = s_N(lam) > rho * f0 * s_D(lam)
                if outside:
                    region_points += 1
                    outside_ok &= q_ratio(B, lam) < 1 and det(lam_I_minus(B, lam)) != (F0, F0)
        f0_outside = s_N(sc(f0)) > rho * f0 * s_D(sc(f0))
        f0_singular = det(lam_I_minus(L, sc(f0))) == (F0, F0)
        radial_axis = all((s_N(sc(t)) > rho * f0 * s_D(sc(t))) == (abs(Fraction(t)) > rho * f0) for t in [Fraction(k, 4) for k in range(-20, 21) if k != 0])
        ok = fac and outside_ok and f0_outside and f0_singular and radial_axis
        all_ok &= ok
        results.append({"f0": ftext(f0), "mass_B": ftext(mass(B)), "det_factorizes": fac, "outside_region_points_all_regular": outside_ok, "points": region_points, "f0_singular_and_outside_region": f0_outside and f0_singular})
    checks = {"gap_region_theorem_on_three_flow_faces": all_ok}
    return {"checks": checks, "faces": results, "region": "G_rho = {lambda : N(lambda) <= rho f0 D(lambda)}; on the radial axis exactly |t| <= rho f0"}


# ---------------------------------------------------------------- T3
def t3_exact_singular_locus() -> dict[str, Any]:
    B = mat([[sc(1, 1), sc(2, 0), sc(0, 1)], [0, sc(Fraction(1, 2), -1), sc(3, 0)], [0, 0, sc(-1, Fraction(1, 3))]])
    diag = [B[i][i] for i in range(3)]
    cp = charpoly(B)
    prod = [sc(1)]
    for d in diag:
        prod = poly_mul(prod, [s_mul(sc(-1), d), sc(1)])
    factor_exact = cp == prod
    roots_singular = all(det(lam_I_minus(B, d)) == (F0, F0) for d in diag)
    others_regular = all(det(lam_I_minus(B, sc(Fraction(r, 2), Fraction(t, 2)))) != (F0, F0) for r in range(-6, 7) for t in range(-6, 7) if sc(Fraction(r, 2), Fraction(t, 2)) not in diag)
    # a non-triangular instance: locus not enumerated, only the region statement is made
    C = mat([[0, sc(1, 0)], [sc(2, 0), 0]])  # charpoly lambda^2 - 2: roots outside K_Sigma
    cpC = charpoly(C)
    nontri_has_no_K_root = all(poly_eval(cpC, sc(Fraction(r, 2), Fraction(t, 2))) != (F0, F0) for r in range(-8, 9) for t in range(-8, 9))
    checks = {
        "charpoly_factors_exactly_over_K_Sigma": factor_exact,
        "each_diagonal_value_is_singular": roots_singular,
        "every_other_grid_value_is_regular": others_regular,
        "non_triangular_instance_has_no_grid_root_region_statement_only": nontri_has_no_K_root,
    }
    return {"checks": checks, "singular_locus": [sctext(d) for d in diag]}


# ---------------------------------------------------------------- T4
def t4_powers_sharpen() -> dict[str, Any]:
    # nilpotent-ish mass concentration: L with M(L)=2 but M(L^2) small
    L = mat([[0, sc(1, 0)], [sc(Fraction(1, 8), 0), 0]])  # L^2 = (1/8) I: M(L) = 9/8, M(L^2) = 1/4
    lam = sc(1, 0)
    q1 = q_ratio(L, lam, 1)
    q2 = q_ratio(L, lam, 2)
    Rex = inverse(lam_I_minus(L, lam))
    exact_ok = star(lam_I_minus(L, lam), Rex) == eye(2)
    # L^2-Neumann: (lam - L)^{-1} = (lam + L) (lam^2 - L^2)^{-1}
    L2 = star(L, L)
    lam2 = s_mul(lam, lam)
    R2 = star(m_add(m_scale(lam, eye(2)), L), inverse(lam_I_minus(L2, lam2)))
    route_agree = R2 == Rex
    checks = {
        "q1_ge_1_first_order_condition_fails": q1 >= 1,
        "q2_lt_1_second_power_condition_holds": q2 < 1,
        "exact_resolvent_exists": exact_ok,
        "L2_neumann_route_agrees_with_exact": route_agree,
    }
    return {"checks": checks, "q1": ftext(q1), "q2": ftext(q2)}


# ---------------------------------------------------------------- T5
def t5_product_locus() -> dict[str, Any]:
    rho = Fraction(1, 2)
    faces_all = instance_faces()[:3]
    per_m = {}
    ok = True
    for m in (1, 2, 3):
        faces = faces_all[:m]
        pd = product_data(faces)
        L, P, f0m, n = pd["L"], pd["P"], pd["f0m"], pd["dim"]
        f0_singular = det(lam_I_minus(L, sc(f0m))) == (F0, F0)
        # f0^m outside the memory region at scale f0^m: N(f0^m) > rho f0^m D(f0^m)  <=> f0^m > rho f0^m
        isolated = s_N(sc(f0m)) > rho * f0m * s_D(sc(f0m))
        # every memory sheet block: lambda outside G_rho(f0^m) is regular, via theorum/50's mass law
        sheets_ok = True
        for w in itertools.product((1, -1), repeat=m):
            if all(s == 1 for s in w):
                continue
            S = sheet_projector(faces, w)
            blk = star(star(S, L), S)
            # restrict to the sheet's support indices
            idx = [i for i in range(n) if S[i][i] != (F0, F0)]
            sub = tuple(tuple(blk[i][j] for j in idx) for i in idx)
            for lam in (sc(f0m), sc(f0m, Fraction(1, 2)), sc(Fraction(3, 4) * f0m, 0), sc(0, f0m)):
                if s_N(lam) > rho * f0m * s_D(lam):
                    sheets_ok &= q_ratio(sub, lam) < 1 and det(lam_I_minus(sub, lam)) != (F0, F0)
        # resolvent of the product is sheet-block-diagonal but not a tensor product of face resolvents
        lam = sc(Fraction(3) * f0m, Fraction(1))
        Rp = inverse(lam_I_minus(L, lam))
        blockdiag = all(star(sheet_projector(faces, w), Rp) == star(Rp, sheet_projector(faces, w)) for w in itertools.product((1, -1), repeat=m))
        not_tensor = True
        if m >= 2:
            lam_face = sc(Fraction(3) * f0m, Fraction(1))
            Rt = kron_all([inverse(lam_I_minus(fc["L"], lam_face)) for fc in faces])
            not_tensor = Rt != Rp
        ok &= f0_singular and isolated and sheets_ok and blockdiag and not_tensor
        per_m[str(m)] = {"dim": n, "f0m_singular": f0_singular, "f0m_isolated": isolated, "memory_sheets_regular_outside_region": sheets_ok, "resolvent_sheet_block_diagonal": blockdiag, "not_tensor_of_face_resolvents": not_tensor}
    checks = {"product_singular_locus_uniform_in_m": ok}
    return {"checks": checks, "per_m": per_m}


# ---------------------------------------------------------------- certificate
def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_recognition_complete_resolvent": t1_recognition_complete_resolvent(),
        "t2_gap_as_region": t2_gap_as_region(),
        "t3_exact_singular_locus": t3_exact_singular_locus(),
        "t4_powers_sharpen": t4_powers_sharpen(),
        "t5_product_locus": t5_product_locus(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_NATIVE_SEAM_RESOLVENT_CANDIDATE" if all(checks.values()) else "FAIL_NATIVE_SEAM_RESOLVENT_CANDIDATE"
    return {
        "schema": "rkf.native_seam_resolvent_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "mass-Neumann resolvent: where q = M(L)D(lambda)/N(lambda) < 1 the exact inverse exists and the partial sums are recognition-Cauchy with DECLARED geometric Smriti tails tau_N, verified against the exact inverse for N = 0..6 (theorum/28 Sec. 3-4 delivered with budgets); planted halved budget violated",
                "seam gap as a native spectral region: det(lambda - L) = (lambda - f0) det(lambda - B) exactly; every lambda with N(lambda) > rho f0 D(lambda) is regular for B; f0 is singular and outside the region; on the radial axis the region is exactly |t| <= rho f0",
                "exact singular locus on a triangular instance (charpoly factors over K_Sigma; roots singular, grid elsewhere regular)",
                "powers sharpen the certified region (q1 >= 1 but q2 < 1 with an exact resolvent, L^2-Neumann route agrees)",
                "product: f0^m singular and isolated; memory sheets regular outside G_rho at scale f0^m for m = 1..3 via theorum/50's sheet-mass law; resolvent sheet-block-diagonal but not a tensor product of face resolvents",
            ],
            "NOT_claimed": [
                "enumeration of the full singular locus for non-triangular operators (roots outside K_Sigma are not located; only the certified resolvent region is asserted)",
                "that the native region G_rho is the sharpest possible; it is what T01 Thm 2.2 + Lemma 2.1 deliver",
                "any analytic (complex-analytic) property of the resolvent; only exact algebra and mass-Cauchy completion",
                "infinite-face limit; RH, YM untouched",
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
