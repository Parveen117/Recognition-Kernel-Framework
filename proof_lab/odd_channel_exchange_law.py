from __future__ import annotations

"""Exact certificate (theorum/51): TRANSPORT OF THE ODD CHANNEL UNDER THE FLOW
-- the EVEN/ODD EXCHANGE LAW ("Aghora transport").

Carrier and verdicts exactly as in theorum/50 (C_Sigma scalars (rad, turn),
path convolution, native dagger, M_Sigma / E_Sigma).  Imported from there by
pinned module; nothing Hilbert.

Flow.  The generalized Euler flow step is the Cayley step (RST-1 T4)
C_h(D) = (I - h/2 D)^{-1}(I + h/2 D), here for ANTI-SELF-DAGGER generators
D^dagger = -D, i.e. D = B + iota A with B^T = -B (even/real part antisymmetric)
and A^T = A (turn part symmetric).  The inverse is exact rational Gaussian
elimination over C_Sigma at a declared rational h; no nilpotency needed.

Results certified:
 T1  C_h is native-unitary: C^dagger * C = I; recognition energy of L is
     invariant under L -> L*C_h; mass is NOT (mass is a gauge, energy the invariant).
 T2  EXCHANGE LAW.  For S = L^dagger*L = R + iota T (R sym, T antisym):
        D^dagger S + S D = ([R,B] + [A,T]) + iota ([T,B] + [R,A])     (exact)
     and C_h - I - hD = (h^2/2)(I - h/2 D)^{-1} D^2                  (exact),
     so the first-order transport of the cut square is: the even generator B
     moves each channel inside itself by a commutator flow, the odd (turn)
     generator A EXCHANGES the channels:  R <- [A,T],  T <- [R,A].
 T3  Channel separation: with A = 0 a turn-free square stays turn-free
     (no creation); with B = 0 and A != 0 a turn-free square acquires a
     nonzero odd channel: the odd channel is CREATED from the even one by the
     odd generator, and the reverse transfer also occurs.
 T4  Invariant: E_Sigma(S_h) = E_Sigma(S) exactly (rad^2 + turn^2 summed),
     the even and odd energies individually change; tr rad(S) = E_Sigma(L)
     conserved; the diagonal of the odd channel stays zero (A1 of theorum/50
     is flow-stable).
 T5  Product: the sum generator D_a(x)I + I(x)D_b is anti-self-dagger; its
     first-order transport of turn(S_ab) is the Leibniz rule of the face
     transports; the Cayley step itself does NOT factor over the product
     (C_h(D_a(x)I + I(x)D_b) != C_h(D_a)(x)C_h(D_b)) -- the generator is local,
     the step is not.
 T6  Controls: theorum/50's nilpotent (non-anti-self-dagger) flow does not
     preserve energy; a symmetric B breaks unitarity; wrong-sign exchange law
     rejected.
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
    cayley_step,
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
    real_neg,
    real_sub,
    real_T,
    s_dag,
    s_mul,
    s_N,
    sc,
    star,
    turn_part,
)


# ---------------------------------------------------------------- exact inverse over C_Sigma
def s_inv(z: Sc) -> Sc:
    n = s_N(z)
    assert n != 0, "division by the zero cut scalar"
    d = s_dag(z)
    return (d[0] / n, d[1] / n)


def inverse(a: Mat) -> Mat:
    """Gauss-Jordan over C_Sigma, exact.  Raises if singular."""
    n = len(a)
    M = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != (F0, F0)), None)
        assert piv is not None, "singular"
        M[c], M[piv] = M[piv], M[c]
        inv = s_inv(M[c][c])
        M[c] = [s_mul(inv, x) for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != (F0, F0):
                f = M[r][c]
                M[r] = [(x[0] - (f[0] * y[0] - f[1] * y[1]), x[1] - (f[0] * y[1] + f[1] * y[0])) for x, y in zip(M[r], M[c])]
    return tuple(tuple(row[n:]) for row in M)


def cayley_unitary(D: Mat, h: Fraction) -> Mat:
    n = len(D)
    half = sc(h / 2)
    return star(inverse(m_sub(eye(n), m_scale(half, D))), m_add(eye(n), m_scale(half, D)))


def comm(X, Y):
    n = len(X)
    return tuple(tuple(sum((X[i][k] * Y[k][j] - Y[i][k] * X[k][j] for k in range(n)), F0) for j in range(n)) for i in range(n))


def real_mat(B, A) -> Mat:
    return tuple(tuple((B[i][j], A[i][j]) for j in range(len(B))) for i in range(len(B)))


def anti_self_dagger_generator(n: int, rng: random.Random, even: bool = True, odd: bool = True) -> tuple[Mat, Any, Any]:
    B = [[F0] * n for _ in range(n)]
    A = [[F0] * n for _ in range(n)]
    for i in range(n):
        if odd:
            A[i][i] = Fraction(rng.randint(-2, 2))
        for j in range(i + 1, n):
            if even:
                b = Fraction(rng.randint(-2, 2))
                B[i][j], B[j][i] = b, -b
            if odd:
                a = Fraction(rng.randint(-2, 2))
                A[i][j], A[j][i] = a, a
    Bt, At = tuple(map(tuple, B)), tuple(map(tuple, A))
    return real_mat(Bt, At), Bt, At


def random_operator(n: int, rng: random.Random) -> Mat:
    return tuple(tuple(sc(Fraction(rng.randint(-2, 2)), Fraction(rng.randint(-2, 2))) for _ in range(n)) for _ in range(n))


def transport(S: Mat, C: Mat) -> Mat:
    return star(star(dagger(C), S), C)


def even_energy(S: Mat) -> Fraction:
    return sum((x * x for row in rad_part(S) for x in row), F0)


def odd_energy(S: Mat) -> Fraction:
    return sum((x * x for row in turn_part(S) for x in row), F0)


def trace_rad(S: Mat) -> Fraction:
    return sum((S[i][i][0] for i in range(len(S))), F0)


# ---------------------------------------------------------------- T1
def t1_native_unitary() -> dict[str, Any]:
    rng = random.Random(51)
    unit = en_inv = mass_changes = 0
    for _ in range(12):
        n = rng.randint(2, 4)
        D, _, _ = anti_self_dagger_generator(n, rng)
        h = Fraction(rng.randint(1, 3), rng.randint(1, 4))
        C = cayley_unitary(D, h)
        unit += star(dagger(C), C) == eye(n)
        L = random_operator(n, rng)
        en_inv += energy(star(L, C)) == energy(L)
        mass_changes += mass(star(L, C)) != mass(L)
    checks = {
        "anti_self_dagger_generator_property": all(dagger(anti_self_dagger_generator(3, random.Random(k))[0]) == m_scale(-1, anti_self_dagger_generator(3, random.Random(k))[0]) for k in range(5)),
        "cayley_step_native_unitary_12_of_12": unit == 12,
        "recognition_energy_invariant_12_of_12": en_inv == 12,
        "mass_is_a_gauge_not_an_invariant": mass_changes > 0,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T2
def t2_exchange_law() -> dict[str, Any]:
    rng = random.Random(52)
    law = resid = 0
    for _ in range(20):
        n = rng.randint(2, 4)
        D, B, A = anti_self_dagger_generator(n, rng)
        L = random_operator(n, rng)
        S = cut_square(L)
        R, T = rad_part(S), turn_part(S)
        dS = m_add(star(dagger(D), S), star(S, D))
        law += rad_part(dS) == real_add(comm(R, B), comm(A, T)) and turn_part(dS) == real_add(comm(T, B), comm(R, A))
        h = Fraction(rng.randint(1, 3), rng.randint(1, 4))
        C = cayley_unitary(D, h)
        lhs = m_sub(m_sub(C, eye(n)), m_scale(h, D))
        rhs = m_scale(h * h / 2, star(inverse(m_sub(eye(n), m_scale(sc(h / 2), D))), star(D, D)))
        resid += lhs == rhs
    # wrong sign rejected
    n = 3
    D, B, A = anti_self_dagger_generator(n, random.Random(9))
    S = cut_square(random_operator(n, random.Random(10)))
    R, T = rad_part(S), turn_part(S)
    dS = m_add(star(dagger(D), S), star(S, D))
    wrong = turn_part(dS) == real_add(comm(T, B), comm(A, R))
    checks = {
        "exchange_law_exact_20_of_20": law == 20,
        "cayley_first_order_residual_identity_20_of_20": resid == 20,
        "wrong_sign_exchange_rejected": not wrong,
    }
    return {"checks": checks, "law": "rad <- [R,B]+[A,T] ; turn <- [T,B]+[R,A]"}


# ---------------------------------------------------------------- T3
def t3_channel_separation() -> dict[str, Any]:
    rng = random.Random(53)
    n = 3
    # turn-free square
    Lr = tuple(tuple(sc(Fraction(rng.randint(-2, 2))) for _ in range(n)) for _ in range(n))
    S0 = cut_square(Lr)
    turn_free = all(x == 0 for row in turn_part(S0) for x in row)
    De, _, _ = anti_self_dagger_generator(n, rng, even=True, odd=False)
    Do, _, _ = anti_self_dagger_generator(n, rng, even=False, odd=True)
    h = Fraction(1, 2)
    Se = transport(S0, cayley_unitary(De, h))
    So = transport(S0, cayley_unitary(Do, h))
    no_creation = all(x == 0 for row in turn_part(Se) for x in row)
    creation = any(x != 0 for row in turn_part(So) for x in row)
    # reverse: a square with odd channel, transported by the odd generator, changes its even channel
    S1 = cut_square(random_operator(n, rng))
    S1o = transport(S1, cayley_unitary(Do, h))
    reverse = rad_part(S1o) != rad_part(S1) and odd_energy(S1o) != odd_energy(S1)
    checks = {
        "start_turn_free": turn_free,
        "even_generator_creates_no_odd_channel": no_creation,
        "odd_generator_creates_odd_channel_from_even": creation,
        "odd_generator_moves_even_channel_and_odd_energy": reverse,
        "even_flow_keeps_odd_channel_zero_is_exact_not_approximate": is_zero(tuple(tuple((F0, x) for x in row) for row in turn_part(Se))),
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T4
def t4_invariant() -> dict[str, Any]:
    rng = random.Random(54)
    tot = diag = tr = exch = 0
    for _ in range(12):
        n = rng.randint(2, 4)
        D, _, _ = anti_self_dagger_generator(n, rng)
        L = random_operator(n, rng)
        S = cut_square(L)
        Sh = transport(S, cayley_unitary(D, Fraction(rng.randint(1, 3), rng.randint(1, 4))))
        tot += energy(Sh) == energy(S)
        diag += all(Sh[i][i][1] == 0 for i in range(n))
        tr += trace_rad(Sh) == trace_rad(S) == energy(L)
        exch += odd_energy(Sh) != odd_energy(S)
    checks = {
        "total_energy_of_cut_square_invariant_12_of_12": tot == 12,
        "odd_energy_changes_somewhere_exchange_is_real": exch > 0,
        "odd_diagonal_stays_zero_12_of_12": diag == 12,
        "trace_of_even_channel_equals_E_L_conserved_12_of_12": tr == 12,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T5
def t5_product() -> dict[str, Any]:
    rng = random.Random(55)
    Da, Ba, Aa = anti_self_dagger_generator(2, rng)
    Db, Bb, Ab = anti_self_dagger_generator(2, rng)
    La, Lb = random_operator(2, rng), random_operator(2, rng)
    Sa, Sb = cut_square(La), cut_square(Lb)
    Dsum = m_add(kron(Da, eye(2)), kron(eye(2), Db))
    asd = dagger(Dsum) == m_scale(-1, Dsum)
    Sab = cut_square(kron(La, Lb))
    dSab = m_add(star(dagger(Dsum), Sab), star(Sab, Dsum))
    dSa = m_add(star(dagger(Da), Sa), star(Sa, Da))
    dSb = m_add(star(dagger(Db), Sb), star(Sb, Db))
    ra, ta, rb, tb = rad_part(Sa), turn_part(Sa), rad_part(Sb), turn_part(Sb)
    dra, dta, drb, dtb = rad_part(dSa), turn_part(dSa), rad_part(dSb), turn_part(dSb)
    leib = real_add(real_add(real_kron(dra, tb), real_kron(ra, dtb)), real_add(real_kron(dta, rb), real_kron(ta, drb)))
    leibniz = turn_part(dSab) == leib
    h = Fraction(1, 3)
    factor = cayley_unitary(Dsum, h) == kron(cayley_unitary(Da, h), cayley_unitary(Db, h))
    unitary = star(dagger(cayley_unitary(Dsum, h)), cayley_unitary(Dsum, h)) == eye(4)
    checks = {
        "sum_generator_anti_self_dagger": asd,
        "first_order_odd_transport_is_Leibniz_of_face_transports": leibniz,
        "product_cayley_step_is_unitary": unitary,
        "cayley_step_does_not_factor_over_product": not factor,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T6
def t6_controls() -> dict[str, Any]:
    rng = random.Random(56)
    fa = instance_faces()[0]
    Dn, h = fa["generator"], fa["h"]
    Cn = cayley_step(Dn, h)
    L = random_operator(len(Dn), rng)
    nil_not_unitary = star(dagger(Cn), Cn) != eye(len(Dn))
    nil_energy_changes = energy(star(L, Cn)) != energy(L)
    # symmetric B breaks unitarity
    n = 3
    B = tuple(tuple(Fraction(1 if i != j else 0) for j in range(n)) for i in range(n))
    A = tuple(tuple(F0 for _ in range(n)) for _ in range(n))
    Dsym = real_mat(B, A)
    sym_not_unitary = star(dagger(cayley_unitary(Dsym, Fraction(1, 2))), cayley_unitary(Dsym, Fraction(1, 2))) != eye(n)
    checks = {
        "C1_nilpotent_flow_of_theorem50_is_not_unitary": nil_not_unitary,
        "C1_nilpotent_flow_does_not_preserve_energy": nil_energy_changes,
        "C2_symmetric_even_generator_breaks_unitarity": sym_not_unitary,
    }
    return {"checks": checks}


# ---------------------------------------------------------------- certificate
def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_native_unitary": t1_native_unitary(),
        "t2_exchange_law": t2_exchange_law(),
        "t3_channel_separation": t3_channel_separation(),
        "t4_invariant": t4_invariant(),
        "t5_product": t5_product(),
        "t6_controls": t6_controls(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_ODD_CHANNEL_EXCHANGE_LAW_CANDIDATE" if all(checks.values()) else "FAIL_ODD_CHANNEL_EXCHANGE_LAW_CANDIDATE"
    return {
        "schema": "rkf.odd_channel_exchange_law_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Cayley step of an anti-self-dagger generator is native-unitary (C^dagger*C = I) with exact rational inverse over C_Sigma; recognition energy invariant, mass not",
                "EXCHANGE LAW: D^dagger S + S D = ([R,B]+[A,T]) + iota([T,B]+[R,A]) exactly, and C_h - I - hD = (h^2/2)(I-h/2 D)^{-1}D^2 exactly, so the first-order transport of the cut square is: even generator -> commutator flow inside each channel; odd (turn) generator -> exchange between channels",
                "channel separation: even generator never creates an odd channel; odd generator creates it from a turn-free square and moves the even channel back",
                "invariant: total energy of the cut square conserved, even/odd energies exchanged; trace of the even channel = E_Sigma(L) conserved; odd diagonal stays zero (theorum/50 A1 flow-stable)",
                "product: sum generator anti-self-dagger; first-order odd transport is the Leibniz rule of face transports; the Cayley step does not factor over the product",
                "controls: theorum/50's nilpotent flow is non-unitary and non-energy-preserving; symmetric even generator breaks unitarity; wrong-sign law rejected",
            ],
            "NOT_claimed": [
                "any statement at second order or for the exact (non-infinitesimal) transport beyond the identities certified",
                "an identification of the exchange law with EMK's RK mixed channel or with the Generalized Euler RK connection (same shape; identification is a separate dock)",
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
