# Curvature-Flux No-Collapse and Minimizer Existence

## Provenance

```text
source repository: Parveen117/MP
source PR: #58
source theorem: adapters/common/CUT_METRIC_NO_COLLAPSE.md
```

## 1. Corrected warped metric

The source audit corrected the proposed angular coefficient by treating it as the square of a warping amplitude:

\[
g=\frac{dr^2}{r}+a(r)^2\cos^2(2\phi)\,d\phi^2,
\]

with

\[
-2ra''-a'=\frac{a}{\sqrt r}.
\]

Under

\[
x=2\sqrt r,
\qquad
y=\frac{\sin(2\phi)}2,
\qquad
A(x)=a(x^2/4),
\]

the metric becomes

\[
\boxed{g=dx^2+A(x)^2dy^2.}
\]

The corrected ODE is

\[
A''+\frac{A}{x}=0,
\]

so the Gaussian curvature is

\[
\boxed{K=-\frac{A''}{A}=\frac1x=\frac1{2\sqrt r}.}
\]

The regular normalized solution used in the source is

\[
A(x)=\frac12\sqrt x\,J_1(2\sqrt x),
\]

restricted to compact strips where \(A>0\).

## 2. Seam-geodesy theorem

The involution

\[
J(x,y)=(x,-y)
\]

has fixed seam \(y=0\). For the warped metric,

\[
\Gamma^y_{xx}=0,
\]

so the fixed seam is a geodesic without inserting an auxiliary metric-choice assumption.

## 3. Connection and lifted curvature memory

With orthonormal coframe

\[
e^1=dx,
\qquad
e^2=A(x)dy,
\]

the rotation connection and curvature are

\[
\omega=-A'(x)dy,
\]

\[
\Omega=d\omega=\frac{A(x)}x\,dx\wedge dy=K\,d\operatorname{Area}_g.
\]

For a loop \(C=\partial S\), define the lifted memory

\[
\Phi(C)=\int_C\omega=\int_S\Omega.
\]

Principal \(SO(2)\) holonomy retains only \(e^{i\Phi}\); the recognition ledger retains the real lifted value \(\Phi\).

## 4. Completed constrained-path minimizer theorem

On a compact regular strip, consider based constant-speed Lipschitz loops with fixed discrete hierarchy ledger and fixed lifted curvature flux.

For a bounded-length minimizing sequence:

- constant-speed parameterization gives equi-Lipschitz control;
- compactness gives a uniformly convergent subsequence;
- derivatives are weak-star compact;
- smoothness of \(\omega\) closes the line-integral constraint;
- Riemannian length is lower semicontinuous.

Therefore the constrained length infimum is attained in the completed compact-strip class.

## 5. Linear no-collapse theorem

Let

\[
B_D=\max_D\frac{|A'|}{A}.
\]

Every rectifiable loop in the strip satisfies

\[
\boxed{L_g(C)\ge\frac{|\Phi(C)|}{B_D}.}
\]

This follows directly from

\[
|\Phi(C)|=\left|\int_C\omega\right|
\le B_D L_g(C).
\]

## 6. Quadratic no-collapse theorem

For a positively oriented simple loop, metric comparison and the Euclidean isoperimetric inequality give

\[
\boxed{
L_g(C)^2
\ge
\frac{4\pi c_D^2x_0}{M}|\Phi(C)|,
}
\]

where

\[
M=\max_D A,
\qquad
c_D=\min(1,\min_D A).
\]

Thus nonzero lifted curvature flux enforces positive geometric length even when principal holonomy is trivial.

## 7. Identity-holonomy primitive witness

The source constructs a hierarchy-resolved loop with

```text
lifted curvature flux = 2π
principal holonomy = identity
visible winding = 0
visible memory = empty
complete hierarchy return only at the endpoint.
```

It is composition-primitive in the declared hierarchy category and obeys both no-collapse bounds. This demonstrates that endpoint closure does not erase lifted curvature memory.

## Claim boundary

```text
CORRECTED WARPED METRIC AND CURVATURE      PROVED
FIXED SEAM GEODESY                        PROVED
STOKES LIFTED CURVATURE MEMORY            PROVED
COMPACT-STRIP MINIMIZER EXISTENCE         PROVED
LINEAR CURVATURE-FLUX NO-COLLAPSE         PROVED
QUADRATIC SIMPLE-LOOP NO-COLLAPSE         PROVED
IDENTITY-HOLONOMY NONCOLLAPSE WITNESS     PROVED

GLOBAL EXTENSION THROUGH DEGENERACIES     OPEN
GLOBAL MINIMIZER CLASSIFICATION           OPEN
CANONICAL ABSOLUTE NORMALIZATION          OPEN
ARITHMETIC PRIME IDENTIFICATION           NOT IMPLIED
```
