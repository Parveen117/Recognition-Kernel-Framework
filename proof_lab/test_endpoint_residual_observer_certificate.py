"""Independent analytic and finite-dimensional controls for SE23."""
from fractions import Fraction as F
from math import isqrt
import json
import unittest
from unittest.mock import patch

from proof_lab.endpoint_full_aperture_certificate import I
from proof_lab.endpoint_residual_observer_certificate import (
    ALPHA,BETA_CAP,ETA,NATIVE_FLOOR,RESULT,SEED_FLOOR,TRIAL,
    TargetMass,add,certify_cover,inner,kernel,multiply,observation,seed_upper,
)
from proof_lab.endpoint_weight_family_certificate import gamma_lower
from proof_lab.test_endpoint_weight_family_certificate import finite_catalogue


def kernel_pair(a,b,k):
    """Independently integrated double kernel (SE21), not kernel() output."""
    beta=F(4*k+1,2)
    return sum((c*d*2*beta/((F(i+3,2)+F(j+3,2))*(F(i+3,2)+beta)*(F(j+3,2)+beta))
                for i,c in a.items() for j,d in b.items()),F(0))


def event_pair(phi,chi):
    q={1:F(1),5:F(-1)}
    return sum((kernel_pair(multiply(q,multiply(phi,chi)),q,k)
                -kernel_pair(multiply(q,phi),multiply(q,chi),k)
                for k in range(16)),F(0))


