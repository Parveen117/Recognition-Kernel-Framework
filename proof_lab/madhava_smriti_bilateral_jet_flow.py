from __future__ import annotations

"""Exact Madhava-Smriti bilateral jet-flow closure certificate.

The packet realizes the Vedic/RSC corrected-recursion grammar on a finite
nilpotent jet flow using only ``fractions.Fraction``. It certifies the algebra
of partial jets, correction windows, signed Smriti, bilateral cut transport,
refinement cocycles, and fail-closed classifications. It does not identify a
specific historical Madhava correction formula or a physical nuclear adapter.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Any, Sequence

Scalar = Fraction
Vector = tuple[Scalar, ...]
Matrix = tuple[tuple[Scalar, ...], ...]


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    out = tuple(tuple(q(x) for x in row) for row in rows)
    if not out:
        return tuple()
    width = len(out[0])
    if width == 0 or any(len(row) != width for row in out):
        raise ValueError("matrix must be nonempty and rectangular")
    return out


def diagonal(values: Sequence[int | Fraction]) -> Matrix:
    vals = tuple(q(x) for x in values)
    return tuple(
        tuple(vals[i] if i == j else Fraction(0) for j in range(len(vals)))
        for i in range(len(vals))
    )


def identity(n: int) -> Matrix:
    return diagonal([1] * n)


def zero(n: int, m: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(m)) for _ in range(n))


def shape(a: Matrix) -> tuple[int, int]:
    return (len(a), len(a[0]) if a else 0)


def add(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise ValueError("matrix shape mismatch")
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def sub(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise ValueError("matrix shape mismatch")
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def scale(c: int | Fraction, a: Matrix) -> Matrix:
    factor = q(c)
    return tuple(tuple(factor * x for x in row) for row in a)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("matrix multiplication shape mismatch")
    return tuple(
        tuple(
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def power(a: Matrix, exponent: int) -> Matrix:
    n, m = shape(a)
    if n != m or exponent < 0:
        raise ValueError("power requires a square matrix and nonnegative exponent")
    out = identity(n)
    for _ in range(exponent):
        out = matmul(out, a)
    return out


def is_zero(a: Matrix) -> bool:
    return all(x == 0 for row in a for x in row)


def matrix_sum(
    items: Sequence[Matrix],
    rows: int | None = None,
    cols: int | None = None,
) -> Matrix:
    if not items:
        if rows is None or cols is None:
            raise ValueError("empty sum requires shape")
        return zero(rows, cols)
    out = zero(*shape(items[0]))
    for item in items:
        out = add(out, item)
    return out


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


def norm_sq(a: Matrix) -> Fraction:
    return sum((x * x for row in a for x in row), Fraction(0))


def nilpotent_exponential(
    g: Matrix,
    t: int | Fraction,
    nilpotency_index: int,
) -> Matrix:
    if not is_zero(power(g, nilpotency_index)):
        raise ValueError("declared nilpotency index does not annihilate generator")
    tau = q(t)
    return matrix_sum(
        [
            scale(tau**k / factorial(k), power(g, k))
            for k in range(nilpotency_index)
        ]
    )


def canonical_fixture() -> tuple[Matrix, Matrix, Matrix]:
    j = diagonal((1, -1, 1, -1, 1))
    g = matrix(
        (
            (0, 1, 0, 0, 0),
            (0, 0, 1, 0, 0),
            (0, 0, 0, 1, 0),
            (0, 0, 0, 0, 1),
            (0, 0, 0, 0, 0),
        )
    )
    observer = matrix(((1, 0, 0, 0, 0),))
    return j, g, observer


def jet_term(
    observer: Matrix,
    g: Matrix,
    t: int | Fraction,
    order: int,
) -> Matrix:
    tau = q(t)
    return scale(
        tau**order / factorial(order),
        matmul(observer, power(g, order)),
    )


def partial_jet(
    observer: Matrix,
    g: Matrix,
    t: int | Fraction,
    order: int,
) -> Matrix:
    return matrix_sum([jet_term(observer, g, t, k) for k in range(order + 1)])


def correction_window(
    observer: Matrix,
    g: Matrix,
    t: int | Fraction,
    base_order: int,
    depth: int,
) -> Matrix:
    if base_order < 0 or depth < 0:
        raise ValueError("orders must be nonnegative")
    rows, _ = shape(observer)
    cols = len(g)
    return matrix_sum(
        [
            jet_term(observer, g, t, k)
            for k in range(base_order + 1, base_order + depth + 1)
        ],
        rows,
        cols,
    )


def recognized_finite_state(
    observer: Matrix,
    g: Matrix,
    t: int | Fraction,
    base_order: int,
    depth: int,
) -> Matrix:
    return add(
        partial_jet(observer, g, t, base_order),
        correction_window(observer, g, t, base_order, depth),
    )


def observed_flow(
    observer: Matrix,
    g: Matrix,
    t: int | Fraction,
    nilpotency_index: int,
) -> Matrix:
    return matmul(observer, nilpotent_exponential(g, t, nilpotency_index))


def signed_smriti(finite_state: Matrix, full_state: Matrix) -> Matrix:
    """Signed Vedic/RSC Smriti: finite state minus recognized limit."""
    return sub(finite_state, full_state)


def tail_smriti(finite_state: Matrix, full_state: Matrix) -> Matrix:
    """Conventional remaining tail, equal to minus signed Smriti."""
    return sub(full_state, finite_state)


def closure_defect(
    finite_state: Matrix,
    full_state: Matrix,
    smriti: Matrix,
) -> Matrix:
    return sub(sub(finite_state, full_state), smriti)


def classify_madhava_smriti(
    *,
    closure_zero: bool,
    bilateral_zero: bool,
    tail_typed: bool,
    tail_zero: bool,
    burden: Fraction | None,
) -> str:
    if not bilateral_zero:
        return "OPEN_BILATERAL_SEAM"
    if not closure_zero:
        return "OPEN_RECOGNITION_RESIDUE"
    if not tail_typed or burden is None:
        return "ABSTAIN_UNTYPED_TAIL"
    if burden > 1:
        return "BURDEN_EXCEEDS_ONE"
    if tail_zero:
        return "EXACT_FINITE_CLOSURE"
    return "MEMORY_CLOSED"


def run_madhava_refinement_fixture() -> dict[str, Any]:
    _, g, observer = canonical_fixture()
    t = Fraction(2, 3)
    full = observed_flow(observer, g, t, 5)
    base_order = 1
    states = [
        recognized_finite_state(observer, g, t, base_order, depth)
        for depth in range(4)
    ]
    signed = [signed_smriti(state, full) for state in states]
    tails = [tail_smriti(state, full) for state in states]
    defects = [
        closure_defect(state, full, memory)
        for state, memory in zip(states, signed)
    ]
    increments = [
        jet_term(observer, g, t, base_order + depth)
        for depth in range(1, 4)
    ]

    checks: dict[str, bool] = {
        "generator_nilpotent_at_five": is_zero(power(g, 5)),
        "intermediate_tail_is_nonzero": not is_zero(tails[0]),
        "final_correction_window_closes_exactly": is_zero(tails[-1]),
        "signed_smriti_is_negative_tail": all(
            signed[i] == scale(-1, tails[i]) for i in range(4)
        ),
        "closure_identity_holds_at_every_depth": all(
            is_zero(defect) for defect in defects
        ),
        "discarding_smriti_opens_residue": not is_zero(sub(states[0], full)),
        "tail_energy_strictly_decreases": all(
            norm_sq(tails[i + 1]) < norm_sq(tails[i]) for i in range(3)
        ),
    }
    for i, increment in enumerate(increments):
        checks[f"finite_state_refinement_{i}"] = (
            sub(states[i + 1], states[i]) == increment
        )
        checks[f"signed_smriti_refinement_{i}"] = (
            sub(signed[i + 1], signed[i]) == increment
        )
        checks[f"tail_transfer_{i}"] = (
            sub(tails[i], tails[i + 1]) == increment
        )

    return {
        "schema": "rkf.madhava_smriti_refinement.v1",
        "time": ftext(t),
        "base_order": base_order,
        "finite_states": [record_matrix(x) for x in states],
        "signed_smriti": [record_matrix(x) for x in signed],
        "tail_smriti": [record_matrix(x) for x in tails],
        "tail_energy": [ftext(norm_sq(x)) for x in tails],
        "checks": checks,
    }


def run_bilateral_smriti_fixture() -> dict[str, Any]:
    j, g, observer = canonical_fixture()
    wrong_cut = identity(5)
    t = Fraction(2, 3)
    base_order = 1
    depth = 1
    plus = recognized_finite_state(observer, g, t, base_order, depth)
    minus = recognized_finite_state(observer, g, -t, base_order, depth)
    full_plus = observed_flow(observer, g, t, 5)
    full_minus = observed_flow(observer, g, -t, 5)
    signed_plus = signed_smriti(plus, full_plus)
    signed_minus = signed_smriti(minus, full_minus)
    tail_plus = tail_smriti(plus, full_plus)
    tail_minus = tail_smriti(minus, full_minus)
    even_tail = scale(Fraction(1, 2), add(tail_plus, tail_minus))
    odd_tail = scale(Fraction(1, 2), sub(tail_plus, tail_minus))
    wrong_defect = sub(matmul(tail_plus, wrong_cut), tail_minus)
    checks = {
        "generator_is_cut_odd": matmul(matmul(j, g), j) == scale(-1, g),
        "observer_is_cut_even": matmul(observer, j) == observer,
        "finite_states_are_bilateral": matmul(plus, j) == minus,
        "signed_smriti_is_bilateral": matmul(signed_plus, j) == signed_minus,
        "tail_smriti_is_bilateral": matmul(tail_plus, j) == tail_minus,
        "even_tail_is_cut_even": matmul(even_tail, j) == even_tail,
        "odd_tail_is_cut_odd": matmul(odd_tail, j) == scale(-1, odd_tail),
        "wrong_cut_negative_control": not is_zero(wrong_defect),
    }
    return {
        "schema": "rkf.madhava_smriti_bilateral.v1",
        "forward_signed_smriti": record_matrix(signed_plus),
        "backward_signed_smriti": record_matrix(signed_minus),
        "forward_tail": record_matrix(tail_plus),
        "backward_tail": record_matrix(tail_minus),
        "even_tail": record_matrix(even_tail),
        "odd_tail": record_matrix(odd_tail),
        "wrong_cut_defect": record_matrix(wrong_defect),
        "checks": checks,
    }


def run_refinement_cocycle_fixture() -> dict[str, Any]:
    _, g, observer = canonical_fixture()
    t = Fraction(3, 5)
    full = observed_flow(observer, g, t, 5)
    states = [
        recognized_finite_state(observer, g, t, 0, depth)
        for depth in range(4)
    ]
    memories = [signed_smriti(state, full) for state in states]

    def seam(a: int, b: int) -> Matrix:
        return sub(
            sub(states[b], states[a]),
            sub(memories[b], memories[a]),
        )

    direct = seam(0, 3)
    composed = add(add(seam(0, 1), seam(1, 2)), seam(2, 3))
    corruption = jet_term(observer, g, t, 4)
    corrupt_memory = add(memories[2], corruption)
    corrupt_seam = sub(
        sub(states[2], states[1]),
        sub(corrupt_memory, memories[1]),
    )
    checks = {
        "each_refinement_seam_closes": all(
            is_zero(seam(i, i + 1)) for i in range(3)
        ),
        "direct_refinement_closes": is_zero(direct),
        "composition_cocycle_is_exact": direct == composed,
        "uncoupled_memory_update_is_detected": not is_zero(corrupt_seam),
    }
    return {
        "schema": "rkf.madhava_smriti_refinement_cocycle.v1",
        "direct_seam": record_matrix(direct),
        "composed_seam": record_matrix(composed),
        "corrupt_seam": record_matrix(corrupt_seam),
        "checks": checks,
    }


def run_correction_smriti_gauge_fixture() -> dict[str, Any]:
    _, g, observer = canonical_fixture()
    t = Fraction(1, 2)
    full = observed_flow(observer, g, t, 5)
    finite = recognized_finite_state(observer, g, t, 1, 1)
    memory = signed_smriti(finite, full)
    gauge = matrix(((Fraction(1, 7), 0, 0, 0, Fraction(-2, 9)),))
    shifted_finite = add(finite, gauge)
    shifted_memory = add(memory, gauge)
    coupled_defect = closure_defect(shifted_finite, full, shifted_memory)
    uncoupled_defect = closure_defect(shifted_finite, full, memory)
    checks = {
        "original_closure": is_zero(closure_defect(finite, full, memory)),
        "coupled_correction_smriti_shift_preserves_closure": is_zero(
            coupled_defect
        ),
        "uncoupled_correction_shift_opens_exact_gauge_defect": (
            uncoupled_defect == gauge
        ),
    }
    return {
        "schema": "rkf.madhava_smriti_gauge.v1",
        "gauge": record_matrix(gauge),
        "coupled_defect": record_matrix(coupled_defect),
        "uncoupled_defect": record_matrix(uncoupled_defect),
        "checks": checks,
    }


def run_fail_closed_fixture() -> dict[str, Any]:
    checks = {
        "memory_closed": classify_madhava_smriti(
            closure_zero=True,
            bilateral_zero=True,
            tail_typed=True,
            tail_zero=False,
            burden=Fraction(1, 4),
        )
        == "MEMORY_CLOSED",
        "exact_finite_closure": classify_madhava_smriti(
            closure_zero=True,
            bilateral_zero=True,
            tail_typed=True,
            tail_zero=True,
            burden=Fraction(1, 4),
        )
        == "EXACT_FINITE_CLOSURE",
        "open_residue_precedes_prediction": classify_madhava_smriti(
            closure_zero=False,
            bilateral_zero=True,
            tail_typed=True,
            tail_zero=False,
            burden=Fraction(1, 4),
        )
        == "OPEN_RECOGNITION_RESIDUE",
        "open_bilateral_precedes_prediction": classify_madhava_smriti(
            closure_zero=True,
            bilateral_zero=False,
            tail_typed=True,
            tail_zero=False,
            burden=Fraction(1, 4),
        )
        == "OPEN_BILATERAL_SEAM",
        "untyped_tail_abstains": classify_madhava_smriti(
            closure_zero=True,
            bilateral_zero=True,
            tail_typed=False,
            tail_zero=False,
            burden=Fraction(1, 4),
        )
        == "ABSTAIN_UNTYPED_TAIL",
        "excess_burden_rejected": classify_madhava_smriti(
            closure_zero=True,
            bilateral_zero=True,
            tail_typed=True,
            tail_zero=False,
            burden=Fraction(5, 4),
        )
        == "BURDEN_EXCEEDS_ONE",
    }
    return {
        "schema": "rkf.madhava_smriti_fail_closed.v1",
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "refinement": run_madhava_refinement_fixture(),
        "bilateral": run_bilateral_smriti_fixture(),
        "cocycle": run_refinement_cocycle_fixture(),
        "gauge": run_correction_smriti_gauge_fixture(),
        "fail_closed": run_fail_closed_fixture(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    status = (
        "PASS_MADHAVA_SMRITI_BILATERAL_JET_FLOW_CLOSURE_CANDIDATE"
        if all(checks.values())
        else "FAIL_MADHAVA_SMRITI_BILATERAL_JET_FLOW_CLOSURE_CANDIDATE"
    )
    return {
        "schema": "rkf.madhava_smriti_bilateral_jet_flow_closure_candidate.v1",
        "source_lineage": {
            "repository": "Parveen117/Vedic",
            "master_spine_commit": (
                "0e9b480ece2f5696a2438199edc689b793f6915a"
            ),
            "vrg_commit": "e7ec7ded5838cddeb9cdef4d235824dfd7cf530f",
            "consumed_grammar": (
                "recognized finite recursion plus correction minus recognized "
                "limit minus signed Smriti equals zero"
            ),
        },
        "status": status,
        "claim_boundary": {
            "certified": [
                "finite corrected jet plus signed Smriti closure",
                "exact correction-to-tail refinement transfer",
                "strict tail-energy descent in the canonical rational fixture",
                "bilateral cut transport of signed and conventional Smriti tails",
                "even/odd tail parity",
                "refinement seam cocycle",
                "coupled correction-Smriti gauge invariance",
                "fail-closed residue, bilateral, tail-typing and burden states",
            ],
            "not_certified": [
                "historical identity with one specific Madhava correction formula",
                "unbounded-generator domain closure",
                "convergence beyond the stated bounded-flow hypotheses",
                "physical identification of Smriti with nuclear shell or deformation memory",
                "improved atomic prediction",
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
    for name, passed in payload["checks"].items():
        print(name.upper(), passed)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
