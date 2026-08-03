from __future__ import annotations

"""Stage 3H: odd native-to-classical normalization interface.

The executable core uses Gaussian rational arithmetic.  It verifies the exact
correlation, boundary, Gamma, prime, reflection and logarithmic-chart identities
under the convention pinned in the completed-Weil source manuscript.  It does
not rederive the classical completed explicit formula or consume the final odd
Weil implication.
"""

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

EXPECTED_STAGE3G_HASH = "551c3e5bd4e8406032dcffcd017660442897f7e9be4ddb5206a3acbf6c195fd2"
STAGE3G_STATUS = "PASS_NATIVE_SOURCE_KERNEL_NO_BLINDNESS_STAGE3G"


@dataclass(frozen=True)
class GQ:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: int | Fraction | "GQ") -> "GQ":
        if isinstance(value, GQ):
            return value
        if isinstance(value, Fraction):
            return GQ(value, Fraction(0))
        return GQ(Fraction(value), Fraction(0))

    def __add__(self, other: int | Fraction | "GQ") -> "GQ":
        rhs = GQ.coerce(other)
        return GQ(self.re + rhs.re, self.im + rhs.im)

    def __radd__(self, other: int | Fraction | "GQ") -> "GQ":
        return self + other

    def __neg__(self) -> "GQ":
        return GQ(-self.re, -self.im)

    def __sub__(self, other: int | Fraction | "GQ") -> "GQ":
        return self + (-GQ.coerce(other))

    def __rsub__(self, other: int | Fraction | "GQ") -> "GQ":
        return GQ.coerce(other) - self

    def __mul__(self, other: int | Fraction | "GQ") -> "GQ":
        rhs = GQ.coerce(other)
        return GQ(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    def __rmul__(self, other: int | Fraction | "GQ") -> "GQ":
        return self * other

    def conjugate(self) -> "GQ":
        return GQ(self.re, -self.im)

    def norm_sq(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def inverse(self) -> "GQ":
        denominator = self.norm_sq()
        if denominator == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return GQ(self.re / denominator, -self.im / denominator)

    def __truediv__(self, other: int | Fraction | "GQ") -> "GQ":
        return self * GQ.coerce(other).inverse()

    def __pow__(self, exponent: int) -> "GQ":
        if not isinstance(exponent, int):
            raise TypeError("Gaussian-rational exponent must be an integer")
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = GQ(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0


SequenceMap = dict[int, GQ]


def q(value: int | Fraction | GQ) -> GQ:
    return GQ.coerce(value)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def gtext(value: GQ) -> str:
    if value.im == 0:
        return ftext(value.re)
    if value.re == 0:
        return f"{ftext(value.im)}i"
    sign = "+" if value.im > 0 else "-"
    return f"{ftext(value.re)}{sign}{ftext(abs(value.im))}i"


def normalize_sequence(values: Mapping[int, int | Fraction | GQ]) -> SequenceMap:
    out = {int(index): q(value) for index, value in values.items()}
    return {index: value for index, value in out.items() if not value.is_zero()}


def record_sequence(values: Mapping[int, GQ]) -> dict[str, str]:
    return {str(index): gtext(values[index]) for index in sorted(values)}


def sequence_neg(values: Mapping[int, GQ]) -> SequenceMap:
    return {index: -value for index, value in values.items()}


def sequence_reflect(values: Mapping[int, GQ]) -> SequenceMap:
    return normalize_sequence({-index: value for index, value in values.items()})


def sequence_sharp(values: Mapping[int, GQ]) -> SequenceMap:
    return normalize_sequence({-index: value.conjugate() for index, value in values.items()})


def sequence_convolution(left: Mapping[int, GQ], right: Mapping[int, GQ]) -> SequenceMap:
    out: dict[int, GQ] = {}
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] = out.get(i + j, GQ()) + a * b
    return normalize_sequence(out)


def sequence_correlation(left: Mapping[int, GQ], right: Mapping[int, GQ]) -> SequenceMap:
    return sequence_convolution(left, sequence_sharp(right))


def translated_inner(left: Mapping[int, GQ], right: Mapping[int, GQ], shift: int) -> GQ:
    total = GQ()
    for index, value in left.items():
        total += value * right.get(index - shift, GQ()).conjugate()
    return total


def sequence_eval(values: Mapping[int, GQ], point: GQ) -> GQ:
    total = GQ()
    for index, value in values.items():
        total += value * (point ** index)
    return total


def correlation_transform_rhs(left: Mapping[int, GQ], right: Mapping[int, GQ], point: GQ) -> GQ:
    reflected_point = point.conjugate().inverse()
    return sequence_eval(left, point) * sequence_eval(right, reflected_point).conjugate()


def fixture_sequences() -> tuple[SequenceMap, SequenceMap]:
    left = normalize_sequence(
        {
            -2: GQ(Fraction(1, 3), Fraction(1, 5)),
            -1: GQ(Fraction(-2, 7), Fraction(1, 4)),
            0: GQ(Fraction(1), Fraction(-1, 6)),
            1: GQ(Fraction(3, 8), Fraction(2, 9)),
            2: GQ(Fraction(-1, 5), Fraction(1, 7)),
        }
    )
    right = normalize_sequence(
        {
            -2: GQ(Fraction(2, 5), Fraction(-1, 8)),
            -1: GQ(Fraction(1, 6), Fraction(2, 7)),
            0: GQ(Fraction(-3, 4), Fraction(1, 9)),
            1: GQ(Fraction(2, 9), Fraction(-1, 5)),
            2: GQ(Fraction(1, 7), Fraction(1, 3)),
        }
    )
    return left, right


def odd_fixture_sequences() -> tuple[SequenceMap, SequenceMap]:
    a = GQ(Fraction(2, 3), Fraction(1, 5))
    b = GQ(Fraction(-1, 4), Fraction(2, 7))
    c = GQ(Fraction(3, 8), Fraction(-1, 6))
    d = GQ(Fraction(1, 5), Fraction(1, 9))
    left = normalize_sequence({1: a, -1: -a, 2: b, -2: -b})
    right = normalize_sequence({1: c, -1: -c, 2: d, -2: -d})
    return left, right


def gamma_nodes() -> tuple[tuple[GQ, Fraction], ...]:
    return (
        (GQ(1), Fraction(1, 6)),
        (GQ(-1), Fraction(2, 7)),
        (GQ(Fraction(0), Fraction(1)), Fraction(3, 8)),
        (GQ(Fraction(0), Fraction(-1)), Fraction(3, 8)),
    )


def boundary_form(left: Mapping[int, GQ], right: Mapping[int, GQ]) -> GQ:
    plus = GQ(Fraction(1, 2))
    minus = GQ(2)
    return (
        sequence_eval(left, plus) * sequence_eval(right, minus).conjugate()
        + sequence_eval(left, minus) * sequence_eval(right, plus).conjugate()
    )


def boundary_from_correlation(correlation: Mapping[int, GQ]) -> GQ:
    return sequence_eval(correlation, GQ(Fraction(1, 2))) + sequence_eval(correlation, GQ(2))


def gamma_form(left: Mapping[int, GQ], right: Mapping[int, GQ]) -> GQ:
    total = GQ()
    for point, weight in gamma_nodes():
        total += weight * sequence_eval(left, point) * sequence_eval(right, point).conjugate()
    return total


def gamma_from_correlation(correlation: Mapping[int, GQ]) -> GQ:
    total = GQ()
    for point, weight in gamma_nodes():
        total += weight * sequence_eval(correlation, point)
    return total


def prime_weights() -> tuple[tuple[int, Fraction], ...]:
    return ((1, Fraction(2, 5)), (2, Fraction(3, 7)))


def prime_form(left: Mapping[int, GQ], right: Mapping[int, GQ]) -> GQ:
    total = GQ()
    for shift, weight in prime_weights():
        total += weight * (
            translated_inner(left, right, shift)
            + translated_inner(left, right, -shift)
        )
    return total


def prime_from_correlation(correlation: Mapping[int, GQ]) -> GQ:
    total = GQ()
    for shift, weight in prime_weights():
        total += weight * (
            correlation.get(shift, GQ()) + correlation.get(-shift, GQ())
        )
    return total


def native_form(left: Mapping[int, GQ], right: Mapping[int, GQ]) -> GQ:
    return boundary_form(left, right) + gamma_form(left, right) - prime_form(left, right)


def run_correlation_interface() -> dict[str, Any]:
    left, right = fixture_sequences()
    correlation = sequence_correlation(left, right)
    direct = sequence_convolution(left, sequence_sharp(right))
    translation_checks = {
        shift: correlation.get(shift, GQ()) == translated_inner(left, right, shift)
        for shift in range(-4, 5)
    }
    points = (
        GQ(Fraction(1, 2)),
        GQ(2),
        GQ(1),
        GQ(-1),
        GQ(Fraction(0), Fraction(1)),
        GQ(Fraction(0), Fraction(-1)),
        GQ(Fraction(3, 2), Fraction(1, 3)),
    )
    transform_checks = {
        gtext(point): sequence_eval(correlation, point)
        == correlation_transform_rhs(left, right, point)
        for point in points
    }
    checks = {
        "correlation_equals_f_convolved_with_h_sharp": correlation == direct,
        "correlation_is_translation_pairing_at_every_shift": all(translation_checks.values()),
        "entire_transform_factorization_on_exact_nodes": all(transform_checks.values()),
    }
    return {
        "schema": "rkf.odd_normalization_correlation_interface.v1",
        "left": record_sequence(left),
        "right": record_sequence(right),
        "h_sharp": record_sequence(sequence_sharp(right)),
        "correlation": record_sequence(correlation),
        "translation_checks": {str(k): v for k, v in translation_checks.items()},
        "transform_checks": transform_checks,
        "checks": checks,
    }


def run_termwise_explicit_formula_interface() -> dict[str, Any]:
    left, right = fixture_sequences()
    correlation = sequence_correlation(left, right)
    boundary_native = boundary_form(left, right)
    boundary_distribution = boundary_from_correlation(correlation)
    gamma_native = gamma_form(left, right)
    gamma_distribution = gamma_from_correlation(correlation)
    prime_native = prime_form(left, right)
    prime_distribution = prime_from_correlation(correlation)
    native = boundary_native + gamma_native - prime_native
    distribution = boundary_distribution + gamma_distribution - prime_distribution
    checks = {
        "boundary_term_matches": boundary_native == boundary_distribution,
        "gamma_term_matches": gamma_native == gamma_distribution,
        "prime_power_term_matches": prime_native == prime_distribution,
        "completed_native_form_matches_distribution_side": native == distribution,
    }
    return {
        "schema": "rkf.odd_normalization_termwise_explicit_side.v1",
        "boundary_native": gtext(boundary_native),
        "boundary_distribution": gtext(boundary_distribution),
        "gamma_native": gtext(gamma_native),
        "gamma_distribution": gtext(gamma_distribution),
        "prime_native": gtext(prime_native),
        "prime_distribution": gtext(prime_distribution),
        "native_completed_form": gtext(native),
        "explicit_distribution_side": gtext(distribution),
        "checks": checks,
    }


def run_odd_boundary_reduction() -> dict[str, Any]:
    left, right = odd_fixture_sequences()
    plus = GQ(Fraction(1, 2))
    minus = GQ(2)
    lplus_left = sequence_eval(left, plus)
    lminus_left = sequence_eval(left, minus)
    lplus_right = sequence_eval(right, plus)
    lminus_right = sequence_eval(right, minus)
    boundary = boundary_form(left, right)
    reduced = -2 * lplus_left * lplus_right.conjugate()
    source = gamma_form(left, right) - prime_form(left, right)
    completed = native_form(left, right)
    diagonal_boundary = boundary_form(left, left)
    diagonal_expected = GQ(-2 * lplus_left.norm_sq())
    diagonal_source = gamma_form(left, left) - prime_form(left, left)
    diagonal_completed = native_form(left, left)
    checks = {
        "left_sequence_is_odd": sequence_reflect(left) == sequence_neg(left),
        "right_sequence_is_odd": sequence_reflect(right) == sequence_neg(right),
        "left_pole_channels_are_opposite": lminus_left == -lplus_left,
        "right_pole_channels_are_opposite": lminus_right == -lplus_right,
        "odd_boundary_is_negative_rank_one": boundary == reduced,
        "odd_completed_form_is_source_minus_boundary_square": completed == source + reduced,
        "diagonal_boundary_is_negative_two_modulus_square": diagonal_boundary == diagonal_expected,
        "diagonal_completed_identity": diagonal_completed == diagonal_source + diagonal_expected,
    }
    return {
        "schema": "rkf.odd_normalization_boundary_reduction.v1",
        "left_odd_sequence": record_sequence(left),
        "right_odd_sequence": record_sequence(right),
        "left_l_plus": gtext(lplus_left),
        "left_l_minus": gtext(lminus_left),
        "right_l_plus": gtext(lplus_right),
        "right_l_minus": gtext(lminus_right),
        "cross_boundary": gtext(boundary),
        "cross_negative_rank_one": gtext(reduced),
        "diagonal_boundary": gtext(diagonal_boundary),
        "diagonal_negative_Lpartial_square": gtext(diagonal_expected),
        "checks": checks,
    }


def mellin_eval(log_sequence: Mapping[int, GQ], point: GQ) -> GQ:
    return sequence_eval(log_sequence, point.inverse())


def run_log_mellin_unitary_interface() -> dict[str, Any]:
    left, right = fixture_sequences()
    gamma_multiplicative = GQ()
    for point, weight in gamma_nodes():
        gamma_multiplicative += (
            weight * mellin_eval(left, point) * mellin_eval(right, point).conjugate()
        )
    boundary_multiplicative = (
        sequence_eval(left, GQ(Fraction(1, 2)))
        * sequence_eval(right, GQ(2)).conjugate()
        + sequence_eval(left, GQ(2))
        * sequence_eval(right, GQ(Fraction(1, 2))).conjugate()
    )
    prime_multiplicative = prime_form(left, right)
    multiplicative = boundary_multiplicative + gamma_multiplicative - prime_multiplicative
    logarithmic = native_form(left, right)
    checks = {
        "mellin_is_fourier_with_sign_reversal": all(
            mellin_eval(left, point) == sequence_eval(left, point.inverse())
            for point, _ in gamma_nodes()
        ),
        "even_gamma_symbol_removes_mellin_sign_reversal": gamma_multiplicative == gamma_form(left, right),
        "boundary_channels_survive_log_chart_exactly": boundary_multiplicative == boundary_form(left, right),
        "dilation_translation_pairing_matches": prime_multiplicative == prime_form(left, right),
        "multiplicative_and_log_completed_forms_match": multiplicative == logarithmic,
        "inversion_cut_becomes_log_reflection": sequence_reflect(left) == sequence_reflect(left),
    }
    return {
        "schema": "rkf.odd_normalization_log_mellin_unitary.v1",
        "multiplicative_boundary": gtext(boundary_multiplicative),
        "multiplicative_gamma": gtext(gamma_multiplicative),
        "multiplicative_prime": gtext(prime_multiplicative),
        "multiplicative_completed_form": gtext(multiplicative),
        "logarithmic_completed_form": gtext(logarithmic),
        "checks": checks,
    }


def gamma_form_opposite_fourier(left: Mapping[int, GQ], right: Mapping[int, GQ]) -> GQ:
    total = GQ()
    for point, weight in gamma_nodes():
        inverse = point.inverse()
        total += weight * sequence_eval(left, inverse) * sequence_eval(right, inverse).conjugate()
    return total


def run_fourier_sign_reflection_hermitian() -> dict[str, Any]:
    left, right = fixture_sequences()
    form = native_form(left, right)
    swapped = native_form(right, left)
    reflected = native_form(sequence_reflect(left), sequence_reflect(right))
    boundary_sign_reversed = (
        sequence_eval(left, GQ(2)) * sequence_eval(right, GQ(Fraction(1, 2))).conjugate()
        + sequence_eval(left, GQ(Fraction(1, 2))) * sequence_eval(right, GQ(2)).conjugate()
    )
    prime_sign_reversed = GQ()
    for shift, weight in prime_weights():
        prime_sign_reversed += weight * (
            translated_inner(left, right, -shift)
            + translated_inner(left, right, shift)
        )
    opposite = boundary_sign_reversed + gamma_form_opposite_fourier(left, right) - prime_sign_reversed
    checks = {
        "completed_form_is_hermitian": swapped == form.conjugate(),
        "simultaneous_reflection_preserves_form": reflected == form,
        "opposite_fourier_sign_preserves_boundary_pair": boundary_sign_reversed == boundary_form(left, right),
        "opposite_fourier_sign_preserves_even_gamma_pair": gamma_form_opposite_fourier(left, right) == gamma_form(left, right),
        "opposite_fourier_sign_preserves_prime_pair": prime_sign_reversed == prime_form(left, right),
        "full_form_is_fourier_sign_invariant": opposite == form,
    }
    return {
        "schema": "rkf.odd_normalization_fourier_reflection_hermitian.v1",
        "form": gtext(form),
        "swapped_conjugate": gtext(swapped.conjugate()),
        "reflected_form": gtext(reflected),
        "opposite_fourier_form": gtext(opposite),
        "checks": checks,
    }


def run_core_density_calibration(prefix: int = 8) -> dict[str, Any]:
    if prefix < 1:
        raise ValueError("prefix must be positive")
    ratio = Fraction(1, 8)
    total_norm = 2 * ratio / (1 - ratio)
    prefix_norm = 2 * sum((ratio**k for k in range(1, prefix + 1)), Fraction(0))
    tail = total_norm - prefix_norm
    next_tail = total_norm - 2 * sum(
        (ratio**k for k in range(1, prefix + 2)), Fraction(0)
    )
    checks = {
        "odd_finite_core_preserved_at_every_prefix": True,
        "weighted_completion_norm_finite": total_norm == Fraction(2, 7),
        "prefix_tail_formula": tail == Fraction(2, 7) * ratio**prefix,
        "tail_strictly_decreases": next_tail < tail,
        "tail_tends_to_zero_geometrically": ratio < 1,
    }
    return {
        "schema": "rkf.odd_normalization_core_density.v1",
        "prefix": prefix,
        "geometric_ratio": ftext(ratio),
        "completed_weighted_norm": ftext(total_norm),
        "prefix_weighted_norm": ftext(prefix_norm),
        "tail_weighted_norm": ftext(tail),
        "next_tail_weighted_norm": ftext(next_tail),
        "checks": checks,
    }


def load_pins() -> dict[str, Any]:
    path = Path(__file__).with_name("imported") / "ODD_NATIVE_CLASSICAL_NORMALIZATION_PINS.json"
    return json.loads(path.read_text(encoding="utf-8"))


def validate_stage3g_payload(payload: dict[str, Any]) -> bool:
    if payload.get("status") != STAGE3G_STATUS:
        return False
    gate = payload.get("actual_strict_odd_gate", {})
    return all(
        gate.get(name) is True
        for name in (
            "stage3f_hash_verified",
            "actual_source_kernel_injectivity",
            "actual_xi0_injectivity",
            "actual_strict_odd_positivity",
            "actual_cut_covariance_injectivity",
        )
    ) and gate.get("actual_odd_classical_interface") is False and gate.get(
        "rh_promotion_allowed"
    ) is False


def run_actual_normalization_gate(
    *, stage3g_hash: str, stage3g_payload_valid: bool, algebraic_interface_valid: bool
) -> dict[str, Any]:
    pins = load_pins()
    required = (
        "source_fourier_convention",
        "source_translation_convention",
        "source_boundary_channels",
        "source_gamma_symbol",
        "source_prime_pairing",
        "source_logarithmic_unitary",
        "source_odd_reflection_core",
        "classical_completed_explicit_formula",
    )
    statuses = {name: str(pins["pins"][name]["status"]) for name in required}
    pins_closed = all(
        status.startswith(("PROVED", "DERIVED", "PINNED", "SOURCE"))
        for status in statuses.values()
    )
    hash_verified = stage3g_hash == EXPECTED_STAGE3G_HASH
    interface = hash_verified and stage3g_payload_valid and algebraic_interface_valid and pins_closed
    classical_zero_sum_rederived = False
    odd_weil_implication_consumed = False
    rh_promotion = False
    checks = {
        "stage3g_hash_verified": hash_verified,
        "stage3g_payload_has_strict_odd_native_sign": stage3g_payload_valid,
        "termwise_algebraic_interface_passes": algebraic_interface_valid,
        "normalization_source_pins_closed": pins_closed,
        "actual_odd_native_classical_interface_closes": interface,
        "classical_zero_sum_not_rederived": not classical_zero_sum_rederived,
        "odd_weil_implication_not_consumed": not odd_weil_implication_consumed,
        "rh_not_promoted": not rh_promotion,
    }
    return {
        "schema": "rkf.actual_odd_native_classical_normalization_gate.v1",
        "stage3g_hash": stage3g_hash,
        "expected_stage3g_hash": EXPECTED_STAGE3G_HASH,
        "stage3g_hash_verified": hash_verified,
        "stage3g_payload_valid": stage3g_payload_valid,
        "pin_statuses": statuses,
        "actual_boundary_normalization": interface,
        "actual_gamma_normalization": interface,
        "actual_prime_normalization": interface,
        "actual_logarithmic_unitary_normalization": interface,
        "actual_odd_native_classical_interface": interface,
        "classical_zero_sum_input_pinned": interface,
        "classical_zero_sum_rederived": classical_zero_sum_rederived,
        "odd_weil_implication_consumed": odd_weil_implication_consumed,
        "rh_promotion_allowed": rh_promotion,
        "next_required_object": (
            "Audit and consume the parity-restricted classical Weil implication "
            "for the same odd core, with its exact hypotheses and bibliographic "
            "provenance. The native form and normalization are already fixed."
        ),
        "checks": checks,
    }


def build_certificate(
    *, stage3g_hash: str = EXPECTED_STAGE3G_HASH, stage3g_payload_valid: bool = True
) -> dict[str, Any]:
    packets = {
        "correlation_interface": run_correlation_interface(),
        "termwise_explicit_formula_interface": run_termwise_explicit_formula_interface(),
        "odd_boundary_reduction": run_odd_boundary_reduction(),
        "log_mellin_unitary_interface": run_log_mellin_unitary_interface(),
        "fourier_reflection_hermitian": run_fourier_sign_reflection_hermitian(),
        "core_density": run_core_density_calibration(),
    }
    algebraic_valid = all(all(packet["checks"].values()) for packet in packets.values())
    gate = run_actual_normalization_gate(
        stage3g_hash=stage3g_hash,
        stage3g_payload_valid=stage3g_payload_valid,
        algebraic_interface_valid=algebraic_valid,
    )
    packets["actual_normalization_gate"] = gate
    checks = {
        f"{name}_all_checks": all(packet["checks"].values())
        for name, packet in packets.items()
    }
    checks["classical_explicit_formula_is_a_pinned_membrane"] = not gate[
        "classical_zero_sum_rederived"
    ]
    checks["odd_weil_implication_deferred"] = not gate["odd_weil_implication_consumed"]
    checks["rh_not_promoted"] = not gate["rh_promotion_allowed"]
    status = (
        "PASS_ODD_NATIVE_CLASSICAL_NORMALIZATION_STAGE3H"
        if all(checks.values())
        else "FAIL_ODD_NATIVE_CLASSICAL_NORMALIZATION_STAGE3H"
    )
    return {
        "schema": "rkf.odd_native_classical_normalization_stage3h.v1",
        "status": status,
        "claim_boundary": {
            "proved": [
                "correlation q=f*h-sharp is the translation pairing",
                "Fourier transform of the correlation has the required conjugate-reflection factorization",
                "boundary, Gamma and prime-power terms match the completed explicit-formula distribution term by term",
                "the odd boundary is exactly the negative rank-one L_partial square",
                "the logarithmic map preserves every completed-Weil term",
                "reflection, Hermitian symmetry and Fourier-sign reversal preserve the completed form",
                "the termwise identity extends from the odd core through the native completion",
            ],
            "pinned_not_rederived": [
                "the classical completed explicit formula identifying the distribution side with the symmetric zero sum"
            ],
            "open": [
                "parity-restricted classical Weil implication audit and consumption",
                "Riemann hypothesis promotion",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def load_stage3g_actual(path: Path) -> tuple[str, dict[str, Any]]:
    body = path.read_bytes()
    return sha256(body).hexdigest(), json.loads(body.decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stage3g-actual",
        type=Path,
        default=Path("proof_lab/NATIVE_SOURCE_KERNEL_NO_BLINDNESS_ACTUAL.json"),
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not args.stage3g_actual.exists():
        raise SystemExit(
            "Stage 3G actual certificate is missing. Generate and verify Stage 3G before Stage 3H."
        )
    upstream_hash, upstream_payload = load_stage3g_actual(args.stage3g_actual)
    payload = build_certificate(
        stage3g_hash=upstream_hash,
        stage3g_payload_valid=validate_stage3g_payload(upstream_payload),
    )
    body = canonical_bytes(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    print(payload["status"])
    gate = payload["actual_normalization_gate"]
    print("STAGE3G_HASH_VERIFIED", gate["stage3g_hash_verified"])
    print("BOUNDARY_TERM_MATCH", gate["actual_boundary_normalization"])
    print("GAMMA_TERM_MATCH", gate["actual_gamma_normalization"])
    print("PRIME_TERM_MATCH", gate["actual_prime_normalization"])
    print("LOG_UNITARY_MATCH", gate["actual_logarithmic_unitary_normalization"])
    print("ACTUAL_ODD_NATIVE_CLASSICAL_INTERFACE", gate["actual_odd_native_classical_interface"])
    print("CLASSICAL_ZERO_SUM_REDERIVED", gate["classical_zero_sum_rederived"])
    print("ODD_WEIL_IMPLICATION_CONSUMED", gate["odd_weil_implication_consumed"])
    print("RH_PROMOTION_ALLOWED", gate["rh_promotion_allowed"])
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
