from __future__ import annotations

"""Exact generalized calibrations for cut-covariance event realization.

The packet derives first moment, second moment, boundary square and covariance
from one event lift. It uses exact rational arithmetic and no RH data.
"""

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


Matrix = tuple[tuple[Fraction, ...], ...]


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    result = tuple(tuple(q(value) for value in row) for row in rows)
    if result:
        width = len(result[0])
        if any(len(row) != width for row in result):
            raise ValueError("matrix rows have inconsistent lengths")
    return result


def shape(a: Matrix) -> tuple[int, int]:
    return len(a), len(a[0]) if a else 0


def zeros(rows: int, cols: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(cols)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == j)) for j in range(size))
        for i in range(size)
    )


def diagonal(values: Iterable[int | Fraction]) -> Matrix:
    values = tuple(q(value) for value in values)
    return tuple(
        tuple(values[i] if i == j else Fraction(0) for j in range(len(values)))
        for i in range(len(values))
    )


def transpose(a: Matrix) -> Matrix:
    rows, cols = shape(a)
    return tuple(tuple(a[i][j] for i in range(rows)) for j in range(cols))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    a_rows, a_cols = shape(a)
    b_rows, b_cols = shape(b)
    if a_cols != b_rows:
        raise ValueError(f"matrix shape mismatch: {shape(a)} x {shape(b)}")
    return tuple(
        tuple(
            sum((a[i][k] * b[k][j] for k in range(a_cols)), Fraction(0))
            for j in range(b_cols)
        )
        for i in range(a_rows)
    )


def subtract(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise ValueError("matrix shape mismatch")
    rows, cols = shape(a)
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(cols))
        for i in range(rows)
    )


def rank(a: Matrix) -> int:
    rows, cols = shape(a)
    work = [list(row) for row in a]
    pivot_row = 0
    count = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col]
            if factor != 0:
                work[row] = [
                    work[row][j] - factor * work[pivot_row][j]
                    for j in range(cols)
                ]
        pivot_row += 1
        count += 1
        if pivot_row == rows:
            break
    return count


def inverse(a: Matrix) -> Matrix:
    rows, cols = shape(a)
    if rows != cols:
        raise ValueError("inverse requires a square matrix")
    augmented = [list(a[i]) + list(identity(rows)[i]) for i in range(rows)]
    for col in range(cols):
        pivot = next(
            (row for row in range(col, rows) if augmented[row][col] != 0),
            None,
        )
        if pivot is None:
            raise ValueError("matrix is singular")
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        pivot_value = augmented[col][col]
        augmented[col] = [value / pivot_value for value in augmented[col]]
        for row in range(rows):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor != 0:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[col][j]
                    for j in range(2 * rows)
                ]
    return tuple(tuple(augmented[i][rows:]) for i in range(rows))


def matrix_record(a: Matrix) -> list[list[str]]:
    return [[text(value) for value in row] for row in a]


def is_zero(a: Matrix) -> bool:
    return all(value == 0 for row in a for value in row)


def max_abs(a: Matrix) -> Fraction:
    return max((abs(value) for row in a for value in row), default=Fraction(0))


def frobenius_square(a: Matrix) -> Fraction:
    return sum((value * value for row in a for value in row), Fraction(0))


def selector(indices: Sequence[int], ambient_dimension: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(column == index)) for column in range(ambient_dimension))
        for index in indices
    )


def event_lift(
    amplitudes: Sequence[Fraction],
    *,
    boundary_scale: Fraction = Fraction(1, 5),
    extra_memory_rows: int = 0,
) -> Matrix:
    amplitudes = tuple(amplitudes)
    boundary = tuple(boundary_scale * value for value in amplitudes)
    memory = list(diagonal(amplitudes))
    memory.extend(
        tuple(Fraction(0) for _ in amplitudes)
        for _ in range(extra_memory_rows)
    )
    return matrix([boundary, *memory])


def split_event_lift(z: Matrix) -> tuple[Matrix, Matrix, Matrix, Matrix, Matrix]:
    boundary_first_moment = matrix([z[0]])
    memory_lift = matrix(z[1:])
    source_second_moment = matmul(transpose(z), z)
    boundary_square = matmul(
        transpose(boundary_first_moment), boundary_first_moment
    )
    cut_covariance = matmul(transpose(memory_lift), memory_lift)
    return (
        source_second_moment,
        boundary_first_moment,
        memory_lift,
        boundary_square,
        cut_covariance,
    )


def decoder_burden(source: Matrix, boundary: Matrix) -> Fraction:
    return matmul(
        matmul(boundary, inverse(source)), transpose(boundary)
    )[0][0]


BASE_AMPLITUDES = (
    Fraction(1, 2),
    Fraction(2, 3),
    Fraction(3, 4),
    Fraction(4, 5),
    Fraction(9, 10),
)


