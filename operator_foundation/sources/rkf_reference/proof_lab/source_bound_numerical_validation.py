#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any


STATUS = "PASS_SOURCE_BOUND_PROOF_CARRYING_NUMERICAL_VALIDATION_CANDIDATE"
PROTOCOL = "source-bound-proof-carrying-numerics-v1"
ADMITTED_OPS = ("add", "sub", "mul", "neg", "div")
ADMITTED_TAIL_RULES = ("geometric_tail", "t43_exponential_jet")


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("interval lower must not exceed upper")

    @classmethod
    def exact(cls, value: Fraction | int) -> "Interval":
        q = Fraction(value)
        return cls(q, q)

    def contains_interval(self, other: "Interval") -> bool:
        return self.lower <= other.lower and other.upper <= self.upper

    @property
    def center(self) -> Fraction:
        return (self.lower + self.upper) / 2

    @property
    def radius(self) -> Fraction:
        return (self.upper - self.lower) / 2


def add(a: Interval, b: Interval) -> Interval:
    return Interval(a.lower + b.lower, a.upper + b.upper)


def sub(a: Interval, b: Interval) -> Interval:
    return Interval(a.lower - b.upper, a.upper - b.lower)


def mul(a: Interval, b: Interval) -> Interval:
    products = (
        a.lower * b.lower,
        a.lower * b.upper,
        a.upper * b.lower,
        a.upper * b.upper,
    )
    return Interval(min(products), max(products))


def neg(a: Interval) -> Interval:
    return Interval(-a.upper, -a.lower)


def reciprocal(a: Interval) -> Interval:
    if a.lower <= 0 <= a.upper:
        raise ZeroDivisionError("division interval contains zero")
    return Interval(min(Fraction(1, 1) / a.lower, Fraction(1, 1) / a.upper), max(Fraction(1, 1) / a.lower, Fraction(1, 1) / a.upper))


def div(a: Interval, b: Interval) -> Interval:
    return mul(a, reciprocal(b))


def canonical_operation(op: str, deps: list[Interval]) -> Interval:
    if op == "add" and len(deps) == 2:
        return add(deps[0], deps[1])
    if op == "sub" and len(deps) == 2:
        return sub(deps[0], deps[1])
    if op == "mul" and len(deps) == 2:
        return mul(deps[0], deps[1])
    if op == "neg" and len(deps) == 1:
        return neg(deps[0])
    if op == "div" and len(deps) == 2:
        return div(deps[0], deps[1])
    raise ValueError(f"unsupported operation or arity: {op}/{len(deps)}")


def _fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _interval_record(value: Interval) -> dict[str, str]:
    return {"lower": _fraction_text(value.lower), "upper": _fraction_text(value.upper)}


def _declared_interval(node: dict[str, Any]) -> Interval:
    interval = node.get("interval")
    if not isinstance(interval, (tuple, list)) or len(interval) != 2:
        raise ValueError("node interval must contain two endpoints")
    return Interval(Fraction(interval[0]), Fraction(interval[1]))


@dataclass(frozen=True)
class TraceResult:
    status: str
    root: Interval | None
    reason: str


def verify_trace(nodes: list[dict[str, Any]], root_id: str, *, source_complete: bool = True) -> TraceResult:
    if not source_complete:
        return TraceResult("OPEN", None, "source completeness / no-blindness obligation is open")
    if not isinstance(nodes, list) or not nodes:
        return TraceResult("INVALID", None, "trace must contain nodes")

    seen: dict[str, Interval] = {}
    all_ids: set[str] = set()
    for node in nodes:
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id:
            return TraceResult("INVALID", None, "every node needs an id")
        if node_id in all_ids:
            return TraceResult("INVALID", None, "duplicate node id")
        all_ids.add(node_id)

    for node in nodes:
        node_id = node["id"]
        try:
            declared = _declared_interval(node)
        except (ValueError, ZeroDivisionError) as exc:
            return TraceResult("INVALID", None, str(exc))

        kind = node.get("kind")
        if kind == "exact_contract":
            try:
                value = Fraction(node.get("value"))
            except (TypeError, ValueError, ZeroDivisionError) as exc:
                return TraceResult("INVALID", None, f"invalid exact leaf: {exc}")
            exact = Interval.exact(value)
            if not declared.contains_interval(exact):
                return TraceResult("FAIL", None, "exact source value is outside declared interval")
            seen[node_id] = declared
            continue

        if kind != "op":
            return TraceResult("OPEN", None, f"unsupported source class or node kind: {kind}")

        op = node.get("op")
        dep_ids = node.get("deps")
        if op not in ADMITTED_OPS or not isinstance(dep_ids, list):
            return TraceResult("INVALID", None, "unsupported operation or malformed deps")
        if any(dep not in seen for dep in dep_ids):
            # Dependency is either missing or points forward/cyclically. Both are invalid
            # in the declared topological trace format.
            return TraceResult("INVALID", None, "dependency missing or not earlier in topological order")
        try:
            canonical = canonical_operation(op, [seen[dep] for dep in dep_ids])
        except ZeroDivisionError as exc:
            return TraceResult("FAIL", None, str(exc))
        except ValueError as exc:
            return TraceResult("INVALID", None, str(exc))
        if not declared.contains_interval(canonical):
            return TraceResult("FAIL", None, "declared interval is narrower than verifier-computed enclosure")
        seen[node_id] = declared

    if root_id not in seen:
        return TraceResult("INVALID", None, "root id is missing")
    return TraceResult("PASS", seen[root_id], "source-bound interval trace verified")


