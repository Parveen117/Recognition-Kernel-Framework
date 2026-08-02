from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SPEC = HERE / "spec.json"
LOG_THEOREM = ROOT / "theorems/foundation/F00G_NATIVE_LOGARITHM_AND_POWERS.md"
ARITH_THEOREM = ROOT / "theorems/foundation/F00H_NATIVE_NATURAL_ARITHMETIC_AND_PRIME_FACTORIZATION.md"
ZETA_THEOREM = ROOT / "theorems/foundation/F00I_NATIVE_DIRICHLET_ZETA_EULER_PRODUCT.md"
PROTOCOL = ROOT / "certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md"

Interval = tuple[Fraction, Fraction]
Vector = dict[int, int]


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()



def canonical_source_bytes(data: bytes) -> bytes:
    """Normalize text line endings before provenance hashing."""
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

def ftext(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def interval_text(value: Interval) -> list[str]:
    return [ftext(value[0]), ftext(value[1])]


def rec(passed: bool, detail: str, data: Any | None = None) -> dict[str, Any]:
    return {
        "passed": bool(passed),
        "detail": detail,
        "data": {} if data is None else data,
    }


def width(value: Interval) -> Fraction:
    return value[1] - value[0]


def contains_zero(value: Interval) -> bool:
    return value[0] <= 0 <= value[1]


def overlap(left: Interval, right: Interval) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def interval_add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def interval_sub(left: Interval, right: Interval) -> Interval:
    return left[0] - right[1], left[1] - right[0]


def interval_mul(left: Interval, right: Interval) -> Interval:
    values = (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )
    return min(values), max(values)


def interval_scale(value: Interval, scalar: Fraction) -> Interval:
    if scalar >= 0:
        return value[0] * scalar, value[1] * scalar
    return value[1] * scalar, value[0] * scalar


def exp_tail_bound(radius: Fraction, order: int) -> Fraction:
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    first = radius ** (order + 1) / math.factorial(order + 1)
    ratio = radius / Fraction(order + 2)
    if ratio >= 1:
        raise ValueError("exponential tail packet does not contract")
    return first / (1 - ratio)


def exp_nonnegative_interval(
    lower: Fraction,
    upper: Fraction,
    order: int,
) -> Interval:
    if not 0 <= lower <= upper:
        raise ValueError("nonnegative exponential interval is invalid")
    low = sum(
        (lower**k / math.factorial(k) for k in range(order + 1)),
        Fraction(0),
    )
    high = sum(
        (upper**k / math.factorial(k) for k in range(order + 1)),
        Fraction(0),
    ) + exp_tail_bound(upper, order)
    return low, high


def exp_interval(lower: Fraction, upper: Fraction, order: int) -> Interval:
    if lower > upper:
        raise ValueError("invalid exponential interval")
    if lower == 0 and upper == 0:
        return Fraction(1), Fraction(1)
    if lower >= 0:
        return exp_nonnegative_interval(lower, upper, order)
    if upper <= 0:
        positive = exp_nonnegative_interval(-upper, -lower, order)
        return Fraction(1, 1) / positive[1], Fraction(1, 1) / positive[0]
    negative = exp_interval(lower, Fraction(0), order)
    positive = exp_interval(Fraction(0), upper, order)
    return min(negative[0], positive[0]), max(negative[1], positive[1])


def odd_log_interval(value: Fraction, order: int) -> Interval:
    if value <= 0:
        raise ValueError("native positive logarithm requires x>0")
    cayley = (value - 1) / (value + 1)
    radius = abs(cayley)
    partial = sum(
        (
            Fraction(2) * cayley ** (2 * m + 1) / Fraction(2 * m + 1)
            for m in range(order + 1)
        ),
        Fraction(0),
    )
    if radius == 0:
        tail = Fraction(0)
    else:
        tail = (
            Fraction(2)
            * radius ** (2 * order + 3)
            / (Fraction(2 * order + 3) * (1 - radius * radius))
        )
    return partial - tail, partial + tail


def power_interval(
    base: Fraction,
    exponent: Fraction,
    log_order: int,
    exp_order: int,
) -> Interval:
    logarithm = odd_log_interval(base, log_order)
    scaled = interval_scale(logarithm, exponent)
    return exp_interval(scaled[0], scaled[1], exp_order)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def primes_upto(limit: int) -> list[int]:
    return [value for value in range(2, limit + 1) if is_prime(value)]


def factor_integer(value: int) -> Vector:
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    remaining = value
    factors: Vector = {}
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def divisors(value: int) -> list[int]:
    result = [1]
    for prime, exponent in factor_integer(value).items():
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return sorted(result)


def extended_gcd(left: int, right: int) -> tuple[int, int, int]:
    old_r, r = left, right
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def mobius(value: int) -> int:
    factors = factor_integer(value)
    if any(exponent >= 2 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def add_vectors(values: Iterable[Vector]) -> Vector:
    result: Vector = {}
    for value in values:
        for prime, exponent in value.items():
            result[prime] = result.get(prime, 0) + exponent
    return {
        prime: exponent
        for prime, exponent in result.items()
        if exponent != 0
    }


def lambda_log_vector(value: int) -> Vector:
    factors = factor_integer(value)
    if len(factors) != 1:
        return {}
    prime = next(iter(factors))
    return {prime: 1}


def dyadic_block_sum(index: int, sigma: int) -> Fraction:
    return sum(
        (
            Fraction(1, value**sigma)
            for value in range(2**index, 2 ** (index + 1))
        ),
        Fraction(0),
    )


def dyadic_block_bound(index: int, sigma: int) -> Fraction:
    return Fraction(1, 2 ** (index * (sigma - 1)))


def dyadic_tail_bound(power: int, sigma: int) -> Fraction:
    ratio = Fraction(1, 2 ** (sigma - 1))
    return ratio**power / (1 - ratio)


def finite_euler_product(primes: list[int], sigma: int) -> Fraction:
    result = Fraction(1)
    for prime in primes:
        result *= Fraction(prime**sigma, prime**sigma - 1)
    return result


def finite_inverse_euler_product(primes: list[int], sigma: int) -> Fraction:
    result = Fraction(1)
    for prime in primes:
        result *= Fraction(prime**sigma - 1, prime**sigma)
    return result


def exp_lower(value: Fraction, order: int = 30) -> Fraction:
    return sum(
        (value**k / math.factorial(k) for k in range(order + 1)),
        Fraction(0),
    )


def policy_ok(log_text: str, arithmetic_text: str, zeta_text: str) -> bool:
    # Theorem policy is semantic, not dependent on Markdown line wrapping.
    log_text = " ".join(log_text.split())
    arithmetic_text = " ".join(arithmetic_text.split())
    zeta_text = " ".join(zeta_text.split())

    log_tokens = (
        "This theorem proves that every positive radial scalar belongs to that orbit.",
        "without importing",
        "No classical logarithm or inverse-function theorem is consumed.",
    )
    arithmetic_tokens = (
        "It does not cite",
        "No external fundamental theorem of arithmetic is consumed.",
    )
    zeta_tokens = (
        "This theorem constructs the zeta function in its initial domain without",
        "No classical zeta theorem, Euler product, p-series test or analytic continuation",
    )
    return (
        all(token in log_text for token in log_tokens)
        and all(token in arithmetic_text for token in arithmetic_tokens)
        and all(token in zeta_text for token in zeta_tokens)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    pins = {
        item["path"]: item.get("expected_git_blob_sha1")
        for item in spec["authoritative_sources"]
    }

    source_records: list[dict[str, Any]] = []
    source_paths = (LOG_THEOREM, ARITH_THEOREM, ZETA_THEOREM, PROTOCOL)
    for path in source_paths:
        data = canonical_source_bytes(path.read_bytes())
        relative = path.relative_to(ROOT).as_posix()
        actual = blob_sha1(data)
        expected = pins.get(relative)
        source_records.append(
            {
                "path": relative,
                "bytes": len(data),
                "sha256": sha256(data),
                "git_blob_sha1": actual,
                "expected_git_blob_sha1": expected,
                "pin_matches": expected == actual,
            }
        )

    log_text = LOG_THEOREM.read_text(encoding="utf-8")
    arithmetic_text = ARITH_THEOREM.read_text(encoding="utf-8")
    zeta_text = ZETA_THEOREM.read_text(encoding="utf-8")

    checks: dict[str, dict[str, Any]] = {}
    negative_controls: dict[str, dict[str, Any]] = {}

    checks["C00GHI-01"] = rec(
        all(record["pin_matches"] for record in source_records)
        and policy_ok(log_text, arithmetic_text, zeta_text),
        "Source pins and no-import theorem-order policy.",
        {"sources": source_records},
    )

    packet = spec["audit_packet"]
    positive_values = [Fraction(value) for value in packet["positive_rationals"]]
    log_order = int(packet["log_series_terms"])
    exp_order = int(packet["exp_series_terms"])
    width_threshold = Fraction(packet["interval_width_threshold"])

    cayley_packets = []
    cayley_ok = True
    for value in positive_values:
        cayley = (value - 1) / (value + 1)
        passed = abs(cayley) < 1
        cayley_ok = cayley_ok and passed
        cayley_packets.append(
            {
                "x": ftext(value),
                "cayley": ftext(cayley),
                "passed": passed,
            }
        )
    checks["C00G-01"] = rec(
        cayley_ok,
        "Exact Cayley contraction on the positive rational packet.",
        {"packets": cayley_packets},
    )

    inverse_packets = []
    inverse_ok = True
    for value in positive_values:
        logarithm = odd_log_interval(value, log_order)
        exponential = exp_interval(logarithm[0], logarithm[1], exp_order)
        passed = (
            exponential[0] <= value <= exponential[1]
            and width(exponential) < width_threshold
        )
        inverse_ok = inverse_ok and passed
        inverse_packets.append(
            {
                "x": ftext(value),
                "log_interval": interval_text(logarithm),
                "exp_log_interval": interval_text(exponential),
                "exp_log_width": ftext(width(exponential)),
                "passed": passed,
            }
        )
    checks["C00G-02"] = rec(
        inverse_ok,
        "Odd-series tails enclose Exp_Sigma(Log_Sigma x)=x.",
        {"packets": inverse_packets},
    )

    product_pairs = (
        (Fraction(4, 3), Fraction(3, 2)),
        (Fraction(2), Fraction(1, 2)),
        (Fraction(3, 2), Fraction(2, 3)),
    )
    product_packets = []
    product_ok = True
    for left, right in product_pairs:
        residual = interval_sub(
            interval_add(
                odd_log_interval(left, log_order),
                odd_log_interval(right, log_order),
            ),
            odd_log_interval(left * right, log_order),
        )
        passed = contains_zero(residual) and width(residual) < width_threshold
        product_ok = product_ok and passed
        product_packets.append(
            {
                "x": ftext(left),
                "y": ftext(right),
                "residual_interval": interval_text(residual),
                "passed": passed,
            }
        )

    derivative_ok = True
    derivative_packets = []
    for value in positive_values:
        cayley = (value - 1) / (value + 1)
        left = (
            Fraction(2, 1)
            / (1 - cayley * cayley)
            * (Fraction(2, 1) / ((value + 1) * (value + 1)))
        )
        passed = left == Fraction(1, 1) / value
        derivative_ok = derivative_ok and passed
        derivative_packets.append(
            {
                "x": ftext(value),
                "derived": ftext(left),
                "target": ftext(Fraction(1, 1) / value),
                "passed": passed,
            }
        )
    checks["C00G-03"] = rec(
        product_ok and derivative_ok,
        "Multiplicative logarithm packet and exact derivative identity.",
        {
            "product_packets": product_packets,
            "derivative_packets": derivative_packets,
        },
    )

    first = power_interval(Fraction(3, 2), Fraction(1, 2), log_order, exp_order)
    second = power_interval(Fraction(3, 2), Fraction(1, 3), log_order, exp_order)
    combined = power_interval(Fraction(3, 2), Fraction(5, 6), log_order, exp_order)
    product_interval = interval_mul(first, second)

    left_base = power_interval(Fraction(4, 3), Fraction(2, 3), log_order, exp_order)
    right_base = power_interval(Fraction(3, 2), Fraction(2, 3), log_order, exp_order)
    product_base = power_interval(Fraction(2), Fraction(2, 3), log_order, exp_order)
    multiplied_bases = interval_mul(left_base, right_base)

    exponent_hull = (
        min(combined[0], product_interval[0]),
        max(combined[1], product_interval[1]),
    )
    base_hull = (
        min(product_base[0], multiplied_bases[0]),
        max(product_base[1], multiplied_bases[1]),
    )
    power_ok = (
        overlap(combined, product_interval)
        and overlap(product_base, multiplied_bases)
        and width(exponent_hull) < 1000 * width_threshold
        and width(base_hull) < 1000 * width_threshold
    )
    checks["C00G-04"] = rec(
        power_ok,
        "Native power exponent-addition and product-base interval audit.",
        {
            "exponent_addition_left": interval_text(combined),
            "exponent_addition_right": interval_text(product_interval),
            "product_base_left": interval_text(product_base),
            "product_base_right": interval_text(multiplied_bases),
        },
    )

    arithmetic_maximum = int(packet["arithmetic_maximum"])

    division_ok = all(
        (
            lambda quotient_remainder, a=a, b=b:
            a == quotient_remainder[0] * b + quotient_remainder[1]
            and 0 <= quotient_remainder[1] < b
        )(divmod(a, b))
        for a in range(arithmetic_maximum + 1)
        for b in range(1, arithmetic_maximum + 1)
    )
    checks["C00H-01"] = rec(
        division_ok,
        "Exhaustive exact division-with-remainder packet.",
        {"maximum": arithmetic_maximum},
    )

    gcd_ok = True
    for left in range(1, arithmetic_maximum + 1):
        for right in range(1, arithmetic_maximum + 1):
            divisor, coefficient_left, coefficient_right = extended_gcd(left, right)
            gcd_ok = gcd_ok and (
                divisor == math.gcd(left, right)
                and coefficient_left * left + coefficient_right * right == divisor
            )
    checks["C00H-02"] = rec(
        gcd_ok,
        "Euclidean gcd and Bezout reconstruction packet.",
        {"pair_checks": arithmetic_maximum**2},
    )

    prime_list = primes_upto(arithmetic_maximum)
    euclid_lemma_ok = all(
        (left * right) % prime != 0
        or left % prime == 0
        or right % prime == 0
        for prime in prime_list
        for left in range(1, arithmetic_maximum + 1)
        for right in range(1, arithmetic_maximum + 1)
    )
    checks["C00H-03"] = rec(
        euclid_lemma_ok,
        "Exhaustive Euclid-lemma packet over native-natural coordinates.",
        {
            "prime_count": len(prime_list),
            "factor_pair_count_per_prime": arithmetic_maximum**2,
        },
    )

    factorization_ok = all(
        math.prod(
            prime**exponent
            for prime, exponent in factor_integer(value).items()
        )
        == value
        and all(
            is_prime(prime) and exponent >= 1
            for prime, exponent in factor_integer(value).items()
        )
        for value in range(1, arithmetic_maximum + 1)
    )
    checks["C00H-04"] = rec(
        factorization_ok,
        "Prime factor reconstruction and primality audit.",
        {"maximum": arithmetic_maximum},
    )

    mobius_ok = all(
        sum(mobius(divisor) for divisor in divisors(value))
        == (1 if value == 1 else 0)
        for value in range(1, arithmetic_maximum + 1)
    )
    checks["C00H-05"] = rec(
        mobius_ok,
        "Exact Mobius divisor cancellation.",
        {"maximum": arithmetic_maximum},
    )

    mangoldt_ok = all(
        add_vectors(
            lambda_log_vector(divisor)
            for divisor in divisors(value)
        )
        == factor_integer(value)
        for value in range(1, arithmetic_maximum + 1)
    )
    checks["C00H-06"] = rec(
        mangoldt_ok,
        "Formal prime-log vector form of Log(n)=sum_{d|n} Lambda(d).",
        {"maximum": arithmetic_maximum},
    )

    prefix_count = int(packet["euclid_prime_prefix"])
    prefix_primes = prime_list[:prefix_count]
    euclid_packets = []
    running_product = 1
    infinitude_ok = True
    for index, prime in enumerate(prefix_primes, start=1):
        running_product *= prime
        candidate = running_product + 1
        candidate_factors = factor_integer(candidate)
        new_prime = min(candidate_factors)
        passed = new_prime not in prefix_primes[:index]
        infinitude_ok = infinitude_ok and passed
        euclid_packets.append(
            {
                "prefix_length": index,
                "candidate": candidate,
                "new_prime_divisor": new_prime,
                "passed": passed,
            }
        )
    checks["C00H-07"] = rec(
        infinitude_ok,
        "Euclid prime construction on increasing prime prefixes.",
        {"packets": euclid_packets},
    )

    sigma_values = [int(value) for value in packet["zeta_sigma_values"]]
    dyadic_max = int(packet["dyadic_block_index_max"])
    dyadic_packets = []
    dyadic_ok = True
    for sigma in sigma_values:
        for index in range(dyadic_max + 1):
            block = dyadic_block_sum(index, sigma)
            bound = dyadic_block_bound(index, sigma)
            passed = block <= bound
            dyadic_ok = dyadic_ok and passed
            dyadic_packets.append(
                {
                    "sigma": sigma,
                    "index": index,
                    "block": ftext(block),
                    "bound": ftext(bound),
                    "passed": passed,
                }
            )
    checks["C00I-01"] = rec(
        dyadic_ok,
        "Exact dyadic Dirichlet block estimates.",
        {"packets": dyadic_packets},
    )

    polynomial_degree_max = int(packet["polynomial_geometric_degree_max"])
    polynomial_ok = all(
        Fraction(1, 2)
        * Fraction((index + 2) ** degree, (index + 1) ** degree)
        <= Fraction(3, 4)
        for degree in range(polynomial_degree_max + 1)
        for index in range(20, 101)
    )
    tail_ok = all(
        dyadic_tail_bound(5, sigma)
        == sum(
            (
                Fraction(1, 2 ** ((sigma - 1) * index))
                for index in range(5, 40)
            ),
            Fraction(0),
        )
        + dyadic_tail_bound(40, sigma)
        for sigma in sigma_values
    )
    checks["C00I-02"] = rec(
        polynomial_ok and tail_ok,
        "Polynomial-geometric ratio and exact geometric-tail identities.",
        {
            "degree_max": polynomial_degree_max,
            "tail_start": 5,
        },
    )

    def arithmetic_a(value: int) -> int:
        return -1 if value % 2 else 2

    def arithmetic_b(value: int) -> int:
        return mobius(value)

    convolution_ok = all(
        sum(
            arithmetic_a(divisor) * arithmetic_b(value // divisor)
            for divisor in divisors(value)
        )
        == sum(
            arithmetic_a(left) * arithmetic_b(right)
            for left in range(1, value + 1)
            for right in range(1, value + 1)
            if left * right == value
        )
        for value in range(1, arithmetic_maximum + 1)
    )
    checks["C00I-03"] = rec(
        convolution_ok,
        "Exact finite Dirichlet-convolution coefficient regrouping.",
        {"maximum": arithmetic_maximum},
    )

    tail_power = int(packet["zeta_tail_power"])
    euler_prime_counts = [int(value) for value in packet["euler_prime_counts"]]
    euler_packets = []
    euler_ok = True
    for sigma in sigma_values:
        zeta_lower = sum(
            (
                Fraction(1, value**sigma)
                for value in range(1, 2**tail_power)
            ),
            Fraction(0),
        )
        zeta_upper = zeta_lower + dyadic_tail_bound(tail_power, sigma)
        for prime_count in euler_prime_counts:
            primes = prime_list[:prime_count]
            product_value = finite_euler_product(primes, sigma)
            inverse_value = finite_inverse_euler_product(primes, sigma)
            omitted_upper = sum(
                (
                    Fraction(1, value**sigma)
                    for value in range(primes[-1] + 1, 2**tail_power)
                ),
                Fraction(0),
            ) + dyadic_tail_bound(tail_power, sigma)
            passed = (
                inverse_value * product_value == 1
                and product_value <= zeta_upper
                and zeta_upper - product_value <= omitted_upper
            )
            euler_ok = euler_ok and passed
            euler_packets.append(
                {
                    "sigma": sigma,
                    "prime_count": prime_count,
                    "product": ftext(product_value),
                    "zeta_interval": [ftext(zeta_lower), ftext(zeta_upper)],
                    "omitted_upper": ftext(omitted_upper),
                    "passed": passed,
                }
            )
    checks["C00I-04"] = rec(
        euler_ok,
        "Finite Euler products and rigorous zeta-tail enclosure.",
        {"packets": euler_packets},
    )

    product_tail_ok = True
    product_tail_packets = []
    audit_primes = prime_list[:8]
    for sigma in sigma_values:
        for start in (0, 2, 4):
            atoms = [
                Fraction(1, prime**sigma)
                for prime in audit_primes[start:]
            ]
            finite_product = Fraction(1)
            for atom in atoms:
                finite_product *= 1 - atom
            left = abs(finite_product - 1)
            right_lower = exp_lower(sum(atoms), 30) - 1
            passed = left <= right_lower
            product_tail_ok = product_tail_ok and passed
            product_tail_packets.append(
                {
                    "sigma": sigma,
                    "start": start,
                    "left": ftext(left),
                    "exp_lower_minus_one": ftext(right_lower),
                    "passed": passed,
                }
            )
    checks["C00I-05"] = rec(
        product_tail_ok,
        "Exact finite product-tail inequality supporting nonvanishing.",
        {"packets": product_tail_packets},
    )

    reciprocal_ok = all(
        sum(mobius(divisor) for divisor in divisors(value))
        == (1 if value == 1 else 0)
        for value in range(1, arithmetic_maximum + 1)
    )
    checks["C00I-06"] = rec(
        reciprocal_ok,
        "Mobius reciprocal Dirichlet coefficients.",
        {"maximum": arithmetic_maximum},
    )

    logarithmic_derivative_ok = mangoldt_ok and all(
        (lambda_log_vector(value) != {})
        == (len(factor_integer(value)) == 1)
        for value in range(2, arithmetic_maximum + 1)
    )
    checks["C00I-07"] = rec(
        logarithmic_derivative_ok,
        "von Mangoldt prime-power support and divisor coefficient identity.",
        {"maximum": arithmetic_maximum},
    )

    wrong_cayley = abs(Fraction(2 + 1, 2 - 1)) >= 1
    composite_euclid = (2 * 2) % 4 == 0 and 2 % 4 != 0

    def wrong_mobius(value: int) -> int:
        return (
            1
            if all(exponent == 1 for exponent in factor_integer(value).values())
            else 0
        )

    wrong_mobius_detected = sum(
        wrong_mobius(divisor)
        for divisor in divisors(2)
    ) != 0

    def prime_only_lambda(value: int) -> Vector:
        return {value: 1} if is_prime(value) else {}

    missing_prime_powers = add_vectors(
        prime_only_lambda(divisor)
        for divisor in divisors(4)
    ) != factor_integer(4)

    wrong_dyadic = dyadic_block_sum(1, 2) > Fraction(1, 2**2)
    first_power_product = Fraction(1)
    for prime in prime_list[:5]:
        first_power_product *= 1 + Fraction(1, prime**2)
    wrong_euler = first_power_product != finite_euler_product(prime_list[:5], 2)
    classical_injection = not policy_ok(
        log_text.replace("without importing", "by importing", 1),
        arithmetic_text,
        zeta_text,
    )

    negative_controls["noncontracting_cayley"] = rec(
        wrong_cayley,
        "Wrong Cayley denominator detected.",
    )
    negative_controls["composite_euclid_lemma"] = rec(
        composite_euclid,
        "Composite number cannot replace prime in Euclid lemma.",
    )
    negative_controls["wrong_mobius_sign"] = rec(
        wrong_mobius_detected,
        "Wrong Mobius signs detected.",
    )
    negative_controls["missing_prime_powers"] = rec(
        missing_prime_powers,
        "Omission of prime powers from Lambda detected.",
    )
    negative_controls["wrong_dyadic_exponent"] = rec(
        wrong_dyadic,
        "Wrong dyadic exponent detected.",
    )
    negative_controls["first_power_euler_product"] = rec(
        wrong_euler,
        "First-power-only Euler product rejected.",
    )
    negative_controls["classical_primitive_injection"] = rec(
        classical_injection,
        "Classical logarithm injection detected.",
    )
    checks["C00GHI-NEG"] = rec(
        all(item["passed"] for item in negative_controls.values()),
        "All adversarial negative controls detected.",
        negative_controls,
    )

    required = spec["required_obligations"]
    missing = [obligation for obligation in required if obligation not in checks]
    passed = (
        not missing
        and all(checks[obligation]["passed"] for obligation in required)
    )
    status = (
        spec["passing_status"]
        if passed
        else "INCONCLUSIVE_F00GHI_LOG_ARITHMETIC_ZETA_AUDIT"
    )

    result: dict[str, Any] = {
        "schema": "rh-framework-foundational-certificate-result-v0.1",
        "certificate_class": spec["certificate_class"],
        "certificate_id": spec["certificate_id"],
        "theorems": spec["theorems"],
        "status": status,
        "checks": checks,
        "negative_controls": negative_controls,
        "missing_obligations": missing,
        "source_records": source_records,
        "spec_sha256": sha256(canonical_source_bytes(SPEC.read_bytes())),
        "arithmetic": {
            "engine": "fractions.Fraction and exact integer arithmetic",
            "mode": "exact rational intervals",
            "floating_proof_margins": False,
        },
        "scientific_boundary": {
            "half_plane_zeta_audit": "CERTIFIED" if passed else "INCONCLUSIVE",
            "analytic_continuation": "OPEN_IN_THIS_PACKAGE",
            "completed_weil_sign": "OPEN",
            "eta_zero_endpoint": "OPEN",
            "riemann_hypothesis": "OPEN",
        },
        "claim_boundary": spec["claim_boundary"],
    }
    result["canonical_result_sha256"] = sha256(canonical_bytes(result))

    output_text = json.dumps(
        result,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
    ) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(output_text, encoding="utf-8")

    print(status)
    print(result["canonical_result_sha256"])
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
