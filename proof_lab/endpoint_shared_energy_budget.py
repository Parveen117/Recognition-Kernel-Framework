"""SE1: exact shared-energy bounds for the pinned T21 chart profile.

This program replays a supplied outward source profile; it does not regenerate
the Arb inequalities or prove attachment to the completed-Weil source.
Only standard-library exact rational arithmetic enters the reported bounds.
"""
from __future__ import annotations

import argparse
import base64
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
import lzma
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "proof_lab/imported/endpoint_shared_energy"
RESULT = ROOT / "proof_lab/ENDPOINT_SHARED_ENERGY_RESULT.json"
XZ_HASH = "63b5f8ed67fe8bba606e1486b98279c8ff2976dd7f8831f2de00294c7ccac95b"
RAW_HASH = "0cf54e6f8e2d30e4d03f70f5826d47972c3a8c698d730d358dca8b5b7e3fcc02"
STEP = F(1, 200)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def exact_binary64(raw: bytes) -> F:
    """Decode finite IEEE-754 binary64 directly to a rational, without a float."""
    bits, = struct.unpack(">Q", raw)
    sign = -1 if bits >> 63 else 1
    exponent = (bits >> 52) & 2047
    mantissa = bits & ((1 << 52) - 1)
    if exponent == 2047:
        raise ValueError("Non-finite profile entry")
    if exponent:
        mantissa += 1 << 52
        power = exponent - 1023 - 52
    else:
        power = -1074
    return F(sign * mantissa) * (F(2) ** power)


def parse_profile(raw: bytes) -> dict:
    if digest(raw) != RAW_HASH:
        raise ValueError("Profile binary hash mismatch")
    if len(raw) != 19344 or raw[:8] != b"NW3T21P1":
        raise ValueError("Profile format mismatch")
    if raw[8:28].hex() != "85f14bff136f441544106867e0aaab72b2199cc7":
        raise ValueError("Source commit mismatch")
    if raw[28:48].hex() != "bae34ce18e280cad064aeeed0df36eb38c8af7f8":
        raise ValueError("Export commit mismatch")
    cells, events = struct.unpack_from(">II", raw, 112)
    if (cells, events) != (2400, 78734):
        raise ValueError("Source event/cell count mismatch")
    slope = exact_binary64(raw[120:128])
    far = exact_binary64(raw[128:136])
    floors = tuple(exact_binary64(raw[i:i+8]) for i in range(136, len(raw), 8))
    if slope <= 0 or far <= 0 or floors[0] != 0:
        raise ValueError("Invalid seam/far source data")
    if not all(a < b for a, b in zip(floors, floors[1:])):
        raise ValueError("Source floors must increase strictly")
    return {"slope": slope, "far": far, "floors": floors, "cells": cells}


def load_profile(path: Path = DATA / "T21_PROFILE.b64") -> dict:
    compressed = base64.b64decode(path.read_text(encoding="ascii").strip(), validate=True)
    if digest(compressed) != XZ_HASH:
        raise ValueError("Compressed profile hash mismatch")
    return parse_profile(lzma.decompress(compressed))


def first_cell_excess(alpha: F, c: F, h: F, tau: F) -> F:
    # The positive part has no internal breakpoint under this checked condition.
    if alpha < 0 or c <= 0 or h <= 0 or tau < 0:
        raise ValueError("Invalid envelope parameters")
    if tau * c * h * h > 1:
        raise ValueError("First-cell breakpoint requires a finer split")
    return 2 * alpha * (h / c - tau * h**3 / 3)


def cell_excess(alpha: F, left: F, right: F, floor: F, tau: F) -> F:
    if alpha < 0 or left < 0 or right <= left or floor <= 0 or tau < 0:
        raise ValueError("Invalid active cell")
    return 2 * alpha * (right**3 - left**3) / 3 * max(1 / floor - tau, F(0))


def shared_bound(profile: dict, *, total_mass: F, moment_square: F) -> dict:
    if total_mass < 0 or moment_square < 0:
        raise ValueError("Energy budgets must be nonnegative")
    tau = 1 / profile["far"]
    first = first_cell_excess(moment_square, profile["slope"] / 2, STEP, tau)
    terms = tuple(cell_excess(moment_square, i*STEP, (i+1)*STEP,
                             profile["floors"][i], tau)
                  for i in range(1, profile["cells"]))
    active = sum(terms, F(0))
    return {"global_mass_charge": tau * total_mass, "first_excess": first,
            "active_excess": active, "positive_cells": sum(t > 0 for t in terms),
            "upper": tau * total_mass + first + active}


