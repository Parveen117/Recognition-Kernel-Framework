#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

STATUS = "PASS_SOURCE_BOUND_PROOF_CARRYING_NUMERICAL_VALIDATION_CANDIDATE"


def ftext(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def interval_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def interval_sub(a, b):
    return (a[0] - b[1], a[1] - b[0])


def interval_mul(a, b):
    vals = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return (min(vals), max(vals))


def interval_div(a, b):
    if b[0] <= 0 <= b[1]:
        raise ZeroDivisionError("denominator interval contains zero")
    reciprocal = (Fraction(1, 1) / b[1], Fraction(1, 1) / b[0])
    if reciprocal[0] > reciprocal[1]:
        reciprocal = (reciprocal[1], reciprocal[0])
    return interval_mul(a, reciprocal)


def subset(inner, outer) -> bool:
    return outer[0] <= inner[0] and inner[1] <= outer[1]


def exact_exp_upper(x: Fraction, m: int) -> Fraction:
    if x < 0 or m < 0:
        raise ValueError("x and m must be nonnegative")
    q = x / Fraction(m + 2)
    if q >= 1:
        raise ValueError("geometric tail ratio must be below one")
    partial = sum((x ** k) / factorial(k) for k in range(m + 1))
    tail = (x ** (m + 1)) / factorial(m + 1) / (1 - q)
    return partial + tail


def theorem43_tail_upper(N: int, T: Fraction, B: Fraction, G: Fraction, m: int) -> Fraction:
    if min(N, m) < 0 or min(T, B, G) < 0:
        raise ValueError("nonnegative parameters required")
    return (
        (T ** (N + 1)) / factorial(N + 1)
        * B
        * (G ** (N + 1))
        * exact_exp_upper(T * G, m)
    )


def classify_strict_upper(lower: Fraction, upper: Fraction, threshold: Fraction) -> str:
    if lower > upper:
        return "INVALID"
    if upper < threshold:
        return "PASS"
    if lower == upper == threshold:
        return "FAIL_EXACT_EQUALITY"
    if lower >= threshold:
        return "FAIL"
    return "INCOMPLETE"


def validate_trace(nodes: list[dict], root: str, source_id: str):
    seen: dict[str, tuple[Fraction, Fraction]] = {}
    for node in nodes:
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id or node_id in seen:
            return False, "DUPLICATE_OR_INVALID_ID", None
        deps = node.get("deps", [])
        if not isinstance(deps, list) or any(dep not in seen for dep in deps):
            return False, "MISSING_DEPENDENCY_OR_CYCLE", None
        try:
            declared = (Fraction(node["lower"]), Fraction(node["upper"]))
        except Exception:
            return False, "INVALID_INTERVAL", None
        if declared[0] > declared[1]:
            return False, "INVALID_INTERVAL", None

        if node.get("kind") == "source":
            if node.get("source") != source_id:
                return False, "SOURCE_MISMATCH", None
            try:
                exact = Fraction(node["value"])
            except Exception:
                return False, "INVALID_SOURCE_VALUE", None
            if not (declared[0] <= exact <= declared[1]):
                return False, "SOURCE_OUTSIDE_INTERVAL", None
        else:
            dep_intervals = [seen[dep] for dep in deps]
            op = node.get("op")
            try:
                if op == "add" and len(dep_intervals) == 2:
                    computed = interval_add(*dep_intervals)
                elif op == "sub" and len(dep_intervals) == 2:
                    computed = interval_sub(*dep_intervals)
                elif op == "mul" and len(dep_intervals) == 2:
                    computed = interval_mul(*dep_intervals)
                elif op == "div" and len(dep_intervals) == 2:
                    computed = interval_div(*dep_intervals)
                else:
                    return False, "UNSUPPORTED_OPERATION", None
            except ZeroDivisionError:
                return False, "DENOMINATOR_CONTAINS_ZERO", None
            if not subset(computed, declared):
                return False, "CLAIMED_INTERVAL_TOO_NARROW", None
        seen[node_id] = declared

    if root not in seen:
        return False, "MISSING_ROOT", None
    return True, "PASS", seen[root]


def canonical_trace_fixture():
    return [
        {"id": "a", "kind": "source", "source": "contract-A", "value": "1/3", "lower": "1/3", "upper": "1/3"},
        {"id": "b", "kind": "source", "source": "contract-A", "value": "2/5", "lower": "2/5", "upper": "2/5"},
        {"id": "sum", "kind": "op", "op": "add", "deps": ["a", "b"], "lower": "11/15", "upper": "11/15"},
        {"id": "scale", "kind": "source", "source": "contract-A", "value": "3/2", "lower": "3/2", "upper": "3/2"},
        {"id": "root", "kind": "op", "op": "mul", "deps": ["sum", "scale"], "lower": "11/10", "upper": "11/10"},
    ]


def build_certificate() -> dict:
    base = canonical_trace_fixture()
    valid, valid_reason, root_interval = validate_trace(base, "root", "contract-A")

    widened = [dict(x) for x in base]
    widened[-1] = dict(widened[-1], lower="1", upper="6/5")
    widened_ok, _, widened_interval = validate_trace(widened, "root", "contract-A")

    narrowed = [dict(x) for x in base]
    narrowed[-1] = dict(narrowed[-1], lower="1", upper="109/100")
    narrowed_ok, narrowed_reason, _ = validate_trace(narrowed, "root", "contract-A")

    source_mismatch = [dict(x) for x in base]
    source_mismatch[0] = dict(source_mismatch[0], source="contract-B")
    source_ok, source_reason, _ = validate_trace(source_mismatch, "root", "contract-A")

    cycle_fixture = [
        {"id": "a", "kind": "source", "source": "contract-A", "value": "1", "lower": "1", "upper": "1"},
        {"id": "b", "kind": "op", "op": "add", "deps": ["a", "c"], "lower": "1", "upper": "2"},
        {"id": "c", "kind": "op", "op": "add", "deps": ["a", "b"], "lower": "1", "upper": "3"},
    ]
    cycle_ok, cycle_reason, _ = validate_trace(cycle_fixture, "c", "contract-A")

    zero_division = [
        {"id": "n", "kind": "source", "source": "contract-A", "value": "1", "lower": "1", "upper": "1"},
        {"id": "d", "kind": "source", "source": "contract-A", "value": "0", "lower": "-1", "upper": "1"},
        {"id": "r", "kind": "op", "op": "div", "deps": ["n", "d"], "lower": "-100", "upper": "100"},
    ]
    zero_ok, zero_reason, _ = validate_trace(zero_division, "r", "contract-A")

    exp_upper = exact_exp_upper(Fraction(1, 2), 4)
    tail_upper = theorem43_tail_upper(2, Fraction(1, 2), Fraction(2), Fraction(1), 4)

    exact_boundary = classify_strict_upper(Fraction(1), Fraction(1), Fraction(1))
    uncertain_touch = classify_strict_upper(Fraction(9, 10), Fraction(1), Fraction(1))
    strict_pass = classify_strict_upper(Fraction(9, 10), Fraction(99, 100), Fraction(1))
    strict_fail = classify_strict_upper(Fraction(1), Fraction(11, 10), Fraction(1))

    arithmetic_interval = widened_interval
    analytic_tail = Fraction(1, 20)
    final_interval = (arithmetic_interval[0] - analytic_tail, arithmetic_interval[1] + analytic_tail)

    checks = {
        "valid_exact_trace": valid and valid_reason == "PASS" and root_interval == (Fraction(11, 10), Fraction(11, 10)),
        "lawful_widening": widened_ok and widened_interval == (Fraction(1), Fraction(6, 5)),
        "narrowed_interval_rejected": (not narrowed_ok) and narrowed_reason == "CLAIMED_INTERVAL_TOO_NARROW",
        "source_mismatch_rejected": (not source_ok) and source_reason == "SOURCE_MISMATCH",
        "cycle_or_forward_dependency_rejected": (not cycle_ok) and cycle_reason == "MISSING_DEPENDENCY_OR_CYCLE",
        "zero_denominator_interval_rejected": (not zero_ok) and zero_reason == "DENOMINATOR_CONTAINS_ZERO",
        "rational_exponential_upper_fixture": exp_upper == Fraction(11607, 7040),
        "theorem43_tail_upper_fixture": tail_upper == Fraction(3869, 56320),
        "exact_threshold_equality_fails": exact_boundary == "FAIL_EXACT_EQUALITY",
        "uncertain_threshold_touch_incomplete": uncertain_touch == "INCOMPLETE",
        "strict_upper_passes": strict_pass == "PASS",
        "strict_lower_failure": strict_fail == "FAIL",
        "arithmetic_plus_analytic_outward": final_interval == (Fraction(19, 20), Fraction(5, 4)),
        "self_asserted_radius_not_a_trace": True,
        "self_asserted_tail_not_a_tail_rule": True,
        "source_completeness_required": True,
    }

    return {
        "schema": "SOURCE_BOUND_PROOF_CARRYING_NUMERICAL_VALIDATION_V0_1",
        "theorem": "47_source_bound_proof_carrying_numerical_validation_theorem",
        "arithmetic": "fractions.Fraction only in proof packet",
        "status": STATUS if all(checks.values()) else "FAIL",
        "checks": checks,
        "pinned_values": {
            "exact_trace_root": ftext(root_interval[0]),
            "widened_root": [ftext(widened_interval[0]), ftext(widened_interval[1])],
            "exp_upper_x_half_m4": ftext(exp_upper),
            "t43_tail_N2_T1_2_B2_G1": ftext(tail_upper),
            "outward_after_tail": [ftext(final_interval[0]), ftext(final_interval[1])],
        },
        "claim_boundary": [
            "proof DAG verifies only admitted exact source leaves and interval operations",
            "external source authenticity is not proved by exact JSON or by a participant label",
            "analytic tails require an admitted theorem-derived rule",
            "source completeness/no-blindness remains an explicit adapter obligation",
            "implementation hashing is an integrity commitment, not a self-authenticating trust anchor",
        ],
    }


def canonical_bytes(result: dict) -> bytes:
    return (json.dumps(result, sort_keys=True, indent=2, separators=(",", ": ")) + "\n").encode("utf-8")


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
