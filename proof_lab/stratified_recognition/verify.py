"""Exact finite calibrations for SR-01 through SR-03."""
from __future__ import annotations

from fractions import Fraction

Matrix = tuple[tuple[Fraction, ...], ...]


def F(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def matrix(rows: list[list[int | Fraction]]) -> Matrix:
    if not rows:
        return tuple()
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have equal width")
    return tuple(tuple(F(v) for v in row) for row in rows)


def rank(A: Matrix) -> int:
    if not A:
        return 0
    work = [list(row) for row in A]
    m = len(work)
    n = len(work[0])
    pivot_row = 0
    for col in range(n):
        pivot = next((r for r in range(pivot_row, m) if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pv = work[pivot_row][col]
        work[pivot_row] = [x / pv for x in work[pivot_row]]
        for r in range(m):
            if r == pivot_row:
                continue
            factor = work[r][col]
            if factor != 0:
                work[r] = [
                    work[r][c] - factor * work[pivot_row][c]
                    for c in range(n)
                ]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row


def stack(A: Matrix, B: Matrix) -> Matrix:
    if not A:
        return B
    if not B:
        return A
    if len(A[0]) != len(B[0]):
        raise ValueError("stacked matrices must have equal column counts")
    return A + B


def faithful(E: Matrix, Pi: Matrix) -> bool:
    """ker(E) subset ker(Pi) iff stacking Pi adds no row rank."""
    return rank(stack(E, Pi)) == rank(E)


def blind_dimension(E: Matrix, Pi: Matrix) -> int:
    return rank(stack(E, Pi)) - rank(E)


def append_observer(E: Matrix, G: Matrix) -> Matrix:
    return stack(E, G)


def identity(n: int) -> Matrix:
    return tuple(
        tuple(F(1 if i == j else 0) for j in range(n))
        for i in range(n)
    )


def truncation_observer(total_dim: int, retained_dim: int) -> Matrix:
    if not (0 <= retained_dim <= total_dim):
        raise ValueError("invalid retained dimension")
    return tuple(
        tuple(F(1 if i == j else 0) for j in range(total_dim))
        for i in range(retained_dim)
    )


def typed_zero(values: tuple[Fraction, ...]) -> bool:
    return all(v == 0 for v in values)


def scalar_sum_zero(values: tuple[Fraction, ...]) -> bool:
    return sum(values, Fraction(0)) == 0


def run_calibration() -> dict[str, object]:
    # SR-01 positive decoder/faithfulness control.
    E_decode = matrix([[1, 0], [0, 1]])
    Pi_decode = matrix([[1, 1]])
    decoder_faithfulness_ok = faithful(E_decode, Pi_decode)

    # SR-01 blindness / exact dimension control.
    E_blind = matrix([[1, 0, 0]])
    Pi_blind = matrix([[0, 1, 0], [0, 0, 1]])
    blind_dimension_ok = (
        not faithful(E_blind, Pi_blind)
        and blind_dimension(E_blind, Pi_blind) == 2
    )

    # SR-02 truncation: omit one target-relevant higher stratum.
    E_trunc = truncation_observer(4, 3)
    Pi_full = identity(4)
    truncation_blind_ok = (
        not faithful(E_trunc, Pi_full)
        and blind_dimension(E_trunc, Pi_full) == 1
    )

    # Exact one-channel repair of that omitted dimension.
    G_last = matrix([[0, 0, 0, 1]])
    truncation_repair_ok = faithful(append_observer(E_trunc, G_last), Pi_full)

    # If the target truly ignores the omitted stratum, truncation is lawful.
    Pi_lower_only = truncation_observer(4, 3)
    target_ignores_omitted_ok = faithful(E_trunc, Pi_lower_only)

    # SR-03 differential-obstruction target.
    D = matrix([[1, -1, 0], [0, 1, -1]])
    E_partial = matrix([[1, 0, 0]])
    differential_blindness_ok = (
        not faithful(E_partial, D)
        and blind_dimension(E_partial, D) == 2
    )

    G_diff = matrix([[0, 1, 0], [0, 0, 1]])
    differential_repair_ok = faithful(append_observer(E_partial, G_diff), D)

    # Explicit blind false-closure witness v=(0,1,0): E v=0 while D v=(-1,1).
    explicit_false_closure_witness_ok = True
    v = (F(0), F(1), F(0))
    e_v = sum(E_partial[0][j] * v[j] for j in range(3))
    d_v = tuple(sum(row[j] * v[j] for j in range(3)) for row in D)
    explicit_false_closure_witness_ok = (e_v == 0 and d_v != (F(0), F(0)))

    # MR-01 typed non-cancellation guard at the integrated layer.
    packet = (F(3), F(-3))
    typed_non_cancellation_ok = (
        scalar_sum_zero(packet)
        and not typed_zero(packet)
    )

    controls = {
        "faithfulness_decoder_rank_control": decoder_faithfulness_ok,
        "blind_dimension_exact": blind_dimension_ok,
        "truncation_blindness_detected": truncation_blind_ok,
        "truncation_minimal_repair": truncation_repair_ok,
        "target_ignores_omitted_is_faithful": target_ignores_omitted_ok,
        "differential_obstruction_blindness": differential_blindness_ok,
        "differential_minimal_repair": differential_repair_ok,
        "explicit_false_closure_witness": explicit_false_closure_witness_ok,
        "typed_scalar_cancellation_rejected": typed_non_cancellation_ok,
    }
    status = all(controls.values())
    return {
        "status": (
            "PASS_STRATIFIED_RECOGNITION_CALIBRATION"
            if status
            else "FAIL_STRATIFIED_RECOGNITION_CALIBRATION"
        ),
        **controls,
    }


if __name__ == "__main__":
    import json

    result = run_calibration()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"].startswith("PASS") else 1)
