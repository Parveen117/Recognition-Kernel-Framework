# SC-05 — Seam-Stokes Memory Theorem

## 1. Setup

Let \(S\) be an oriented compact 2-surface transverse to a regular seam
\(\Sigma=\{\rho=0\}\). Let

\[
S_\pm=S\cap U_\pm,
\qquad
\Gamma_\Sigma=S\cap\Sigma.
\]

Give \(\Gamma_\Sigma\) the intersection orientation determined by the chosen
coorientation \(d\rho\).

Let \(\alpha\) be the piecewise-smooth process form from SC-03.

## Theorem 1.1 — Stokes formula with seam memory

In the current sense,

\[
\boxed{
\oint_{\partial S}\alpha
=
\int_{S_-}d\alpha_-
+
\int_{S_+}d\alpha_+
+
\int_{\Gamma_\Sigma}R_\Sigma.
}
\]

### Proof

SC-03 gives

\[
d\alpha
=
(1-H)d\alpha_-+Hd\alpha_+
+\delta(\rho)d\rho\wedge(\alpha_+-\alpha_-).
\]

Pair this current with the integration current \([S]\). The first two terms
give the ordinary bulk integrals. Transversality converts the delta-supported
term into the integral of the tangential jump residue over
\(\Gamma_\Sigma\). Distributional Stokes gives

\[
\langle d\alpha,[S]\rangle
=
\langle\alpha,\partial[S]\rangle
=
\oint_{\partial S}\alpha.
\]

Combining these identities proves the formula. ∎

## Corollary 1.2 — Pure seam memory in flat bulk sectors

If

\[
d\alpha_-=0,
\qquad
d\alpha_+=0,
\]

then

\[
\boxed{
\oint_{\partial S}\alpha
=
\int_{\Gamma_\Sigma}R_\Sigma.
}
\]

Thus a loop can carry nonzero Recognition memory even when both smooth bulk
sectors are individually flat.

## Example 1.3 — Exact rectangular calibration

On \(\mathbb R^2\) with coordinates \((x,y)\), take

\[
\Sigma=\{x=0\},
\qquad
\alpha_-=0,
\qquad
\alpha_+=c\,dy.
\]

Then

\[
R_\Sigma=c\,dy,
\qquad
d\alpha_\pm=0,
\]

and for the rectangle

\[
S=[-a,a]\times[0,b],
\]

one gets

\[
\boxed{
\oint_{\partial S}\alpha
=
cb
=
\int_{S\cap\Sigma}c\,dy.
}
\]

The proof-lab verifies this identity using exact rational arithmetic.

## Recognition interpretation

This theorem is the singularity-calculus analogue of path memory:

```text
bulk return/flatness
does not imply
zero seam ledger.
```

It interfaces naturally with Morphic Recognition MR-03, but does not identify
the seam residue with a cocycle unless a domain adapter proves that
identification.

## Status

```text
DISTRIBUTIONAL STOKES WITH SEAM TERM PROVED
PURE SEAM MEMORY IN FLAT BULK        PROVED
EXACT RECTANGLE CALIBRATION          VERIFIED
COCYCLE IDENTIFICATION               OPTIONAL / NOT AUTOMATIC
```
