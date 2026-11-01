"""SE23: one source-attached Gamma observation improves the global eta bound.

The trial is rational. Full-cell integral enclosures and complete inherited
tails certify the residual target; floating-point candidate searches are not
loaded. The native source and every earlier result remain unchanged.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import heapq
import json
from pathlib import Path

try:
    from proof_lab.endpoint_full_aperture_certificate import I
    from proof_lab.endpoint_precision_frontier_certificate import refined_constants
    from proof_lab.endpoint_reciprocal_pole_certificate import exterior, pole_mass, seed_cell
    from proof_lab.endpoint_signed_return_certificate import MG_CAP, prime_catalogue, rational
    from proof_lab.endpoint_weight_family_certificate import add_auxiliary_catalogue, gamma_lower
except ModuleNotFoundError:
    from endpoint_full_aperture_certificate import I
    from endpoint_precision_frontier_certificate import refined_constants
    from endpoint_reciprocal_pole_certificate import exterior, pole_mass, seed_cell
    from endpoint_signed_return_certificate import MG_CAP, prime_catalogue, rational
    from endpoint_weight_family_certificate import add_auxiliary_catalogue, gamma_lower

ETA, ALPHA = F(113,200), F(513,1000)
SEED_FLOOR, BETA_CAP = F(1,1000), F(199,200)
NATIVE_FLOOR = (1-BETA_CAP)*SEED_FLOOR/(2+MG_CAP)
TRIAL = {2:F(-28,100),4:F(2274,100),6:F(-4103,100),8:F(2064,100)}
RESULT = Path(__file__).with_name('ENDPOINT_RESIDUAL_OBSERVER_RESULT.json')
PINS = Path(__file__).resolve().parents[1]/'papers/rkf_completed_weil_endpoint/development/SE23_SOURCE_PINS.json'


def add(a,b,scale=F(1)):
    out=a.copy()
    for k,c in b.items():
        out[k]=out.get(k,F(0))+scale*c
    return {k:c for k,c in out.items() if c}


def multiply(a,b):
    out={}
    for i,c in a.items():
        for j,d in b.items():
            out[i+j]=out.get(i+j,F(0))+c*d
    return {k:c for k,c in out.items() if c}


def inner(a,b):
    """Exact half-line L2 pairing after z=exp(-x/2)."""
    if any(i+j<=0 for i in a for j in b):
        raise ValueError('Nonintegrable monomial pair')
    return sum((2*c*d/F(i+j) for i,c in a.items() for j,d in b.items()),F(0))


def kernel(a,k):
    """Exact odd Gamma kernel action on nonresonant exponentials."""
    if not isinstance(k,int) or not 0<=k<16:
        raise ValueError('One of the sixteen retained Gamma modes is required')
    beta=F(4*k+1,2)
    out={}
    for p,c in a.items():
        den=F(p+3,2)**2-beta**2
        if den==0:
            raise ValueError('Resonant exponential requires a logarithmic chart')
        value=2*beta*c/den
        out=add(out,{4*k+4:value,p+6:-value})
    return out


def observation(trial=TRIAL):
    """u=q*trial; d=D_Gamma*u, with its exact event norm squared."""
    q={1:F(1),5:F(-1)}
    u=multiply(q,trial)
    d={}
    for k in range(16):
        d=add(d,add(multiply(trial,kernel(q,k)),kernel(u,k),F(-1)))
    energy=inner(u,d)
    residual=add({2:F(1,2),4:F(-1,2)},d,F(-1))
    if energy<=0 or sum(d.values())!=0:
        raise AssertionError('Observation has invalid energy or boundary return')
    return u,d,energy,residual


class TargetMass:
    """Enclose integral 8*r(z)^2/z on each entire rational interval."""
    def __init__(self,residual):
        square=multiply(residual,residual)
        if not square or min(square)<=0:
            raise ValueError('The residual target must vanish at infinity')
        primitive={k:8*c/k for k,c in square.items()}
        self.coeff=[I(primitive.get(k,F(0))) for k in range(max(primitive)+1)]
        self.total=sum(primitive.values(),F(0))

    def primitive(self,z):
        z=I(z)
        out=I(0)
        for c in reversed(self.coeff):
            out=out*z+c
        return out

    def __call__(self,left,right):
        left,right=F(left),F(right)
        if not 0<=left<=right<=1:
            raise ValueError('A cell in [0,1] is required')
        val=self.primitive(right)-self.primitive(left)
        if val.hi<0:
            raise AssertionError('Squared-target mass enclosure is inconsistent')
        return I(max(0,val.lo),val.hi)


def seed_upper(left,right,cat,eta=ETA,alpha=ALPHA):
    """Independent upper bound on W for the diagonal-only failure control."""
    left,right=F(left),F(right)
    if not 0<left<=right<=1 or int(1/left**2)>cat['limit']:
        raise ValueError('Use a covered inner cell')
    low,high=int(1/right**2),int(1/left**2)
    base=left**6*(cat['prefix'][low]+cat['mass'])+cat['suffix'][high]/right**2
    aux=right**6*(cat['aux_prefix'][low]+cat['aux_mass'])+(
        cat['aux_suffix'][high]+I(0,cat['aux_tail'].hi))/left**14
    for n in range(low+1,high+1):
        root,w=cat['aux_roots'][n],cat['weights'][n]
        base+=I(min((left**6*w*n*root).lo,(w/(n*n*root*right**2)).lo))
        aux+=w*n*root
    numerator=base-alpha*right**6*aux
    prime_lower=max(0,(I(numerator.lo)/(1-alpha*left**6)).lo)
    z=I(left,right)
    return (eta*(1+z**6)+(1-eta)*gamma_lower(z)-I(prime_lower)).hi


def certify_cover(cat,mass,energy,eta=ETA,alpha=ALPHA,floor=SEED_FLOOR,cap=BETA_CAP):
    if not 0<eta<1 or not 0<=alpha<1 or not floor>0 or not 0<cap<1 or not energy>0:
        raise ValueError('Invalid certificate parameters')
    outer=exterior(cat,eta,alpha)
    if F(outer['seed_lower'].lo)<floor:
        raise AssertionError('Infinite exterior misses the seed floor')
    left0=F(1,64)
    cost=I(4*energy/(1-eta))
    outer_mass=mass(0,left0)
    outer_upper=outer_mass/I(outer['seed_lower'].lo)
    total=F(cost.hi)+F(outer_upper.hi)
    if total>=cap:
        raise AssertionError('Observation cost alone is too large')
    leaves,heap={},[]
    next_id=0
    def insert(a,b,depth,lower):
        nonlocal total,next_id
        numerator=mass(a,b)
        upper=F((numerator/I(lower)).hi)
        mid=(a+b)/2
        midpoint=seed_cell(mid,mid,cat,eta,alpha).lo
        optimistic=F((numerator/I(max(lower,midpoint))).hi)
        priority=max(F(0),upper-optimistic)
        ident=next_id;next_id+=1
        leaves[ident]=(a,b,depth,lower,upper,numerator.lo,numerator.hi)
        heapq.heappush(heap,(-priority,ident))
        total+=upper
    stack=[(left0,F(1),0)]
    while stack:
        a,b,depth=stack.pop()
        lower=seed_cell(a,b,cat,eta,alpha).lo
        if F(lower)>=floor:
            insert(a,b,depth,lower)
        else:
            if depth>=27:
                raise AssertionError('Uncertified seed cell: '+str((a,b,lower)))
            mid=(a+b)/2
            stack.extend(((mid,b,depth+1),(a,mid,depth+1)))
    initial=len(leaves)
    while total>=cap:
        _,ident=heapq.heappop(heap)
        a,b,depth,parent,upper,_,_=leaves.pop(ident)
        if depth>=30 or len(leaves)>100000:
            raise AssertionError('Residual-target certificate remains inconclusive')
        total-=upper
        mid=(a+b)/2
        for c,d in ((a,mid),(mid,b)):
            insert(c,d,depth+1,max(parent,seed_cell(c,d,cat,eta,alpha).lo))
    cells=sorted(leaves.values())
    assert cells[0][0]==left0 and cells[-1][1]==1
    assert all(a[1]==b[0] for a,b in zip(cells,cells[1:]))
    assert all(F(row[3])>=floor for row in cells)
    sum_lo=F(outer_mass.lo)+sum((F(row[5]) for row in cells),F(0))
    sum_hi=F(outer_mass.hi)+sum((F(row[6]) for row in cells),F(0))
    assert sum_lo<=mass.total<=sum_hi
    recomputed=F(cost.hi)+F(outer_upper.hi)+sum((row[4] for row in cells),F(0))
    assert recomputed==total<cap
    outer.update(target_mass=outer_mass,target_burden=outer_upper)
    return cells,outer,cost,total,initial


def replay():
    cat=add_auxiliary_catalogue(prime_catalogue())
    _,_,mg=refined_constants()
    u,d,energy,residual=observation()
    mass=TargetMass(residual)
    cells,outer,cost,total,initial=certify_cover(cat,mass,energy)
    # The omitted exterior is nonnegative, so it may be dropped for this
    # LOWER bound only. It is included in the passing upper certificate.
    diagonal_lower=sum((F((I(pole_mass(a,b))/I(seed_upper(a,b,cat))).lo)
                        for a,b,*_ in cells),F(0))
    checks=[]
    def check(name,condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name,status='PASS'))
    check('complete_gamma_ground_cap',mg.hi<I(MG_CAP).lo)
    check('exact_source_observation_has_positive_event_energy',energy>0)
    check('exact_boundary_return',sum(d.values())==0)
    check('target_total_matches_half_line_norm',mass.total==4*inner(residual,residual))
    check('whole_inner_seed_floor',min(F(row[3]) for row in cells)>=SEED_FLOOR)
    check('entire_infinite_exterior_seed_floor',F(outer['seed_lower'].lo)>=SEED_FLOOR)
    check('complete_residual_target_budget',total<BETA_CAP<1)
    check('diagonal_only_pole_test_fails_at_same_parameters',diagonal_lower>F(103,100))
    check('positive_gamma_energy_covers_native_floor',NATIVE_FLOOR<ETA)
    check('global_eta_improves_SE22',ETA-NATIVE_FLOOR<F(837629,1476000))
    records=[[rational(a),rational(b),str(lower),rational(upper),str(lo),str(hi)]
             for a,b,_,lower,upper,lo,hi in cells]
    digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest()
    return dict(schema='rkf.endpoint-residual-observer.v1',date='2026-10-12',
        status='PASS_GLOBAL_RESIDUAL_OBSERVER',arithmetic='Exact Fraction and inherited 90-digit outward Decimal',
        global_source=dict(eta=rational(ETA),shifted_native_floor=rational(NATIVE_FLOOR),
            implied_nonnegative_shift=rational(ETA-NATIVE_FLOOR),invariant_negative_count=0,nullity=0,
            scope='Entire corrected complex odd native source; all eta >= 113/200',eta_zero_certified=False),
        comparison=dict(alpha=rational(ALPHA),uniform_seed_floor=rational(SEED_FLOOR),
            pole_cap=rational(BETA_CAP),recovered_burden_upper=I(total).record(),
            diagonal_burden_lower=I(diagonal_lower).record(),negative_actual_source_claim=False),
        observation=dict(retained_event_coordinates=1,gamma_modes=list(range(16)),
            trial_polynomial={str(k):rational(c) for k,c in sorted(TRIAL.items())},
            trial='u=(z-z^5)*trial_polynomial',response='d=D_Gamma*u',
            exact_energy=rational(energy),energy_interval=I(energy).record(),observation_cost=cost.record(),
            response_coefficients={str(k):rational(c) for k,c in sorted(d.items())},
            exact_residual_target_mass=rational(mass.total),residual_degree=max(residual),
            remaining_event_energy_nonnegative=True),
        primes=dict(cutoff=cat['limit'],prime_power_count=cat['prime_power_count'],
            catalogue_sha256=cat['catalogue_sha256'],base_mass=cat['mass'].record(),
            base_tail=cat['tail'].record(),auxiliary_mass=cat['aux_mass'].record(),
            auxiliary_tail=cat['aux_tail'].record(),all_prime_powers_included=True),
        spatial_cover=dict(initial_seed_cells=initial,integral_cells=len(cells),
            maximum_depth=max(row[2] for row in cells),minimum_seed_lower=str(min(row[3] for row in cells)),
            partition_sha256=digest,complete_partition=True),
        infinite_exterior={key:val.record() for key,val in outer.items()},
        check_count=len(checks),checks=checks,unchanged_positive_support_radius='21/25',
        preserved_zero_shift_evidence='SE21 finite V16 only',
        not_certified=['eta=1/2','global eta=0 or RH','critical observer contractivity',
            'historical five-label attachment or K0','operator-engine gate PASS',
            'Atiyah-Singer extension or orientation-free spectral flow'])


def verify_source_pins():
    root=Path(__file__).resolve().parents[1]
    pins=json.loads(PINS.read_text())
    for name,expected in pins['sha256'].items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=expected:
            raise AssertionError('SE23 source pin mismatch: '+name)
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
            raise AssertionError('SE23 result differs from the checked-in evidence')
        print('Source pins checked:',verify_source_pins())
    print(json.dumps({key:result[key] for key in ('status','global_source','comparison','spatial_cover','check_count')},indent=2))


if __name__=='__main__':
    main()