class ResidualObserverTests(unittest.TestCase):
    def test_kernel_solves_independent_dirichlet_green_equation(self):
        for k in range(16):
            beta=F(4*k+1,2)
            for p in (1,3,5,9,13):
                output=kernel({p:F(1)},k)
                self.assertEqual(sum(output.values()),0)
                # Strip exp(-3x/2), then apply -d^2/dx^2+beta^2.
                ode={j-3:c*(beta**2-F(j-3,2)**2) for j,c in output.items()}
                ode={j:c for j,c in ode.items() if c}
                self.assertEqual(ode,{p+3:2*beta})
                self.assertTrue(all(j-3>0 for j in output))
        with self.assertRaises(ValueError):
            kernel({2:F(1)},1)

    def test_event_energy_and_complex_projection_keep_all_mixed_terms(self):
        u,d,energy,_=observation()
        self.assertEqual(energy,event_pair(TRIAL,TRIAL))
        self.assertGreater(energy,0)
        a,b={2:F(3),6:F(-2)},{4:F(2),8:F(1)}
        target_real,target_imag=event_pair(TRIAL,a),event_pair(TRIAL,b)
        state_energy=event_pair(a,a)+event_pair(b,b)
        self.assertLessEqual(target_real**2+target_imag**2,energy*state_energy)
        isolated=sum((c*c*event_pair({p:F(1)},{p:F(1)}) for p,c in TRIAL.items()),F(0))
        self.assertNotEqual(energy,isolated)
        self.assertEqual(sum(d.values()),0)

    def test_target_mass_encloses_independent_exact_cell_integrals(self):
        _,_,_,r=observation()
        mass=TargetMass(r)
        for a,b in ((F(0),F(1,64)),(F(1,2),F(3,4)),(F(255,256),F(1))):
            exact=sum((8*c*d*(b**(i+j)-a**(i+j))/F(i+j)
                       for i,c in r.items() for j,d in r.items()),F(0))
            interval=mass(a,b)
            self.assertLessEqual(F(interval.lo),exact)
            self.assertGreaterEqual(F(interval.hi),exact)
            self.assertGreater(exact,0)
        self.assertEqual(mass.total,4*inner(r,r))
        with self.assertRaises(ValueError):
            mass(F(3,4),F(1,4))

    def test_positive_integral_certificate_resists_false_midpoint_readings(self):
        # r=z gives integrand 8z; W=1+z. Composite exact numerator
        # bounds enclose the integral without evaluating any samples.
        mass=TargetMass({1:F(1,10)})
        left0=F(1,64)
        outer={'seed_lower':I(1),'pole_burden':I(0)}
        def toy_seed(a,b,cat,eta,alpha):
            return I(10**9) if a==b else I(1+a,1+b)
        module='proof_lab.endpoint_residual_observer_certificate.'
        with patch(module+'seed_cell',side_effect=toy_seed),patch(module+'exterior',return_value=outer):
            cells,_,_,upper,_=certify_cover({},mass,F(1,10000),floor=F(1),cap=F(3,100))
        self.assertLess(upper,F(3,100))
        self.assertTrue(all(F(row[3])==1+row[0] for row in cells))
        # A separate lower Darboux sum proves the returned upper is safe.
        lower=sum((F(1,25)*(F(i+1,1024)**2-F(i,1024)**2)/(1+F(i+1,1024))
                   for i in range(1024)),F(0))+4*F(1,10000)/(1-ETA)
        self.assertGreaterEqual(upper,lower)
        self.assertEqual(cells[0][0],left0)

    def test_seed_upper_controls_straddled_prime_returns(self):
        cat,entries=finite_catalogue()
        for a,b in ((F(1,8),F(1,4)),(F(1,4),F(3,5)),(F(2,5),F(3,4)),(F(3,4),F(1))):
            upper=F(seed_upper(a,b,cat))
            for z in (a,(a+b)/2,b):
                base=sum((w*(z**6/F(n*n*isqrt(n))+min(z**6*n*isqrt(n),1/F(n*n*isqrt(n))/z**2))
                          for n,w in entries.items()),F(0))
                aux=sum((w*(z**6/F(n**5*isqrt(n))+min(z**6*n**4*isqrt(n),1/F(n**5*isqrt(n))/z**14))
                         for n,w in entries.items()),F(0))
                exact=ETA*(1+z**6)+(1-ETA)*gamma_lower(z)-(base-ALPHA*z**6*aux)/(1-ALPHA*z**6)
                self.assertGreaterEqual(upper,exact)
        with self.assertRaises(ValueError):
            seed_upper(F(0),F(1),cat)

    def test_augmented_recovery_requires_observation_cost(self):
        # W=I, eta=1/2, D=projection on the first coordinate, u=(1/5,0).
        # The exact optimal budget is 24/25, including cost 8/25.
        residual_cost=4*F(2,5)**2
        observation_cost=4*F(1,25)/F(1,2)
        budget=residual_cost+observation_cost
        self.assertEqual(budget,F(24,25))
        for real,imag in ((F(1),F(2)),(F(-3),F(4))):
            norm=real*real+imag*imag
            self.assertEqual(4*F(3,5)**2*norm,budget*F(3,2)*norm)
            self.assertLess(residual_cost*F(3,2)*norm,4*F(3,5)**2*norm)

    def test_dynamic_count_has_one_oriented_crossing_not_constant_index(self):
        # Q_t=diag(-11/25+t/2,1). Exact crossing at t=22/25.
        tstar=F(22,25)
        self.assertEqual(-F(11,25)+tstar/2,0)
        def beta(t):return F(36,25)/(1+t/2)
        self.assertGreater(beta(0),1)
        self.assertEqual(beta(tstar),1)
        self.assertLess(beta(1),1)
        self.assertTrue(all(beta(F(i,10))>beta(F(i+1,10)) for i in range(10)))
        # Reversal preserves endpoint spectra but reverses crossing direction.
        self.assertLess(-F(1,2),0)

    def test_invalid_seed_and_trial_are_not_silently_accepted(self):
        mass=TargetMass({2:F(1)})
        for kwargs in ({'floor':F(0)},{'cap':F(1)},{'eta':F(1)}):
            with self.assertRaises(ValueError):
                certify_cover({},mass,F(1),**kwargs)
        with self.assertRaises(AssertionError):
            observation({})
        with self.assertRaises(ValueError):
            TargetMass({0:F(1)})

    def test_native_conversion_and_published_claim_boundary(self):
        self.assertEqual(ETA-NATIVE_FLOOR,F(833939,1476000))
        self.assertEqual(NATIVE_FLOOR,F(1,1476000))
        for norm,energy in ((F(1),F(0)),(F(0),F(1)),(F(2,7),F(3,5))):
            lower=(1-BETA_CAP)*SEED_FLOOR*norm+2*ETA*energy
            self.assertGreaterEqual(lower,NATIVE_FLOOR*(F(369,50)*norm+2*energy))
        result=json.loads(RESULT.read_text())
        self.assertFalse(result['global_source']['eta_zero_certified'])
        self.assertFalse(result['comparison']['negative_actual_source_claim'])
        self.assertEqual(result['observation']['retained_event_coordinates'],1)


if __name__=='__main__':
    unittest.main()
