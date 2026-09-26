# Verified Singularity Calculus — Multi-Seam Composition Extension

## Status

```text
THEORY EXTENSION STATUS:
RNKE_VERIFIED_SINGULARITY_THEORY_V2_WITH_EXCLUSIONS
```

This extension consumes the verified SC-01 through SC-09 theory and adds SC-10
and SC-11. It answers the composition question for a finite family of regular,
pairwise-disjoint Recognition seams.

## 1. Finite multi-seam law

For regions \(U_0,\ldots,U_m\) separated by regular disjoint seams
\(\Sigma_1,\ldots,\Sigma_m\), with process forms \(\alpha_k\), define

\[
\Omega_k=d\alpha_k,
\qquad
R_j=i_j^*(\alpha_j-\alpha_{j-1}).
\]

The distributional curvature is

\[
\boxed{
 d\alpha
 =
 \sum_{k=0}^{m}\mathbf 1_{U_k}\Omega_k
 +
 \sum_{j=1}^{m}\delta(\rho_j)d\rho_j\wedge(\alpha_j-\alpha_{j-1}).
}
\]

The finite closure packet is therefore

\[
\boxed{
\mathfrak C_{\rm multi}
=(\Omega_0,\ldots,\Omega_m;R_1,\ldots,R_m).
}
\]

Complete closure is componentwise:

\[
\boxed{
 d\alpha=0
 \iff
 \Omega_k=0\ \forall k
 \text{ and }
 R_j=0\ \forall j.
}
\]

For an oriented comparison surface \(S\),

\[
\boxed{
\oint_{\partial S}\alpha
=
\sum_k\int_{S\cap U_k}\Omega_k
+
\sum_j\int_{S\cap\Sigma_j}R_j.
}
\]

Hence in flat bulk sectors the seam memory is additive.

## 2. Composition fillers

Choose path representatives \(\gamma_a\) and, for each composable pair \((b,a)\),
a comparison 2-chain \(F(b,a)\) satisfying

\[
\partial F(b,a)=\gamma_b+\gamma_a-\gamma_{ba}.
\]

Define the seam-memory coordinate

\[
\boxed{
\omega_\Sigma(b,a)
=
\sum_j\int_{F(b,a)\cap\Sigma_j}R_j.
}
\]

For a composable triple define the closed associator comparison cycle

\[
\boxed{
\mathcal A(c,b,a)
=
F(c,ba)+F(b,a)-F(cb,a)-F(c,b).
}
\]

## 3. Cocycle / interaction theorem

The seam-memory cocycle defect is

\[
\boxed{
\delta\omega_\Sigma(c,b,a)
=
\omega_\Sigma(c,ba)+\omega_\Sigma(b,a)
-\omega_\Sigma(cb,a)-\omega_\Sigma(c,b).
}
\]

SC-11 proves

\[
\boxed{
\delta\omega_\Sigma(c,b,a)
=
\sum_j\int_{\mathcal A(c,b,a)\cap\Sigma_j}R_j.
}
\]

Because \(\mathcal A(c,b,a)\) is closed and the full curvature is exact,

\[
\boxed{
\delta\omega_\Sigma(c,b,a)
=
-\sum_k\int_{\mathcal A(c,b,a)\cap U_k}\Omega_k.
}
\]

This is the central v2 result.

### Flat bulk

If

\[
\Omega_k=0\qquad\forall k,
\]

then

\[
\boxed{\delta\omega_\Sigma=0.}
\]

With normalized identity fillers, \(\omega_\Sigma\) is exactly an MR-03
normalized memory cocycle. Seam memory therefore produces an associative
memory-lifted Recognition category.

### Curved bulk

If the associator bulk flux is nonzero, then seam memory alone is not a cocycle:

\[
\boxed{
\delta\omega_\Sigma=-\mathcal B.
}
\]

The interaction term \(\mathcal B\) is not an error to be averaged away. It is a
separate typed curvature obligation. A faithful Recognition carrier must retain
it or restrict to a sector where it vanishes.

Thus the composition hierarchy is

\[
\boxed{
\begin{array}{c}
\text{individual disjoint seams}\to\text{additive memory},\\[1mm]
\text{flat bulk}\to\text{cocyclic memory},\\[1mm]
\text{curved bulk}\to\text{cocycle defect = curvature interaction}.
\end{array}
}
\]

## 4. Gauge compatibility

The associator cycle is closed. Exact seam-gauge changes therefore do not alter
its closed-cycle seam period. The cocycle defect is invariant under the coherent
gauge re-presentations already admitted by SC-08.

Individual filler coordinates may change by cochain terms, matching the MR-03
coboundary picture; the associator defect is the invariant obstruction.

## 5. Verification

The proof lab adds exact controls for:

- additive Stokes memory across several seams;
- exact MR-03 cocycle closure for the flat-bulk integer calibration;
- a deliberately noncocyclic rule with defect `60` and compensating bulk flux
  `-60`;
- preservation of all SC-01 through SC-09 controls.

The validated theorem head passes the complete suite on Python 3.11 and 3.12.

## 6. Boundary

This v2 extension does not yet claim a general codimension-2 junction calculus
for intersecting seams. At an actual seam intersection, traces, corner currents,
and junction compatibility require a separate theorem. No delta-times-delta term
is introduced here by wishful notation.

It also does not identify the bulk interaction with a physical force, winding
jump, Onsager coefficient, atomic shell, chemical bond, or device threshold
without an explicit domain adapter.
