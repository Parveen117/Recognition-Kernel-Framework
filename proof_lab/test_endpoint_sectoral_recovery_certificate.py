"""Independent algebraic and finite-source controls for SE25 (Python 3.12)."""
from fractions import Fraction as F
import unittest

from proof_lab import endpoint_sectoral_recovery_certificate as s


class SectoralRecoveryTests(unittest.TestCase):
    def test_gamma_Bernstein_identity_and_strict_positivity(self):
        u={2:F(1)};one_minus={0:F(1),2:F(-1)}
        def power(p,n):
            out={0:F(1)}
            for _ in range(n):out=s.multiply(out,p)
            return out
        bern=[F(1),F(514,375),F(119,1500),F(107,250)]
        p={}
        for j,multiplicity in enumerate((1,3,3,1)):
            p=s.add(p,s.multiply(power(u,j),power(one_minus,3-j)),bern[j]*multiplicity)
        self.assertEqual(p,{k-1:c for c,k in s.GAMMA_WEIGHT})
        self.assertGreater(min(bern),0)

    def test_prime_positive_decomposition(self):
        p=s.add({0:F(1697,20000),4:F(107,10000)},
                s.multiply({2:F(1),4:F(-1)},{0:F(1),2:F(-7419,20000)}))
        self.assertEqual(p,{k-1:c for c,k in s.PRIME_WEIGHT})
        self.assertLess(F(7419,20000),1)

    def test_kernel_pairing_symmetry(self):
        for k in (0,1,7,15):
            for p in (1,3,5,7):
                for q in (1,3,5,9):
                    self.assertEqual(s.inner({p:F(1)},s.kernel({q:F(1)},k)),
                                     s.inner({q:F(1)},s.kernel({p:F(1)},k)))

    def test_sixteen_sheet_event_energy_matches_sum(self):
        u,d,e,_=s.observation();q={k:c for c,k in s.GAMMA_WEIGHT}
        es=[]
        for k in range(16):
            dk=s.add(s.multiply(s.TRIAL,s.kernel(q,k)),s.kernel(u,k),F(-1))
            es.append(s.inner(u,dk))
        self.assertTrue(all(v>=0 for v in es))
        self.assertEqual(sum(es,F(0)),e)
        self.assertEqual(sum(d.values()),0)

    def test_four_trial_directions_keep_the_full_Gram(self):
        obs=[s.observation({k:F(1)}) for k in (2,4,6,8)]
        gram=[[s.inner(a[0],b[1]) for b in obs] for a in obs]
        self.assertEqual(gram,list(map(list,zip(*gram))))
        c=[s.TRIAL[k] for k in (2,4,6,8)]
        e=sum((c[i]*gram[i][j]*c[j] for i in range(4) for j in range(4)),F(0))
        self.assertEqual(e,s.observation()[2])
        diagonal=sum((c[i]**2*gram[i][i] for i in range(4)),F(0))
        self.assertNotEqual(e,diagonal)
        # Exact Schur elimination: every pivot of this declared Gram is positive.
        for k in range(4):
            pivot=gram[k][k];self.assertGreater(pivot,0)
            for i in range(k+1,4):
                for j in range(k+1,4):gram[i][j]-=gram[i][k]*gram[k][j]/pivot

    def test_constant_trial_is_null_and_rejected(self):
        with self.assertRaisesRegex(ValueError,'positive-energy'):
            s.observation({0:F(1)})

    def test_kernel_resonance_is_not_silently_divided(self):
        with self.assertRaisesRegex(ValueError,'Resonant'):
            s.kernel({2:F(1)},1)

    def test_residual_mass_retains_interference(self):
        _,d,_,r=s.observation();v={2:F(1,2),4:F(-1,2)}
        self.assertEqual(s.inner(r,r),s.inner(v,v)-2*s.inner(v,d)+s.inner(d,d))
        self.assertNotEqual(s.inner(r,r),s.inner(v,v)+s.inner(d,d))
        mass=s.TargetMass(r)
        self.assertEqual(mass.total,4*s.inner(r,r))
        for a,b in ((F(0),F(1,512)),(F(1,512),F(3,4)),(F(3,4),F(1))):
            integral=mass(a,b);self.assertGreaterEqual(integral.lo,0)
            self.assertGreater(integral.hi,0)

    def test_analytic_exterior_requires_full_catalogue(self):
        with self.assertRaisesRegex(ValueError,'Catalogue'):
            s.exterior({'limit':4096})

    def test_eta_zero_cannot_enter_this_positive_seed_replay(self):
        with self.assertRaisesRegex(ValueError,'0 < eta < 1'):
            s.seed_cell(F(1,2),F(3,4),None,eta=F(0))

    def test_native_floor_and_strict_global_improvement(self):
        self.assertEqual(s.NATIVE_FLOOR,F(1,369000))
        self.assertEqual(s.ETA-s.NATIVE_FLOOR,F(199259,369000))
        self.assertLess(s.ETA-s.NATIVE_FLOOR,F(20659,36900))


if __name__=='__main__':unittest.main()
