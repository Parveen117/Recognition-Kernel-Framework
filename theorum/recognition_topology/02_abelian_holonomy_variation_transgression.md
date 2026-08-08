# RT-02 - Abelian Holonomy-Variation and Curvature-Transgression Theorem

## 1. Geometric datum

Let \(M\) be a smooth manifold and let
\[
\omega\in\Omega^1(M;\mathbb R)
\]
be a fixed abelian connection one-form in a declared trivialization.

Its curvature is
\[
\boxed{
\Omega=d\omega.
}
\]

Let
\[
c:[0,1]\times S^1\to M
\]
be a smooth family of closed loops
\[
C_t=c_t(S^1),
\qquad
c_t(s):=c(t,s).
\]

Write the deformation vector along the swept surface as
\[
V_t=\partial_t c(t,\cdot).
\]

Define the lifted holonomy phase
\[
\boxed{
\Phi(t)=\oint_{C_t}\omega.
}
\]

Use the convention
\[
\boxed{
U(t)=e^{-i\Phi(t)}\in U(1).
}
\]

## 2. Theorem - curvature transgression

For every \(t\),
\[
\boxed{
\dot\Phi(t)
=
\oint_{C_t}\iota_{V_t}\Omega.
}
\]

Consequently,
\[
\boxed{
iU(t)^{-1}\dot U(t)
=
\dot\Phi(t)
=
\oint_{C_t}\iota_{V_t}\Omega.
}
\]

### Proof

Differentiate the pullback line integral:
\[
\frac d{dt}\oint_{S^1}c_t^*\omega
=
\oint_{S^1}c_t^*(\mathcal L_{V_t}\omega).
\]

Cartan's identity gives
\[
\mathcal L_{V_t}\omega
=
\iota_{V_t}d\omega
+
d(\iota_{V_t}\omega).
\]

Because \(S^1\) is closed,
\[
\oint_{S^1}d(\iota_{V_t}\omega)=0.
\]

Hence
\[
\dot\Phi(t)
=
\oint_{C_t}\iota_{V_t}d\omega
=
\oint_{C_t}\iota_{V_t}\Omega.
\]

Finally,
\[
\dot U=-i\dot\Phi\,U,
\]
so
\[
iU^{-1}\dot U=\dot\Phi.
\]
QED.

## 3. Gauge covariance

For a single-valued smooth gauge function \(\chi\),
\[
\omega'=\omega+d\chi.
\]

For every closed loop,
\[
\oint_C\omega'
=
\oint_C\omega+\oint_Cd\chi
=
\oint_C\omega.
\]

Therefore \(\Phi\), \(U\), and the transgression law above are unchanged under
this exact gauge change.

Large gauge transformations and nontrivial bundle patching require branch data;
they belong to RT-03 rather than being silently identified with the exact-gauge
case.

## 4. Time-dependent connection correction

If the connection itself varies,
\[
\omega=\omega_t,
\]
then the correct formula is
\[
\boxed{
\frac d{dt}\oint_{C_t}\omega_t
=
\oint_{C_t}
\left(
\partial_t\omega_t+\iota_{V_t}d\omega_t
\right).
}
\]

Thus the pure curvature-transgression formula requires a fixed connection, or a
separate proof that the explicit \(\partial_t\omega_t\) contribution vanishes.

## 5. Exact rectangle calibration

On \(\mathbb R^2\), let
\[
\omega=x\,dy,
\qquad
\Omega=dx\wedge dy.
\]

For the positively oriented rectangle
\[
C_a=\partial([0,a]\times[0,1]),
\]
Stokes gives
\[
\Phi(a)
=
\oint_{C_a}x\,dy
=
\int_{[0,a]\times[0,1]}dx\wedge dy
=
a.
\]

Hence for a smooth width \(a(t)\),
\[
\dot\Phi(t)=\dot a(t),
\]
exactly matching curvature flux through the swept strip.

## 6. Recognition meaning

RT-02 supplies the missing theorem-grade bridge
\[
\boxed{
\text{curvature}
\longrightarrow
\text{holonomy-phase variation}.
}
\]

RT-01 supplies a different bridge
\[
\boxed{
\text{integer topological-sector change}
\longrightarrow
\text{seam event}.
}
\]

The two statements must not be collapsed into the false implication
“nonzero curvature automatically changes winding.”

## 7. Claim status

```text
FIXED U(1) HOLONOMY-VARIATION FORMULA       PROVED
CURVATURE TRANSGRESSION                     PROVED
EXACT-GAUGE INVARIANCE ON CLOSED LOOPS      PROVED
TIME-DEPENDENT CONNECTION CORRECTION        PROVED
RECTANGLE CALIBRATION                       VERIFIED
PLAIN FORMULA FOR NONABELIAN HOLONOMY       NOT CLAIMED
CURVATURE MAGNITUDE => TOPOLOGICAL JUMP     NOT CLAIMED
```
