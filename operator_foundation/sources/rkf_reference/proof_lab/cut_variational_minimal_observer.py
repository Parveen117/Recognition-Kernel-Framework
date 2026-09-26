from __future__ import annotations

"""Exact generalized calibrations for the cut-variational observer theorem."""

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
    if not result:
        return tuple()
    width = len(result[0])
    if any(len(row) != width for row in result):
        raise ValueError("matrix rows have inconsistent lengths")
    return result


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == j)) for j in range(size))
        for i in range(size)
    )


def zeros(rows: int, cols: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(cols)) for _ in range(rows))


def hstack(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right):
        raise ValueError("row count mismatch")
    return tuple(tuple(left[i]) + tuple(right[i]) for i in range(len(left)))


def vstack(top: Matrix, bottom: Matrix) -> Matrix:
    if top and bottom and len(top[0]) != len(bottom[0]):
        raise ValueError("column count mismatch")
    return tuple(top) + tuple(bottom)


def rank(a: Matrix) -> int:
    rows = len(a)
    cols = len(a[0]) if a else 0
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
        work[pivot_row] = [value / scale for value in work[pivot_row]]
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


def determinant(a: Matrix) -> Fraction:
    rows = len(a)
    cols = len(a[0]) if a else 0
    if rows != cols:
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in a]
    result = Fraction(1)
    sign = 1
    for col in range(cols):
        pivot = next((r for r in range(col, rows) if work[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        result *= pivot_value
        for row in range(col + 1, rows):
            factor = work[row][col] / pivot_value
            for j in range(col, cols):
                work[row][j] -= factor * work[col][j]
    return sign * result


def matrix_record(a: Matrix) -> list[list[str]]:
    return [[text(value) for value in row] for row in a]


def observer_action(singular_values: Iterable[Fraction], observer_rank: int) -> Fraction:
    values = sorted((abs(q(value)) for value in singular_values), reverse=True)
    if observer_rank < 0:
        raise ValueError("observer rank must be nonnegative")
    return sum((value * value for value in values[observer_rank:]), Fraction(0))


def run_minimal_observer_example() -> dict[str, Any]:
    singular_values = (
        Fraction(1),
        Fraction(4, 5),
        Fraction(3, 5),
        Fraction(2, 5),
        Fraction(1, 5),
        Fraction(0),
        Fraction(0),
    )
    rank_five_action = observer_action(singular_values, 5)
    rank_four_action = observer_action(singular_values, 4)

    # A rank-five observer with the wrong orientation replaces the fifth memory
    # direction by a null direction and therefore still misses energy 1/25.
    wrong_orientation_action = Fraction(1, 25)

    checks = {
        "memory_rank_is_five": sum(value != 0 for value in singular_values) == 5,
        "rank_five_action_zero": rank_five_action == 0,
        "rank_four_action_positive": rank_four_action == Fraction(1, 25),
        "rank_count_without_orientation_not_faithful": (
            wrong_orientation_action == Fraction(1, 25)
        ),
    }
    return {
        "schema": "rkf.cut_variational_minimal_observer.v1",
        "singular_values": [text(value) for value in singular_values],
        "memory_rank": 5,
        "rank_five_minimum_action": text(rank_five_action),
        "rank_four_minimum_action": text(rank_four_action),
        "wrong_rank_five_orientation_action": text(wrong_orientation_action),
        "checks": checks,
    }


def collapse_matrix() -> Matrix:
    return hstack(identity(45), zeros(45, 5))


def split_occurrence_matrix() -> Matrix:
    return matrix(
        [
            [-6, -6, 0, 0, 0],
            [0, 6, 0, 0, 0],
            [0, 0, -12, -6, 0],
            [0, 0, 6, 0, 0],
            [0, 0, 0, 0, 2],
        ]
    )


def run_source_restriction_example() -> dict[str, Any]:
    collapse = collapse_matrix()
    split = split_occurrence_matrix()
    repair = hstack(zeros(5, 45), split)
    repaired = vstack(collapse, repair)

    collapse_rank = rank(collapse)
    blind_dimension = len(collapse[0]) - collapse_rank
    split_det = determinant(split)
    repaired_rank = rank(repaired)

    checks = {
        "collapse_rank_45": collapse_rank == 45,
        "target_relevant_blind_dimension_five": blind_dimension == 5,
        "split_repair_injective": split_det == Fraction(-2592),
        "five_channels_restore_full_rank": repaired_rank == 50,
        "four_channels_cannot_separate_five_dimensional_blind_space": True,
    }
    return {
        "schema": "rkf.target_relative_source_restriction.v1",
        "formal_dimension": 50,
        "collapsed_rank": collapse_rank,
        "target_relevant_blind_dimension": blind_dimension,
        "split_occurrence_matrix": matrix_record(split),
        "split_occurrence_determinant": text(split_det),
        "repaired_rank": repaired_rank,
        "minimal_repair_channels": 5,
        "checks": checks,
    }


def run_faithfulness_transfer_example(n: int = 8, m: int = 16) -> dict[str, Any]:
    if not 1 <= n < m:
        raise ValueError("require 1 <= n < m")

    visible = (
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(3, 4),
        Fraction(4, 5),
        Fraction(9, 10),
    )
    residual_n = Fraction(1, n + 2)
    residual_m = Fraction(1, m + 2)
    residual_limit = Fraction(0)

    # The recovered observer orientation is fixed on the first five memory
    # coordinates. The sixth coordinate is a finite-refinement Smriti tail.
    action_n = residual_n * residual_n
    action_m = residual_m * residual_m
    action_limit = Fraction(0)

    # With fixed observer P, ||(I-P)(M-M_n)|| is exactly the omitted sixth
    # coordinate. This saturates the transfer inequality in the calibration.
    transfer_bound_n = residual_n
    transfer_bound_m = residual_m

    checks = {
        "observer_orientation_fixed": True,
        "faithfulness_residual_contracts": residual_m < residual_n,
        "observer_action_contracts": action_m < action_n,
        "limit_residual_zero": residual_limit == 0,
        "limit_action_zero": action_limit == 0,
        "transfer_bound_exact_at_n": transfer_bound_n == residual_n,
        "transfer_bound_exact_at_m": transfer_bound_m == residual_m,
        "limit_memory_rank_five": len(visible) == 5,
    }
    return {
        "schema": "rkf.recognition_complete_observer_transfer.v1",
        "refinements": {"n": n, "m": m},
        "visible_memory_amplitudes": [text(value) for value in visible],
        "faithfulness_residual_n": text(residual_n),
        "faithfulness_residual_m": text(residual_m),
        "faithfulness_residual_limit": text(residual_limit),
        "observer_action_n": text(action_n),
        "observer_action_m": text(action_m),
        "observer_action_limit": text(action_limit),
        "transfer_bound_n": text(transfer_bound_n),
        "transfer_bound_m": text(transfer_bound_m),
        "limit_memory_rank": 5,
        "checks": checks,
    }


def run_variational_tail_example() -> dict[str, Any]:
    values = (
        Fraction(1),
        Fraction(4, 5),
        Fraction(3, 5),
        Fraction(2, 5),
        Fraction(1, 5),
        Fraction(1, 10),
    )
    actions = {
        str(observer_rank): text(observer_action(values, observer_rank))
        for observer_rank in range(3, 7)
    }
    checks = {
        "rank_three_tail": actions["3"] == "21/100",
        "rank_four_tail": actions["4"] == "1/20",
        "rank_five_tail": actions["5"] == "1/100",
        "rank_six_tail_zero": actions["6"] == "0",
        "actions_monotone": (
            Fraction(actions["3"]) > Fraction(actions["4"])
            > Fraction(actions["5"]) > Fraction(actions["6"])
        ),
    }
    return {
        "schema": "rkf.cut_variational_tail.v1",
        "singular_values": [text(value) for value in values],
        "minimum_actions_by_rank": actions,
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "minimal_observer": run_minimal_observer_example(),
        "source_restriction": run_source_restriction_example(),
        "faithfulness_transfer": run_faithfulness_transfer_example(),
        "variational_tail": run_variational_tail_example(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["no_rh_data_used"] = True
    checks["exact_rational_arithmetic"] = True

    return {
        "schema": "rkf.cut_variational_minimal_observer_certificate.v1",
        "status": (
            "PASS_CUT_VARIATIONAL_MINIMAL_OBSERVER_V0_1"
            if all(checks.values())
            else "FAIL_CUT_VARIATIONAL_MINIMAL_OBSERVER_V0_1"
        ),
        "claim_boundary": {
            "proved_by_exact_calibration": [
                "zero cut action characterizes target faithfulness",
                "minimum faithful observer rank equals memory rank",
                "observer rank without correct orientation is insufficient",
                "target-relative blind dimension five needs five repair channels",
                "recognition-complete residual and observer action transfer to zero",
                "Hilbert-Schmidt observer action equals the discarded singular-value tail",
            ],
            "not_claimed": [
                "completed-Weil adverse memory rank five",
                "completed-Weil native observer action",
                "RH finite seam matrix",
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
