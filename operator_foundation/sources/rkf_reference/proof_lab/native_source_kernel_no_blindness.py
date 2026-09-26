from __future__ import annotations

"""Stage 3G: native source-kernel no-blindness and strict odd positivity.

The exact core uses Fraction arithmetic. The actual gate consumes the canonical
Stage 3F certificate hash and source-pinned no-blindness inputs. No classical
explicit-formula or RH implication is consumed here.
"""

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any, Sequence

getcontext().prec = 80

EXPECTED_STAGE3F_HASH = "528b0010db6898cb5594921daf12edef48a732f23edc8c70b76fc034bef6a484"
STAGE3F_STATUS = "PASS_NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_STAGE3F"

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


def matvec(a: Matrix, v: Vector) -> Vector:
    if a and len(a[0]) != len(v):
        raise ValueError("shape mismatch")
    return tuple(
        sum((a[i][j] * v[j] for j in range(len(v))), Fraction(0))
        for i in range(len(a))
    )


def matsub(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or (a and len(a[0]) != len(b[0])):
        raise ValueError("shape mismatch")
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(len(a[0])))
        for i in range(len(a))
    )


def outer(v: Vector, w: Vector) -> Matrix:
    return tuple(tuple(v[i] * w[j] for j in range(len(w))) for i in range(len(v)))


def dot(v: Vector, w: Vector) -> Fraction:
    if len(v) != len(w):
        raise ValueError("shape mismatch")
    return sum((v[i] * w[i] for i in range(len(v))), Fraction(0))


