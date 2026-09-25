from __future__ import annotations

"""Exact cut-graded universal-generator calibration.

The module uses only ``fractions.Fraction``. It verifies finite-dimensional
shadows of the abstract cut-graded generator theorem without importing a
spectral library, fitted basis, floating point, or a post-hoc matrix factor.

The exact certificate is a calibration of the theorem. It is not a substitute
for the analytic domain hypotheses required by an unbounded generator.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

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
    if n < 1:
        raise ValueError("dimension must be positive")
    return diagonal([1] * n)


def zero(n: int, m: int) -> Matrix:
    if n < 1 or m < 1:
        raise ValueError("dimensions must be positive")
    return tuple(tuple(Fraction(0) for _ in range(m)) for _ in range(n))


def shape(a: Matrix) -> tuple[int, int]:
    return (len(a), len(a[0]) if a else 0)


def assert_same_shape(a: Matrix, b: Matrix) -> None:
    if shape(a) != shape(b):
        raise ValueError("matrix shape mismatch")


def add(a: Matrix, b: Matrix) -> Matrix:
    assert_same_shape(a, b)
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(len(a[0])))
        for i in range(len(a))
    )


def sub(a: Matrix, b: Matrix) -> Matrix:
    assert_same_shape(a, b)
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(len(a[0])))
        for i in range(len(a))
    )


def scale(c: int | Fraction, a: Matrix) -> Matrix:
    factor = q(c)
    return tuple(tuple(factor * x for x in row) for row in a)


def transpose(a: Matrix) -> Matrix:
    if not a:
        return tuple()
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


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
    if n != m:
        raise ValueError("power requires a square matrix")
    if exponent < 0:
        raise ValueError("negative powers are not used")
    out = identity(n)
    for _ in range(exponent):
        out = matmul(out, a)
    return out


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def is_zero(a: Matrix) -> bool:
    return all(x == 0 for row in a for x in row)


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


def involution_projectors(j: Matrix) -> tuple[Matrix, Matrix]:
    n, m = shape(j)
    if n != m or matmul(j, j) != identity(n):
        raise ValueError("j must be an involution")
    return (
        scale(Fraction(1, 2), add(identity(n), j)),
        scale(Fraction(1, 2), sub(identity(n), j)),
    )


def cut_decomposition(g: Matrix, j: Matrix) -> tuple[Matrix, Matrix]:
    if shape(g) != shape(j) or len(g) != len(g[0]):
        raise ValueError("g and j must be square matrices of the same size")
    if matmul(j, j) != identity(len(j)):
        raise ValueError("j must be an involution")
    jgj = matmul(matmul(j, g), j)
    g_even = scale(Fraction(1, 2), add(g, jgj))
    g_odd = scale(Fraction(1, 2), sub(g, jgj))
    return g_even, g_odd


def exponential_series(g: Matrix, order: int) -> tuple[Matrix, ...]:
    if order < 0:
        raise ValueError("order must be nonnegative")
    n, m = shape(g)
    if n != m:
        raise ValueError("g must be square")
    coefficients: list[Matrix] = []
    factorial = 1
    for k in range(order + 1):
        if k > 0:
            factorial *= k
        coefficients.append(scale(Fraction(1, factorial), power(g, k)))
    return tuple(coefficients)


def multiply_series(a: Sequence[Matrix], b: Sequence[Matrix], order: int) -> tuple[Matrix, ...]:
    if len(a) <= order or len(b) <= order:
        raise ValueError("series must contain all requested coefficients")
    n, m = shape(a[0])
    out: list[Matrix] = []
    for degree in range(order + 1):
        coefficient = zero(n, m)
        for left_degree in range(degree + 1):
            coefficient = add(
                coefficient,
                matmul(a[left_degree], b[degree - left_degree]),
            )
        out.append(coefficient)
    return tuple(out)


def cut_loop_series(g: Matrix, j: Matrix, order: int = 3) -> tuple[Matrix, ...]:
    jgj = matmul(matmul(j, g), j)
    return multiply_series(
        exponential_series(jgj, order),
        exponential_series(g, order),
        order,
    )


def log_series_first_two(loop: Sequence[Matrix]) -> tuple[Matrix, Matrix]:
    """Return coefficients of t and t^2 in log(I + H1 t + H2 t^2 + ...)."""
    if len(loop) < 3:
        raise ValueError("loop series must be known through order two")
    h1 = loop[1]
    h2 = loop[2]
    return h1, sub(h2, scale(Fraction(1, 2), matmul(h1, h1)))


def nilpotent_odd_flow(g_odd: Matrix, t: int | Fraction) -> dict[str, Matrix]:
    if not is_zero(power(g_odd, 2)):
        raise ValueError("exact finite flow fixture requires g_odd^2=0")
    tau = q(t)
    i = identity(len(g_odd))
    u_plus = add(i, scale(tau, g_odd))
    u_minus = sub(i, scale(tau, g_odd))
    join = add(u_plus, u_minus)
    cut = sub(u_plus, u_minus)
    return {
        "u_plus": u_plus,
        "u_minus": u_minus,
        "join": join,
        "cut": cut,
    }


def closure_sign(phase_in_pi_units: Fraction, steps: int) -> int | None:
    """Return the sign of exp(i*pi*steps*phase), or None when it is not ±1."""
    if steps < 1:
        raise ValueError("steps must be positive")
    winding = q(steps) * phase_in_pi_units
    if winding.denominator != 1:
        return None
    return 1 if winding.numerator % 2 == 0 else -1


def eye_sectors(frequencies_in_2pi_units: Iterable[Fraction]) -> dict[str, tuple[int, ...]]:
    frequencies = tuple(q(x) for x in frequencies_in_2pi_units)
    single_step = tuple(i for i, value in enumerate(frequencies) if value.denominator == 1)
    all_time = tuple(i for i, value in enumerate(frequencies) if value == 0)
    blind = tuple(i for i in single_step if i not in all_time)
    return {
        "single_step_fixed": single_step,
        "all_time_fixed": all_time,
        "stroboscopic_blind": blind,
    }


def component_gram(components: Sequence[Matrix]) -> Matrix:
    if not components:
        raise ValueError("at least one component is required")
    n = len(components[0][0])
    out = zero(n, n)
    for component in components:
        out = add(out, matmul(transpose(component), component))
    return out


def run_cut_decomposition_fixture() -> dict[str, Any]:
    j = diagonal((1, 1, -1, -1))
    g_even_declared = matrix(
        (
            (1, 2, 0, 0),
            (0, -1, 0, 0),
            (0, 0, 2, 1),
            (0, 0, 0, 3),
        )
    )
    g_odd_declared = matrix(
        (
            (0, 0, 1, 2),
            (0, 0, 0, 1),
            (3, 0, 0, 0),
            (1, 4, 0, 0),
        )
    )
    g = add(g_even_declared, g_odd_declared)
    g_even, g_odd = cut_decomposition(g, j)
    p_plus, p_minus = involution_projectors(j)
    checks = {
        "reconstruction": add(g_even, g_odd) == g,
        "even_part_recovered": g_even == g_even_declared,
        "odd_part_recovered": g_odd == g_odd_declared,
        "even_cut_covariance": matmul(matmul(j, g_even), j) == g_even,
        "odd_cut_covariance": matmul(matmul(j, g_odd), j) == scale(-1, g_odd),
        "even_cross_blocks_zero": (
            is_zero(matmul(matmul(p_plus, g_even), p_minus))
            and is_zero(matmul(matmul(p_minus, g_even), p_plus))
        ),
        "odd_diagonal_blocks_zero": (
            is_zero(matmul(matmul(p_plus, g_odd), p_plus))
            and is_zero(matmul(matmul(p_minus, g_odd), p_minus))
        ),
    }
    return {
        "schema": "rkf.cut_graded_generator_decomposition.v1",
        "cut": record_matrix(j),
        "generator": record_matrix(g),
        "even_part": record_matrix(g_even),
        "odd_part": record_matrix(g_odd),
        "checks": checks,
    }


def run_cut_loop_fixture() -> dict[str, Any]:
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
    loop = cut_loop_series(g, j, order=3)
    log_first, log_second = log_series_first_two(loop)
    expected_loop_first = scale(2, g_even)
    expected_loop_second = add(
        scale(2, matmul(g_even, g_even)),
        commutator(g_even, g_odd),
    )
    checks = {
        "cut_loop_first_derivative_is_twice_even_generator": loop[1] == expected_loop_first,
        "cut_loop_second_coefficient": loop[2] == expected_loop_second,
        "log_loop_linear_memory": log_first == scale(2, g_even),
        "log_loop_quadratic_seam_curvature": log_second == commutator(g_even, g_odd),
        "general_fixture_has_nonzero_memory": not is_zero(g_even),
        "general_fixture_has_nonzero_seam_curvature": not is_zero(commutator(g_even, g_odd)),
    }
    return {
        "schema": "rkf.cut_loop_memory_curvature.v1",
        "generator_even": record_matrix(g_even),
        "generator_odd": record_matrix(g_odd),
        "cut_loop_t_coefficient": record_matrix(loop[1]),
        "cut_loop_t2_coefficient": record_matrix(loop[2]),
        "log_loop_t_coefficient": record_matrix(log_first),
        "log_loop_t2_coefficient": record_matrix(log_second),
        "checks": checks,
    }


def run_bilateral_flow_fixture() -> dict[str, Any]:
    j = diagonal((1, 1, -1, -1))
    g_odd = matrix(
        (
            (0, 0, 1, 2),
            (0, 0, 0, 1),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        )
    )
    flow = nilpotent_odd_flow(g_odd, Fraction(3, 2))
    join = flow["join"]
    cut = flow["cut"]
    i = identity(4)
    checks = {
        "odd_generator_nilpotent": is_zero(power(g_odd, 2)),
        "cut_reverses_generator": matmul(matmul(j, g_odd), j) == scale(-1, g_odd),
        "cut_reverses_flow": matmul(matmul(j, flow["u_plus"]), j) == flow["u_minus"],
        "bilateral_reconstruction_forward": scale(Fraction(1, 2), add(join, cut)) == flow["u_plus"],
        "bilateral_reconstruction_backward": scale(Fraction(1, 2), sub(join, cut)) == flow["u_minus"],
        "derived_channels_commute": matmul(join, cut) == matmul(cut, join),
        "exponential_cut_square": sub(matmul(join, join), matmul(cut, cut)) == scale(4, i),
        "corrected_cut_join_product": matmul(join, cut) == scale(6, g_odd),
    }
    return {
        "schema": "rkf.bilateral_exponential_cut_square.v1",
        "time": "3/2",
        "generator_odd": record_matrix(g_odd),
        "forward_flow": record_matrix(flow["u_plus"]),
        "backward_flow": record_matrix(flow["u_minus"]),
        "join_channel": record_matrix(join),
        "cut_channel": record_matrix(cut),
        "checks": checks,
    }


def run_closure_spectrum_fixture() -> dict[str, Any]:
    cases = {
        "eight_step_plus": closure_sign(Fraction(1, 2), 8),
        "eight_step_minus": closure_sign(Fraction(1, 8), 8),
        "eight_step_nonclosure": closure_sign(Fraction(1, 3), 8),
        "four_step_minus": closure_sign(Fraction(1, 4), 4),
    }
    checks = {
        "plus_sector_detected": cases["eight_step_plus"] == 1,
        "minus_sector_detected": cases["eight_step_minus"] == -1,
        "nonclosure_rejected": cases["eight_step_nonclosure"] is None,
        "minus_not_lost_by_two_pi_only_rule": cases["four_step_minus"] == -1,
    }
    return {
        "schema": "rkf.periodic_antiperiodic_closure_spectrum.v1",
        "cases": cases,
        "checks": checks,
    }


def run_eye_fixture() -> dict[str, Any]:
    sectors = eye_sectors(
        (
            Fraction(0),
            Fraction(1),
            Fraction(-2),
            Fraction(1, 2),
            Fraction(3, 2),
        )
    )
    checks = {
        "single_step_eye_contains_integer_frequencies": sectors["single_step_fixed"] == (0, 1, 2),
        "clock_free_eye_is_zero_frequency_only": sectors["all_time_fixed"] == (0,),
        "stroboscopic_blind_modes_detected": sectors["stroboscopic_blind"] == (1, 2),
    }
    return {
        "schema": "rkf.clock_free_eye_projector.v1",
        "frequencies_in_2pi_units": ["0", "1", "-2", "1/2", "3/2"],
        "single_step_fixed_indices": list(sectors["single_step_fixed"]),
        "all_time_fixed_indices": list(sectors["all_time_fixed"]),
        "stroboscopic_blind_indices": list(sectors["stroboscopic_blind"]),
        "checks": checks,
    }


def run_component_observer_fixture() -> dict[str, Any]:
    g = matrix(((1, 2), (3, 4)))
    p_first = diagonal((1, 0))
    p_second = diagonal((0, 1))
    components = (matmul(p_first, g), matmul(p_second, g))
    direct_gram = component_gram(components)
    generator_gram = matmul(transpose(g), g)

    cancelling_left = identity(2)
    cancelling_right = scale(-1, identity(2))
    probe = (Fraction(1), Fraction(2))
    aggregate = add(cancelling_left, cancelling_right)
    aggregate_probe = tuple(
        sum((aggregate[i][j] * probe[j] for j in range(2)), Fraction(0))
        for i in range(2)
    )
    direct_probe_energy = sum(
        (
            sum((component[i][j] * probe[j] for j in range(2)), Fraction(0)) ** 2
            for component in (cancelling_left, cancelling_right)
            for i in range(2)
        ),
        Fraction(0),
    )
    checks = {
        "orthogonal_complete_components_preserve_gram": direct_gram == generator_gram,
        "orthogonal_components_have_no_hidden_cancellation": direct_gram != zero(2, 2),
        "nonorthogonal_aggregate_can_cancel": aggregate_probe == (0, 0),
        "direct_sum_retains_cancelled_activity": direct_probe_energy == 10,
    }
    return {
        "schema": "rkf.component_observer_and_cancellation_control.v1",
        "generator": record_matrix(g),
        "direct_component_gram": record_matrix(direct_gram),
        "generator_gram": record_matrix(generator_gram),
        "negative_control_probe": ["1", "2"],
        "negative_control_aggregate_output": [ftext(x) for x in aggregate_probe],
        "negative_control_direct_energy": ftext(direct_probe_energy),
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "cut_decomposition": run_cut_decomposition_fixture(),
        "cut_loop": run_cut_loop_fixture(),
        "bilateral_flow": run_bilateral_flow_fixture(),
        "closure_spectrum": run_closure_spectrum_fixture(),
        "clock_free_eye": run_eye_fixture(),
        "component_observer": run_component_observer_fixture(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    status = (
        "PASS_CUT_GRADED_UNIVERSAL_GENERATOR_CANDIDATE"
        if all(checks.values())
        else "FAIL_CUT_GRADED_UNIVERSAL_GENERATOR_CANDIDATE"
    )
    return {
        "schema": "rkf.cut_graded_universal_generator_candidate.v1",
        "status": status,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "unique cut-even/cut-odd decomposition",
                "block support relative to the cut projectors",
                "cut-loop linear memory coefficient",
                "cut-loop quadratic seam-curvature coefficient",
                "bilateral reconstruction for an exact nilpotent odd flow",
                "exponential cut-square identity",
                "periodic and antiperiodic closure-character classification",
                "single-step versus clock-free Eye distinction",
                "direct-sum component observer and cancellation negative control",
            ],
            "analytic_theorem_requires": [
                "a Hilbert carrier",
                "a unitary self-adjoint involution preserving Dom(G)",
                "a closed densely defined generator",
                "a lawful exponential or strongly continuous group",
                "common invariant cores for unbounded products and commutators",
            ],
            "held_until_user_run": [
                "central theorem promotion",
                "manuscript replacement of the uploaded universal-generator theorem",
                "public claim that a physical universal generator has been identified",
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
    print("CUT_DECOMPOSITION", payload["checks"]["cut_decomposition_all_checks"])
    print("CUT_LOOP_MEMORY_CURVATURE", payload["checks"]["cut_loop_all_checks"])
    print("BILATERAL_EXPONENTIAL_CUT_SQUARE", payload["checks"]["bilateral_flow_all_checks"])
    print("CLOSURE_SPECTRUM", payload["checks"]["closure_spectrum_all_checks"])
    print("CLOCK_FREE_EYE", payload["checks"]["clock_free_eye_all_checks"])
    print("COMPONENT_OBSERVER", payload["checks"]["component_observer_all_checks"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
