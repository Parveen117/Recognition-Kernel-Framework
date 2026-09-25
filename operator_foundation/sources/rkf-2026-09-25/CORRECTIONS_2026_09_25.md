# Mathematical corrections, 2026-09-25

Base revision: 86198d29cbf30390059079f38675c952e506ea9c.

- T50: tensor cut-tail mass is bounded by the product; repeated mixed entries
  strictly refute equality. Positive floors and 0<=rho<1 are explicit and
  enforced. The general uniform energy proof survives the corrected inequality.
- T54: memory increment upper bound; equality is scoped to pure-axis fixtures.
- Morphic Algebra / Calculus: successive-prefix cocycle formula with telescoping
  proof; Euler quadratic defects, area-scaled loop limit, all-mode torus
  obstruction, relative-entropy clock and spectral assumptions corrected.
- Morphic Geometry: abstract matches admitted-diamond flatness, without a converse.
- F00-I: the first Taylor majorant has exponent 1+2 delta before absorbing n^|h|.
- Lambda geometry 10: phase-path index replaces spectral flow of the instantaneous
  generator. The winding orientation is explicit here and in RT-04.

Written proofs are in the corrected sources. Finite regression evidence is in
proof_lab/test_correction_regressions.py and the refreshed T50/T54/ladder
certificates. The finite evidence is not a universal or Lean proof. Historical
source_original.tex files are preserved. Existing open manuscript claims, RH,
K0, Yang--Mills mass gap and physical identifications are not promoted.

The Publications correction record supplies the SPECTRAL 2 zero-extension
erratum, information-observer scope correction and thermodynamic measurement
contract. RH-Framework contains the parallel scalar-tail completion repair.

Reproduce:

    python -m unittest proof_lab.test_mathematics_index -v
    python -m unittest proof_lab.test_correction_regressions -v
    python -m unittest proof_lab.test_native_seam_gap_odd_covariance -v
    python -m unittest proof_lab.test_infinite_face_recognition_completion -v
    python -m unittest proof_lab.test_ladder_audit_50_59 -v

PUBLIC_IMPORT_REPORT.json remains a historical import record. Current theorem
identity is given by the refreshed package source pins and correction manifest.
