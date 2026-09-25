# Ladder audit 74–75 (Aug 23 2026)

Same discipline as `AUDIT_LADDER_50_59.md`: hunt for controls that cannot
fail, tampers that do not bite, and narration that does not match
arithmetic. Both certificates were re-pinned after the fixes; both still
PASS, now with controls that can genuinely fail.

## Defects found and fixed

1. **theorum/74 C3 refusal control was VACUOUS.** It tested the identity
   pencil, whose doubled ceiling is exactly 1, so `not (1 < 1)` was true
   no matter what the code did. Replaced by a pencil with a heavy
   complement (weight 5 against θ = 1): σ ≥ θ is required, so a broken
   ceiling routine would report contraction and fail the control.

2. **theorum/75 C1 planted-wrong test was VACUOUS.** The planted claim was
   ten times *stronger* than the true ratio, so its condition could never
   fire. Replaced by a DISCRIMINATION test: the claimed bound
   κ/(2(2c+2)) must hold and the next sharper claim κ/(2(2c+3)) must
   FAIL. Finding: the proved ladder law is **sharp to 0.07 %**
   (ratio/bound = 0.99935 at c = 0, κ = 1/8) — a tight law, not a loose
   majorant.

3. **theorum/75 tryambaka mass/energy budget was too coarse to fail.**
   DOWNGRADED honestly to a printed diagnostic. The load-bearing verdicts
   of a release step are now stated to be the seam-count equality and its
   tamper (below), not the budget.

4. **theorum/75 retention clause had no biting tamper.** Added: killing
   the lopa ladder (flat faces f_c = f₀) must make the counts DIFFER.
   It does, decisively — 3 vs 11 and 6 vs 19 at every grid κ. This
   promotes "release preserves the seam count" from a coincidence on one
   instance to a verdict that demonstrably depends on the ladder: the
   mṛtyu clause is load-bearing.

5. **Double-import bug in the new tamper (caught by the audit itself).**
   Written first as `import proof_lab.selective_release as _self` and
   patched there; run as `__main__` that import yields a SECOND module
   object, so the tamper patched a copy and silently did not bite — the
   certificate reported FAIL, which is how it was found. Fixed by
   patching the module's own `globals()`. Rule recorded: a tamper must be
   verified to change the outcome, never assumed to.

## Not changed
theorum/74 T1/T2/T4 and theorum/75 T1/T2/T3-counts/T4 survived untouched.
The declared components are unchanged and still declared: the Haar ↔ Φ_Σ
identification (RH T01-E5C/E6) and, in theorum/75 T4, the Gram-uniformity
of content levels > 2 entering through theorum/28 §4.

## Status
theorum/74, theorum/75: certificates PASS, controls non-vacuous, names
still CANDIDATE pending the owner's own audit.

## STANDING CORRECTION (owner's provenance challenge, same day)

**Found after the audit, by the owner asking "did you audit with classical
tools?".** The audit's method was mutation testing (can a control fail?) —
engineering, importing nothing. But it checked CONTROLS, not PROVENANCE,
and it therefore missed a classical import in the audited object itself:

- `proof_lab/selective_release.py::laplace_nullspace` defines the content
  grading as the **nullspace of the classical Laplace operator**;
  `rail_harmonic_setup` / `rail_cinv` use it to build **B**. It is
  load-bearing for every seam count and every beta in theorum/75.
- This is classical harmonic analysis on the sphere — the Peter-Weyl side
  of the declared Haar <-> Phi_Sigma shadow, but a NEW classical
  ingredient that was not named in the ledger. theorum/74 avoided it only
  because its degree <= 2 grading was written out by hand.
- STATUS of theorum/75: T1 (ladder law), T2 (stationarity) and the
  tamper results are unaffected — they do not pass through `rail_cinv`.
  T3's counts and T4's outward certificate are **ANCHORED** pending the
  native regrading (YM-19 / YM-37 precedent).
- NAMED FIX (next capsule): define the grading by the framework's own
  character ladder — the native three-term recurrence
  `chi_{c+1/2} = u chi_c - chi_{c-1/2}` (already present in the file as
  `chi_of_u`) together with the fusion coefficients (YM-30 CG machinery,
  RST-2 squared-amplitude discipline). Expected: identical rationals;
  any discrepancy is itself the finding.
- **RESOLVED same day**: grading regraded natively (`rail_cinv_native`:
  character ladder + convolution; projector laws certified as exact
  rational identities on the carrier; Laplacian route demoted to an
  independent cross-check control, reproducing identical rationals on
  every monomial). T75 T3/T4 restored to PROVED; certificate re-pinned
  with C5 extended (`C5_moments_native_grading_certified_and_laplacian_crosscheck`).
- LESSON RECORDED: an audit must include a provenance pass —
  "which imported operator defines this object?" — not only a control
  pass. Vacuous controls and borrowed definitions are different defects
  and need different sweeps.
