# Singularity Calculus

This folder contains the audited and theorem-grade Singularity Calculus layer of
the Recognition Kernel Framework.

The raw source draft was not imported wholesale. False or unsupported claims were
rejected. The surviving mathematics has been rebuilt as a piecewise-smooth,
distributional, and normal-crossing calculus with explicit claim boundaries and
machine-checkable exact controls.

Current status:

```text
RNKE_VERIFIED_SINGULARITY_THEORY_V5_WITH_EXCLUSIONS
```

## Development chain

```text
smooth process form
-> bulk curvature
-> seam-supported distributional curvature
-> tangential seam residue
-> Stokes and gauge-period memory
-> typed single-seam closure
-> finite multi-seam additivity
-> seam-memory cocycle / bulk associator interaction
-> transverse two-seam junction Bianchi law
-> transverse three-seam alternating compatibility
-> general finite normal-crossing jump complex D_Delta^2=0
-> total stratified differential mathbb D^2=0
-> general realizability/cohomology obstruction.
```

## Certified theorem chain

1. `01_orientation_reversal_no_singularity.md` — smooth orientation reversal is
   not a rank singularity.
2. `02_process_form_curvature_and_maxwell_defect.md` — lawful process-form
   curvature and Maxwell defect.
3. `03_distributional_seam_curvature.md` — seam-supported distributional
   curvature.
4. `04_tangential_jump_removability_and_gauge.md` — removable seam criterion and
   coherent-gauge law.
5. `05_seam_stokes_memory.md` — exact Stokes memory with seam contribution.
6. `06_regular_singular_typed_non_cancellation.md` — bulk and seam channels do
   not scalar-cancel.
7. `07_piecewise_enthalpy_seam_law.md` — thermodynamic specialization.
8. `08_seam_gauge_class_and_period_memory.md` — gauge class and closed-period
   memory.
9. `09_master_singularity_closure_theorem.md` — complete single-seam closure.
10. `10_finite_multi_seam_additivity_and_closure.md` — disjoint multi-seam
    additivity and componentwise closure.
11. `11_seam_filler_cocycle_and_curvature_interaction.md` — seam-memory cocycle
    in flat bulk and explicit curvature interaction otherwise.
12. `12_normal_crossing_no_spurious_double_delta.md` — two-seam mixed-jump
    compatibility and no spurious double-delta term in first curvature.
13. `13_stratified_bianchi_junction_residue.md` — pairwise junction Bianchi
    residue.
14. `14_triple_normal_crossing_alternating_junction.md` — triple alternating
    compatibility residue.
15. `15_codimension_three_realizability_obstruction.md` — nonzero triple residue
    forbids compatible lower-stratum realization.
16. `16_general_normal_crossing_jump_complex.md` — defines the general
    normal-crossing cochain complex and proves
    \[
    \boxed{D_\Delta^2=0.}
    \]
17. `17_total_stratified_differential.md` — defines
    \[
    \boxed{\mathbb D=d+(-1)^pD_\Delta}
    \]
    and proves \(\mathbb D^2=0\) under the declared commutation laws.
18. `18_general_realizability_obstruction_and_cohomology.md` — proves the general
    fail-closed realizability gate and defines jump/total cohomology.

## Theory documents

- `VERIFIED_THEORY.md` — SC-01 through SC-09.
- `VERIFIED_THEORY_MULTI_SEAM_EXTENSION.md` — SC-10/SC-11.
- `VERIFIED_THEORY_JUNCTION_EXTENSION.md` — SC-12/SC-13.
- `VERIFIED_THEORY_TRIPLE_EXTENSION.md` — SC-14/SC-15.
- `VERIFIED_THEORY_GENERAL_COMPLEX_EXTENSION.md` — SC-16/SC-18 and the v5
  general normal-crossing closure.

Certificates remain versioned:

- `THEORY_CERTIFICATE.json`
- `THEORY_CERTIFICATE_V2.json`
- `THEORY_CERTIFICATE_V3.json`
- `THEORY_CERTIFICATE_V4.json`
- `THEORY_CERTIFICATE_V5.json`

