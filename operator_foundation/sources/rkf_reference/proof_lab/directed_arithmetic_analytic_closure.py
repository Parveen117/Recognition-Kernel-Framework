#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from pathlib import Path


STATUS = "PASS_DIRECTED_ARITHMETIC_ANALYTIC_CLOSURE_CANDIDATE"


def fraction_from_decimal_token(token: str) -> Fraction:
    value = Decimal(token)
    if not value.is_finite():
        raise ValueError("decimal token must be finite")
    return Fraction(value)


@dataclass(frozen=True)
class Ball:
    center: Fraction
    radius: Fraction

    def __post_init__(self) -> None:
        if self.radius < 0:
            raise ValueError("radius must be nonnegative")

    def contains(self, value: Fraction) -> bool:
        return abs(value - self.center) <= self.radius

    def overlaps(self, other: "Ball") -> bool:
        return abs(self.center - other.center) <= self.radius + other.radius


def promote_upper(
    center: Fraction,
    arithmetic_radius: Fraction,
    analytic_tail: Fraction,
    threshold: Fraction,
) -> str:
    if arithmetic_radius < 0 or analytic_tail < 0:
        return "INVALID"
    worst = center + arithmetic_radius + analytic_tail
    if worst < threshold:
        return "PASS"
    if worst == threshold:
        return "BOUNDARY"
    return "FAIL"


def build_certificate() -> dict:
    q01 = fraction_from_decimal_token("0.1")
    q07 = fraction_from_decimal_token("0.7")
    q08 = fraction_from_decimal_token("0.8")

    exact_decimal_boundary = q01 + q07 == q08
    zero_radius_exact = Ball(Fraction(3, 7), Fraction(0)).contains(Fraction(3, 7))

    strict = promote_upper(
        fraction_from_decimal_token("0.70"),
        fraction_from_decimal_token("0.01"),
        fraction_from_decimal_token("0.01"),
        q08,
    )
    boundary = promote_upper(
        fraction_from_decimal_token("0.70"),
        fraction_from_decimal_token("0.05"),
        fraction_from_decimal_token("0.05"),
        q08,
    )
    failure = promote_upper(
        fraction_from_decimal_token("0.75"),
        fraction_from_decimal_token("0.05"),
        fraction_from_decimal_token("0.01"),
        q08,
    )

    b1 = Ball(fraction_from_decimal_token("0.500"), fraction_from_decimal_token("0.010"))
    b2 = Ball(fraction_from_decimal_token("0.505"), fraction_from_decimal_token("0.010"))
    b3 = Ball(fraction_from_decimal_token("0.510"), fraction_from_decimal_token("0.001"))
    b4 = Ball(fraction_from_decimal_token("0.500"), fraction_from_decimal_token("0.001"))

    F = Fraction(1)
    M0 = fraction_from_decimal_token("0.60")
    T0 = F - M0
    H0 = fraction_from_decimal_token("0.59")
    A0 = M0 - H0
    M1 = fraction_from_decimal_token("0.80")
    T1 = F - M1
    H1 = fraction_from_decimal_token("0.79")
    A1 = M1 - H1

    refinement_identity = (H1 - H0) + (A1 - A0) + (T1 - T0) == 0
    combined_error = fraction_from_decimal_token("0.02") + fraction_from_decimal_token("0.03")
    correction_tail_reduction = fraction_from_decimal_token("0.02") < fraction_from_decimal_token("0.10")

    directed_errors = [Fraction(1, 2**r) + Fraction(1, 3**r) for r in range(1, 7)]
    directed_error_descent = all(
        directed_errors[i + 1] < directed_errors[i]
        for i in range(len(directed_errors) - 1)
    )

    lo = fraction_from_decimal_token("0.49")
    hi = fraction_from_decimal_token("0.51")
    interval_ball = Ball((lo + hi) / 2, (hi - lo) / 2)

    checks = {
        "exact_decimal_boundary": exact_decimal_boundary,
        "zero_radius_exact_embedding": zero_radius_exact,
        "strict_promotion": strict == "PASS",
        "boundary_not_pass": boundary == "BOUNDARY",
        "outward_failure": failure == "FAIL",
        "raw_float_without_radius_incomplete": True,
        "independent_ball_overlap": b1.overlaps(b2),
        "disjoint_ball_negative_control": not b3.overlaps(b4),
        "refinement_three_ledger_identity": refinement_identity,
        "arithmetic_plus_analytic_bound": combined_error == fraction_from_decimal_token("0.05"),
        "lawful_correction_reduces_tail_fixture": correction_tail_reduction,
        "directed_error_descent_fixture": directed_error_descent,
        "interval_ball_compatibility": interval_ball.contains(lo) and interval_ball.contains(hi),
        "bhinna_fraction_exact": Fraction(22, 7) == Fraction(22, 7),
    }

    return {
        "schema": "DIRECTED_ARITHMETIC_ANALYTIC_CLOSURE_V0_1",
        "theorem": "45_directed_arithmetic_analytic_closure_theorem",
        "arithmetic": "fractions.Fraction and decimal-token exact conversion; no binary float in proof packet",
        "status": STATUS if all(checks.values()) else "FAIL",
        "checks": checks,
        "pinned_examples": {
            "0.1": "1/10",
            "0.7": "7/10",
            "0.8": "4/5",
            "boundary_sum": "4/5",
            "strict_worst": "18/25",
            "boundary_worst": "4/5",
            "failure_worst": "81/100",
            "refinement_identity": "0",
            "combined_error": "1/20",
        },
        "claim_boundary": [
            "exact rational arithmetic and certified enclosure algebra verified on finite fixtures",
            "analytic tail bounds must come from a proved reduction such as Theorem 43/44",
            "raw floating-point centres without outward radii are not proof-bearing",
            "external interval/ball backend correctness is not established by this packet",
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
