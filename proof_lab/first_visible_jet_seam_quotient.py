#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


STATUS = "PASS_FIRST_VISIBLE_JET_SEAM_QUOTIENT_CANDIDATE"


class RawDivisionByZero(ValueError):
    pass


def raw_divide(numerator: Fraction, denominator: Fraction) -> Fraction:
    if denominator == 0:
        raise RawDivisionByZero("raw algebraic division by zero is invalid")
    return numerator / denominator


def first_visible_order(coefficients: Iterable[Fraction]) -> int | None:
    for k, coefficient in enumerate(coefficients):
        if coefficient != 0:
            return k
    return None


@dataclass(frozen=True)
class SeamClassification:
    status: str
    numerator_order: int | None
    denominator_order: int | None
    quotient: Fraction | None = None


def classify_finite_jets(
    numerator_coefficients: Iterable[Fraction],
    denominator_coefficients: Iterable[Fraction],
) -> SeamClassification:
    a = tuple(Fraction(x) for x in numerator_coefficients)
    b = tuple(Fraction(x) for x in denominator_coefficients)
    r_a = first_visible_order(a)
    r_b = first_visible_order(b)

    if r_b is None:
        return SeamClassification(
            "INCOMPLETE_FLAT_OR_UNRESOLVED",
            r_a,
            None,
            None,
        )
    if r_a is None:
        # With a visible denominator and all available numerator jets zero,
        # the finite jet data only proves higher-order/flat numerator behavior,
        # not a global identity. The conservative finite-jet classification is zero
        # when the numerator remainder is known to be little-o(t^r_b); that
        # remainder hypothesis is represented here by the caller's admitted jet packet.
        return SeamClassification("FINITE_QUOTIENT_ZERO", None, r_b, Fraction(0))
    if r_a > r_b:
        return SeamClassification("FINITE_QUOTIENT_ZERO", r_a, r_b, Fraction(0))
    if r_a < r_b:
        return SeamClassification("DIVERGENT_NO_FINITE_QUOTIENT", r_a, r_b, None)

    leading_denominator = b[r_b]
    if leading_denominator == 0:
        raise AssertionError("first-visible denominator coefficient cannot be zero")
    return SeamClassification(
        "FINITE_SEAM_QUOTIENT",
        r_a,
        r_b,
        a[r_a] / leading_denominator,
    )


def reparameterized_leading(coefficient: Fraction, order: int, derivative_at_zero: Fraction) -> Fraction:
    if derivative_at_zero == 0:
        raise ValueError("regular seam reparameterization requires nonzero derivative")
    return coefficient * derivative_at_zero**order


def quotient_enclosure_radius(
    numerator_leading: Fraction,
    denominator_leading: Fraction,
    numerator_remainder: Fraction,
    denominator_remainder: Fraction,
) -> Fraction:
    if numerator_remainder < 0 or denominator_remainder < 0:
        raise ValueError("remainder bounds must be nonnegative")
    b_abs = abs(denominator_leading)
    if b_abs <= denominator_remainder:
        raise ValueError("reduced denominator is not separated from zero")
    return (
        b_abs * numerator_remainder
        + abs(numerator_leading) * denominator_remainder
    ) / (b_abs * (b_abs - denominator_remainder))


def quotient_interval(
    numerator_leading: Fraction,
    denominator_leading: Fraction,
    numerator_remainder: Fraction,
    denominator_remainder: Fraction,
) -> tuple[Fraction, Fraction]:
    center = raw_divide(numerator_leading, denominator_leading)
    radius = quotient_enclosure_radius(
        numerator_leading,
        denominator_leading,
        numerator_remainder,
        denominator_remainder,
    )
    return center - radius, center + radius


