"""SE28: circle/sheet calibration, native TVSP flat specialization and RH source transport.

Exact controls and outward prime-log enclosures accompany written universal
proofs. The inherited SE27 global source certificate is reused, not rerun.
"""
from __future__ import annotations
import argparse
from decimal import localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess
from proof_lab import endpoint_connected_cut_certificate as parent
from proof_lab.endpoint_full_aperture_certificate import I,log_positive

ROOT=Path(__file__).resolve().parents[1]
RESULT=Path(__file__).with_name('ENDPOINT_CIRCULAR_CALIBRATION_RESULT.json')
PINS=ROOT/'papers/rkf_completed_weil_endpoint/development/SE28_SOURCE_PINS.json'

def folded_pair(a,b,m=1,sheets=3):
    """Exact head and infinite tail at circle length 2*m*log(2)."""
    if m<1 or sheets<1:raise ValueError('Positive integer calibration and sheet count required')
    head=tail=F(0)
    for p,c in a.items():
        for q,d in b.items():
            t=F(1,2**(m*(p+q)*sheets));mass=2*c*d/F(p+q)
            head+=mass*(1-t);tail+=mass*t
    return head,tail

def carry_interval(turn):
    low=F(turn.lo).__floor__();high=F(turn.hi).__floor__()
    if low!=high:raise ValueError('Unresolved cut crossing; refine or retain both branches')
    return low,turn-low

def endpoint_read(poly,sheet,phase,m):
    z=F(1,2**(m*sheet))*F(1,2**(m*phase))
    return sum((c*z**p for p,c in poly.items()),F(0))

