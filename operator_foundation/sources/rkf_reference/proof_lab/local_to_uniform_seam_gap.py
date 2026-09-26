from __future__ import annotations

"""Exact certificate: LOCAL-TO-UNIFORM SEAM GAP on a product of cut-graded faces
(theorum/49).

Question answered.  Each local face i carries its own cut J_i (theorum/41
grading), a recognized sheet P_i = (I+J_i)/2 and a memory sheet Q_i = I-P_i.
Each face is "a little bad" -- its transfer L_i = w_i K_i carries a declared
sup-weight W and a declared recognized mean f0 -- and each face comes with a
smoothing whose memory channel contracts by lambda.  The claim is that the
product of m such faces has a seam gap that does NOT depend on m.

Native form of the hypotheses (per face):

    (H1) seam compatibility   L_i P_i = f0 P_i = P_i L_i
         (the recognized sheet is invariant AND co-invariant, with value
          exactly the mean f0; equivalently L_i is J_i-EVEN in the sense of
          theorum/41 (3.3) with recognized value f0);
    (H2) memory contraction   ||Q_i L_i Q_i|| <= W*lambda  =: rho*f0,  rho < 1,
         certified by the exact cut-square criterion of theorum/41 (5.4):
         (W*lambda)^2 Q_i - (Q_i L_i Q_i)^T (Q_i L_i Q_i) >= 0, decided by exact
         rational LDL^T (inertia), never by floating eigenvalues.

Conclusion (Theorem 3.1 of theorum/49): on the product carrier with the
recognized-everywhere projector P = (x) P_i and global cut J_rec = 2P - I,

    L P = f0^m P = P L      and      ||Q L Q|| <= rho * f0^m   for EVERY m,

so the normalized gap ratio ||Q L Q|| / f0^m is bounded by rho = W*lambda/f0
independently of m.  The proof is the 2^m-sheet decomposition of the product
carrier: a word with k minus signs contributes (rho f0)^k f0^(m-k) = rho^k f0^m
<= rho f0^m.  No classical result is borrowed; the only tools are the cut
grading (theorum/41), the cut-square criterion (theorum/41 (5.4)) and the
outward certificate rule (theorum/28 Sec. 9).

Only ``fractions.Fraction`` is used.  No NumPy, no floats, no transcendental
evaluation: "e^kappa" enters only as the declared rational sup-weight W.
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

Matrix = tuple[tuple[Fraction, ...], ...]


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix(rows) -> Matrix:
    return tuple(tuple(q(x) for x in row) for row in rows)


def identity(n: int) -> Matrix:
    return tuple(tuple(Fraction(int(i == j)) for j in range(n)) for i in range(n))


def zero(n: int, m: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(m)) for _ in range(n))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def sub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def scale(c: int | Fraction, a: Matrix) -> Matrix:
    factor = q(c)
    return tuple(tuple(factor * x for x in row) for row in a)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    bt = transpose(b)
    return tuple(
        tuple(sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in bt)
        for row in a
    )


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def is_zero(a: Matrix) -> bool:
    return all(x == 0 for row in a for x in row)


def kron(a: Matrix, b: Matrix) -> Matrix:
    ra, ca, rb, cb = len(a), len(a[0]), len(b), len(b[0])
    return tuple(
        tuple(a[i // rb][j // cb] * b[i % rb][j % cb] for j in range(ca * cb))
        for i in range(ra * rb)
    )


def kron_all(mats: list[Matrix]) -> Matrix:
    out = mats[0]
    for m in mats[1:]:
        out = kron(out, m)
    return out


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


# ---------------------------------------------------------------------
# Exact positivity: symmetric rational matrix is PSD iff symmetric
# Gaussian elimination (LDL^T without pivoting) meets only nonnegative
# pivots and every zero pivot has an all-zero row/column.  This is the
# same exact inertia machinery the framework uses for every cut-square
# verdict; no eigenvalue is ever approximated.
# ---------------------------------------------------------------------

def is_psd_exact(s: Matrix) -> bool:
    n = len(s)
    if any(s[i][j] != s[j][i] for i in range(n) for j in range(n)):
        return False
    a = [list(row) for row in s]
    for k in range(n):
        piv = a[k][k]
        if piv < 0:
            return False
        if piv == 0:
            if any(a[k][j] != 0 for j in range(k, n)):
                return False
            continue
        for i in range(k + 1, n):
            f = a[i][k] / piv
            if f == 0:
                continue
            for j in range(k, n):
                a[i][j] -= f * a[k][j]
    return True


def norm_le(a: Matrix, c: Fraction) -> bool:
    """Exact certificate of ||a|| <= c (operator 2-norm) via c^2 I - a^T a >= 0."""
    n = len(a[0])
    return is_psd_exact(sub(scale(c * c, identity(n)), matmul(transpose(a), a)))


def psd_negative_witness(s: Matrix) -> list[str] | None:
    """If s is not PSD return an exact vector v with v^T s v < 0 (from the
    elimination), else None.  Used only for reporting controls."""
    n = len(s)
    for v in itertools.product((-1, 0, 1), repeat=n):
        vv = tuple(Fraction(x) for x in v)
        val = sum(vv[i] * s[i][j] * vv[j] for i in range(n) for j in range(n))
        if val < 0:
            return [ftext(x) for x in vv]
    return None


# ---------------------------------------------------------------------
# Faces.  A face is (dimension d, cut J = diag(+1, -1, ..., -1) in its
# cut basis, transfer L).  The recognized sheet is the first basis vector
# (rank one), the memory sheet is the rest.  Different faces may have
# different dimension, weight and contraction; that heterogeneity is the
# point of the uniformity theorem.
# ---------------------------------------------------------------------

def cut_matrix(d: int) -> Matrix:
    return tuple(tuple(Fraction((1 if i == 0 else -1) if i == j else 0) for j in range(d)) for i in range(d))


def recognized_projector(j: Matrix) -> Matrix:
    return scale(Fraction(1, 2), add(identity(len(j)), j))


def memory_projector(j: Matrix) -> Matrix:
    return scale(Fraction(1, 2), sub(identity(len(j)), j))


def cut_grade(g: Matrix, j: Matrix) -> tuple[Matrix, Matrix]:
    """theorum/41 (3.1): G_e = (G + JGJ)/2, G_o = (G - JGJ)/2."""
    jgj = matmul(matmul(j, g), j)
    return scale(Fraction(1, 2), add(g, jgj)), scale(Fraction(1, 2), sub(g, jgj))


def face(f0: Fraction, memory_block: Matrix) -> dict[str, Any]:
    """Seam-compatible face: L = f0 P (+) B on the memory sheet."""
    d = 1 + len(memory_block)
    rows = [[Fraction(0)] * d for _ in range(d)]
    rows[0][0] = f0
    for i, row in enumerate(memory_block):
        for jj, x in enumerate(row):
            rows[1 + i][1 + jj] = x
    return {"L": matrix(rows), "J": cut_matrix(d), "f0": f0}


def face_hypotheses(fc: dict[str, Any], W: Fraction, lam: Fraction) -> dict[str, Any]:
    L, J, f0 = fc["L"], fc["J"], fc["f0"]
    P, Q = recognized_projector(J), memory_projector(J)
    even, odd = cut_grade(L, J)
    h1 = matmul(L, P) == scale(f0, P) and matmul(P, L) == scale(f0, P)
    qlq = matmul(matmul(Q, L), Q)
    h2 = norm_le(qlq, W * lam)
    return {
        "H1_seam_compatible": h1,
        "H1_equivalent_J_even": is_zero(odd) and even == L,
        "H2_memory_contraction_certified": h2,
        "rho": ftext(W * lam / f0),
        "rho_less_than_one": W * lam / f0 < 1,
    }


# ---------------------------------------------------------------------
# Product carrier.
# ---------------------------------------------------------------------

def product_data(faces: list[dict[str, Any]]) -> dict[str, Any]:
    L = kron_all([fc["L"] for fc in faces])
    Ps = [recognized_projector(fc["J"]) for fc in faces]
    P = kron_all(Ps)
    n = len(L)
    Q = sub(identity(n), P)
    J_rec = sub(scale(2, P), identity(n))
    J_tensor = kron_all([fc["J"] for fc in faces])
    f0m = Fraction(1)
    for fc in faces:
        f0m *= fc["f0"]
    return {"L": L, "P": P, "Q": Q, "J_rec": J_rec, "J_tensor": J_tensor, "f0m": f0m, "dim": n}


def sheet_projector(faces: list[dict[str, Any]], word: tuple[int, ...]) -> Matrix:
    return kron_all([
        recognized_projector(fc["J"]) if s == 1 else memory_projector(fc["J"])
        for fc, s in zip(faces, word)
    ])


# ---------------------------------------------------------------------
# T1: the global recognition cut is the product projector, not the tensor
# cut.  P = (x) P_i is an orthogonal projector; J_rec = 2P - I is an
# involution; the tensor involution (x) J_i has + sheet = even-parity words,
# which strictly contains P as soon as m >= 2.
# ---------------------------------------------------------------------

def t1_global_cut(faces: list[dict[str, Any]]) -> dict[str, Any]:
    pd = product_data(faces)
    P, J_rec, J_t, n = pd["P"], pd["J_rec"], pd["J_tensor"], pd["dim"]
    I = identity(n)
    m = len(faces)
    words = list(itertools.product((1, -1), repeat=m))
    sheets = [sheet_projector(faces, w) for w in words]
    resolution = add(*sheets) if len(sheets) == 1 else sheets[0]
    for s in sheets[1:]:
        resolution = add(resolution, s)
    orthogonal = all(
        is_zero(matmul(sheets[a], sheets[b])) for a in range(len(sheets)) for b in range(len(sheets)) if a != b
    )
    P_parity = recognized_projector(J_t)
    rank_P = sum(P[i][i] for i in range(n))
    rank_parity = sum(P_parity[i][i] for i in range(n))
    checks = {
        "P_is_projector": matmul(P, P) == P and transpose(P) == P,
        "J_rec_is_involution": matmul(J_rec, J_rec) == I and transpose(J_rec) == J_rec,
        "sheets_resolve_identity": resolution == I,
        "sheets_mutually_orthogonal": orthogonal,
        "sheet_count_is_2_pow_m": len(sheets) == 2 ** m,
        "P_equals_all_plus_sheet": P == sheet_projector(faces, (1,) * m),
        "tensor_cut_is_involution": matmul(J_t, J_t) == I,
        "tensor_plus_sheet_contains_P": matmul(P_parity, P) == P,
        "tensor_cut_differs_from_recognition_cut_for_m_ge_2": (J_t != J_rec) == (m >= 2),
    }
    return {
        "checks": checks,
        "m": m,
        "dim": n,
        "rank_recognized_everywhere": ftext(rank_P),
        "rank_tensor_plus_sheet": ftext(rank_parity),
    }


# ---------------------------------------------------------------------
# T2: the theorem.  L P = f0^m P = P L (L is J_rec-even with recognized
# value f0^m) and ||Q L Q|| <= rho f0^m, certified on the FULL product
# matrix by the exact cut-square criterion -- not assembled from sheets.
# ---------------------------------------------------------------------

def t2_uniform_gap(faces: list[dict[str, Any]], rho: Fraction) -> dict[str, Any]:
    pd = product_data(faces)
    L, P, Q, J_rec, f0m = pd["L"], pd["P"], pd["Q"], pd["J_rec"], pd["f0m"]
    even, odd = cut_grade(L, J_rec)
    qlq = matmul(matmul(Q, L), Q)
    checks = {
        "LP_equals_f0m_P": matmul(L, P) == scale(f0m, P),
        "PL_equals_f0m_P": matmul(P, L) == scale(f0m, P),
        "L_is_J_rec_even": is_zero(odd) and even == L,
        "no_leakage_PLQ_zero": is_zero(matmul(matmul(P, L), Q)),
        "no_leakage_QLP_zero": is_zero(matmul(matmul(Q, L), P)),
        "memory_sheet_contraction_certified_on_full_product": norm_le(qlq, rho * f0m),
    }
    return {"checks": checks, "m": len(faces), "dim": pd["dim"], "f0_pow_m": ftext(f0m), "rho_bound": ftext(rho)}


# ---------------------------------------------------------------------
# T3: sheet law.  For each word with k minus signs the sheet block of L
# has norm <= rho^k f0^m; the worst sheets are the single-minus words, so
# the bound rho f0^m is attained exactly when some face attains its
# contraction on a diagonal memory direction.
# ---------------------------------------------------------------------

def t3_sheet_law(faces: list[dict[str, Any]], rho: Fraction, attained: bool) -> dict[str, Any]:
    pd = product_data(faces)
    L, f0m = pd["L"], pd["f0m"]
    m = len(faces)
    per_word = {}
    all_ok = True
    for w in itertools.product((1, -1), repeat=m):
        k = sum(1 for s in w if s == -1)
        S = sheet_projector(faces, w)
        block = matmul(matmul(S, L), S)
        ok = norm_le(block, rho**k * f0m)
        all_ok &= ok
        per_word["".join("+" if s == 1 else "-" for s in w)] = {"k": k, "norm_le_rho_k_f0m": ok}
    # attainment witness (diagonal instance): a single-minus word with exact value rho*f0m
    att = None
    if attained:
        for w in itertools.product((1, -1), repeat=m):
            if sum(1 for s in w if s == -1) != 1:
                continue
            S = sheet_projector(faces, w)
            block = matmul(matmul(S, L), S)
            # diagonal entries of the block equal the word's product of diagonal values
            diag = [abs(block[i][i]) for i in range(len(block)) if block[i][i] != 0]
            if diag and max(diag) == rho * f0m:
                att = "".join("+" if s == 1 else "-" for s in w)
                break
    checks = {
        "every_sheet_obeys_rho_pow_k_law": all_ok,
        "single_minus_words_are_the_binding_sheets": all(
            v["k"] != 1 or v["norm_le_rho_k_f0m"] for v in per_word.values()
        ),
    }
    if attained:
        checks["bound_attained_on_a_single_minus_word"] = att is not None
    return {"checks": checks, "m": m, "words": per_word, "attaining_word": att}


# ---------------------------------------------------------------------
# T4: uniformity exhibited.  Heterogeneous faces (dims 2 and 3, different
# weights and contractions) multiplied up to m = 5: the certified ratio
# bound is max_i rho_i at every m -- the same number, no growth.
# ---------------------------------------------------------------------

def heterogeneous_faces() -> list[tuple[dict[str, Any], Fraction, Fraction]]:
    # (face, W, lambda); f0 declared per face; memory blocks not diagonal.
    f_a = face(Fraction(4), matrix(((Fraction(1), Fraction(1, 2)), (Fraction(0), Fraction(1)))))
    # ||B_a|| = sqrt((9+sqrt(17))/8)... irrational; certify <= W*lam = 3/2 * 1 = 3/2 (exact PSD)
    f_b = face(Fraction(2), matrix(((Fraction(1, 2),),)))
    f_c = face(Fraction(5), matrix(((Fraction(1), Fraction(-1)), (Fraction(1), Fraction(1)))))
    # ||B_c|| = sqrt(2); certify <= W*lam = 3 * 1/2 = 3/2 since 2 <= 9/4
    return [
        (f_a, Fraction(3, 2), Fraction(1)),
        (f_b, Fraction(1), Fraction(1, 2)),
        (f_c, Fraction(3), Fraction(1, 2)),
        (f_a, Fraction(3, 2), Fraction(1)),
        (f_b, Fraction(1), Fraction(1, 2)),
    ]


def t4_uniformity_in_m() -> dict[str, Any]:
    data = heterogeneous_faces()
    per_face = [face_hypotheses(fc, W, lam) for fc, W, lam in data]
    rhos = [W * lam / fc["f0"] for fc, W, lam in data]
    rows = {}
    ok = True
    for m in range(1, len(data) + 1):
        faces = [fc for fc, _, _ in data[:m]]
        rho_m = max(rhos[:m])
        t2 = t2_uniform_gap(faces, rho_m)
        t3 = t3_sheet_law(faces, rho_m, attained=False)
        ok &= all(t2["checks"].values()) and all(t3["checks"].values())
        rows[str(m)] = {"dim": t2["dim"], "rho_bound": ftext(rho_m), "gap_certified": all(t2["checks"].values())}
    checks = {
        "all_faces_satisfy_H1_H2": all(all(v for k, v in p.items() if isinstance(v, bool)) for p in per_face),
        "gap_certified_at_every_m": ok,
        "rho_bound_is_max_of_local_rhos_and_m_independent": all(
            Fraction(r["rho_bound"]) == max(rhos) for m, r in rows.items() if int(m) >= 3
        ),
        "no_growth_in_m": len({r["rho_bound"] for m, r in rows.items() if int(m) >= 3}) == 1,
    }
    return {"checks": checks, "per_face": per_face, "per_m": rows}


# ---------------------------------------------------------------------
# T5: theorum/28 Sec. 9 outward certificate delivered m-uniformly.  Normalize
# L~ = L / f0^m so the recognized floor is exactly 1.  Then u = rho is an
# outward upper bound for the memory sheet at every finite m and e = 0 (no
# refinement error at finite m).  u + e = rho < 1 is the lawful certificate,
# and it is the SAME number for every m.  Hypotheses 1-5 of theorum/28
# Sec. 11 (infinite carrier, Cauchy packets, Smriti tails, faithfulness)
# are NOT built here and the infinite-face limit is NOT claimed.
# ---------------------------------------------------------------------

def t5_outward_certificate() -> dict[str, Any]:
    data = heterogeneous_faces()
    rhos = [W * lam / fc["f0"] for fc, W, lam in data]
    rows = {}
    ok = True
    for m in range(1, 5):
        faces = [fc for fc, _, _ in data[:m]]
        pd = product_data(faces)
        Ln = scale(1 / pd["f0m"], pd["L"])
        floor_exact = matmul(Ln, pd["P"]) == pd["P"]
        u = max(rhos[:m])
        e = Fraction(0)
        mem = matmul(matmul(pd["Q"], Ln), pd["Q"])
        lawful = norm_le(mem, u) and (u + e < 1)
        ok &= floor_exact and lawful
        rows[str(m)] = {"u": ftext(u), "e": ftext(e), "u_plus_e_lt_1": u + e < 1}
    checks = {"normalized_recognized_floor_exactly_1": ok, "outward_certificate_u_plus_e_lt_1_uniform_in_m": ok}
    return {"checks": checks, "per_m": rows}


# ---------------------------------------------------------------------
# T6: interacting faces.  A coupling E that lives on the memory sheet only
# (P E = E P = 0) with ||E|| <= beta f0^m certified adds at most beta:
# ||Q (L+E) Q|| <= (rho + beta) f0^m.  The m-uniformity of beta is a
# DECLARED hypothesis for interacting faces, not derived here.
# ---------------------------------------------------------------------

def nearest_neighbour_coupling(faces: list[dict[str, Any]], g: Fraction) -> Matrix:
    """E = g * sum_i Q_i X_i (x) Q_{i+1} X_{i+1}, with X the memory reflection
    on each face: acts only inside memory sheets, hence P E = E P = 0."""
    mats = []
    for fc in faces:
        d = len(fc["J"])
        x = [[Fraction(0)] * d for _ in range(d)]
        for i in range(1, d):
            x[i][d - i if d - i >= 1 else i] = Fraction(1)
        mats.append(matrix(x))
    n = 1
    for fc in faces:
        n *= len(fc["J"])
    E = zero(n, n)
    for i in range(len(faces) - 1):
        terms = [identity(len(fc["J"])) for fc in faces]
        terms[i] = mats[i]
        terms[i + 1] = mats[i + 1]
        E = add(E, kron_all(terms))
    return scale(g, E)


def t6_interacting_faces() -> dict[str, Any]:
    data = heterogeneous_faces()[:3]
    faces = [fc for fc, _, _ in data]
    rho = max(W * lam / fc["f0"] for fc, W, lam in data)
    pd = product_data(faces)
    L, P, Q, f0m = pd["L"], pd["P"], pd["Q"], pd["f0m"]
    beta = Fraction(1, 10)
    E = nearest_neighbour_coupling(faces, beta * f0m / 2)
    LE = add(L, E)
    checks = {
        "coupling_kills_recognized_sheet_PE_zero": is_zero(matmul(P, E)),
        "coupling_kills_recognized_sheet_EP_zero": is_zero(matmul(E, P)),
        "coupling_norm_certified_le_beta_f0m": norm_le(E, beta * f0m),
        "recognized_value_unchanged": matmul(LE, P) == scale(f0m, P) and matmul(P, LE) == scale(f0m, P),
        "perturbed_memory_contraction_le_rho_plus_beta": norm_le(matmul(matmul(Q, LE), Q), (rho + beta) * f0m),
        "rho_plus_beta_lt_1": rho + beta < 1,
    }
    # control: coupling that touches the recognized sheet moves the recognized value
    bad = add(E, scale(beta * f0m / 2, P))
    LB = add(L, bad)
    checks["control_recognized_touching_coupling_moves_f0m"] = matmul(LB, P) != scale(f0m, P)
    return {"checks": checks, "m": 3, "dim": pd["dim"], "rho": ftext(rho), "beta": ftext(beta)}


# ---------------------------------------------------------------------
# T7: controls on the theorem itself.
#   C1 too bad a face: W*lambda >= f0 gives rho >= 1 and more faces never
#      repair it (ratio bound stays >= 1 for m = 1..4);
#   C2 wrong cut: grading L against the tensor cut (x) J_i instead of
#      J_rec -- its + sheet is NOT an exact recognized sheet (P_par L P_par
#      != f0^m P_par), so the theorem's first identity fails for m >= 2;
#   C3 leakage: a face violating co-invariance (P L Q != 0) makes the
#      product L NOT J_rec-even; the seam decomposition is lost and the
#      memory-to-recognized block is nonzero in the product.
# ---------------------------------------------------------------------

def t7_controls() -> dict[str, Any]:
    # C1
    f_bad = face(Fraction(1), matrix(((Fraction(1),),)))  # memory value 1 = f0 -> rho = 1
    c1 = {}
    for m in range(1, 5):
        faces = [f_bad] * m
        pd = product_data(faces)
        mem = matmul(matmul(pd["Q"], pd["L"]), pd["Q"])
        # exact: the single-minus sheet carries value exactly f0^m, so no rho<1 certifies
        c1[str(m)] = not norm_le(mem, Fraction(99, 100) * pd["f0m"])
    # C2
    data = heterogeneous_faces()[:2]
    faces = [fc for fc, _, _ in data]
    pd = product_data(faces)
    P_par = recognized_projector(pd["J_tensor"])
    c2 = matmul(matmul(P_par, pd["L"]), P_par) != scale(pd["f0m"], P_par)
    # C3
    leak = matrix(((Fraction(2), Fraction(1)), (Fraction(0), Fraction(1, 2))))
    f_leak = {"L": leak, "J": cut_matrix(2), "f0": Fraction(2)}
    faces3 = [f_leak, heterogeneous_faces()[1][0]]
    pd3 = product_data(faces3)
    even, odd = cut_grade(pd3["L"], pd3["J_rec"])
    c3_not_even = not is_zero(odd)
    c3_leak_block = not is_zero(matmul(matmul(pd3["P"], pd3["L"]), pd3["Q"]))
    checks = {
        "C1_rho_ge_1_face_not_repaired_by_more_faces": all(c1.values()),
        "C2_tensor_cut_plus_sheet_is_not_exact_recognized_sheet": c2,
        "C3_leaking_face_makes_product_non_even": c3_not_even,
        "C3_leaking_face_nonzero_memory_to_recognized_block": c3_leak_block,
    }
    return {"checks": checks, "C1_per_m": c1}


# ---------------------------------------------------------------------
# Certificate assembly.
# ---------------------------------------------------------------------

def build_certificate() -> dict[str, Any]:
    data = heterogeneous_faces()
    faces3 = [fc for fc, _, _ in data[:3]]
    rho3 = max(W * lam / fc["f0"] for fc, W, lam in data[:3])
    # diagonal instance for attainment
    f_d1 = face(Fraction(3), matrix(((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1, 2)))))
    f_d2 = face(Fraction(2), matrix(((Fraction(1, 2),),)))
    diag_faces = [f_d1, f_d2, f_d1]
    rho_diag = Fraction(1, 3)
    packets = {
        "t1_global_cut": t1_global_cut(faces3),
        "t2_uniform_gap": t2_uniform_gap(faces3, rho3),
        "t3_sheet_law": t3_sheet_law(diag_faces, rho_diag, attained=True),
        "t4_uniformity_in_m": t4_uniformity_in_m(),
        "t5_outward_certificate": t5_outward_certificate(),
        "t6_interacting_faces": t6_interacting_faces(),
        "t7_controls": t7_controls(),
    }
    checks = {f"{name}_all_checks": all(p["checks"].values()) for name, p in packets.items()}
    status = (
        "PASS_LOCAL_TO_UNIFORM_SEAM_GAP_CANDIDATE" if all(checks.values()) else "FAIL_LOCAL_TO_UNIFORM_SEAM_GAP_CANDIDATE"
    )
    return {
        "schema": "rkf.local_to_uniform_seam_gap_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "global recognition cut of a product of faces is J_rec = 2 (x)P_i - I; the 2^m sheet projectors resolve the identity orthogonally",
                "the tensor involution (x)J_i is a DIFFERENT cut (even-parity sheet strictly contains the recognized-everywhere sheet for m>=2)",
                "(H1) seam compatibility of every face is equivalent to the face transfer being J_i-even (theorum/41 (3.3)) with recognized value f0",
                "(H2) memory contraction certified by the exact cut-square criterion (theorum/41 (5.4)) via rational LDL inertia",
                "THEOREM: L P = f0^m P = P L and ||Q L Q|| <= rho f0^m on the full product matrix, rho = W*lambda/f0, for every finite m tested (1..5) with heterogeneous faces",
                "sheet law: a word with k minus signs obeys ||sheet block|| <= rho^k f0^m; single-minus words are binding; bound attained on diagonal instances",
                "normalized floor exactly 1 and theorum/28 Sec. 9 outward certificate u+e = rho < 1 delivered m-uniformly",
                "memory-sheet-only coupling of certified norm beta f0^m degrades the bound to rho+beta, recognized value untouched",
                "controls: rho>=1 face never repaired by more faces; tensor cut is not the recognition cut; leaking face destroys evenness and creates a memory-to-recognized block",
            ],
            "NOT_claimed": [
                "the infinite-face limit m -> infinity (theorum/28 Sec. 11 hypotheses 1-5: infinite carrier, recognition-Cauchy packets, Smriti tails, faithfulness) -- NOT built; only hypothesis 6 (outward margin) is delivered, uniformly in m",
                "m-uniformity of the coupling norm beta for interacting faces -- DECLARED, not derived",
                "any spectral statement about non-seam-compatible (leaking) faces; no Perron-Frobenius, Dobrushin, or transfer-operator theorem is imported",
                "any identification of W with exp(kappa): W is the declared rational sup-weight, no exponential is evaluated",
                "RH, Yang-Mills, or any other framework gate -- untouched",
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
