# Primitive Flux Witnesses, Restricted Minimizers, and Canonicality Obstruction

## Provenance

```text
source repository: Parveen117/MP
source PRs: #59, #60, #61
source theorems:
  adapters/common/PRIMITIVE_FLUX_SPECTRUM.md
  adapters/common/PRIMITIVE_FLUX_MINIMIZER_CLASSIFICATION.md
  adapters/common/PRIMITIVE_FLUX_STRIP_VARIATION.md
```

## 1. Integer lifted-flux witness theorem

Fix a compact-strip rectangular witness block carrying lifted flux \(2\pi/q_0\), with \(q_0=14\) in the source calibration. For each nonzero integer \(n\), take \(q_0|n|\) oriented laps and assign fresh hierarchy depths so that the complete hierarchy state returns only at the endpoint.

Then the resulting sector satisfies

\[
\boxed{\Phi_n=2\pi n,}
\]

while

```text
principal holonomy = identity
visible winding = 0
visible memory = empty
composition-primitive = true.
```

Thus principal holonomy collapses the integer classes modulo \(2\pi\), whereas lifted curvature memory distinguishes them.

The witness family obeys the linear and quadratic no-collapse inequalities. Within every finite audited integer range, the witness lengths form a discrete set, and same-orientation witness composition is additive.

## 2. Restricted rectangular minimizer theorem

Fix endpoints

\[
(x_0,x_1)=(0.5,3.0)
\]

and consider congruent rectangular multi-lap representatives with half-width \(\eta<1/2\). Put

\[
D=A'(x_0)-A'(x_1)>0.
\]

For lifted flux \(\Phi_n=2\pi n\), the least admissible lap count in this restricted family is

\[
\boxed{
q_{\min}(n)=\left\lfloor\frac{2\pi|n|}{D}\right\rfloor+1.
}
\]

The corresponding half-width is

\[
\boxed{
\eta(n)=\frac{\pi|n|}{q_{\min}(n)D},
}
\]

and the restricted minimum length is

\[
\boxed{
L_{\min}^{\mathrm{rect}}(n)
=2q_{\min}(n)(x_1-x_0)
+\frac{2\pi|n|\bigl(A(x_0)+A(x_1)\bigr)}{D}.
}
\]

The floor-plus-one is forced by the strict regular-strip constraint \(\eta<1/2\). The preceding lap count is inadmissible.

This theorem classifies only the fixed-endpoint congruent-rectangle family.

## 3. Endpoint-variation obstruction theorem

The fixed rectangle is not stable under endpoint variation. For the source's \(n=1\) calibration,

```text
fixed endpoints (0.5, 3.0):
  length ≈ 74.3656751841

admissible varied endpoints (0.35, 1.125):
  q_min = 24
  η ≈ 0.4987180752
  length ≈ 47.8830145962.
```

Hence an admissible shorter representative exists. Therefore

\[
\boxed{
L_{\min}^{\mathrm{rect}}\text{ at the original fixed endpoints is not a canonical native normalization}.
}
\]

This negative theorem is load-bearing: a restricted minimizer formula cannot be promoted into an arithmetic length merely because it is explicit and visually well behaved.

## 4. What survives the obstruction

The endpoint-variation result does not invalidate:

- lifted flux as protected memory;
- composition-primitivity of the hierarchy-resolved witnesses;
- the no-collapse inequalities;
- the fixed-family minimizer formula within its declared class;
- finite-window discreteness diagnostics.

It blocks only the unsupported step from one convenient rectangle to a canonical global normalization.

## Claim boundary

```text
INTEGER LIFTED-FLUX WITNESSES             PROVED
IDENTITY PRINCIPAL HOLONOMY               PROVED FOR WITNESS FAMILY
HIERARCHY-RESOLVED PRIMITIVITY            PROVED IN DECLARED CATEGORY
FINITE-RANGE WITNESS DISCRETENESS         PROVED / AUDITED
FIXED-ENDPOINT RECTANGULAR MINIMIZER      PROVED IN RESTRICTED FAMILY
FIXED RECTANGLE CANONICALITY              DISPROVED BY SHORTER COMPETITOR

GLOBAL SHAPE MINIMIZER                    OPEN
GLOBAL FLUX-SPECTRUM DISCRETENESS         OPEN
CANONICAL ARITHMETIC NORMALIZATION        NOT PROVED
NATIVE LENGTH = log p                     NOT PROVED
```
