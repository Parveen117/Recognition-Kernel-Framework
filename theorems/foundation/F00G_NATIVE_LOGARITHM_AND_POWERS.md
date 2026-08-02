# F00-G — Native Logarithm on the Positive Radial Cone and Native Powers

## Classification

`PROVED`

## Purpose

F00-E derives the native exponential

\[
\operatorname{Exp}_\Sigma:\mathbb C_\Sigma\to\mathbb C_\Sigma
\]

from finite factorial polynomials and cut-complex completion. F00-F proves that
its restriction to the radial line is strictly increasing and defines an inverse
only on the earned Euler orbit

\[
\mathbb P_\Sigma
=
\{\operatorname{Exp}_\Sigma(x):x\in\mathbb R_\Sigma\}.
\]

This theorem proves that every positive radial scalar belongs to that orbit. It
derives the logarithm without importing

```text
ordinary real logarithm;
an inverse-function theorem;
integration of 1/x;
the ordinary positive real line;
complex analysis;
a pre-existing power x^s.
```

The construction order is

```text
positive radial scalar
-> Cayley coordinate y=(x-1)/(x+1)
-> native odd power series
-> inverse identity with Exp_Sigma
-> full positive Euler orbit
-> multiplicative logarithm
-> native complex powers.
```

---

## 1. Established input

Let

\[
\mathbb C_\Sigma
=
\mathbb R_\Sigma\oplus\iota_\Sigma\mathbb R_\Sigma,
\qquad
\iota_\Sigma^2=-1,
\]

with dagger

\[
(a+\iota_\Sigma b)^\dagger=a-\iota_\Sigma b.
\]

The radial field `R_Sigma` is complete, Archimedean and ordered. The exponential
satisfies

\[
\operatorname{Exp}_\Sigma(z+w)
=
\operatorname{Exp}_\Sigma(z)
\operatorname{Exp}_\Sigma(w),
\]

\[
\partial_\Sigma\operatorname{Exp}_\Sigma
=
\operatorname{Exp}_\Sigma,
\qquad
\operatorname{Exp}_\Sigma(0)=1,
\]

and is strictly increasing on `R_Sigma`.

For radial `u`, write `|u|_Sigma` for the ordered absolute value.

---

## 2. The native Cayley coordinate

Let `x>0` be radial and define

\[
\boxed{
\mathcal C_\Sigma(x)
=
\frac{x-1}{x+1}.
}
\]

### Lemma 2.1 — Cayley contraction

For every radial `x>0`,

\[
\left|\mathcal C_\Sigma(x)\right|_\Sigma<1.
\]

### Proof

Because `x>0`,

\[
x+1>0.
\]

Also

\[
(x+1)^2-(x-1)^2=4x>0.
\]

Hence

\[
|x-1|_\Sigma<x+1.
\]

Division by the positive scalar `x+1` gives the result. ∎

The inverse rational transformation is

\[
\boxed{
x=\frac{1+y}{1-y}}
\]

whenever

\[
y=\mathcal C_\Sigma(x).
\]

Indeed,

\[
1+y=\frac{2x}{x+1},
\qquad
1-y=\frac{2}{x+1}.
\]

---

## 3. The native odd logarithm series

For radial `y` with `|y|_Sigma<1`, define finite odd polynomials

\[
A_{\Sigma,N}(y)
=
2\sum_{m=0}^{N}
\frac{y^{2m+1}}{2m+1}.
\]

### Lemma 3.1 — Native convergence

For every `|y|_Sigma<1`, the sequence `A_{Sigma,N}(y)` is Cauchy in
`R_Sigma`.

### Proof

Choose a radial rational `q` with

\[
|y|_\Sigma<q<1.
\]

For `M>N`,

\[
\begin{aligned}
|A_{\Sigma,M}(y)-A_{\Sigma,N}(y)|_\Sigma
&\le
2\sum_{m=N+1}^{M}
\frac{|y|_\Sigma^{2m+1}}{2m+1}\\
&\le
2\sum_{m=N+1}^{\infty}q^{2m+1}\\
&=
\frac{2q^{2N+3}}{1-q^2}.
\end{aligned}
\]

