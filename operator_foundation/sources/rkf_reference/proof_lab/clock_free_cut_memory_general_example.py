from __future__ import annotations

"""Stage-1 generalized examples for the clock-free cut-memory calculus.

The examples use only declared arrows and exact rational arithmetic.  No
external time parameter, fitted Gram factor, spectral eigensolver, or classical
operator decomposition is used to define the objects.

The module contains four calibrations:

1. local transition closure with nonzero global seam holonomy;
2. exact composition residues from cut-corner multiplication;
3. target-blind stable repair with memory ranks 2 -> 1 -> 2;
4. a cut-generated five-memory packet whose full relative sign/gap problem is
   exactly represented by a 5 x 5 seam matrix.

This file is an implementation stage.  A separate test module is intentionally
reserved for the next stage.
"""

from dataclasses import dataclass
from fractions import Fraction
import argparse
import json
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


Number = Fraction
Matrix = tuple[tuple[Number, ...], ...]


# ---------------------------------------------------------------------------
# Exact matrix utilities
# ---------------------------------------------------------------------------


def _f(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    converted = tuple(tuple(_f(value) for value in row) for row in rows)
    if not converted:
        return tuple()
    width = len(converted[0])
    if any(len(row) != width for row in converted):
        raise ValueError("matrix rows have different lengths")
    return converted


def shape(a: Matrix) -> tuple[int, int]:
    return (len(a), len(a[0]) if a else 0)


def zeros(rows: int, cols: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(cols)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == j)) for j in range(size)) for i in range(size)
    )


def diagonal(values: Iterable[int | Fraction]) -> Matrix:
    values = tuple(_f(value) for value in values)
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


def add(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise ValueError("matrix shape mismatch")
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(shape(a)[1]))
        for i in range(shape(a)[0])
    )


def subtract(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise ValueError("matrix shape mismatch")
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(shape(a)[1]))
        for i in range(shape(a)[0])
    )


def vstack(a: Matrix, b: Matrix) -> Matrix:
    if shape(a)[1] != shape(b)[1]:
        raise ValueError("vertical stack width mismatch")
    return tuple(a) + tuple(b)


def hstack(a: Matrix, b: Matrix) -> Matrix:
    if shape(a)[0] != shape(b)[0]:
        raise ValueError("horizontal stack height mismatch")
    return tuple(tuple(a[i]) + tuple(b[i]) for i in range(shape(a)[0]))


def is_zero(a: Matrix) -> bool:
    return all(value == 0 for row in a for value in row)


def rank(a: Matrix) -> int:
    rows, cols = shape(a)
    work = [list(row) for row in a]
    pivot_row = 0
    pivot_count = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col] != 0),
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
        pivot_count += 1
        if pivot_row == rows:
            break
    return pivot_count


def determinant(a: Matrix) -> Fraction:
    rows, cols = shape(a)
    if rows != cols:
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in a]
    result = Fraction(1)
    sign = 1
    for col in range(cols):
        pivot = next((row for row in range(col, rows) if work[row][col] != 0), None)
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
    return result * sign


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix_record(a: Matrix) -> list[list[str]]:
    return [[fraction_text(value) for value in row] for row in a]


def transition_differential(g_source: Matrix, g_target: Matrix, arrow: Matrix) -> Matrix:
    return subtract(matmul(matmul(transpose(arrow), g_target), arrow), g_source)


# ---------------------------------------------------------------------------
# Example A: nonlinear seam holonomy
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PhaseSeamState:
    theta1: Fraction
    theta2: Fraction
    memory: int

    def normalized(self) -> "PhaseSeamState":
        return PhaseSeamState(self.theta1 % 1, self.theta2 % 1, self.memory)


@dataclass(frozen=True)
class SeamLedger:
    theta1: Fraction
    theta2: Fraction
    memory: int

    def normalized(self) -> "SeamLedger":
        return SeamLedger(self.theta1 % 1, self.theta2 % 1, self.memory)

    def is_zero(self) -> bool:
        value = self.normalized()
        return value.theta1 == 0 and value.theta2 == 0 and value.memory == 0


def _chi(theta1: Fraction) -> int:
    theta1 %= 1
    return 0 if theta1 < Fraction(1, 2) else 1


def _state_difference(target: PhaseSeamState, source: PhaseSeamState) -> SeamLedger:
    return SeamLedger(
        target.theta1 - source.theta1,
        target.theta2 - source.theta2,
        target.memory - source.memory,
    ).normalized()


