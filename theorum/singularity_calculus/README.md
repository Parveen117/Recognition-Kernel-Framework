# Singularity Calculus

This folder contains the certified mathematical core extracted from an audited source draft and then rebuilt as a theorem-grade Recognition layer.

The raw source was **not** imported as a theorem manuscript. False or unsupported claims were rejected during audit. The retained development is a calculus of piecewise-smooth differential forms, Recognition seams, seam memory, multi-seam composition, and transverse junction compatibility.

Current theory status:

```text
RNKE_VERIFIED_SINGULARITY_THEORY_V3_WITH_EXCLUSIONS
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
-> transverse normal-crossing compatibility
-> stratified Bianchi junction residue.
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
   - proves
     \[
     d\alpha=(1-H)d\alpha_-+Hd\alpha_+
     +\delta(\rho)d\rho\wedge(\alpha_+-\alpha_-).
     \]

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
   - proves the gauge class
     \[
     [R_\Sigma]\in\Omega^1(\Sigma)/d_\Sigma\Omega^0(\Sigma);
     \]
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
    - seam filler memory has cocycle defect
      \[
      \delta\omega_\Sigma=-\mathcal B_{\rm associator};
      \]
    - flat bulk gives an MR-03 cocycle;
    - curved bulk produces an explicit typed interaction channel.

12. `12_normal_crossing_no_spurious_double_delta.md`
    - for two transverse seams, the two mixed-jump routes agree;
    - `d alpha` contains no independent `delta(rho1)delta(rho2)` term;
    - potential codimension-two terms cancel in `d^2 alpha`.

13. `13_stratified_bianchi_junction_residue.md`
    - for independently declared stratified curvature data, defines
      \[
      J_{12}=\Delta_1\beta_2-\Delta_2\beta_1;
      \]
    - proves the bulk/seam/junction Bianchi decomposition and componentwise closure law.

## Theory documents

- `VERIFIED_THEORY.md` — SC-01 through SC-09 integrated single-seam theory.
- `VERIFIED_THEORY_MULTI_SEAM_EXTENSION.md` — SC-10/SC-11 multi-seam composition extension.
- `VERIFIED_THEORY_JUNCTION_EXTENSION.md` — SC-12/SC-13 transverse junction extension.

Certificates and status files are versioned rather than silently overwritten:

- `THEORY_CERTIFICATE.json`, `THEORY_STATUS.md`
- `THEORY_CERTIFICATE_V2.json`, `THEORY_STATUS_V2.md`
- `THEORY_CERTIFICATE_V3.json`, `THEORY_STATUS_V3.md`

## Central closure packets

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

Each packet closes only componentwise.

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
curvature threshold    != automatic winding jump
```

A domain adapter must prove any such identification.

## Current verification

The SC-12/SC-13 theorem head passed:

```text
19/19 unit tests
18 exact calibration controls
Python 3.11
Python 3.12
GitHub Actions run 31259516097
```

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

NONTRANSVERSE JUNCTIONS                                 OPEN
TRIPLE/HIGHER NORMAL-CROSSING JUNCTION HIERARCHY        OPEN
GLOBAL POTENTIAL RECONSTRUCTION FROM CLOSED DATA        OPEN
AUTOMATIC TOPOLOGICAL / MICROSCOPIC IDENTIFICATION      NOT CLAIMED
ATOMIC / PERIODIC-TABLE / CHEMICAL-BOND CLAIMS          NOT PROMOTED
DEVICE PERFORMANCE CLAIMS                               NOT PROMOTED
```
