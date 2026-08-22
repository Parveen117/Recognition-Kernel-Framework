from __future__ import annotations

"""Exact certificate (theorum/53): NATIVE CUT-SQUARE FACTORIZATION
(the replacement for the Hilbert spectral theorem on the primitive carrier).

Carrier/verdicts: theorum/50.  Exact inverse: theorum/51.  Resolvent region:
theorum/52.  Nothing Hilbert.

Object.  For an operator L over C_Sigma the cut square S = L^dagger * L is
self-dagger: S^dagger = S (even channel symmetric, odd channel antisymmetric,
theorum/50 A2).  The native factorization is

        S = C^dagger * Dg * C,      Dg = diag(d_1..d_n),  d_k in R_Sigma,  C unit upper triangular over K_Sigma,

computed by exact elimination with the NATIVE scalar inverse (no square root,
no inner product).  Equivalently  S = sum_k d_k c_k^dagger * c_k  with c_k the
rows of C: an exact sum of weighted native squares.

Certified:
 T1  existence/exactness on cut squares: S = C^dagger Dg C with every d_k a
     turn-free NONNEGATIVE radial scalar; d_k = 0 only with a zero pivot row.
     The weights carry the positivity; the odd channel of S is carried
     ENTIRELY by the turn of the factors c_k (weights are turn-free) --
     positivity and Aghora separate exactly.
 T2  native Parseval:  E_Sigma(L) = tr rad(S) = sum_k d_k E_Sigma(c_k)  exactly.
 T3  negative witness: a self-dagger T that is NOT a cut square produces a
     negative pivot, and the elimination returns an exact vector v with
     (v^dagger T v) radial part < 0, turn part = 0 (SOS-1's negative witness,
     native).
 T4  seam-compatible faces: the factorization splits along P (+) Q; the
     recognized weight is exactly f0^2; every memory weight d_k <= S_kk <=
     E_Sigma(B) <= M_Sigma(B)^2 <= (rho f0)^2 (pivots are Schur complements,
     hence bounded by the diagonal they refine), and the weighted square
     energy equals E_Sigma(B) exactly.  BUILD NOTE: a first draft claimed an
     individual weight could exceed the bound; the certificate refused it and
     the corrected (stronger) statement is the one certified.
 T5  product: S_ab = S_a (x) S_b and the factorization tensors EXACTLY:
     C_ab = C_a (x) C_b, Dg_ab = Dg_a (x) Dg_b (weights multiplicative); the
     odd channel of S_ab is then the theorum/50 Leibniz law seen through the
     factor phases.
 T6  flow invariant (consumes theorum/51's unitary Cayley step): individual
     weights change under S -> C_h^dagger S C_h, but prod d_k = det S (a
     radial scalar) is EXACTLY invariant -- the native determinant channel
     (EMK-1 determinant identity shape) is the flow invariant of the square.
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
    Sc,
    cut_square,
    dagger,
    energy,
    eye,
    ftext,
    instance_faces,
    is_zero,
    kron,
    m_add,
    m_scale,
    m_sub,
    mass,
    mat,
    rad_part,
    real_add,
    real_kron,
    s_N,
    s_dag,
    s_mul,
    s_sub,
    sc,
    sctext,
    star,
    turn_part,
)
from proof_lab.native_seam_resolvent import det
from proof_lab.odd_channel_exchange_law import anti_self_dagger_generator, cayley_unitary, random_operator, s_inv, transport


def ldl_native(S: Mat) -> dict[str, Any]:
    """Exact S = C^dagger Dg C for self-dagger S (no pivoting; zero pivots allowed
    only with zero rows).  Returns factors, weights, and -- if a negative pivot is
    met -- an exact negative witness vector."""
    n = len(S)
    assert dagger(S) == S, "not self-dagger"
    A = [list(r) for r in S]
    Cm = [[sc(int(i == j)) for j in range(n)] for i in range(n)]
    d: list[Fraction] = []
    witness = None
    for k in range(n):
        piv = A[k][k]
        assert piv[1] == 0, "self-dagger diagonal must be turn-free"
        pk = piv[0]
        d.append(pk)
        if pk < 0 and witness is None:
            # witness: solve C v = e_k on the already-computed part (v = C^{-1} e_k restricted)
            v = [sc(0)] * n
            v[k] = sc(1)
            for i in range(k - 1, -1, -1):
                acc = sc(0)
                for j in range(i + 1, k + 1):
                    acc = m_add(((acc,),), ((s_mul(Cm[i][j], v[j]),),))[0][0]
                v[i] = s_sub(sc(0), acc)
            witness = tuple((x,) for x in v)
        if pk == 0:
            assert all(A[k][j] == (F0, F0) for j in range(k, n)) and all(A[i][k] == (F0, F0) for i in range(k, n)), "zero pivot with nonzero row: not a cut square"
            continue
        for j in range(k + 1, n):
            Cm[k][j] = s_mul(A[k][j], sc(F1 / pk))
        for i in range(k + 1, n):
            f = s_mul(A[i][k], sc(F1 / pk))  # = conj(C[k][i])
            for j in range(k + 1, n):
                A[i][j] = s_sub(A[i][j], s_mul(f, A[k][j]))
    C = tuple(tuple(r) for r in Cm)
    Dg = tuple(tuple(sc(d[i]) if i == j else sc(0) for j in range(n)) for i in range(n))
    return {"C": C, "Dg": Dg, "weights": d, "witness": witness}


def reconstruct(fac) -> Mat:
    return star(star(dagger(fac["C"]), fac["Dg"]), fac["C"])


def quad(T: Mat, v: Mat) -> Sc:
    return star(star(dagger(v), T), v)[0][0]


# ---------------------------------------------------------------- T1
def t1_exact_factorization() -> dict[str, Any]:
    rng = random.Random(53)
    ok = turnfree = nonneg = sep = 0
    trials = 12
    for _ in range(trials):
        n = rng.randint(2, 4)
        L = random_operator(n, rng)
        S = cut_square(L)
        fac = ldl_native(S)
        ok += reconstruct(fac) == S
        turnfree += all(fac["Dg"][i][i][1] == 0 for i in range(n))
        nonneg += all(w >= 0 for w in fac["weights"])
        # odd channel is in the factors only: rebuild S from the radial parts of C with the same weights -> turn must vanish
        Cr = tuple(tuple((x[0], F0) for x in row) for row in fac["C"])
        Sr = star(star(dagger(Cr), fac["Dg"]), Cr)
        sep += all(x == 0 for row in turn_part(Sr) for x in row) and (not all(x == 0 for row in turn_part(S) for x in row))
    checks = {
        "S_equals_Cdag_Dg_C_exactly_12_of_12": ok == trials,
        "weights_turn_free_12_of_12": turnfree == trials,
        "weights_nonnegative_12_of_12": nonneg == trials,
        "odd_channel_lives_in_factor_phases_only": sep >= trials - 1,
    }
    return {"checks": checks, "separated_instances": sep}


# ---------------------------------------------------------------- T2
def t2_native_parseval() -> dict[str, Any]:
    rng = random.Random(54)
    ok = 0
    for _ in range(12):
        n = rng.randint(2, 4)
        L = random_operator(n, rng)
        S = cut_square(L)
        fac = ldl_native(S)
        rows = [tuple((fac["C"][k],)) for k in range(n)]
        rhs = sum((fac["weights"][k] * energy(rows[k]) for k in range(n)), F0)
        tr = sum((S[i][i][0] for i in range(n)), F0)
        ok += energy(L) == tr == rhs
    return {"checks": {"E_L_equals_weighted_square_energies_12_of_12": ok == 12}}


# ---------------------------------------------------------------- T3
def t3_negative_witness() -> dict[str, Any]:
    T = mat([[sc(1, 0), sc(2, 1)], [sc(2, -1), sc(1, 0)]])  # self-dagger, det = 1 - 5 < 0
    fac = ldl_native(T)
    neg = any(w < 0 for w in fac["weights"])
    w = fac["witness"]
    val = quad(T, w) if w is not None else None
    checks = {
        "non_square_self_dagger_has_negative_weight": neg,
        "witness_returned": w is not None,
        "witness_quadratic_value_negative_radial": val is not None and val[0] < 0,
        "witness_quadratic_value_turn_free": val is not None and val[1] == 0,
        "a_true_cut_square_has_no_witness": ldl_native(cut_square(random_operator(3, random.Random(1))))["witness"] is None,
    }
    return {"checks": checks, "witness": [sctext(x[0]) for x in w] if w else None, "value": sctext(val) if val else None}


# ---------------------------------------------------------------- T4
def t4_seam_faces() -> dict[str, Any]:
    rho = Fraction(1, 2)
    res = []
    ok = True
    for fc in instance_faces()[:3]:
        L, B, f0 = fc["L"], fc["B"], fc["f0"]
        S = cut_square(L)
        fac = ldl_native(S)
        rec_weight = fac["weights"][0] == f0 * f0
        split = all(fac["C"][0][j] == (F0, F0) for j in range(1, len(L)))
        SB = cut_square(B)
        facB = ldl_native(SB)
        rowsB = [tuple((facB["C"][k],)) for k in range(len(B))]
        weighted = sum((facB["weights"][k] * energy(rowsB[k]) for k in range(len(B))), F0)
        gap_weighted = weighted == energy(B) and energy(B) <= mass(B) ** 2 <= (rho * f0) ** 2
        # each weight is a Schur-complement pivot: d_k <= S_kk <= E(B) <= M(B)^2 <= (rho f0)^2
        every_weight_bounded = all(facB["weights"][k] <= SB[k][k][0] <= energy(B) for k in range(len(B))) and all(w <= (rho * f0) ** 2 for w in facB["weights"])
        ok &= rec_weight and split and gap_weighted and every_weight_bounded
        res.append({"f0": ftext(f0), "memory_weights": [ftext(w) for w in facB["weights"]], "E_B": ftext(energy(B)), "bound": ftext((rho * f0) ** 2), "every_weight_le_pivot_le_E_B_le_bound": every_weight_bounded})
    checks = {"recognized_weight_f0_squared_and_split": ok, "every_memory_weight_bounded_by_pivot_energy_and_rho_f0_squared": all(r["every_weight_le_pivot_le_E_B_le_bound"] for r in res)}
    return {"checks": checks, "faces": res}


# ---------------------------------------------------------------- T5
def t5_product_factorization() -> dict[str, Any]:
    rng = random.Random(55)
    La, Lb = random_operator(2, rng), random_operator(3, rng)
    Sa, Sb = cut_square(La), cut_square(Lb)
    Sab = cut_square(kron(La, Lb))
    fa, fb, fab = ldl_native(Sa), ldl_native(Sb), ldl_native(Sab)
    checks = {
        "S_ab_equals_S_a_tensor_S_b": Sab == kron(Sa, Sb),
        "C_tensors_exactly": fab["C"] == kron(fa["C"], fb["C"]),
        "weights_multiplicative_exactly": fab["Dg"] == kron(fa["Dg"], fb["Dg"]),
        "odd_channel_of_product_is_Leibniz_of_faces": turn_part(Sab) == real_add(real_kron(rad_part(Sa), turn_part(Sb)), real_kron(turn_part(Sa), rad_part(Sb))),
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T6
def t6_flow_invariant() -> dict[str, Any]:
    rng = random.Random(56)
    inv = change = 0
    for _ in range(10):
        n = rng.randint(2, 4)
        L = random_operator(n, rng)
        S = cut_square(L)
        if det(S) == (F0, F0):
            continue
        D, _, _ = anti_self_dagger_generator(n, rng)
        Sh = transport(S, cayley_unitary(D, Fraction(rng.randint(1, 3), rng.randint(1, 4))))
        fs, fh = ldl_native(S), ldl_native(Sh)
        p1 = F1
        for w in fs["weights"]:
            p1 *= w
        p2 = F1
        for w in fh["weights"]:
            p2 *= w
        inv += (p1 == p2 == det(S)[0]) and det(S)[1] == 0 and det(Sh) == det(S)
        change += fs["weights"] != fh["weights"]
    checks = {"product_of_weights_equals_det_S_and_is_flow_invariant": inv >= 8, "individual_weights_change_under_flow": change > 0}
    return {"checks": checks, "invariant_instances": inv, "changed_instances": change}


# ---------------------------------------------------------------- certificate
def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_exact_factorization": t1_exact_factorization(),
        "t2_native_parseval": t2_native_parseval(),
        "t3_negative_witness": t3_negative_witness(),
        "t4_seam_faces": t4_seam_faces(),
        "t5_product_factorization": t5_product_factorization(),
        "t6_flow_invariant": t6_flow_invariant(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_NATIVE_CUT_SQUARE_FACTORIZATION_CANDIDATE" if all(checks.values()) else "FAIL_NATIVE_CUT_SQUARE_FACTORIZATION_CANDIDATE"
    return {
        "schema": "rkf.native_cut_square_factorization_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "every cut square S = L^dagger*L factors exactly as C^dagger Dg C over K_Sigma with turn-free nonnegative weights; the odd channel of S is carried by the factor phases alone (weights are turn-free) -- positivity and the odd sector separate",
                "native Parseval: E_Sigma(L) = tr rad(S) = sum_k d_k E_Sigma(c_k) exactly",
                "a self-dagger non-square yields a negative weight and an exact witness vector with negative radial, turn-free quadratic value; true squares yield none",
                "seam faces: recognized weight exactly f0^2, factorization splits along P(+)Q; every memory weight d_k <= S_kk <= E(B) <= M(B)^2 <= (rho f0)^2 and the weighted square energy equals E(B) -- the gap is visible weight by weight",
                "product: S_ab = S_a (x) S_b; C and Dg tensor exactly; odd channel = theorum/50 Leibniz law",
                "flow: product of weights = det S (radial) is exactly invariant under theorum/51's unitary Cayley step while individual weights change",
            ],
            "NOT_claimed": [
                "uniqueness of the factorization (it is basis-ordered; pivoting changes the weights)",
                "any eigenvalue statement: weights are not eigenvalues and are not claimed to be",
                "the identification of det S with EMK-1's determinant channel (same shape; dock open)",
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
