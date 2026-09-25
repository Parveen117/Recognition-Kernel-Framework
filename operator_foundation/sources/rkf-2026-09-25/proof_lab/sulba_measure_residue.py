from __future__ import annotations

"""Exact certificate (theorum/72): ŚULBA — Baudhāyana's constructions on an
exact rational carrier, classified by the owner's note (Vedic repo,
VRG_Sulba_Invariant_Geometry_v1): a construction (Rekha) is FLAT when its
measure-residue  Res = Rec(Measure(r(X))) − Rec(Measure(X))  is 0, and
MEMORY-CLOSED when Res ≠ 0 but is stored exactly as Smṛti (G_Sulba = 0).

Everything is rational arithmetic (Fraction); no float, no sqrt evaluated.
Where the text uses √2 it uses its own cord 577/408 (BŚS 2.12), and so do we.

Facts certified:
 T1  Diagonal theorem (BŚS 1.48 dīrghacaturasrasyākṣṇayā rajjuḥ …) as the
     diagonal Bindu d² − a² − b² = 0 on the triples the text itself names
     (BŚS 1.49: 3-4-5, 12-5-13, 15-8-17, 7-24-25, 12-35-37, 15-36-39): FLAT.
     Each triple is a rational point on the native circle, i.e. an instance
     of F00E Thm 5.4 (Cos² + Sin² = 1) with Cos = a/d, Sin = b/d.
 T2  The √2 cord (BŚS 2.12): 1 + 1/3 + 1/(3·4) − 1/(3·4·34) = 577/408;
     Smṛti = (577/408)² − 2 = 1/166464 exactly; 577² − 2·408² = 1 (a Pell
     unit, so the cord is a convergent — verified by native Euclid, no
     continued-fraction theory imported, just the identity).  MEMORY-CLOSED.
     Control: dropping the last term (17/12) leaves Smṛti 1/144 — the text's
     correction term reduces the residue by a factor 1156.
 T3  Area transfers:
     square → rectangle (BŚS 2.1–2.4): residue 0, FLAT (exact).
     rectangle → square (BŚS 2.5, gnomon): side² = a·b exactly when the gnomon
       closes; residue 0, FLAT, and the leftover small square is exactly the
       diagonal Bindu of T1 (d² − c² form).
     square → circle (BŚS 2.9): r = a/2 + (d − a)/3 · ... with d = 577/408·a;
       the area residue against πr² cannot be rational -- so the construction
       is MEMORY-CLOSED with Smṛti recorded against the text's own circle
       measure (BŚS 2.10 circle → square, side = d·9785/11136).  We certify
       the ROUND TRIP: square → circle → square returns side·(9785/11136)·
       (2·r/a) = exact rational, and its deviation from 1 is the Smṛti.
 T4  Classification table: flat / memory-closed per construction, as the
     owner's note defines.
"""

import argparse
import hashlib
import json
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

TRIPLES = [(3, 4, 5), (12, 5, 13), (15, 8, 17), (7, 24, 25), (12, 35, 37), (15, 36, 39)]


def diagonal_bindu(a, b, d) -> Fr:
    return Fr(d) ** 2 - Fr(a) ** 2 - Fr(b) ** 2


def sqrt2_cord(terms: int = 4) -> Fr:
    seq = [Fr(1), Fr(1, 3), Fr(1, 12), Fr(-1, 408)]
    return sum(seq[:terms])