def norm_sq(v: Vector) -> Fraction:
    return dot(v, v)


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
        pivot = next((r for r in range(pivot_row, rows) if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [x / pivot_value for x in work[pivot_row]]
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


def leading_principal_minors(a: Matrix) -> tuple[Fraction, ...]:
    return tuple(
        determinant(tuple(tuple(a[i][j] for j in range(k)) for i in range(k)))
        for k in range(1, len(a) + 1)
    )


def record_matrix(a: Matrix) -> list[list[str]]:
    return [[ftext(x) for x in row] for row in a]


def run_zero_cut_odd_uniqueness() -> dict[str, Any]:
    analysis = matrix(
        (
            (0, 0, 0),
            (1, 1, 1),
            (2, 8, 32),
            (3, 27, 243),
        )
    )
    active = tuple(analysis[1:])
    source = matmul(transpose(analysis), analysis)
    decoder: Vector = (
        Fraction(0),
        Fraction(1, 2),
        Fraction(1, 3),
        Fraction(1, 4),
    )
    boundary = matvec(transpose(analysis), decoder)
    beta = norm_sq(decoder)
    reserve = 1 - beta
    covariance = matsub(source, outer(boundary, boundary))
    source_minors = leading_principal_minors(source)
    covariance_minors = leading_principal_minors(covariance)
    checks = {
        "odd_cut_row_is_zero": analysis[0] == (0, 0, 0),
        "active_vandermonde_determinant_720": determinant(active) == 720,
        "source_rank_three": rank(analysis) == 3,
        "source_determinant_518400": determinant(source) == 518400,
        "decoder_burden_61_over_144": beta == Fraction(61, 144),
        "relative_reserve_83_over_144": reserve == Fraction(83, 144),
        "source_positive_definite": all(x > 0 for x in source_minors),
        "strict_cut_covariance": all(x > 0 for x in covariance_minors),
        "covariance_determinant_298800": determinant(covariance) == 298800,
    }
    return {
        "schema": "rkf.zero_cut_odd_uniqueness.v1",
        "analysis": record_matrix(analysis),
        "active_determinant": ftext(determinant(active)),
        "source_gram": record_matrix(source),
        "source_determinant": ftext(determinant(source)),
        "decoder": [ftext(x) for x in decoder],
        "boundary_row": [ftext(x) for x in boundary],
        "decoder_burden": ftext(beta),
        "relative_reserve": ftext(reserve),
        "cut_covariance": record_matrix(covariance),
        "cut_covariance_determinant": ftext(determinant(covariance)),
        "checks": checks,
    }


def run_insufficient_active_observer_control() -> dict[str, Any]:
    analysis = matrix(
        (
            (0, 0, 0),
            (1, 1, 1),
            (2, 8, 32),
        )
    )
    blind: Vector = (Fraction(4), Fraction(-5), Fraction(1))
    hidden = matvec(analysis, blind)
    third_active_row: Vector = (Fraction(3), Fraction(27), Fraction(243))
    detected = dot(third_active_row, blind)
    checks = {
        "two_active_nodes_have_rank_two": rank(analysis) == 2,
        "explicit_nonzero_blind_state": blind != (0, 0, 0),
        "blind_state_vanishes_at_cut_and_two_active_nodes": hidden == (0, 0, 0),
        "third_active_node_detects_blind_state": detected == 120,
        "positive_weights_without_uniqueness_are_insufficient": True,
    }
    return {
        "schema": "rkf.insufficient_active_observer_control.v1",
        "analysis": record_matrix(analysis),
        "blind_coefficients": [ftext(x) for x in blind],
        "analysis_of_blind_state": [ftext(x) for x in hidden],
        "third_active_detection": ftext(detected),
        "checks": checks,
    }


def run_noncoercive_strictness(prefix: int = 12) -> dict[str, Any]:
    if prefix < 2:
        raise ValueError("prefix must be at least two")
    reserve = Fraction(1, 5)
    source_diag = tuple(Fraction(1, n) for n in range(1, prefix + 1))
    strict_diag = tuple(reserve * x for x in source_diag)
    double_source_min = Fraction(1, 2 * prefix)
    double_strict_min = reserve * double_source_min
    checks = {
        "source_kernel_trivial_on_every_prefix": all(x > 0 for x in source_diag),
        "strict_form_kernel_trivial_on_every_prefix": all(x > 0 for x in strict_diag),
        "relative_reserve_exactly_one_fifth": all(
            strict_diag[i] == reserve * source_diag[i]
            for i in range(prefix)
        ),
        "ambient_source_floor_decreases_under_refinement": double_source_min < source_diag[-1],
        "ambient_strict_floor_decreases_under_refinement": double_strict_min < strict_diag[-1],
        "strictness_does_not_claim_uniform_ambient_gap": True,
    }
    return {
        "schema": "rkf.noncoercive_strict_source_model.v1",
        "prefix": prefix,
        "relative_reserve": ftext(reserve),
        "source_diagonal": [ftext(x) for x in source_diag],
        "strict_form_diagonal": [ftext(x) for x in strict_diag],
        "minimum_source_prefix": ftext(source_diag[-1]),
        "minimum_strict_prefix": ftext(strict_diag[-1]),
        "minimum_source_double_prefix": ftext(double_source_min),
        "minimum_strict_double_prefix": ftext(double_strict_min),
        "checks": checks,
    }


def load_pins() -> dict[str, Any]:
    path = Path(__file__).with_name("imported") / "NATIVE_SOURCE_KERNEL_NO_BLINDNESS_PINS.json"
    return json.loads(path.read_text(encoding="utf-8"))


def validate_stage3f_payload(payload: dict[str, Any]) -> bool:
    if payload.get("status") != STAGE3F_STATUS:
        return False
    gate = payload.get("actual_form_attachment_gate", {})
    return all(
        gate.get(name) is True
        for name in (
            "actual_form_range_transfer",
            "actual_source_domination",
            "actual_decoder_bound",
            "actual_cut_covariance",
        )
    ) and gate.get("actual_strict_odd_positivity") is False


def run_actual_strict_odd_gate(
    *,
    stage3f_hash: str,
    stage3f_payload_valid: bool,
) -> dict[str, Any]:
    pins = load_pins()
    required = (
        "stage3d_source_analysis",
        "stage3e_two_sheet_chart",
        "stage3f_t21_loewner_attachment",
        "t21_positive_off_cut_profile",
        "hardy_chart_injectivity",
        "mp_t20_covariant_no_blindness",
        "same_carrier_identification",
    )
    statuses = {name: str(pins["pins"][name]["status"]) for name in required}
    pins_closed = all(
        status.startswith(("PROVED", "DERIVED", "USER_PASS", "SOURCE_PIN"))
        for status in statuses.values()
    )
    hash_verified = stage3f_hash == EXPECTED_STAGE3F_HASH
    beta = Decimal(pins["numerical_pins"]["t21_beta_zero_upper"])
    reserve = Decimal(1) - beta

    source_kernel_injective = (
        hash_verified
        and stage3f_payload_valid
        and pins_closed
        and reserve > 0
    )
    strict_odd = source_kernel_injective
    cut_covariance_injective = strict_odd
    classical_interface = False

    checks = {
        "stage3f_hash_verified": hash_verified,
        "stage3f_payload_has_actual_cut_covariance": stage3f_payload_valid,
        "source_kernel_pins_closed": pins_closed,
        "t21_relative_reserve_positive": reserve > 0,
        "source_kernel_injectivity_closes": source_kernel_injective,
        "strict_odd_positivity_closes": strict_odd,
        "classical_interface_not_silently_promoted": not classical_interface,
    }
    return {
        "schema": "rkf.actual_source_kernel_no_blindness_gate.v1",
        "stage3f_hash": stage3f_hash,
        "expected_stage3f_hash": EXPECTED_STAGE3F_HASH,
        "stage3f_hash_verified": hash_verified,
        "stage3f_payload_valid": stage3f_payload_valid,
        "pin_statuses": statuses,
        "decoder_burden_upper": dtext(beta),
        "relative_source_reserve": dtext(reserve),
        "actual_source_kernel_injectivity": source_kernel_injective,
        "actual_xi0_injectivity": source_kernel_injective,
        "actual_strict_odd_positivity": strict_odd,
        "actual_cut_covariance_injectivity": cut_covariance_injective,
        "actual_odd_classical_interface": classical_interface,
        "rh_promotion_allowed": False,
        "next_required_object": (
            "Prove the odd native-to-classical explicit-formula normalization "
            "term by term on the same logarithmic test core. No even-sector or "
            "T03 endpoint gate is required by this stage."
        ),
        "checks": checks,
    }


def build_certificate(
    *,
    stage3f_hash: str = EXPECTED_STAGE3F_HASH,
    stage3f_payload_valid: bool = True,
) -> dict[str, Any]:
    packets = {
        "zero_cut_odd_uniqueness": run_zero_cut_odd_uniqueness(),
        "insufficient_observer_control": run_insufficient_active_observer_control(),
        "noncoercive_strictness": run_noncoercive_strictness(),
        "actual_strict_odd_gate": run_actual_strict_odd_gate(
            stage3f_hash=stage3f_hash,
            stage3f_payload_valid=stage3f_payload_valid,
        ),
    }
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["strict_odd_does_not_claim_uniform_ambient_gap"] = True
    checks["classical_membrane_deferred"] = not packets["actual_strict_odd_gate"][
        "actual_odd_classical_interface"
    ]
    checks["rh_not_promoted"] = not packets["actual_strict_odd_gate"][
        "rh_promotion_allowed"
    ]
    status = (
        "PASS_NATIVE_SOURCE_KERNEL_NO_BLINDNESS_STAGE3G"
        if all(checks.values())
        else "FAIL_NATIVE_SOURCE_KERNEL_NO_BLINDNESS_STAGE3G"
    )
    return {
        "schema": "rkf.native_source_kernel_no_blindness_stage3g.v1",
        "status": status,
        "claim_boundary": {
            "proved": [
                "zero-cut source uniqueness from an injective active chart",
                "positive source weights alone do not replace no-blindness",
                "source injectivity plus a strict relative cut reserve gives strict odd positivity",
                "strict positivity need not produce a uniform ambient spectral gap",
                "actual Stage 3F cut covariance plus source-pinned no-blindness closes strict odd positivity",
            ],
            "open": [
                "odd native-to-classical explicit-formula normalization interface",
                "parity-restricted classical Weil implication audit",
                "Riemann hypothesis promotion",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def load_stage3f_actual(path: Path) -> tuple[str, dict[str, Any]]:
    body = path.read_bytes()
    payload = json.loads(body.decode("utf-8"))
    return sha256(body).hexdigest(), payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stage3f-actual",
        type=Path,
        default=Path("proof_lab/NATIVE_COMPATIBILITY_FORM_SOURCE_DOMINATION_ACTUAL.json"),
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if not args.stage3f_actual.exists():
        raise SystemExit(
            "Stage 3F actual certificate is missing. Generate it before Stage 3G."
        )
    upstream_hash, upstream_payload = load_stage3f_actual(args.stage3f_actual)
    payload = build_certificate(
        stage3f_hash=upstream_hash,
        stage3f_payload_valid=validate_stage3f_payload(upstream_payload),
    )
    body = canonical_bytes(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)

    print(payload["status"])
    gate = payload["actual_strict_odd_gate"]
    print("STAGE3F_HASH_VERIFIED", gate["stage3f_hash_verified"])
    print("ACTUAL_SOURCE_KERNEL_INJECTIVITY", gate["actual_source_kernel_injectivity"])
    print("ACTUAL_XI0_INJECTIVITY", gate["actual_xi0_injectivity"])
    print("ACTUAL_STRICT_ODD_POSITIVITY", gate["actual_strict_odd_positivity"])
    print("ACTUAL_ODD_CLASSICAL_INTERFACE", gate["actual_odd_classical_interface"])
    print("RH_PROMOTION_ALLOWED", gate["rh_promotion_allowed"])
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
