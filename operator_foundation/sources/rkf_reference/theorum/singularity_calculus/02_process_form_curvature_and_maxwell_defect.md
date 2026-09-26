# SC-02 — Process-Form Curvature and the Maxwell-Defect Theorem

## 1. The exterior-derivative obstruction

For every \(C^2\) scalar potential \(\Phi\),

\[
\boxed{d(d\Phi)=0.}
\]

Therefore the source formula

\[
d(d\Phi)=\Omega\neq0
\]

cannot hold for an ordinary smooth scalar potential.

The correct object is a process 1-form that need not be exact.

## 2. Process 1-form

Let \(U\subset\mathbb R^2\) have coordinates \((P,S)\), and let

\[
T,V\in C^1(U).
\]

Define

\[
\boxed{
\alpha_H
=
T(P,S)\,dS+V(P,S)\,dP.
}
\]

Its curvature/nonclosure 2-form is

\[
\Omega_H=d\alpha_H.
\]

## Theorem 2.1 — Maxwell-defect curvature

One has

\[
\boxed{
\Omega_H
=
\left(
\frac{\partial T}{\partial P}
-
\frac{\partial V}{\partial S}
\right)
dP\wedge dS.
}
\]

### Proof

Compute

\[
d(T\,dS)=dT\wedge dS
=\frac{\partial T}{\partial P}\,dP\wedge dS,
\]

and

\[
d(V\,dP)=dV\wedge dP
=\frac{\partial V}{\partial S}\,dS\wedge dP
=
-\frac{\partial V}{\partial S}\,dP\wedge dS.
\]

Adding the terms gives the formula. ∎

## Corollary 2.2 — Exact enthalpy implies Maxwell flatness

If there exists \(H\in C^2(U)\) with

\[
dH=T\,dS+V\,dP,
\]

then

\[
\Omega_H=d(dH)=0
\]

and therefore

\[
\boxed{
\left(\frac{\partial T}{\partial P}\right)_S
=
\left(\frac{\partial V}{\partial S}\right)_P.
}
\]

## Corollary 2.3 — Local converse

On a simply connected chart, if

\[
\Omega_H=0,
\]

then \(\alpha_H\) is exact, so a local/global-on-chart enthalpy potential exists.

This is the ordinary Poincare-lemma direction under the declared chart
hypotheses.

## Recognition interpretation

The lawful chain is

```text
potential Phi
    => exact 1-form dPhi
    => d(dPhi)=0;

general process 1-form alpha
    => curvature/nonclosure d alpha
    => possible nonzero defect.
```

Curvature measures failure of a declared process form to be exact. It is not a
failure of the identity \(d^2=0\).

## Status

```text
d^2 = 0 FOR SMOOTH POTENTIALS       PROVED
SOURCE d(d Phi) != 0 CLAIM          REJECTED
PROCESS-FORM CURVATURE              PROVED
MAXWELL-DEFECT FORMULA              PROVED
EXACTNESS => MAXWELL RELATION       PROVED
SIMPLY-CONNECTED FLAT CONVERSE      PROVED
```
