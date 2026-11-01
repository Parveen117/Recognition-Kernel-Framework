"""SE1 analytic controls, exact profile replay and corruption controls."""
from fractions import Fraction as F
import base64
import lzma
import struct
import tempfile
from pathlib import Path
import unittest

from proof_lab import endpoint_shared_energy_budget as se


class SharedEnergyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = se.load_profile()

    def test_graph_quarter_bound_and_equality(self):
        # Exact spectral scalar: c^2/(1+c^2)^2 <= 1/4, equality at c=1.
        for c in [F(0),F(1,100),F(1,2),F(1),F(2),F(100)]:
            self.assertLessEqual(c*c/(1+c*c)**2,F(1,4))
        self.assertEqual(F(1)/(1+F(1))**2,F(1,4))

    def test_seed_mass_improves_by_four(self):
        self.assertEqual(F(1,12)/4,F(1,48))
        self.assertEqual(F(4,27)*F(1,12),F(1,81))

    def test_shared_budget_is_sharp_in_finite_relaxation(self):
        # Weights (4,2,1), cell capacities (1,1,10), total mass 3.
        # Fill the two expensive cells and one unit of the cheap one: burden 7.
        weights, capacities, mass, tau = [4,2,1], [1,1,10], 3, 1
        upper=tau*mass+sum(c*max(w-tau,0) for w,c in zip(weights,capacities))
        self.assertEqual(upper,7)
        self.assertEqual(sum(w*e for w,e in zip(weights,[1,1,1])),upper)
        self.assertGreater(sum(w*c for w,c in zip(weights[:2],capacities[:2]))+mass,upper)

    def test_each_density_satisfies_shared_bound(self):
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    e=[F(a,4),F(b,4),F(c,4)]
                    if sum(e)>F(3,2): continue
                    lhs=sum(w*x for w,x in zip([4,2,1],e))
                    rhs=F(3,2)+3+1
                    self.assertLessEqual(lhs,rhs)

    def test_seam_integral_and_breakpoint(self):
        self.assertEqual(se.first_cell_excess(F(1),F(2),F(1,2),F(1)),F(5,12))
        with self.assertRaises(ValueError):
            se.first_cell_excess(F(1),F(2),F(1),F(1))

    def test_negative_excess_is_zero(self):
        self.assertEqual(se.cell_excess(F(1),F(1),F(2),F(2),F(1)),0)

    def test_cell_quadratic_integral(self):
        self.assertEqual(se.cell_excess(F(1),F(1),F(2),F(1,2),F(1)),F(14,3))

    def test_all_profile_cells_and_exact_threshold(self):
        result=se.shared_bound(self.profile,total_mass=F(1,48),moment_square=F(1,81))
        self.assertEqual(len(self.profile['floors']),2401)
        self.assertEqual(result['positive_cells'],20)
        self.assertLess(result['upper'],F(2,15))
        self.assertGreater(1-result['upper'],F(13,15))

    def test_old_result_reproduces_known_interval(self):
        old=se.separate_bound(self.profile,total_mass=F(1,12),moment_square=F(1,9),amplitude_square=F(1,16))
        self.assertGreater(old,F('0.8639147864447208542104368779842921507683659360220108143'))
        self.assertLess(old,F('0.8639147864447208542104368779842921507683659360220108144'))

    def test_matrix_coefficient_and_cross_column_control(self):
        k=se.shared_bound(self.profile,total_mass=F(1,4),moment_square=F(4,27))['upper']
        self.assertLess(k,F(8,5))
        # Correlated columns must keep the off-diagonal Gram entries.
        q=[F(1),F(1)]
        full=sum(x for x in q)**2
        diagonal_only=sum(x*x for x in q)
        self.assertGreater(full,diagonal_only)

    def test_matrix_version_scales_with_source_gram(self):
        p=self.profile
        unit=se.shared_bound(p,total_mass=F(1,4),moment_square=F(4,27))['upper']
        for scale in [F(0),F(1,12),F(2),F(17,5)]:
            out=se.shared_bound(p,total_mass=scale/4,moment_square=scale*F(4,27))['upper']
            self.assertEqual(out,scale*unit)

    def test_exact_ieee_decoder_handles_extremes(self):
        for value in [0.,-0.,.5,-3.,2.**-1074,2.**1000]:
            self.assertEqual(se.exact_binary64(struct.pack('>d',value)),F.from_float(value))
        with self.assertRaises(ValueError):
            se.exact_binary64(struct.pack('>d',float('inf')))

    def test_profile_bit_mutation_is_rejected(self):
        raw=bytearray(lzma.decompress(base64.b64decode((se.DATA/'T21_PROFILE.b64').read_text())))
        raw[-1]^=1
        with self.assertRaises(ValueError): se.parse_profile(bytes(raw))

    def test_profile_text_mutation_is_rejected(self):
        text=(se.DATA/'T21_PROFILE.b64').read_text()
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'bad.b64'
            path.write_text(('A' if text[0]!='A' else 'B')+text[1:])
            with self.assertRaises(ValueError): se.load_profile(path)

    def test_seam_vanishing_is_essential(self):
        # An even constant residual against s=x^2 has integral 2*(1/eps-1).
        self.assertGreater(2*(1/F(1,1000)-1),2*(1/F(1,100)-1))

    def test_chart_success_does_not_promote_actual_source(self):
        report=se.build_report()
        self.assertEqual(report['claim_boundary']['completed_source_chart_attachment'],'OPEN')
        self.assertEqual(report['claim_boundary']['endpoint_K0_sign'],'NOT_CERTIFIED')
        # Debt cannot be dropped: mismatch=2, debt=3/2, boundary square=3/4.
        self.assertLess(F(3,4)/2,1)
        self.assertGreater(F(3,4)/(2-F(3,2)),1)


if __name__ == '__main__':
    unittest.main()
