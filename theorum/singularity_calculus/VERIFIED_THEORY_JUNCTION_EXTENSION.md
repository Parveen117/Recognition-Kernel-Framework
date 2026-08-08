# Verified Singularity Calculus — Junction Extension

## Status

```text
THEORY EXTENSION STATUS:
RNKE_VERIFIED_SINGULARITY_THEORY_V3_WITH_EXCLUSIONS
```

This extension consumes SC-01 through SC-11 and adds the first transverse
codimension-two junction layer.

## 1. What changes at an intersecting seam

For two transverse regular seams

\[
\Sigma_1=\{\rho_1=0\},\qquad
\Sigma_2=\{\rho_2=0\},
\]

with junction

\[
J=\Sigma_1\cap\Sigma_2,
\]

a genuine piecewise process 1-form has four smooth sector representatives.

The first crucial result is negative but important:

\[
\boxed{
\text{there is no independent }
\delta(\rho_1)\delta(\rho_2)
\text{ term in }d\alpha.
}
\]

Exterior differentiation is first order. The first curvature contains bulk and
codimension-one seam currents only.

## 2. Mixed-jump compatibility

For the four sector forms define the two routes to the mixed jump:

\[
\Delta_1^+\alpha-\Delta_1^-\alpha,
\qquad
\Delta_2^+\alpha-\Delta_2^-\alpha.
\]

SC-12 proves

\[
\boxed{
\Delta_1^+\alpha-\Delta_1^-\alpha
=
\Delta_2^+\alpha-\Delta_2^-\alpha
=
\Delta_{12}\alpha.
}
\]

When the two seam currents are differentiated, their possible codimension-two
contributions are opposite and cancel. This is the local stratified form of

\[
\boxed{d^2\alpha=0.}
\]

## 3. Junction residue for independently declared curvature

The codimension-two object becomes nontrivial only when a curvature packet is
declared independently rather than generated automatically as \(d\alpha\).

Write

\[
\Omega
=
\Omega_{\rm bulk}
+
\delta(\rho_1)d\rho_1\wedge\beta_1
+
\delta(\rho_2)d\rho_2\wedge\beta_2.
\]

The seam Bianchi residues are

\[
B_i=i_i^*(\Delta_i\Omega)-d_{\Sigma_i}\beta_i.
\]

The new junction residue is

\[
\boxed{
J_{12}
=
k^*(\Delta_1\beta_2-\Delta_2\beta_1).
}
\]

SC-13 proves the stratified decomposition

\[
\boxed{
\begin{aligned}
d\Omega
={}&
(d\Omega)_{\rm bulk}
+
\delta(\rho_1)d\rho_1\wedge B_1
+
\delta(\rho_2)d\rho_2\wedge B_2\\
&+
\delta(\rho_1)\delta(\rho_2)
 d\rho_1\wedge d\rho_2\wedge J_{12}.
\end{aligned}
}
\]

The double-delta object belongs to **the derivative of the stratified curvature
packet**, not to the first curvature of a genuine piecewise 1-form.

## 4. Stratified Bianchi closure

The verified closure packet is

\[
\boxed{
\mathfrak B_{\rm strat}
=
(d\Omega_{\rm bulk};B_1,B_2;J_{12}).
}
\]

Under the transverse regularity assumptions,

\[
\boxed{
d\Omega=0
\iff
\mathfrak B_{\rm strat}=0.
}
\]

So the Recognition hierarchy is now:

```text
bulk curvature closure
        ↓
seam Bianchi closure
        ↓
junction compatibility closure.
```

A scalar total cannot replace this typed packet.

## 5. Relation to earlier theory

SC-10 showed that disjoint seams contribute additively.

SC-11 showed that, for comparison fillers, flat bulk makes seam memory an MR-03
cocycle while curved bulk produces an explicit associator defect.

SC-12/13 now explain the additional local compatibility required when seam
supports themselves intersect:

\[
\boxed{
\text{path composition interaction}
\quad\text{and}\quad
\text{geometric junction compatibility}
}
\]

are distinct typed obligations.

The first is a filler/associator statement. The second is a normal-crossing
Bianchi statement.

## 6. Verification

Validated theorem head:

```text
431408ff4dadfe13cb917c96e0c46dd3cd8ab048
```

Exact verification:

```text
19/19 unit tests PASS
18 exact calibration controls PASS
Python 3.11 PASS
Python 3.12 PASS
GitHub Actions run 31259516097 PASS
```

## 7. What is not claimed

This extension does not claim:

- a double-delta term in \(d\alpha\);
- arbitrary nontransverse seam intersection theory;
- triple-junction or higher-normal-crossing formulas;
- global potential reconstruction from arbitrary closed stratified data;
- automatic topological, thermodynamic, microscopic, atomic, chemical or device
  interpretation of \(J_{12}\).

Those require later theorems or domain adapters.
