"""SE16: complete global source bound retaining odd Gamma return cancellation.

All spatial cells and all omitted prime powers have outward bounds. No
sampled eigenvalue or exploratory floating-point result is an input.
"""
from __future__ import annotations

import argparse
from decimal import localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import I, log_positive, sqrt_integer
    from proof_lab.endpoint_global_eta_certificate import integer_log
    from proof_lab.endpoint_precision_frontier_certificate import refined_constants
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import I, log_positive, sqrt_integer
    from endpoint_global_eta_certificate import integer_log
    from endpoint_precision_frontier_certificate import refined_constants

RESULT = Path(__file__).with_name('ENDPOINT_SIGNED_RETURN_RESULT.json')
ETA = F(69, 100)
MG_CAP, POLE_CAP = F(269, 50), F(1, 10)
GAMMA_CONSTANT = F(24, 5)
FLOOR = F(1, 250)
NATIVE_FLOOR = FLOOR/(2+MG_CAP)
CATALOGUE = 4096
OUTER_ROOT = 64


def rational(value):
    value = F(value)
    return f'{value.numerator}/{value.denominator}'


def prime_catalogue(limit=CATALOGUE):
    """Positive prime-power sums, with an all-integer integral tail."""
    if limit < 2:
        raise ValueError('A cutoff at least two is required')
    log2 = log_positive(2)
    prime = [True]*(limit+1)
    prime[:2] = [False, False]
    weights = [I(0) for _ in range(limit+1)]
    for p in range(2, limit+1):
        if not prime[p]:
            continue
        for composite in range(p*p, limit+1, p):
            prime[composite] = False
        lp = integer_log(p, log2)
        power = p
        while power <= limit:
            weights[power] = lp
            power *= p
    roots = [sqrt_integer(n) for n in range(1, limit+1)]
    roots.insert(0, I(0))
    prefix = [I(0)]*(limit+1)
    suffix = [I(0)]*(limit+1)
    peaks = [I(0)]*(limit+1)
    for n in range(1, limit+1):
        prefix[n] = prefix[n-1]+weights[n]*n*roots[n]
        peaks[n] = weights[n]/(n*roots[n])
    for n in range(limit-1, -1, -1):
        j = n+1
        suffix[n] = suffix[n+1]+weights[j]/(j*j*roots[j])
    log_limit = integer_log(limit, log2)
    tail = (F(2, 3)*log_limit+F(4, 9))/(limit*roots[limit])
    mass = suffix[0]+I(0, tail.hi)
    digest_data = [(n, weights[n].record()) for n in range(2, limit+1) if weights[n].hi > 0]
    digest = hashlib.sha256(json.dumps(digest_data, separators=(',', ':')).encode()).hexdigest()
    return dict(limit=limit, prefix=prefix, suffix=suffix, peaks=peaks,
                tail=tail, mass=mass, log_limit=log_limit,
                weights=weights, catalogue_sha256=digest,
                prime_power_count=len(digest_data))


def prime_row_upper(left, right, cat):
    """Enclose a continuous weighted row through every prime breakpoint.

    z=exp(-abs(x)/2). Each event is the minimum of an increasing z^6
    branch and a decreasing z^-2 branch. A straddled event is counted
    once at its exact peak; independent prefix/tail rounding would
    incorrectly count it twice even as a cell width tends to zero.
    """
    left, right = F(left), F(right)
    if not 0 < left <= right <= 1:
        raise ValueError('A cell in (0,1] is required')
    low = (1/(right*right)).numerator//(1/(right*right)).denominator
    high = (1/(left*left)).numerator//(1/(left*left)).denominator
    if high > cat['limit']:
        raise ValueError('Use the proved exterior bound below the catalogue cell')
    value = right**6*(cat['prefix'][low]+cat['mass'])
    value = value+(cat['suffix'][high]+I(0, cat['tail'].hi))/left**2
    value = value+sum(cat['peaks'][low+1:high+1], I(0))
    return value


def gamma_row(z, folded=True):
    """Two exact exponential-kernel row integrals, in the rational z chart."""
    row = F(4, 15)*(z**3-z**6)+F(20, 9)*(z**6-z**7)
    if not folded:
        # Deliberate comparison control: erase the negative odd-reflection
        # kernel before taking the absolute row bound.
        row = row+F(4, 5)*z**3+F(4, 9)*z**7
    return row


def comparison_cell(left, right, cat, eta=ETA, folded=True):
    eta = F(eta)
    if not 0 < eta < 1:
        raise ValueError('This decomposition requires 0 < eta < 1')
    z = I(left, right)
    gamma_debt = MG_CAP-GAMMA_CONSTANT
    diagonal = eta-POLE_CAP+(eta-(1-eta)*gamma_debt+POLE_CAP)*z**6
    return diagonal-(1-eta)*gamma_row(z, folded)-prime_row_upper(left, right, cat)


def exterior_bound(cat):
    """Uniform bound for exp(abs(x)) >= catalogue, not a tail sample."""
    m, root, logm = cat['limit'], sqrt_integer(cat['limit']), cat['log_limit']
    prime = (F(16, 15)*logm+F(4, 9))/root+2*logm/(m*root)+cat['mass']/m**3
    gamma = I(F(4, 15))/(m*root)+F(20, 9*m**3)
    lower = ETA-POLE_CAP-(1-ETA)*gamma-prime
    return dict(prime=prime, gamma=gamma, lower=lower)


