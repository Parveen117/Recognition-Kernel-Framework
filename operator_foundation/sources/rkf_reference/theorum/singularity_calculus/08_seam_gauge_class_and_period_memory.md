# SC-08 — Seam Gauge-Class and Closed-Period Memory Theorem

## 1. Seam residue transformation

Let the regular seam and piecewise process form be as in SC-03 and SC-04, with
tangential seam residue

\[
R_\Sigma=i^*(\alpha_+-\alpha_-)\in\Omega^1(\Sigma).
\]

Allow independent smooth side-gauge changes

\[
\alpha_\pm'=\alpha_\pm+d\chi_\pm.
\]

Write

\[
g=i^*(\chi_+-\chi_-)\in\Omega^0(\Sigma).
\]

Then SC-04 gives

\[
\boxed{
R_\Sigma'=R_\Sigma+d_\Sigma g.
}
\]

## Theorem 1.1 — Gauge class of the seam residue

The equivalence class

\[
\boxed{
[R_\Sigma]_{\rm gauge}
\in
\Omega^1(\Sigma)/d_\Sigma\Omega^0(\Sigma)
}
\]

is invariant under arbitrary smooth side-gauge changes.

### Proof

The transformation law changes the residue by the exact seam form
\(d_\Sigma g\). Therefore \(R_\Sigma\) and \(R_\Sigma'\) define the same class
modulo exact one-forms. ∎

## Theorem 1.2 — Closed-cycle period memory

For every piecewise smooth closed 1-cycle \(C\subset\Sigma\),

\[
\boxed{
\oint_C R_\Sigma'
=
\oint_C R_\Sigma.
}
\]

### Proof

Using the transformation law,

\[
\oint_C R_\Sigma'
=
\oint_C R_\Sigma+\oint_C d_\Sigma g.
\]

The final term vanishes on a closed cycle. ∎

## Corollary 1.3 — Cohomological specialization

If additionally

\[
d_\Sigma R_\Sigma=0,
\]

then \(R_\Sigma\) determines a de Rham class

\[
\boxed{
[R_\Sigma]_{\rm dR}\in H^1_{\rm dR}(\Sigma),
}
\]

and the class is invariant under side-gauge changes.

## Recognition interpretation

The point is not that every local seam residue is topological. It is that
representation changes cannot alter the exact-quotient class or its closed-cycle
periods:

```text
local seam residue
-> gauge class modulo exact seam forms
-> closed-cycle period memory.
```

This gives a lawful interface to Recognition Topology when a domain adapter
also proves the required closedness/topological hypotheses.

## Status

```text
GENERAL SIDE-GAUGE TRANSFORMATION LAW PROVED
GAUGE CLASS MODULO EXACT FORMS        PROVED
CLOSED-CYCLE PERIOD INVARIANCE        PROVED
DE RHAM CLASS WHEN R_SIGMA IS CLOSED  PROVED
AUTOMATIC TOPOLOGICAL INTERPRETATION  NOT CLAIMED
```
