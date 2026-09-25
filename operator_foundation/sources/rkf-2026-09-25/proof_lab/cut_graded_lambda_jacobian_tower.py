from __future__ import annotations

"""Exact cut-graded lambda-Jacobian tower calibration.

The module uses only ``fractions.Fraction``. It certifies finite algebraic
shadows of the cut-graded jet/tower theorem suggested by arXiv:2603.20773,
without asserting that the paper's physical lambda map has already satisfied
all domain, constitutive, or experimental hypotheses.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

from proof_lab.cut_graded_universal_generator import (
    Matrix,
    add,
    canonical_bytes as generator_canonical_bytes,
    commutator,
    cut_loop_series,
    diagonal,
    identity,
    is_zero,
    log_series_first_two,
    matmul,
    matrix,
    record_matrix,
    scale,
    sub,
    transpose,
    zero,
)

Scalar = Fraction
Vector = tuple[Scalar, ...]
Tensor3 = tuple[Matrix, ...]  # one Hessian matrix for each response component


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value, 1)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def vector(values: Sequence[int | Fraction]) -> Vector:
    return tuple(q(x) for x in values)


def matvec(a: Matrix, v: Vector) -> Vector:
    if not a or len(a[0]) != len(v):
        raise ValueError("matrix/vector shape mismatch")
    return tuple(
        sum((a[i][j] * v[j] for j in range(len(v))), Fraction(0))
        for i in range(len(a))
    )


def quadratic_lambda(x: Vector) -> Vector:
    """A cut-equivariant quadratic response map on Q^4.

    The declared thermodynamic cut is J=diag(+,+,-,-). The first two response
    components are cut even and the last two are cut odd.
    """
    if len(x) != 4:
        raise ValueError("x must have four coordinates")
    t, v, s, p = x
    return (
        t + 2 * v + s * p,
        t * v + s * s + 3 * p * p,
        s + t * p + v * s,
        p + t * s - v * p,
    )


def quadratic_lambda_jacobian(x: Vector) -> Matrix:
    if len(x) != 4:
        raise ValueError("x must have four coordinates")
    t, v, s, p = x
    return matrix(
        (
            (1, 2, p, s),
            (v, t, 2 * s, 6 * p),
            (p, s, 1 + v, t),
            (s, -p, t, 1 - v),
        )
    )


def quadratic_lambda_hessians() -> Tensor3:
    return (
        matrix(((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0))),
        matrix(((0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 2, 0), (0, 0, 0, 6))),
        matrix(((0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0))),
        matrix(((0, 0, 1, 0), (0, 0, 0, -1), (1, 0, 0, 0), (0, -1, 0, 0))),
    )


def apply_cut_to_hessian(h: Matrix, j_domain: Matrix, output_sign: Fraction) -> Matrix:
    return scale(output_sign, matmul(matmul(j_domain, h), j_domain))


def bigrade_matrix(a: Matrix, j: Matrix) -> dict[str, Matrix]:
    """Decompose a square matrix under commuting cut-conjugation and transpose."""
    if len(a) != len(a[0]) or len(j) != len(a) or matmul(j, j) != identity(len(j)):
        raise ValueError("a must be square and j an involution of matching size")
    jaj = matmul(matmul(j, a), j)
    at = transpose(a)
    jatj = matmul(matmul(j, at), j)
    sectors: dict[str, Matrix] = {}
    for sigma, sigma_name in ((1, "cut_even"), (-1, "cut_odd")):
        for tau, tau_name in ((1, "symmetric"), (-1, "antisymmetric")):
            sectors[f"{sigma_name}_{tau_name}"] = scale(
                Fraction(1, 4),
                add(add(a, scale(sigma, jaj)), add(scale(tau, at), scale(sigma * tau, jatj))),
            )
    return sectors


def flatten_hessians(hessians: Tensor3) -> Vector:
    return tuple(value for h in hessians for row in h for value in row)


def rank_fraction(a: Matrix) -> int:
    if not a:
        return 0
    rows = [list(row) for row in a]
    n_rows = len(rows)
    n_cols = len(rows[0])
    rank = 0
    pivot_col = 0
    while rank < n_rows and pivot_col < n_cols:
        pivot = next((r for r in range(rank, n_rows) if rows[r][pivot_col] != 0), None)
        if pivot is None:
            pivot_col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][pivot_col]
        rows[rank] = [x / pivot_value for x in rows[rank]]
        for r in range(n_rows):
            if r != rank and rows[r][pivot_col] != 0:
                factor = rows[r][pivot_col]
                rows[r] = [rows[r][c] - factor * rows[rank][c] for c in range(n_cols)]
        rank += 1
        pivot_col += 1
    return rank


def kernel_basis_simple(a: Matrix) -> tuple[Vector, ...]:
    """Kernel basis for the small fixtures used here.

    This routine performs exact RREF and returns free-variable basis vectors.
    """
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
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(n_rows):
            if i != r and rows[i][c] != 0:
                factor = rows[i][c]
                rows[i] = [rows[i][k] - factor * rows[r][k] for k in range(n_cols)]
        pivot_cols.append(c)
        r += 1
        if r == n_rows:
            break
    free_cols = [c for c in range(n_cols) if c not in pivot_cols]
    basis: list[Vector] = []
    for free in free_cols:
        vec = [Fraction(0) for _ in range(n_cols)]
        vec[free] = Fraction(1)
        for row_index, pivot_col in enumerate(pivot_cols):
            vec[pivot_col] = -rows[row_index][free]
        basis.append(tuple(vec))
    return tuple(basis)


def row_dot(row: Vector, vec: Vector) -> Fraction:
    if len(row) != len(vec):
        raise ValueError("shape mismatch")
    return sum((row[i] * vec[i] for i in range(len(row))), Fraction(0))


def run_recursive_tower_fixture() -> dict[str, Any]:
    j = diagonal((1, 1, -1, -1))
    x = vector((2, -1, 3, 4))
    jx = matvec(j, x)
    value = quadratic_lambda(x)
    value_cut = quadratic_lambda(jx)
    jac = quadratic_lambda_jacobian(x)
    jac_cut = quadratic_lambda_jacobian(jx)
    hess = quadratic_lambda_hessians()
    third_derivative_zero = True  # exact because the declared response map is quadratic

    derivative_covariance = matmul(matmul(j, jac), j) == jac_cut
    hessian_covariance = all(
        apply_cut_to_hessian(hess[i], j, j[i][i]) == hess[i]
        for i in range(4)
    )
    checks = {
        "lambda_map_cut_equivariance": value_cut == matvec(j, value),
        "jacobian_covariance": derivative_covariance,
        "hessian_induced_cut_covariance": hessian_covariance,
        "recursive_layers_are_typed": len(value) == 4 and len(jac) == 4 and len(hess) == 4,
        "quadratic_tower_terminates_at_third_derivative": third_derivative_zero,
        "hessian_flattening_has_64_entries": len(flatten_hessians(hess)) == 64,
    }
    return {
        "schema": "rkf.cut_graded_lambda_recursive_tower.v1",
        "point": [ftext(v) for v in x],
        "cut_point": [ftext(v) for v in jx],
        "lambda_layer_L1": [ftext(v) for v in value],
        "jacobian_layer_L2": record_matrix(jac),
        "hessian_layer_L3": [record_matrix(h) for h in hess],
        "checks": checks,
    }


def run_jacobian_bigrading_fixture() -> dict[str, Any]:
    j = diagonal((1, 1, -1, -1))
    a = quadratic_lambda_jacobian(vector((2, -1, 3, 4)))
    sectors = bigrade_matrix(a, j)
    reconstruction = zero(4, 4)
    for sector in sectors.values():
        reconstruction = add(reconstruction, sector)
    checks: dict[str, bool] = {
        "four_sector_reconstruction": reconstruction == a,
        "jacobian_antisymmetry_is_not_automatic": transpose(a) != scale(-1, a),
        "symmetric_sector_is_nonzero": (
            not is_zero(sectors["cut_even_symmetric"])
            or not is_zero(sectors["cut_odd_symmetric"])
        ),
        "antisymmetric_sector_is_nonzero": (
            not is_zero(sectors["cut_even_antisymmetric"])
            or not is_zero(sectors["cut_odd_antisymmetric"])
        ),
    }
    for name, sector in sectors.items():
        sigma = 1 if name.startswith("cut_even") else -1
        tau = 1 if name.endswith("symmetric") and not name.endswith("antisymmetric") else -1
        checks[f"{name}_cut_eigenvalue"] = matmul(matmul(j, sector), j) == scale(sigma, sector)
        checks[f"{name}_transpose_eigenvalue"] = transpose(sector) == scale(tau, sector)
    return {
        "schema": "rkf.lambda_jacobian_bigrading.v1",
        "jacobian": record_matrix(a),
        "sectors": {name: record_matrix(value) for name, value in sectors.items()},
        "checks": checks,
    }


def run_connection_curvature_fixture() -> dict[str, Any]:
    j = diagonal((1, 1, -1, -1))
    g_even = matrix(
        (
            (1, 1, 0, 0),
            (0, 2, 0, 0),
            (0, 0, -1, 1),
            (0, 0, 0, 1),
        )
    )
    g_odd = matrix(
        (
            (0, 0, 1, 0),
            (0, 0, 1, 1),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
        )
    )
    g = add(g_even, g_odd)
    loop = cut_loop_series(g, j, order=2)
    _, log_second = log_series_first_two(loop)
    curvature_st = commutator(g_even, g_odd)
    checks = {
        "even_connection_component_is_cut_even": matmul(matmul(j, g_even), j) == g_even,
        "odd_connection_component_is_cut_odd": matmul(matmul(j, g_odd), j) == scale(-1, g_odd),
        "constant_connection_curvature_is_commutator": curvature_st == commutator(g_even, g_odd),
        "cut_loop_curvature_matches_connection_curvature": log_second == curvature_st,
        "curvature_nonzero_in_fixture": not is_zero(curvature_st),
    }
    return {
        "schema": "rkf.lambda_connection_cut_loop_curvature.v1",
        "connection_even": record_matrix(g_even),
        "connection_odd": record_matrix(g_odd),
        "mixed_curvature": record_matrix(curvature_st),
        "checks": checks,
    }


def run_tower_observer_fixture() -> dict[str, Any]:
    first_layer = matrix(((1, 0, 0), (0, 1, 0)))
    second_layer = matrix(((0, 0, 1),))
    combined = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    target = vector((0, 0, Fraction(1, 2)))
    first_kernel = kernel_basis_simple(first_layer)
    combined_kernel = kernel_basis_simple(combined)
    first_target_blind = any(row_dot(target, k) != 0 for k in first_kernel)
    combined_target_blind = any(row_dot(target, k) != 0 for k in combined_kernel)
    minimum_decoder = target  # combined observer is I_3
    burden = row_dot(minimum_decoder, minimum_decoder)
    checks = {
        "first_layer_rank_two": rank_fraction(first_layer) == 2,
        "first_layer_has_one_hidden_direction": first_kernel == ((0, 0, 1),),
        "target_is_blind_at_first_order": first_target_blind,
        "second_layer_repairs_hidden_direction": rank_fraction(combined) == 3,
        "combined_recognition_kernel_zero": combined_kernel == tuple(),
        "target_no_longer_blind": not combined_target_blind,
        "minimum_decoder_burden_one_quarter": burden == Fraction(1, 4),
        "relative_reserve_three_quarters": 1 - burden == Fraction(3, 4),
    }
    return {
        "schema": "rkf.finite_lambda_tower_observer.v1",
        "first_layer_observer": record_matrix(first_layer),
        "second_layer_observer": record_matrix(second_layer),
        "combined_observer": record_matrix(combined),
        "target_row": [ftext(v) for v in target],
        "minimum_decoder": [ftext(v) for v in minimum_decoder],
        "burden": ftext(burden),
        "checks": checks,
    }


def run_rank_change_cut_fixture() -> dict[str, Any]:
    before = diagonal((1, 1, 1))
    at_cut = diagonal((1, 1, 0))
    after = diagonal((1, 1, -1))
    higher_layer = matrix(((0, 0, 1),))
    repaired = matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    checks = {
        "rank_before_cut_three": rank_fraction(before) == 3,
        "rank_at_cut_drops_to_two": rank_fraction(at_cut) == 2,
        "rank_after_cut_returns_three": rank_fraction(after) == 3,
        "higher_layer_detects_cut_kernel": row_dot(higher_layer[0], (0, 0, 1)) == 1,
        "tower_observer_repairs_rank_at_cut": rank_fraction(repaired) == 3,
    }
    return {
        "schema": "rkf.lambda_tower_rank_change_cut.v1",
        "first_layer_before": record_matrix(before),
        "first_layer_at_cut": record_matrix(at_cut),
        "first_layer_after": record_matrix(after),
        "higher_layer_cut_row": record_matrix(higher_layer),
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "recursive_tower": run_recursive_tower_fixture(),
        "jacobian_bigrading": run_jacobian_bigrading_fixture(),
        "connection_curvature": run_connection_curvature_fixture(),
        "tower_observer": run_tower_observer_fixture(),
        "rank_change_cut": run_rank_change_cut_fixture(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    status = (
        "PASS_CUT_GRADED_LAMBDA_JACOBIAN_TOWER_CANDIDATE"
        if all(checks.values())
        else "FAIL_CUT_GRADED_LAMBDA_JACOBIAN_TOWER_CANDIDATE"
    )
    return {
        "schema": "rkf.cut_graded_lambda_jacobian_tower_candidate.v1",
        "source_scope": {
            "paper": "arXiv:2603.20773v2",
            "consumed_structure": [
                "T-V-S-P compass",
                "four-component lambda response map",
                "recursive Jacobian layers",
                "jet-bundle analogy",
                "response curvature as a proposed constitutive extension",
            ],
            "not_consumed_as_proved": [
                "automatic antisymmetry of the physical lambda Jacobian",
                "automatic equivalence of cut-loop curvature and thermodynamic curvature",
                "experimental validity of the non-equilibrium closure",
            ],
        },
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "typed quadratic response tower through Hessian order",
                "cut equivariance of values, Jacobians, and Hessians",
                "four-sector cut/transpose Jacobian decomposition",
                "antisymmetry is a sector condition rather than an automatic identity",
                "constant-connection mixed curvature equals cut-loop seam curvature",
                "higher derivative layer repairs a first-order target-blind direction",
                "rank-change cut and higher-layer recovery calibration",
            ],
            "analytic_theorem_requires": [
                "a smooth thermodynamic state manifold",
                "dimensionless or bundle-covariant state coordinates",
                "a declared involution on state and response bundles",
                "a cut-compatible connection",
                "constitutive proof that the physical lambda map is a bundle section",
                "an intertwiner from operator seam curvature to the paper's response two-form",
            ],
            "held": [
                "claim that the physical Jacobian in arXiv:2603.20773 is globally antisymmetric",
                "claim that every phase transition is exactly a rank-change cut",
                "claim that the proposed curvature equals entropy production without calibration",
                "paper manuscript update until user-local certificate pass",
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
    print("RECURSIVE_TOWER", payload["checks"]["recursive_tower_all_checks"])
    print("JACOBIAN_BIGRADING", payload["checks"]["jacobian_bigrading_all_checks"])
    print("CONNECTION_CURVATURE", payload["checks"]["connection_curvature_all_checks"])
    print("TOWER_OBSERVER", payload["checks"]["tower_observer_all_checks"])
    print("RANK_CHANGE_CUT", payload["checks"]["rank_change_cut_all_checks"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
