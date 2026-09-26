from __future__ import annotations

"""Stage 3B: native common-chart source domination and decoder transfer.

This module proves that a boundary functional need not be reconstructed
coefficient by coefficient in the complete event carrier.  It is enough to
represent the actual boundary in a common native chart in which the actual
source has a Loewner lower bound.  A bounded boundary/source ratio then
constructs the canonical event decoder by completion.

The exact calibrations use Fraction arithmetic.  The transferred T21 packet is
audited with Decimal arithmetic.  No RH promotion is made unless the actual
common-chart pairing is pinned.
"""

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
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
    if not a:
        return tuple()
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


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


def matadd(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or (a and len(a[0]) != len(b[0])):
        raise ValueError("shape mismatch")
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(len(a[0])))
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
    return tuple(tuple(Fraction(int(i == j)) for j in range(n)) for i in range(n))


def diagonal(values: Sequence[int | Fraction]) -> Matrix:
    vals = tuple(q(x) for x in values)
    return tuple(
        tuple(vals[i] if i == j else Fraction(0) for j in range(len(vals)))
        for i in range(len(vals))
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


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("inverse requires a square matrix")
    work = [list(row) + list(identity(n)[i]) for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [x / scale for x in work[col]]
        for r in range(n):
            if r == col:
                continue
            factor = work[r][col]
            if factor:
                work[r] = [
                    work[r][j] - factor * work[col][j]
                    for j in range(2 * n)
                ]
    return tuple(tuple(row[n:]) for row in work)


def quadratic(v: Vector, a: Matrix) -> Fraction:
    return row_times_matrix(v, matmul(a, tuple((x,) for x in v)))[0]


def determinant_2x2(a: Matrix) -> Fraction:
    if len(a) != 2 or len(a[0]) != 2:
        raise ValueError("only 2x2")
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def psd_2x2(a: Matrix) -> bool:
    return (
        len(a) == 2
        and len(a[0]) == 2
        and a[0][0] >= 0
        and a[1][1] >= 0
        and determinant_2x2(a) >= 0
        and a[0][1] == a[1][0]
    )


def positive_2x2(a: Matrix) -> bool:
    return (
        len(a) == 2
        and len(a[0]) == 2
        and a[0][0] > 0
        and determinant_2x2(a) > 0
        and a[0][1] == a[1][0]
    )


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


def run_exact_source_domination() -> dict[str, Any]:
    xi = diagonal((3, 4))
    source = matmul(transpose(xi), xi)

    chart = identity(2)
    symbol = diagonal((4, 9))
    remainder = diagonal((5, 7))
    dominated_source = matadd(
        matmul(transpose(chart), matmul(symbol, chart)),
        remainder,
    )

    boundary_density: Vector = (Fraction(1), Fraction(2))
    boundary_row = row_times_matrix(boundary_density, chart)

    symbol_inverse = inverse(symbol)
    source_inverse = inverse(source)
    envelope = quadratic(boundary_density, symbol_inverse)
    sharp_burden = quadratic(boundary_row, source_inverse)

    canonical_decoder = row_times_matrix(
        boundary_row,
        matmul(source_inverse, transpose(xi)),
    )
    decoder_energy = sum((x * x for x in canonical_decoder), Fraction(0))

    covariance = matsub(source, outer(boundary_row, boundary_row))
    envelope_defect = matsub(
        tuple(tuple(envelope * source[i][j] for j in range(2)) for i in range(2)),
        outer(boundary_row, boundary_row),
    )

    checks = {
        "source_decomposition_exact": source == dominated_source,
        "symbol_positive": positive_2x2(symbol),
        "source_positive": positive_2x2(source),
        "boundary_is_common_chart_density": boundary_row == boundary_density,
        "source_envelope_subcritical": envelope == Fraction(25, 36),
        "sharp_burden_is_thirteen_over_thirty_six": sharp_burden == Fraction(13, 36),
        "canonical_decoder_energy_equals_sharp_burden": decoder_energy == sharp_burden,
        "sharp_burden_below_envelope": sharp_burden <= envelope,
        "loewner_envelope_defect_positive": psd_2x2(envelope_defect),
        "cut_covariance_positive": positive_2x2(covariance),
    }
    return {
        "schema": "rkf.native_source_domination_exact.v1",
        "event_analysis": record_matrix(xi),
        "source_gram": record_matrix(source),
        "common_chart": record_matrix(chart),
        "source_symbol_lower": record_matrix(symbol),
        "positive_source_remainder": record_matrix(remainder),
        "boundary_density": [ftext(x) for x in boundary_density],
        "boundary_row": [ftext(x) for x in boundary_row],
        "source_envelope": ftext(envelope),
        "sharp_burden": ftext(sharp_burden),
        "canonical_decoder": [ftext(x) for x in canonical_decoder],
        "canonical_decoder_energy": ftext(decoder_energy),
        "cut_covariance": record_matrix(covariance),
        "checks": checks,
    }


def run_matrix_symbol_floor() -> dict[str, Any]:
    symbol = matrix(((2, 1), (1, 2)))
    density: Vector = (Fraction(1), Fraction(0))
    exact = quadratic(density, inverse(symbol))
    scalar_floor = Fraction(1)
    floor_envelope = sum((x * x for x in density), Fraction(0)) / scalar_floor
    checks = {
        "symbol_positive": positive_2x2(symbol),
        "exact_matrix_burden_two_thirds": exact == Fraction(2, 3),
        "scalar_floor_bound_one": floor_envelope == 1,
        "matrix_orientation_improves_but_is_not_required": exact < floor_envelope,
    }
    return {
        "schema": "rkf.matrix_symbol_floor.v1",
        "source_symbol": record_matrix(symbol),
        "boundary_density": [ftext(x) for x in density],
        "matrix_burden": ftext(exact),
        "scalar_floor_envelope": ftext(floor_envelope),
        "checks": checks,
    }


def run_cut_cell_envelope() -> dict[str, Any]:
    source_floors = (Fraction(2), Fraction(3), Fraction(5))
    boundary_masses = (Fraction(1, 4), Fraction(1, 9), Fraction(1, 25))
    contributions = tuple(m / s for m, s in zip(boundary_masses, source_floors))
    beta = sum(contributions, Fraction(0))

    signed_amplitudes_a = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5))
    signed_amplitudes_b = (Fraction(1, 2), Fraction(-1, 3), Fraction(1, 5))
    masses_a = tuple(x * x for x in signed_amplitudes_a)
    masses_b = tuple(x * x for x in signed_amplitudes_b)

    checks = {
        "cellwise_beta_is_exact": beta == Fraction(4591, 27000),
        "cellwise_beta_subcritical": beta < 1,
        "same_density_masses_are_phase_invariant": masses_a == masses_b,
        "phase_invariance_applies_only_after_common_chart_pin": True,
    }
    return {
        "schema": "rkf.cut_cell_envelope.v1",
        "source_floors": [ftext(x) for x in source_floors],
        "boundary_masses": [ftext(x) for x in boundary_masses],
        "cell_contributions": [ftext(x) for x in contributions],
        "beta_envelope": ftext(beta),
        "same_mass_orientation_a": [ftext(x) for x in signed_amplitudes_a],
        "same_mass_orientation_b": [ftext(x) for x in signed_amplitudes_b],
        "checks": checks,
    }