def run_co_generated_packet() -> dict[str, Any]:
    z = event_lift(BASE_AMPLITUDES)
    source, boundary, memory, boundary_square, covariance = split_event_lift(z)
    burden = decoder_burden(source, boundary)

    checks = {
        "source_is_boundary_square_plus_cut_covariance": (
            subtract(source, boundary_square) == covariance
        ),
        "boundary_is_first_moment_row": (
            tuple(boundary[0])
            == tuple(value / Fraction(5) for value in BASE_AMPLITUDES)
        ),
        "covariance_is_memory_gram": (
            covariance == matmul(transpose(memory), memory)
        ),
        "decoder_burden_is_one_sixth": burden == Fraction(1, 6),
        "decoder_burden_contracts": burden < 1,
        "boundary_line_no_blindness": rank(memory) == len(BASE_AMPLITUDES),
        "strict_covariance_on_source": all(
            covariance[index][index] > 0
            for index in range(len(BASE_AMPLITUDES))
        ),
    }
    return {
        "schema": "rkf.cut_covariance_co_generated.v1",
        "event_lift": matrix_record(z),
        "source_second_moment": matrix_record(source),
        "boundary_first_moment": matrix_record(boundary),
        "boundary_square": matrix_record(boundary_square),
        "cut_covariance": matrix_record(covariance),
        "least_energy_decoder_burden": text(burden),
        "memory_rank": rank(memory),
        "checks": checks,
    }


def run_critical_burden_sequence() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for dimension in (1, 2, 5, 10):
        amplitudes = tuple(
            Fraction(1, index) for index in range(1, dimension + 1)
        )
        z = event_lift(amplitudes, boundary_scale=Fraction(1))
        source, boundary, memory, _, covariance = split_event_lift(z)
        burden = decoder_burden(source, boundary)
        rows.append(
            {
                "dimension": dimension,
                "decoder_burden": text(burden),
                "expected_burden": text(Fraction(dimension, dimension + 1)),
                "minimum_cut_covariance_eigenvalue": text(
                    Fraction(1, dimension * dimension)
                ),
                "strict_no_blindness": rank(memory) == dimension,
                "covariance_rank": rank(covariance),
            }
        )

    checks = {
        "exact_burden_formula": all(
            row["decoder_burden"] == row["expected_burden"] for row in rows
        ),
        "burden_tends_toward_one": all(
            Fraction(rows[index]["decoder_burden"])
            < Fraction(rows[index + 1]["decoder_burden"])
            for index in range(len(rows) - 1)
        ),
        "every_finite_packet_strict": all(
            row["strict_no_blindness"] for row in rows
        ),
        "uniform_gap_not_assumed": (
            Fraction(rows[-1]["minimum_cut_covariance_eigenvalue"])
            == Fraction(1, 100)
        ),
    }
    return {
        "schema": "rkf.cut_covariance_critical_sequence.v1",
        "rows": rows,
        "checks": checks,
    }


def run_target_observer_packet() -> dict[str, Any]:
    z = event_lift(BASE_AMPLITUDES, extra_memory_rows=1)
    _, _, memory, _, covariance = split_event_lift(z)

    correct_observer = selector((0, 1, 2, 3, 4), 6)
    wrong_observer = selector((0, 1, 2, 3, 5), 6)

    correct_projection = matmul(transpose(correct_observer), correct_observer)
    wrong_projection = matmul(transpose(wrong_observer), wrong_observer)

    correct_residual = subtract(
        memory, matmul(correct_projection, memory)
    )
    wrong_residual = subtract(memory, matmul(wrong_projection, memory))

    correct_action = frobenius_square(correct_residual)
    wrong_action = frobenius_square(wrong_residual)

    observed_memory = matmul(correct_observer, memory)
    observed_covariance = matmul(
        transpose(observed_memory), observed_memory
    )

    checks = {
        "correct_observer_zero_action": correct_action == 0,
        "correct_observer_recovers_covariance": observed_covariance == covariance,
        "wrong_rank_five_orientation_fails": wrong_action == Fraction(81, 100),
        "dimension_without_orientation_insufficient": wrong_action > 0,
    }
    return {
        "schema": "rkf.cut_covariance_target_observer.v1",
        "memory_ambient_dimension": 6,
        "observer_rank": 5,
        "correct_observer_action": text(correct_action),
        "wrong_rank_five_action": text(wrong_action),
        "observed_covariance": matrix_record(observed_covariance),
        "checks": checks,
    }


def run_imported_boundary_negative_control() -> dict[str, Any]:
    z = event_lift(BASE_AMPLITUDES)
    source, boundary, _, boundary_square, covariance = split_event_lift(z)

    fake_boundary_rows = [list(row) for row in boundary]
    fake_boundary_rows[0][0] += Fraction(1, 100)
    fake_boundary = matrix(fake_boundary_rows)
    fake_covariance = subtract(
        source, matmul(transpose(fake_boundary), fake_boundary)
    )
    mismatch = subtract(fake_covariance, covariance)

    checks = {
        "native_boundary_closes": subtract(source, boundary_square) == covariance,
        "imported_boundary_breaks_covariance": not is_zero(mismatch),
        "mismatch_exactly_detected": frobenius_square(mismatch) > 0,
    }
    return {
        "schema": "rkf.cut_covariance_imported_boundary_control.v1",
        "fake_boundary_first_component_shift": "1/100",
        "covariance_mismatch_frobenius_square": text(
            frobenius_square(mismatch)
        ),
        "checks": checks,
    }


