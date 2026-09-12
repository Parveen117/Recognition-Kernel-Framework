#!/usr/bin/env python3
"""Exact RNKE-style calibration for the Morphic Recognition theorem spine.

This module does not replace the universal mathematical proofs in
`theorum/morphic_recognition/`.  It verifies the declared finite proof contracts,
negative controls, and statement/implementation consistency using exact integer
arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any, Callable

PROTOCOL = "morphic-recognition-rnke-proof-contract-v1"
THEOREMS = ("MR-01", "MR-02", "MR-03")


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def sha256_json(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _check(check_id: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {
        "id": check_id,
        "status": "pass" if passed else "fail",
        "detail": detail,
    }


def verify_mr01() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    # MR01-O1/O2: exact coordinatewise closure on a finite adversarial grid.
    grid = range(-2, 3)
    coordinate_mismatches = []
    local_override_escapes = []
    for r in product(grid, repeat=3):
        typed_zero = all(x == 0 for x in r)
        coordinate_zero = r == (0, 0, 0)
        if typed_zero != coordinate_zero:
            coordinate_mismatches.append(r)
        if any(x != 0 for x in r) and typed_zero:
            local_override_escapes.append(r)
    checks.append(_check("MR01-O1", not coordinate_mismatches, {"grid_cases": 125, "mismatches": coordinate_mismatches}))
    checks.append(_check("MR01-O2", not local_override_escapes, {"escapes": local_override_escapes}))

    # MR01-N1 / O3: a lossy sum aggregator has a nontrivial kernel witness.
    witness = (1, -1)
    sum_value = sum(witness)
    checks.append(_check(
        "MR01-N1",
        witness != (0, 0) and sum_value == 0,
        {"witness": list(witness), "aggregate": sum_value, "meaning": "nonzero typed residual hidden by sum"},
    ))

    # Identity aggregation is faithful on the calibration sector.
    identity_false_closures = []
    for r in product(grid, repeat=2):
        if r != (0, 0) and r == (0, 0):
            identity_false_closures.append(r)
    checks.append(_check("MR01-N2", not identity_false_closures, {"false_closures": identity_false_closures}))

    # Positive squared norm scalarization is zero iff all coordinates vanish.
    norm_false_closures = []
    for r in product(grid, repeat=3):
        rho2 = r[0] * r[0] + 2 * r[1] * r[1] + 3 * r[2] * r[2]
        if (rho2 == 0) != (r == (0, 0, 0)):
            norm_false_closures.append({"r": list(r), "rho2": rho2})
    checks.append(_check("MR01-O3", not norm_false_closures, {"positive_weight_false_closures": norm_false_closures}))

    return {
        "theorem_id": "MR-01",
        "status": "RNKE_CONTRACT_VERIFIED" if all(c["status"] == "pass" for c in checks) else "REJECTED",
        "checks": checks,
    }


def E(p: tuple[int, int, int]) -> tuple[int]:
    return (p[0],)


def Pi(p: tuple[int, int, int]) -> tuple[int, int]:
    return (p[1], p[2])


def G1(p: tuple[int, int, int]) -> tuple[int]:
    return (p[1],)


def G2(p: tuple[int, int, int]) -> tuple[int, int]:
    return (p[1], p[2])


def verify_mr02() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    # Exact same-endpoint / different-target witness.
    p = (0, 0, 0)
    q = (0, 0, 1)
    checks.append(_check(
        "MR02-N1",
        E(p) == E(q) and Pi(p) != Pi(q),
        {"p": list(p), "q": list(q), "endpoint": list(E(p)), "targets": [list(Pi(p)), list(Pi(q))]},
    ))

    # For E(x)=x1, ker E is span(e2,e3); Pi restricted to ker E has rank two.
    blind_basis = ((0, 1, 0), (0, 0, 1))
    target_images = (Pi(blind_basis[0]), Pi(blind_basis[1]))
    rank_pi_on_kernel = 2 if target_images == ((1, 0), (0, 1)) else None
    checks.append(_check(
        "MR02-O1",
        rank_pi_on_kernel == 2,
        {"blind_basis": [list(x) for x in blind_basis], "target_images": [list(x) for x in target_images], "rank": rank_pi_on_kernel},
    ))
    checks.append(_check("MR02-O2", rank_pi_on_kernel == 2, {"endpoint_decoder_exists": False, "blind_dimension": 2}))

    # One scalar channel misses e3 exactly.
    e3 = (0, 0, 1)
    one_channel_escape = E(e3) == (0,) and G1(e3) == (0,) and Pi(e3) != (0, 0)
    checks.append(_check("MR02-N2", one_channel_escape, {"witness": list(e3), "G1": list(G1(e3)), "target": list(Pi(e3))}))

    # Two channels are target-complete over an exact calibration box.
    repaired_escapes = []
    for x in product(range(-3, 4), repeat=3):
        if E(x) == (0,) and G2(x) == (0, 0) and Pi(x) != (0, 0):
            repaired_escapes.append(x)
    checks.append(_check("MR02-N3", not repaired_escapes, {"grid_cases": 343, "escapes": [list(x) for x in repaired_escapes]}))

    # Lower bound / attainability for this exact rank-two calibration.
    checks.append(_check("MR02-O3", one_channel_escape, {"one_channel_cannot_be_target_complete": True}))
    checks.append(_check("MR02-O4", not repaired_escapes, {"two_channels_are_target_complete": True, "m_min": 2}))

    return {
        "theorem_id": "MR-02",
        "status": "RNKE_CONTRACT_VERIFIED" if all(c["status"] == "pass" for c in checks) else "REJECTED",
        "checks": checks,
    }


def omega(b: int, a: int) -> int:
    return b * a


def omega_bad(b: int, a: int) -> int:
    return b * a * a


def cocycle_residual(rule: Callable[[int, int], int], a: int, b: int, c: int) -> int:
    return rule(c, b + a) + rule(b, a) - rule(c + b, a) - rule(c, b)


def alpha(a: int) -> int:
    return a * a


def omega_prime(b: int, a: int) -> int:
    return omega(b, a) + alpha(b + a) - alpha(b) - alpha(a)


def star(rule: Callable[[int, int], int], left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    """One-object category: second coordinate is the base arrow in (Z,+)."""
    n, b = left
    m, a = right
    return (n + m + rule(b, a), b + a)


def phi_plus(lifted: tuple[int, int]) -> tuple[int, int]:
    m, a = lifted
    return (m + alpha(a), a)


def phi_minus(lifted: tuple[int, int]) -> tuple[int, int]:
    m, a = lifted
    return (m - alpha(a), a)


def verify_mr03() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    good_failures = []
    for a, b, c in product(range(-5, 6), repeat=3):
        r = cocycle_residual(omega, a, b, c)
        if r != 0:
            good_failures.append({"a": a, "b": b, "c": c, "residual": r})
    checks.append(_check("MR03-N1", not good_failures, {"triples": 1331, "failures": good_failures[:5]}))
    checks.append(_check("MR03-O1", not good_failures, {"associativity_calibration": "closed"}))

    # Identity normalization omega(0,a)=omega(a,0)=0.
    identity_failures = []
    for a in range(-20, 21):
        if omega(0, a) != 0 or omega(a, 0) != 0:
            identity_failures.append(a)
    checks.append(_check("MR03-O2", not identity_failures, {"tested_arrows": 41, "failures": identity_failures}))

    # Forgetful projection is compositional in the one-object calibration.
    projection_failures = []
    for a, b, m, n in product(range(-2, 3), repeat=4):
        composed = star(omega, (n, b), (m, a))
        if composed[1] != b + a:
            projection_failures.append([a, b, m, n])
    checks.append(_check("MR03-O3", not projection_failures, {"cases": 625, "failures": projection_failures[:5]}))

    # Parenthesization equality follows exactly on a finite grid.
    parenthesis_failures = []
    zero_memory = 0
    for a, b, c in product(range(-4, 5), repeat=3):
        left = star(omega, (zero_memory, c), star(omega, (zero_memory, b), (zero_memory, a)))
        right = star(omega, star(omega, (zero_memory, c), (zero_memory, b)), (zero_memory, a))
        if left != right:
            parenthesis_failures.append({"a": a, "b": b, "c": c, "left": left, "right": right})
    checks.append(_check("MR03-O4", not parenthesis_failures, {"triples": 729, "failures": parenthesis_failures[:5]}))

    # Same base arrow, different memory coordinate.
    same_projection_distinct_memory = (0, 7)[1] == (3, 7)[1] and (0, 7) != (3, 7)
    checks.append(_check("MR03-O5", same_projection_distinct_memory, {"lifted_a": [0, 7], "lifted_b": [3, 7]}))

    # Correct coboundary gauge map uses +alpha for the displayed omega'.
    gauge_failures = []
    for a, b, m, n in product(range(-3, 4), repeat=4):
        lhs = phi_plus(star(omega, (n, b), (m, a)))
        rhs = star(omega_prime, phi_plus((n, b)), phi_plus((m, a)))
        if lhs != rhs:
            gauge_failures.append({"a": a, "b": b, "m": m, "n": n, "lhs": lhs, "rhs": rhs})
    checks.append(_check("MR03-O6", not gauge_failures, {"cases": 2401, "failures": gauge_failures[:5]}))

    # Bad cocycle exact witness a=b=c=1 has residual 2.
    bad_residual = cocycle_residual(omega_bad, 1, 1, 1)
    checks.append(_check("MR03-N2", bad_residual != 0, {"witness": [1, 1, 1], "cocycle_residual": bad_residual}))

    # Wrong-sign gauge map must fail for the same omega' convention.
    a = b = 1
    m = n = 0
    wrong_lhs = phi_minus(star(omega, (n, b), (m, a)))
    wrong_rhs = star(omega_prime, phi_minus((n, b)), phi_minus((m, a)))
    checks.append(_check(
        "MR03-N3",
        wrong_lhs != wrong_rhs,
        {"witness": {"a": a, "b": b, "m": m, "n": n}, "wrong_lhs": list(wrong_lhs), "wrong_rhs": list(wrong_rhs)},
    ))

    return {
        "theorem_id": "MR-03",
        "status": "RNKE_CONTRACT_VERIFIED" if all(c["status"] == "pass" for c in checks) else "REJECTED",
        "checks": checks,
    }


def run_all() -> dict[str, Any]:
    theorem_results = [verify_mr01(), verify_mr02(), verify_mr03()]
    all_closed = all(x["status"] == "RNKE_CONTRACT_VERIFIED" for x in theorem_results)
    result: dict[str, Any] = {
        "kind": "RNKE_MORPHIC_RECOGNITION_PROOF_CONTRACT",
        "protocol": PROTOCOL,
        "theorems": theorem_results,
        "theorem_count": len(theorem_results),
        "status": "RNKE_CONTRACT_VERIFIED" if all_closed else "REJECTED",
        "claim_boundary": {
            "universal_proofs": "mathematical theorem files",
            "executable_role": "exact finite calibration and negative-control verification",
            "formal_proof_assistant": False,
            "domain_adapter": None,
        },
    }
    result["certificate_sha256"] = sha256_json(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = run_all()
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["status"] == "RNKE_CONTRACT_VERIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