The last expression tends to zero by the native geometric-tail identity. ∎

### Definition 3.2 — Native odd logarithm coordinate

For `|y|_Sigma<1`, define

\[
\boxed{
\operatorname{Atanh}_\Sigma(y)
=
\sum_{m=0}^{\infty}
\frac{y^{2m+1}}{2m+1},
}
\]

and

\[
\boxed{
A_\Sigma(y)=2\operatorname{Atanh}_\Sigma(y).
}
\]

The name records the later classical shadow only. The definition is the native
odd power series above.

---

## 4. Difference rules used below

All rules in this section are derived from the cut-complex difference quotient.
They are not imported as real-calculus theorems.

### Lemma 4.1 — Product rule

If native derivatives of `f` and `g` exist at `y`, then

\[
\partial_\Sigma(fg)(y)
=
(\partial_\Sigma f)(y)g(y)
+f(y)(\partial_\Sigma g)(y).
\]

### Proof

Write

\[
\frac{f(y+h)g(y+h)-f(y)g(y)}{h}
=
\frac{f(y+h)-f(y)}{h}g(y+h)
+f(y)\frac{g(y+h)-g(y)}{h}.
\]

Pass to the native limit. ∎

### Lemma 4.2 — Inverse rule

If `g(y)` is nonzero and native differentiable, then

\[
\partial_\Sigma(g^{-1})(y)
=-g(y)^{-2}(\partial_\Sigma g)(y).
\]

### Proof

Apply the product rule to `g g^{-1}=1`. ∎

### Lemma 4.3 — Analytic chain rule

Let `F` be represented by a native convergent power series on a neighbourhood
of `g(y)`, and let `g` be native differentiable. Then

\[
\partial_\Sigma(F\circ g)(y)
=F'(g(y))\partial_\Sigma g(y).
\]

### Proof

The rule holds for every polynomial by induction using the product rule. On a
strictly smaller native neighbourhood, the power series and its formal
derivative have uniformly Cauchy tails. Pass the polynomial identity to the
native limit. ∎

### Lemma 4.4 — Derivative of the odd series

For `|y|_Sigma<1`,

\[
\boxed{
\partial_\Sigma A_\Sigma(y)
=
\frac{2}{1-y^2}.
}
\]

### Proof

On every closed native subinterval `|y|_Sigma<=q<1`, termwise differentiation
is justified by the geometric majorant. Thus

\[
\partial_\Sigma A_\Sigma(y)
=
2\sum_{m=0}^{\infty}y^{2m}
=
\frac{2}{1-y^2}.
\]

The last identity follows from the finite geometric identity followed by native
completion. ∎

---

## 5. Inversion of the native exponential

For `|y|_Sigma<1`, define

\[
G_\Sigma(y)
=
\operatorname{Exp}_\Sigma(A_\Sigma(y))
\frac{1-y}{1+y}.
\]

The factors `1-y` and `1+y` are positive and therefore invertible.

### Theorem 5.1 — Native Cayley–exponential identity

For every radial `|y|_Sigma<1`,

\[
\boxed{
\operatorname{Exp}_\Sigma(A_\Sigma(y))
=
\frac{1+y}{1-y}.
}
\]

### Proof

Using the native Euler equation, the chain rule, product rule and inverse rule,

\[
\begin{aligned}
\partial_\Sigma G_\Sigma(y)
&=
G_\Sigma(y)
\left(
\frac{2}{1-y^2}
-
\frac{1}{1-y}
-
\frac{1}{1+y}
\right)\\
&=0.
\end{aligned}
\]

The expression in parentheses is zero after passage to the common denominator
`1-y^2`.

It remains to justify that a native analytic function with zero derivative on
the interval `(-1,1)_Sigma` is constant. Around every point it has a convergent
power series. Vanishing of the derivative forces every positive-degree
coefficient to vanish. Overlapping neighbourhoods propagate the same constant
through the connected ordered interval.

At `y=0`,

\[
A_\Sigma(0)=0,
\qquad
G_\Sigma(0)=1.
\]

