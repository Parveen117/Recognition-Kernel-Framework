"""Exact supplied-model controls for SE39; not a zeta/RH certificate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path


RESULT = Path(__file__).with_name("ENDPOINT_RH_BRIDGE_CONTROLS.json")


def multiply(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def evaluate(p, t):
    value = F(0)
    for a in reversed(p):
        value = value * t + a
    return value


def derivative(p):
    return [i * a for i, a in enumerate(p)][1:]


def response(p, t):
    h = evaluate(p, t)
    hp = evaluate(derivative(p), t)
    hpp = evaluate(derivative(derivative(p)), t)
    return 2 * t * hp / h, 2 * hp / h + 2 * t * (hpp * h - hp * hp) / (h * h)


def response_matrix(p, points):
    readings = [response(p, t) for t in points]
    return [
        [2 * readings[i][1] if i == j else
         2 * (readings[i][0] - readings[j][0]) / (t - u)
         for j, u in enumerate(points)]
        for i, t in enumerate(points)
    ]


def pair_entry(x, y, t, u):
    # Re[a / ((t-a)(u-a))] evaluated in real rational arithmetic.
    real_den = (t - x) * (u - x) - y * y
    imag_den = -y * (t + u - 2 * x)
    return -8 * (x * real_den + y * imag_den) / (real_den**2 + imag_den**2)


def determinant(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def reading(m, c):
    return sum(c[i] * m[i][j] * c[j] for i in range(2) for j in range(2))


def encoded(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, list):
        return [encoded(v) for v in value]
    if isinstance(value, dict):
        return {k: encoded(v) for k, v in value.items()}
    return value


def replay():
    checks = []

    def require(name, condition):
        if not condition:
            raise ArithmeticError(name)
        checks.append(name)

    x, y = F(-1), F(1)
    points = [F(3), F(4)]
    pair_poly = [x*x + y*y, -2*x, F(1)]
    pair = response_matrix(pair_poly, points)
    sector = [[pair_entry(x, y, t, u) for u in points] for t in points]
    require("mixed and diagonal readings match the independent pair formula", pair == sector)
    require("pair matrix exact values", pair == [[F(184, 289), F(112, 221)], [F(112, 221), F(68, 169)]])
    require("pair diagonals are positive", all(pair[i][i] > 0 for i in range(2)))
    predicted_det = -64 * (x*x+y*y) * y*y * (points[1]-points[0])**2
    predicted_det /= ((points[0]-x)**2+y*y)**2 * ((points[1]-x)**2+y*y)**2
    require("sector determinant identity and negative sign", determinant(pair) == predicted_det == F(-32, 48841))

    # Decode a negative direction only from detached serialized matrix readings.
    detached = [[F(v) for v in row] for row in json.loads(json.dumps(encoded(pair))) ]
    witness = [-detached[0][1] / detached[0][0], F(1)]
    q = reading(detached, witness)
    require("mixed reading detects a negative direction", q < 0 and q == determinant(detached) / detached[0][0])

    masked_poly = pair_poly
    for v in (F(1), F(2)):
        for _ in range(10):
            masked_poly = multiply(masked_poly, [v, F(1)])
    masked = response_matrix(masked_poly, points)
    sums = [[pair[i][j] + sum(40*v/((t+v)*(u+v)) for v in (F(1), F(2)))
             for j, u in enumerate(points)] for i, t in enumerate(points)]
    require("full degree-22 response matches summed sectors", masked == sums)
    require("masked matrix exact values", masked == [[F(18313, 2890), F(3430, 663)], [F(3430, 663), F(32128, 7605)]])
    require("two-probe masked reading is positive definite", masked[0][0] > 0 and determinant(masked) == F(57532, 10989225) > 0)
    for v in (F(1), F(2)):
        atom = response_matrix([v, F(1)], points)
        require(f"real atom {v} has positive rank one", atom[0][0] > 0 and determinant(atom) == 0)
    return encoded({
        "stage": "SE39",
        "scope": "Exact rational controls on supplied polynomial response models; no xi zero computation or global RH certificate.",
        "points": points,
        "pair": {"polynomial_coefficients_ascending": pair_poly, "readings": pair,
                 "determinant": determinant(pair), "decoded_negative_vector": witness, "decoded_reading": q},
        "masked": {"polynomial_coefficients_ascending": masked_poly, "readings": masked,
                   "determinant": determinant(masked)},
        "checks": checks,
        "check_count": len(checks),
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = replay()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    elif json.loads(RESULT.read_text(encoding="utf-8")) != result:
        raise SystemExit("Saved SE39 model readings differ from exact replay")
    print(f"SE39: {result['check_count']} exact supplied-model controls passed; RH not certified")


if __name__ == "__main__":
    main()
