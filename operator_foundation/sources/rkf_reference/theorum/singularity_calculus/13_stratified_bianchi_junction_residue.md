# SC-13 — Stratified Bianchi and Junction-Residue Theorem

## 1. Why a junction residue is a second-level object

SC-12 proves that a genuine piecewise process 1-form does not acquire an independent
\(\delta(\rho_1)\delta(\rho_2)\) term in its first curvature \(d\alpha\).

A codimension-two obstruction appears instead when bulk and seam curvature data are
declared independently and one asks whether the resulting stratified curvature packet is
closed.

Assume \(\dim U\ge3\), and retain the transverse seams

\[
\Sigma_1=\{\rho_1=0\},\qquad
\Sigma_2=\{\rho_2=0\},\qquad
J=\Sigma_1\cap\Sigma_2.
\]

Let \(\Omega_{\varepsilon_1\varepsilon_2}\) be smooth 2-forms in the four bulk sectors.
Let \(\beta_1\) be a piecewise-smooth tangential 1-form on \(\Sigma_1\), allowed to jump
across \(J\), and let \(\beta_2\) be the corresponding object on \(\Sigma_2\).

Consider the stratified 2-current

\[
\boxed{
\Omega
=
\sum_{\varepsilon_1,\varepsilon_2}
\mathbf 1_{U_{\varepsilon_1\varepsilon_2}}
\Omega_{\varepsilon_1\varepsilon_2}
+
\delta(\rho_1)d\rho_1\wedge\beta_1
+
\delta(\rho_2)d\rho_2\wedge\beta_2.
}
\]

This need not have been constructed as \(d\alpha\).

## 2. Codimension-one Bianchi residues

Across \(\Sigma_i\), let \(\Delta_i\Omega\) denote the appropriate one-sided jump of the
bulk 2-form. Define the seam Bianchi residues

\[
\boxed{
B_i
=
i_i^*(\Delta_i\Omega)-d_{\Sigma_i}\beta_i,
\qquad i=1,2.
}
\]

They measure whether the declared seam curvature is compatible with the jump in the bulk
curvature.

## 3. Codimension-two junction residue

Let

\[
\Delta_2\beta_1
\]

denote the jump of the \(\Sigma_1\)-residue when crossing \(\Sigma_2\), and let

\[
\Delta_1\beta_2
\]

denote the jump of the \(\Sigma_2\)-residue when crossing \(\Sigma_1\). Their common
traces are compared on \(J\).

### Definition 3.1 — Junction Bianchi residue

Define

\[
\boxed{
J_{12}
=
k^*(\Delta_1\beta_2-\Delta_2\beta_1),
}
\]

where \(k:J\hookrightarrow U\) is inclusion.

For data produced by a genuine four-sector process form, SC-12 gives

\[
\Delta_1\beta_2=\Delta_2\beta_1=\Delta_{12}\alpha,
\]

and therefore

\[
\boxed{J_{12}=0.}
\]

## Theorem 3.2 — Stratified derivative decomposition

The distributional derivative of the declared curvature packet decomposes by stratum as

\[
\boxed{
\begin{aligned}
d\Omega
={}&
\sum_{\varepsilon_1,\varepsilon_2}
\mathbf 1_{U_{\varepsilon_1\varepsilon_2}}
 d\Omega_{\varepsilon_1\varepsilon_2}\\
&+
\delta(\rho_1)d\rho_1\wedge \widetilde B_1
+
\delta(\rho_2)d\rho_2\wedge \widetilde B_2\\
&+
\delta(\rho_1)\delta(\rho_2)
 d\rho_1\wedge d\rho_2\wedge\widetilde J_{12},
\end{aligned}
}
\]

where the tildes denote arbitrary local extensions of the intrinsic seam/junction forms.
The current is independent of the chosen extensions.

### Proof

Differentiate the bulk characteristic-function terms. Their singular derivatives give the
bulk jumps \(\delta(\rho_i)d\rho_i\wedge\Delta_i\Omega\).

For a seam term,

\[
d\bigl(\delta(\rho_i)d\rho_i\wedge\beta_i\bigr)
=
-\delta(\rho_i)d\rho_i\wedge d\beta_i,
\]

because \(d(\delta(\rho_i)d\rho_i)=d^2H(\rho_i)=0\).
The smooth tangential part of \(d\beta_i\) produces \(-d_{\Sigma_i}\beta_i\), yielding
\(B_i\).

The jump of \(\beta_1\) across \(\Sigma_2\) contributes

\[
-\delta(\rho_1)\delta(\rho_2)
 d\rho_1\wedge d\rho_2\wedge\Delta_2\beta_1,
\]

whereas the jump of \(\beta_2\) across \(\Sigma_1\) contributes

\[
+\delta(\rho_1)\delta(\rho_2)
 d\rho_1\wedge d\rho_2\wedge\Delta_1\beta_2.
\]

Their difference is exactly \(J_{12}\). ∎

## Theorem 3.3 — Stratified Bianchi closure criterion

Under the declared regularity and transversality assumptions,

\[
\boxed{d\Omega=0}
\]

if and only if all three recognition layers close:

\[
\boxed{
\begin{aligned}
&d\Omega_{\varepsilon_1\varepsilon_2}=0
&&\text{in every bulk sector},\\
&B_1=B_2=0
&&\text{on the codimension-one seams},\\
&J_{12}=0
&&\text{on the codimension-two junction}.
\end{aligned}
}
\]

### Proof

The three families of terms are supported on strata of different codimension. Testing away
from the seams forces bulk closure. Testing on a seam away from \(J\) forces the seam
Bianchi residue to vanish. The remaining current is supported on \(J\), forcing
\(J_{12}=0\). The converse follows directly from Theorem 3.2. ∎

## Corollary 3.4 — Genuine piecewise curvature automatically satisfies junction closure

If

\[
\Omega=d\alpha
\]

for the four-sector process form of SC-12, then

\[
\boxed{d\Omega=d^2\alpha=0}
\]

and the entire stratified Bianchi packet vanishes:

\[
\boxed{
(d\Omega_{00},d\Omega_{10},d\Omega_{01},d\Omega_{11};B_1,B_2;J_{12})=0.
}
\]

Thus a nonzero \(J_{12}\) is a certificate that independently supplied seam data do not fit
together as the seam curvature of one compatible piecewise potential, unless additional
junction data are explicitly introduced in a higher model.

## Recognition packet

Define

\[
\boxed{
\mathfrak B_{\rm strat}
=
(d\Omega_{\rm bulk};B_{\rm seams};J_{\rm junction}).
}
\]

Recognition may declare Bianchi closure only when every typed component vanishes.
Scalar cancellation between strata is not lawful closure.

## Boundary

This theorem treats a transverse two-seam normal crossing. It does not yet provide:

- nontransverse/tangent seam intersection theory;
- triple or higher normal-crossing junction formulas;
- a sufficiency theorem constructing a global process potential from arbitrary closed stratified data;
- a physical interpretation of \(J_{12}\) without a domain adapter.

## Status

```text
SEAM BIANCHI RESIDUE                              DEFINED
JUNCTION RESIDUE J_12                             DEFINED
STRATIFIED d OMEGA DECOMPOSITION                  PROVED
BULK/SEAM/JUNCTION BIANCHI CLOSURE CRITERION       PROVED
GENUINE PIECEWISE POTENTIAL => J_12=0              PROVED
GENERAL INTEGRABILITY / POTENTIAL EXISTENCE        NOT CLAIMED
NONTRANSVERSE OR HIGHER JUNCTIONS                   NOT CLAIMED
```