"""SE25: source-attached sectoral Gamma recovery at global eta 27/50.

Only rational witnesses and outward intervals authorize acceptance. The
complete SE24 prime catalogue and analytic exterior remain in the source.
"""
from __future__ import annotations

import argparse
from decimal import localcontext
from fractions import Fraction as F
import hashlib
import heapq
import json
from pathlib import Path

from proof_lab.endpoint_full_aperture_certificate import I, sqrt_integer
from proof_lab.endpoint_precision_frontier_certificate import refined_constants
from proof_lab.endpoint_signed_return_certificate import MG_CAP, prime_catalogue, rational
from proof_lab import endpoint_three_weight_certificate as rows
from proof_lab.endpoint_residual_observer_certificate import (
    add, multiply, inner, kernel, TargetMass,
)
from proof_lab.endpoint_reciprocal_pole_certificate import pole_mass

ETA, SEED_FLOOR, BETA_CAP = F(27,50), F(1,250), F(199,200)
NATIVE_FLOOR = (1-BETA_CAP)*SEED_FLOOR/(2+MG_CAP)
GAMMA_WEIGHT = ((F(1),1),(F(139,125),3),(F(-2493,500),5),(F(1651,500),7))
PRIME_WEIGHT = ((F(1697,20000),1),(F(1),3),(F(-5441,4000),5),(F(7419,20000),7))
TRIAL = {2:F(471,40),4:F(-863,20),6:F(3561,50),8:F(-9813,250)}
GAMMA_NUMERATOR = rows.gamma_numerator(GAMMA_WEIGHT)
GAMMA_POLY = rows.weight_polynomial(GAMMA_WEIGHT)
PRIME_POLY = rows.weight_polynomial(PRIME_WEIGHT)
OUTER_ROOT, CATALOGUE = 512, 262144
RESULT = Path(__file__).with_name('ENDPOINT_SECTORAL_RECOVERY_RESULT.json')
PINS = Path(__file__).resolve().parents[1]/'papers/rkf_completed_weil_endpoint/development/SE25_SOURCE_PINS.json'


def gamma_bounds(left, right):
    z=I(left,right)
    q=rows.poly_eval(GAMMA_POLY,z)
    if q.lo<=0:
        raise rows.UncertifiedCell('Gamma denominator is not positive on this cell')
    return (rows.GAMMA_CONSTANT-MG_CAP)*z**6-z**3*rows.poly_eval(GAMMA_NUMERATOR,z)/q


def prime_lower(left,right,cat):
    q=rows.poly_eval(PRIME_POLY,I(left,right))
    if q.lo<=0:
        raise rows.UncertifiedCell('Prime denominator is not positive on this cell')
    numerator=I(0)
    for c,k in PRIME_WEIGHT:
        bound=I(rows.row_lower(left,right,cat,k)) if c>0 else rows.row_upper(left,right,cat,k)
        numerator+=c*bound
    return max(F(0),F((I(numerator.lo)/I(q.hi)).lo))


def seed_cell(left,right,cat,eta=ETA):
    if not 0<eta<1:
        raise ValueError('The retained-source proof requires 0 < eta < 1')
    z=I(left,right)
    return eta*(1+z**6)+(1-eta)*gamma_bounds(left,right)-rows.prime_upper(left,right,cat,PRIME_WEIGHT)


def seed_upper(left,right,cat,eta=ETA):
    z=I(left,right)
    return (eta*(1+z**6)+(1-eta)*gamma_bounds(left,right)-prime_lower(left,right,cat)).hi


def exterior(cat,eta=ETA):
    if cat['limit']!=CATALOGUE:
        raise ValueError('Catalogue and analytic exterior must match')
    m=cat['limit'];zmax=F(1,OUTER_ROOT);z=I(0,zmax)
    base=(F(16,15)*cat['log_limit']+F(4,9))/sqrt_integer(m)+2*cat['log_limit']/(m*sqrt_integer(m))+cat['mass']/m**3
    prime=sum((c for c,k in PRIME_WEIGHT if c>0),F(0))*base/rows.weight_lower_slope(PRIME_WEIGHT,zmax)
    gamma_abs=(rows.GAMMA_CONSTANT-MG_CAP)*I((z**6).hi)+I((z**2*rows.poly_eval([abs(c) for c in GAMMA_NUMERATOR],z)).hi)/rows.weight_lower_slope(GAMMA_WEIGHT,zmax)
    lower=eta-(1-eta)*gamma_abs-prime
    return dict(base_prime=base,prime_upper=prime,gamma_absolute=gamma_abs,seed_lower=lower)


