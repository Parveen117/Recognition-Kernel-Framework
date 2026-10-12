"""SE17: a complete global certificate for a family of comparison weights.

Retains sixteen odd Gamma modes and every prime event. All spatial cells,
the removable boundary value, and both infinite tails have proved bounds.
Exploratory floating-point candidates are not loaded by this replay.
"""
from __future__ import annotations

import argparse
from decimal import localcontext
from fractions import Fraction as F
import json
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import I, log_positive, sqrt_integer
    from proof_lab.endpoint_precision_frontier_certificate import refined_constants
    from proof_lab.endpoint_signed_return_certificate import (
        MG_CAP, POLE_CAP, OUTER_ROOT, prime_catalogue, prime_row_upper, rational,
    )
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import I, log_positive, sqrt_integer
    from endpoint_precision_frontier_certificate import refined_constants
    from endpoint_signed_return_certificate import (
        MG_CAP, POLE_CAP, OUTER_ROOT, prime_catalogue, prime_row_upper, rational,
    )

RESULT = Path(__file__).with_name('ENDPOINT_WEIGHT_FAMILY_RESULT.json')
ETA, FLOOR = F(59, 100), F(1, 1000)
NATIVE_FLOOR = FLOOR/(2+MG_CAP)
ALPHAS = (F(21, 40), F(53, 100))
GAMMA_MODES = 16
GAMMA_CONSTANT = sum((F(4, 4*k+1) for k in range(GAMMA_MODES)), F(0))


def difference_quotient(a, b):
    """Exact coefficients of (z**a-z**b)/(1-z), including z=1."""
    coeff = [F(0)]*max(a, b)
    for j in range(min(a, b), max(a, b)):
        coeff[j] = F(1 if a < b else -1)
    return coeff


def gamma_polynomial(modes=GAMMA_MODES):
    """Numerator of the Gamma lower potential over 1+z+z^2+z^3."""
    if not isinstance(modes, int) or modes < 1:
        raise ValueError('A positive finite mode count is required')
    coeff = [F(0)]*max(10, 4*(modes-1)+3)
    constant = sum((F(4, 4*k+1) for k in range(modes)), F(0))
    for j in range(6, 10):
        coeff[j] += constant-MG_CAP
    for k in range(modes):
        b = 4*k+1
        c2, c4 = F(4*b, 16-b*b), F(4*b, 64-b*b)
        for j, value in enumerate(difference_quotient(4*k+3, 6)):
            coeff[j] -= c2*value
        for j, value in enumerate(difference_quotient(4*k+3, 10)):
            coeff[j] += c4*value
    return coeff


GAMMA_POLYNOMIAL = gamma_polynomial()


def polynomial(coeff, z):
    out = I(0) if isinstance(z, I) else F(0)
    for value in reversed(coeff):
        out = out*z+value
    return out


def gamma_lower(z, coeff=GAMMA_POLYNOMIAL):
    return polynomial(coeff, z)/(1+z+z*z+z**3)


def add_auxiliary_catalogue(cat):
    """Positive head and full integral tail at exponent 11/2."""
    m = cat['limit']
    prefix, suffix = [I(0)]*(m+1), [I(0)]*(m+1)
    roots = [I(0)]+[sqrt_integer(n) for n in range(1, m+1)]
    for n in range(1, m+1):
        prefix[n] = prefix[n-1]+cat['weights'][n]*n**4*roots[n]
    for n in range(m-1, -1, -1):
        j = n+1
        suffix[n] = suffix[n+1]+cat['weights'][j]/(j**5*roots[j])
    tail = (F(2, 9)*cat['log_limit']+F(4, 81))/(m**4*roots[m])
    return dict(cat, aux_prefix=prefix, aux_suffix=suffix, aux_roots=roots,
                aux_tail=tail, aux_mass=suffix[0]+I(0, tail.hi))


def auxiliary_row_lower(left, right, cat):
    """A lower bound on the whole row V_(7/2); not a two-sided enclosure."""
    left, right = F(left), F(right)
    if not 0 < left <= right <= 1:
        raise ValueError('A spatial cell in (0,1] is required')
    low, high = int(1/right**2), int(1/left**2)
    if high > cat['limit']:
        raise ValueError('The exterior requires its separate analytic bound')
    out = left**6*(cat['aux_prefix'][low]+cat['aux_mass'])
    out = out+cat['aux_suffix'][high]/right**14
    for n in range(low+1, high+1):
        w, root = cat['weights'][n], cat['aux_roots'][n]
        increasing = w*n**4*root*left**6
        decreasing = w/(n**5*root*right**14)
        # On a cell a unimodal min of these two branches is at least
        # their smaller endpoint lower bound. An omitted tail is positive.
        out = out+I(min(increasing.lo, decreasing.lo))
    return out.lo


