"""SE27: connected measurement-reference cuts on the actual RH source.

The Gamma event Gram and target are exact. Complete inherited cell/tail
bounds certify the source, while the continuous-cut identities retain
overlap costs and nontrivial return memory.
"""
from __future__ import annotations
import argparse
from decimal import localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess
from proof_lab import endpoint_sectoral_recovery_certificate as s
from proof_lab import endpoint_diagonal_seam_certificate as seam

ROOT=Path(__file__).resolve().parents[1]
RESULT=Path(__file__).with_name('ENDPOINT_CONNECTED_CUT_RESULT.json')
PINS=ROOT/'papers/rkf_completed_weil_endpoint/development/SE27_SOURCE_PINS.json'
ETA,FLOOR,CAP=F(1079,2000),F(3,1000),F(199,200)
NATIVE_FLOOR=(1-CAP)*FLOOR/(2+s.MG_CAP)
TRIALS=(s.TRIAL,{2:F(1)},{4:F(1)})
COEFFICIENTS=(F(203,200),F(-1,50),F(13,500))

def event_basis():
    raw=[s.observation(p) for p in TRIALS]
    gram=[[s.inner(a[0],b[1]) for b in raw] for a in raw]
    orth=[]
    for phi in TRIALS:
        p=dict(phi)
        for old,u,d,e in orth:
            current=s.observation(p)
            p=s.add(p,old,-s.inner(current[0],d)/e)
        u,d,e,_=s.observation(p)
        orth.append((p,u,d,e))
    return raw,gram,orth

