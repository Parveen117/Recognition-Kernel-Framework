# Thermodynamic-Lambda Geometry Archive

This subarchive records the earlier theorem chain developed in `Parveen117/MP` PRs #52 through #61.

It begins with a thermodynamic response hierarchy, then studies the additional geometry required to turn that hierarchy into a connection, holonomy, memory-preserving length, constrained path space, and curvature-flux no-collapse theory.

## Typing warning

PR #52 used the historical first-layer coordinates

\[
\lambda_p=-ST/C_p,
\qquad
\lambda_v=-ST/C_v,
\]

\[
\lambda_s=V(\partial P/\partial V)_S,
\qquad
\lambda_t=-P(\partial V/\partial P)_T.
\]

PR #239 later corrected the physical typing by distinguishing those derivative coordinates from the uniform entropy-scaled response tetrad

\[
\lambda_X^{\mathrm{th}}=-ST/C_X,
\qquad X\in\{p,v,s,t\}.
\]

Therefore the files in this subfolder preserve the geometric theorems from PRs #52–#61 without silently identifying the historical \(s,t\) derivative coordinates with the later entropy-scaled tetrad.

## Reading order

1. `10_lambda_holonomy_and_branch_memory.md`
2. `11_noncommutative_holonomy_and_factorization.md`
3. `12_refinement_and_continuum_length.md`
4. `13_constrained_variational_length.md`
5. `14_curvature_flux_no_collapse.md`
6. `15_primitive_flux_spectrum_and_obstruction.md`

## Status

```text
THERMODYNAMIC FIRST RESPONSE LAYER              HISTORICAL PROVENANCE
CONNECTION FROM RESPONSE HIERARCHY              ADDITIONAL DATA / NOT UNIQUE
UNITARY HOLONOMY-RATE OPERATOR                  PROVED
STATIC LOGARITHM BRANCH MEMORY                  PROVED
NONCOMMUTATIVE PATH-ORDER COLLISION             PROVED
ADMISSIBLE FACTORIZATION WITH CROSS CURVATURE   PROVED
REFINEMENT-STABLE LENGTH RIGIDITY                PROVED
CONTINUUM AND REPARAMETERIZATION DESCENT         PROVED
UNRESTRICTED HOMOTOPY INVARIANCE                DISPROVED
CONSTRAINED VARIATIONAL LOWER BOUND             PROVED
CURVATURE-FLUX NO-COLLAPSE                      PROVED ON COMPACT STRIPS
INTEGER FLUX WITNESS FAMILY                     PROVED
FIXED-RECTANGLE CANONICALITY                     DISPROVED
```
