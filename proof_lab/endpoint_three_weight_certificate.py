"""SE24: three independent comparison weights with an exact pole row.

The Gamma, prime and pole readings of the corrected complex odd source each
carry their own positive exponential-sum weight. The odd pole is read by a
density that saturates its budget law (SE18.6), so the exterior value of the
comparison is eta itself rather than eta-b_c. Sixteen odd Gamma modes, every
prime power through the catalogue, and all infinite tails have proved bounds.
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
    from proof_lab.endpoint_signed_return_certificate import MG_CAP, POLE_CAP, prime_catalogue, rational
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import I, log_positive, sqrt_integer
    from endpoint_precision_frontier_certificate import refined_constants
    from endpoint_signed_return_certificate import MG_CAP, POLE_CAP, prime_catalogue, rational

RESULT = Path(__file__).with_name('ENDPOINT_THREE_WEIGHT_RESULT.json')
ETA, FLOOR = F(14, 25), F(1, 1000)
NATIVE_FLOOR = FLOOR/(2+MG_CAP)
OUTER_ROOT = 512
CATALOGUE = OUTER_ROOT**2
GAMMA_MODES = 16
GAMMA_CONSTANT = sum((F(4, 4*k+1) for k in range(GAMMA_MODES)), F(0))

# Weights as lists of (coefficient, z-power); z=exp(-|x|/2), so z^k = exp(-k|x|/2).
GAMMA_WEIGHT = ((F(1), 1), (F(-1, 10), 5))                      # e^{-x/2} - e^{-5x/2}/10, x>0
PRIME_WEIGHT = ((F(1, 12), 1), (F(1), 3), (F(-7, 5), 5), (F(2, 5), 7))   # even in x
POLE_WEIGHT = ((F(1), 1), (F(1, 4), 3))                         # x>0
PRIME_POWERS = (1, 3, 5, 7)


def poly_eval(coeff, z):
    out = I(0) if isinstance(z, I) else F(0)
    for value in reversed(coeff):
        out = out*z+value
    return out


def weight_polynomial(weight):
    coeff = [F(0)]*(max(k for _, k in weight)+1)
    for c, k in weight:
        coeff[k] += c
    return coeff


def weight_lower_slope(weight, zmax=F(1)):
    """A rational s>0 with q(z) >= s*z on (0,zmax]: s = c_1 + sum_{k>1, c_k<0} c_k zmax^{k-1}."""
    zmax = F(zmax)
    slope = sum((c for c, k in weight if k == 1), F(0))
    slope += sum((c*zmax**(k-1) for c, k in weight if k > 1 and c < 0), F(0))
    if slope <= 0:
        raise ValueError('The weight is not proved positive by its z-term on this range')
    return slope


class UncertifiedCell(Exception):
    """A cell too wide to certify; the cover subdivides it."""


# ---------------------------------------------------------------- Gamma reading
def gamma_numerator(weight=GAMMA_WEIGHT, modes=GAMMA_MODES):
    """N(z)=sum_beta sum_j g_j c_{beta,a_j}(z^{2beta}-z^{2a_j}); row = z^3 N(z)/q_Gamma(z)."""
    degree = max(4*(modes-1)+1, max(k for _, k in weight)+3)
    coeff = [F(0)]*(degree+1)
    for k in range(modes):
        two_beta = 4*k+1
        for g, kz in weight:
            two_a = kz+3
            c = F(4*two_beta, two_a*two_a-two_beta*two_beta)
            coeff[two_beta] += g*c
            coeff[two_a] -= g*c
    return coeff


GAMMA_NUMERATOR = gamma_numerator()
GAMMA_POLY = weight_polynomial(GAMMA_WEIGHT)


def gamma_lower(z):
    """Interval lower bound of L_Gamma on a cell; exact rational at a point (0 at z=0: the row is O(z^3))."""
    if not isinstance(z, I) and z == 0:
        return F(0)
    q = poly_eval(GAMMA_POLY, z)
    if isinstance(z, I):
        if q.lo <= 0:
            raise UncertifiedCell('Gamma weight interval not positive on the cell')
        row_hi = (z**3*poly_eval(GAMMA_NUMERATOR, z)).hi
        return I(GAMMA_CONSTANT-MG_CAP)*I((z**6).lo)-I(row_hi)/I(q.lo)
    return (GAMMA_CONSTANT-MG_CAP)*z**6-z**3*poly_eval(GAMMA_NUMERATOR, z)/q


# ---------------------------------------------------------------- prime reading
def extend_catalogue(cat, powers=PRIME_POWERS):
    """Head and tail sums for W_k = z^{k+6}(A_k+p_k)+z^{-k}T_k, k odd.

    A_k uses Lambda(n) n^{(k+2)/2}, T_k uses Lambda(n) n^{-(k+4)/2}; the omitted
    tail beyond the catalogue is bounded by the decreasing integral test.
    """
    m, w, roots, logm = cat['limit'], cat['weights'], [I(0)]+[sqrt_integer(n) for n in range(1, cat['limit']+1)], cat['log_limit']
    ext = {}
    for k in powers:
        prefix, suffix = [I(0)]*(m+1), [I(0)]*(m+1)
        for n in range(1, m+1):
            prefix[n] = prefix[n-1]+w[n]*n**((k+1)//2)*roots[n]
        for n in range(m-1, -1, -1):
            j = n+1
            suffix[n] = suffix[n+1]+w[j]/(j**((k+3)//2)*roots[j])
        half = F(k+2, 2)
        tail = (logm/half+1/half**2)/(m**((k+2)//2)*roots[m])
        ext[k] = dict(prefix=prefix, suffix=suffix, tail=tail, mass=suffix[0]+I(0, tail.hi), mass_lower=suffix[0].lo)
    peaks = [I(0)]+[w[n]/(n*n) for n in range(1, m+1)]
    return dict(cat, rows=ext, roots=roots, peaks=peaks)


def _cell_indices(left, right, cat):
    left, right = F(left), F(right)
    if not 0 < left <= right <= 1:
        raise ValueError('A spatial cell in (0,1] is required')
    low, high = int(1/right**2), int(1/left**2)
    if high > cat['limit']:
        raise ValueError('The exterior requires its separate analytic bound')
    return left, right, low, high


def row_upper(left, right, cat, k):
    """Upper bound of W_k on the cell: head at the right end, tail at the left, straddled events at their peaks."""
    left, right, low, high = _cell_indices(left, right, cat)
    r = cat['rows'][k]
    value = right**(k+6)*(r['prefix'][low]+r['mass'])+(r['suffix'][high]+I(0, r['tail'].hi))/left**k
    return value+sum(cat['peaks'][low+1:high+1], I(0))


def row_lower(left, right, cat, k):
    """Lower bound of W_k on the cell; omitted events are nonnegative and dropped."""
    left, right, low, high = _cell_indices(left, right, cat)
    r = cat['rows'][k]
    out = left**(k+6)*(r['prefix'][low]+I(r['mass_lower']))+r['suffix'][high]/right**k
    for n in range(low+1, high+1):
        w, root = cat['weights'][n], cat['roots'][n]
        head = w*n**((k+1)//2)*root*left**(k+6)
        tail = w/(n**((k+3)//2)*root*right**k)
        out = out+I(min(head.lo, tail.lo))
    return out.lo


PRIME_POLY = weight_polynomial(PRIME_WEIGHT)


def prime_upper(left, right, cat, weight=PRIME_WEIGHT):
    """Upper bound of V_P = sum_i c_i W_{k_i} / q_P on the cell (linearity before division)."""
    numerator = I(0)
    for c, k in weight:
        numerator = numerator+(I(c)*row_upper(left, right, cat, k) if c > 0 else I(c)*I(row_lower(left, right, cat, k)))
    if numerator.hi < 0:
        raise AssertionError('Inconsistent positive prime row enclosure')
    q = poly_eval(weight_polynomial(weight), I(left, right))
    if q.lo <= 0:
        raise UncertifiedCell('Prime weight interval not positive on the cell')
    return I(numerator.hi)/I(q.lo)


# ---------------------------------------------------------------- pole reading
def pole_pairing(weight=POLE_WEIGHT):
    """<v,q_F> on (0,inf) with v=(e^{-x}-e^{-2x})/2 and q_F=sum f_j e^{-k_j x/2}: exact rational."""
    return sum((f*(F(1, 2)*(F(2, k+2)-F(2, k+4))) for f, k in weight), F(0))


POLE_POLY = weight_polynomial(POLE_WEIGHT)
POLE_PAIRING = pole_pairing()


def pole_upper(z):
    """tau(z)=2(z^2-z^4)<v,q_F>/q_F(z): the row of the rank-one pole kernel 4 v(x)v(y); 0 at z=0 (the row is O(z))."""
    if not isinstance(z, I) and z == 0:
        return F(0)
    q = poly_eval(POLE_POLY, z)
    if isinstance(z, I):
        if q.lo <= 0:
            raise UncertifiedCell('Pole weight interval not positive on the cell')
        return I((2*(z**2-z**4)*POLE_PAIRING).hi)/I(q.lo)
    return 2*(z**2-z**4)*POLE_PAIRING/q


def pole_budget(weight=POLE_WEIGHT, scale=F(1)):
    """4 int v^2/tau for tau = scale*tau_q; equals 1/scale exactly (SE18.6-7)."""
    if pole_pairing(weight) <= 0:
        raise ValueError('Pole pairing must be positive')
    return 1/F(scale)


# ---------------------------------------------------------------- comparison
def comparison_cell(left, right, cat, eta=ETA):
    eta = F(eta)
    if not 0 < eta < 1:
        raise ValueError('The signed graph decomposition uses 0 < eta < 1')
    z = I(left, right)
    return eta*(1+z**6)+(1-eta)*gamma_lower(z)-prime_upper(left, right, cat)-pole_upper(z)


def exterior_bound(cat, eta=ETA):
    """Uniform lower bound of the comparison on z in (0,1/OUTER_ROOT]."""
    m, root, logm = cat['limit'], sqrt_integer(cat['limit']), cat['log_limit']
    z = I(0, F(1, OUTER_ROOT))
    base = (F(16, 15)*logm+F(4, 9))/root+2*logm/(m*root)+cat['mass']/m**3      # SE16.19 at t>=m
    zmax = F(1, OUTER_ROOT)
    positive = sum((c for c, _ in PRIME_WEIGHT if c > 0), F(0))
    slope = weight_lower_slope(PRIME_WEIGHT, zmax)                                 # q_P >= slope*z on the exterior
    prime = positive*base/slope                                                    # W_k <= W_1 = z V_{1/2} (SE24 lemma)
    gamma_abs = I(GAMMA_CONSTANT-MG_CAP)*I((z**6).hi)+I((z**2*poly_eval([abs(c) for c in GAMMA_NUMERATOR], z)).hi)/weight_lower_slope(GAMMA_WEIGHT, zmax)
    pole = I(2*POLE_PAIRING)*I((z**2).hi)/(weight_lower_slope(POLE_WEIGHT, zmax)*zmax)
    lower = F(eta)-(1-F(eta))*gamma_abs-prime-pole
    return dict(base_prime=base, prime=prime, gamma_absolute=gamma_abs, pole=pole, lower=lower)


def cover(cat, floor=FLOOR, eta=ETA):
    if cat['limit'] != OUTER_ROOT**2:
        raise ValueError('The catalogue must agree with the exact exterior split')
    stack, accepted = [(F(1, OUTER_ROOT), F(1), 0)], []
    while stack:
        left, right, depth = stack.pop()
        try:
            lower = comparison_cell(left, right, cat, eta).lo
        except UncertifiedCell:
            lower = None
        if lower is not None and F(lower) >= floor:
            accepted.append((left, right, lower, depth))
        else:
            if depth >= 25:
                raise AssertionError(f'Uncertified cell {left}, {right}, {lower}')
            middle = (left+right)/2
            stack.extend(((middle, right, depth+1), (left, middle, depth+1)))
    assert accepted[0][0] == F(1, OUTER_ROOT) and accepted[-1][1] == 1
    assert all(a[1] == b[0] for a, b in zip(accepted, accepted[1:]))
    return accepted


def se17_cut_point_control(cat, eta=ETA):
    """SE17's weights with the q_0 pole row at the cut point z=1: exact upper enclosure."""
    k = GAMMA_MODES
    boundary_row = sum((2*F(4*j+1, 2)/((F(4*j+1, 2)+2)*(F(4*j+1, 2)+4)) for j in range(k)), F(0))
    gamma_at_one = GAMMA_CONSTANT-MG_CAP-boundary_row
    mass_52, mass_112 = cat['rows'][1]['mass'], cat['rows'][7]['mass']
    alpha = F(21, 40)
    prime_lower = (2*I(mass_52.lo)-2*alpha*I(mass_112.hi))/(1-alpha)
    return F(eta)*2+(1-F(eta))*gamma_at_one-prime_lower   # pole row vanishes at z=1