def geometric_tail(first_omitted_upper: Fraction, ratio_upper: Fraction) -> Fraction:
    first = Fraction(first_omitted_upper)
    q = Fraction(ratio_upper)
    if first < 0:
        raise ValueError("first omitted magnitude must be nonnegative")
    if q < 0 or q >= 1:
        raise ValueError("geometric ratio upper must satisfy 0 <= q < 1")
    return first / (1 - q)


def exp_rational_upper(x: Fraction, order: int) -> Fraction:
    x = Fraction(x)
    if x < 0:
        raise ValueError("x must be nonnegative")
    if not isinstance(order, int) or isinstance(order, bool) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    q = x / (order + 2)
    if q >= 1:
        raise ValueError("order too small for geometric domination of exponential tail")
    partial = sum((x**k) / math.factorial(k) for k in range(order + 1))
    first_omitted = (x ** (order + 1)) / math.factorial(order + 1)
    return partial + geometric_tail(first_omitted, q)


def t43_tail_upper(
    time_upper: Fraction,
    observer_norm_upper: Fraction,
    generator_norm_upper: Fraction,
    jet_order: int,
    exp_order: int,
) -> Fraction:
    T = Fraction(time_upper)
    B = Fraction(observer_norm_upper)
    G = Fraction(generator_norm_upper)
    if T < 0 or B < 0 or G < 0:
        raise ValueError("T, B and G norm bounds must be nonnegative")
    if not isinstance(jet_order, int) or isinstance(jet_order, bool) or jet_order < 0:
        raise ValueError("jet_order must be a nonnegative integer")
    x = T * G
    exp_upper = exp_rational_upper(x, exp_order)
    return (
        (T ** (jet_order + 1))
        / math.factorial(jet_order + 1)
        * B
        * (G ** (jet_order + 1))
        * exp_upper
    )


def strict_upper_decision(interval: Interval, threshold: Fraction) -> str:
    theta = Fraction(threshold)
    if interval.upper < theta:
        return "PASS"
    if interval.lower >= theta:
        return "FAIL"
    return "INCOMPLETE"


