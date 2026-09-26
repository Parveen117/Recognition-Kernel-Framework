from __future__ import annotations

"""Exact certificate: the EMK primitive algebra {I,K,R,RK} is a concrete,
finite-dimensional instantiation of the abstract cut-graded Jacobian-tower
machinery of theorum/42 (cut involution J_E, even/odd grading, cut-loop
curvature F_st = [G_e, G_o]), and the resulting curvature has an EXACT
closed form on this carrier rather than a truncated series.

Only ``fractions.Fraction`` is used. No floating point, no NumPy, no
transcendental evaluation.

This capsule does NOT claim the physical adapter of theorum/42 Eq. (6.7)
(operator curvature -> thermodynamic response two-form Omega_H). It closes
a narrower, purely algebraic gap: theorum/42 lists "physical T-V-S-P cut
and response-fibre involution" and "operator curvature -> response
two-form adapter" as OPEN/NEXT; this certificate exhibits ONE concrete,
independently-derived algebra (matching the grading already certified in
Publications repo EMK-1/EMK-2, reproduced here from scratch rather than
imported, per cross-repo independence discipline) that satisfies theorum/42's
abstract axioms and computes its curvature exactly.
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

Scalar = Fraction
Matrix = tuple[tuple[Scalar, ...], ...]


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix(rows) -> Matrix:
    return tuple(tuple(q(x) for x in row) for row in rows)


def identity(n: int) -> Matrix:
    return tuple(tuple(Fraction(1) if i == j else Fraction(0) for j in range(n)) for i in range(n))


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
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0)) for j in range(len(b[0])))
        for i in range(len(a))
    )


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def is_zero(a: Matrix) -> bool:
    return all(x == 0 for row in a for x in row)


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


# ---------------------------------------------------------------------
# Part 1: the EMK primitive algebra, derived independently on the 2x2
# matrix carrier (self-contained; reproduces, does not import, the
# Publications-repo EMK-1 relations).
# ---------------------------------------------------------------------

I2 = identity(2)
K = matrix(((0, 1), (1, 0)))
R = matrix(((0, -1), (1, 0)))
RK = matmul(R, K)

BASIS = {"I": I2, "K": K, "R": R, "RK": RK}


def primitive_relations() -> dict[str, Any]:
    checks = {
        "K_squared_is_I": matmul(K, K) == I2,
        "R_squared_is_minus_I": matmul(R, R) == scale(-1, I2),
        "RK_squared_is_I": matmul(RK, RK) == I2,
        "RK_equals_minus_KR": RK == scale(-1, matmul(K, R)),
        "basis_matches_named_block": matmul(R, K) == RK,
    }
    return {"checks": checks, "matrices": {name: record_matrix(m) for name, m in BASIS.items()}}


# ---------------------------------------------------------------------
# Part 2: theorum/42's involution axiom, instantiated with J_E := K.
# theorum/42 Sec. 2 requires J_E^2 = I. Sec. 4 defines the even/odd
# grading of any object G via G^+- = (1/2)(G +- J_E G J_E).
# ---------------------------------------------------------------------

def cut_grade(g: Matrix, j: Matrix) -> tuple[Matrix, Matrix]:
    jgj = matmul(matmul(j, g), j)
    g_even = scale(Fraction(1, 2), add(g, jgj))
    g_odd = scale(Fraction(1, 2), sub(g, jgj))
    return g_even, g_odd


def involution_and_grading() -> dict[str, Any]:
    j_ok = matmul(K, K) == I2
    grading = {}
    for name, m in BASIS.items():
        even, odd = cut_grade(m, K)
        grading[name] = {
            "is_pure_even": is_zero(odd),
            "is_pure_odd": is_zero(even),
        }
    checks = {
        "J_E_is_involution": j_ok,
        "I_is_even": grading["I"]["is_pure_even"],
        "K_is_even": grading["K"]["is_pure_even"],
        "R_is_odd": grading["R"]["is_pure_odd"],
        "RK_is_odd": grading["RK"]["is_pure_odd"],
        "grading_matches_EMK2_Z2_grading": (
            grading["I"]["is_pure_even"]
            and grading["K"]["is_pure_even"]
            and grading["R"]["is_pure_odd"]
            and grading["RK"]["is_pure_odd"]
        ),
    }
    return {"checks": checks}


# ---------------------------------------------------------------------
# Part 3: theorum/42 Theorem 6.1 cut-loop curvature F_st = [G_e, G_o],
# evaluated exactly (closed form, no series truncation) for the
# representative even/odd pair G_e = K, G_o = R.
# ---------------------------------------------------------------------

def representative_curvature() -> dict[str, Any]:
    F_st = commutator(K, R)
    predicted = scale(-2, RK)
    is_odd_even, is_odd_odd = cut_grade(F_st, K)
    checks = {
        "F_st_equals_minus_two_RK_exact": F_st == predicted,
        "F_st_is_purely_cut_odd": is_zero(is_odd_even),
        "F_st_nonzero": not is_zero(F_st),
    }
    return {
        "checks": checks,
        "F_st": record_matrix(F_st),
        "predicted_minus_2_RK": record_matrix(predicted),
    }


# ---------------------------------------------------------------------
# Part 4: general closed form. For ANY even element G_e = a*I + b*K and
# ANY odd element G_o = c*R + d*RK, verify
#     [G_e, G_o] = -2b (d*R + c*RK)
# exactly, over a grid of rational (a,b,c,d), and confirm the output is
# always cut-odd (a structural fact not stated in theorum/42, which left
# the commutator abstract).
# ---------------------------------------------------------------------

def general_closed_form() -> dict[str, Any]:
    values = [Fraction(n, 1) for n in range(-3, 4)] + [Fraction(1, 2), Fraction(-1, 3)]
    total = 0
    mismatches = 0
    always_odd = True
    for a, b, c, d in itertools.product(values, repeat=4):
        total += 1
        g_e = add(scale(a, I2), scale(b, K))
        g_o = add(scale(c, R), scale(d, RK))
        lhs = commutator(g_e, g_o)
        rhs = scale(-2 * b, add(scale(d, R), scale(c, RK)))
        if lhs != rhs:
            mismatches += 1
        even_part, _odd_part = cut_grade(lhs, K)
        if not is_zero(even_part):
            always_odd = False
    checks = {
        "closed_form_matches_on_all_sampled_points": mismatches == 0,
        "commutator_is_always_cut_odd": always_odd,
        "sample_count_at_least_100": total >= 100,
    }
    return {"checks": checks, "sampled_points": total, "mismatches": mismatches}


# ---------------------------------------------------------------------
# Part 5: negative controls.
#  N1: a J that is NOT the algebra's own K (e.g. diag(1,-1), a generic
#      involution unrelated to the RK relations) does not, in general,
#      grade R and RK the same way -- the specific identification
#      J_E := K is load-bearing, not an arbitrary choice of involution.
#  N2: pure-even input (G_o = 0) gives zero curvature -- the odd sector
#      is necessary for a nonzero cut-loop curvature on this carrier.
#  N3: wrong-sign tamper (claiming F_st = +2 RK) is rejected.
# ---------------------------------------------------------------------

def negative_controls() -> dict[str, Any]:
    generic_j = matrix(((1, 0), (0, -1)))
    generic_j_is_involution = matmul(generic_j, generic_j) == I2
    even_r, odd_r = cut_grade(R, generic_j)
    r_pure_odd_under_generic_j = is_zero(even_r)
    even_rk, odd_rk = cut_grade(RK, generic_j)
    rk_pure_odd_under_generic_j = is_zero(even_rk)
    # N1 tamper: a GENERIC involution unrelated to the algebra's own
    # multiplication table must NOT reproduce the same grading partition
    # {I,K} even / {R,RK} odd -- if it did, the specific identification
    # J_E := K would be arbitrary rather than load-bearing. We assert the
    # control correctly SEPARATES: the generic involution fails to grade
    # R,RK as odd, confirming K is the algebra's own, not any, involution.
    generic_j_matches_algebra_grading = r_pure_odd_under_generic_j and rk_pure_odd_under_generic_j
    n1_control_separates = not generic_j_matches_algebra_grading

    zero_odd_curvature = commutator(K, zero(2, 2)) == zero(2, 2)

    wrong_sign_claim = scale(2, RK)
    wrong_sign_rejected = commutator(K, R) != wrong_sign_claim

    checks = {
        "N1_generic_involution_is_itself_an_involution": generic_j_is_involution,
        "N1_generic_involution_does_NOT_reproduce_algebra_grading": n1_control_separates,
        "N2_pure_even_vs_zero_gives_zero_curvature": zero_odd_curvature,
        "N3_wrong_sign_curvature_correctly_rejected": wrong_sign_rejected,
    }
    return {"checks": checks}


# ---------------------------------------------------------------------
# Certificate assembly
# ---------------------------------------------------------------------

def build_certificate() -> dict[str, Any]:
    packets = {
        "primitive_relations": primitive_relations(),
        "involution_and_grading": involution_and_grading(),
        "representative_curvature": representative_curvature(),
        "general_closed_form": general_closed_form(),
        "negative_controls": negative_controls(),
    }
    checks = {f"{name}_all_checks": all(packet["checks"].values()) for name, packet in packets.items()}
    status = (
        "PASS_EMK_ALGEBRA_CUT_GRADED_CURVATURE_CANDIDATE"
        if all(checks.values())
        else "FAIL_EMK_ALGEBRA_CUT_GRADED_CURVATURE_CANDIDATE"
    )
    return {
        "schema": "rkf.emk_algebra_cut_graded_curvature_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "EMK primitive relations K^2=I, R^2=-I, RK=-KR, RK^2=I (reproduced, not imported)",
                "J_E := K satisfies theorum/42's involution axiom J_E^2 = I",
                "the induced cut-grading matches EMK-2's independently-certified Z/2 grading exactly: {I,K} even, {R,RK} odd",
                "theorum/42 Theorem 6.1 cut-loop curvature F_st = [G_e,G_o] evaluated in EXACT closed form for the representative pair (K,R): F_st = -2*RK",
                "general closed form [a*I+b*K, c*R+d*RK] = -2b(d*R + c*RK) verified exactly on a grid of >100 rational points",
                "NEW structural fact (not stated in theorum/42): on this carrier the cut-loop curvature of any even/odd pair is ALWAYS itself cut-odd",
                "negative controls: generic non-algebra involution, zero-odd-input null curvature, wrong-sign rejection",
            ],
            "NOT_claimed": [
                "theorum/42 Eq. (6.7), the operator-curvature -> thermodynamic response two-form adapter rho([G_e,G_o]) = Omega_H -- still OPEN",
                "identification of the physical T-V-S-P lambda map (arXiv:2603.20773) with THIS algebra -- still OPEN, this is a candidate instantiation only",
                "any claim about entropy production, phase transitions, or the emk_thermo_seed.tex recursive lambda tower Lambda^(n)",
                "RH, Yang-Mills, or any other framework gate -- untouched",
            ],
            "what_this_capsule_actually_closes": [
                "theorum/42's claim boundary lists PHYSICAL T-V-S-P CUT AND RESPONSE-FIBRE INVOLUTION as OPEN/NEXT",
                "this capsule supplies ONE concrete, algebraically closed, exactly-computable involution (J_E=K) and generator pair (G_e=K, G_o=R) satisfying every abstract axiom theorum/42 states, with an exact rather than truncated-series curvature",
                "whether THIS specific instantiation is the physically correct one for the T-V-S-P lambda map is a separate, still-open question",
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
    print("PRIMITIVE_RELATIONS", payload["checks"]["primitive_relations_all_checks"])
    print("INVOLUTION_AND_GRADING", payload["checks"]["involution_and_grading_all_checks"])
    print("REPRESENTATIVE_CURVATURE", payload["checks"]["representative_curvature_all_checks"])
    print("GENERAL_CLOSED_FORM", payload["checks"]["general_closed_form_all_checks"])
    print("NEGATIVE_CONTROLS", payload["checks"]["negative_controls_all_checks"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