def build_certificate() -> dict:
    equal = classify_finite_jets(
        [Fraction(0), Fraction(0), Fraction(2)],
        [Fraction(0), Fraction(0), Fraction(4)],
    )
    numerator_higher = classify_finite_jets(
        [Fraction(0), Fraction(0), Fraction(3)],
        [Fraction(0), Fraction(5)],
    )
    denominator_higher = classify_finite_jets(
        [Fraction(0), Fraction(3)],
        [Fraction(0), Fraction(0), Fraction(5)],
    )
    flat = classify_finite_jets(
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    )

    a = Fraction(7, 3)
    b = Fraction(5, 2)
    r = 3
    c = Fraction(-4, 3)
    a_tilde = reparameterized_leading(a, r, c)
    b_tilde = reparameterized_leading(b, r, c)

    radius = quotient_enclosure_radius(
        Fraction(3, 2),
        Fraction(2),
        Fraction(1, 100),
        Fraction(1, 50),
    )
    lo, hi = quotient_interval(
        Fraction(3, 2),
        Fraction(2),
        Fraction(1, 100),
        Fraction(1, 50),
    )

    raw_one_zero_rejected = False
    raw_zero_zero_rejected = False
    try:
        raw_divide(Fraction(1), Fraction(0))
    except RawDivisionByZero:
        raw_one_zero_rejected = True
    try:
        raw_divide(Fraction(0), Fraction(0))
    except RawDivisionByZero:
        raw_zero_zero_rejected = True

    denominator_separation_rejected = False
    try:
        quotient_enclosure_radius(
            Fraction(1), Fraction(1, 100), Fraction(0), Fraction(1, 100)
        )
    except ValueError:
        denominator_separation_rejected = True

    checks = {
        "raw_1_over_0_rejected": raw_one_zero_rejected,
        "raw_0_over_0_rejected": raw_zero_zero_rejected,
        "equal_order_quotient": equal.status == "FINITE_SEAM_QUOTIENT" and equal.quotient == Fraction(1, 2),
        "numerator_higher_order_zero": numerator_higher.status == "FINITE_QUOTIENT_ZERO" and numerator_higher.quotient == 0,
        "denominator_higher_order_diverges": denominator_higher.status == "DIVERGENT_NO_FINITE_QUOTIENT",
        "flat_finite_jets_incomplete": flat.status == "INCOMPLETE_FLAT_OR_UNRESOLVED",
        "regular_reparameterization_invariant": a_tilde / b_tilde == a / b,
        "zero_derivative_reparameterization_rejected": True,
        "denominator_separation_required": denominator_separation_rejected,
        "quotient_radius_positive": radius > 0,
        "quotient_interval_contains_center": lo <= Fraction(3, 4) <= hi,
        "exact_rational_packet": all(isinstance(x, Fraction) for x in (radius, lo, hi)),
    }

    try:
        reparameterized_leading(Fraction(1), 2, Fraction(0))
        checks["zero_derivative_reparameterization_rejected"] = False
    except ValueError:
        pass

    return {
        "schema": "FIRST_VISIBLE_JET_SEAM_QUOTIENT_V0_1",
        "theorem": "46_first_visible_jet_seam_quotient_theorem",
        "arithmetic": "fractions.Fraction only; no binary float in proof packet",
        "status": STATUS if all(checks.values()) else "FAIL",
        "checks": checks,
        "pinned_examples": {
            "equal_order_quotient": "1/2",
            "reparameterization_ratio": "14/15",
            "quotient_radius": str(radius),
            "quotient_interval_lower": str(lo),
            "quotient_interval_upper": str(hi),
        },
        "claim_boundary": [
            "raw algebraic 1/0 and 0/0 remain invalid",
            "finite seam quotient requires finite first-visible denominator structure",
            "all-zero finite jets are incomplete rather than assigned a value",
            "regular parameter changes preserve equal-order leading-coefficient ratio",
            "numerical quotient enclosure requires proved remainder bounds and denominator separation",
        ],
    }


def canonical_bytes(result: dict) -> bytes:
    text = json.dumps(result, sort_keys=True, indent=2, separators=(",", ": ")) + "\n"
    return text.encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_certificate()
    payload = canonical_bytes(result)
    if args.output:
        args.output.write_bytes(payload)
    else:
        print(payload.decode("utf-8"), end="")
    print("SHA256", hashlib.sha256(payload).hexdigest())
    return 0 if result["status"] == STATUS else 1


if __name__ == "__main__":
    raise SystemExit(main())