def run_holonomy_example(beta: Fraction = Fraction(1, 7)) -> dict[str, Any]:
    initial = PhaseSeamState(Fraction(0), Fraction(0), 0)

    def arrow_a(state: PhaseSeamState) -> PhaseSeamState:
        return PhaseSeamState(
            state.theta1 + Fraction(1, 2), state.theta2, state.memory
        ).normalized()

    def arrow_a_inverse(state: PhaseSeamState) -> PhaseSeamState:
        return PhaseSeamState(
            state.theta1 - Fraction(1, 2), state.theta2, state.memory
        ).normalized()

    def arrow_b(state: PhaseSeamState) -> PhaseSeamState:
        return PhaseSeamState(
            state.theta1,
            state.theta2 + beta,
            state.memory + _chi(state.theta1),
        ).normalized()

    def arrow_b_inverse(state: PhaseSeamState) -> PhaseSeamState:
        return PhaseSeamState(
            state.theta1,
            state.theta2 - beta,
            state.memory - _chi(state.theta1),
        ).normalized()

    transitions: list[
        tuple[
            str,
            Callable[[PhaseSeamState], PhaseSeamState],
            Callable[[PhaseSeamState], SeamLedger],
        ]
    ] = [
        ("a", arrow_a, lambda _s: SeamLedger(Fraction(1, 2), Fraction(0), 0)),
        ("b", arrow_b, lambda s: SeamLedger(Fraction(0), beta, _chi(s.theta1))),
        (
            "a_inverse",
            arrow_a_inverse,
            lambda _s: SeamLedger(Fraction(-1, 2), Fraction(0), 0),
        ),
        (
            "b_inverse",
            arrow_b_inverse,
            lambda s: SeamLedger(Fraction(0), -beta, -_chi(s.theta1)),
        ),
    ]

    current = initial
    local_records: list[dict[str, Any]] = []
    for name, transport, ledger_fn in transitions:
        ledger = ledger_fn(current)
        target = transport(current)
        observed = _state_difference(target, current)
        residue = SeamLedger(
            observed.theta1 - ledger.theta1,
            observed.theta2 - ledger.theta2,
            observed.memory - ledger.memory,
        ).normalized()
        local_records.append(
            {
                "arrow": name,
                "ledger": {
                    "theta1": fraction_text(ledger.theta1),
                    "theta2": fraction_text(ledger.theta2),
                    "memory": ledger.memory,
                },
                "local_residue_zero": residue.is_zero(),
            }
        )
        current = target

    holonomy = _state_difference(current, initial)
    return {
        "schema": "rkf.clock_free_holonomy.v1",
        "clock_used": False,
        "visible_return": (
            current.theta1 == initial.theta1 and current.theta2 == initial.theta2
        ),
        "memory_holonomy": holonomy.memory,
        "all_local_residues_zero": all(
            record["local_residue_zero"] for record in local_records
        ),
        "steps": local_records,
    }


# ---------------------------------------------------------------------------
# Example B: exact composition residue
# ---------------------------------------------------------------------------


def run_composition_residue_example() -> dict[str, Any]:
    p = diagonal([1, 0])
    q = diagonal([0, 1])

    # First arrow creates cut memory; second arrow repairs memory into the
    # recognized channel.  Their composition has a generated recognized seam
    # residue J_delta C_gamma = 1.
    u_gamma = matrix([[1, 0], [1, 1]])
    u_delta = matrix([[1, 1], [0, 1]])
    composed = matmul(u_delta, u_gamma)

    def corners(u: Matrix) -> dict[str, Matrix]:
        return {
            "R": matmul(matmul(p, u), p),
            "J": matmul(matmul(p, u), q),
            "C": matmul(matmul(q, u), p),
            "M": matmul(matmul(q, u), q),
        }

    gamma = corners(u_gamma)
    delta = corners(u_delta)
    total = corners(composed)

    recognized_naive = matmul(delta["R"], gamma["R"])
    recognized_residue = matmul(delta["J"], gamma["C"])
    recognized_exact = add(recognized_naive, recognized_residue)

    memory_naive = matmul(delta["M"], gamma["M"])
    memory_residue = matmul(delta["C"], gamma["J"])
    memory_exact = add(memory_residue, memory_naive)

    return {
        "schema": "rkf.clock_free_composition_residue.v1",
        "clock_used": False,
        "recognized_composition_identity": recognized_exact == total["R"],
        "memory_composition_identity": memory_exact == total["M"],
        "recognized_residue": matrix_record(recognized_residue),
        "recognized_residue_nonzero": not is_zero(recognized_residue),
        "memory_residue": matrix_record(memory_residue),
        "transition_differential_gamma": matrix_record(
            subtract(matmul(p, u_gamma), matmul(u_gamma, p))
        ),
        "transition_differential_delta": matrix_record(
            subtract(matmul(p, u_delta), matmul(u_delta, p))
        ),
    }


