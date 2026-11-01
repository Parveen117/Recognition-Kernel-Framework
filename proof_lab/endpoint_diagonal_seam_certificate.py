"""SE26: exact diagonal/circle transport with the actual RH source retained.

This audit implements a comparison diagonal, reversible rational circle
coordinates, an explicit reference shift, and actual Gamma/prime controls.
It does not subtract a reference constant from a positivity obligation.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from proof_lab import endpoint_sectoral_recovery_certificate as source

ROOT = Path(__file__).resolve().parents[1]
RESULT = Path(__file__).with_name('ENDPOINT_DIAGONAL_SEAM_RESULT.json')
PINS = ROOT/'papers/rkf_completed_weil_endpoint/development/SE26_SOURCE_PINS.json'


@dataclass(frozen=True)
class ShiftReference:
    baseline: F

    def display(self, eta):
        return F(eta)-self.baseline

    def source_eta(self, displayed):
        return self.baseline+F(displayed)

    @property
    def unshifted_target(self):
        return -self.baseline


def diagonal_split(before, after):
    """Same typed scalar carrier: return common and contrast coordinates."""
    before,after=F(before),F(after)
    return (before+after)/2,(before-after)/2


def circle_coordinate(value, scale=F(1)):
    """(scale+iota*value)/(scale-iota*value), as two exact cut scalars."""
    value,scale=F(value),F(scale)
    if scale<=0:
        raise ValueError('A positive circle calibration is required')
    denominator=scale*scale+value*value
    return (scale*scale-value*value)/denominator,2*scale*value/denominator


def circle_inverse(real, turn, scale=F(1)):
    real,turn,scale=F(real),F(turn),F(scale)
    if scale<=0 or real*real+turn*turn!=1 or real==-1:
        raise ValueError('An admitted finite circle chart is required')
    return scale*turn/(1+real)


def replay():
    with localcontext() as context:
        context.prec=90
        inherited=source.verify_source_pins()
        archive=json.loads(source.RESULT.read_text())
        if archive['status']!='PASS_GLOBAL_SECTORAL_RECOVERY':
            raise AssertionError('The declared parent source certificate is absent')
        checks=[]
        def check(name, condition):
            if not condition:
                raise AssertionError(name)
            checks.append(dict(name=name,status='PASS'))

        ref=ShiftReference(F(1,2))
        check('parent_eta_and_floor',F(archive['global_source']['eta'])==source.ETA
              and F(archive['global_source']['shifted_native_floor'])==source.NATIVE_FLOOR)
        check('displayed_distance_is_004',ref.display(source.ETA)==F(1,25))
        check('displayed_004_keeps_source_eta_054',ref.source_eta(F(1,25))==F(27,50))
        check('unshifted_source_target_transports_to_minus_half',
              ref.source_eta(ref.unshifted_target)==0 and ref.unshifted_target==F(-1,2))
        check('displayed_zero_is_not_unshifted_source',ref.source_eta(0)==F(1,2))

        pairs=[(F(3),F(3)),(F(2),F(-1)),(F(0),F(5)),(F(-7,3),F(2,5))]
        for a,b in pairs:
            mean,contrast=diagonal_split(a,b)
            check('pair_recovery_'+str(len(checks)),(mean+contrast,mean-contrast)==(a,b))
            check('pair_full_energy_'+str(len(checks)),a*a+b*b==2*mean*mean+2*contrast*contrast)
        check('nonzero_diagonal_has_zero_contrast',diagonal_split(3,3)==(F(3),F(0)))

        circle=[]
        for value in (F(-1),F(-1,4),F(0),F(1,25),F(1,2),F(27,50),F(1)):
            for scale in (F(1),F(2)):
                real,turn=circle_coordinate(value,scale)
                check('circle_roundtrip_'+str(len(checks)),real*real+turn*turn==1
                      and circle_inverse(real,turn,scale)==value
                      and ((turn>0)-(turn<0))==((value>0)-(value<0)))
                circle.append(dict(value=str(value),scale=str(scale),real=str(real),turn=str(turn)))
        check('source_zero_is_circle_identity',circle_coordinate(0)==(F(1),F(0)))
        check('same_circle_radius_does_not_identify_states',
              circle_coordinate(F(1,4))!=circle_coordinate(F(-1,4)))
        try:
            circle_inverse(-1,0)
        except ValueError:
            check('excluded_infinite_chart_point_rejected',True)
        else:
            raise AssertionError('Infinite chart point was silently identified with zero')

        # A source invariant under every frame still cannot lose a half-unit shift.
        witness=F(-1,4)
        check('symmetric_negative_source_satisfies_parent_style_bound',
              witness+source.ETA>=source.NATIVE_FLOOR)
        check('same_source_fails_false_004_reinterpretation',witness+F(1,25)<0)

        q={k:c for c,k in source.GAMMA_WEIGHT}
        null_response={}
        for k in range(16):
            null_response=source.add(null_response,
                source.add(source.kernel(q,k),source.kernel(q,k),F(-1)))
        pole_pairing=source.inner({2:F(1,2),4:F(-1,2)},q)
        check('actual_Gamma_comparison_diagonal_is_null',null_response=={})
        check('actual_Gamma_null_mode_is_nonzero',source.inner(q,q)>0)
        check('actual_Gamma_null_mode_has_nonzero_pole_target',pole_pairing>0)
        try:
            source.observation({0:F(1)})
        except ValueError:
            check('null_event_coordinate_cannot_be_normalized',True)
        else:
            raise AssertionError('Zero-energy observation was accepted')

        # A smaller head suffices for a local failure control. All-integer
        # upper tails remain included; this is not the SE25 global replay.
        cat=source.rows.extend_catalogue(source.prime_catalogue(4096))
        left,right=F(9,10),F(9001,10000)
        failures={}
        for eta,ceiling in ((F(1,2),F(-3,50)),(F(1,25),F(-9,10))):
            upper=source.seed_upper(left,right,cat,eta)
            check('whole_cell_seed_failure_eta_'+str(eta),F(upper)<ceiling)
            failures[str(eta)]=dict(upper=str(upper),strict_rational_ceiling=str(ceiling))
        delta=ref.display(source.ETA)
        old=source.seed_cell(left,right,cat,source.ETA)
        transported=source.seed_cell(left,right,cat,ref.source_eta(delta))
        check('faithful_reference_preserves_the_entire_seed_interval',
              old.lo==transported.lo and old.hi==transported.hi)

        return dict(schema='rkf.endpoint-diagonal-seam.v1',date='2026-10-12',
            status='PASS_DIAGONAL_SEAM_ACCOUNTING_GLOBAL_BOUND_UNCHANGED',
            arithmetic='Exact Fraction and 90-digit outward Decimal',
            reference=dict(baseline=str(ref.baseline),parent_eta=str(source.ETA),
                displayed_distance=str(delta),source_at_displayed_zero='S_b + (1/2) I_X',
                displayed_unshifted_target=str(ref.unshifted_target),
                omitted_native_shift_if_misidentified='1/2'),
            diagonal=dict(kernel='All pairs (a,a) on the same admitted typed carrier',
                zero_contrast_implies_zero_state=False,mean_coordinate_retained=True),
            circle=dict(samples=circle,source_zero_image=['1','0'],
                source_sign_requires_oriented_arc=True,phase_discarding_is_not_faithful=True),
            actual_Gamma_blindness=dict(weight=[[str(c),k] for c,k in source.GAMMA_WEIGHT],
                modes=16,response_is_zero=True,norm_squared=str(source.inner(q,q)),
                pole_pairing=str(pole_pairing),full_pole_energy=str(4*pole_pairing*pole_pairing),
                conclusion='No bounded recovery of the pole from these Gamma differences alone',
                negative_actual_source_claim=False),
            seed_failure=dict(cell=[str(left),str(right)],catalogue=4096,
                prime_power_count=cat['prime_power_count'],complete_analytic_tails=True,
                upper_bounds=failures,scope='SE25 fixed-weight positive-multiplication-seed route only',
                actual_source_negativity_or_impossibility=False),
            unchanged_global_certificate=archive['global_source'],
            inherited_source_pins_checked=inherited,check_count=len(checks),checks=checks,
            not_certified=['global eta=0, eta=1/2 or eta=1/25 positivity',
                'RH or historical five-label/K0 completion','actual TVSP-to-VTSP arrow map',
                'zero scalar is not a number','whole operator-engine gate PASS',
                'formal proof-assistant or external verification'])


def verify_source_pins():
    pins=json.loads(PINS.read_text())['sha256']
    for p,expected in pins.items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=expected:
            raise AssertionError('SE26 source pin mismatch: '+p)
    return len(pins)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--write',action='store_true');group.add_argument('--check',action='store_true')
    args=parser.parse_args();result=replay()
    if args.write:
        if RESULT.exists():
            raise SystemExit('Refuse to overwrite existing evidence')
        RESULT.write_text(json.dumps(result,indent=2)+'\n')
    if args.check:
        if json.loads(RESULT.read_text())!=result:
            raise AssertionError('SE26 replay differs from archived evidence')
        print('Source pins checked:',verify_source_pins())
    print(json.dumps({k:result[k] for k in ('status','reference','actual_Gamma_blindness',
        'seed_failure','check_count')},indent=2))


if __name__=='__main__':
    main()
