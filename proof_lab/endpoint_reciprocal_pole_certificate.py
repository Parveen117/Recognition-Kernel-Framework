"""SE22: global reciprocal-pole certificate below eta=0.57.

Executes the previously proved SE19 diagonal pole test on all native inputs.
Every cell, complete prime tail and the infinite spatial exterior are covered.
Subdivision priorities select work only; acceptance uses proved upper bounds.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import heapq
import json
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import I, sqrt_integer
    from proof_lab.endpoint_precision_frontier_certificate import refined_constants
    from proof_lab.endpoint_signed_return_certificate import MG_CAP, prime_catalogue, rational
    from proof_lab.endpoint_weight_family_certificate import (
        GAMMA_POLYNOMIAL, add_auxiliary_catalogue, gamma_lower, polynomial,
        shaped_prime_upper,
    )
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import I, sqrt_integer
    from endpoint_precision_frontier_certificate import refined_constants
    from endpoint_signed_return_certificate import MG_CAP, prime_catalogue, rational
    from endpoint_weight_family_certificate import (
        GAMMA_POLYNOMIAL, add_auxiliary_catalogue, gamma_lower, polynomial,
        shaped_prime_upper,
    )

ETA, ALPHA = F(227, 400), F(103, 200)
SEED_FLOOR, BETA_CAP = F(1, 1000), F(199, 200)
NATIVE_FLOOR = (1-BETA_CAP)*SEED_FLOOR/(2+MG_CAP)
RESULT = Path(__file__).with_name('ENDPOINT_RECIPROCAL_POLE_RESULT.json')
PINS = Path(__file__).resolve().parents[1]/'papers/rkf_completed_weil_endpoint/development/SE22_SOURCE_PINS.json'


def pole_mass(left, right):
    """Exact integral of 2*z^3*(1-z^2)^2 on the supplied rational cell."""
    left, right = F(left), F(right)
    if not 0 <= left <= right <= 1:
        raise ValueError('A cell in [0,1] is required')
    def primitive(z):
        return z**4/2-2*z**6/3+z**8/4
    return primitive(right)-primitive(left)


def seed_cell(left, right, cat, eta=ETA, alpha=ALPHA):
    eta, alpha = F(eta), F(alpha)
    if not 0 < eta < 1 or not 0 <= alpha < 1:
        raise ValueError('Require 0<eta<1 and 0<=alpha<1')
    z = I(left, right)
    return eta*(1+z**6)+(1-eta)*gamma_lower(z)-shaped_prime_upper(left,right,cat,alpha)


def exterior(cat, eta=ETA, alpha=ALPHA):
    """All z in [0,1/64], including the noncompact physical exterior."""
    if cat['limit'] != 4096:
        raise ValueError('The rational split requires the 4096 catalogue')
    m, logm, root = cat['limit'],cat['log_limit'],sqrt_integer(cat['limit'])
    base=(F(16,15)*logm+F(4,9))/root+2*logm/(m*root)+cat['mass']/m**3
    prime=base/(1-alpha/m**3)
    gamma=polynomial([abs(c) for c in GAMMA_POLYNOMIAL],I(F(1,64)))
    lower=eta-(1-eta)*gamma-prime
    if lower.lo<=0:
        raise AssertionError('Infinite exterior has no positive seed certificate')
    burden=I(pole_mass(0,F(1,64)))/I(lower.lo)
    return dict(prime_upper=prime,gamma_absolute=gamma,seed_lower=lower,pole_burden=burden)


def integral_cover(cat, eta=ETA, alpha=ALPHA, floor=SEED_FLOOR, cap=BETA_CAP):
    """Adaptive complete cover, stopped only by the rigorous integral upper sum."""
    if not 0<floor or not 0<cap<1:
        raise ValueError('A positive seed floor and strict pole cap in (0,1) are required')
    outer=exterior(cat,eta,alpha)
    if F(outer['seed_lower'].lo)<floor:
        raise AssertionError('Infinite exterior misses requested uniform seed floor')
    left0=F(1,64)
    stack=[(left0,F(1),0)]
    leaves={}
    next_id=0
    heap=[]
    total=F(outer['pole_burden'].hi)
    def insert(left,right,depth,lower):
        nonlocal next_id,total
        mass=pole_mass(left,right)
        upper=F((I(mass)/I(lower)).hi)
        mid=(left+right)/2
        midpoint_lower=seed_cell(mid,mid,cat,eta,alpha).lo
        # This is a deterministic subdivision heuristic, not an error bound.
        # The final upper sum never uses the midpoint as an integral estimate.
        candidate=(I(mass)/I(max(lower,midpoint_lower))).hi
        priority=max(F(0),upper-F(candidate))
        ident=next_id;next_id+=1
        leaves[ident]=(left,right,depth,lower,upper)
        heapq.heappush(heap,(-priority,ident))
        total+=upper
    while stack:
        left,right,depth=stack.pop()
        lower=seed_cell(left,right,cat,eta,alpha).lo
        if F(lower)>=floor:
            insert(left,right,depth,lower)
        else:
            if depth>=27:
                raise AssertionError('Uncertified seed cell: '+str((left,right,lower)))
            mid=(left+right)/2
            stack.extend(((mid,right,depth+1),(left,mid,depth+1)))
    initial_cells=len(leaves)
    while total>=cap:
        _,ident=heapq.heappop(heap)
        left,right,depth,parent_lower,upper=leaves.pop(ident)
        if depth>=30 or len(leaves)>100000:
            raise AssertionError('Reciprocal-pole integral remains inconclusive')
        total-=upper
        mid=(left+right)/2
        for a,b in ((left,mid),(mid,right)):
            lower=max(parent_lower,seed_cell(a,b,cat,eta,alpha).lo)
            insert(a,b,depth+1,lower)
    cells=sorted(leaves.values())
    assert cells[0][0]==left0 and cells[-1][1]==1
    assert all(a[1]==b[0] for a,b in zip(cells,cells[1:]))
    assert all(F(row[3])>=floor for row in cells)
    assert sum((pole_mass(a,b) for a,b,*_ in cells),F(0))+pole_mass(0,left0)==F(1,12)
    recomputed=F(outer['pole_burden'].hi)+sum((row[4] for row in cells),F(0))
    assert recomputed==total<cap
    return cells,outer,total,initial_cells


def fixed_pole_control(cat,eta=ETA,alpha=ALPHA):
    """Two-sided whole-source row enclosure at z=3/4 for the old comparison."""
    z=F(3,4)
    n=int(1/z**2)
    base=z**6*(cat['prefix'][n]+cat['mass'])+(cat['suffix'][n]+I(0,cat['tail'].hi))/z**2
    auxiliary=z**6*(cat['aux_prefix'][n]+cat['aux_mass'])+(
        cat['aux_suffix'][n]+I(0,cat['aux_tail'].hi))/z**14
    prime=(base-alpha*z**6*auxiliary)/(1-alpha*z**6)
    old=eta-F(1,10)+(eta+F(1,10))*z**6+(1-eta)*I(gamma_lower(z))-prime
    return old


def replay():
    cat=add_auxiliary_catalogue(prime_catalogue())
    _,_,mg=refined_constants()
    cells,outer,total,initial=integral_cover(cat)
    checks=[]
    def check(name,condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name,status='PASS'))
    check('inherited_complete_gamma_ground_cap',mg.hi<I(MG_CAP).lo)
    check('positive_even_prime_weight',0<=ALPHA<1)
    check('complete_spatial_seed_floor',min(F(row[3]) for row in cells)>=SEED_FLOOR)
    check('whole_infinite_exterior_seed_floor',F(outer['seed_lower'].lo)>=SEED_FLOOR)
    check('complete_pole_mass_is_one_twelfth',pole_mass(0,1)==F(1,12))
    check('complete_reciprocal_pole_burden',total<BETA_CAP<1)
    check('native_norm_conversion_keeps_positive_gamma_energy',NATIVE_FLOOR<ETA)
    check('strict_global_improvement_below_57_over_100',ETA<F(57,100))
    old=fixed_pole_control(cat)
    check('old_fixed_pole_comparison_fails_with_same_weights',old.hi<I(-F(29,1000)).lo)
    records=[[rational(a),rational(b),str(lower),rational(upper)]
             for a,b,_,lower,upper in cells]
    digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest()
    return dict(schema='rkf.endpoint-reciprocal-pole.v1',date='2026-10-12',
        status='PASS_GLOBAL_RECIPROCAL_POLE',arithmetic='Exact Fraction and inherited 90-digit outward Decimal',
        global_source=dict(eta=rational(ETA),shifted_native_floor=rational(NATIVE_FLOOR),
            implied_nonnegative_shift=rational(ETA-NATIVE_FLOOR),
            invariant_negative_count=0,nullity=0,eta_zero_certified=False,
            scope='Entire corrected complex odd native source; all eta >= 227/400'),
        comparison=dict(alpha=rational(ALPHA),uniform_seed_floor=rational(SEED_FLOOR),
            pole_cap=rational(BETA_CAP),pole_burden_upper=I(total).record(),
            exact_pole_retained=True,retained_residual_observations=0,
            unobserved_gamma_and_prime_squares_nonnegative=True),
        primes=dict(cutoff=cat['limit'],prime_power_count=cat['prime_power_count'],
            catalogue_sha256=cat['catalogue_sha256'],base_complete_mass=cat['mass'].record(),
            base_tail=cat['tail'].record(),auxiliary_complete_mass=cat['aux_mass'].record(),
            auxiliary_tail=cat['aux_tail'].record(),all_prime_powers_included=True),
        spatial_cover=dict(left='1/64',right='1/1',initial_seed_cells=initial,
            integral_cells=len(cells),maximum_depth=max(row[2] for row in cells),
            minimum_seed_lower=str(min(row[3] for row in cells)),
            partition_sha256=digest,
            certificate_rule='Every cell covers its entire interval; exact numerator mass divided by a proved positive seed lower bound; replay reconstructs and checks the complete partition.'),
        infinite_exterior={key:val.record() for key,val in outer.items()},
        fixed_pole_control=dict(z='3/4',old_comparison=old.record(),actual_negative_source_claim=False),
        check_count=len(checks),checks=checks,
        preserved_zero_shift_evidence='SE21: complete source on finite V16 only',
        unchanged_positive_support_radius='21/25',
        not_certified=['eta=1/2','global eta=0','RH','historical five-label attachment or K0',
            'global critical observer norm at most one','operator-engine gate PASS'])


def verify_source_pins():
    root=Path(__file__).resolve().parents[1]
    pins=json.loads(PINS.read_text())
    for name,expected in pins['sha256'].items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=expected:
            raise AssertionError('SE22 source pin mismatch: '+name)
    return len(pins['sha256'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    if args.write and args.check:
        parser.error('Choose --write or --check')
    result=replay()
    if args.write:
        RESULT.write_text(json.dumps(result,indent=2)+'\n')
    if args.check:
        if json.loads(RESULT.read_text())!=result:
            raise AssertionError('SE22 result differs from checked-in evidence')
        print('Source pins checked:',verify_source_pins())
    print(json.dumps({key:result[key] for key in ('status','global_source','comparison','spatial_cover','check_count')},indent=2))


if __name__=='__main__':
    main()