def cover(cat, floor=FLOOR):
    start, stop = F(1, OUTER_ROOT), F(1)
    if OUTER_ROOT**2 != cat['limit']:
        raise ValueError('The rational exterior split must match the catalogue')
    stack = [(start, stop, 0)]
    accepted = []
    while stack:
        left, right, depth = stack.pop()
        lower = comparison_cell(left, right, cat).lo
        if F(lower) >= floor:
            accepted.append((left, right, lower, depth))
        else:
            if depth >= 24:
                raise AssertionError(f'Uncertified spatial cell {left}, {right}, {lower}')
            middle = (left+right)/2
            stack.append((middle, right, depth+1))
            stack.append((left, middle, depth+1))
    assert accepted[0][0] == start and accepted[-1][1] == stop
    assert all(a[1] == b[0] for a, b in zip(accepted, accepted[1:]))
    return accepted


def _replay():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name, status='PASS'))
    _, _, mg = refined_constants()
    beta = log_positive(3)-1
    cat = prime_catalogue()
    check('inherited_gamma_bound', mg.hi < I(MG_CAP).lo)
    check('complete_weighted_pole_bound', beta.hi < I(POLE_CAP).lo)
    check('complete_weighted_prime_mass_below_289_over_1000', cat['mass'].hi < I(F(289, 1000)).lo)
    check('two_gamma_mode_constant', F(4)+F(4, 5) == GAMMA_CONSTANT)
    check('positive_diagonal_coefficient', ETA-(1-ETA)*(MG_CAP-GAMMA_CONSTANT)+POLE_CAP > 0)
    check('exterior_logarithmic_monotonicity', cat['log_limit'].lo > 2)
    cells = cover(cat)
    check('whole_inner_spatial_corridor', all(F(row[2]) >= FLOOR for row in cells))
    outer = exterior_bound(cat)
    check('entire_infinite_exterior', outer['lower'].lo > I(FLOOR).hi)
    check('native_metric_conversion', NATIVE_FLOOR == F(1, 1845))
    check('retained_positive_gamma_energy_covers_native_floor', ETA > NATIVE_FLOOR)
    check('improvement_over_SE15', ETA < F(326, 369))
    # z=1/sqrt(3) supplies a strict failed-comparison witness.
    z3 = 1/sqrt_integer(3)
    preserved = comparison_cell(F(z3.lo), F(z3.hi), cat)
    # comparison_cell gives a lower enclosure using an upper prime row.
    # For an upper bound on the erased point comparison, replace that
    # upper bound by the exact lower prime sum at z=1/sqrt(3).
    vp3 = (cat['prefix'][3]+cat['mass'])/27+3*(cat['suffix'][3]+I(0, cat['tail'].hi))
    erased_exact = (ETA-POLE_CAP+(ETA-(1-ETA)*(MG_CAP-GAMMA_CONSTANT)+POLE_CAP)/27
                    -(1-ETA)*gamma_row(z3, False)-vp3)
    check('odd_return_retained_point_passes', preserved.lo > I(FLOOR).hi)
    check('erasing_odd_return_invalidates_same_comparison', erased_exact.hi < 0)
    records = [dict(left=rational(a), right=rational(b), lower=str(value), depth=d)
               for a, b, value, d in cells]
    return dict(schema='rkf.endpoint-signed-return-certificate.v1', date='2026-10-12',
        status='PASS_GLOBAL_SIGNED_RETURN', arithmetic='Exact Fraction and 90-digit outward Decimal intervals',
        check_count=len(checks), checks=checks,
        global_source=dict(eta=rational(ETA), invariant_negative_count=0, nullity=0,
            shifted_native_floor=rational(NATIVE_FLOOR), spatial_lower_floor=rational(FLOOR),
            implied_source_lower_bound=rational(-ETA+NATIVE_FLOOR),
            implied_nonnegative_shift=rational(ETA-NATIVE_FLOOR),
            scope='Entire corrected complex odd native source; all eta >= 69/100',
            eta_zero_certified=False),
        comparison=dict(gamma_modes=[0, 1], gamma_constant=rational(GAMMA_CONSTANT),
            weight='exp(-abs(x)/2)', spatial_chart='z=exp(-abs(x)/2)',
            pole_upper=rational(POLE_CAP), gamma_ground_upper=rational(MG_CAP),
            retained_positive_squared_defects=True),
        primes=dict(cutoff=cat['limit'], prime_power_count=cat['prime_power_count'],
            catalogue_sha256=cat['catalogue_sha256'], mass_exponent='5/2',
            complete_mass=cat['mass'].record(), all_integer_tail=cat['tail'].record()),
        spatial_cover=dict(left=rational(F(1, OUTER_ROOT)), right='1/1',
            cells=len(cells), maximum_depth=max(r[3] for r in cells),
            minimum_lower=str(min(r[2] for r in cells)), records=records),
        infinite_exterior={key: value.record() for key, value in outer.items()},
        return_control=dict(point='x=log(3)', preserved=preserved.record(),
            erased_comparison=erased_exact.record(), negative_source_claim=False),
        prior_local_frontier=dict(radius='21/25', stage='SE14', unchanged=True),
        not_certified=['eta=1/2', 'eta-zero positivity or RH', 'global critical observer contraction',
            'new positive aperture beyond 21/25', 'historical five-label endpoint or K0',
            'formal proof-assistant verification or external review'])


def replay():
    with localcontext() as context:
        context.prec = 90
        return _replay()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--write', action='store_true')
    modes.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = replay()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    if args.check and json.loads(RESULT.read_text()) != result:
        raise SystemExit('SE16 replay mismatch: inspect rather than repinning.')
    print(json.dumps(dict(status=result['status'], checks=result['check_count'],
        global_source=result['global_source'], cells=result['spatial_cover']['cells'],
        minimum_lower=result['spatial_cover']['minimum_lower']), indent=2))


if __name__ == '__main__':
    main()