Hence `G_Sigma(y)=1`, proving the identity. ∎

---

## 6. Full positive logarithm

### Definition 6.1 — Native positive logarithm

For every radial `x>0`, define

\[
\boxed{
\operatorname{Log}_\Sigma^+(x)
=
2\sum_{m=0}^{\infty}
\frac{1}{2m+1}
\left(
\frac{x-1}{x+1}
\right)^{2m+1}.
}
\]

The series is lawful by Lemma 2.1 and Lemma 3.1.

### Theorem 6.2 — Exact inverse identities

For every radial `x>0`,

\[
\boxed{
\operatorname{Exp}_\Sigma
(\operatorname{Log}_\Sigma^+(x))
=x.
}
\]

For every radial `u`,

\[
\boxed{
\operatorname{Log}_\Sigma^+
(\operatorname{Exp}_\Sigma(u))
=u.
}
\]

### Proof

Put

\[
y=\frac{x-1}{x+1}.
\]

Theorem 5.1 gives

\[
\operatorname{Exp}_\Sigma
(\operatorname{Log}_\Sigma^+(x))
=
\frac{1+y}{1-y}
=x.
\]

For the second identity, apply the first identity with
`x=Exp_Sigma(u)`. Both `u` and `Log_Sigma^+(Exp_Sigma(u))` are radial and have
the same exponential. Strict radial injectivity of `Exp_Sigma` gives equality.
∎

### Corollary 6.3 — Full positive Euler orbit

\[
\boxed{
\mathbb P_\Sigma
=
\mathbb R_{\Sigma,>0}.
}
\]

Thus the logarithm introduced in F00-F on `P_Sigma` extends to the whole
positive radial cone and agrees with `Log_Sigma^+`.

From now on write simply

\[
\operatorname{Log}_\Sigma(x)
\]

for `x>0`.

---

## 7. Logarithmic laws

### Theorem 7.1 — Multiplicative-to-additive law

For radial `x,y>0`,

\[
\boxed{
\operatorname{Log}_\Sigma(xy)
=
\operatorname{Log}_\Sigma(x)
+
\operatorname{Log}_\Sigma(y).
}
\]

### Proof

The exponential addition law gives

\[
\operatorname{Exp}_\Sigma
(\operatorname{Log}_\Sigma(x)+
 \operatorname{Log}_\Sigma(y))
=xy.
\]

Apply the radial inverse identity. ∎

### Corollary 7.2

For radial `x>0` and integers `n`,

\[
\operatorname{Log}_\Sigma(x^n)
=n\operatorname{Log}_\Sigma(x).
\]

Also

\[
\operatorname{Log}_\Sigma(1)=0,
\qquad
\operatorname{Log}_\Sigma(x^{-1})
=-\operatorname{Log}_\Sigma(x).
\]

### Theorem 7.3 — Native derivative

For radial `x>0`,

\[
\boxed{
\partial_\Sigma\operatorname{Log}_\Sigma(x)
=x^{-1}.
}
\]

### Proof

Put

\[
y(x)=\frac{x-1}{x+1}.
\]

The quotient rule gives

\[
y'(x)=\frac{2}{(x+1)^2}.
\]

Moreover,

\[
1-y(x)^2
=
\frac{4x}{(x+1)^2}.
\]

Apply Lemma 4.4 and the chain rule:

\[
\partial_\Sigma\operatorname{Log}_\Sigma(x)
=
\frac{2}{1-y^2}
\frac{2}{(x+1)^2}
=
\frac1x.
\]

∎

### Theorem 7.4 — Strict order preservation

For radial `x,y>0`,

\[
x<y
\quad\Longleftrightarrow\quad
\operatorname{Log}_\Sigma(x)
<
\operatorname{Log}_\Sigma(y).
\]

### Proof

This follows because `Log_Sigma` is the inverse of the strictly increasing
radial exponential. ∎

---

## 8. Native complex powers

### Definition 8.1 — Native power

For radial `x>0` and `z in C_Sigma`, define

\[
\boxed{
x^z_\Sigma
=
\operatorname{Exp}_\Sigma
(z\operatorname{Log}_\Sigma(x)).
}
\]

