"""Exact finite calibration for MR-07; the general limit proof is in its capsule.

No floating-point asymptotic experiment and no proof-assistant claim are made.
All public bound evaluators require exact rational inputs and a declared domain.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Any

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
Polynomial = tuple[Matrix, ...]  # ascending powers of h


def _q(value: int | Fraction) -> Fraction:
    if not isinstance(value, (int, Fraction)):
        raise TypeError("exact integer or Fraction required")
    return Fraction(value)


def matrix(a: int | Fraction, b: int | Fraction,
           c: int | Fraction, d: int | Fraction) -> Matrix:
    return ((_q(a), _q(b)), (_q(c), _q(d)))


I = matrix(1, 0, 0, 1)
ZERO = matrix(0, 0, 0, 0)
X = matrix(0, 1, 0, 0)
Y = matrix(0, 0, 1, 0)


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2))
                 for i in range(2))  # type: ignore[return-value]


def scale(value: int | Fraction, a: Matrix) -> Matrix:
    q = _q(value)
    return tuple(tuple(q * a[i][j] for j in range(2))
                 for i in range(2))  # type: ignore[return-value]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2))
                 for i in range(2))  # type: ignore[return-value]


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return add(multiply(a, b), scale(-1, multiply(b, a)))


def norm_inf(a: Matrix) -> Fraction:
    return max(sum(abs(value) for value in row) for row in a)


def _trim(coefficients: list[Matrix]) -> Polynomial:
    while len(coefficients) > 1 and coefficients[-1] == ZERO:
        coefficients.pop()
    return tuple(coefficients)


def polynomial_multiply(a: Polynomial, b: Polynomial) -> Polynomial:
    result = [ZERO for _ in range(len(a) + len(b) - 1)]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            result[i + j] = add(result[i + j], multiply(left, right))
    return _trim(result)


def nilpotent_euler_holonomy_coefficients(x: Matrix, y: Matrix) -> Polynomial:
    """Coefficients of (I+hX)(I+hY)(I-hX)(I-hY), requiring X²=Y²=0."""
    if multiply(x, x) != ZERO or multiply(y, y) != ZERO:
        raise ValueError("exact Euler inverse requires square-zero generators")
    result = (I,)
    for generator in (x, y, scale(-1, x), scale(-1, y)):
        result = polynomial_multiply(result, (I, generator))
    return result


def determinant_coefficients(p: Polynomial) -> tuple[Fraction, ...]:
    result = [Fraction(0) for _ in range(2 * len(p) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(p):
            result[i + j] += a[0][0] * b[1][1] - a[0][1] * b[1][0]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def evaluate(p: Polynomial, h: int | Fraction) -> Matrix:
    h = _q(h)
    result = ZERO
    for coefficient in reversed(p):
        result = add(scale(h, result), coefficient)
    return result


def matrix_power(a: Matrix, n: int) -> Matrix:
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer power required")
    result = I
    while n:
        if n & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        n //= 2
    return result


def exp_upper_rational(x: int | Fraction) -> Fraction:
    """Exact majorant exp(x) <= (1-x/m)^(-m), m=floor(x)+1."""
    x = _q(x)
    if x < 0:
        raise ValueError("nonnegative exponent required")
    m = x.numerator // x.denominator + 1
    return (1 - x / m) ** (-m)


def _bound_inputs(h: int | Fraction, n: int, k: int | Fraction,
                  c: int | Fraction, h0: int | Fraction
                  ) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    h, k, c, h0 = map(_q, (h, k, c, h0))
    if type(n) is not int or n <= 0:
        raise ValueError("positive integer repetition count required")
    if h0 <= 0 or not 0 <= h <= h0 or k < 0 or c < 0:
        raise ValueError("require h0>0, 0<=h<=h0, k>=0, c>=0")
    return h, k, c, h0


def holonomy_error_bound(h: int | Fraction, n: int, k: int | Fraction,
                         c: int | Fraction, h0: int | Fraction) -> Fraction:
    """Rational bound on ||H_h^n-exp(nh²K)|| under the MR-07 datum.

    This evaluates a conditional bound; it does not verify a caller's remainder
    hypothesis ||R_h||<=c h³ or the claimed k>=||K||.
    """
    h, k, c, _ = _bound_inputs(h, n, k, c, h0)
    step_error = c * h**3 + h**4 * k**2 * exp_upper_rational(h*h*k) / 2
    return n * step_error * exp_upper_rational(n*h*h*(k+c*h))


def identity_error_bound(h: int | Fraction, n: int, k: int | Fraction,
                         c: int | Fraction, h0: int | Fraction) -> Fraction:
    """Rational bound on ||H_h^n-I|| under the same declared hypotheses."""
    h, k, c, _ = _bound_inputs(h, n, k, c, h0)
    a = n*h*h*(k+c*h)
    return a * exp_upper_rational(a)


def _check(check_id: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"id": check_id, "status": "pass" if passed else "fail", "detail": detail}


def _encoded(a: Matrix) -> list[list[str]]:
    return [[str(value) for value in row] for row in a]


def verify_holonomy_contract() -> dict[str, Any]:
    """Finite exact witnesses for MR-07, not a numerical proof of convergence."""
    coefficients = nilpotent_euler_holonomy_coefficients(X, Y)
    k = commutator(X, Y)
    l = matrix(0, -1, 1, 0)
    q = matrix(1, 0, 0, 0)
    checks = [
        _check("MR07-O1", multiply(X, X) == ZERO and multiply(Y, Y) == ZERO
               and polynomial_multiply((I, X), (I, scale(-1, X))) == (I,)
               and polynomial_multiply((I, Y), (I, scale(-1, Y))) == (I,),
               {"square_zero_generators": [_encoded(X), _encoded(Y)]}),
        _check("MR07-O2", coefficients == (I, ZERO, k, l, q)
               and k == matrix(1, 0, 0, -1)
               and determinant_coefficients(coefficients) == (Fraction(1),),
               {"loop_coefficients": [_encoded(a) for a in coefficients],
                "determinant_coefficients": [str(x) for x in determinant_coefficients(coefficients)]}),
        _check("MR07-O3", norm_inf(k) == 1 and norm_inf(l) == 1 and norm_inf(q) == 1,
               {"k": str(norm_inf(k)), "C": str(norm_inf(l) + norm_inf(q)),
                "h0": "1", "remainder_proof": "h^3||L||+h^4||Q||<=2h^3 for 0<=h<=1"}),
    ]
    scales = (8, 16, 32)
    bounds = [holonomy_error_bound(Fraction(1, m), m*m, 1, 2, 1) for m in scales]
    checks.append(_check("MR07-O4", all(m*m*Fraction(1, m)**2 == 1 for m in scales)
                         and all(left > right > 0 for left, right in zip(bounds, bounds[1:])),
                         {"tau": "1", "evaluations": [
                             {"h": str(Fraction(1, m)), "n": m*m, "error_upper": str(bound)}
                             for m, bound in zip(scales, bounds)],
                          "role": "finite exact bound evaluations; general rate proved in capsule"}))
    checks.append(_check("MR07-O5", evaluate(coefficients, 0) == I
                         and holonomy_error_bound(0, 1, 1, 2, 1) == 0
                         and nilpotent_euler_holonomy_coefficients(X, X) == (I,),
                         {"zero_area": "identity", "equal_generators": "identity polynomial"}))
    wrong_bound = identity_error_bound(Fraction(1, 8), 8, 1, 2, 1)
    exact_distance = norm_inf(add(matrix_power(evaluate(coefficients, Fraction(1, 8)), 8), scale(-1, I)))
    checks.append(_check("MR07-N1", exact_distance <= wrong_bound == Fraction(5, 27)
                         and 1 - wrong_bound == Fraction(22, 27) > 0,
                         {"n": 8, "h": "1/8", "identity_distance": str(exact_distance),
                          "identity_upper": str(wrong_bound),
                          "exp_K_distance_strict_lower": "22/27",
                          "all_n_ge_8_proof": "a_n=(1+2/n)/n decreases; ||exp(K)-I||=e-1>1"}))
    reversed_coefficients = nilpotent_euler_holonomy_coefficients(Y, X)
    checks.append(_check("MR07-N2", reversed_coefficients[2] == scale(-1, k)
                         and reversed_coefficients[2] != k,
                         {"reversed_quadratic_coefficient": _encoded(reversed_coefficients[2])}))
    return {
        "theorem_id": "MR-07",
        "status": "RNKE_CONTRACT_VERIFIED" if all(c["status"] == "pass" for c in checks) else "REJECTED",
        "checks": checks,
        "claim_boundary": {
            "general_proof": "finite matrices, explicit uniform remainder contract",
            "executable_role": "exact polynomial identities, rational bounds, and negative controls",
            "formal_proof_assistant": False,
            "unbounded_operators": "excluded",
            "other_manuscript_claims": "not certified by this contract",
        },
    }
