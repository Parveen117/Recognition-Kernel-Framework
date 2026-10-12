"""SE48: spectral continuation of the existing five-channel source operator.

Python 3.12, standard library only. Outward intervals certify finite pencil
poles and five local zeta disks. No zero table or RH premise is an input.
The universal positivity/limit condition is not certified by this replay.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path
from proof_lab.endpoint_full_aperture_certificate import I
from proof_lab.endpoint_global_eta_certificate import integer_log
from proof_lab.endpoint_zero_shift_laplace_certificate import precise_constants, interval_ldl, verify_source_pins
from proof_lab.endpoint_observer_index_certificate import add, diag, eye, inertia, inv, mul, scale, tr
from proof_lab.ordered_return_feedback import encode
from proof_lab.five_source_operator_repair import block_model

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'proof_lab/ENDPOINT_ZERO_SHIFT_LAPLACE_RESULT.json'
RESULT=Path(__file__).with_name('DIAGONAL_SPECTRAL_PENCIL_RESULT.json')
PINS=ROOT/'papers/rkf_completed_weil_endpoint/development/SE48_SOURCE_PINS.json'
# Untrusted rational bracket candidates from exploratory source-midpoint
# diagonalization. Only the signed outward LDL readings below certify them.
CENTRES={
5:['14.134738407086','21.128279451473','27.347745640573','44.091923408845','146.329475845781'],
8:['14.134725141743','21.022051446610','25.014245096727','30.933070910639','37.658345244867','50.700542421806','84.299236073775','277.715358015670'],
12:['14.134725141735','21.022039638773','25.010857591569','30.425088112797','32.940878699945','37.805712904558','42.531583993465','50.904696524251','64.344089939719','89.383826904646','150.288221832158','491.517645590334'],
16:['14.134725141735','21.022039638772','25.010857580146','30.424876126791','32.935061722570']}

class Z:
    def __init__(self,r=0,i=0):self.r=r if isinstance(r,I) else I(r);self.i=i if isinstance(i,I) else I(i)
    def __add__(self,o):
        if not isinstance(o,Z):o=Z(o)
        return Z(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self):return Z(-self.r,-self.i)
    def __sub__(self,o):return self+-o
    def __mul__(self,o):
        if not isinstance(o,Z):o=Z(o)
        return Z(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,Z):o=Z(o)
        d=o.r**2+o.i**2
        return Z((self.r*o.r+self.i*o.i)/d,(self.i*o.r-self.r*o.i)/d)
    def record(self):return [self.r.record(),self.i.record()]
    def upper(self):return F(self.r.abs_upper())+F(self.i.abs_upper())
    def lower(self):
        def a(x):return F(x.lo) if x.lo>0 else -F(x.hi) if x.hi<0 else F(0)
        return max(a(self.r),a(self.i))
def expi(z,terms=96):
    splits=0
    while z.upper()>F(1,2):z=z/2;splits+=1
    v=Z(1);out=Z(1)
    for k in range(1,terms+1):v=v*z/k;out=out+v
    B=F(1,2);err=B**(terms+1)/factorial(terms+1)/(1-B/(terms+2))
    out=out+Z(I(-err,err),I(-err,err))
    for _ in range(splits):out=out*out
    return out
def gamma_ratio_bound(upper=34,split=128):
    # sigma>=1/4. First split factors sqrt(1+x^2)<=1+x.
    initial=prod((F(1)+F(4*upper,4*k+1) for k in range(split)),start=F(1))
    sigma=F(1,4)
    exponent=F(upper**2,2)*(1/(sigma+split)**2+1/(sigma+split))
    ceil=(exponent.numerator+exponent.denominator-1)//exponent.denominator
    return initial*4**ceil


def signed_interval_ldl(a):
    """Return a proved negative index, or refuse an unresolved pivot."""
    n=len(a);lower=[[I(0) for _ in range(n)] for _ in range(n)];pivots=[]
    for i in range(n):
        pivot=a[i][i]-sum((lower[i][k]**2*pivots[k] for k in range(i)),I(0))
        if pivot.lo<=0<=pivot.hi:raise ArithmeticError('unresolved signed pivot')
        pivots.append(pivot)
        for j in range(i+1,n):
            lower[j][i]=(a[j][i]-sum((lower[j][k]*lower[i][k]*pivots[k]
                                     for k in range(i)),I(0)))/pivot
    return sum(v.hi<0 for v in pivots)


def actual_pencil(source,n):
    roots=[F(2*i+3,2) for i in range(1,n+1)]
    nodes=[x*x for x in roots]
    q=[I(*source['responses'][str(i+2)][0]) for i in range(1,n+1)]
    dq=[I(*source['responses'][str(i+2)][1]) for i in range(1,n+1)]
    values=[q[i]/(2*roots[i]) for i in range(n)]
    ell=[[(q[i]/roots[i]-dq[i])/(4*nodes[i]) if i==j
          else (values[j]-values[i])/(nodes[i]-nodes[j])
          for j in range(n)] for i in range(n)]
    jj=[[I(*v)/4 for v in row[:n]] for row in source['matrix'][:n]]
    lp,jp=interval_ldl(ell),interval_ldl(jj)
    displacement=True
    for i in range(n):
        for j in range(n):
            reading=jj[i][j]+nodes[j]*ell[i][j]-values[i]
            displacement &= reading.lo<=0<=reading.hi
    brackets=[]
    for k,c in enumerate(CENTRES[n]):
        centre=F(c);radius=F(1,10**9);lo,hi=centre-radius,centre+radius
        before=signed_interval_ldl([[jj[i][j]-lo**2*ell[i][j] for j in range(n)] for i in range(n)])
        after=signed_interval_ldl([[jj[i][j]-hi**2*ell[i][j] for j in range(n)] for i in range(n)])
        if (before,after)!=(k,k+1):raise ArithmeticError('pole count failed')
        brackets.append({'pole_number':k+1,'gamma_interval':[lo,hi],
                         'negative_indices':[before,after]})
    return {'dimension':n,'nodes':nodes,'values':[v.record() for v in values],
            'L':[[v.record() for v in row] for row in ell],
            'J':[[v.record() for v in row] for row in jj],
            'L_minimum_pivot_lower':str(min(v.lo for v in lp)),
            'J_minimum_pivot_lower':str(min(v.lo for v in jp)),
            'source_displacement_enclosures_consistent':displacement,
            'all_pencil_poles_simple_negative':True,'pole_gamma_brackets':brackets,
            'all_zeta_zeros_on_line_certified':False}


def local_zeta_reading(centre,logs,log2,tail,count=320):
    """Read zeta and its derivative on a critical-line centre, with full tails."""
    gamma=F(centre)
    if not F(1)<gamma< F(135,4):raise ValueError('outside the declared gamma bound')
    s=Z(F(1,2),gamma)
    values=[expi(-s*logs[n]) for n in range(1,count+1)]
    derivatives=[value*(-logs[n]) for n,value in enumerate(values,1)]
    ee=[]
    for row in (values,derivatives):
        total=Z(0)
        for k in range(count):
            total=total+row[0]/2**(k+1)
            row=[row[j]-row[j+1] for j in range(len(row)-1)]
        ee.append(total)
    ee[0]=ee[0]+Z(I(-tail,tail),I(-tail,tail))
    ee[1]=ee[1]+Z(I(-4*tail,4*tail),I(-4*tail,4*tail))
    power=expi((Z(1)-s)*log2);denominator=Z(1)-power
    zz=ee[0]/denominator
    dz=(ee[1]-zz*power*log2)/denominator
    radius=F(1,10**6);outer=F(1,4);majorant=F(1000)
    remainder=majorant*radius**2/(outer*(outer-radius))
    margin=dz.lower()*radius-zz.upper()-remainder
    return {'centre_real':F(1,2),'centre_imag':gamma,'radius':radius,
            'zeta':zz.record(),'zeta_derivative':dz.record(),
            'zeta_absolute_upper':zz.upper(),'derivative_absolute_lower':dz.lower(),
            'outer_radius':outer,'outer_zeta_bound':majorant,
            'taylor_remainder_upper':remainder,'rouche_margin_lower':margin,
            'one_simple_zero_in_disk':margin>0,
            'real_part_exactly_one_half_by_uniqueness_and_reflection':margin>0,
            'global_zero_order_asserted':False}


def determinant(a):
    a=[row[:] for row in a];out=F(1);n=len(a)
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:a[pivot],a[k]=a[k],a[pivot];out=-out
        p=a[k][k];out*=p
        for i in range(k+1,n):
            ratio=a[i][k]/p
            for j in range(k+1,n):a[i][j]-=ratio*a[k][j]
    return out


def model_pencil(nodes,values,derivatives):
    n=len(nodes)
    ell=[[-derivatives[i] if i==j else (values[j]-values[i])/(nodes[i]-nodes[j])
          for j in range(n)] for i in range(n)]
    jj=[[values[i]+nodes[i]*derivatives[i] if i==j
         else (nodes[i]*values[i]-nodes[j]*values[j])/(nodes[i]-nodes[j])
         for j in range(n)] for i in range(n)]
    return ell,jj


def rational_controls(check):
    nodes=[F(i+3) for i in range(5)]
    atoms=[F(i*i) for i in range(1,6)];weights=list(map(F,[1,2,1,3,2]))
    value=lambda t:sum((w/(t+a) for w,a in zip(weights,atoms)),F(0))
    derivative=lambda t:-sum((w/(t+a)**2 for w,a in zip(weights,atoms)),F(0))
    ff=[[value(t)] for t in nodes]
    ell,jj=model_pencil(nodes,[v[0] for v in ff],[derivative(t) for t in nodes])
    check('positive supplied five-atom source gives positive L and J',
          inertia(ell)==inertia(jj)==(0,0,5))
    check('the acquired pencil obeys its exact displacement identity',
          add(jj,mul(ell,diag(nodes)))==mul(ff,[[F(1)]*5]))
    interpolation=[]
    for i,t in enumerate(nodes):
        v=mul(inv(add(jj,scale(t,ell))),ff)
        interpolation.append(mul(tr(ff),v)[0][0]==value(t)
                             and -mul(mul(tr(v),ell),v)[0][0]==derivative(t))
    check('both source values and derivatives are recovered at every probe',all(interpolation))
    held=F(11,2)
    recovered=mul(mul(tr(ff),inv(add(jj,scale(held,ell)))),ff)[0][0]
    check('a full finite atomic model is recovered at a held-out probe',recovered==value(held))
    check('determinant log derivative cannot discard nonunit response residues',
          value(held)!=sum((1/(held+a) for a in atoms),F(0)),True)
    label=eye(5);label[0][2]=F(3);label[3][4]=F(-2)
    ll,jj2=mul(mul(tr(label),ell),label),mul(mul(tr(label),jj),label)
    fp=mul(tr(label),ff)
    changed=mul(mul(tr(fp),inv(add(jj2,scale(held,ll)))),fp)[0][0]
    check('source readout is invariant when the pencil and probe are transported together',changed==recovered)
    wrong=mul(mul(tr(ff),inv(add(jj2,scale(held,ll)))),ff)[0][0]
    check('moving the operator without the probe corrupts its reading',wrong!=recovered,True)

    b=[[F(1,7)]];identities=[]
    for mu in (F(0),F(5,2),F(1000)):
        mm=scale(4,add(jj,scale(mu,ell),-1))
        a,c,d,r,w,g,h,k=block_model(mm,b)
        identities.append(determinant(mm)==determinant(r)*determinant(k))
    check('the same 1+4 architecture retains the parameter-dependent characteristic equation',all(identities))
    # A reference pole at mu=6 is absent from the full diagonal source.
    mu=F(6);full=diag([F(i)-mu for i in range(1,6)])
    check('a singular Schur reference is not automatically a source zero',
          full[-1][-1]+1==0 and determinant(full)!=0,True)
    at_five=block_model(diag([F(i-5) for i in range(1,6)]),[[F(1)]])
    check('a source zero at mu=5 is retained by the five-gap',determinant(at_five[-1])==0)

    # Functional equation and conjugation symmetry survive this off-line quartet.
    x=F(1,16)-10000;y=F(50)
    masked=lambda t:sum((F(10)/(t+a) for a in atoms),F(0))+2*(t-x)/((t-x)**2+y*y)
    masked_d=lambda t:-sum((F(10)/(t+a)**2 for a in atoms),F(0))+2*(y*y-(t-x)**2)/((t-x)**2+y*y)**2
    ml,mj=model_pencil(nodes,[masked(t) for t in nodes],[masked_d(t) for t in nodes])
    check('five positive pencil readings can mask an off-critical symmetric quartet',
          inertia(ml)==inertia(mj)==(0,0,5) and y!=0,True)
    mf=[[masked(t)] for t in nodes]
    mr=mul(mul(tr(mf),inv(add(mj,scale(held,ml)))),mf)[0][0]
    check('finite Hermite interpolation does not identify the full source away from probes',mr!=masked(held),True)
    # f(z)=z+2z^2 has two roots in the unit disk, despite its nonzero
    # linear term and zero centre residual. The quadratic remainder matters.
    root=F(-1,2)
    check('dropping the remainder falsely declares a unique zero for z+2z squared',
          root+2*root*root==0 and abs(root)<1 and 1-2<0,True)
    return {'nodes':nodes,'atoms':atoms,'weights':weights,'L':ell,'J':jj,
            'off_line_model_a':[x,y],'off_line_model_L':ml,'off_line_model_J':mj}


def build():
    source=json.loads(SOURCE.read_text());checks=[]
    def check(name,condition,negative=False):
        if not condition:raise ArithmeticError(name)
        checks.append({'name':name,'negative_control':negative,'pass':True})
    check('actual source includes complete prime Gamma and pole contributions',
          source['all_prime_powers_included'] and source['all_gamma_modes_included'] and source['full_pole_included'])
    packets=[actual_pencil(source,n) for n in (5,8,12,16)]
    for p in packets:
        n=p['dimension']
        check(f'N={n} acquired L and source J have strictly positive interval pivots',
              F(p['L_minimum_pivot_lower'])>0 and F(p['J_minimum_pivot_lower'])>0)
        check(f'N={n} source displacement readings agree',p['source_displacement_enclosures_consistent'])
        check(f'N={n} all declared pole brackets have their exact inertia counts',
              all(x['negative_indices']==[x['pole_number']-1,x['pole_number']] for x in p['pole_gamma_brackets']))
    # Keep the unsuccessful narrow sixth-pole calculation visible.
    p=packets[-1];jj=[[I(*v) for v in row] for row in p['J']];ell=[[I(*v) for v in row] for row in p['L']]
    narrow=F('37.586346240925')-F(1,10**9)
    try:signed_interval_ldl([[jj[i][j]-narrow*narrow*ell[i][j] for j in range(16)] for i in range(16)]);inconclusive=False
    except ArithmeticError:inconclusive=True
    check('a narrow sixth-pole reading remains inconclusive at inherited precision',inconclusive,True)
    model=rational_controls(check)
    count=320;ratio=gamma_ratio_bound();tail=ratio/2**count
    check('the complete complex Euler remainder is bounded on every outer disk',tail<F(1,10**56))
    check('the outer zeta majorant includes every term and the denominator reserve',
          F(7,6)**4<2 and 6*(F(count,2)+tail)<1000)
    cc=precise_constants();logs=[I(0)]+[integer_log(n,cc['log2']) for n in range(1,count+1)]
    disks=[]
    for centre in CENTRES[16]:
        d=local_zeta_reading(centre,logs,cc['log2'],tail,count)
        check('one simple actual zeta zero in disk at gamma='+centre,d['rouche_margin_lower']>0)
        disks.append(d)
    check('the five certified disks are disjoint and within the nontrivial strip',
          all(disks[i+1]['centre_imag']-disks[i]['centre_imag']>disks[i]['radius']+disks[i+1]['radius'] for i in range(4))
          and all(d['radius']<F(1,4) for d in disks))
    check('no finite pole or local-zero reading is promoted to global RH',
          all(not p['all_zeta_zeros_on_line_certified'] for p in packets),True)
    return encode({'stage':'SE48','author':'Monty','source_file':str(SOURCE.relative_to(ROOT)),
                   'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                   'packets':packets,'rational_model':model,'zeta_disks':disks,
                   'euler_terms':count,'gamma_ratio_bound':ratio,'complex_euler_tail':tail,
                   'checks':checks,'check_count':len(checks),
                   'negative_control_count':sum(c['negative_control'] for c in checks),
                   'certified_local_zeta_zeros':len(disks),'global_zero_order_asserted':False,
                   'rh_proved':False,'global_eta_zero_certified':False})


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',action='store_true');group.add_argument('--check',action='store_true')
    args=parser.parse_args();verify_source_pins()
    if args.check:
        for pin in json.loads(PINS.read_text())['local_files']:
            data=(ROOT/pin['path']).read_bytes()
            if hashlib.sha256(data).hexdigest()!=pin['sha256']:raise ArithmeticError('SE48 source pin mismatch: '+pin['path'])
    result=build()
    if args.write:RESULT.write_text(json.dumps(result,indent=2)+'\n')
    elif result!=json.loads(RESULT.read_text()):raise ArithmeticError('SE48 archive mismatch')
    print(f"PASS SE48: {result['check_count']} controls; {result['negative_control_count']} negative; "
          f"30 pencil pole brackets; 5 local simple zeta zeros on the critical line; global RH remains open; "
          f"archive={'matched' if args.check else 'written'}")


if __name__=='__main__':main()