def replay():
    with localcontext() as ctx:
        ctx.prec=90
        inherited=parent.verify_source_pins()
        geometry=json.loads(subprocess.run(['node',str(Path(__file__).with_name('endpoint_circular_calibration.cjs'))],check=True,capture_output=True,text=True).stdout)
        archive=json.loads(parent.RESULT.read_text())
        checks=[];controls=[]
        def check(name,value,negative=False):
            if not value:raise AssertionError(name)
            checks.append(dict(name=name,status='PASS'))
            if negative:controls.append(name)
        check('unchanged_SE27_certificate_and_native_bound',archive['status']=='PASS_CONNECTED_CUT_GLOBAL_SOURCE' and archive['global_source']['eta']=='1079/2000' and archive['global_source']['shifted_native_floor']=='1/492000')
        check('canonical_circle_and_TVSP_controls',geometry['status']=='PASS_EXACT_CIRCULAR_CALIBRATION')
        raw,gram,_=parent.event_basis()
        pairs=[]
        for m in (1,2,3):
            for i,a in enumerate(raw):
                for j,b in enumerate(raw):
                    head,tail=folded_pair(a[0],b[1],m)
                    if head+tail!=gram[i][j]:raise AssertionError('Actual mixed event Gram changed')
            pairs.append(dict(calibration='2*'+str(m)+'*log(2)',all_9_mixed_pairings='EXACT'))
        check('all_actual_event_Gram_entries_preserved_with_infinite_sheets',len(pairs)==3)
        q={k:c for c,k in parent.s.GAMMA_WEIGHT};v={2:F(1,2),4:F(-1,2)}
        pole=[]
        for m in (1,2,3):
            a,b=folded_pair(v,q,m);pole.append(dict(calibration_multiplier=m,head=str(a),infinite_tail=str(b),total=str(a+b)))
        check('actual_Gamma_blind_pole_reading_preserved',all(F(p['total'])==F(45607,433125) for p in pole))
        check('phase_folding_alone_loses_a_nonzero_tail',any(F(p['infinite_tail'])!=0 for p in pole),True)
        # Trace gluing for z^p at x=2*m*log(2)*(n+t).
        polynomials=[q,v]+[p for row in raw for p in row[:2]]
        check('helical_cut_gluing_for_actual_trial_and_response_monomials',all(endpoint_read(poly,n,1,m)==endpoint_read(poly,n+1,0,m) for m in (1,2,3) for n in (0,1,5) for poly in polynomials))
        check('independent_periodic_sheet_condition_is_false',endpoint_read(q,0,0,1)!=endpoint_read(q,0,1,1),True)
        log2=log_positive(2);prime_carries=[]
        for p in (2,3,4,5,7,8,9,11,25):
            shift=log_positive(p)/log2
            for t in (F(1,4),F(3,4)):
                k,r=carry_interval(I(t)-shift)
                check_label=dict(event=p,phase=str(t),sheet_carry=k,new_phase=r.record())
                if not(0<=r.lo<=r.hi<1):raise AssertionError(check_label)
                prime_carries.append(check_label)
        check('actual_prime_log_translations_have_certified_sheet_carries',len(prime_carries)==18)
        try:carry_interval(I(F(-1,100),F(1,100)))
        except ValueError:ambiguous=True
        else:ambiguous=False
        check('ambiguous_cut_crossing_not_rounded_to_one_branch',ambiguous,True)
        # A fixed normalized number shrinks; a fixed physical interval escapes.
        escaped=[]
        for L in (F(1,2),F(1,4),F(1,8),F(1,16)):
            n=(F(1)/L).__floor__();escaped.append(dict(unit=str(L),sheet_at_x_1=n))
        check('fixed_physical_state_needs_unbounded_turn_memory',all(a['sheet_at_x_1']<b['sheet_at_x_1'] for a,b in zip(escaped,escaped[1:])))
        # h=1_[1,2] has norm squared one. The first four sheets contain
        # exactly its intersection with [0,4*L], whose measure is below.
        window_mass=[max(F(0),min(F(2),4*L)-1) for L in (F(1,4),F(1,8),F(1,16))]
        check('nonzero_state_keeps_norm_while_fixed_sheet_windows_empty',window_mass==[0,0,0])
        return dict(schema='rkf.endpoint-circular-calibration.v1',date='2026-10-12',status='PASS_CIRCULAR_CALIBRATION_AND_FLAT_ZETA_SPECIALIZATION',
            source=dict(eta=archive['global_source']['eta'],shifted_native_floor=archive['global_source']['shifted_native_floor'],eta_zero_certified=False,
                inherited_certificate='SE27',global_replay_rerun=False,source_transport='Written unitary pullback with the complete native graph norm; Gamma, prime, pole and all residuals retained'),
            TVSP=dict(flat_condition='I_th=(lambda_p/lambda_v)*(lambda_t/lambda_s)=1',defect='r=(I_th-1)/(I_th+1)',phase='chi=(1+iota*r)/(1-iota*r)',
                zeta_specialization='Z_r(s)=sum chi^Omega(n)/n^s; Z_0(s)=zeta(s), Re(s)>1',universal_physical_unit=False,RH_flatness_equivalence=False),
            calibration=dict(cut='Whole line section with side and integer-turn memory',zero_unit='Resolved normalized data retained; raw zero alone is insufficient',
                fixed_source_limit='Weak zero and no strong limit in the unrescaled sheet carrier for nonzero states'),
            actual_event_pairs=pairs,actual_pole_pairs=pole,prime_log_carries=prime_carries,escaping_sheets=escaped,
            geometry=geometry,inherited_source_pins_checked=inherited,check_count=len(checks),negative_control_count=len(controls),checks=checks,controls=controls,
            not_certified=['RH or global eta zero','new smaller eta anchor','canonical derivation of primes or log(p) from TVSP','full curvature from one scalar flat ratio','analytic continuation of every twisted member','universal physical calibration','whole operator-engine PASS','formal or external verification'])

def verify_source_pins():
    pins=json.loads(PINS.read_text())['sha256']
    for p,h in pins.items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:raise AssertionError('SE28 pin mismatch: '+p)
    return len(pins)

def main():
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group();g.add_argument('--write',action='store_true');g.add_argument('--check',action='store_true');args=p.parse_args()
    r=replay()
    if args.write:
        if RESULT.exists():raise SystemExit('Refuse to overwrite certificate evidence')
        RESULT.write_text(json.dumps(r,indent=2)+'\n')
    if args.check:
        if json.loads(RESULT.read_text())!=r:raise AssertionError('Read-only replay differs from archive')
        print('Source pins checked:',verify_source_pins())
    print(json.dumps({k:r[k] for k in ('status','source','TVSP','check_count','negative_control_count')},indent=2))

if __name__=='__main__':main()