def euclid_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def build_certificate() -> dict[str, Any]:
    # T1
    t1 = all(diagonal_bindu(a, b, d) == 0 for a, b, d in TRIPLES)
    circle_pts = all(Fr(a, d) ** 2 + Fr(b, d) ** 2 == 1 for a, b, d in TRIPLES)
    # T2
    s = sqrt2_cord()
    smriti2 = s * s - 2
    pell = 577 * 577 - 2 * 408 * 408
    coprime = euclid_gcd(577, 408) == 1
    s3 = sqrt2_cord(3)
    smriti3 = s3 * s3 - 2
    # T3
    a = Fr(12)  # square side (any rational)
    # square -> rectangle of sides a and b keeping area: b = a*a/ c for chosen c
    c = Fr(9)
    rect = (c, a * a / c)
    t3a = rect[0] * rect[1] - a * a == 0
    # rectangle (p,q) -> square by gnomon (BŚS 2.5): cut q into p + (q-p); the strip (q-p) x p is bisected and
    # laid along two sides of the p-square making a gnomon; the completing small square has side (q-p)/2.
    p, q = Fr(6), Fr(24)
    big = p + (q - p) / 2  # side of the completed square
    small = (q - p) / 2  # side of the small square to be removed
    t3b = big * big - small * small == p * q  # area identity = difference of squares = diagonal Bindu form
    # square -> circle (BŚS 2.9): r = a/2 + (d/2 - a/2)/3 where d = diagonal = (577/408)·a
    d = s * a
    r = a / 2 + (d / 2 - a / 2) / 3
    # circle -> square (BŚS 2.10): side = d_circle · 9785/11136 with d_circle = 2r
    side_back = 2 * r * Fr(9785, 11136)
    roundtrip = side_back / a
    smriti_round = roundtrip - 1
    # implied "pi" of the text's pair: area a^2 = (text) area of circle radius r  =>  pi_text = a^2 / r^2 (exact rational)
    pi_text = a * a / (r * r)
    checks = {
        "T1_diagonal_bindu_zero_on_BSS_1_49_triples_FLAT": t1,
        "T1_each_triple_rational_point_of_native_circle_F00E_5_4": circle_pts,
        "T2_sqrt2_cord_577_over_408_smriti_1_over_166464": s == Fr(577, 408) and smriti2 == Fr(1, 166464),
        "T2_pell_unit_577sq_minus_2x408sq_eq_1_coprime": pell == 1 and coprime,
        "T2_control_three_terms_17_over_12_smriti_1_over_144": s3 == Fr(17, 12) and smriti3 == Fr(1, 144) and smriti3 / smriti2 == 1156,
        "T3_square_to_rectangle_residue_zero_FLAT": t3a,
        "T3_rectangle_to_square_gnomon_identity_FLAT": t3b,
        "T3_square_circle_square_roundtrip_rational_smriti_recorded": roundtrip != 1 and abs(smriti_round) < Fr(1, 100),
    }
    status = "PASS_SULBA_MEASURE_RESIDUE_CANDIDATE" if all(checks.values()) else "FAIL_SULBA_MEASURE_RESIDUE_CANDIDATE"
    table = {
        "diagonal (1.48)": "FLAT", "square→rectangle (2.1–2.4)": "FLAT", "rectangle→square gnomon (2.5)": "FLAT",
        "√2 cord (2.12)": f"MEMORY-CLOSED, Smṛti = {smriti2}", "square→circle→square (2.9, 2.10)": f"MEMORY-CLOSED, Smṛti = {smriti_round} (round trip), π_text = {pi_text} ≈ {float(pi_text):.6f} [float for display only]",
    }
    return {
        "schema": "rkf.sulba_measure_residue_candidate.v1",
        "status": status,
        "sqrt2_cord": str(s), "smriti_sqrt2": str(smriti2), "pi_text": str(pi_text), "roundtrip_smriti": str(smriti_round),
        "classification": table,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "diagonal theorem on the text's own triples as a zero diagonal Bindu; each triple a rational point of the native circle (F00E 5.4)",
                "√2 cord = 577/408 with exact Smṛti 1/166464; Pell unit identity; the last correction term reduces the residue by 1156",
                "area transfers: square↔rectangle and gnomon exact (flat); square→circle→square round trip an exact rational with recorded Smṛti",
                "owner's flat / memory-closed classification applied per construction",
            ],
            "NOT_claimed": ["that the text's circle rule is the best rational approximation; the general proof of the diagonal theorem (only the named triples, plus the gnomon identity)", "any irrational quantity evaluated", "RH, YM untouched"],
        },
        "checks": checks,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k, v)
    print("CLASS", payload["classification"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
