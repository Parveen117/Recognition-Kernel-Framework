# Singularity Calculus

This folder contains the certified mathematical core extracted from an audited source draft and rebuilt as a theorem-grade Recognition layer.

The raw source was **not** imported as a theorem manuscript. False or unsupported claims were rejected during audit. The retained development is a calculus of piecewise-smooth differential forms, Recognition seams, seam memory, multi-seam composition, transverse junction compatibility, and higher normal-crossing obstruction.

Current theory status:

```text
RNKE_VERIFIED_SINGULARITY_THEORY_V4_WITH_EXCLUSIONS
```

## Development chain

```text
smooth process form
-> bulk curvature d alpha
-> seam-supported distributional curvature
-> tangential jump residue
-> Stokes memory
-> gauge/period memory
-> typed closure
-> finite multi-seam additivity
-> seam-memory cocycle / bulk interaction
-> transverse two-seam compatibility
-> stratified Bianchi junction residue
-> transverse three-seam alternating compatibility
-> codimension-three realizability obstruction.
```

## Certified theorem chain

1. `01_orientation_reversal_no_singularity.md`
   - smooth `(T,V)->(V,T)` has determinant `-1`, not `0`;
   - orientation reversal alone does not create a singular current.

2. `02_process_form_curvature_and_maxwell_defect.md`
   - rejects nonzero `d(d Phi)` for smooth scalar `Phi`;
   - defines lawful process-form curvature `Omega=d alpha`;
   - proves the Maxwell-defect coefficient in the enthalpy chart.

3. `03_distributional_seam_curvature.md`
   - proves the distributional seam-jump curvature formula.

4. `04_tangential_jump_removability_and_gauge.md`
   - seam curvature vanishes exactly when the tangential jump vanishes;
   - coherent side-gauge changes preserve the seam residue.

5. `05_seam_stokes_memory.md`
   - proves the Stokes formula with an explicit seam-memory term;
   - flat bulk can still retain nonzero seam memory.

6. `06_regular_singular_typed_non_cancellation.md`
   - bulk and seam curvature occupy mutually singular measure channels;
   - scalar cancellation is not typed closure.

7. `07_piecewise_enthalpy_seam_law.md`
   - separates smooth Maxwell defects from interface-supported seam curvature.

8. `08_seam_gauge_class_and_period_memory.md`
   - proves the gauge class of the seam residue modulo exact seam forms;
   - closed-cycle seam periods are gauge invariant.

9. `09_master_singularity_closure_theorem.md`
   - proves
     \[
     d\alpha=0
     \iff
     (\Omega_-,\Omega_+,R_\Sigma)=(0,0,0).
     \]

10. `10_finite_multi_seam_additivity_and_closure.md`
    - finite pairwise-disjoint seams contribute additively;
    - multi-seam closure is componentwise.

11. `11_seam_filler_cocycle_and_curvature_interaction.md`
    - proves
      \[
      \delta\omega_\Sigma=-\mathcal B_{\rm associator};
      \]
    - flat bulk gives an MR-03 cocycle;
    - curved bulk produces an explicit typed interaction channel.

12. `12_normal_crossing_no_spurious_double_delta.md`
    - for two transverse seams, mixed-jump routes agree;
    - `d alpha` contains no independent `delta(rho1)delta(rho2)` term;
    - potential codimension-two terms cancel in `d^2 alpha`.

13. `13_stratified_bianchi_junction_residue.md`
    - defines
      \[
      J_{12}=\Delta_1\beta_2-\Delta_2\beta_1;
      \]
    - proves the bulk/seam/junction Bianchi decomposition and componentwise closure law.

14. `14_triple_normal_crossing_alternating_junction.md`
    - for three transverse seams defines
      \[
      T_{123}=\Delta_1J_{23}-\Delta_2J_{13}+\Delta_3J_{12};
      \]
    - proves `T_123=0` for compatible seam-derived junction data.

15. `15_codimension_three_realizability_obstruction.md`
    - proves the no-go implication
      \[
      T_{123}\neq0
      \Rightarrow
      \text{no compatible lower-stratum seam realization};
      \]
    - explicitly does not claim the converse global reconstruction theorem.

## Theory documents

- `VERIFIED_THEORY.md` — SC-01 through SC-09 integrated single-seam theory.
- `VERIFIED_THEORY_MULTI_SEAM_EXTENSION.md` — SC-10/SC-11 multi-seam composition extension.
- `VERIFIED_THEORY_JUNCTION_EXTENSION.md` — SC-12/SC-13 transverse two-seam junction extension.
- `VERIFIED_THEORY_TRIPLE_EXTENSION.md` — SC-14/SC-15 transverse three-seam compatibility extension.