def implementation_manifest_hash() -> str:
    manifest = {
        "protocol": PROTOCOL,
        "source_classes": ["exact_contract"],
        "operations": list(ADMITTED_OPS),
        "tail_rules": list(ADMITTED_TAIL_RULES),
        "boundary": "strict-upper-v1",
        "raw_asserted_radius": "not proof-bearing",
        "raw_asserted_tail": "not proof-bearing",
    }
    payload = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_certificate() -> dict[str, Any]:
    valid_nodes = [
        {"id": "a", "kind": "exact_contract", "value": Fraction(1, 3), "interval": (Fraction(1, 3), Fraction(1, 3))},
        {"id": "b", "kind": "exact_contract", "value": Fraction(1, 6), "interval": (Fraction(1, 6), Fraction(1, 6))},
        {"id": "sum", "kind": "op", "op": "add", "deps": ["a", "b"], "interval": (Fraction(1, 2), Fraction(1, 2))},
        {"id": "scale", "kind": "exact_contract", "value": Fraction(3), "interval": (Fraction(3), Fraction(3))},
        # The verifier-computed value is 3/2. A wider declared enclosure is lawful.
        {"id": "root", "kind": "op", "op": "mul", "deps": ["sum", "scale"], "interval": (Fraction(149, 100), Fraction(151, 100))},
    ]
    valid = verify_trace(valid_nodes, "root")

    forged_nodes = [
        {"id": "a", "kind": "exact_contract", "value": Fraction(1, 3), "interval": (Fraction(1, 3), Fraction(1, 3))},
        {"id": "b", "kind": "exact_contract", "value": Fraction(1, 6), "interval": (Fraction(1, 6), Fraction(1, 6))},
        {"id": "root", "kind": "op", "op": "add", "deps": ["a", "b"], "interval": (Fraction(49, 100), Fraction(49, 100))},
    ]
    forged = verify_trace(forged_nodes, "root")

    zero_div_nodes = [
        {"id": "one", "kind": "exact_contract", "value": Fraction(1), "interval": (Fraction(1), Fraction(1))},
        {"id": "zero", "kind": "exact_contract", "value": Fraction(0), "interval": (Fraction(0), Fraction(0))},
        {"id": "root", "kind": "op", "op": "div", "deps": ["one", "zero"], "interval": (Fraction(0), Fraction(0))},
    ]
    zero_div = verify_trace(zero_div_nodes, "root")

    forward_cycle = [
        {"id": "a", "kind": "op", "op": "neg", "deps": ["b"], "interval": (Fraction(-1), Fraction(1))},
        {"id": "b", "kind": "op", "op": "neg", "deps": ["a"], "interval": (Fraction(-1), Fraction(1))},
    ]
    cycle = verify_trace(forward_cycle, "a")

    unsupported = verify_trace([
        {"id": "root", "kind": "external_backend_claim", "interval": (Fraction(1), Fraction(1))}
    ], "root")

    source_open = verify_trace(valid_nodes, "root", source_complete=False)

    geo = geometric_tail(Fraction(1, 8), Fraction(1, 2))
    exp_up = exp_rational_upper(Fraction(1, 2), 2)
    t43 = t43_tail_upper(Fraction(1, 2), Fraction(2), Fraction(1, 3), 2, 2)

    exact_boundary = strict_upper_decision(Interval.exact(Fraction(4, 5)), Fraction(4, 5))
    touching_boundary = strict_upper_decision(Interval(Fraction(79, 100), Fraction(4, 5)), Fraction(4, 5))
    strict_pass = strict_upper_decision(Interval(Fraction(7, 10), Fraction(79, 100)), Fraction(4, 5))

    checks = {
        "valid_source_bound_trace": valid.status == "PASS" and valid.root == Interval(Fraction(149, 100), Fraction(151, 100)),
        "derived_radius_is_one_percent": valid.root is not None and valid.root.radius == Fraction(1, 100),
        "forged_narrow_interval_rejected": forged.status == "FAIL",
        "division_interval_containing_zero_rejected": zero_div.status == "FAIL",
        "cycle_or_forward_dependency_rejected": cycle.status == "INVALID",
        "unsupported_source_held_open": unsupported.status == "OPEN",
        "source_completeness_held_open": source_open.status == "OPEN",
        "geometric_tail_exact": geo == Fraction(1, 4),
        "exponential_upper_exact": exp_up == Fraction(277, 168),
        "t43_tail_positive_exact": t43 > 0 and isinstance(t43, Fraction),
        "exact_threshold_equality_fails": exact_boundary == "FAIL",
        "uncertain_threshold_touch_is_incomplete": touching_boundary == "INCOMPLETE",
        "strict_interval_below_threshold_passes": strict_pass == "PASS",
        "implementation_manifest_hash_is_sha256": len(implementation_manifest_hash()) == 64,
    }

    return {
        "schema": "SOURCE_BOUND_PROOF_CARRYING_NUMERICAL_VALIDATION_V0_1",
        "theorem": "47_source_bound_proof_carrying_numerical_validation_theorem",
        "protocol": PROTOCOL,
        "arithmetic": "fractions.Fraction only; verifier derives enclosures and tails",
        "status": STATUS if all(checks.values()) else "FAIL",
        "checks": checks,
        "pinned_examples": {
            "root_interval": _interval_record(valid.root) if valid.root else None,
            "root_radius": _fraction_text(valid.root.radius) if valid.root else None,
            "geometric_tail": _fraction_text(geo),
            "exp_upper_x_half_order_2": _fraction_text(exp_up),
            "t43_tail": _fraction_text(t43),
            "implementation_manifest_sha256": implementation_manifest_hash(),
        },
        "claim_boundary": [
            "a bound cannot validate itself",
            "source completeness remains an adapter obligation",
            "raw participant radius or analytic tail is not proof-bearing without an admitted validator",
            "division by an interval containing zero is rejected",
            "exact strict equality is failure while uncertain boundary contact is incomplete",
            "internal implementation hashing is integrity metadata, not an external authenticity anchor",
        ],
    }


def canonical_bytes(result: dict[str, Any]) -> bytes:
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
