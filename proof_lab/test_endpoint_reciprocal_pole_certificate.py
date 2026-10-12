"""Independent controls for SE22's global reciprocal target budget."""
from fractions import Fraction as F
import json
import unittest
from unittest.mock import patch

from proof_lab.endpoint_full_aperture_certificate import I
from proof_lab.endpoint_reciprocal_pole_certificate import (
    ALPHA,BETA_CAP,ETA,NATIVE_FLOOR,RESULT,SEED_FLOOR,
    fixed_pole_control,integral_cover,pole_mass,
)
from proof_lab.endpoint_signed_return_certificate import prime_catalogue
from proof_lab.endpoint_weight_family_certificate import add_auxiliary_catalogue,shaped_prime_upper
from proof_lab.test_endpoint_weight_family_certificate import finite_catalogue


class ReciprocalPoleTests(unittest.TestCase):
    def test_exact_mass_against_independent_monomial_integration(self):
        coefficients={3:F(2),5:F(-4),7:F(2)}
        for a,b in ((F(0),F(1)),(F(1,64),F(1,3)),(F(7,8),F(1))):
            expected=sum((c*(b**(k+1)-a**(k+1))/(k+1)
                          for k,c in coefficients.items()),F(0))
            self.assertEqual(pole_mass(a,b),expected)
            self.assertGreater(expected,0)
        self.assertEqual(pole_mass(0,1),F(1,12))
        with self.assertRaises(ValueError):
            pole_mass(F(3,4),F(1,4))

    def test_refinement_covers_every_piece_and_boundary_mass(self):
        for count in (2,7,64):
            self.assertEqual(sum((pole_mass(F(k,count),F(k+1,count))
                                  for k in range(count)),F(0)),F(1,12))
        a,b,c=F(1,64),F(5,16),F(1)
        self.assertEqual(pole_mass(a,b)+pole_mass(b,c),pole_mass(a,c))
        self.assertGreater(pole_mass(0,F(1,64)),0)

    def test_reciprocal_integral_against_independently_integrated_linear_seed(self):
        # 2*z^3*(1-z^2)^2/(1+z)=2*z^3-2*z^4-2*z^5+2*z^6.
        exact=F(1,2)-F(2,5)-F(1,3)+F(2,7)
        self.assertEqual(exact,F(11,210))
        uppers=[]
        for count in (8,16,32,64):
            upper=sum((pole_mass(F(k,count),F(k+1,count))/(1+F(k,count))
                       for k in range(count)),F(0))
            self.assertGreater(upper,exact)
            uppers.append(upper)
        self.assertTrue(all(a>b for a,b in zip(uppers,uppers[1:])))

    def test_adaptive_acceptance_ignores_optimistic_midpoint_heuristic(self):
        module='proof_lab.endpoint_reciprocal_pole_certificate.'
        boundary=F(1,64)
        def toy_seed(left,right,cat,eta,alpha):
            if left==right:
                return I(1000000)  # deliberately false reading, used only to prioritize
            return I(1+left,1+right)
        outer={'seed_lower':I(1),'pole_burden':I(pole_mass(0,boundary))}
        with patch(module+'seed_cell',side_effect=toy_seed),patch(module+'exterior',return_value=outer):
            cells,_,upper,_=integral_cover({},floor=F(1),cap=F(53,1000))
        self.assertGreaterEqual(upper,F(11,210))
        self.assertLess(upper,F(53,1000))
        self.assertTrue(all(F(lower)==1+a for a,b,d,lower,u in cells))
        self.assertGreater(len(cells),1)

    def test_nonpositive_seed_and_non_strict_pole_cap_are_refused(self):
        with self.assertRaises(ValueError):
            integral_cover({},floor=F(0))
        with self.assertRaises(ValueError):
            integral_cover({},cap=F(1))
        module='proof_lab.endpoint_reciprocal_pole_certificate.'
        with patch(module+'exterior',return_value={'seed_lower':I(-1),'pole_burden':I(0)}):
            with self.assertRaises(AssertionError):
                integral_cover({})

    def test_rank_one_target_keeps_mixed_terms(self):
        # Each individual source diagonal is positive but their sum direction fails.
        v=[F(2,5),F(2,5)]
        beta=4*sum(x*x for x in v)
        self.assertGreater(beta,1)
        self.assertTrue(all(1-4*x*x>0 for x in v))
        source=sum(x*x for x in v)-4*sum(x*x for x in v)**2
        self.assertLess(source,0)
        # Complete complex weighted Cauchy control for a separate passing example.
        w=[F(1),F(2)];v=[F(1,4),F(1,4)]
        beta=4*sum(x*x/weight for x,weight in zip(v,w))
        self.assertEqual(beta,F(3,8))
        h=[(F(1),F(2)),(F(-3),F(1))]
        real=sum(v[k]*h[k][0] for k in range(2))
        imag=sum(v[k]*h[k][1] for k in range(2))
        energy=sum(w[k]*sum(t*t for t in h[k]) for k in range(2))
        self.assertLessEqual(4*(real*real+imag*imag),beta*energy)

    def test_new_alpha_against_direct_even_weight_translation(self):
        cat,entries=finite_catalogue()
        for k in range(4):
            def m(j):return F(1,8**abs(j))
            def q(j):return F(1,2**abs(j))*(1-ALPHA*F(1,64**abs(j)))
            direct=F(0)
            for j,n in enumerate((4,16,64),start=1):
                direct+=entries[n]*F(1,2**j)*m(k)/q(k)*(
                    m(k-j)*q(k-j)+m(k+j)*q(k+j))
            z=F(1,2**k)
            upper=shaped_prime_upper(z,z,cat,ALPHA)
            self.assertGreaterEqual(F(upper.hi),direct)
            self.assertLess(F(upper.hi)-direct,F(1,10**70))

    def test_same_weight_fixed_pole_failure_is_not_a_source_negative_witness(self):
        old=fixed_pole_control(add_auxiliary_catalogue(prime_catalogue()))
        self.assertLess(old.hi,I(-F(29,1000)).lo)
        record=json.loads(RESULT.read_text())
        self.assertEqual(record['status'],'PASS_GLOBAL_RECIPROCAL_POLE')
        self.assertFalse(record['fixed_pole_control']['actual_negative_source_claim'])

    def test_exact_native_conversion_and_zero_boundary(self):
        self.assertEqual(ETA,F(227,400))
        self.assertEqual(NATIVE_FLOOR,F(1,1476000))
        self.assertEqual(ETA-NATIVE_FLOOR,F(837629,1476000))
        self.assertLess(ETA-NATIVE_FLOOR,F(57,100))
        for physical,positive in ((F(0),F(1)),(F(3),F(0)),(F(2,7),F(4,3))):
            lower=(1-BETA_CAP)*SEED_FLOOR*physical+2*ETA*positive
            native_upper=F(369,50)*physical+2*positive
            self.assertGreaterEqual(lower,NATIVE_FLOOR*native_upper)
        record=json.loads(RESULT.read_text())
        self.assertFalse(record['global_source']['eta_zero_certified'])


if __name__=='__main__':
    unittest.main()