# ---------------------------------------------------------------------------
# Example C: stable repair 2 -> 1 -> 2
# ---------------------------------------------------------------------------


def run_stable_repair_example() -> dict[str, Any]:
    u_a = matrix([[2, 0, 0], [0, 1, 1]])
    u_b = matrix([[3, 0], [0, 1], [0, 0]])
    u_ba = matmul(u_b, u_a)

    p_x = diagonal([1, 0, 0])
    p_y = diagonal([1, 0])
    p_z = diagonal([1, 0, 0])
    q_x = subtract(identity(3), p_x)
    q_y = subtract(identity(2), p_y)
    q_z = subtract(identity(3), p_z)

    cut_diff_a = subtract(matmul(p_y, u_a), matmul(u_a, p_x))
    cut_diff_b = subtract(matmul(p_z, u_b), matmul(u_b, p_y))
    cut_diff_ba = subtract(matmul(p_z, u_ba), matmul(u_ba, p_x))

    induced_a = matrix([[1, 1]])
    induced_b = matrix([[1], [0]])
    induced_ba = matmul(induced_b, induced_a)

    def loss_birth(a: Matrix) -> tuple[int, int]:
        rows, cols = shape(a)
        r = rank(a)
        return cols - r, rows - r

    loss_a, birth_a = loss_birth(induced_a)
    loss_b, birth_b = loss_birth(induced_b)
    loss_ba, birth_ba = loss_birth(induced_ba)

    # Clock-free form differential and exact composition chain rule.
    s_x, s_y, s_z = identity(3), identity(2), identity(3)
    delta_a = transition_differential(s_x, s_y, u_a)
    delta_b = transition_differential(s_y, s_z, u_b)
    delta_ba = transition_differential(s_x, s_z, u_ba)
    chain_rhs = add(delta_a, matmul(matmul(transpose(u_a), delta_b), u_a))

    return {
        "schema": "rkf.clock_free_stable_repair.v1",
        "clock_used": False,
        "repair_ranks": {"x": 2, "y": 1, "z": 2},
        "cut_compatible": {
            "a": is_zero(cut_diff_a),
            "b": is_zero(cut_diff_b),
            "ba": is_zero(cut_diff_ba),
        },
        "a": {
            "loss": loss_a,
            "birth": birth_a,
            "repair_index": loss_a - birth_a,
        },
        "b": {
            "loss": loss_b,
            "birth": birth_b,
            "repair_index": loss_b - birth_b,
        },
        "ba": {
            "loss": loss_ba,
            "birth": birth_ba,
            "repair_index": loss_ba - birth_ba,
        },
        "repair_index_additive": (
            loss_ba - birth_ba
            == (loss_a - birth_a) + (loss_b - birth_b)
        ),
        "form_chain_rule_exact": delta_ba == chain_rhs,
        "memory_corner_composes": (
            matmul(matmul(q_z, u_ba), q_x)
            == matmul(
                matmul(matmul(q_z, u_b), q_y),
                matmul(matmul(q_y, u_a), q_x),
            )
        ),
    }


# ---------------------------------------------------------------------------
# Example D: exact five-memory cut packet
# ---------------------------------------------------------------------------


