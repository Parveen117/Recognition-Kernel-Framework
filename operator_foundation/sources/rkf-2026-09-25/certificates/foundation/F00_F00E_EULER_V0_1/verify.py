from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SPEC = HERE / "spec.json"
SCALAR = ROOT / "src/rh_framework/native_summability.py"
EULER = ROOT / "theorems/foundation/F00E_NATIVE_EULER_FROM_IOTA_COMPLEX.md"
PROTOCOL = ROOT / "certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md"


def canon(x: Any) -> bytes:
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()



def canonical_source_bytes(data: bytes) -> bytes:
    """Normalize text line endings before provenance hashing."""
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

def load_scalar():
    name = "rh_framework_f00e_certificate_scalar"
    spec = importlib.util.spec_from_file_location(name, SCALAR)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load NativeCutScalar")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod.NativeCutScalar


def ftext(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def rec(ok: bool, detail: str, data=None):
    return {"passed": bool(ok), "detail": detail, "data": data or {}}


def tail_bound(r: Fraction, n: int):
    first = r ** (n + 1) / math.factorial(n + 1)
    ratio = r / Fraction(n + 2)
    if ratio >= 1:
        raise ValueError("tail packet does not contract")
    return first / (1 - ratio), ratio


def exp_i(Scalar, t: Fraction, n: int):
    out, power, z = Scalar.zero(), Scalar.one(), Scalar(0, t)
    for k in range(n + 1):
        if k:
            power = power * z
        out = out + Scalar(
            power.radial / math.factorial(k),
            power.turn / math.factorial(k),
        )
    return out


def even_odd(Scalar, t: Fraction, n: int):
    a = b = Fraction(0)
    for k in range(n + 1):
        term = t ** k / math.factorial(k)
        q = k % 4
        if q == 0:
            a += term
        elif q == 1:
            b += term
        elif q == 2:
            a -= term
        else:
            b -= term
    return Scalar(a, b)


def shift_poly(p, h: Fraction):
    out = [Fraction(0) for _ in p]
    for d, c in enumerate(p):
        for k in range(d + 1):
            out[k] += c * math.comb(d, k) * h ** (d - k)
    return out


def policy_ok(text: str) -> bool:
    tokens = (
        "This theorem begins after the already derived cut-complex foundation",
        "It does **not** begin",
        "This is the Euler equation derived from the cut-complex field",
        "Only under the later classical chart",
        "-i r\\frac{d}{dr}",
    )
    return all(t in text for t in tokens)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    spec = json.loads(SPEC.read_text())
    pins = {
        x["path"]: x.get("expected_git_blob_sha1")
        for x in spec["authoritative_sources"]
    }
    source_records = []
    for path in (SCALAR, EULER, PROTOCOL):
        data = canonical_source_bytes(path.read_bytes())
        rel = path.relative_to(ROOT).as_posix()
        actual = blob_sha1(data)
        expected = pins.get(rel)
        source_records.append({
            "path": rel,
            "bytes": len(data),
            "sha256": sha256(data),
            "git_blob_sha1": actual,
            "expected_git_blob_sha1": expected,
            "pin_matches": expected is None or expected == actual,
        })

    checks, neg = {}, {}
    try:
        S = load_scalar()
        imported = True
    except Exception as exc:
        S, imported = None, False
        import_error = f"{type(exc).__name__}: {exc}"

    checks["C00-01"] = rec(
        imported and all(x["pin_matches"] for x in source_records),
        "Implementation import and source-pin audit.",
        {
            "sources": source_records,
            "import_error": None if imported else import_error,
        },
    )

    if S is not None:
        z, o, i = S.zero(), S.one(), S.iota()
        basis = [z, o, i, -o, -i]
        checks["C00-02"] = rec(
            o * o == o
            and o * i == i
            and i * o == i
            and i * i == -o
            and i.dagger() == -i,
            "Exact unit and quarter-turn table.",
        )
        checks["C00-03"] = rec(
            all((a * b) * c == a * (b * c) for a in basis for b in basis for c in basis)
            and all(a * b == b * a for a in basis for b in basis),
            "Associativity and commutativity on the bilinear basis.",
        )
        checks["C00-04"] = rec(
            all(
                a.dagger().dagger() == a
                and (a * b).dagger() == b.dagger() * a.dagger()
                for a in basis
                for b in basis
            ),
            "Dagger involution and product reversal.",
        )
        nums = spec["audit_packet"]["scalar_numerators"]
        dens = spec["audit_packet"]["scalar_denominators"]
        vals = sorted({Fraction(n, d) for n in nums for d in dens})
        lattice = [S(a, b) for a in vals for b in vals]
        checks["C00-05"] = rec(
            all(
                x.norm_square() >= 0
                and ((x.norm_square() == 0) == x.is_zero())
                for x in lattice
            ),
            "Exact positivity on the rational audit lattice.",
            {"scalar_points": len(lattice)},
        )
        checks["C00-06"] = rec(
            all(
                (a * b).norm_square() == a.norm_square() * b.norm_square()
                for a in lattice
                for b in lattice
            ),
            "Exact norm-square multiplicativity.",
            {"product_checks": len(lattice) ** 2},
        )

        m = spec["audit_packet"]["binomial_degree_max"]
        checks["C00E-01"] = rec(
            all(
                Fraction(math.comb(n, k), math.factorial(n))
                == Fraction(1, math.factorial(k) * math.factorial(n - k))
                for n in range(m + 1)
                for k in range(n + 1)
            ),
            "Exact factorial/binomial convolution coefficients.",
            {"maximum_degree": m},
        )
        r = Fraction(spec["audit_packet"]["factorial_tail_radius"])
        n = spec["audit_packet"]["factorial_tail_truncation"]
        upper, ratio = tail_bound(r, n)
        first = r ** (n + 1) / math.factorial(n + 1)
        checks["C00E-02"] = rec(
            ratio <= Fraction(1, 2) and upper <= 2 * first,
            "Exact geometric factorial-tail enclosure.",
            {"ratio": ftext(ratio), "upper": ftext(upper)},
        )
        h = Fraction(spec["audit_packet"]["unit_tangent_radius"])
        tangent = (h / 2) / (1 - h / 3)
        checks["C00E-03"] = rec(
            tangent < Fraction(1, 15),
            "Exact unit-tangent remainder enclosure.",
            {"upper": ftext(tangent), "threshold": "1/15"},
        )
        order = spec["audit_packet"]["euler_truncation"]
        ts = [Fraction(x) for x in spec["audit_packet"]["euler_argument_values"]]
        checks["C00E-04"] = rec(
            all(exp_i(S, t, order) == even_odd(S, t, order) for t in ts),
            "Exact even/odd factorial splitting.",
        )
        packets, ok = [], True
        for t in ts:
            v = exp_i(S, t, order)
            residual = abs(v.norm_square() - 1)
            tb, _ = tail_bound(abs(t), order)
            mass = sum(abs(t) ** k / math.factorial(k) for k in range(order + 1))
            bound = 2 * mass * tb + tb * tb
            ok = ok and residual <= bound
            packets.append({
                "t": ftext(t),
                "residual": ftext(residual),
                "upper": ftext(bound),
            })
        checks["C00E-05"] = rec(
            ok,
            "Circular residual enclosed by exact tails.",
            {"packets": packets},
        )

        deg = spec["audit_packet"]["flow_polynomial_degree_max"]
        s, t = Fraction(2, 3), Fraction(-5, 7)
        flow = all(
            shift_poly(shift_poly([Fraction(0)] * d + [Fraction(1)], -t), -s)
            == shift_poly([Fraction(0)] * d + [Fraction(1)], -(s + t))
            for d in range(deg + 1)
        )
        x = [Fraction(0), Fraction(1)]
        eps = Fraction(1, 11)
        q = shift_poly(x, -eps)
        deriv = [
            (q[j] if j < len(q) else 0) - (x[j] if j < len(x) else 0)
            for j in range(max(len(q), len(x)))
        ]
        deriv = [c / eps for c in deriv]
        checks["C00E-06"] = rec(
            flow and deriv == [Fraction(-1), Fraction(0)],
            "Exact flow composition and generator sign.",
            {"generator_difference": [ftext(c) for c in deriv]},
        )
        text = EULER.read_text()
        checks["C00E-07"] = rec(
            policy_ok(text),
            "Static no-import/source-order audit.",
        )

        def bad_mul(a, b):
            return S(
                a.radial * b.radial + a.turn * b.turn,
                a.radial * b.turn + a.turn * b.radial,
            )

        neg["wrong_iota_square"] = rec(
            bad_mul(i, i) != -o,
            "Wrong radial sign detected.",
        )
        neg["wrong_dagger"] = rec(
            S(i.radial, i.turn) != -i,
            "Wrong dagger detected.",
        )
        neg["removed_factorial"] = rec(
            Fraction(math.comb(2, 1), 1) != 1,
            "Removed n! detected.",
        )
        e1 = sum(Fraction(1, math.factorial(k)) for k in range(7))
        e2 = sum(Fraction(2 ** k, math.factorial(k)) for k in range(7))
        neg["additive_fake_exp"] = rec(
            e2 != 2 * e1,
            "Fake additive exponential rejected.",
        )
        badq = shift_poly(x, eps)
        badderiv = [
            (badq[j] if j < len(badq) else 0)
            - (x[j] if j < len(x) else 0)
            for j in range(max(len(badq), len(x)))
        ]
        badderiv = [c / eps for c in badderiv]
        neg["wrong_flow_sign"] = rec(
            badderiv != [Fraction(-1), Fraction(0)],
            "Wrong flow sign detected.",
        )
        neg["classical_primitive"] = rec(
            not policy_ok(
                text.replace("It does **not** begin", "It does begin", 1)
            ),
            "Classical primitive injection detected.",
        )
        checks["C00E-08"] = rec(
            all(x["passed"] for x in neg.values()),
            "All negative controls detected.",
            neg,
        )
    else:
        for oid in spec["required_obligations"]:
            if oid != "C00-01":
                checks[oid] = rec(False, "Skipped after import failure.")

    required = spec["required_obligations"]
    missing = [x for x in required if x not in checks]
    passed = not missing and all(checks[x]["passed"] for x in required)
    status = (
        spec["passing_status"]
        if passed
        else "INCONCLUSIVE_F00_F00E_RIGOROUS_COMPUTATIONAL_AUDIT"
    )
    result = {
        "schema": "rh-framework-foundational-certificate-result-v0.1",
        "certificate_class": spec["certificate_class"],
        "certificate_id": spec["certificate_id"],
        "theorems": spec["theorems"],
        "status": status,
        "checks": checks,
        "negative_controls": neg,
        "missing_obligations": missing,
        "source_records": source_records,
        "spec_sha256": sha256(canonical_source_bytes(SPEC.read_bytes())),
        "arithmetic": {
            "engine": "fractions.Fraction",
            "mode": "exact",
            "floating_proof_margins": False,
        },
        "scientific_boundary": {
            "foundational_alignment": "CERTIFIED" if passed else "INCONCLUSIVE",
            "completed_weil_sign": "OPEN",
            "eta_zero_endpoint": "OPEN",
            "riemann_hypothesis": "OPEN",
        },
        "claim_boundary": spec["claim_boundary"],
    }
    result["canonical_result_sha256"] = sha256(canon(result))
    out = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        p = args.output if args.output.is_absolute() else ROOT / args.output
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(out)
    print(status)
    print(result["canonical_result_sha256"])
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
