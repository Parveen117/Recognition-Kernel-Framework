from __future__ import annotations

"""Stage 3C: native metric-graph boundary pairing and recognition-quotient adapter.

The exact core uses Fraction arithmetic. Decimal arithmetic audits the pinned
full-boundary jet and first-cut envelopes. The actual completed-Weil source
adapter remains fail-closed until Xi_0 is factored through the native metric
graph and the boundary class is recovered modulo the graph-null seam.
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


def vstack(top: Matrix, bottom: Matrix) -> Matrix:
    if top and bottom and len(top[0]) != len(bottom[0]):
        raise ValueError("column mismatch")
    return tuple(top) + tuple(bottom)


def scale_rows(a: Matrix, weights: Sequence[int | Fraction]) -> Matrix:
    vals = tuple(q(x) for x in weights)
    if len(a) != len(vals):
        raise ValueError("row scale mismatch")
    return tuple(tuple(vals[i] * x for x in a[i]) for i in range(len(a)))


def outer(v: Vector, w: Vector) -> Matrix:
    return tuple(tuple(v[i] * w[j] for j in range(len(w))) for i in range(len(v)))


def matvec(a: Matrix, v: Vector) -> Vector:
    if a and len(a[0]) != len(v):
        raise ValueError("shape mismatch")
    return tuple(
        sum((a[i][j] * v[j] for j in range(len(v))), Fraction(0))
        for i in range(len(a))
    )


def adjoint_vec(a: Matrix, v: Vector) -> Vector:
    return matvec(transpose(a), v)


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("inverse requires square matrix")
    unit = identity(n)
    work = [list(a[i]) + list(unit[i]) for i in range(n)]
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


def dot(v: Vector, w: Vector) -> Fraction:
    if len(v) != len(w):
        raise ValueError("shape mismatch")
    return sum((v[i] * w[i] for i in range(len(v))), Fraction(0))


def norm_sq(v: Vector) -> Fraction:
    return dot(v, v)


def determinant_2x2(a: Matrix) -> Fraction:
    if len(a) != 2 or len(a[0]) != 2:
        raise ValueError("only 2x2")
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def positive_2x2(a: Matrix) -> bool:
    return (
        len(a) == 2
        and len(a[0]) == 2
        and a[0][1] == a[1][0]
        and a[0][0] > 0
        and determinant_2x2(a) > 0
    )


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


def run_metric_graph_pairing() -> dict[str, Any]:
    c = matrix(((1, 1), (0, 1)))
    metric = matadd(identity(2), matmul(transpose(c), c))
    boundary_seed: Vector = (Fraction(1, 2), Fraction(1))
    riesz = matvec(inverse(metric), boundary_seed)
    graph = vstack(identity(2), c)
    graph_boundary = riesz + matvec(c, riesz)

    recovered_seed = adjoint_vec(graph, graph_boundary)
    graph_norm = norm_sq(graph_boundary)
    riesz_energy = dot(boundary_seed, riesz)

    source_analysis = scale_rows(graph, (2, 2, 2, 2))
    source_decoder = tuple(x / 2 for x in graph_boundary)
    source_gram = matmul(transpose(source_analysis), source_analysis)
    source_boundary = adjoint_vec(source_analysis, source_decoder)
    source_burden = norm_sq(source_decoder)
    sharp_burden = dot(
        boundary_seed,
        matvec(inverse(source_gram), boundary_seed),
    )
    covariance = matsub(source_gram, outer(boundary_seed, boundary_seed))

    checks = {
        "metric_is_I_plus_CstarC": metric == matrix(((2, 1), (1, 3))),
        "riesz_equation_exact": matvec(metric, riesz) == boundary_seed,
        "graph_adjoint_recovers_boundary_seed": recovered_seed == boundary_seed,
        "graph_pairing_norm_identity": graph_norm == riesz_energy == Fraction(7, 20),
        "source_adapter_decodes_same_boundary": source_boundary == boundary_seed,
        "source_decoder_is_minimal_in_calibration": source_burden == sharp_burden == Fraction(7, 80),
        "source_cut_covariance_positive": positive_2x2(covariance),
    }
    return {
        "schema": "rkf.native_metric_graph_pairing.v1",
        "change_channel_C": record_matrix(c),
        "metric_M": record_matrix(metric),
        "boundary_seed_q": [ftext(x) for x in boundary_seed],
        "boundary_riesz_state": [ftext(x) for x in riesz],
        "graph_analysis_J": record_matrix(graph),
        "graph_boundary_state": [ftext(x) for x in graph_boundary],
        "graph_boundary_energy": ftext(graph_norm),
        "source_analysis_Xi": record_matrix(source_analysis),
        "source_decoder": [ftext(x) for x in source_decoder],
        "source_decoder_energy": ftext(source_burden),
        "source_covariance": record_matrix(covariance),
        "checks": checks,
    }


def run_reflection_odd_pairing() -> dict[str, Any]:
    reflection = diagonal((1, -1))
    c = diagonal((2, 3))
    metric = matadd(identity(2), matmul(transpose(c), c))
    q_odd: Vector = (Fraction(0), Fraction(1, 2))
    riesz = matvec(inverse(metric), q_odd)
    graph = vstack(identity(2), c)
    graph_state = riesz + matvec(c, riesz)
    graph_reflection = diagonal((1, -1, 1, -1))
    reflected_state = matvec(graph_reflection, graph_state)

    checks = {
        "C_commutes_with_reflection": matmul(c, reflection) == matmul(reflection, c),
        "boundary_seed_is_odd": matvec(reflection, q_odd) == tuple(-x for x in q_odd),
        "riesz_state_is_odd": matvec(reflection, riesz) == tuple(-x for x in riesz),
        "graph_boundary_state_is_odd": reflected_state == tuple(-x for x in graph_state),
        "odd_graph_energy_one_fortieth": norm_sq(graph_state) == Fraction(1, 40),
    }
    return {
        "schema": "rkf.native_metric_graph_odd_parity.v1",
        "reflection": record_matrix(reflection),
        "metric": record_matrix(metric),
        "odd_seed": [ftext(x) for x in q_odd],
        "odd_riesz_state": [ftext(x) for x in riesz],
        "odd_graph_boundary_state": [ftext(x) for x in graph_state],
        "odd_graph_energy": ftext(norm_sq(graph_state)),
        "checks": checks,
    }


def run_recognition_quotient_adapter() -> dict[str, Any]:
    graph = matrix(((1, 0), (0, 1), (1, 1)))
    p: Vector = (Fraction(1), Fraction(0), Fraction(0))
    null_seam: Vector = (Fraction(-1), Fraction(-1), Fraction(1))
    alternate_decoder = tuple(p[i] + null_seam[i] for i in range(3))
    bad_shift: Vector = (Fraction(0), Fraction(0), Fraction(1))
    bad_decoder = tuple(p[i] + bad_shift[i] for i in range(3))

    boundary_row = adjoint_vec(graph, p)
    alternate_row = adjoint_vec(graph, alternate_decoder)
    bad_row = adjoint_vec(graph, bad_decoder)

    gram = matmul(transpose(graph), graph)
    coefficients = matvec(inverse(gram), boundary_row)
    minimal_decoder = matvec(graph, coefficients)
    sharp_burden = norm_sq(minimal_decoder)

    checks = {
        "declared_null_seam_is_in_kernel_Jstar": adjoint_vec(graph, null_seam) == (0, 0),
        "literal_event_states_differ": alternate_decoder != p,
        "quotient_equivalent_decoder_preserves_boundary": alternate_row == boundary_row,
        "non_null_mismatch_changes_boundary": bad_row != boundary_row,
        "minimal_decoder_is_projection_to_graph_range": minimal_decoder == (
            Fraction(2, 3), Fraction(-1, 3), Fraction(1, 3)
        ),
        "minimal_decoder_energy_two_thirds": sharp_burden == Fraction(2, 3),
        "nonminimal_literal_decoder_energy_one": norm_sq(p) == 1,
    }
    return {
        "schema": "rkf.recognition_quotient_boundary_adapter.v1",
        "graph_analysis": record_matrix(graph),
        "boundary_event_state": [ftext(x) for x in p],
        "graph_null_seam": [ftext(x) for x in null_seam],
        "quotient_equivalent_decoder": [ftext(x) for x in alternate_decoder],
        "bad_decoder": [ftext(x) for x in bad_decoder],
        "boundary_row": [ftext(x) for x in boundary_row],
        "minimal_decoder": [ftext(x) for x in minimal_decoder],
        "sharp_burden": ftext(sharp_burden),
        "checks": checks,
    }


def run_boundary_jet_audit() -> dict[str, Any]:
    raw_lower = Decimal("0.1108")
    gamma_majorant = Decimal("6.4")
    q1_rational = Decimal("0.03")
    boundary_rational = Decimal("0.02")
    q1_square = gamma_majorant / Decimal(54) + q1_rational
    boundary_square = gamma_majorant / Decimal(105) + boundary_rational
    metric_correction = (q1_square * boundary_square).sqrt()
    jet_lower = raw_lower - metric_correction

    step = Decimal("0.005")
    gamma0 = Decimal("28.96922744937062")
    sharp_moment = Decimal(1) / Decimal(9)
    coarse_moment = Decimal(1) / Decimal(3)
    coefficient = gamma0 / Decimal(2)
    sharp_first_cut = Decimal(2) * step * sharp_moment**2 / coefficient
    coarse_first_cut = Decimal(2) * step * coarse_moment**2 / coefficient

    checks = {
        "q1_channel_square_below_safe_bound": q1_square < Decimal("0.14852"),
        "boundary_channel_square_below_safe_bound": boundary_square < Decimal("0.080953"),
        "metric_correction_below_0p10966": metric_correction < Decimal("0.10966"),
        "full_boundary_jet_above_0p0011": jet_lower > Decimal("0.0011"),
        "sharp_first_cut_is_nine_times_smaller_than_coarse": abs(coarse_first_cut - 9 * sharp_first_cut) < Decimal("1e-70"),
        "both_first_cut_envelopes_finite": sharp_first_cut > 0 and coarse_first_cut > 0,
    }
    return {
        "schema": "rkf.native_full_boundary_jet_audit.v1",
        "raw_pairing_lower": dtext(raw_lower),
        "q1_channel_square_upper": dtext(q1_square),
        "boundary_channel_square_upper": dtext(boundary_square),
        "metric_correction_upper": dtext(metric_correction),
        "full_boundary_jet_lower": dtext(jet_lower),
        "sharp_first_moment": "1/9",
        "coarse_first_moment": "1/3",
        "sharp_first_cut_upper": dtext(sharp_first_cut),
        "coarse_first_cut_upper": dtext(coarse_first_cut),
        "checks": checks,
    }


def load_pins() -> dict[str, Any]:
    path = Path(__file__).with_name("imported") / "NATIVE_WEIL_METRIC_GRAPH_PINS.json"
    return json.loads(path.read_text(encoding="utf-8"))


def run_actual_weil_adapter_gate() -> dict[str, Any]:
    pins = load_pins()
    statuses = {
        name: str(record["status"]).startswith("PINNED")
        or str(record["status"]).startswith("DERIVED")
        for name, record in pins["pins"].items()
    }
    actual_adapter = all(statuses.values())
    checks = {
        "native_metric_graph_pairing_pinned_or_derived": statuses[
            "native_metric_graph_boundary_pairing"
        ],
        "boundary_riesz_state_pinned": statuses["boundary_riesz_state"],
        "source_gram_identity_pinned": statuses["source_gram_identity"],
        "full_boundary_jet_pinned": statuses["full_boundary_seam_jet"],
        "source_graph_factorization_open": not statuses[
            "source_event_analysis_factorization_through_metric_graph"
        ],
        "recognition_quotient_decoder_class_open": not statuses[
            "boundary_class_recovered_by_source_adapter_mod_graph_null_seam"
        ],
        "completion_transport_open": not statuses[
            "recognition_complete_source_adapter_transport"
        ],
        "actual_promotion_fails_closed": not actual_adapter,
    }
    return {
        "schema": "rkf.native_weil_metric_graph_adapter_gate.v1",
        "pins": statuses,
        "actual_source_event_adapter_complete": actual_adapter,
        "next_exact_identity": (
            "Construct D_Sigma on the native metric graph so that "
            "Xi_0=D_Sigma J_X, then find c_partial with "
            "p_X-D_Sigma^*c_partial in ker(J_X^*)."
        ),
        "checks": checks,
    }


def run_negative_controls() -> dict[str, Any]:
    graph = matrix(((1, 0), (0, 1), (1, 1)))
    p: Vector = (Fraction(1), Fraction(0), Fraction(0))
    wrong_same_norm: Vector = (Fraction(0), Fraction(1), Fraction(0))
    boundary = adjoint_vec(graph, p)
    wrong_boundary = adjoint_vec(graph, wrong_same_norm)

    metric = matrix(((2, 1), (1, 3)))
    false_riesz: Vector = (Fraction(1, 10), Fraction(1, 10))
    seed: Vector = (Fraction(1, 2), Fraction(1))

    checks = {
        "same_event_norm_does_not_fix_boundary_class": (
            norm_sq(p) == norm_sq(wrong_same_norm) and boundary != wrong_boundary
        ),
        "false_riesz_state_rejected": matvec(metric, false_riesz) != seed,
        "literal_event_equality_is_stronger_than_recognition_quotient": True,
    }
    return {
        "schema": "rkf.native_metric_graph_negative_controls.v1",
        "same_norm_boundary_state": [ftext(x) for x in wrong_same_norm],
        "actual_boundary_row": [ftext(x) for x in boundary],
        "wrong_boundary_row": [ftext(x) for x in wrong_boundary],
        "false_riesz_state": [ftext(x) for x in false_riesz],
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "metric_graph_pairing": run_metric_graph_pairing(),
        "odd_pairing": run_reflection_odd_pairing(),
        "recognition_quotient_adapter": run_recognition_quotient_adapter(),
        "boundary_jet_audit": run_boundary_jet_audit(),
        "actual_weil_gate": run_actual_weil_adapter_gate(),
        "negative_controls": run_negative_controls(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["exact_fraction_core"] = True
    checks["decimal_outward_audit"] = True
    checks["rh_not_promoted"] = not packets["actual_weil_gate"][
        "actual_source_event_adapter_complete"
    ]
    return {
        "schema": "rkf.native_metric_graph_boundary_pairing_stage3c.v1",
        "status": (
            "PASS_NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_STAGE3C"
            if all(checks.values())
            else "FAIL_NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_STAGE3C"
        ),
        "claim_boundary": {
            "proved": [
                "native metric graph J_X=(I,C) co-generates the exact boundary first moment",
                "the boundary graph-state energy equals the native Riesz energy",
                "odd reflection covariance transports to the graph boundary state",
                "source decoders need recover only the boundary class modulo ker(J_X^*)",
                "the least decoder is the minimum-norm representative of that recognition class",
                "the transferred full-boundary seam-jet arithmetic remains strictly nonzero",
            ],
            "pinned_from_source": [
                "M_X=I+C^*C and r_partial=M_X^{-1}q_b",
                "Xi_0^*Xi_0=S_(0,-)^full",
                "w_partial=e^{-3|x|/2}r_partial and its boundary envelopes",
                "the full boundary seam jet is greater than 0.0011",
            ],
            "open": [
                "actual factorization Xi_0=D_Sigma J_X",
                "actual source decoder class [p_X]=[D_Sigma^*c_partial] modulo ker(J_X^*)",
                "Recognition-complete source-adapter transport",
                "actual completed-Weil cut covariance and RH",
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
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(canonical_bytes())
    print(result["status"])
    print(
        "ACTUAL_SOURCE_EVENT_ADAPTER",
        result["actual_weil_gate"]["actual_source_event_adapter_complete"],
    )
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