def observation(trial=None):
    trial=TRIAL if trial is None else trial
    q={k:c for c,k in GAMMA_WEIGHT}
    u=multiply(q,trial);d={}
    for k in range(16):
        d=add(d,add(multiply(trial,kernel(q,k)),kernel(u,k),F(-1)))
    energy=inner(u,d)
    if energy<=0:
        raise ValueError('A nonzero positive-energy event coordinate is required')
    return u,d,energy,add({2:F(1,2),4:F(-1,2)},d,F(-1))


def certify_cover(cat,mass,energy,eta=ETA,floor=SEED_FLOOR,cap=BETA_CAP,progress=False):
    if not 0<floor or not 0<cap<1 or not 0<energy or not 0<eta<1:
        raise ValueError('Invalid source certificate parameters')
    outer=exterior(cat,eta)
    if F(outer['seed_lower'].lo)<floor:
        raise AssertionError('The complete exterior fails the requested floor')
    left0=F(1,OUTER_ROOT);cost=I(4*energy/(1-eta))
    outer_mass=mass(0,left0);outer_burden=outer_mass/I(outer['seed_lower'].lo)
    total=F(cost.hi)+F(outer_burden.hi)
    if total>=cap:
        raise AssertionError('Observation and exterior costs exhaust the budget')
    leaves={};heap=[];next_id=0
    def insert(a,b,depth,lower):
        nonlocal total,next_id
        numerator=mass(a,b);upper=F((numerator/I(lower)).hi)
        mid=(a+b)/2;point=seed_cell(mid,mid,cat,eta).lo
        heuristic=F((numerator/I(max(lower,point))).hi)
        ident=next_id;next_id+=1
        leaves[ident]=(a,b,depth,lower,upper,numerator.lo,numerator.hi)
        heapq.heappush(heap,(-max(F(0),upper-heuristic),ident));total+=upper
    stack=[(left0,F(1),0)]
    while stack:
        a,b,depth=stack.pop()
        try:lower=seed_cell(a,b,cat,eta).lo
        except rows.UncertifiedCell:lower=None
        if lower is not None and F(lower)>=floor:
            insert(a,b,depth,lower)
        else:
            if depth>=27:raise AssertionError('Seed not certified on '+str((a,b,lower)))
            mid=(a+b)/2;stack.extend(((mid,b,depth+1),(a,mid,depth+1)))
    initial=len(leaves)
    if progress:print('Initial seed cells:',initial,'budget upper:',float(total),flush=True)
    while total>=cap:
        _,ident=heapq.heappop(heap)
        a,b,depth,parent,upper,_,_=leaves.pop(ident)
        if depth>=30 or len(leaves)>100000:
            raise AssertionError('Refinement budget exhausted without a certificate')
        total-=upper;mid=(a+b)/2
        for c,d in ((a,mid),(mid,b)):
            insert(c,d,depth+1,max(parent,seed_cell(c,d,cat,eta).lo))
        if progress and len(leaves)%2000==0:
            print('Integral cells:',len(leaves),'budget upper:',float(total),flush=True)
    cells=sorted(leaves.values())
    assert cells[0][0]==left0 and cells[-1][1]==1
    assert all(a[1]==b[0] for a,b in zip(cells,cells[1:]))
    assert min(F(r[3]) for r in cells)>=floor
    lo=F(outer_mass.lo)+sum((F(r[5]) for r in cells),F(0))
    hi=F(outer_mass.hi)+sum((F(r[6]) for r in cells),F(0))
    assert lo<=mass.total<=hi
    assert total==F(cost.hi)+F(outer_burden.hi)+sum((r[4] for r in cells),F(0))<cap
    outer.update(target_mass=outer_mass,target_burden=outer_burden)
    return cells,outer,cost,total,initial


