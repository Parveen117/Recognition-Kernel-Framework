# SC-06 — Regular/Singular Typed Non-Cancellation Theorem

## 1. Measure-valued curvature

Let \(\mu\) be a smooth volume measure on a chart and let
\(\sigma_\Sigma\) be hypersurface measure on a regular seam \(\Sigma\).
For a finite-dimensional coefficient space \(E\), consider an \(E\)-valued
curvature measure

\[
\Omega
=
\Omega_{\mathrm{bulk}}
+
\Omega_{\mathrm{seam}},
\]

where

\[
\Omega_{\mathrm{bulk}}\ll\mu
\]

is absolutely continuous and

\[
\Omega_{\mathrm{seam}}\ll\sigma_\Sigma,
\qquad
\Omega_{\mathrm{seam}}\perp\mu.
\]

The two channels are mutually singular measures.

## Theorem 1.1 — Typed non-cancellation

If

\[
\boxed{\Omega=0}
\]

as an \(E\)-valued measure/current, then

\[
\boxed{
\Omega_{\mathrm{bulk}}=0,
\qquad
\Omega_{\mathrm{seam}}=0.
}
\]

### Proof

Apply the uniqueness of the Lebesgue decomposition componentwise in a basis of
the finite-dimensional coefficient space \(E\). The zero measure has zero
absolutely-continuous part and zero singular part. Since the decomposition is
unique, both channels vanish separately. ∎

## Corollary 1.2 — Scalar integral cancellation is not closure

It may happen numerically that a bulk integral and a seam integral have opposite
values:

\[
\int \Omega_{\mathrm{bulk}}
+
\int \Omega_{\mathrm{seam}}
=
0.
\]

This does **not** imply

\[
\Omega=0.
\]

Recognition closure must retain the typed packet

\[
\boxed{
(\Omega_{\mathrm{bulk}},\Omega_{\mathrm{seam}})
}
\]

or an equivalent faithful representation.

## Interface to MR-01

This theorem is a geometric realization of the Typed Residue Non-Cancellation
principle:

```text
different support/type channels
must close componentwise;
a scalar total can hide nonzero obligations.
```

## Status

```text
MUTUAL SINGULARITY OF DECLARED CHANNELS PROVED
LEBESGUE-DECOMPOSITION UNIQUENESS       STANDARD / CONSUMED
REGULAR/SINGULAR NON-CANCELLATION       PROVED
SCALAR TOTAL AS COMPLETE CLOSURE TEST   REJECTED
```