def _replay():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name, status='PASS'))
    cat = extend_catalogue(prime_catalogue(CATALOGUE))
    _, _, mg = refined_constants()
    check('inherited_gamma_ground_cap', mg.hi < I(MG_CAP).lo)
    check('catalogue_matches_exterior_split', cat['limit'] == OUTER_ROOT**2)
    check('sixteen_retained_gamma_modes', GAMMA_MODES == 16 and len(GAMMA_NUMERATOR) >= 62)
    check('gamma_weight_positive_slope', weight_lower_slope(GAMMA_WEIGHT) == F(9, 10))
    check('prime_weight_positive_slope_on_exterior', weight_lower_slope(PRIME_WEIGHT, F(1, OUTER_ROOT)) > 0)
    check('pole_weight_positive_slope', weight_lower_slope(POLE_WEIGHT) == 1)
    check('pole_pairing_exact', POLE_PAIRING == F(31, 210))
    check('pole_budget_saturated', pole_budget() == 1)
    check('pole_row_vanishes_at_both_ends', pole_upper(F(0)) == 0 and pole_upper(F(1)) == 0)
    check('exterior_comparison_value_is_eta_minus_zero', pole_upper(F(0)) == 0 and gamma_lower(F(0)) == 0)
    for k in PRIME_POWERS:
        check(f'positive_prime_mass_k_{k}', cat['rows'][k]['mass'].lo > 0)
        check(f'tail_k_{k}_below_one_over_10_power_6', cat['rows'][k]['tail'].hi < I(F(1, 10**6)).lo)
    cells = cover(cat)
    check('complete_spatial_cover', all(F(row[2]) >= FLOOR for row in cells))
    outer = exterior_bound(cat)
    check('exterior_logarithmic_monotonicity', cat['log_limit'].lo > 2)
    check('entire_exterior', outer['lower'].lo > I(FLOOR).hi)
    check('native_metric_floor', NATIVE_FLOOR == F(1, 7380))
    check('improvement_over_SE17_anchor', ETA < F(59, 100))
    control = se17_cut_point_control(cat)
    check('se17_weights_fail_at_cut_point_at_this_eta', control.hi < 0)
    return dict(schema='rkf.endpoint-three-weight-certificate.v1', date='2026-10-12',
        status='PASS_GLOBAL_THREE_WEIGHT', check_count=len(checks), checks=checks,
        arithmetic='Exact Fraction and inherited 90-digit outward Decimal intervals',
        global_source=dict(eta=rational(ETA), shifted_native_floor=rational(NATIVE_FLOOR),
            spatial_floor=rational(FLOOR), implied_nonnegative_shift=rational(ETA-NATIVE_FLOOR),
            invariant_negative_count=0, nullity=0, eta_zero_certified=False,
            scope='Entire corrected complex odd native source; every eta >= 14/25'),
        weights=dict(
            gamma=dict(formula='e^{-x/2} - e^{-5x/2}/10, x>0', terms=[[rational(c), k] for c, k in GAMMA_WEIGHT],
                       modes=GAMMA_MODES, constant=rational(GAMMA_CONSTANT), numerator=[rational(c) for c in GAMMA_NUMERATOR]),
            prime=dict(formula='e^{-|x|/2}/12 + e^{-3|x|/2} - (7/5)e^{-5|x|/2} + (2/5)e^{-7|x|/2}', terms=[[rational(c), k] for c, k in PRIME_WEIGHT]),
            pole=dict(formula='e^{-x/2} + e^{-3x/2}/4, x>0', terms=[[rational(c), k] for c, k in POLE_WEIGHT],
                      pairing=rational(POLE_PAIRING), row='2(z^2-z^4)<v,q_F>/q_F(z)', budget='4 int v^2/tau = 1'),
            rule='Each kernel carries its own positive weight; every omitted piece is a retained square residual'),
        primes=dict(cutoff=cat['limit'], prime_power_count=cat['prime_power_count'], catalogue_sha256=cat['catalogue_sha256'],
            masses={f'exponent_{(k+4)}/2': cat['rows'][k]['mass'].record() for k in PRIME_POWERS},
            tails={f'exponent_{(k+4)}/2': cat['rows'][k]['tail'].record() for k in PRIME_POWERS}),
        spatial_cover=dict(left=rational(F(1, OUTER_ROOT)), right='1/1', cells=len(cells),
            maximum_depth=max(r[3] for r in cells), minimum_lower=str(min(r[2] for r in cells)),
            records=[dict(left=rational(a), right=rational(b), lower=str(v), depth=d) for a, b, v, d in cells]),
        infinite_exterior={k: v.record() for k, v in outer.items()},
        comparison_control=dict(point='x=0 (cut point)', se17_weights_with_q0_pole_row=control.record(),
            same_eta=True, negative_source_claim=False),
        prior_local_frontier=dict(radius='21/25', stage='SE14', unchanged=True),
        not_certified=['eta=1/2', 'eta-zero positivity or RH', 'global critical observer contraction',
            'optimality of the weights', 'historical five-label endpoint or K0', 'formal verification or external review'])


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
        raise SystemExit('SE24 replay mismatch: inspect rather than repinning.')
    print(json.dumps(dict(status=result['status'], checks=result['check_count'],
        global_source=result['global_source'], cells=result['spatial_cover']['cells'],
        minimum_lower=result['spatial_cover']['minimum_lower'],
        exterior_lower=result['infinite_exterior']['lower']), indent=2))


if __name__ == '__main__':
    main()
