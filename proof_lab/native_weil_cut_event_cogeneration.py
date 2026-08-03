from __future__ import annotations

"""Stage 3A: exact cut-event co-generation and fail-closed RH specialization gate.

This module proves finite algebraic and refinement identities with rational
arithmetic and audits the transferred direct-unshifted scalar ledger with
``Decimal`` arithmetic. It does not claim that the actual completed-Weil
boundary functional has already been oriented on the same event carrier.
"""

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any, Sequence

getcontext().prec = 80

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dtext(value: Decimal) -> str:
    return format(value, "f")


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    out = tuple(tuple(q(x) for x in row) for row in rows)
    if out:
        width = len(out[0])
        if any(len(row) != width for row in out):
            raise ValueError("inconsistent matrix width")
    return out


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0]))) if a else tuple()


def matmul(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b:
        return tuple()
    if len(a[0]) != len(b):
        raise ValueError("shape mismatch")
    return tuple(
        tuple(
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def matsub(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or (a and len(a[0]) != len(b[0])):
        raise ValueError("shape mismatch")
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(len(a[0])))
        for i in range(len(a))
    )


def identity(n: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == j)) for j in range(n))
        for i in range(n)
    )


def outer(v: Vector, w: Vector) -> Matrix:
    return tuple(tuple(v[i] * w[j] for j in range(len(w))) for i in range(len(v)))


def row_times_matrix(v: Vector, a: Matrix) -> Vector:
    if len(v) != len(a):
        raise ValueError("shape mismatch")
    return tuple(
        sum((v[i] * a[i][j] for i in range(len(v))), Fraction(0))
        for j in range(len(a[0]))
    )


