"""SE8: certify a 21/20 observer transport on the fixed SE7 reference chart.

The exact source dilation and native metric are derived in SE8. This replay
encloses the transported frequency minorant, including its full infinite tail.
It imports the immutable SE7 interval primitives; no new operator engine.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from math import prod
from pathlib import Path

try:
    from proof_lab import endpoint_full_aperture_certificate as seed_module
    from proof_lab.endpoint_full_aperture_certificate import (
        I, N, T, UP, constants, sqrt_integer, hurwitz_power, gamma_symbol,
        cosine, odd_bessel, gauss8, interval_ldl, analytic_budgets,
    )
    from proof_lab.endpoint_paired_aperture_budget import exp_upper
except ModuleNotFoundError:
    import endpoint_full_aperture_certificate as seed_module
    from endpoint_full_aperture_certificate import (
        I, N, T, UP, constants, sqrt_integer, hurwitz_power, gamma_symbol,
        cosine, odd_bessel, gauss8, interval_ldl, analytic_budgets,
    )
    from endpoint_paired_aperture_budget import exp_upper

SCALE=F(21,20)
RESULT=Path(__file__).with_name("ENDPOINT_OBSERVER_TRANSPORT_RESULT.json")
MATRIX=Path(__file__).with_name("ENDPOINT_OBSERVER_TRANSPORT_MATRIX.json")
SEED_MATRIX=Path(__file__).with_name("ENDPOINT_FULL_APERTURE_MATRIX.json")
SEED_RESULT=Path(__file__).with_name("ENDPOINT_FULL_APERTURE_RESULT.json")
SEED_SHA="93341695f66dcac38301464ee907da7aad5906c91cdbe42e5bf9cbea45f65c16"


def transported_poles(roots):
    """h_n(c)=integral phi_n(x)sinh(c*x/2) dx; c remains outside the Gram."""
    out=[]
    z=SCALE/4
    for n,root in zip(range(1,80,2),roots):
        term=I(z**n/prod(range(1,2*n+2,2)))
        total=term
        for k in range(1,41):
            term=term*z*z/(2*k*(2*n+2*k+1))
            total=total+term
        nxt=term*z*z/(82*(2*n+83))
        ratio=z*z/(84*(2*n+85))
        out.append(root*(total+I(0,(nxt/(1-ratio)).hi)))
    return out


def assemble(progress=False):
    pi,log2,mg=constants()
    zeta=[hurwitz_power(2*r+1) for r in range(1,12)]
    roots=[sqrt_integer(2*n+1) for n in range(1,80,2)]
    poles=transported_poles(roots)
    nodes,weights=gauss8()
    matrix=[[I(0) for _ in range(N)] for _ in range(N)]
    for panel in range(384):
        center=F(2*panel+1,16)
        for node,weight in zip(nodes,weights):
            t=center+node/16
            assert 0<t.lo<=t.hi<T
            physical_frequency=t/SCALE
            symbol=(gamma_symbol(physical_frequency,mg,zeta)
                    -sqrt_integer(2)*log2*cosine(physical_frequency*log2,pi)-F(1,5))
            bessel=odd_bessel(t/2)
            vector=[root*j*((-1)**k) for k,(root,j) in enumerate(zip(roots,bessel))]
            measure=weight*symbol/(16*pi)
            for i in range(N):
                scaled=measure*vector[i]
                for j in range(i+1):
                    matrix[i][j]=matrix[i][j]+scaled*vector[j]
        if progress and panel%64==63:
            print(f"transport panels {panel+1}/384",flush=True)
    for i in range(N):
        for j in range(i+1):
            value=matrix[i][j]-2*SCALE*poles[i]*poles[j]
            if i==j: value=value+F(1,5)
            matrix[i][j]=matrix[j][i]=value
    return matrix


def budgets():
    epsilon,_,_,symbol_bound=analytic_budgets()
    n=81
    d=F(24**n,prod(range(1,2*n,2)))
    tail_f=d/(1-F(576,163*165))
    # sqrt(c)<2 and exp(c/4)<2; use the complete vector sqrt(c)*h(c).
    e=4*(SCALE/4)**n/prod(range(1,2*n,2))
    tail_h=e/(1-(SCALE/4)**2/(163*165))
    tau_d=1600*tail_f**2+2*tail_h**2
    tau_b=11200*tail_f+2*tail_h
    assert tau_d<F(1,10**20) and tau_b<F(1,10**20)
    # The exact three-term lower bound for log(3) keeps prime 3 inactive.
    log3_lower=2*sum((F(1,2)**(2*k+1)/(2*k+1) for k in range(3)),F(0))
    assert F(7,10)<1<=SCALE<log3_lower
    assert F(T,1)/SCALE>24
    assert exp_upper(SCALE/4,12)<2 and SCALE<4
    aperture=SCALE/2
    assert exp_upper(3*aperture,20)<5
    # 2(sinh A-A) <= A^3 cosh(A)/3; bound the cosh tail after A^2/2.
    cosh_upper=1+(aperture**2/2)/(1-aperture**2/12)
    boundary_bound=aperture**3*cosh_upper/3
    assert boundary_bound<F(1,16)
    # sup_t t G'(t) <= 5/2: small-t first term + monotone tail.
    assert 2+4*(F(5,2)**(-3)+F(1,4)*F(5,2)**(-2))<F(5,2)
    assert F(27,16)<F(9,4) # 3*sqrt(3)/4 < 3/2 for t >= 1.
    assert 1-F(3,4)**2>0 and 3+6*F(-3,4)==F(-3,2)
    return epsilon,tau_d,tau_b,symbol_bound,log3_lower,boundary_bound


def _replay(progress=False):
    seed_bytes=SEED_MATRIX.read_bytes()
    assert hashlib.sha256(seed_bytes).hexdigest()==SEED_SHA
    seed=json.loads(seed_bytes)
    seed_result=json.loads(SEED_RESULT.read_text())
    assert seed_result['matrix_sha256']==SEED_SHA
    old=seed['matrix']
    epsilon,tau_d,tau_b,symbol_bound,log3_lower,boundary_bound=budgets()
    enclosed=assemble(progress)
    candidate=[[x.midpoint() for x in row] for row in enclosed]
    radius=Decimal(0)
    for row,midrow in zip(enclosed,candidate):
        total=Decimal(0)
        for x,mid in zip(row,midrow):
            total=UP.add(total,max(UP.subtract(mid,x.lo),UP.subtract(x.hi,mid)))
        radius=max(radius,total)
    error=I(radius)+N*epsilon
    assert error.hi<Decimal('0.000001')
    pivots=interval_ldl(candidate,F(18,1000000))
    assert I(F(18,1000000)-F(1,60000)).lo>error.hi
    q=F(1,100000)
    assert min(F(1,60000),F(1,5)-tau_d)-tau_b>q
    native=q/(q+F(289,16))
    reserve=2*native/11
    # Enclose exact comparison-form defects, not just midpoint differences.
    old_error=I(Decimal(seed_result['point_evaluation_matrix_norm_error_upper']))+epsilon
    new_quad=I(-epsilon,epsilon)
    deltas=[]
    for i in [0,3]:
        exact_new=enclosed[i][i]+new_quad
        exact_old=I(Decimal(old[i][i]))+I(old_error.hi.copy_negate(),old_error.hi)
        deltas.append(exact_new-exact_old)
    assert deltas[0].hi<I(F(-3,50)).lo
    assert deltas[1].lo>I(F(1,25)).hi
    assert F(1,25000)-F(3,50)<0
    archive={'schema':'rkf.endpoint-observer-transport-matrix.v1',
             'reference_aperture':'1/2','physical_aperture':'21/40','scale':'21/20',
             'basis':seed['basis'],'matrix':[[str(x) for x in row] for row in candidate]}
    encoded=json.dumps(archive,indent=2)+'\n'
    def rat(x):return f'{x.numerator}/{x.denominator}'
    result={
        'schema':'rkf.endpoint-observer-transport-certificate.v1','date':'2026-10-12','status':'PASS',
        'arithmetic':'SE7 outward-rounded 90-digit Decimal; exact Fraction budgets; guarded ambient precision 90',
        'scale':rat(SCALE),'reference_aperture':'1/2','physical_aperture':'21/40',
        'all_intermediate_scales_by_native_inclusion':['1','21/20'],
        'active_prime_powers':[2],'log3_lower':rat(log3_lower),'boundary_upper':rat(boundary_bound),
        'frequency_split_in_reference_coordinates':T,'high_frequency_floor':'1/5',
        'matrix_dimension':N,'quadrature_order':8,'panels':384,
        'quadrature_error_per_entry':rat(epsilon),'analytic_symbol_bound':rat(symbol_bound),
        'point_evaluation_matrix_norm_error_upper':str(radius),
        'total_leading_matrix_error_upper':str(error.hi),
        'ldl_shift':'18/1000000','positive_ldl_pivots':len(pivots),
        'ldl_pivot_enclosures':[x.record() for x in pivots],
        'exact_leading_matrix_floor':'1/60000','tail_deviation_upper':rat(tau_d),
        'tail_coupling_upper':rat(tau_b),'physical_source_floor':rat(q),
        'native_source_floor':rat(native),'relative_joint_reserve':rat(reserve),
        'comparison_defect_P1_diagonal':deltas[0].record(),
        'comparison_defect_P7_diagonal':deltas[1].record(),
        'comparison_defect_is_indefinite':True,'scalar_seed_floor_minus_defect_norm_test':'FAILS',
        'seed_matrix_sha256':SEED_SHA,'matrix_sha256':hashlib.sha256(encoded.encode()).hexdigest(),
        'not_certified':['all-scale transport','all-prime-event transitions','global eta=0 source sign',
                         'historical five-label endpoint or K0','Riemann hypothesis',
                         'proof-assistant verification or external review']}
    return result,encoded


def replay(progress=False):
    # The imported Bessel helper negates a Decimal tail. With precision 90
    # this is exact for its at-most-90-digit bound, unlike default precision 28.
    with localcontext() as ctx:
        ctx.prec=90
        return _replay(progress)


def audit_seed():
    """Revalidate the unchanged SE7 archive with exact Decimal sign handling."""
    with localcontext() as ctx:
        ctx.prec=90
        result,matrix=seed_module.replay(progress=True)
    assert matrix==SEED_MATRIX.read_text(encoding='utf-8')
    assert result==json.loads(SEED_RESULT.read_text(encoding='utf-8'))
    print(json.dumps({'status':'PASS','ambient_precision':90,
        'archived_seed_matrix_and_all_bounds_identical':True,
        'seed_matrix_sha256':result['matrix_sha256']},indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--check',action='store_true')
    mode.add_argument('--audit-seed',action='store_true')
    args=parser.parse_args()
    if args.audit_seed:
        audit_seed()
        return
    result,matrix=replay(progress=True)
    if args.write:
        MATRIX.write_text(matrix,encoding='utf-8')
        RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if args.check:
        if MATRIX.read_text(encoding='utf-8')!=matrix or json.loads(RESULT.read_text())!=result:
            raise SystemExit('SE8 replay mismatch: inspect changes instead of repinning.')
    keys=['status','scale','physical_aperture','positive_ldl_pivots','physical_source_floor',
          'native_source_floor','relative_joint_reserve','comparison_defect_is_indefinite','matrix_sha256']
    print(json.dumps({k:result[k] for k in keys},indent=2))


if __name__=='__main__':main()
