# SC-10 — Finite Multi-Seam Additivity and Closure Theorem

## 1. Ordered disjoint seam family

Let a smooth chart \(U\) be divided into regions

\[
U_0,U_1,\ldots,U_m
\]

by a finite family of pairwise-disjoint regular cooriented hypersurfaces

\[
\Sigma_j=\{\rho_j=0\},\qquad d\rho_j\neq0\text{ on }\Sigma_j,
\qquad j=1,\ldots,m.
\]

Assume \(\Sigma_j\) separates the neighboring regions \(U_{j-1}\) and \(U_j\).
On each region let

\[
\alpha_j\in\Omega^1(U_j)
\]

be \(C^1\) and admit one-sided traces on the neighboring seams.

Define the jump and tangential residue at \(\Sigma_j\) by

\[
\Delta_j\alpha
=\alpha_j|_{\Sigma_j}-\alpha_{j-1}|_{\Sigma_j},
\qquad
\boxed{R_j=i_j^*(\Delta_j\alpha)}.
\]

## Theorem 1.1 — Multi-seam distributional decomposition

The piecewise process form has distributional curvature

\[
\boxed{
 d\alpha
 =
 \sum_{k=0}^{m}\mathbf 1_{U_k}\,d\alpha_k
 +
 \sum_{j=1}^{m}
 \delta(\rho_j)d\rho_j\wedge\Delta_j\alpha.
}
\]

No additional cross-delta term occurs for pairwise-disjoint seams.

### Proof

Near any one seam \(\Sigma_j\), all other seams are absent. The local statement is
exactly SC-03. A partition of unity subordinate to the bulk regions and seam
neighborhoods patches the local current identities. Exterior differentiation is
linear and first-order, so no product of two seam delta currents is generated in
this disjoint-seam setting. ∎

## Theorem 1.2 — Additive multi-seam Stokes law

Let \(S\) be an oriented compact 2-surface transverse to every \(\Sigma_j\), and
write

\[
\Gamma_j=S\cap\Sigma_j.
\]

Then

\[
\boxed{
\oint_{\partial S}\alpha
=
\sum_{k=0}^{m}\int_{S\cap U_k}d\alpha_k
+
\sum_{j=1}^{m}\int_{\Gamma_j}R_j.
}
\]

### Proof

Pair Theorem 1.1 with the integration current \([S]\). Each delta-supported term
reduces by transversality to the integral of the tangential jump residue over
\(\Gamma_j\). Distributional Stokes completes the identity. ∎

## Corollary 1.3 — Flat-bulk seam memory is additive

If

\[
d\alpha_k=0\qquad\text{for every }k,
\]

then

\[
\boxed{
\oint_{\partial S}\alpha
=
\sum_{j=1}^{m}\int_{\Gamma_j}R_j.
}
\]

Thus the seam-memory contribution of a finite disjoint family is the algebraic
sum of the individual seam memories, with signs determined by the chosen
coorientations and intersection orientations.

## Theorem 1.4 — Multi-seam closure criterion

Under the stated disjointness and regularity assumptions,

\[
\boxed{d\alpha=0}
\]

if and only if

\[
\boxed{
 d\alpha_k=0\ \text{for all }k,
 \qquad
 R_j=0\ \text{for all }j.
}
\]

### Proof

The forward implication is obtained by testing in the interiors of the regions,
which forces every bulk curvature to vanish, followed by testing in disjoint seam
neighborhoods and using SC-04, which forces every tangential seam residue to
vanish. The reverse implication is immediate from Theorem 1.1. ∎

## Recognition closure packet

The finite multi-seam closure packet is

\[
\boxed{
\mathfrak C_{\rm multi}
=
(\Omega_0,\ldots,\Omega_m;R_1,\ldots,R_m),
\qquad
\Omega_k=d\alpha_k.
}
\]

Complete closure is componentwise:

\[
\boxed{
\mathfrak C_{\rm multi}=0
\iff
\Omega_k=0\ \forall k
\text{ and }
R_j=0\ \forall j.
}
\]

## Exact calibration

On \(\mathbb R^2\), take two vertical seams \(x=0\) and \(x=1\) and flat bulk
forms

\[
\alpha_0=0,
\qquad
\alpha_1=c_1\,dy,
\qquad
\alpha_2=(c_1+c_2)\,dy.
\]

For a rectangle crossing both seams, the boundary integral is

\[
(c_1+c_2)h
\]

and the two seam terms are

\[
c_1h+c_2h.
\]

The proof lab checks this identity with exact rational arithmetic.

## Status

```text
FINITE DISJOINT-SEAM CURVATURE DECOMPOSITION  PROVED
MULTI-SEAM STOKES ADDITIVITY                  PROVED
FLAT-BULK SEAM MEMORY ADDITIVITY              PROVED
MULTI-SEAM COMPONENTWISE CLOSURE              PROVED
CROSS-DELTA INTERACTION FOR DISJOINT SEAMS     ABSENT / PROVED
INTERSECTING-SEAM JUNCTION THEORY              NOT CLAIMED HERE
```