Certificates and status files are versioned rather than silently overwritten:

- `THEORY_CERTIFICATE.json`, `THEORY_STATUS.md`
- `THEORY_CERTIFICATE_V2.json`, `THEORY_STATUS_V2.md`
- `THEORY_CERTIFICATE_V3.json`, `THEORY_STATUS_V3.md`
- `THEORY_CERTIFICATE_V4.json`, `THEORY_STATUS_V4.md`

## Central typed packets

Single seam:

\[
\boxed{
\mathfrak C_{\rm sing}=(\Omega_-,\Omega_+,R_\Sigma).
}
\]

Finite disjoint seams:

\[
\boxed{
\mathfrak C_{\rm multi}
=(\Omega_0,\ldots,\Omega_m;R_1,\ldots,R_m).
}
\]

Transverse two-seam Bianchi hierarchy:

\[
\boxed{
\mathfrak B_{\rm strat}
=(d\Omega_{\rm bulk};B_1,B_2;J_{12}).
}
\]

Transverse triple-junction compatibility:

\[
\boxed{
\mathfrak J_3=(J_{12},J_{13},J_{23};T_{123}).
}
\]

These packets have different semantics. Pairwise junction closure, triple compatibility, path-composition cocycle closure, and bulk curvature closure are not interchangeable scalar tests.

## Interface to the Recognition Framework

This folder complements rather than replaces:

- `theorum/24_clock_free_recognition_seam_cut_calculus.md` for clock-free transition calculus;
- `theorum/morphic_recognition/` for typed non-cancellation, blindness, and MR-03 cocycle memory;
- `theorum/recognition_topology/` for winding, holonomy, branch memory, and topological seam events;
- `theorum/thermodynamics/02_curvature_to_seam_spectral_flow.md` for the operator threshold interface once an operator representation is supplied.

Important separations remain:

```text
singular seam current != automatic topological transition
junction residue       != automatic physical defect
T_123 obstruction      != automatic microscopic event
curvature threshold    != automatic winding jump
```

A domain adapter must prove any such identification.

## Current verification

The v4 theorem/proof head is:

```text
e392b4ae69aa3b058ec88ff66bc7635857922e0b
```

Verification:

```text
legacy suite 19/19 PASS
triple suite 4/4 PASS
combined 23/23 PASS
legacy exact controls 18 PASS
triple exact controls 3 PASS
combined exact controls 21 PASS
Python 3.11 PASS
Python 3.12 PASS
GitHub Actions run 31260404317 PASS
```

The first v4 candidate run failed only because two expected calibration values used stale table-index ordering. The theorem formula and alternating sign were unchanged; the corrected exact values then passed both Python versions. This audit is retained in `THEORY_CERTIFICATE_V4.json`.

## Claim boundary

```text
SMOOTH ORIENTATION REVERSAL AS SINGULARITY             REJECTED
NONZERO d(d Phi) FOR SMOOTH Phi                        REJECTED
PROCESS-FORM / DISTRIBUTIONAL SEAM CURVATURE            PROVED
GAUGE-PERIOD SEAM MEMORY                                PROVED
SINGLE-SEAM MASTER CLOSURE                              PROVED
FINITE DISJOINT MULTI-SEAM ADDITIVITY                   PROVED
FLAT-BULK SEAM MEMORY AS MR-03 COCYCLE                  PROVED
CURVED-BULK ASSOCIATOR INTERACTION                      PROVED
NO SPURIOUS DOUBLE-DELTA TERM IN d alpha                PROVED
TRANSVERSE TWO-SEAM JUNCTION BIANCHI LAW                PROVED
TRANSVERSE THREE-SEAM T_123 COMPATIBILITY               PROVED
T_123 != 0 REALIZABILITY OBSTRUCTION                    PROVED

T_123 = 0 => GLOBAL RECONSTRUCTION                      NOT CLAIMED
NONTRANSVERSE JUNCTIONS                                 OPEN
QUADRUPLE / GENERAL HIGHER NORMAL-CROSSING HIERARCHY    OPEN
GLOBAL POTENTIAL RECONSTRUCTION FROM CLOSED DATA        OPEN
AUTOMATIC TOPOLOGICAL / MICROSCOPIC IDENTIFICATION      NOT CLAIMED
ATOMIC / PERIODIC-TABLE / CHEMICAL-BOND CLAIMS          NOT PROMOTED
DEVICE PERFORMANCE CLAIMS                               NOT PROMOTED
```
