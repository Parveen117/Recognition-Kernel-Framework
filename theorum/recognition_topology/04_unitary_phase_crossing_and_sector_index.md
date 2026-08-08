# RT-04 - Unitary Phase-Crossing and Topological Sector-Index Theorem

## 1. Scalar unitary loop

Let
\[
U:[0,1]\to U(1)
\]
be continuous with
\[
U(0)=U(1).
\]

Choose a continuous real lift
\[
\phi:[0,1]\to\mathbb R
\]
such that
\[
\boxed{
U(t)=e^{-i\phi(t)}.
}
\]

Because the endpoints agree,
\[
\phi(1)-\phi(0)=2\pi\nu
\]
for a unique
\[
\nu\in\mathbb Z.
\]

This integer is the winding degree of the unitary loop.

## 2. Theorem - signed reference-phase crossing count

Let
\[
z_*=e^{-i\theta_*}\in U(1)
\]
be a regular reference value of \(U\), so all crossings are isolated and
transverse.

Then the signed number of crossings of \(z_*\) by \(U(t)\) is
\[
\boxed{
N_{\mathrm{cross}}(U;z_*)=\nu.
}
\]

### Proof

The map \(U:S^1\to S^1\) has degree \(\nu\).
For a regular value \(z_*\), the degree theorem in one dimension states that
the degree equals the signed number of preimages of \(z_*\).
Those preimages are precisely the transverse eigenphase crossings of the
reference phase. Therefore
\[
N_{\mathrm{cross}}(U;z_*)=\deg U=\nu.
\]
QED.

## 3. Nontransverse paths

If a path has tangential or degenerate crossings, the stable definition is the
topological degree (or an equivalent regularized crossing count after a small
admissible perturbation), not independent sorting of principal phases.

The integer is stable under homotopies that preserve the relevant endpoint and
gap/reference-value conditions.

## 4. Operator-language boundary

The theorem concerns the unitary phase path \(U(t)\) itself, equivalently its
continuously lifted eigenphase in the scalar case.

It does **not** assert, without additional hypotheses, that the spectral flow of
the instantaneous rate generator
\[
G_t=iU(t)^{-1}\dot U(t)
\]
equals the winding of \(U\).

The rate \(G_t\) and the accumulated phase \(\phi(t)\) are different typed
objects:
\[
G_t=\dot\phi(t)
\]
under the convention above.

Crossings of \(\dot\phi\) through a fixed real level are not generally the same
as crossings of \(\phi\) modulo \(2\pi\).

## 5. Finite-rank extension boundary

For a finite-rank unitary path with a reference point outside the endpoint
spectrum, a unitary spectral-flow / eigenphase-crossing index can be defined by
continuously following spectral branches, with multiplicity.

At degeneracies, independent sorting of principal angles is not a valid proof
of branch identity.

This folder does not promote an infinite-dimensional Fredholm spectral-flow
claim without the corresponding continuity, Fredholm, and gap hypotheses.

## 6. Recognition meaning

The topological event ledger should retain the integer crossing/degree index
when the target depends on sector history.

Terminal principal holonomy can be identical before and after a full turn, as
RT-03 proves, while the crossing ledger records the nontrivial topological path.

## 7. Claim status

```text
SCALAR UNITARY LOOP DEGREE                   PROVED
SIGNED REGULAR-PHASE CROSSING = DEGREE       PROVED
DEGENERACY HANDLED BY DEGREE/REGULARIZATION  PROVED AT TOPOLOGICAL LEVEL
RATE-GENERATOR SPECTRAL FLOW = WINDING       NOT CLAIMED
FINITE-RANK EIGENPHASE EXTENSION             CONDITIONAL ON BRANCH/GAP DATA
INFINITE-DIMENSIONAL FREDHOLM EXTENSION       OPEN HERE
```