def replay(progress=False):
    with localcontext() as context:
        context.prec=90
        inherited=seam.verify_source_pins()
        geometry=json.loads(subprocess.run(['node',str(Path(__file__).with_name('endpoint_connected_cut_geometry.cjs'))],check=True,capture_output=True,text=True).stdout)
        raw,gram,orth=event_basis();trial={}
        for c,p in zip(COEFFICIENTS,TRIALS):trial=s.add(trial,p,c)
        u,d,energy,residual=s.observation(trial)
        checks=[]
        def check(name,condition):
            if not condition:raise AssertionError(name)
            checks.append(dict(name=name,status='PASS'))
        check('actual_event_Gram_is_symmetric',gram==list(map(list,zip(*gram))))
        check('three_actual_event_directions_independent',all(t[3]>0 for t in orth))
        check('exact_orthogonal_event_embedding',all(s.inner(a[1],b[2])==0 for i,a in enumerate(orth) for j,b in enumerate(orth) if i!=j))
        full=sum((COEFFICIENTS[i]*gram[i][j]*COEFFICIENTS[j] for i in range(3) for j in range(3)),F(0))
        diagonal=sum((COEFFICIENTS[i]**2*gram[i][i] for i in range(3)),F(0))
        check('full_mixed_event_energy_retained',energy==full and energy!=diagonal)
        orth_coeff=[s.inner(u,t[2])/t[3] for t in orth]
        rebuilt={}
        for c,t in zip(orth_coeff,orth):rebuilt=s.add(rebuilt,t[1],c)
        check('recovery_target_in_the_connected_cut_span',rebuilt==u)
        check('normalized_decoder_cost_identity',sum((c*c*t[3] for c,t in zip(orth_coeff,orth)),F(0))==energy)
        check('canonical_cut_geometry_controls',geometry['status']=='PASS_EXACT_CUT_CONTROLS')
        if progress:print('Building complete source catalogue...',flush=True)
        cat=s.rows.extend_catalogue(s.prime_catalogue(s.CATALOGUE))
        if progress:print('Catalogue complete:',cat['prime_power_count'],'events',flush=True)
        mass=s.TargetMass(residual)
        cells,outer,cost,total,initial=s.certify_cover(cat,mass,energy,eta=ETA,floor=FLOOR,cap=CAP,progress=progress)
        check('whole_inner_seed_floor',min(F(r[3]) for r in cells)>=FLOOR)
        check('infinite_exterior_floor',F(outer['seed_lower'].lo)>=FLOOR)
        check('full_paid_source_recovery_budget',total<CAP<1)
        check('native_source_floor',NATIVE_FLOOR==F(1,492000) and NATIVE_FLOOR<ETA)
        check('strict_improvement_over_SE25',ETA-NATIVE_FLOOR<s.ETA-s.NATIVE_FLOOR)
        check('complete_target_mass',mass.total==4*s.inner(residual,residual))
        check('actual_Gamma_blind_common_mode_not_deleted',s.inner({2:F(1,2),4:F(-1,2)},{k:c for c,k in s.GAMMA_WEIGHT})==F(45607,433125))
        records=[[str(a),str(b),depth,str(lower),str(up),str(lo),str(hi)] for a,b,depth,lower,up,lo,hi in cells]
        digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest()
        return dict(schema='rkf.endpoint-connected-cut.v1',date='2026-10-12',status='PASS_CONNECTED_CUT_GLOBAL_SOURCE',
            global_source=dict(eta=str(ETA),shifted_native_floor=str(NATIVE_FLOOR),implied_nonnegative_shift=str(ETA-NATIVE_FLOOR),
                scope='Entire corrected complex odd native source; every cut-path parameter and eta >= 1079/2000',
                invariant_negative_count=0,nullity=0,eta_zero_certified=False),
            zero_reference=dict(type='Connected calibrated family of measurement cuts, with transition and return memory',
                cuts=3,event_span_dimension=3,overlap_charge='1/2',holonomy=geometry['holonomy'],
                uniform_source_energy=True,transport_alone_changes_eta=False),
            event_embedding=dict(input_trials=[{str(k):str(c) for k,c in sorted(p.items())} for p in TRIALS],
                full_Gram=[[str(x) for x in r] for r in gram],
                orthogonal_trials=[{str(k):str(c) for k,c in sorted(t[0].items())} for t in orth],
                orthogonal_energies=[str(t[3]) for t in orth],
                recovery_coefficients=[str(c) for c in COEFFICIENTS],
                orthogonal_recovery_coefficients=[str(c) for c in orth_coeff],
                recovered_trial={str(k):str(c) for k,c in sorted(trial.items())},energy=str(energy),
                response_coefficients={str(k):str(c) for k,c in sorted(d.items())}),
            comparison=dict(seed_floor=str(FLOOR),budget_cap=str(CAP),budget_upper=s.I(total).record(),observation_cost=cost.record()),
            primes=dict(cutoff=cat['limit'],prime_power_count=cat['prime_power_count'],catalogue_sha256=cat['catalogue_sha256'],
                tails={str(k):cat['rows'][k]['tail'].record() for k in s.rows.PRIME_POWERS}),
            spatial_cover=dict(initial_cells=initial,integral_cells=len(cells),maximum_depth=max(r[2] for r in cells),
                minimum_seed_lower=str(min(r[3] for r in cells)),partition_sha256=digest,complete_partition=True),
            infinite_exterior={k:v.record() for k,v in outer.items()},geometry=geometry,
            inherited_source_pins_checked=inherited,check_count=len(checks),checks=checks,
            not_certified=['eta zero or RH','global source improvement from chart transport alone',
                'all possible curved cuts without source contracts','new physical TVSP arrow identification',
                'whole operator-engine gate PASS','formal proof-assistant or external verification'])

def verify_source_pins():
    pins=json.loads(PINS.read_text())['sha256']
    for p,h in pins.items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:raise AssertionError('SE27 source pin mismatch: '+p)
    return len(pins)

def main():
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group()
    group.add_argument('--write',action='store_true');group.add_argument('--check',action='store_true')
    parser.add_argument('--progress',action='store_true');args=parser.parse_args();result=replay(args.progress)
    if args.write:
        if RESULT.exists():raise SystemExit('Refuse to overwrite existing certificate evidence')
        RESULT.write_text(json.dumps(result,indent=2)+'\n')
    if args.check:
        if json.loads(RESULT.read_text())!=result:raise AssertionError('SE27 replay differs from archived evidence')
        print('Source pins checked:',verify_source_pins())
    print(json.dumps({k:result[k] for k in ('status','global_source','comparison','spatial_cover','check_count')},indent=2))

if __name__=='__main__':main()
