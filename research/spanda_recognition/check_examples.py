"""Direct exact controls for SP1's displayed examples; no numerical campaign.

Fractions are the rational coordinate realization of the declared cut scalars.
The six-coordinate jet example retains every coefficient through epsilon^2.
This script checks finite fixtures and immutable dependencies, not the general
proof, physical readings, a universal lambda carrier or the existing engine.
"""

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def matrix(rows):
    return tuple(tuple(Q(x) for x in row) for row in rows)


def vector(values):
    return tuple(Q(x) for x in values)


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def mul(a, b):
    return matrix([[sum(x * y for x, y in zip(row, col))
                    for col in zip(*b)] for row in a])


def act(a, v):
    return vector(sum(x * y for x, y in zip(row, v)) for row in a)


def add(a, b):
    return vector(x + y for x, y in zip(a, b))


def sub(a, b):
    return vector(x - y for x, y in zip(a, b))


def step(action, v):
    h, b = action
    return add(act(h, v), b)


def compose(later, earlier):
    h2, b2 = later
    h1, b1 = earlier
    return mul(h2, h1), add(b2, act(h2, b1))


def require(condition, name):
    if not condition:
        raise AssertionError(name)
    print(f"PASS {name}")


def main():
    pins = json.loads((HERE / "SOURCE_PINS.json").read_text())
    for path, expected in pins["sha256"].items():
        actual = sha256((ROOT / path).read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError(f"dependency changed: {path}")
    require(bool(pins["sha256"]), "unchanged dependency hashes")

    one = identity(2)
    j = matrix([[0, -1], [1, 0]])
    require(j != one and mul(mul(j, j), mul(j, j)) == one,
            "nonidentity quarter-turn has a four-step source return")

    a = (matrix([[1, 1], [0, 1]]), vector([1, 0]))
    b = (matrix([[1, 0], [1, 1]]), vector([0, 1]))
    c = (matrix([[-1, 0], [0, 1]]), vector([2, 3]))
    start = vector([2, -3])
    ba = compose(b, a)
    ab = compose(a, b)
    require(ba[1] == vector([1, 2]) and ab[1] == vector([2, 1])
            and step(ba, start) == step(b, step(a, start))
            and step(ba, start) != step(ab, start),
            "ordered transport rejects reversing the word or summing bare increments")
    require(compose(c, ba) == compose(compose(c, b), a)
            and step(compose(c, ba), start) == step(c, step(b, step(a, start))),
            "three-edge associativity agrees with direct sequential action")

    cancel = (matrix([[-1, 0], [0, -1]]), vector([2, 4]))
    fixed = vector([1, 2])
    require(step(cancel, fixed) == fixed
            and step(cancel, step(cancel, start)) == start,
            "nonzero raw increment can have a fixed point and a two-cycle")
    require(step((matrix([[2, 0], [0, 2]]), vector([0, 0])), start) != start,
            "zero obstruction does not reset every initial state")

    drift = (one, vector([0, 1]))
    m = vector([4, 0])
    for n in range(7):
        if m != vector([4, n]):
            raise AssertionError("translation clock or hidden coordinate")
        m = step(drift, m)
    require(True, "a fixed visible coordinate can hide a linear event count")

    shear = (matrix([[1, 1], [0, 1]]), vector([0, 1]))
    m = vector([0, 0])
    for n in range(7):
        if m != vector([Q(n * (n - 1), 2), n]):
            raise AssertionError("binomial memory law")
        m = step(shear, m)
    require(True, "transported increments produce the exact quadratic record")

    g = matrix([[1, 0], [1, 1]])
    gi = matrix([[1, 0], [-1, 1]])
    origin = vector([2, -1])
    hp = mul(mul(g, shear[0]), gi)
    bp = add(act(g, shear[1]), sub(origin, act(hp, origin)))
    shifted = add(act(g, start), origin)
    expected = add(act(g, step(shear, start)), origin)
    wrong_bp = sub(act(g, shear[1]), sub(origin, act(hp, origin)))
    require(step((hp, bp), shifted) == expected
            and step((hp, wrong_bp), shifted) != expected,
            "affine frame covariance detects the wrong origin-change sign")
    require(all(sub(vector([4, n]), vector([0, n])) == vector([4, 0])
                for n in range(7)),
            "a stationary compensated reading retains drift in calibration")

    # Complete K-basis: (x0,x1,x2,y0,y1,y2) in (K[e]/e^3)^2.
    rows = [list(row) for row in identity(6)]
    rows[1][3] = Q(1)
    rows[2][4] = Q(1)
    hjet = matrix(rows)
    bjet = vector([0, 0, 0, 0, 1, 0])
    jet = (hjet, bjet)
    z = vector([0] * 6)
    for n in range(7):
        expected = vector([0, 0, Q(n * (n - 1), 2), 0, n, 0])
        if z != expected or z[0] != 0 or z[3] != 0:
            raise AssertionError("full-jet return or zero reading")
        z = step(jet, z)
    require(True, "full-family coefficients accumulate while zero memory stays fixed")

    probes = [vector([0] * 6)] + [vector(row) for row in identity(6)]
    for z in probes:
        nxt = step(jet, z)
        if (nxt[0], nxt[3]) != (z[0], z[3]):
            raise AssertionError("specialization does not intertwine")
        if nxt[2] - z[2] != z[4] or nxt[4] - z[4] != 1:
            raise AssertionError("future-reading clock decoder")
    require(bjet[0] == bjet[3] == 0 and bjet[4] == 1,
            "future bank reads the clock and zero projection cannot decode it")
    epsilon = matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    u, v = vector([1, 0, 0]), vector([1, 0, 1])
    require(u != v and act(epsilon, u) == act(epsilon, v),
            "division by the nilpotent coefficient is not unique")
    require([(n + 1) % 3 for n in range(3)] == [1, 2, 0],
            "characteristic-three translation rejects dropping the rational hypothesis")
    print("SP1: 13 finite mathematical controls and dependency hashes passed.")


if __name__ == "__main__":
    main()