def shaped_prime_upper(left, right, cat, alpha):
    alpha = F(alpha)
    if not 0 <= alpha < 1:
        raise ValueError('The even prime weight must be strictly positive')
    base = prime_row_upper(left, right, cat)
    aux_lower = auxiliary_row_lower(left, right, cat)
    z = I(left, right)
    numerator = base-alpha*z**6*I(aux_lower)
    # The exact numerator is positive, as it is Kq with a positive kernel
    # and q=e^(-|x|/2)*(1-alpha*e^(-3|x|)).
    if numerator.hi < 0:
        raise AssertionError('Inconsistent positive row enclosure')
    denominator_lower = I(1-alpha*F(right)**6).lo
    return I(numerator.hi)/I(denominator_lower)


def comparison_cell(left, right, cat, alpha, eta=ETA):
    eta = F(eta)
    if not 0 < eta < 1:
        raise ValueError('The signed graph decomposition uses 0 < eta < 1')
    z = I(left, right)
    diagonal = eta-POLE_CAP+(eta+POLE_CAP)*z**6
    return diagonal+(1-eta)*gamma_lower(z)-shaped_prime_upper(left, right, cat, alpha)


def exterior_bound(cat):
    m, root, logm = cat['limit'], sqrt_integer(cat['limit']), cat['log_limit']
    base = (F(16, 15)*logm+F(4, 9))/root+2*logm/(m*root)+cat['mass']/m**3
    shaped = base/(1-ALPHAS[-1]/m**3)
    # Every remaining z is in [0,1/64]; the polynomial denominator >=1.
    gamma_abs = polynomial([abs(c) for c in GAMMA_POLYNOMIAL], I(F(1, OUTER_ROOT)))
    lower = ETA-POLE_CAP-(1-ETA)*gamma_abs-shaped
    return dict(base_prime=base, shaped_prime=shaped, gamma_absolute=gamma_abs, lower=lower)


def cover(cat, floor=FLOOR):
    if cat['limit'] != OUTER_ROOT**2:
        raise ValueError('The catalogue must agree with the exact exterior split')
    stack, accepted = [(F(1, OUTER_ROOT), F(1), 0)], []
    while stack:
        left, right, depth = stack.pop()
        lower = [comparison_cell(left, right, cat, alpha).lo for alpha in ALPHAS]
        if min(F(v) for v in lower) >= floor:
            accepted.append((left, right, lower, depth))
        else:
            if depth >= 25:
                raise AssertionError(f'Uncertified family cell {left}, {right}, {lower}')
            middle = (left+right)/2
            stack.extend(((middle, right, depth+1), (left, middle, depth+1)))
    assert accepted[0][0] == F(1, OUTER_ROOT) and accepted[-1][1] == 1
    assert all(a[1] == b[0] for a, b in zip(accepted, accepted[1:]))
    return accepted


