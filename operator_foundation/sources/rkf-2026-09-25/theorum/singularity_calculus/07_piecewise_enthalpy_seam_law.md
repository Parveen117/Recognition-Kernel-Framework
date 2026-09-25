# SC-07 — Piecewise-Enthalpy Seam Law

## 1. Two thermodynamic sectors

Let \((P,S)\) be a chart cut by a regular seam

\[
\Sigma=\{\rho(P,S)=0\}.
\]

On the two sides, let

\[
\alpha_\pm
=
T_\pm(P,S)\,dS
+
V_\pm(P,S)\,dP.
\]

Define the piecewise process form

\[
\alpha
=
\alpha_-+H(\rho)(\alpha_+-\alpha_-).
\]

## Theorem 1.1 — Bulk Maxwell defect plus seam defect

The distributional curvature is

\[
\boxed{
\begin{aligned}
d\alpha
={}&
(1-H(\rho))
\left(
\partial_P T_-
-
\partial_S V_-
\right)dP\wedge dS\\
&+
H(\rho)
\left(
\partial_P T_+
-
\partial_S V_+
\right)dP\wedge dS\\
&+
\delta(\rho)d\rho\wedge
\left[
(T_+-T_-)\,dS
+
(V_+-V_-)\,dP
\right].
\end{aligned}
}
\]

### Proof

Apply SC-02 to each smooth side and SC-03 to their Heaviside gluing. ∎

## Corollary 1.2 — Equilibrium-on-each-side, singular-at-interface

If each side separately satisfies the Maxwell relation,

\[
\partial_P T_\pm
=
\partial_S V_\pm,
\]

then all nonclosure is seam-supported:

\[
\boxed{
d\alpha
=
\delta(\rho)d\rho\wedge
\left[
\Delta T\,dS+\Delta V\,dP
\right].
}
\]

This gives a precise meaning to an interface that is flat in both bulk phases
but carries irreversible/non-exact seam memory.

## Corollary 1.3 — Removable thermodynamic seam criterion

The singular curvature vanishes exactly when the tangential pullback satisfies

\[
\boxed{
i^*(\Delta T\,dS+\Delta V\,dP)=0.
}
\]

A discontinuity can therefore be present in a normal component without
generating a singular 2-form; what matters is the tangential process-form jump.

## What this does not prove

This theorem does not identify the seam with:

- a topological winding transition;
- an Onsager antisymmetric coefficient;
- a microscopic phase transition;
- a chemical bond;
- an atomic shell;
- a device threshold.

Any such identification requires an explicit domain adapter.

## Status

```text
PIECEWISE ENTHALPY CURVATURE LAW       PROVED
BULK MAXWELL + SEAM DECOMPOSITION      PROVED
FLAT-BULK / SINGULAR-INTERFACE LIMIT   PROVED
THERMODYNAMIC SEAM REMOVABILITY        PROVED
MICROSCOPIC OR TOPOLOGICAL IDENTITY    OPEN / DOMAIN-SPECIFIC
```
