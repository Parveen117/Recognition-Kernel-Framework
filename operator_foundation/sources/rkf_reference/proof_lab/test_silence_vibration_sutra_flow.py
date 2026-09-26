from __future__ import annotations

import hashlib
import unittest
from fractions import Fraction
from pathlib import Path

from proof_lab.generalized_euler_emk_dock import I2, R
from proof_lab.loop_residue_first_visible_jet_binding import j_add
from proof_lab.native_seam_gap_odd_covariance import m_scale
from proof_lab.silence_vibration_sutra_flow import build_certificate, canonical_bytes, certificate_sha256, cos_sin_jets, exp_jet_matrix, scalar_jet_times

EXPECTED = Path(__file__).with_name("SILENCE_VIBRATION_SUTRA_FLOW_EXPECTED.sha256")


class SilenceVibrationSutraFlowTests(unittest.TestCase):
    def test_no_hilbert_verdict(self) -> None:
        src = Path(__file__).with_name("silence_vibration_sutra_flow.py").read_text(encoding="utf-8")
        for forbidden in ("numpy", "eigval", "cholesky", "math.cos", "math.sin", "float("):
            self.assertNotIn(forbidden, src)

    def test_circular_system_jets(self) -> None:
        w = Fraction(3)
        D = m_scale(w, R)
        cos, sin = cos_sin_jets(w)
        self.assertEqual(exp_jet_matrix(D), j_add(scalar_jet_times(cos, I2), scalar_jet_times(sin, m_scale(Fraction(1) / w, D))))
        self.assertEqual(cos[2], -w * w / 2)
        self.assertEqual(sin[3], -w**3 / 6)

    def test_certificate_pin(self) -> None:
        payload = build_certificate()
        self.assertEqual(payload["status"], "PASS_SILENCE_VIBRATION_SUTRA_FLOW_CANDIDATE")
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        self.assertEqual(digest, certificate_sha256(payload))
        self.assertEqual(digest, EXPECTED.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
