from __future__ import annotations

"""Exact bilateral jet-flow capstone calibration.

This module joins the certified cut-graded generator with the typed
lambda-Jacobian tower through a finite, exact recognition-flow packet. It uses
only :class:`fractions.Fraction`; no floating point, fitted basis, eigensolver,
or physical constitutive law is imported.

The certificate proves a finite-dimensional shadow of the capstone theorem. It
is deliberately fail-closed about unbounded domains and physical adapters.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Any, Sequence

from proof_lab.cut_graded_universal_generator import (
    Matrix,
    add,
    commutator,
    cut_decomposition,
    cut_loop_series,
    diagonal,
    ftext,
    identity,
    is_zero,
    log_series_first_two,
    matmul,
    matrix,
    power,
    record_matrix,
    scale,
    shape,
    sub,
    zero,
)

Scalar = Fraction
Vector = tuple[Scalar, ...]


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def stack(blocks: Sequence[Matrix]) -> Matrix:
    if not blocks:
        raise ValueError("at least one block is required")
    width = len(blocks[0][0])
    if any(not block or any(len(row) != width for row in block) for block in blocks):
        raise ValueError("all blocks must be nonempty and have one common width")
    return tuple(row for block in blocks for row in block)


def matrix_sum(blocks: Sequence[Matrix]) -> Matrix:
    if not blocks:
        raise ValueError("at least one matrix is required")
    out = zero(*shape(blocks[0]))
    for block in blocks:
        out = add(out, block)
    return out


def nilpotent_exponential(g: Matrix, t: int | Fraction, nilpotency_index: int) -> Matrix:
    """Return ``exp(tG)`` exactly when ``G**nilpotency_index == 0``."""
    n, m = shape(g)
    if n != m:
        raise ValueError("generator must be square")
    if nilpotency_index < 1 or not is_zero(power(g, nilpotency_index)):
        raise ValueError("declared nilpotency index does not annihilate the generator")
    tau = q(t)
    terms = [
        scale(tau**k / factorial(k), power(g, k))
        for k in range(nilpotency_index)
    ]
    return matrix_sum(terms)


def jet_layers(observer: Matrix, g: Matrix, order: int) -> tuple[Matrix, ...]:
    if order < 0:
        raise ValueError("order must be nonnegative")
    if not observer or len(observer[0]) != len(g):
        raise ValueError("observer/generator shape mismatch")
    return tuple(matmul(observer, power(g, k)) for k in range(order + 1))


def finite_jet_observer(observer: Matrix, g: Matrix, order: int) -> Matrix:
    return stack(jet_layers(observer, g, order))


def jet_reconstruction(observer: Matrix, g: Matrix, t: int | Fraction, order: int) -> Matrix:
    tau = q(t)
    return matrix_sum(
        [
            scale(tau**k / factorial(k), layer)
            for k, layer in enumerate(jet_layers(observer, g, order))
        ]
    )


def observed_flow(observer: Matrix, flow: Matrix) -> Matrix:
    return matmul(observer, flow)


def rank_fraction(a: Matrix) -> int:
    if not a:
        return 0
    rows = [list(row) for row in a]
    n_rows = len(rows)
    n_cols = len(rows[0])
    rank = 0
    for c in range(n_cols):
        pivot = next((r for r in range(rank, n_rows) if rows[r][c] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][c]
        rows[rank] = [x / pivot_value for x in rows[rank]]
        for r in range(n_rows):
            if r != rank and rows[r][c] != 0:
                factor = rows[r][c]
                rows[r] = [
                    rows[r][j] - factor * rows[rank][j]
                    for j in range(n_cols)
                ]
        rank += 1
        if rank == n_rows:
            break
    return rank


def kernel_basis(a: Matrix) -> tuple[Vector, ...]:
    if not a:
        return tuple()
    rows = [list(row) for row in a]
    n_rows = len(rows)
    n_cols = len(rows[0])
    pivot_cols: list[int] = []
    r = 0
    for c in range(n_cols):
        pivot = next((i for i in range(r, n_rows) if rows[i][c] != 0), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pivot_value = rows[r][c]
        rows[r] = [x / pivot_value for x in rows[r]]
        for i in range(n_rows):
            if i != r and rows[i][c] != 0:
                factor = rows[i][c]
                rows[i] = [
                    rows[i][j] - factor * rows[r][j]
                    for j in range(n_cols)
                ]
        pivot_cols.append(c)
        r += 1
        if r == n_rows:
            break
    free_cols = [c for c in range(n_cols) if c not in pivot_cols]
    basis: list[Vector] = []
    for free in free_cols:
        v = [Fraction(0) for _ in range(n_cols)]
        v[free] = Fraction(1)
        for row_index, pivot_col in enumerate(pivot_cols):
            v[pivot_col] = -rows[row_index][free]
        basis.append(tuple(v))
    return tuple(basis)


def row_dot(row: Vector, vector: Vector) -> Fraction:
    if len(row) != len(vector):
        raise ValueError("shape mismatch")
    return sum(
        (row[i] * vector[i] for i in range(len(row))),
        Fraction(0),
    )


def target_is_blind(observer: Matrix, target: Vector) -> bool:
    return any(
        row_dot(target, hidden) != 0
        for hidden in kernel_basis(observer)
    )


def classify_capstone(
    *,
    closure_defect_zero: bool,
    target_blind: bool,
    repaired_by_higher_layer: bool,
    burden: Fraction | None,
) -> str:
    """Fail-closed theorem-level classification."""
    if not closure_defect_zero:
        return "OPEN_SEAM"
    if target_blind and not repaired_by_higher_layer:
        return "ABSTAIN"
    if burden is None:
        return "ABSTAIN"
    if burden > 1:
        return "BURDEN_EXCEEDS_ONE"
    if repaired_by_higher_layer:
        return "HIGHER_LAYER_REPAIR"
    return "CLOSED"


def canonical_fixture() -> tuple[Matrix, Matrix, Matrix]:
    j = diagonal((1, -1, 1, -1))
    g = matrix(
        (
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
            (0, 0, 0, 0),
        )
    )
    observer = matrix(((1, 0, 0, 0),))
    return j, g, observer


def run_bilateral_flow_fixture() -> dict[str, Any]:
    j, g, observer = canonical_fixture()
    t = Fraction(2, 3)
    u_plus = nilpotent_exponential(g, t, 4)
    u_minus = nilpotent_exponential(g, -t, 4)
    join = add(u_plus, u_minus)
    cut = sub(u_plus, u_minus)
    closure_defect = sub(matmul(matmul(j, u_plus), j), u_minus)
    observed_closure_defect = sub(
        matmul(matmul(matmul(observer, j), u_plus), j),
        observed_flow(observer, u_minus),
    )
    wrong_cut = diagonal((1, 1, -1, -1))
    wrong_defect = sub(
        matmul(matmul(wrong_cut, u_plus), wrong_cut),
        u_minus,
    )
    checks = {
        "generator_is_cut_odd": matmul(matmul(j, g), j) == scale(-1, g),
        "bilateral_cut_conjugacy": is_zero(closure_defect),
        "observer_bilateral_conjugacy": is_zero(observed_closure_defect),
        "flow_inverse_exact": matmul(u_plus, u_minus) == identity(4),
        "exponential_cut_square": (
            sub(matmul(join, join), matmul(cut, cut))
            == scale(4, identity(4))
        ),
        "derived_channels_commute": matmul(join, cut) == matmul(cut, join),
        "wrong_cut_negative_control_nonzero": not is_zero(wrong_defect),
    }
    return {
        "schema": "rkf.bilateral_cut_flow.v1",
        "time": ftext(t),
        "cut": record_matrix(j),
        "generator": record_matrix(g),
        "u_plus": record_matrix(u_plus),
        "u_minus": record_matrix(u_minus),
        "join_channel": record_matrix(join),
        "cut_channel": record_matrix(cut),
        "helix_closure_defect": record_matrix(closure_defect),
        "wrong_cut_defect": record_matrix(wrong_defect),
        "checks": checks,
    }


def run_jet_reconstruction_fixture() -> dict[str, Any]:
    j, g, observer = canonical_fixture()
    t = Fraction(2, 3)
    u_plus = nilpotent_exponential(g, t, 4)
    u_minus = nilpotent_exponential(g, -t, 4)
    layers = jet_layers(observer, g, 3)
    reconstruction = jet_reconstruction(observer, g, t, 3)
    truncated = jet_reconstruction(observer, g, t, 2)
    exact_observed = observed_flow(observer, u_plus)
    lower_remainder = sub(exact_observed, truncated)
    full_remainder = sub(exact_observed, reconstruction)
    forward = observed_flow(observer, u_plus)
    backward = observed_flow(observer, u_minus)
    even_strand = scale(Fraction(1, 2), add(forward, backward))
    odd_strand = scale(Fraction(1, 2), sub(forward, backward))
    even_series = matrix_sum(
        [scale(t**k / factorial(k), layers[k]) for k in (0, 2)]
    )
    odd_series = matrix_sum(
        [scale(t**k / factorial(k), layers[k]) for k in (1, 3)]
    )
    parity_checks = {
        f"layer_{k}_cut_parity": (
            matmul(layer, j) == scale((-1) ** k, layer)
        )
        for k, layer in enumerate(layers)
    }
    checks = {
        **parity_checks,
        "full_nilpotent_jet_reconstructs_observed_flow": (
            reconstruction == exact_observed
        ),
        "third_order_full_remainder_zero": is_zero(full_remainder),
        "second_order_remainder_nonzero": not is_zero(lower_remainder),
        "even_bilateral_strand_equals_even_jet": even_strand == even_series,
        "odd_bilateral_strand_equals_odd_jet": odd_strand == odd_series,
        "bilateral_strands_reconstruct_forward": (
            add(even_strand, odd_strand) == forward
        ),
        "bilateral_strands_reconstruct_backward": (
            sub(even_strand, odd_strand) == backward
        ),
    }
    return {
        "schema": "rkf.bilateral_jet_reconstruction.v1",
        "jet_layers": [record_matrix(layer) for layer in layers],
        "forward_observed_strand": record_matrix(forward),
        "backward_observed_strand": record_matrix(backward),
        "even_strand": record_matrix(even_strand),
        "odd_strand": record_matrix(odd_strand),
        "second_order_remainder": record_matrix(lower_remainder),
        "third_order_remainder": record_matrix(full_remainder),
        "checks": checks,
    }


def run_recognition_repair_fixture() -> dict[str, Any]:
    _, g, observer = canonical_fixture()
    observers = [finite_jet_observer(observer, g, n) for n in range(4)]
    kernels = [kernel_basis(a) for a in observers]
    ranks = [rank_fraction(a) for a in observers]
    target: Vector = (0, 0, 0, Fraction(1, 2))
    blind = [target_is_blind(a, target) for a in observers]
    burden = row_dot(target, target)
    classification = classify_capstone(
        closure_defect_zero=True,
        target_blind=blind[0],
        repaired_by_higher_layer=blind[0] and not blind[3],
        burden=burden,
    )
    checks = {
        "observer_ranks_increase_one_by_one": ranks == [1, 2, 3, 4],
        "kernel_dimensions_decrease_one_by_one": (
            [len(k) for k in kernels] == [3, 2, 1, 0]
        ),
        "target_blind_through_second_order": blind[:3] == [True, True, True],
        "third_order_repairs_target": blind[3] is False,
        "full_jet_observer_is_identity": observers[3] == identity(4),
        "minimum_decoder_burden_one_quarter": burden == Fraction(1, 4),
        "recognition_reserve_three_quarters": 1 - burden == Fraction(3, 4),
        "classification_is_higher_layer_repair": (
            classification == "HIGHER_LAYER_REPAIR"
        ),
    }
    return {
        "schema": "rkf.jet_flow_recognition_repair.v1",
        "observers": [record_matrix(a) for a in observers],
        "kernel_bases": [
            [[ftext(x) for x in v] for v in basis]
            for basis in kernels
        ],
        "ranks": ranks,
        "target": [ftext(x) for x in target],
        "target_blind_by_order": blind,
        "burden": ftext(burden),
        "reserve": ftext(1 - burden),
        "classification": classification,
        "checks": checks,
    }


def run_curvature_response_fixture() -> dict[str, Any]:
    j, g_odd, observer = canonical_fixture()
    g_even = diagonal((1, 2, -1, 0))
    g = add(g_even, g_odd)
    recovered_even, recovered_odd = cut_decomposition(g, j)
    loop = cut_loop_series(g, j, order=2)
    log_linear, log_quadratic = log_series_first_two(loop)
    curvature = commutator(g_even, g_odd)
    observed_curvature = matmul(observer, curvature)
    observed_log_quadratic = matmul(observer, log_quadratic)
    checks = {
        "declared_even_component_recovered": recovered_even == g_even,
        "declared_odd_component_recovered": recovered_odd == g_odd,
        "cut_loop_linear_memory_is_twice_even_generator": (
            log_linear == scale(2, g_even)
        ),
        "cut_loop_quadratic_is_seam_curvature": log_quadratic == curvature,
        "observer_consumes_same_seam_curvature": (
            observed_log_quadratic == observed_curvature
        ),
        "observed_seam_curvature_nonzero": not is_zero(observed_curvature),
    }
    return {
        "schema": "rkf.jet_flow_curvature_adapter.v1",
        "generator_even": record_matrix(g_even),
        "generator_odd": record_matrix(g_odd),
        "seam_curvature": record_matrix(curvature),
        "observed_seam_curvature": record_matrix(observed_curvature),
        "checks": checks,
    }


def run_fail_closed_fixture() -> dict[str, Any]:
    open_seam = classify_capstone(
        closure_defect_zero=False,
        target_blind=False,
        repaired_by_higher_layer=False,
        burden=Fraction(1, 4),
    )
    abstain = classify_capstone(
        closure_defect_zero=True,
        target_blind=True,
        repaired_by_higher_layer=False,
        burden=None,
    )
    excessive = classify_capstone(
        closure_defect_zero=True,
        target_blind=False,
        repaired_by_higher_layer=False,
        burden=Fraction(4, 1),
    )
    closed = classify_capstone(
        closure_defect_zero=True,
        target_blind=False,
        repaired_by_higher_layer=False,
        burden=Fraction(1, 4),
    )
    checks = {
        "nonzero_closure_defect_opens_seam": open_seam == "OPEN_SEAM",
        "unrepaired_blind_target_abstains": abstain == "ABSTAIN",
        "burden_above_one_is_rejected": excessive == "BURDEN_EXCEEDS_ONE",
        "visible_low_burden_target_closes": closed == "CLOSED",
    }
    return {
        "schema": "rkf.jet_flow_fail_closed_classification.v1",
        "classifications": {
            "open_seam": open_seam,
            "unrepaired_blind": abstain,
            "excessive_burden": excessive,
            "closed": closed,
        },
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "bilateral_flow": run_bilateral_flow_fixture(),
        "jet_reconstruction": run_jet_reconstruction_fixture(),
        "recognition_repair": run_recognition_repair_fixture(),
        "curvature_response": run_curvature_response_fixture(),
        "fail_closed": run_fail_closed_fixture(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    status = (
        "PASS_BILATERAL_JET_FLOW_CAPSTONE_CANDIDATE"
        if all(checks.values())
        else "FAIL_BILATERAL_JET_FLOW_CAPSTONE_CANDIDATE"
    )
    return {
        "schema": "rkf.bilateral_jet_flow_capstone_candidate.v1",
        "source_pin": {
            "repository": "Parveen117/Recognition-Kernel-Framework",
            "parent_branch": "agent/cut-graded-lambda-jacobian-tower",
            "parent_commit": "9f5792ee62ce3a1a71d9ed242ff9cb10e6745f3e",
            "consumed_theorems": [
                "theorum/41_cut_graded_universal_generator_theorem.md",
                "theorum/42_cut_graded_lambda_jacobian_tower_theorem.md",
            ],
        },
        "status": status,
        "proved_by_exact_finite_certificate": [
            "cut-odd bilateral Euler/recognition flow conjugacy",
            "exponential cut-square and commuting derived channels",
            "alternating cut parity of successive observer jets",
            "exact nilpotent finite-jet reconstruction with explicit lower-order remainder",
            "bilateral even/odd strand reconstruction",
            "strict monotone reduction of recognition blindness by higher jet layers",
            "third-order repair of a target blind to lower layers",
            "minimum decoder burden and reserve on the repaired target",
            "observer consumption of the cut-loop seam-curvature coefficient",
            "fail-closed CLOSED, HIGHER_LAYER_REPAIR, OPEN_SEAM, BURDEN_EXCEEDS_ONE, and ABSTAIN classes",
        ],
        "claim_boundary": {
            "analytic_extension_requires": [
                "bounded generator or one pinned common invariant core",
                "cut-invariant generator domain",
                "convergent functional calculus or controlled semigroup",
                "bounded observer and target maps on the declared domain",
                "a proved remainder topology for non-nilpotent infinite jets",
            ],
            "not_claimed": [
                "a physical nuclear cut has already been identified",
                "the repository already contains a proved Madhava-named operator",
                "the bilateral strands are already a physical double helix",
                "an unbounded universal generator theorem is closed without domain pins",
                "higher jet order must improve every physical prediction",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


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
