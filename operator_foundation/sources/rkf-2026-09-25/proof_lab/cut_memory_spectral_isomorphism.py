from __future__ import annotations

"""Cut-memory spectral isomorphism and finite-rank reduction.

This module implements the finite-dimensional numerical shadow of the theorem:

    F = R - V V*
    B = V* R^{-1} V

with R positive definite and V finite rank. The exact conclusions are:

    N_-(F) = N_+(B-I)
    dim ker(F) = dim ker(I-B)
    inf <x,Fx>/<x,Rx> = lambda_min(I-B)
    det(F)/det(R) = det(I-B)

The determinant sign alone is not a positivity criterion when rank(V) >= 2.
"""

from dataclasses import dataclass
from fractions import Fraction
import json
from math import prod
from pathlib import Path
from typing import Any, Iterable

import numpy as np


TOL = 1.0e-10


def _hermitian(matrix: np.ndarray) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=np.complex128)
    return 0.5 * (matrix + matrix.conj().T)


def _positive_inverse_sqrt(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    matrix = _hermitian(matrix)
    values, vectors = np.linalg.eigh(matrix)
    if float(np.min(values)) <= 0.0:
        raise ValueError("reference matrix must be positive definite")
    sqrt = (vectors * np.sqrt(values)) @ vectors.conj().T
    inverse_sqrt = (vectors * (1.0 / np.sqrt(values))) @ vectors.conj().T
    return sqrt, inverse_sqrt


def inertia(matrix: np.ndarray, *, tol: float = TOL) -> dict[str, int]:
    values = np.linalg.eigvalsh(_hermitian(matrix))
    return {
        "negative": int(np.sum(values < -tol)),
        "zero": int(np.sum(np.abs(values) <= tol)),
        "positive": int(np.sum(values > tol)),
    }


def positive_spectrum(matrix: np.ndarray, *, tol: float = TOL) -> np.ndarray:
    values = np.linalg.eigvalsh(_hermitian(matrix))
    return np.asarray(values[values > tol], dtype=float)


@dataclass(frozen=True)
class CutBridgeAudit:
    source_dimension: int
    event_dimension: int
    rank: int
    kernel_dimension: int
    adjoint_kernel_dimension: int
    index: int
    positive_spectrum_residual: float
    iota_square_residual: float


def audit_cut_bridge(cut_bridge: np.ndarray, *, tol: float = TOL) -> CutBridgeAudit:
    """Verify shared positive spectrum and directional zero memory."""

    c = np.asarray(cut_bridge, dtype=np.complex128)
    event_dimension, source_dimension = c.shape
    rank = int(np.linalg.matrix_rank(c, tol=tol))
    kernel_dimension = source_dimension - rank
    adjoint_kernel_dimension = event_dimension - rank

    c_star_c = _hermitian(c.conj().T @ c)
    c_c_star = _hermitian(c @ c.conj().T)
    left = positive_spectrum(c_star_c, tol=tol)
    right = positive_spectrum(c_c_star, tol=tol)
    if left.shape != right.shape:
        spectrum_residual = float("inf")
    elif left.size:
        spectrum_residual = float(np.max(np.abs(left - right)))
    else:
        spectrum_residual = 0.0

    # Polar partial isometry U = C (C*C)^dagger/2.
    values, vectors = np.linalg.eigh(c_star_c)
    inverse_sqrt_values = np.zeros_like(values)
    mask = values > tol
    inverse_sqrt_values[mask] = 1.0 / np.sqrt(values[mask])
    c_star_c_dagger_half = (
        vectors * inverse_sqrt_values
    ) @ vectors.conj().T
    u = c @ c_star_c_dagger_half

    # On the initial and final support, iota^2 = -I.
    p_initial = _hermitian(u.conj().T @ u)
    p_final = _hermitian(u @ u.conj().T)
    iota = np.block(
        [
            [np.zeros((source_dimension, source_dimension), dtype=np.complex128), -u.conj().T],
            [u, np.zeros((event_dimension, event_dimension), dtype=np.complex128)],
        ]
    )
    support = np.block(
        [
            [p_initial, np.zeros((source_dimension, event_dimension), dtype=np.complex128)],
            [np.zeros((event_dimension, source_dimension), dtype=np.complex128), p_final],
        ]
    )
    iota_square_residual = float(np.linalg.norm(iota @ iota + support, ord=2))

    return CutBridgeAudit(
        source_dimension=source_dimension,
        event_dimension=event_dimension,
        rank=rank,
        kernel_dimension=kernel_dimension,
        adjoint_kernel_dimension=adjoint_kernel_dimension,
        index=kernel_dimension - adjoint_kernel_dimension,
        positive_spectrum_residual=spectrum_residual,
        iota_square_residual=iota_square_residual,
    )


@dataclass(frozen=True)
class FiniteReductionAudit:
    ambient_dimension: int
    memory_rank: int
    b_eigenvalues: tuple[float, ...]
    relative_gap_from_full_operator: float
    relative_gap_from_five_matrix: float
    gap_residual: float
    full_negative_index: int
    seam_integer: int
    kernel_dimension_full: int
    kernel_dimension_five: int
    determinant_ratio: float
    determinant_five: float
    determinant_residual: float
    normalized_factorization_residual: float


def audit_finite_reduction(
    reference: np.ndarray,
    memory_columns: np.ndarray,
    *,
    tol: float = TOL,
) -> FiniteReductionAudit:
    """Audit the exact Birman--Schwinger/Fredholm reduction."""

    r = _hermitian(reference)
    v = np.asarray(memory_columns, dtype=np.complex128)
    ambient_dimension = r.shape[0]
    if r.shape != (ambient_dimension, ambient_dimension):
        raise ValueError("reference must be square")
    if v.shape[0] != ambient_dimension:
        raise ValueError("memory columns must live in the reference carrier")

    _, r_inverse_sqrt = _positive_inverse_sqrt(r)
    r_inverse = r_inverse_sqrt @ r_inverse_sqrt
    a = r_inverse_sqrt @ v
    b = _hermitian(v.conj().T @ r_inverse @ v)
    f = _hermitian(r - v @ v.conj().T)
    normalized = _hermitian(r_inverse_sqrt @ f @ r_inverse_sqrt)
    factorized = _hermitian(np.eye(ambient_dimension) - a @ a.conj().T)

    b_values = np.linalg.eigvalsh(b)
    relative_gap_full = float(np.min(np.linalg.eigvalsh(normalized)))
    relative_gap_five = float(np.min(np.linalg.eigvalsh(np.eye(b.shape[0]) - b)))

    full_inertia = inertia(f, tol=tol)
    five_inertia = inertia(np.eye(b.shape[0]) - b, tol=tol)
    seam_integer = int(np.sum(b_values > 1.0 + tol))

    sign_r, logdet_r = np.linalg.slogdet(r)
    sign_f, logdet_f = np.linalg.slogdet(f)
    if sign_r == 0:
        raise ValueError("reference determinant vanished")
    determinant_ratio_value = np.real_if_close(
        (sign_f / sign_r) * np.exp(logdet_f - logdet_r)
    )
    determinant_ratio = float(np.real(determinant_ratio_value))
    determinant_five = float(np.linalg.det(np.eye(b.shape[0]) - b).real)

    return FiniteReductionAudit(
        ambient_dimension=ambient_dimension,
        memory_rank=v.shape[1],
        b_eigenvalues=tuple(float(x) for x in b_values),
        relative_gap_from_full_operator=relative_gap_full,
        relative_gap_from_five_matrix=relative_gap_five,
        gap_residual=abs(relative_gap_full - relative_gap_five),
        full_negative_index=full_inertia["negative"],
        seam_integer=seam_integer,
        kernel_dimension_full=full_inertia["zero"],
        kernel_dimension_five=five_inertia["zero"],
        determinant_ratio=determinant_ratio,
        determinant_five=determinant_five,
        determinant_residual=abs(determinant_ratio - determinant_five),
        normalized_factorization_residual=float(
            np.linalg.norm(normalized - factorized, ord=2)
        ),
    )


def _diagonal_packet(
    values: Iterable[Fraction],
    *,
    ambient_dimension: int = 8,
) -> tuple[np.ndarray, np.ndarray]:
    values = list(values)
    if ambient_dimension < len(values):
        raise ValueError("ambient dimension must dominate memory rank")
    reference = np.eye(ambient_dimension, dtype=np.float64)
    memory = np.zeros((ambient_dimension, len(values)), dtype=np.float64)
    for index, value in enumerate(values):
        numerator_sqrt = int(round(value.numerator ** 0.5))
        denominator_sqrt = int(round(value.denominator ** 0.5))
        if numerator_sqrt * numerator_sqrt != value.numerator:
            raise ValueError("calibration numerator must be a square")
        if denominator_sqrt * denominator_sqrt != value.denominator:
            raise ValueError("calibration denominator must be a square")
        memory[index, index] = numerator_sqrt / denominator_sqrt
    return reference, memory


def _stable(value: Any) -> Any:
    """Round floating diagnostics for byte-stable cross-platform certificates."""
    if isinstance(value, float):
        if not np.isfinite(value):
            return value
        return float(f"{value:.13g}")
    if isinstance(value, dict):
        return {key: _stable(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return tuple(_stable(item) for item in value)
    if isinstance(value, list):
        return [_stable(item) for item in value]
    return value


def _fraction_product(values: Iterable[Fraction]) -> Fraction:
    return prod(values, start=Fraction(1, 1))


def build_certificate() -> dict[str, Any]:
    # A 5 x 7 bridge: five transported positive modes and two source-side zero memories.
    cut_bridge = np.zeros((5, 7), dtype=np.float64)
    cut_bridge[:, :5] = np.diag([1.0, 2.0, 3.0, 4.0, 5.0])
    bridge = audit_cut_bridge(cut_bridge)

    subcritical_values = [
        Fraction(1, 4),
        Fraction(4, 9),
        Fraction(9, 16),
        Fraction(16, 25),
        Fraction(81, 100),
    ]
    r_sub, v_sub = _diagonal_packet(subcritical_values)
    subcritical = audit_finite_reduction(r_sub, v_sub)
    exact_subcritical_det = _fraction_product(1 - x for x in subcritical_values)
    exact_subcritical_gap = min(1 - x for x in subcritical_values)

    threshold_values = [
        Fraction(1, 4),
        Fraction(4, 9),
        Fraction(9, 16),
        Fraction(16, 25),
        Fraction(1, 1),
    ]
    r_thr, v_thr = _diagonal_packet(threshold_values)
    threshold = audit_finite_reduction(r_thr, v_thr)

    # Two super-threshold eigenvalues make det(I-B) positive: determinant sign is insufficient.
    supercritical_values = [
        Fraction(4, 1),
        Fraction(9, 4),
        Fraction(1, 4),
        Fraction(4, 9),
        Fraction(9, 16),
    ]
    r_sup, v_sup = _diagonal_packet(supercritical_values)
    supercritical = audit_finite_reduction(r_sup, v_sup)
    exact_supercritical_det = _fraction_product(1 - x for x in supercritical_values)

    # Non-diagonal covariance calibration.
    rng = np.random.default_rng(20260803)
    raw = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    q, _ = np.linalg.qr(raw)
    r_cov = q @ np.diag(np.linspace(1.5, 4.0, 8)) @ q.conj().T
    raw_v = rng.normal(size=(8, 5)) + 1j * rng.normal(size=(8, 5))
    preliminary = audit_finite_reduction(r_cov, raw_v)
    scale = 0.75 / max(preliminary.b_eigenvalues) ** 0.5
    v_cov = scale * raw_v
    covariant = audit_finite_reduction(r_cov, v_cov)

    checks = {
        "positive_spectrum_shared": bridge.positive_spectrum_residual < 1.0e-12,
        "directional_zero_memory_index": bridge.index == 2,
        "polar_iota_square": bridge.iota_square_residual < 1.0e-12,
        "subcritical_gap_exact": abs(
            subcritical.relative_gap_from_five_matrix - float(exact_subcritical_gap)
        ) < 1.0e-12,
        "subcritical_full_five_gap_match": subcritical.gap_residual < 1.0e-12,
        "subcritical_inertia_match": (
            subcritical.full_negative_index == subcritical.seam_integer == 0
        ),
        "subcritical_kernel_match": (
            subcritical.kernel_dimension_full == subcritical.kernel_dimension_five == 0
        ),
        "subcritical_determinant_identity": (
            subcritical.determinant_residual < 1.0e-12
            and abs(subcritical.determinant_five - float(exact_subcritical_det)) < 1.0e-12
        ),
        "threshold_zero_memory": (
            threshold.kernel_dimension_full == threshold.kernel_dimension_five == 1
            and abs(threshold.determinant_five) < 1.0e-12
        ),
        "positive_determinant_negative_control": (
            exact_supercritical_det > 0
            and supercritical.determinant_five > 0
            and supercritical.full_negative_index == supercritical.seam_integer == 2
        ),
        "nondiagonal_gap_match": covariant.gap_residual < 5.0e-12,
        "nondiagonal_inertia_match": (
            covariant.full_negative_index == covariant.seam_integer
        ),
        "nondiagonal_determinant_identity": covariant.determinant_residual < 5.0e-11,
        "normalized_factorization": (
            subcritical.normalized_factorization_residual < 1.0e-12
            and threshold.normalized_factorization_residual < 1.0e-12
            and supercritical.normalized_factorization_residual < 1.0e-12
            and covariant.normalized_factorization_residual < 5.0e-12
        ),
    }

    status = (
        "PASS_CUT_MEMORY_SPECTRAL_ISOMORPHISM_V0_1"
        if all(checks.values())
        else "FAIL_CUT_MEMORY_SPECTRAL_ISOMORPHISM_V0_1"
    )

    return _stable({
        "schema": "rkf-cut-memory-spectral-isomorphism-v0.1",
        "status": status,
        "theorem_boundary": {
            "proved": [
                "positive nonzero spectra of C*C and CC* coincide",
                "zero-mode asymmetry is the Fredholm index of C",
                "F >= 0 iff B <= I",
                "negative index of F equals seam integer N_+(B-I)",
                "relative gap equals lambda_min(I-B)",
                "relative Fredholm determinant equals det(I-B)",
                "rank-at-most-five cut memory reduces the infinite sign/gap test to at most 5x5",
            ],
            "explicitly_rejected": [
                "det(I-B) > 0 alone implies positivity when rank >= 2",
                "centrality of the cut projection alone implies rank five",
                "ordinary spectral gap equals lambda_min(I-B) without reference normalization",
            ],
        },
        "cut_bridge": bridge.__dict__,
        "subcritical": {
            **subcritical.__dict__,
            "exact_relative_gap": str(exact_subcritical_gap),
            "exact_determinant": str(exact_subcritical_det),
        },
        "threshold": threshold.__dict__,
        "supercritical_positive_determinant_control": {
            **supercritical.__dict__,
            "exact_determinant": str(exact_supercritical_det),
        },
        "nondiagonal_covariance": covariant.__dict__,
        "checks": checks,
    })


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = build_certificate()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(report["status"])
    print(json.dumps(report["checks"], indent=2, sort_keys=True))
    return 0 if report["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