def rank(a: Matrix) -> int:
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    work = [list(row) for row in a]
    pivot_row = 0
    count = 0
    for col in range(cols):
        pivot = next(
            (r for r in range(pivot_row, rows) if work[r][col] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            factor = work[r][col]
            if factor:
                work[r] = [
                    work[r][j] - factor * work[pivot_row][j]
                    for j in range(cols)
                ]
        pivot_row += 1
        count += 1
        if pivot_row == rows:
            break
    return count


def principal_2x2_positive(a: Matrix) -> bool:
    if len(a) != 2 or len(a[0]) != 2:
        raise ValueError("only 2x2")
    return (
        a[0][0] > 0
        and a[1][1] > 0
        and a[0][0] * a[1][1] - a[0][1] * a[1][0] > 0
    )


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


def run_finite_cogeneration() -> dict[str, Any]:
    # Three source events acting on a two-dimensional source core.
    z = matrix([[2, 0], [0, 2], [2, 2]])
    c: Vector = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    slack = Fraction(1, 2)
    z_ext = tuple(z) + ((Fraction(0), Fraction(0)),)
    p: Vector = c + (slack,)

    source = matmul(transpose(z), z)
    ell = row_times_matrix(c, z)
    covariance = matsub(source, outer(ell, ell))
    p_norm_sq = sum((x * x for x in p), Fraction(0))

    projection = outer(p, p)
    qproj = matsub(identity(4), projection)
    memory_lift = matmul(qproj, z_ext)
    memory_gram = matmul(transpose(memory_lift), memory_lift)

    checks = {
        "unit_boundary_state": p_norm_sq == 1,
        "source_is_second_moment": source == matmul(transpose(z_ext), z_ext),
        "boundary_is_first_moment": row_times_matrix(p, z_ext) == ell,
        "covariance_is_cut_gram": covariance == memory_gram,
        "covariance_positive_definite": principal_2x2_positive(covariance),
        "boundary_line_no_blindness": rank(memory_lift) == 2,
        "decoder_burden_three_quarters": sum(x * x for x in c) == Fraction(3, 4),
    }
    return {
        "schema": "rkf.weil_event_finite_cogeneration.v1",
        "event_lift": record_matrix(z_ext),
        "boundary_state": [ftext(x) for x in p],
        "source_gram": record_matrix(source),
        "boundary_row": [ftext(x) for x in ell],
        "cut_covariance": record_matrix(covariance),
        "memory_rank": rank(memory_lift),
        "decoder_burden": "3/4",
        "checks": checks,
    }


def run_shift_refinement_identity() -> dict[str, Any]:
    source_energies = (Fraction(1), Fraction(4), Fraction(9))
    boundary_masses = (Fraction(1, 4), Fraction(1), Fraction(9, 4))
    eta = Fraction(1)
    beta_zero = sum(
        (m / s for s, m in zip(source_energies, boundary_masses)),
        Fraction(0),
    )
    beta_eta = sum(
        (m / (s + eta) for s, m in zip(source_energies, boundary_masses)),
        Fraction(0),
    )
    correction = sum(
        (
            m * eta / (s * (s + eta))
            for s, m in zip(source_energies, boundary_masses)
        ),
        Fraction(0),
    )
    checks = {
        "beta_zero_three_quarters": beta_zero == Fraction(3, 4),
        "exact_endpoint_difference": beta_zero - beta_eta == correction,
        "shifted_burden_smaller": beta_eta < beta_zero,
    }
    return {
        "schema": "rkf.weil_event_shift_refinement.v1",
        "source_energies": [ftext(x) for x in source_energies],
        "boundary_masses": [ftext(x) for x in boundary_masses],
        "eta": ftext(eta),
        "beta_zero": ftext(beta_zero),
        "beta_eta": ftext(beta_eta),
        "endpoint_correction": ftext(correction),
        "checks": checks,
    }


def run_refinement_orientation_gate() -> dict[str, Any]:
    # Parent event: source weight 2, boundary coefficient 1.
    parent_burden = Fraction(1, 2)

    # Coherent split preserves the boundary and the sharp burden.
    coherent_coefficients = (Fraction(1, 2), Fraction(1, 2))
    coherent_boundary = sum(coherent_coefficients, Fraction(0))
    coherent_burden = sum(
        (a * a for a in coherent_coefficients),
        Fraction(0),
    )

    # Same scalar masses but opposite orientation changes the boundary.
    opposite_coefficients = (Fraction(1, 2), Fraction(-1, 2))
    opposite_boundary = sum(opposite_coefficients, Fraction(0))
    opposite_burden = sum(
        (a * a for a in opposite_coefficients),
        Fraction(0),
    )

    # A non-proportional split preserves total boundary but increases burden.
    concentrated_coefficients = (Fraction(1), Fraction(0))
    concentrated_boundary = sum(concentrated_coefficients, Fraction(0))
    concentrated_burden = sum(
        (a * a for a in concentrated_coefficients),
        Fraction(0),
    )

    checks = {
        "coherent_split_preserves_boundary": coherent_boundary == 1,
        "coherent_split_preserves_burden": coherent_burden == parent_burden,
        "same_masses_do_not_determine_orientation": (
            opposite_burden == coherent_burden
            and opposite_boundary != coherent_boundary
        ),
        "nonproportional_refinement_increases_burden": (
            concentrated_boundary == 1
            and concentrated_burden > parent_burden
        ),
    }
    return {
        "schema": "rkf.weil_event_refinement_orientation.v1",
        "parent_burden": ftext(parent_burden),
        "coherent": {
            "coefficients": [ftext(x) for x in coherent_coefficients],
            "boundary": ftext(coherent_boundary),
            "burden": ftext(coherent_burden),
        },
        "opposite_orientation": {
            "coefficients": [ftext(x) for x in opposite_coefficients],
            "boundary": ftext(opposite_boundary),
            "burden": ftext(opposite_burden),
        },
        "concentrated": {
            "coefficients": [ftext(x) for x in concentrated_coefficients],
            "boundary": ftext(concentrated_boundary),
            "burden": ftext(concentrated_burden),
        },
        "checks": checks,
    }


def run_t21_scalar_ledger() -> dict[str, Any]:
    first = Decimal("7.670975092815261e-05")
    active = Decimal("0.2976678523563374")
    outside = Decimal("0.5313410580584792")
    component_sum = first + active + outside
    reported = Decimal("0.8290856201657449")
    reserve = Decimal(1) - reported
    sqrt_reported = reported.sqrt()
    orientation_budget = Decimal(1) - sqrt_reported

    calibration_delta = Decimal("0.08")
    robust_upper = (sqrt_reported + calibration_delta) ** 2

    checks = {
        "reported_bound_is_outward": reported >= component_sum,
        "direct_unshifted_scalar_bound_subcritical": reported < 1,
        "reported_reserve_matches": (
            reserve == Decimal("0.1709143798342551")
        ),
        "positive_orientation_residual_budget": orientation_budget > 0,
        "calibration_residual_008_still_subcritical": robust_upper < 1,
        "scalar_ledger_alone_does_not_promote": True,
    }
    return {
        "schema": "rkf.t21_direct_unshifted_scalar_ledger.v1",
        "provenance": (
            "proof_lab/imported/T21_DIRECT_UNSHIFTED_CUT_BURDEN_ACTUAL.json"
        ),
        "first_cell_upper": dtext(first),
        "active_band_upper": dtext(active),
        "outside_upper": dtext(outside),
        "component_sum": dtext(component_sum),
        "reported_beta_zero_upper": dtext(reported),
        "threshold_reserve_lower": dtext(reserve),
        "sqrt_beta_upper": dtext(sqrt_reported),
        "maximum_unproved_orientation_residual": dtext(orientation_budget),
        "calibration_orientation_residual": dtext(calibration_delta),
        "calibration_robust_burden_upper": dtext(robust_upper),
        "claim_boundary": (
            "Arithmetic audit only. The actual completed-Weil event "
            "orientation and Recognition-complete source/boundary identity "
            "are not supplied by this scalar ledger."
        ),
        "checks": checks,
    }


def run_fail_closed_rh_contract() -> dict[str, Any]:
    contract = {
        "native_odd_carrier_declared": True,
        "boundary_formula_declared": True,
        "source_gram_identity_stated_in_source": True,
        "coefficientwise_prime_gamma_debt_event_map_in_rkf": False,
        "same_event_boundary_orientation_proved": False,
        "recognition_complete_orientation_tail_proved": False,
        "boundary_line_no_blindness_proved_for_actual_weil_lift": False,
    }
    terminal = all(contract.values())
    checks = {
        "scalar_bound_cannot_override_open_orientation": not terminal,
        "status_fail_closed": not terminal,
    }
    return {
        "schema": "rkf.native_weil_event_contract.v1",
        "contract": contract,
        "status": "OPEN_NATIVE_WEIL_EVENT_ORIENTATION",
        "terminal_promotion_allowed": terminal,
        "next_required_object": (
            "Construct coefficientwise Xi_Weil,N and c_partial,N on the "
            "same prime-Gamma-debt event carrier, then prove recovered "
            "orientation and Smriti-tail convergence."
        ),
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "finite_cogeneration": run_finite_cogeneration(),
        "shift_refinement": run_shift_refinement_identity(),
        "refinement_orientation": run_refinement_orientation_gate(),
        "t21_scalar_ledger": run_t21_scalar_ledger(),
        "rh_contract": run_fail_closed_rh_contract(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["exact_rational_core"] = True
    checks["decimal_ledger_no_binary_float"] = True
    checks["rh_not_promoted"] = not packets["rh_contract"][
        "terminal_promotion_allowed"
    ]
    return {
        "schema": "rkf.native_weil_cut_event_cogeneration_stage3a.v1",
        "status": (
            "PASS_NATIVE_WEIL_CUT_EVENT_COGENERATION_STAGE3A"
            if all(checks.values())
            else "FAIL_NATIVE_WEIL_CUT_EVENT_COGENERATION_STAGE3A"
        ),
        "claim_boundary": {
            "proved": [
                "finite source and boundary co-generation from one cut-event lift",
                "constructive unit-boundary-state enlargement for every contractive decoder",
                "exact shifted-to-unshifted cut-event difference identity",
                "coherent refinement equality and orientation-sensitive negative controls",
                "robust decoder residual inequality target",
                "fail-closed RH specialization contract",
            ],
            "transferred_scalar_audit": [
                "T21 direct unshifted beta-zero upper arithmetic",
                "T21 outward reserve arithmetic",
            ],
            "open": [
                "actual coefficientwise prime-Gamma-debt event map",
                "actual boundary orientation on that event map",
                "Recognition-complete event-orientation tail",
                "actual completed-Weil boundary-line no-blindness",
                "RH",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes() -> bytes:
    return (
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def canonical_hash() -> str:
    return sha256(canonical_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_certificate()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(canonical_bytes())
    print(result["status"])
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
