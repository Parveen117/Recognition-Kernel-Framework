# SC-12 — Normal-Crossing Junction and No-Spurious-Double-Delta Theorem

## 1. Transverse two-seam setup

Let \(U\) be a smooth manifold of dimension at least two and let

\[
\Sigma_1=\{\rho_1=0\},\qquad \Sigma_2=\{\rho_2=0\}
\]

be regular cooriented hypersurfaces meeting transversely along

\[
J=\Sigma_1\cap\Sigma_2,
\qquad
 d\rho_1\wedge d\rho_2\neq0\ \text{on }J.
\]

The seams divide a neighborhood of \(J\) into four sectors
\(U_{00},U_{10},U_{01},U_{11}\). Let

\[
\alpha_{00},\alpha_{10},\alpha_{01},\alpha_{11}
\]

be \(C^1\) process 1-forms with one-sided traces on the seams.

Write \(H_i=H(\rho_i)\), and define

\[
\Delta_1^-\alpha=\alpha_{10}-\alpha_{00},
\qquad
\Delta_1^+\alpha=\alpha_{11}-\alpha_{01},
\]

\[
\Delta_2^-\alpha=\alpha_{01}-\alpha_{00},
\qquad
\Delta_2^+\alpha=\alpha_{11}-\alpha_{10}.
\]

The mixed jump is

\[
\boxed{
\Delta_{12}\alpha
=
\Delta_1^+\alpha-\Delta_1^-\alpha
=
\Delta_2^+\alpha-\Delta_2^-\alpha
=
\alpha_{11}-\alpha_{10}-\alpha_{01}+\alpha_{00}.
}
\]

The equality of the two routes is an algebraic identity for a genuine four-sector assignment.

## Theorem 1.1 — First derivative contains no double-delta curvature

The piecewise process form may be written

\[
\alpha
=
\alpha_{00}
+H_1(\alpha_{10}-\alpha_{00})
+H_2(\alpha_{01}-\alpha_{00})
+H_1H_2\Delta_{12}\alpha.
\]

Its distributional curvature has the form

\[
\boxed{
 d\alpha
 =
 \sum_{\varepsilon_1,\varepsilon_2}
 \mathbf 1_{U_{\varepsilon_1\varepsilon_2}}
 d\alpha_{\varepsilon_1\varepsilon_2}
 +\delta(\rho_1)d\rho_1\wedge\beta_1
 +\delta(\rho_2)d\rho_2\wedge\beta_2,
}
\]

where

\[
\beta_1=(1-H_2)\Delta_1^-\alpha+H_2\Delta_1^+\alpha,
\]

\[
\beta_2=(1-H_1)\Delta_2^-\alpha+H_1\Delta_2^+\alpha.
\]

There is **no** term proportional to

\[
\delta(\rho_1)\delta(\rho_2)
\]

in \(d\alpha\).

### Proof

Differentiate the Heaviside representation. Since exterior differentiation is first order,

\[
d(H_1H_2)=H_2\,dH_1+H_1\,dH_2,
\]

with

\[
dH_i=\delta(\rho_i)d\rho_i.
\]

No product \(dH_1\wedge dH_2\) appears in the first derivative. Collecting sector and seam terms gives the displayed formula. ∎

## Theorem 1.2 — Junction cancellation in \(d^2\alpha\)

When the seam-current terms are differentiated, their codimension-two contributions are

\[
-\delta(\rho_1)\delta(\rho_2)
 d\rho_1\wedge d\rho_2\wedge\Delta_{12}\alpha
\]

from the \(\Sigma_1\) channel and

\[
+\delta(\rho_1)\delta(\rho_2)
 d\rho_1\wedge d\rho_2\wedge\Delta_{12}\alpha
\]

from the \(\Sigma_2\) channel.

Hence they cancel exactly:

\[
\boxed{d^2\alpha=0}
\]

at the junction as required.

### Proof

The jump of \(\beta_1\) across \(\Sigma_2\) is \(\Delta_{12}\alpha\), while the jump of \(\beta_2\) across \(\Sigma_1\) is the same mixed jump. The two current derivatives acquire opposite signs because

\[
d\rho_2\wedge d\rho_1=-d\rho_1\wedge d\rho_2.
\]

The codimension-two terms therefore cancel. The remaining bulk/seam pieces cancel by ordinary \(d^2=0\) and the commutation of trace with exterior differentiation. ∎

## Corollary 1.3 — Junction data are compatibility data, not extra curvature in \(d\alpha\)

For a genuine piecewise 1-form, a transverse seam intersection does not create an additional independent point/line curvature term in the first derivative. What the junction tests is whether the two seam jumps arise from one compatible sector assignment.

This distinction matters:

```text
first derivative d alpha
    -> bulk + codimension-1 seam curvature;

junction compatibility
    -> appears in the next Bianchi/closure level.
```

## Recognition interpretation

A red-team or domain adapter must not manufacture a `delta times delta` curvature term merely because two seams cross. A genuine junction obstruction appears only when independently declared seam data fail the mixed-jump compatibility law developed in SC-13.

## Status

```text
TRANSVERSE FOUR-SECTOR DECOMPOSITION          DEFINED
MIXED-JUMP ROUTE IDENTITY                     PROVED
NO DOUBLE-DELTA TERM IN d alpha               PROVED
CODIMENSION-2 CANCELLATION IN d^2 alpha       PROVED
ARBITRARY NONTRANSVERSE / SINGULAR JUNCTIONS  NOT CLAIMED
```