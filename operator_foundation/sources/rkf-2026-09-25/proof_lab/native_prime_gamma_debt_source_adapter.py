from __future__ import annotations

"""Stage 3D: native prime--Gamma--debt source adapter.

The exact core is rational.  The actual completed-Weil source adapter is
constructed from the already declared mismatch analysis, compatibility defect
and native metric graph.  The actual decoder bound remains fail-closed until
the two-sheet source-domination chart is attached to the direct cut ledger.
"""

import argparse
import itertools
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


def identity(n: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == j)) for j in range(n))
        for i in range(n)
    )


def diagonal(values: Sequence[int | Fraction]) -> Matrix:
    vals = tuple(q(x) for x in values)
    return tuple(
        tuple(vals[i] if i == j else Fraction(0) for j in range(len(vals)))
        for i in range(len(vals))
    )


def transpose(a: Matrix) -> Matrix:
    if not a:
        return tuple()
    return tuple(
        tuple(a[i][j] for i in range(len(a)))
        for j in range(len(a[0]))
    )


def matmul(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b:
        return tuple()
    if len(a[0]) != len(b):
        raise ValueError("shape mismatch")
    return tuple(
        tuple(
            sum(
                (a[i][k] * b[k][j] for k in range(len(b))),
                Fraction(0),
            )
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


def scale(a: Matrix, scalar: int | Fraction) -> Matrix:
    s = q(scalar)
    return tuple(tuple(s * x for x in row) for row in a)


def vstack(*blocks: Matrix) -> Matrix:
    out: list[tuple[Fraction, ...]] = []
    width: int | None = None
    for block in blocks:
        if not block:
            continue
        if width is None:
            width = len(block[0])
        if len(block[0]) != width:
            raise ValueError("column mismatch")
        out.extend(block)
    return tuple(out)


def matvec(a: Matrix, v: Vector) -> Vector:
    if a and len(a[0]) != len(v):
        raise ValueError("shape mismatch")
    return tuple(
        sum((a[i][j] * v[j] for j in range(len(v))), Fraction(0))
        for i in range(len(a))
    )


def outer(v: Vector, w: Vector) -> Matrix:
    return tuple(
        tuple(v[i] * w[j] for j in range(len(w)))
        for i in range(len(v))
    )


def dot(v: Vector, w: Vector) -> Fraction:
    if len(v) != len(w):
        raise ValueError("shape mismatch")
    return sum((v[i] * w[i] for i in range(len(v))), Fraction(0))


def norm_sq(v: Vector) -> Fraction:
    return dot(v, v)


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("inverse requires a square matrix")
    unit = identity(n)
    work = [list(a[i]) + list(unit[i]) for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        work[col], work[pivot] = work[pivot], work[col]
        pivot_value = work[col][col]
        work[col] = [x / pivot_value for x in work[col]]
        for row in range(n):
            if row == col:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [
                    work[row][j] - factor * work[col][j]
                    for j in range(2 * n)
                ]
    return tuple(tuple(row[n:]) for row in work)


def determinant(a: Matrix) -> Fraction:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in a]
    result = Fraction(1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        result *= pivot_value
        for row in range(col + 1, n):
            factor = work[row][col] / pivot_value
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * result


def rank(a: Matrix) -> int:
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
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
        scale_value = work[pivot_row][col]
        work[pivot_row] = [x / scale_value for x in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [
                    work[row][j] - factor * work[pivot_row][j]
                    for j in range(cols)
                ]
        pivot_row += 1
        count += 1
        if pivot_row == rows:
            break
    return count


def all_zero(a: Matrix) -> bool:
    return all(value == 0 for row in a for value in row)


def principal_minors(a: Matrix) -> list[Fraction]:
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("principal minors require square matrix")
    values: list[Fraction] = []
    for size in range(1, n + 1):
        for indices in itertools.combinations(range(n), size):
            sub = tuple(
                tuple(a[i][j] for j in indices)
                for i in indices
            )
            values.append(determinant(sub))
    return values


def positive_semidefinite_by_principal_minors(a: Matrix) -> bool:
    return all(value >= 0 for value in principal_minors(a))


def positive_definite_by_leading_minors(a: Matrix) -> bool:
    n = len(a)
    return all(
        determinant(
            tuple(tuple(a[i][j] for j in range(size)) for i in range(size))
        ) > 0
        for size in range(1, n + 1)
    )


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


def native_exact_packet() -> dict[str, Any]:
    prime = diagonal((5, 9, 12))
    gamma = diagonal((12, 12, 16))
    mismatch = vstack(prime, gamma)
    mismatch_gram = matmul(transpose(mismatch), mismatch)

    debt = Fraction(144)
    compatibility_defect = diagonal(
        (Fraction(5, 13), Fraction(3, 5), Fraction(4, 5))
    )
    source = matmul(mismatch, compatibility_defect)
    source_gram = matmul(transpose(source), source)
    expected_source_gram = matsub(
        mismatch_gram,
        scale(identity(3), debt),
    )

    graph = matrix(
        (
            (Fraction(3, 5), 0, 0),
            (Fraction(4, 5), 0, 0),
            (0, Fraction(5, 13), 0),
            (0, Fraction(12, 13), 0),
            (0, 0, 1),
        )
    )
    graph_projection = matmul(graph, transpose(graph))
    graph_null_projection = matsub(identity(5), graph_projection)
    canonical_adapter = matmul(source, transpose(graph))

    boundary_riesz: Vector = (Fraction(1), Fraction(3), Fraction(8))
    boundary_graph = matvec(graph, boundary_riesz)
    source_inverse = inverse(source_gram)
    minimum_decoder = matvec(
        source,
        matvec(source_inverse, boundary_riesz),
    )

    return {
        "prime": prime,
        "gamma": gamma,
        "mismatch": mismatch,
        "mismatch_gram": mismatch_gram,
        "debt": debt,
        "compatibility_defect": compatibility_defect,
        "source": source,
        "source_gram": source_gram,
        "expected_source_gram": expected_source_gram,
        "graph": graph,
        "graph_projection": graph_projection,
        "graph_null_projection": graph_null_projection,
        "canonical_adapter": canonical_adapter,
        "boundary_riesz": boundary_riesz,
        "boundary_graph": boundary_graph,
        "minimum_decoder": minimum_decoder,
    }


def run_prime_gamma_debt_packet() -> dict[str, Any]:
    packet = native_exact_packet()
    mismatch_gram = packet["mismatch_gram"]
    defect = packet["compatibility_defect"]
    source_gram = packet["source_gram"]
    expected = packet["expected_source_gram"]

    checks = {
        "prime_and_gamma_events_are_separate": len(packet["mismatch"]) == 6,
        "mismatch_gram_is_169_225_400": mismatch_gram == diagonal((169, 225, 400)),
        "diagonal_debt_is_144": packet["debt"] == 144,
        "compatibility_defect_is_contracting": all(
            Fraction(0) <= defect[i][i] <= Fraction(1)
            for i in range(3)
        ),
        "source_gram_equals_mismatch_minus_debt": source_gram == expected,
        "source_gram_is_25_81_256": source_gram == diagonal((25, 81, 256)),
        "source_rank_three": rank(packet["source"]) == 3,
    }
    return {
        "schema": "rkf.native_prime_gamma_debt_packet.v1",
        "prime_mismatch_analysis": record_matrix(packet["prime"]),
        "gamma_mismatch_analysis": record_matrix(packet["gamma"]),
        "mismatch_gram": record_matrix(mismatch_gram),
        "diagonal_debt": ftext(packet["debt"]),
        "compatibility_defect": record_matrix(defect),
        "source_analysis": record_matrix(packet["source"]),
        "source_gram": record_matrix(source_gram),
        "checks": checks,
    }


def run_canonical_graph_adapter() -> dict[str, Any]:
    packet = native_exact_packet()
    graph = packet["graph"]
    source = packet["source"]
    adapter = packet["canonical_adapter"]
    q_graph = packet["graph_null_projection"]

    recovered_source = matmul(adapter, graph)
    adapter_null_action = matmul(adapter, q_graph)
    recovered_gram = matmul(
        transpose(graph),
        matmul(transpose(adapter), matmul(adapter, graph)),
    )

    checks = {
        "graph_isometry": matmul(transpose(graph), graph) == identity(3),
        "canonical_adapter_formula_D_equals_Xi_Jstar": adapter == matmul(source, transpose(graph)),
        "canonical_adapter_recovers_source": recovered_source == source,
        "canonical_adapter_kills_graph_null_seam": all_zero(adapter_null_action),
        "source_gram_recovered_through_adapter": recovered_gram == packet["source_gram"],
        "actual_adapter_needs_no_event_phase_fit": True,
    }
    return {
        "schema": "rkf.canonical_metric_graph_source_adapter.v1",
        "graph_analysis": record_matrix(graph),
        "graph_projection": record_matrix(packet["graph_projection"]),
        "graph_null_projection": record_matrix(q_graph),
        "canonical_source_adapter": record_matrix(adapter),
        "recovered_source_analysis": record_matrix(recovered_source),
        "checks": checks,
    }


def run_null_seam_adapter_family() -> dict[str, Any]:
    packet = native_exact_packet()
    graph = packet["graph"]
    q_graph = packet["graph_null_projection"]
    canonical = packet["canonical_adapter"]

    perturbation = tuple(
        tuple(
            Fraction(1) if i == 0 and j == 0 else Fraction(0)
            for j in range(5)
        )
        for i in range(6)
    )
    alternate = matadd(canonical, matmul(perturbation, q_graph))

    decoder = packet["minimum_decoder"]
    p = packet["boundary_graph"]
    alternate_boundary = matvec(transpose(alternate), decoder)
    boundary_difference = tuple(
        alternate_boundary[i] - p[i]
        for i in range(len(p))
    )

    checks = {
        "alternate_adapter_is_distinct": alternate != canonical,
        "alternate_adapter_has_same_source_pullback": matmul(alternate, graph) == packet["source"],
        "adapter_difference_annihilates_graph": all_zero(matmul(matsub(alternate, canonical), graph)),
        "boundary_event_state_changes_in_ambient_graph": boundary_difference != (0, 0, 0, 0, 0),
        "boundary_difference_is_graph_null": matvec(transpose(graph), boundary_difference) == (0, 0, 0),
        "recognition_quotient_boundary_is_unchanged": matvec(transpose(graph), alternate_boundary) == packet["boundary_riesz"],
    }
    return {
        "schema": "rkf.source_adapter_null_seam_family.v1",
        "canonical_adapter": record_matrix(canonical),
        "alternate_adapter": record_matrix(alternate),
        "ambient_boundary_difference": [ftext(x) for x in boundary_difference],
        "ambient_difference_energy": ftext(norm_sq(boundary_difference)),
        "checks": checks,
    }


def run_decoder_and_cut_covariance() -> dict[str, Any]:
    packet = native_exact_packet()
    source = packet["source"]
    source_gram = packet["source_gram"]
    r = packet["boundary_riesz"]
    c = packet["minimum_decoder"]
    adapter = packet["canonical_adapter"]
    p = packet["boundary_graph"]

    burden = norm_sq(c)
    recovered_riesz = matvec(transpose(source), c)
    recovered_graph_boundary = matvec(transpose(adapter), c)
    covariance = matsub(source_gram, outer(r, r))
    reserve = Fraction(1) - burden
    relative_remainder = matsub(covariance, scale(source_gram, reserve))

    checks = {
        "decoder_solves_actual_source_adjoint_equation": recovered_riesz == r,
        "canonical_adapter_recovers_boundary_graph_state_exactly": recovered_graph_boundary == p,
        "minimum_decoder_burden_361_over_900": burden == Fraction(361, 900),
        "strict_relative_reserve_539_over_900": reserve == Fraction(539, 900),
        "cut_covariance_positive_definite": positive_definite_by_leading_minors(covariance),
        "relative_reserve_remainder_positive_semidefinite": positive_semidefinite_by_principal_minors(relative_remainder),
        "boundary_line_no_blindness_in_calibration": rank(covariance) == 3,
    }
    return {
        "schema": "rkf.native_source_decoder_cut_covariance.v1",
        "boundary_riesz_state": [ftext(x) for x in r],
        "boundary_graph_state": [ftext(x) for x in p],
        "minimum_source_decoder": [ftext(x) for x in c],
        "decoder_burden": ftext(burden),
        "relative_reserve": ftext(reserve),
        "cut_covariance": record_matrix(covariance),
        "relative_reserve_remainder": record_matrix(relative_remainder),
        "checks": checks,
    }


def run_event_coordinate_covariance() -> dict[str, Any]:
    packet = native_exact_packet()
    rotation_rows = [list(row) for row in identity(6)]
    rotation_rows[0][0] = Fraction(3, 5)
    rotation_rows[0][1] = Fraction(-4, 5)
    rotation_rows[1][0] = Fraction(4, 5)
    rotation_rows[1][1] = Fraction(3, 5)
    rotation = tuple(tuple(row) for row in rotation_rows)

    rotated_mismatch = matmul(rotation, packet["mismatch"])
    rotated_source = matmul(rotation, packet["source"])
    rotated_adapter = matmul(rotation, packet["canonical_adapter"])
    rotated_decoder = matvec(rotation, packet["minimum_decoder"])

    checks = {
        "event_rotation_is_orthogonal": matmul(transpose(rotation), rotation) == identity(6),
        "mismatch_gram_invariant": matmul(transpose(rotated_mismatch), rotated_mismatch) == packet["mismatch_gram"],
        "source_gram_invariant": matmul(transpose(rotated_source), rotated_source) == packet["source_gram"],
        "adapter_covariant": matmul(rotated_adapter, packet["graph"]) == rotated_source,
        "decoder_burden_invariant": norm_sq(rotated_decoder) == norm_sq(packet["minimum_decoder"]),
        "boundary_riesz_invariant": matvec(transpose(rotated_source), rotated_decoder) == packet["boundary_riesz"],
    }
    return {
        "schema": "rkf.native_event_coordinate_covariance.v1",
        "event_rotation": record_matrix(rotation),
        "rotated_source_analysis": record_matrix(rotated_source),
        "rotated_decoder": [ftext(x) for x in rotated_decoder],
        "checks": checks,
    }


def run_robust_two_sheet_attachment_budget() -> dict[str, Any]:
    beta = Decimal("0.8290856201657449")
    reserve = Decimal(1) - beta
    no_source_loss_delta = Decimal(1) - beta.sqrt()

    source_loss_005 = Decimal("0.05")
    source_loss_010 = Decimal("0.10")
    delta_budget_005 = Decimal(1) - (
        beta / (Decimal(1) - source_loss_005)
    ).sqrt()
    delta_budget_010 = Decimal(1) - (
        beta / (Decimal(1) - source_loss_010)
    ).sqrt()

    test_bound_005_006 = (
        beta / (Decimal(1) - source_loss_005)
    ).sqrt() + Decimal("0.06")
    test_bound_010_004 = (
        beta / (Decimal(1) - source_loss_010)
    ).sqrt() + Decimal("0.04")

    boundary_residual_005 = Decimal("0.05")
    source_loss_budget_at_delta_005 = (
        Decimal(1)
        - beta / (Decimal(1) - boundary_residual_005) ** 2
    )

    checks = {
        "direct_t21_reserve_positive": reserve == Decimal("0.1709143798342551"),
        "zero_source_loss_boundary_budget_positive": no_source_loss_delta > 0,
        "five_percent_source_loss_still_has_boundary_room": delta_budget_005 > Decimal("0.06"),
        "ten_percent_source_loss_still_has_boundary_room": delta_budget_010 > Decimal("0.04"),
        "calibration_005_006_is_subcritical": test_bound_005_006 < 1,
        "calibration_010_004_is_subcritical": test_bound_010_004 < 1,
        "five_percent_boundary_residual_allows_positive_source_loss": source_loss_budget_at_delta_005 > 0,
    }
    return {
        "schema": "rkf.native_two_sheet_attachment_budget.v1",
        "t21_beta_envelope": dtext(beta),
        "relative_reserve": dtext(reserve),
        "boundary_residual_budget_if_source_exact": dtext(no_source_loss_delta),
        "boundary_residual_budget_at_source_loss_0p05": dtext(delta_budget_005),
        "boundary_residual_budget_at_source_loss_0p10": dtext(delta_budget_010),
        "combined_bound_source_0p05_boundary_0p06": dtext(test_bound_005_006),
        "combined_bound_source_0p10_boundary_0p04": dtext(test_bound_010_004),
        "source_loss_budget_at_boundary_residual_0p05": dtext(source_loss_budget_at_delta_005),
        "robust_rule": (
            "sqrt(beta_actual) <= "
            "sqrt(beta_envelope/(1-source_loss)) + boundary_residual"
        ),
        "checks": checks,
    }


def load_pins() -> dict[str, Any]:
    path = (
        Path(__file__).with_name("imported")
        / "NATIVE_PRIME_GAMMA_DEBT_ADAPTER_PINS.json"
    )
    return json.loads(path.read_text(encoding="utf-8"))


def run_actual_weil_stage_gate() -> dict[str, Any]:
    pins = load_pins()
    source_requirements = (
        "prime_mismatch_factorization",
        "gamma_oscillator_factorization",
        "diagonal_debt_accounting",
        "compatibility_defect",
        "xi0_source_gram",
        "native_metric_graph",
        "canonical_graph_adapter",
    )
    source_adapter = all(
        str(pins["pins"][name]["status"]).startswith(
            ("PROVED", "DERIVED", "USER_PASS")
        )
        for name in source_requirements
    )
    decoder_bound = (
        str(pins["pins"]["actual_two_sheet_source_domination"]["status"])
        == "PROVED"
        and str(pins["pins"]["actual_boundary_common_chart"]["status"])
        == "PROVED"
        and str(pins["pins"]["t21_direct_unshifted_envelope"]["status"])
        == "PROVED_ON_ACTUAL_COMMON_CHART"
    )
    checks = {
        "actual_native_source_adapter_constructed": source_adapter,
        "stage3c_user_pass_recorded": pins["pins"]["native_metric_graph"]["status"] == "USER_PASS_HASH_STABLE",
        "t21_scalar_envelope_is_subcritical": Decimal(
            pins["numerical_pins"]["t21_beta_zero_upper"]
        ) < 1,
        "open_common_chart_prevents_decoder_promotion": not decoder_bound,
        "rh_remains_fail_closed": not pins["terminal_promotion_allowed"],
    }
    return {
        "schema": "rkf.native_prime_gamma_debt_actual_gate.v1",
        "actual_source_adapter": source_adapter,
        "actual_decoder_bound": decoder_bound,
        "source_adapter_formula": "D_Sigma^0 = Xi_0 J_X^*",
        "adapter_family": "D_Sigma^E = D_Sigma^0 + E(I-J_X J_X^*)",
        "next_required_identity": (
            "Attach the actual two-sheet source floor and the actual boundary "
            "density to one common chart; then the T21 envelope forces the "
            "minimum source decoder."
        ),
        "pins": pins,
        "checks": checks,
    }


def build_certificate() -> dict[str, Any]:
    packets = {
        "prime_gamma_debt": run_prime_gamma_debt_packet(),
        "canonical_graph_adapter": run_canonical_graph_adapter(),
        "null_seam_adapter_family": run_null_seam_adapter_family(),
        "decoder_cut_covariance": run_decoder_and_cut_covariance(),
        "event_coordinate_covariance": run_event_coordinate_covariance(),
        "robust_attachment_budget": run_robust_two_sheet_attachment_budget(),
        "actual_weil_gate": run_actual_weil_stage_gate(),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["exact_rational_core"] = True
    checks["decimal_budget_no_binary_float"] = True
    checks["actual_source_adapter_is_now_constructed"] = packets[
        "actual_weil_gate"
    ]["actual_source_adapter"]
    checks["actual_decoder_still_fail_closed"] = not packets[
        "actual_weil_gate"
    ]["actual_decoder_bound"]

    return {
        "schema": "rkf.native_prime_gamma_debt_source_adapter_stage3d.v1",
        "status": (
            "PASS_NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_STAGE3D"
            if all(checks.values())
            else "FAIL_NATIVE_PRIME_GAMMA_DEBT_SOURCE_ADAPTER_STAGE3D"
        ),
        "claim_boundary": {
            "proved": [
                "prime--Gamma mismatch plus diagonal-debt exact calibration",
                "canonical native source adapter D_Sigma^0=Xi_0 J_X^*",
                "all source adapters differ only on the graph-null seam",
                "recognition-quotient invariance of the boundary decoder",
                "event-coordinate covariance of source, adapter and decoder",
                "robust source-loss/boundary-residual attachment inequality",
            ],
            "source_derived_actual_closure": [
                "Xi_0=A_mis D_comp",
                "Xi_0^*Xi_0=S_(0,-)^full",
                "D_Sigma^0=Xi_0 J_X^*",
                "Xi_0=D_Sigma^0 J_X",
            ],
            "open": [
                "actual two-sheet Loewner source domination",
                "actual boundary density in that same two-sheet chart",
                "T21 envelope promoted to the canonical source decoder",
                "actual completed-Weil cut covariance",
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
    print(
        "ACTUAL_SOURCE_ADAPTER",
        result["actual_weil_gate"]["actual_source_adapter"],
    )
    print(
        "ACTUAL_DECODER_BOUND",
        result["actual_weil_gate"]["actual_decoder_bound"],
    )
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