## General normal-crossing complex

For the finite seam index set \(N=\{1,\ldots,n\}\), let

\[
C^k_\Delta=\bigoplus_{|I|=k}A_I.
\]

The alternating jump differential is

\[
\boxed{
(D_\Delta c)_I
=
\sum_r(-1)^r\Delta_{i_r}c_{I\setminus\{i_r\}}.
}
\]

Commuting normal-crossing jump squares imply

\[
\boxed{D_\Delta^2=0.}
\]

Thus the earlier pairwise and triple formulas are low-degree instances of one
finite complex rather than separate rules.

## Total stratified differential

For a differential-graded coefficient system \(B_I^p\), assume

\[
d^2=0,
\qquad D_\Delta^2=0,
\qquad dD_\Delta=D_\Delta d.
\]

Then

\[
\boxed{
\mathbb D=d+(-1)^pD_\Delta,
\qquad
\mathbb D^2=0.
}
\]

This combines within-stratum and between-stratum closure without collapsing their
types.

## General realizability gate

If a declared packet \(c\) is claimed to be generated from lower-stratum data,
then

\[
c=D_\Delta b
\]

requires

\[
\boxed{D_\Delta c=0.}
\]

Therefore

\[
\boxed{
D_\Delta c\neq0
\Rightarrow
\text{no compatible lower-stratum realization}.
}
\]

Passing this gate is not enough for global exactness. Closed-but-nonexact packets
are measured by

\[
H^k_\Delta=\ker D_\Delta/\operatorname{im}D_\Delta.
\]

## Verification

Validated v5 theorem/proof head:

```text
6e113dec673920a9c201041542e125d26777025f
```

GitHub Actions run:

```text
31262484822
```

Results:

```text
SC-01..SC-15 legacy tests       23/23 PASS
SC-16..SC-18 general tests       7/7 PASS
combined                         30/30 PASS
combined exact controls             27 PASS
D_Delta^2 cases n=2..8              28 PASS
Python 3.11                        PASS
Python 3.12                        PASS
```

Negative controls detect missing alternating signs, wrong total-complex signs,
and corrupted derived packets.

## Vertical freeze

The finite transverse normal-crossing hierarchy is now structurally complete at
the abstract level. SC-16 subsumes manual codimension-four, codimension-five, and
higher formulas.

Future Singularity Calculus work should require genuinely new assumptions or
phenomena, such as nontransverse strata, infinite/accumulating seams, analytic
convergence, or a concrete physical/operator adapter.

## Interface to the Recognition Framework

This layer complements:

- `theorum/24_clock_free_recognition_seam_cut_calculus.md`;
- `theorum/morphic_recognition/`;
- `theorum/recognition_topology/`;
- `theorum/thermodynamics/02_curvature_to_seam_spectral_flow.md`.

The next useful development is integration: a general **Stratified Recognition
Faithfulness Theorem** saying that any observer/representation must preserve every
target-relevant obstruction channel across path, bulk, seam, junction, and higher
strata.

## Claim boundary

```text
FINITE TRANSVERSE NORMAL-CROSSING COMPLEX             PROVED
D_DELTA^2 = 0                                         PROVED
TOTAL STRATIFIED DIFFERENTIAL mathbb D^2 = 0          PROVED UNDER DECLARED COMMUTATION
GENERAL NONREALIZABILITY GATE                         PROVED
JUMP / TOTAL COHOMOLOGY                               DEFINED
ACYCLICITY                                             NOT CLAIMED
GLOBAL POTENTIAL RECONSTRUCTION                       NOT CLAIMED
NONTRANSVERSE JUNCTION THEORY                         OPEN
INFINITE / ACCUMULATING SEAM FAMILIES                 OPEN
AUTOMATIC TOPOLOGICAL OR PHYSICAL IDENTIFICATION      NOT CLAIMED
ATOMIC / CHEMICAL / DEVICE CLAIMS                     NOT PROMOTED
```