The subscript is omitted when no confusion is possible.

### Theorem 8.2 — Exponent laws

For radial `x,y>0` and `z,w in C_Sigma`,

\[
\boxed{x^{z+w}=x^zx^w,}
\]

\[
\boxed{(xy)^z=x^zy^z,}
\]

\[
\boxed{(x^z)^\dagger=x^{z^\dagger},}
\]

and for every integer `n`,

\[
\boxed{x^n=x\cdots x}
\]

with the ordinary repeated-product interpretation.

### Proof

Use the addition law for `Exp_Sigma`, the logarithmic product law, dagger
covariance, and `Log_Sigma(x^n)=nLog_Sigma(x)`. ∎

### Theorem 8.3 — Exponent derivative

For fixed `x>0`,

\[
\boxed{
\partial_\Sigma^z x^z
=
\operatorname{Log}_\Sigma(x)x^z.
}
\]

For fixed `z`, differentiation in the positive radial variable gives

\[
\boxed{
\partial_\Sigma^x x^z
=z x^{z-1}.
}
\]

### Proof

Apply the chain rule to the defining exponential and use
`partial Log_Sigma(x)=1/x`. ∎

### Corollary 8.4 — Native modulus law

Write

\[
z=\sigma+\iota_\Sigma\tau.
\]

Then

\[
(x^z)^\dagger x^z
=x^{2\sigma}.
\]

Thus the radial magnitude of `x^{-z}` is controlled entirely by
`x^{-sigma}`.

---

## 9. Positive integers and prime logarithms

The natural number `n` is the radial scalar obtained by adding the unit `n`
times. Every `n>=1` is positive, so

\[
\operatorname{Log}_\Sigma(n)
\]

and

\[
n^{-s}_\Sigma
=
\operatorname{Exp}_\Sigma
(-s\operatorname{Log}_\Sigma(n))
\]

are now native objects for every `s in C_Sigma`.

For positive integers `m,n`,

\[
\operatorname{Log}_\Sigma(mn)
=
\operatorname{Log}_\Sigma(m)
+
\operatorname{Log}_\Sigma(n),
\]

and therefore

\[
(mn)^{-s}=m^{-s}n^{-s}.
\]

This is the arithmetic multiplicativity required for the native Dirichlet zeta
construction.

---

## 10. Coordinate shadow

Under a later scalar chart

\[
\kappa:\mathbb C_\Sigma\to\mathbb C
\]

that preserves cut-complex addition, multiplication, dagger, order and the
factorial exponential,

\[
\kappa(\operatorname{Exp}_\Sigma z)=e^{\kappa(z)}.
\]

The inverse identity forces

\[
\kappa(\operatorname{Log}_\Sigma x)=\log\kappa(x)
\]

for positive radial `x`, and

\[
\kappa(x^z_\Sigma)=
\kappa(x)^{\kappa(z)}
\]

with the positive-real branch.

These are coordinate consequences, not definitions.

---

## 11. Claim boundary

Proved here:

```text
Cayley contraction for every positive radial scalar;
convergence of the native odd logarithm series;
native product, inverse and analytic chain rules used in the proof;
Exp_Sigma(2 Atanh_Sigma y)=(1+y)/(1-y);
Log_Sigma on the entire positive radial cone;
Exp_Sigma and Log_Sigma are inverse order isomorphisms;
P_Sigma=R_{Sigma,>0};
Log_Sigma(xy)=Log_Sigma(x)+Log_Sigma(y);
partial Log_Sigma(x)=1/x;
native complex powers x^z;
exponent laws and modulus law;
native logarithms and powers of every positive integer.
```

Not proved here:

```text
unique factorization of native natural numbers;
Dirichlet-series convergence;
Euler product;
analytic continuation;
Gamma or theta functions;
Poisson summation;
completed zeta functional equation;
explicit formula;
Weil criterion;
K0>=0;
RH.
```

No classical logarithm or inverse-function theorem is consumed. No separate
certificate is created at this algebraic-analytic foundation stage. The later
native zeta and completed-zeta promotion audits will consume the load-bearing
identities proved here.