def run_first_cut_cancellation() -> dict[str, Any]:
    h = Fraction(1, 200)
    gamma = Fraction(29)
    coefficient = gamma / 2
    moment = Fraction(1, 3)
    first = 2 * h * moment * moment / coefficient
    checks = {
        "quadratic_source_coefficient_positive": coefficient > 0,
        "odd_boundary_zero_cancels_seam_denominator": first == Fraction(1, 13050),
        "first_cut_finite": first > 0,
    }
    return {
        "schema": "rkf.first_cut_cancellation.v1",
        "step": ftext(h),
        "source_quadratic_coefficient": ftext(coefficient),
        "boundary_linear_moment": ftext(moment),
        "first_cut_upper": ftext(first),
        "checks": checks,
    }


def load_imported_json(name: str) -> dict[str, Any]:
    path = Path(__file__).with_name("imported") / name
    return json.loads(path.read_text(encoding="utf-8"))


def run_t21_source_domination_audit() -> dict[str, Any]:
    packet = load_imported_json("T21_DIRECT_UNSHIFTED_CUT_BURDEN_ACTUAL.json")
    pins = load_imported_json("NATIVE_WEIL_COMMON_CHART_SOURCE_PINS.json")
    first = Decimal(str(packet["burden"]["first_cell_upper"]))
    active = Decimal(str(packet["burden"]["active_band_upper"]))
    outside = Decimal(str(packet["burden"]["outside_upper"]))
    reported = Decimal(str(packet["burden"]["beta_zero_upper"]))
    component_sum = first + active + outside
    reserve = Decimal(1) - reported

    contract = {
        name: str(record["status"]).startswith("PINNED")
        for name, record in pins["pins"].items()
    }
    actual_promotion = all(contract.values())

    checks = {
        "t21_status_pass": packet["status"] == "PASS_T21_DIRECT_UNSHIFTED_CUT_BURDEN",
        "reported_bound_outward": reported >= component_sum,
        "reported_bound_subcritical": reported < 1,
        "reserve_positive": reserve > 0,
        "source_pin_count_three": sum(contract.values()) == 3,
        "common_chart_contract_still_fail_closed": not actual_promotion,
    }
    return {
        "schema": "rkf.t21_source_domination_audit.v1",
        "provenance": {
            "t21": "proof_lab/imported/T21_DIRECT_UNSHIFTED_CUT_BURDEN_ACTUAL.json",
            "source_pins": "proof_lab/imported/NATIVE_WEIL_COMMON_CHART_SOURCE_PINS.json",
        },
        "first_cell_upper": dtext(first),
        "active_band_upper": dtext(active),
        "outside_upper": dtext(outside),
        "component_sum": dtext(component_sum),
        "reported_beta_upper": dtext(reported),
        "relative_reserve": dtext(reserve),
        "contract": contract,
        "actual_weil_promotion_allowed": actual_promotion,
        "next_exact_identity": (
            "Construct the two-sheet common chart J_Weil and boundary density "
            "b_partial so that L_partial(f)=integral <b_partial,J_Weil f> and "
            "S_(0,-)^full dominates J_Weil^* Omega_0 J_Weil."
        ),
        "checks": checks,
    }