def _replay():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name, status='PASS'))
    cat = add_auxiliary_catalogue(prime_catalogue())
    _, _, mg = refined_constants()
    check('inherited_gamma_ground_cap', mg.hi < I(MG_CAP).lo)
    check('inherited_complete_pole_cap', (log_positive(3)-1).hi < I(POLE_CAP).lo)
    check('positive_prime_family', 0 <= ALPHAS[0] < ALPHAS[-1] < 1)
    check('sixteen_complete_retained_gamma_modes', len(GAMMA_POLYNOMIAL) == 63)
    boundary_row = sum((2*F(4*k+1, 2)/((F(4*k+1, 2)+2)*(F(4*k+1, 2)+4))
                        for k in range(GAMMA_MODES)), F(0))
    check('exact_removable_gamma_boundary', gamma_lower(F(1)) == GAMMA_CONSTANT-MG_CAP-boundary_row)
    check('positive_entire_auxiliary_mass', cat['aux_mass'].lo > 0)
    check('entire_auxiliary_tail_smaller_than_one_over_10_power_15', cat['aux_tail'].hi < I(F(1, 10**15)).lo)
    cells = cover(cat)
    check('complete_spatial_cover', all(F(v) >= FLOOR for row in cells for v in row[2]))
    outer = exterior_bound(cat)
    check('exterior_logarithmic_monotonicity', cat['log_limit'].lo > 2)
    check('entire_exterior_for_the_whole_family', outer['lower'].lo > I(FLOOR).hi)
    check('native_metric_floor', NATIVE_FLOOR == F(1, 7380))
    check('positive_gamma_energy_covers_native_floor', ETA > NATIVE_FLOOR)
    check('improvement_over_SE16_implied_shift', ETA < F(25441, 36900))
    # Same Gamma weight and same source, but erase the prime shape.
    # At exp(x)=3 the exact old prime row has a lower enclosure.
    z = 1/sqrt_integer(3)
    plain_prime = (cat['prefix'][3]+cat['mass'])/27+3*(cat['suffix'][3]+I(0, cat['tail'].hi))
    unshaped = ETA-POLE_CAP+(ETA+POLE_CAP)/27+(1-ETA)*gamma_lower(z)-plain_prime
    check('unshaped_comparison_fails_at_same_eta', unshaped.hi < 0)
    return dict(schema='rkf.endpoint-weight-family-certificate.v1', date='2026-10-12',
        status='PASS_GLOBAL_WEIGHT_FAMILY', check_count=len(checks), checks=checks,
        arithmetic='Exact Fraction and inherited 90-digit outward Decimal intervals',
        global_source=dict(eta=rational(ETA), shifted_native_floor=rational(NATIVE_FLOOR),
            spatial_floor=rational(FLOOR), implied_nonnegative_shift=rational(ETA-NATIVE_FLOOR),
            invariant_negative_count=0, nullity=0, eta_zero_certified=False,
            scope='Entire corrected complex odd native source; every eta >= 59/100'),
        weights=dict(gamma='exp(-x/2)*(1-exp(-2*x)), x>0',
            prime='exp(-abs(x)/2)*(1-alpha*exp(-3*abs(x)))',
            alpha_closed_interval=[rational(a) for a in ALPHAS],
            family_rule='Pointwise affine inequality in the whole weight, before division; no pointwise switching',
            gamma_modes=GAMMA_MODES, gamma_constant=rational(GAMMA_CONSTANT),
            gamma_polynomial=[rational(c) for c in GAMMA_POLYNOMIAL],
            gamma_denominator=['1/1']*4, positive_square_residuals=True),
        primes=dict(cutoff=cat['limit'], prime_power_count=cat['prime_power_count'],
            catalogue_sha256=cat['catalogue_sha256'],
            base_mass_exponent='5/2', base_mass=cat['mass'].record(), base_tail=cat['tail'].record(),
            auxiliary_mass_exponent='11/2', auxiliary_mass=cat['aux_mass'].record(),
            auxiliary_tail=cat['aux_tail'].record()),
        spatial_cover=dict(left=rational(F(1, OUTER_ROOT)), right='1/1',
            cells=len(cells), endpoint_weight_checks=2*len(cells),
            maximum_depth=max(r[3] for r in cells),
            minimum_lower=str(min(v for row in cells for v in row[2])),
            records=[dict(left=rational(a), right=rational(b),
                          endpoint_lowers=[str(v) for v in vv], depth=d) for a,b,vv,d in cells]),
        infinite_exterior={k:v.record() for k,v in outer.items()},
        comparison_control=dict(point='x=log(3)', erased_prime_shape=unshaped.record(),
            same_gamma_weight=True, negative_source_claim=False),
        prior_local_frontier=dict(radius='21/25', stage='SE14', unchanged=True),
        not_certified=['eta=1/2', 'eta-zero positivity or RH', 'global critical observer contraction',
            'arbitrary pointwise weight switching', 'historical five-label endpoint or K0',
            'formal verification or external review'])


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
        raise SystemExit('SE17 replay mismatch: inspect rather than repinning.')
    print(json.dumps(dict(status=result['status'], checks=result['check_count'],
        global_source=result['global_source'], cells=result['spatial_cover']['cells'],
        minimum_lower=result['spatial_cover']['minimum_lower']), indent=2))


if __name__ == '__main__':
    main()