def run_five_memory_example() -> dict[str, Any]:
    amplitudes = (
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(3, 4),
        Fraction(4, 5),
        Fraction(9, 10),
    )
    a = diagonal(amplitudes)
    i5 = identity(5)
    z = vstack(i5, a)
    p = diagonal([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
    q = subtract(identity(10), p)
    target = hstack(zeros(5, 5), identity(5))

    source = matmul(transpose(z), z)
    recognized = matmul(matmul(transpose(z), p), z)
    memory = matmul(matmul(transpose(z), q), z)
    signed = subtract(recognized, memory)

    cut_bridge = matmul(q, z)
    target_visible = matmul(target, cut_bridge)
    reconstructed_bridge = matmul(transpose(target), target_visible)
    b = matmul(target_visible, transpose(target_visible))

    memory_values = tuple(value * value for value in amplitudes)
    gap_values = tuple(Fraction(1) - value for value in memory_values)
    relative_gap = min(gap_values)
    determinant_value = Fraction(1)
    for value in gap_values:
        determinant_value *= value

    threshold_amplitudes = amplitudes[:-1] + (Fraction(1),)
    threshold_b = diagonal(value * value for value in threshold_amplitudes)
    threshold_gap = diagonal(Fraction(1) - value for value in (
        x * x for x in threshold_amplitudes
    ))

    supercritical_b = diagonal(
        [Fraction(4), Fraction(9, 4), Fraction(1, 4), Fraction(4, 9), Fraction(9, 16)]
    )
    supercritical_gap = subtract(identity(5), supercritical_b)
    supercritical_det = determinant(supercritical_gap)
    supercritical_negative_index = sum(
        1 for value in [Fraction(4), Fraction(9, 4), Fraction(1, 4), Fraction(4, 9), Fraction(9, 16)]
        if value > 1
    )

    checks = {
        "source_is_recognized_plus_memory": source == add(recognized, memory),
        "recognized_reference_is_identity": recognized == i5,
        "memory_is_cut_gram": memory == matmul(transpose(cut_bridge), cut_bridge),
        "target_faithfulness": cut_bridge == reconstructed_bridge,
        "finite_seam_matrix_is_cut_derived": b == diagonal(memory_values),
        "full_relative_gap_matches_five_matrix": signed == diagonal(gap_values),
        "subcritical": all(value > 0 for value in gap_values),
        "threshold_kernel_dimension_one": (
            sum(1 for i in range(5) if threshold_gap[i][i] == 0) == 1
        ),
        "positive_determinant_not_sufficient": (
            supercritical_det > 0 and supercritical_negative_index == 2
        ),
    }

    return {
        "schema": "rkf.clock_free_five_memory.v1",
        "clock_used": False,
        "event_lift": matrix_record(z),
        "source": matrix_record(source),
        "recognized_reference": matrix_record(recognized),
        "memory_gram": matrix_record(memory),
        "signed_cut_form": matrix_record(signed),
        "finite_seam_matrix": matrix_record(b),
        "memory_rank": rank(cut_bridge),
        "relative_gap": fraction_text(relative_gap),
        "fredholm_determinant": fraction_text(determinant_value),
        "threshold_kernel_dimension": sum(
            1 for i in range(5) if threshold_gap[i][i] == 0
        ),
        "positive_determinant_negative_control": {
            "determinant": fraction_text(supercritical_det),
            "negative_index": supercritical_negative_index,
        },
        "checks": checks,
    }


def build_stage1_certificate() -> dict[str, Any]:
    holonomy = run_holonomy_example()
    composition = run_composition_residue_example()
    repair = run_stable_repair_example()
    five_memory = run_five_memory_example()

    checks = {
        "holonomy_local_closure": holonomy["all_local_residues_zero"],
        "holonomy_visible_return": holonomy["visible_return"],
        "holonomy_memory_nonzero": holonomy["memory_holonomy"] == 1,
        "composition_recognized_identity": composition[
            "recognized_composition_identity"
        ],
        "composition_memory_identity": composition["memory_composition_identity"],
        "composition_residue_nonzero": composition["recognized_residue_nonzero"],
        "repair_cut_compatible": all(repair["cut_compatible"].values()),
        "repair_index_additive": repair["repair_index_additive"],
        "clock_free_chain_rule": repair["form_chain_rule_exact"],
        "five_memory_all_checks": all(five_memory["checks"].values()),
        "no_external_clock_anywhere": all(
            not packet["clock_used"]
            for packet in (holonomy, composition, repair, five_memory)
        ),
    }

    return {
        "schema": "rkf.clock_free_cut_memory_stage1.v1",
        "status": (
            "PASS_CLOCK_FREE_CUT_MEMORY_GENERAL_EXAMPLE_STAGE1"
            if all(checks.values())
            else "FAIL_CLOCK_FREE_CUT_MEMORY_GENERAL_EXAMPLE_STAGE1"
        ),
        "claim_boundary": {
            "proved_by_exact_examples": [
                "local closure can coexist with global seam memory",
                "composition residues are generated by cut-corner multiplication",
                "stable repair index is clock-free and additive",
                "source/recognized/memory forms are derived from one cut lift",
                "target-faithful five-memory reduction reproduces sign, threshold and relative gap",
                "positive determinant sign alone is not a positivity criterion",
            ],
            "not_claimed": [
                "native completed-Weil event lift",
                "RH target faithfulness",
                "RH numerical certificate",
            ],
        },
        "checks": checks,
        "holonomy": holonomy,
        "composition_residue": composition,
        "stable_repair": repair,
        "five_memory": five_memory,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = build_stage1_certificate()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["status"])
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