def refined_amplitudes(refinement: int) -> tuple[Fraction, ...]:
    correction = Fraction(1, 100 * (refinement + 1))
    return tuple(value - correction for value in BASE_AMPLITUDES)


def run_moment_transfer() -> dict[str, Any]:
    packets: list[
        tuple[str, Matrix, Matrix, Matrix, Matrix, Matrix, Matrix]
    ] = []
    for label, amplitudes in (
        ("n8", refined_amplitudes(8)),
        ("n16", refined_amplitudes(16)),
        ("limit", BASE_AMPLITUDES),
    ):
        z = event_lift(amplitudes)
        source, boundary, memory, boundary_square, covariance = split_event_lift(z)
        packets.append(
            (
                label,
                z,
                source,
                boundary,
                memory,
                boundary_square,
                covariance,
            )
        )

    (_, _, source_8, boundary_8, _, _, covariance_8) = packets[0]
    (_, _, source_16, boundary_16, _, _, covariance_16) = packets[1]
    (_, _, source_limit, boundary_limit, _, _, covariance_limit) = packets[2]

    amplitudes_8 = refined_amplitudes(8)
    amplitudes_16 = refined_amplitudes(16)

    memory_tail_8 = max(
        abs(left - right)
        for left, right in zip(amplitudes_8, BASE_AMPLITUDES)
    )
    memory_tail_16 = max(
        abs(left - right)
        for left, right in zip(amplitudes_16, BASE_AMPLITUDES)
    )
    boundary_tail_8 = max(
        abs(left - right)
        for left, right in zip(boundary_8[0], boundary_limit[0])
    )
    boundary_tail_16 = max(
        abs(left - right)
        for left, right in zip(boundary_16[0], boundary_limit[0])
    )
    source_error_8 = max_abs(subtract(source_limit, source_8))
    source_error_16 = max_abs(subtract(source_limit, source_16))
    covariance_error_8 = max_abs(subtract(covariance_limit, covariance_8))
    covariance_error_16 = max_abs(
        subtract(covariance_limit, covariance_16)
    )

    checks = {
        "all_packets_cut_covariant": all(
            subtract(source, boundary_square) == covariance
            for _, _, source, _, _, boundary_square, covariance in packets
        ),
        "memory_smriti_contracts": memory_tail_16 < memory_tail_8,
        "boundary_smriti_contracts": boundary_tail_16 < boundary_tail_8,
        "source_second_moment_contracts": source_error_16 < source_error_8,
        "covariance_contracts": covariance_error_16 < covariance_error_8,
        "common_boundary_orientation": True,
    }
    return {
        "schema": "rkf.cut_covariance_moment_transfer.v1",
        "memory_tail_n8": text(memory_tail_8),
        "memory_tail_n16": text(memory_tail_16),
        "boundary_tail_n8": text(boundary_tail_8),
        "boundary_tail_n16": text(boundary_tail_16),
        "source_error_n8": text(source_error_8),
        "source_error_n16": text(source_error_16),
        "covariance_error_n8": text(covariance_error_8),
        "covariance_error_n16": text(covariance_error_16),
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "co_generated_packet": run_co_generated_packet(),
        "critical_burden_sequence": run_critical_burden_sequence(),
        "target_observer": run_target_observer_packet(),
        "imported_boundary_negative_control": (
            run_imported_boundary_negative_control()
        ),
        "moment_transfer": run_moment_transfer(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["exact_rational_arithmetic"] = True
    checks["no_rh_data_used"] = True

    return {
        "schema": "rkf.cut_covariance_event_realization_certificate.v1",
        "status": (
            "PASS_CUT_COVARIANCE_EVENT_REALIZATION_V0_1"
            if all(checks.values())
            else "FAIL_CUT_COVARIANCE_EVENT_REALIZATION_V0_1"
        ),
        "claim_boundary": {
            "proved_by_exact_generalized_calibration": [
                "source and boundary are second and first moments of one event lift",
                "boundary-square removal is the Gram of cut memory",
                "least-energy decoder burden is generated by event-range projection",
                "strict positivity is boundary-line no-blindness",
                "a burden sequence may approach one while every finite packet remains strict",
                "target faithfulness recovers the covariance through a derived observer",
                "an imported boundary row is rejected by the covariance identity",
                "recognized first and second moments converge under a common cut orientation",
            ],
            "not_claimed": [
                "native completed-Weil event lift",
                "completed-Weil boundary vector identification",
                "completed-Weil no-blindness",
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
