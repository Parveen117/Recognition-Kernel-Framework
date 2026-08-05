# Thermodynamic-Lambda Geometry Source Provenance

## Repository lineage

```text
source repository: Parveen117/MP
source PR range: #52 through #61
transfer repository: Parveen117/Recognition-Kernel-Framework
transfer folder: theorum/thermodynamics/lambda_geometry/
```

## Source theorem map

```text
PR #52
adapters/common/LAMBDA_HOLONOMY_SPECTRAL_OPERATOR.md
-> 10_lambda_holonomy_and_branch_memory.md

PR #53
adapters/common/NONCOMMUTATIVE_PATH_ORDERED_HOLONOMY.md
-> 11_noncommutative_holonomy_and_irreducibility.md

PR #54
adapters/common/ADMISSIBLE_SECTOR_FACTORIZATION.md
-> 12_admissible_factorization_and_primitivity.md

PR #55
adapters/common/REFINEMENT_INVARIANT_NATIVE_LENGTH.md
-> 13_refinement_and_continuum_length.md

PR #56
adapters/common/CONTINUUM_HOMOTOPY_DESCENT.md
-> 13_refinement_and_continuum_length.md

PR #57
adapters/common/CONSTRAINED_HOMOTOPY_GROUPOID.md
-> 14_constrained_variational_length.md

PR #58
adapters/common/CUT_METRIC_NO_COLLAPSE.md
-> 15_curvature_flux_no_collapse.md

PR #59
adapters/common/PRIMITIVE_FLUX_SPECTRUM.md
-> 16_primitive_flux_spectrum_and_obstruction.md

PR #60
adapters/common/PRIMITIVE_FLUX_MINIMIZER_CLASSIFICATION.md
-> 16_primitive_flux_spectrum_and_obstruction.md

PR #61
adapters/common/PRIMITIVE_FLUX_STRIP_VARIATION.md
-> 16_primitive_flux_spectrum_and_obstruction.md
```

## Nonduplication rule

The parent thermodynamics archive already transfers the direct PR #239/#243 theorem families:

```text
response tetrad and flat closure
curvature-to-seam spectral flow
canonical response cost / barrier
projection defect and source overlap
Onsager compass and Hodge no-leakage
thermo-Weil provenance and Schur realization
canonical physical flux.
```

Those results are not copied into this subfolder. This folder contains only the earlier missing lambda-holonomy, length, variational, and curvature-flux lineage.

## Typing repair

PR #52 used historical derivative coordinates in the \(s,t\) directions. PR #239 later separated them from the uniform entropy-scaled thermodynamic coordinates

\[
\lambda_X^{\mathrm{th}}=-ST/C_X.
\]

The transfer preserves the geometric theorems from PRs #52–#61 while treating the PR #239 convention as authoritative for thermodynamic typing.

## Transfer discipline

Each capsule retains:

1. typed definitions;
2. theorem statements and supported proofs;
3. exact hypotheses;
4. negative controls and obstruction theorems;
5. explicit open boundaries.

No arithmetic-prime identification, universal absolute length scale, global flux-spectrum classification, or RH conclusion is promoted by this transfer.