def separate_bound(profile: dict, *, total_mass: F, moment_square: F,
                   amplitude_square: F) -> F:
    first = 2 * STEP * moment_square / (profile["slope"] / 2)
    active = sum((2 * STEP * min(amplitude_square, moment_square*((i+1)*STEP)**2)
                  / profile["floors"][i] for i in range(1, profile["cells"])), F(0))
    return first + active + total_mass / profile["far"]


def summary(value: F) -> dict:
    with localcontext() as ctx:
        ctx.prec = 65
        display = format(Decimal(value.numerator) / Decimal(value.denominator), ".45f")
    # The decimal is display-only. All comparisons use the exact fraction.
    def integer_bytes(number: int) -> bytes:
        width = max(1, (abs(number).bit_length() + 7) // 8)
        return (b"-" if number < 0 else b"+") + width.to_bytes(8,"big") + abs(number).to_bytes(width,"big")
    return {"display_decimal": display,
            "exact_fraction_sha256": digest(integer_bytes(value.numerator) + integer_bytes(value.denominator)),
            "numerator_bits": value.numerator.bit_length(),
            "denominator_bits": value.denominator.bit_length()}


def build_report() -> dict:
    p = load_profile()
    old = separate_bound(p, total_mass=F(1,12), moment_square=F(1,9),
                         amplitude_square=F(1,16))
    sharp_separate = separate_bound(p, total_mass=F(1,12), moment_square=F(1,81),
                                    amplitude_square=F(1,18))
    shared = shared_bound(p, total_mass=F(1,12), moment_square=F(1,81))
    graph = shared_bound(p, total_mass=F(1,48), moment_square=F(1,81))
    matrix_coefficient = shared_bound(p, total_mass=F(1,4), moment_square=F(4,27))["upper"]
    if not (graph["upper"] < F(2,15) and matrix_coefficient < F(8,5)):
        raise AssertionError("Claimed rational comparison failed")
    if not (old > sharp_separate > shared["upper"] > graph["upper"]):
        raise AssertionError("Refinement ordering failed")
    if matrix_coefficient != 12 * graph["upper"]:
        raise AssertionError("Scalar/matrix homogeneity failed")
    return {
        "schema": "rkf.endpoint-shared-energy.v1",
        "status": "PASS_EXACT_PROFILE_ACCUMULATION",
        "arithmetic": "Python standard library; exact Fraction comparisons",
        "profile": {"binary_sha256": RAW_HASH, "compressed_sha256": XZ_HASH,
                    "cells": p["cells"], "prime_power_events": 78734,
                    "near_zero_slope": str(p["slope"]), "far_floor": str(p["far"])},
        "graph_boundary": {"seed_norm_square": "1/12", "old_mass_upper": "1/12",
                           "new_mass_upper": "1/48", "moment_square_upper": "1/81",
                           "fourier_normalization": "unitary; pointwise 1/sqrt(2pi) relaxed to 1"},
        "comparisons": {"old_rational_separate": summary(old),
                        "sharper_moment_separate": summary(sharp_separate),
                        "shared_mass_only": summary(shared["upper"]),
                        "graph_energy_and_shared_mass": summary(graph["upper"])},
        "new_budget": {key: summary(value) if isinstance(value,F) else value
                       for key,value in graph.items()},
        "matrix_residual_coefficient": summary(matrix_coefficient),
        "exact_conclusions": {"chart_upper_less_than": "2/15",
                              "chart_reserve_greater_than": "13/15",
                              "residual_matrix_coefficient_less_than": "8/5"},
        "claim_boundary": {
            "native_graph_energy_inequality": "PROVED_UNDER_T35_GRAPH_HYPOTHESES",
            "profile_accumulation": "EXACT_OVER_PINNED_OUTWARD_INPUTS",
            "arb_profile_regenerated": False,
            "actual_residual_columns_computed": False,
            "completed_source_chart_attachment": "OPEN",
            "full_odd_boundary_vs_feshbach_source_identified": False,
            "endpoint_K0_sign": "NOT_CERTIFIED",
            "riemann_hypothesis": "NOT_CLAIMED"}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.check == args.write:
        parser.error("Choose exactly one of --check or --write")
    report = build_report()
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write:
        RESULT.write_text(encoded, encoding="utf-8")
    elif RESULT.read_text(encoding="utf-8") != encoded:
        raise AssertionError("Stored result differs from exact replay")
    print(report["status"])
    print("CHART_UPPER", report["comparisons"]["graph_energy_and_shared_mass"]["display_decimal"])
    print("SOURCE_ATTACHMENT", report["claim_boundary"]["completed_source_chart_attachment"])


if __name__ == "__main__":
    main()
