from __future__ import annotations

"""Exact certificate (theorum/54): INFINITE PRODUCT OF FACES AS A
RECOGNITION-COMPLETE LIMIT -- theorum/28's hypothesis list delivered on the
product carrier, with exact budgets.

Carrier/verdicts: theorum/50.  Gap law: theorum/50 T2.  Resolvent tails:
theorum/52 (same Smriti-tail discipline).  Nothing Hilbert.

Normalization.  Each face is scaled to recognized value 1:
        L~_i = L_i / f0_i = P_i (+) B~_i,     mu_i := M_Sigma(B~_i) = M_Sigma(B_i)/f0_i.
Finite packet n (theorum/28 Sec. 2, "transported to one common carrier"):
        Z_n = L~_1 (x) ... (x) L~_n (x) P_{n+1} (x) P_{n+2} (x) ...
i.e. faces beyond n are DECLARED recognized (the Smriti tail is "recognized
everywhere beyond n").  Every Z_n is a finite path element of the infinite
product groupoid: a finite sum over words w in {+,-}^N with finitely many
minus faces, each word carrying the block (x)_{i in w-} B~_i.

Certified:
 T1  consistency: for n <= 3 the word-block masses computed from the face
     masses equal the masses of the actual tensor-product blocks (exact kron).
 T2  sheet stationarity (recovered identity, theorum/28 Sec. 11 hyp. 1):
     for every word supported in faces <= n,  Z_{n+1} block == Z_n block exactly
     (the refinement arrow n -> n+1 is the identity on every already-present
     sheet; it only ADDS sheets with face n+1 minus).
 T3  channel Cauchy bounds (hyp. 2) with exact Smriti tails (hyp. 3):
        recognized channel   P Z_n P = P (all n)            -> rho^rec_n = 0
        memory channel       M(Z_{n+1} - Z_n) = Pi_n * mu_{n+1},   Pi_n = prod_{i<=n}(1+mu_i)
        tail(n)              sum_{k>n} M(Z_{k+1}-Z_k) <= Pi_inf * sum_{k>n} mu_k   (declared, closed form)
     With mu_i = a r^i (geometric) the tail is exact rational and -> 0.
 T4  uniform floor (hyp. 5) and outward margin (hyp. 6):  Z_n P = P exactly
     (floor 1); every memory word of the limit has block mass <= rho := sup mu_i,
     so u = rho, e_n = tail(n), and u + e_n < 1 for all n >= n_0 (n_0 computed).
 T5  SEPARATION OF TWO NOTIONS (the owner's question sharpened):
        uniform gap (theorum/50)  needs   sup mu_i < 1
        recognition-complete limit needs  sum mu_i < inf
     Control: constant mu_i = rho (not summable) -- the gap is uniform at every
     n (theorum/50 holds) yet M(Z_{n+1}-Z_n) = (1+rho)^n rho GROWS: no mass
     limit, the infinite product does not exist as a recognition-complete
     object.  Uniformity of the gap is strictly weaker than existence of the
     infinite product.
 T6  hypothesis ledger for theorum/28 Sec. 11 written to the certificate:
     1,2,3,5,6 DELIVERED with budgets; 4 (target-faithfulness residual for a
     declared observer T) NOT APPLICABLE here / NOT BUILT -- no observer is
     declared in this capsule.
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.native_seam_gap_odd_covariance import (
    F0,
    F1,
    Mat,
    cayley_step,
    face,
    flow_face,
    ftext,
    kron_all,
    m_scale,
    mass,
    mat,
    product_data,
    sc,
    sheet_projector,
    star,
)


def normalized_face(f0: Fraction, w: Fraction, h: Fraction) -> dict[str, Any]:
    D = mat([[0, sc(0, 1)], [0, 0]])
    fc = flow_face(f0, w, D, h)
    Ln = m_scale(F1 / f0, fc["L"])
    fc["Ln"] = Ln
    fc["Bn"] = m_scale(F1 / f0, fc["B"])
    fc["mu"] = mass(fc["Bn"])
    return fc


def geometric_faces(a: Fraction, r: Fraction, n: int) -> list[dict[str, Any]]:
    """Faces with mu_i = a r^i exactly: B~ = (a r^i / 2)(I + 0*D) has mass a r^i ... use w = a r^i / (2 + h) with h = 0
    -> cayley at h=0 is I; mass(w I_2) = 2w.  Keep a turn-carrying face via h=1: mass = w(2+1)=3w."""
    faces = []
    for i in range(1, n + 1):
        mu = a * r**i
        f0 = Fraction(2)
        fc = normalized_face(f0, mu * f0 / 3, Fraction(1))  # B = w C_1(D) = w(I + D), mass 3w -> mu = 3w/f0
        assert fc["mu"] == mu
        faces.append(fc)
    return faces


def word_mass(faces: list[dict[str, Any]], word: tuple[int, ...]) -> Fraction:
    m = F1
    for fc, s in zip(faces, word):
        m *= F1 if s == 1 else fc["mu"]
    return m


# ---------------------------------------------------------------- T1
def t1_consistency() -> dict[str, Any]:
    faces = geometric_faces(Fraction(1, 2), Fraction(1, 2), 3)
    ok = True
    for n in (1, 2, 3):
        fs = faces[:n]
        L = kron_all([fc["Ln"] for fc in fs])
        for w in itertools.product((1, -1), repeat=n):
            S = sheet_projector(fs, w)
            blk = star(star(S, L), S)
            ok &= mass(blk) == word_mass(fs, w)
    return {"checks": {"word_masses_equal_actual_block_masses_n_le_3": ok}}


# ---------------------------------------------------------------- T2
def t2_stationarity() -> dict[str, Any]:
    faces = geometric_faces(Fraction(1, 2), Fraction(1, 2), 4)
    ok = True
    for n in (1, 2, 3):
        fs, fs1 = faces[:n], faces[: n + 1]
        Ln = kron_all([fc["Ln"] for fc in fs])
        Ln1 = kron_all([fc["Ln"] for fc in fs1])
        # Z_n lives on n+1 faces with face n+1 recognized: Z_n = L_n (x) P_{n+1}
        Zn = kron_all([Ln, fs1[-1]["P"]])
        for w in itertools.product((1, -1), repeat=n):
            S = sheet_projector(fs1, w + (1,))
            ok &= star(star(S, Ln1), S) == star(star(S, Zn), S)
        # the difference is supported exactly on words with face n+1 minus
        diff = tuple(tuple((x[0] - y[0], x[1] - y[1]) for x, y in zip(r1, r2)) for r1, r2 in zip(Ln1, Zn))
        Splus = sheet_projector(fs1, (1,) * n + (1,))
        for w in itertools.product((1, -1), repeat=n):
            S = sheet_projector(fs1, w + (1,))
            ok &= all(x == (F0, F0) for row in star(star(S, diff), S) for x in row)
        Sminus_total = tuple(tuple((F0, F0) for _ in range(len(Ln1))) for _ in range(len(Ln1)))
    return {"checks": {"present_sheets_unchanged_by_refinement_n_le_3": ok}}


# ---------------------------------------------------------------- T3 / T4
def t3_t4_cauchy_tails_and_margin(a: Fraction, r: Fraction, nmax: int) -> dict[str, Any]:
    faces = geometric_faces(a, r, nmax)
    mus = [fc["mu"] for fc in faces]
    rho = max(mus)
    Pi_inf_bound = F1
    # prod (1+mu_i) <= exp(sum mu_i) is transcendental; use the exact finite product to nmax and
    # the declared bound prod_{i>nmax}(1+mu_i) <= 1 + 2*sum_{i>nmax} mu_i (valid since sum < 1/2 on instances)
    Pi_n = [F1]
    for mu in mus:
        Pi_n.append(Pi_n[-1] * (1 + mu))
    tail_sum = lambda n: a * r ** (n + 1) / (1 - r)  # sum_{k>n} a r^k exactly
    assert tail_sum(nmax) < Fraction(1, 2)
    Pi_inf_bound = Pi_n[-1] * (1 + 2 * tail_sum(nmax))
    rows = {}
    ok = True
    n0 = None
    for n in range(1, nmax):
        # exact mass of the increment from the word law: new words = (any word on <=n) x (face n+1 minus)
        inc_exact = Pi_n[n] * mus[n]
        # cross-check against actual kron for small n
        if n <= 3:
            fs1 = faces[: n + 1]
            Ln1 = kron_all([fc["Ln"] for fc in fs1])
            Zn = kron_all([kron_all([fc["Ln"] for fc in faces[:n]]), fs1[-1]["P"]])
            diff = tuple(tuple((x[0] - y[0], x[1] - y[1]) for x, y in zip(r1, r2)) for r1, r2 in zip(Ln1, Zn))
            ok &= mass(diff) == inc_exact
        tail = Pi_inf_bound * tail_sum(n)
        rec_cauchy = True  # P Z_n P = P exactly at every n (word ++...+ has mass 1, block = P): certified in T4 below
        margin = rho + tail < 1
        if margin and n0 is None:
            n0 = n
        rows[str(n)] = {"increment_mass": ftext(inc_exact), "declared_tail": ftext(tail), "u_plus_e_lt_1": margin}
    # floor and gap on the limit's memory words: any word with k>=1 minus faces has mass prod mu <= rho
    floor = True
    for n in (1, 2, 3):
        fs = faces[:n]
        Ln = kron_all([fc["Ln"] for fc in fs])
        P = kron_all([fc["P"] for fc in fs])
        floor &= star(Ln, P) == P and star(P, Ln) == P
    gap_words = all(word_mass(faces, w) <= rho for w in itertools.product((1, -1), repeat=nmax) if any(s == -1 for s in w))
    # declared tail-product bound, native justification: prod(1+x_i) = sum_k e_k(x) <= sum_k s^k = 1/(1-s) <= 1+2s for s <= 1/2
    s_all = sum(mus, F0)
    product_bound_holds = Pi_n[-1] <= 1 / (1 - s_all) <= 1 + 2 * s_all
    checks = {
        "finite_product_le_1_over_1_minus_sum_le_1_plus_2sum": product_bound_holds,
        "increment_mass_law_matches_kron_n_le_3": ok,
        "declared_tail_to_zero": tail_sum(nmax - 1) * Pi_inf_bound < tail_sum(0) * Pi_inf_bound / 100,
        "recognized_channel_exact_floor_1": floor,
        "every_memory_word_mass_le_rho": gap_words,
        "outward_margin_u_plus_e_lt_1_from_n0": n0 is not None and all(r["u_plus_e_lt_1"] for k, r in rows.items() if int(k) >= n0),
    }
    return {"checks": checks, "mu_i": "a r^i", "a": ftext(a), "r": ftext(r), "rho": ftext(rho), "Pi_inf_bound": ftext(Pi_inf_bound), "n0": n0, "per_n": rows}


# ---------------------------------------------------------------- T5
def t5_separation() -> dict[str, Any]:
    rho = Fraction(1, 2)
    faces = [normalized_face(Fraction(2), rho * 2 / 3, Fraction(1)) for _ in range(6)]
    assert all(fc["mu"] == rho for fc in faces)
    incs = [((1 + rho) ** n) * rho for n in range(1, 6)]
    growing = all(incs[i + 1] > incs[i] for i in range(len(incs) - 1))
    # the gap is still uniform: worst memory word mass = rho at every n (theorum/50)
    gap_uniform = all(max(word_mass(faces[:n], w) for w in itertools.product((1, -1), repeat=n) if any(s == -1 for s in w)) == rho for n in range(1, 7))
    # kron cross-check of growth at n=1,2
    ok = True
    for n in (1, 2):
        fs1 = faces[: n + 1]
        Ln1 = kron_all([fc["Ln"] for fc in fs1])
        Zn = kron_all([kron_all([fc["Ln"] for fc in faces[:n]]), fs1[-1]["P"]])
        diff = tuple(tuple((x[0] - y[0], x[1] - y[1]) for x, y in zip(r1, r2)) for r1, r2 in zip(Ln1, Zn))
        ok &= mass(diff) == incs[n - 1]
    checks = {
        "constant_mu_increments_grow_no_mass_limit": growing and ok,
        "gap_nevertheless_uniform_at_every_n": gap_uniform,
        "sum_mu_diverges_partial_sums_exceed_every_N_le_50": all(sum(rho for _ in range(2 * N + 2)) > N for N in range(1, 51)),
    }
    return {"checks": checks, "increments": [ftext(x) for x in incs]}


# ---------------------------------------------------------------- certificate
def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_consistency": t1_consistency(),
        "t2_stationarity": t2_stationarity(),
        "t3_t4_cauchy_tails_and_margin": t3_t4_cauchy_tails_and_margin(Fraction(1, 2), Fraction(1, 2), 12),
        "t5_separation": t5_separation(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_INFINITE_FACE_RECOGNITION_COMPLETION_CANDIDATE" if all(checks.values()) else "FAIL_INFINITE_FACE_RECOGNITION_COMPLETION_CANDIDATE"
    return {
        "schema": "rkf.infinite_face_recognition_completion_candidate.v1",
        "status": status,
        "theorum_28_section_11_ledger": {
            "1_recovered_identity_across_refinement_arrows": "DELIVERED: refinement n->n+1 is the exact identity on every present sheet (T2)",
            "2_recognized_and_memory_channel_cauchy_bounds": "DELIVERED: rho^rec_n = 0 exactly; memory increment mass Pi_n mu_{n+1} exact (T3)",
            "3_smriti_tail_bounds": "DELIVERED: declared closed-form tail Pi_inf_bound * sum_{k>n} mu_k, exact rational, -> 0 (T3)",
            "4_target_faithfulness_residual": "NOT APPLICABLE / NOT BUILT: no observer T declared in this capsule",
            "5_uniform_positive_recognized_floor": "DELIVERED: Z_n P = P, floor exactly 1 (T4)",
            "6_outward_finite_seam_margin": "DELIVERED: u = rho = sup mu_i, e_n = tail(n), u + e_n < 1 for n >= n0 (T4)",
        },
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "word-mass law equals actual tensor-block masses (n <= 3)",
                "sheet stationarity: refinement only adds sheets, never alters present ones",
                "memory-channel increments Pi_n mu_{n+1} exact; declared geometric Smriti tail -> 0; recognized channel exactly stationary",
                "floor 1 and outward margin u + e_n < 1 from a computed n0 (summable mu_i = a r^i)",
                "SEPARATION: sup mu < 1 gives the uniform gap (theorum/50) while sum mu < inf is needed for the infinite product to exist as a recognition-complete limit; constant mu = 1/2 has uniform gap and divergent increments",
            ],
            "NOT_claimed": [
                "existence of the limit in any topology other than cut-tail mass on finite-support path elements",
                "theorum/28 hyp. 4 (target faithfulness): no observer declared",
                "prod(1+mu_i) evaluated transcendentally: only the exact finite product times the declared bound 1+2*tail is used",
                "RH event family, RH, YM untouched",
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
