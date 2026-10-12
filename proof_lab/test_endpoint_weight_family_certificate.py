"""Independent controls for SE17's source-preserving weight family."""
from fractions import Fraction as F
import itertools
from math import isqrt
import unittest

from proof_lab.endpoint_full_aperture_certificate import I, log_positive, sqrt_integer
from proof_lab.endpoint_global_eta_certificate import integer_log
from proof_lab.endpoint_signed_return_certificate import prime_catalogue
from proof_lab.endpoint_weight_family_certificate import (
    ALPHAS, ETA, FLOOR, MG_CAP, NATIVE_FLOOR, add_auxiliary_catalogue,
    auxiliary_row_lower, gamma_lower, gamma_polynomial, shaped_prime_upper,
)


def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def finite_catalogue():
    """Independent rational catalogue at three square prime-power positions."""
    limit = 64
    entries = {4:F(1), 16:F(2), 64:F(3)}
    weights = [I(entries.get(n, 0)) for n in range(limit+1)]
    prefix, suffix, peaks = [], [], []
    for n in range(limit+1):
        prefix.append(I(sum((w*j*isqrt(j) for j,w in entries.items() if j<=n), F(0))))
        suffix.append(I(sum((w/F(j*j*isqrt(j)) for j,w in entries.items() if j>n), F(0))))
        peaks.append(I(entries.get(n,F(0))/F(n*isqrt(n)) if n in entries else 0))
    cat = dict(limit=limit, prefix=prefix, suffix=suffix, peaks=peaks,
               weights=weights, mass=suffix[0], tail=I(0), log_limit=log_positive(limit))
    cat=add_auxiliary_catalogue(cat)
    cat['aux_mass'],cat['aux_tail']=cat['aux_suffix'][0],I(0)
    return cat,entries


class WeightFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat=add_auxiliary_catalogue(prime_catalogue())

    def test_gamma_potential_against_separately_integrated_exponentials(self):
        # Three pieces: y<x, y>x, and the reflected kernel. At rational z
        # all exponential values are rational; no floating quadrature enters.
        for modes,z in itertools.product((1,2,4,16),(F(1,2),F(1,4),F(3,4))):
            row=F(0)
            for k in range(modes):
                beta=F(4*k+1,2)
                for a,sign in ((F(2),1),(F(4),-1)):
                    eb,ea=z**int(2*beta),z**int(2*a)
                    left=(eb-ea)/(a-beta)
                    right=ea/(a+beta)
                    reflected=eb/(a+beta)
                    row+=sign*z**3*(left+right-reflected)/(z-z**5)
            c=sum((F(4,4*k+1) for k in range(modes)),F(0))
            self.assertEqual(gamma_lower(z,gamma_polynomial(modes)),(c-MG_CAP)*z**6-row)

    def test_removable_boundary_uses_the_odd_derivative_not_zero(self):
        for modes in (1,2,4,16):
            # At x->0, derivative of each odd kernel gives the integral
            # 2 beta*(1/(beta+2)-1/(beta+4)); q_Gamma'(0)=2.
            derivative_row=sum((F(4*k+1)*
                (1/(F(4*k+1,2)+2)-1/(F(4*k+1,2)+4))/2
                for k in range(modes)),F(0))
            c=sum((F(4,4*k+1) for k in range(modes)),F(0))
            actual=gamma_lower(F(1),gamma_polynomial(modes))
            self.assertEqual(actual,c-MG_CAP-derivative_row)
            self.assertNotEqual(actual,c-MG_CAP)

    def test_auxiliary_mass_against_independent_alternating_series(self):
        count,log2=2048,log_positive(2)
        e,d=I(0),I(0)
        for n in range(1,count+1):
            coefficient=F((-1)**(n-1),n**5)/sqrt_integer(n)
            e=e+coefficient
            d=d+coefficient*integer_log(n,log2)
        remainder=I(1)/((count+1)**5*sqrt_integer(count+1))
        e=e+I(0,remainder.hi)
        d=d+I(0,(remainder*integer_log(count+1,log2)).hi)
        oracle=log2/(16*sqrt_integer(2)-1)+d/e
        self.assertLess(self.cat['aux_mass'].lo,oracle.lo)
        self.assertGreater(self.cat['aux_mass'].hi,oracle.hi)
        wrong=log2/(16*sqrt_integer(2)-1)-d/e
        self.assertGreater(wrong.lo,self.cat['aux_mass'].hi)

    def test_prime_shape_against_direct_translated_positive_weight(self):
        cat,entries=finite_catalogue()
        for k,alpha in itertools.product((0,1,2,3),ALPHAS):
            def m(j): return F(1,8**abs(j))
            def q(j): return F(1,2**abs(j))*(1-alpha*F(1,64**abs(j)))
            direct=F(0)
            for j,n in enumerate((4,16,64),start=1):
                direct+=entries[n]*F(1,2**j)*m(k)/q(k)*(
                    m(k-j)*q(k-j)+m(k+j)*q(k+j))
            z=F(1,2**k)
            upper=shaped_prime_upper(z,z,cat,alpha)
            self.assertGreaterEqual(F(upper.hi),direct)
            self.assertLess(F(upper.hi)-direct,F(1,10**70))

    def test_auxiliary_cell_lower_handles_a_straddled_event(self):
        cat,entries=finite_catalogue()
        left,right=F(49,100),F(51,100)
        lower=auxiliary_row_lower(left,right,cat)
        mass=sum((w/F(n**5*isqrt(n)) for n,w in entries.items()),F(0))
        for z in (left,F(1,2),right):
            direct=z**6*mass+sum((w*min(F(n**4*isqrt(n))*z**6,
                1/(F(n**5*isqrt(n))*z**14)) for n,w in entries.items()),F(0))
            self.assertLessEqual(F(lower),direct)

    def test_certifying_weight_cone_is_affine_before_division(self):
        kernel=[[F(0),F(1),F(1)],[F(1),F(0),F(0)],[F(1),F(0),F(0)]]
        q0,q1=[F(1),F(2),F(1)],[F(1),F(1),F(2)]
        diagonal=[F(3),F(1),F(1)]
        def slack(q): return [diagonal[i]*q[i]-dot(kernel[i],q) for i in range(3)]
        for t in (F(0),F(1,7),F(1,2),F(1)):
            q=[(1-t)*a+t*b for a,b in zip(q0,q1)]
            self.assertEqual(slack(q),[(1-t)*a+t*b for a,b in zip(slack(q0),slack(q1))])
            self.assertTrue(all(v>=0 for v in slack(q)))
            self.assertEqual([dot(row,q)/q[i] for i,row in enumerate(kernel)],
                             [dot(row,[7*v for v in q])/(7*q[i]) for i,row in enumerate(kernel)])

    def test_pointwise_switching_does_not_follow_from_family_endpoints(self):
        # Each full endpoint weight has nonnegative slack in the preceding
        # star kernel. Selecting its larger leaf independently breaks it.
        kernel=[[F(0),F(1),F(1)],[F(1),F(0),F(0)],[F(1),F(0),F(0)]]
        diagonal=[F(3),F(1),F(1)]
        for q in ([F(1),F(2),F(1)],[F(1),F(1),F(2)]):
            self.assertTrue(all(diagonal[i]*q[i]>=dot(kernel[i],q) for i in range(3)))
        switched=[F(1),F(2),F(2)]
        self.assertLess(diagonal[0]*switched[0]-dot(kernel[0],switched),0)

    def test_two_different_weights_preserve_the_complex_source_identity(self):
        kernels=([[F(2),F(1)],[F(1),F(3)]],[[F(1),F(4)],[F(4),F(2)]])
        weights=([F(1),F(3)],[F(2),F(1)])
        h=[(F(2),F(1)),(F(-1),F(3))]
        source,comparison,residual=F(0),F(0),F(0)
        for kernel,q,scale in zip(kernels,weights,(1-ETA,F(1))):
            for i,j in itertools.product(range(2),repeat=2):
                source-=scale*kernel[i][j]*dot(h[i],h[j])
                comparison-=scale*kernel[i][j]*q[j]/q[i]*dot(h[i],h[i])
                delta=[h[i][a]/q[i]-h[j][a]/q[j] for a in range(2)]
                residual+=scale*kernel[i][j]*q[i]*q[j]*dot(delta,delta)/2
        self.assertEqual(source,comparison+residual)
        self.assertGreater(residual,0)

    def test_native_shift_uses_the_graph_conversion(self):
        self.assertEqual(NATIVE_FLOOR,F(1,7380))
        self.assertEqual(ETA-NATIVE_FLOOR,F(10883,18450))
        self.assertLess(NATIVE_FLOOR,FLOOR)
        for physical,positive in itertools.product((F(0),F(1,7),F(3)),repeat=2):
            source_lower=FLOOR*physical+2*ETA*positive
            native_upper=(2+MG_CAP)*physical+2*positive
            self.assertGreaterEqual(source_lower,NATIVE_FLOOR*native_upper)


if __name__=='__main__':
    unittest.main()