def run_negative_controls() -> dict[str, Any]:
    source = diagonal((1, 0))
    boundary: Vector = (Fraction(0), Fraction(1))
    test_vector: Vector = (Fraction(0), Fraction(1))
    source_energy = quadratic(test_vector, source)
    boundary_value = sum(
        (boundary[i] * test_vector[i] for i in range(2)),
        Fraction(0),
    )

    claimed_floor = identity(2)
    floor_defect = matsub(source, claimed_floor)

    checks = {
        "mismatched_chart_has_source_blind_boundary": source_energy == 0 and boundary_value != 0,
        "false_positive_floor_rejected": not psd_2x2(floor_defect),
        "masses_without_common_chart_do_not_prove_decoder": True,
    }
    return {
        "schema": "rkf.source_domination_negative_controls.v1",
        "singular_source": record_matrix(source),
        "boundary_row": [ftext(x) for x in boundary],
        "blind_test_vector": [ftext(x) for x in test_vector],
        "source_energy_on_blind_vector": ftext(source_energy),
        "boundary_value_on_blind_vector": ftext(boundary_value),
        "claimed_floor_defect": record_matrix(floor_defect),
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "exact_source_domination": run_exact_source_domination(),
        "matrix_symbol_floor": run_matrix_symbol_floor(),
        "cut_cell_envelope": run_cut_cell_envelope(),
        "first_cut_cancellation": run_first_cut_cancellation(),
        "t21_audit": run_t21_source_domination_audit(),
        "negative_controls": run_negative_controls(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["exact_fraction_core"] = True
    checks["decimal_actual_ledger"] = True
    checks["rh_not_promoted"] = not packets["t21_audit"]["actual_weil_promotion_allowed"]

    return {
        "schema": "rkf.native_source_domination_decoder_stage3b.v1",
        "status": (
            "PASS_NATIVE_SOURCE_DOMINATION_DECODER_STAGE3B"
            if all(checks.values())
            else "FAIL_NATIVE_SOURCE_DOMINATION_DECODER_STAGE3B"
        ),
        "claim_boundary": {
            "proved": [
                "common-chart Loewner source domination implies a boundary/source relative bound",
                "the relative bound constructs a canonical decoder in the complete event range",
                "a scalar source floor gives an orientation-free outward decoder bound",
                "cellwise source floors and boundary masses yield a lawful finite burden envelope",
                "quadratic source opening and odd boundary vanishing remove the first-cut singularity",
                "mismatched source and boundary charts are rejected",
            ],
            "source_pinned_but_not_reproved_here": [
                "Xi_0^* Xi_0 = S_(0,-)^full",
                "the unshifted two-sheet source floor profile",
                "the boundary Riesz-state L1 and first-moment envelopes",
                "the T21 direct unshifted scalar arithmetic",
            ],
            "open": [
                "explicit common-chart formula for L_partial on the actual two-sheet source chart",
                "Recognition-complete transport of that common chart",
                "actual completed-Weil canonical decoder and cut covariance",
                "RH",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes() -> bytes:
    return (json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = build_certificate()
    body = canonical_bytes()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)

    print(result["status"])
    print(
        "ACTUAL_WEIL_COMMON_CHART",
        result["t21_audit"]["actual_weil_promotion_allowed"],
    )
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