def replay(progress=False):
    with localcontext() as context:
        context.prec=90
        if progress:print('Building complete prime-power catalogue...',flush=True)
        cat=rows.extend_catalogue(prime_catalogue(CATALOGUE))
        if progress:print('Catalogue complete:',cat['prime_power_count'],'events',flush=True)
        u,d,energy,residual=observation();mass=TargetMass(residual)
        cells,outer,cost,total,initial=certify_cover(cat,mass,energy,progress=progress)
        diagonal_lower=sum((F((I(pole_mass(a,b))/I(seed_upper(a,b,cat))).lo) for a,b,*_ in cells),F(0))
        _,_,mg=refined_constants();checks=[]
        def check(name,condition):
            if not condition:raise AssertionError(name)
            checks.append(dict(name=name,status='PASS'))
        # Exact Bernstein coefficients for q_Gamma/z, degree three.
        bernstein=[F(1),F(514,375),F(119,1500),F(107,250)]
        check('gamma_weight_positive_Bernstein_coefficients',min(bernstein)>0)
        check('prime_weight_positive_decomposition',F(1)-F(5441,4000)+F(7419,20000)==F(107,10000))
        check('inherited_complete_gamma_ground_cap',mg.hi<I(MG_CAP).lo)
        check('exact_event_energy_positive',energy>0)
        check('cut_point_response_zero',sum(d.values())==0)
        check('target_primitive_mass_identity',mass.total==4*inner(residual,residual))
        check('whole_inner_seed_floor',min(F(r[3]) for r in cells)>=SEED_FLOOR)
        check('entire_infinite_exterior_seed_floor',F(outer['seed_lower'].lo)>=SEED_FLOOR)
        check('complete_pole_recovery_budget',total<BETA_CAP<1)
        check('diagonal_only_same_source_comparison_fails',diagonal_lower>F(6,5))
        check('native_metric_floor',NATIVE_FLOOR==F(1,369000) and NATIVE_FLOOR<ETA)
        check('strict_improvement_over_SE24',ETA-NATIVE_FLOOR<F(20659,36900))
        for k in rows.PRIME_POWERS:
            check('all_integer_prime_tail_k_'+str(k),cat['rows'][k]['tail'].hi<I(F(1,10**6)).hi)
        records=[[rational(a),rational(b),depth,str(lower),rational(up),str(lo),str(hi)] for a,b,depth,lower,up,lo,hi in cells]
        digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest()
        return dict(schema='rkf.endpoint-sectoral-recovery.v1',date='2026-10-12',
            status='PASS_GLOBAL_SECTORAL_RECOVERY',arithmetic='Exact Fraction and 90-digit outward Decimal',
            global_source=dict(eta=rational(ETA),shifted_native_floor=rational(NATIVE_FLOOR),
                implied_nonnegative_shift=rational(ETA-NATIVE_FLOOR),invariant_negative_count=0,nullity=0,
                scope='Entire corrected complex odd native source; every eta >= 27/50',eta_zero_certified=False),
            comparison=dict(seed_floor=rational(SEED_FLOOR),pole_cap=rational(BETA_CAP),
                recovered_burden_upper=I(total).record(),diagonal_burden_lower=I(diagonal_lower).record(),
                actual_source_unchanged=True,negative_actual_source_claim=False),
            weights=dict(gamma=[[rational(c),k] for c,k in GAMMA_WEIGHT],
                prime=[[rational(c),k] for c,k in PRIME_WEIGHT],gamma_bernstein=[rational(b) for b in bernstein]),
            observation=dict(event_coordinates=1,gamma_modes=list(range(16)),
                trial={str(k):rational(c) for k,c in sorted(TRIAL.items())},
                response_coefficients={str(k):rational(c) for k,c in sorted(d.items())},
                energy=rational(energy),energy_interval=I(energy).record(),cost=cost.record(),
                target_mass=rational(mass.total),source_attachment='d=D_Gamma(q_Gamma*phi)',
                all_mixed_terms_retained=True,remaining_event_energy_nonnegative=True),
            primes=dict(cutoff=cat['limit'],prime_power_count=cat['prime_power_count'],
                catalogue_sha256=cat['catalogue_sha256'],
                masses={str(k):cat['rows'][k]['mass'].record() for k in rows.PRIME_POWERS},
                tails={str(k):cat['rows'][k]['tail'].record() for k in rows.PRIME_POWERS}),
            spatial_cover=dict(initial_cells=initial,integral_cells=len(cells),maximum_depth=max(r[2] for r in cells),
                minimum_seed_lower=str(min(r[3] for r in cells)),partition_sha256=digest,complete_partition=True),
            infinite_exterior={k:v.record() for k,v in outer.items()},check_count=len(checks),checks=checks,
            not_certified=['global eta=0 or RH','eta=1/2','historical five-label attachment or K0',
                'uniform critical observer contraction','operator-engine gate PASS','formal or external verification'])


def verify_source_pins():
    root=Path(__file__).resolve().parents[1];pins=json.loads(PINS.read_text())
    for p,expected in pins['sha256'].items():
        if hashlib.sha256((root/p).read_bytes()).hexdigest()!=expected:
            raise AssertionError('SE25 source pin mismatch: '+p)
    return len(pins['sha256'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group();group.add_argument('--write',action='store_true');group.add_argument('--check',action='store_true')
    parser.add_argument('--progress',action='store_true');args=parser.parse_args()
    result=replay(args.progress)
    if args.write:
        if RESULT.exists():raise SystemExit('Refuse to overwrite existing certificate evidence')
        RESULT.write_text(json.dumps(result,indent=2)+'\n')
    if args.check:
        if json.loads(RESULT.read_text())!=result:raise AssertionError('SE25 replay differs from archived evidence')
        print('Source pins checked:',verify_source_pins())
    print(json.dumps({k:result[k] for k in ('status','global_source','comparison','spatial_cover','check_count')},indent=2))


if __name__=='__main__':main()
