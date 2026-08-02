# F00-I — Native Dirichlet Zeta, Euler Product and von Mangoldt Derivative

## Classification

`PROVED` on the native half-plane

\[
\operatorname{Re}_\Sigma(s)>1.
\]

## Purpose

F00-G derives the native logarithm and powers of every positive natural scalar.
F00-H derives native primes, unique factorization, the Möbius function and the
von Mangoldt weight.

This theorem constructs the zeta function in its initial domain without
importing

```text
the classical Riemann zeta function;
the ordinary p-series or integral test;
the classical Euler product;
ordinary complex logarithms;
Weierstrass convergence theorems;
the classical von Mangoldt logarithmic derivative.
```

The construction order is

```text
native powers n^{-s}
-> dyadic convergence
-> native differentiability
-> native Dirichlet convolution products
-> finite prime Euler products
-> infinite Euler product
-> nonvanishing
-> Möbius reciprocal
-> von Mangoldt logarithmic derivative.
```

---

## 1. Native half-plane and powers

For

\[
s=\sigma+\iota_\Sigma\tau\in\mathbb C_\Sigma,
\]

define

\[
\operatorname{Re}_\Sigma(s)
=\frac{s+s^\dagger}{2}=\sigma.
\]

For every positive natural `n`, F00-G defines

\[
\boxed{
n^{-s}_\Sigma
=
\operatorname{Exp}_\Sigma
\bigl(-s\operatorname{Log}_\Sigma(n)\bigr).
}
\]

The subscript is suppressed below.

### Lemma 1.1 — Native magnitude of a Dirichlet atom

For `s=sigma+iota_Sigma tau`,

\[
\boxed{
(n^{-s})^\dagger n^{-s}=n^{-2\sigma}.
}
\]

Hence

\[
|n^{-s}|_\Sigma=n^{-\sigma}.
\]

### Proof

Dagger covariance and the exponential addition law give

\[
\begin{aligned}
(n^{-s})^\dagger n^{-s}
&=
\operatorname{Exp}_\Sigma
(-s^\dagger\operatorname{Log}_\Sigma n)
\operatorname{Exp}_\Sigma
(-s\operatorname{Log}_\Sigma n)\\
&=
\operatorname{Exp}_\Sigma
(-(s+s^\dagger)\operatorname{Log}_\Sigma n)\\
&=n^{-2\sigma}.
\end{aligned}
\]

The positive square root is `n^{-sigma}`. ∎

### Lemma 1.2 — Multiplicativity

For positive naturals `m,n`,

\[
\boxed{(mn)^{-s}=m^{-s}n^{-s}.}
\]

### Proof

Use

\[
\operatorname{Log}_\Sigma(mn)
=
\operatorname{Log}_\Sigma(m)+
\operatorname{Log}_\Sigma(n)
\]

and the exponential addition law. ∎

---

## 2. Dyadic convergence

For `k>=0`, let the native dyadic block be

\[
D_k=\{n\in\mathbb N_\Sigma:2^k\le n<2^{k+1}\}.
\]

It contains exactly `2^k` natural scalars.

### Lemma 2.1 — Dyadic block estimate

If `sigma=Re_Sigma(s)>1`, then

\[
\boxed{
\sum_{n\in D_k}|n^{-s}|_\Sigma
\le
2^{-k(\sigma-1)}.
}
\]

### Proof

For `n in D_k`, monotonicity of the logarithm and negative radial exponent give

\[
n^{-\sigma}\le(2^k)^{-\sigma}=2^{-k\sigma}.
\]

There are `2^k` terms. ∎

### Theorem 2.2 — Native Dirichlet convergence

For every `s` with

\[
\operatorname{Re}_\Sigma(s)>1,
\]

the partial sums

\[
Z_{\Sigma,N}(s)=\sum_{n=1}^{N}n^{-s}
\]

are Cauchy in `C_Sigma`.

### Proof

Choose radial `delta>0` such that

\[
\operatorname{Re}_\Sigma(s)\ge1+\delta.
\]

Every tail beginning beyond `2^K` is bounded by

\[
\sum_{k=K}^{\infty}2^{-k\delta},
\]

which is a native convergent geometric tail. ∎

### Definition 2.3 — Native Dirichlet zeta

For `Re_Sigma(s)>1`, define

\[
\boxed{
\zeta_\Sigma(s)
=
\sum_{n=1}^{\infty}n^{-s}.
}
\]

This is the first definition of zeta in RH-Framework. No classical zeta
function is referenced.

### Corollary 2.4 — Uniform half-plane tails

For every radial `delta>0`, convergence is uniform in the native magnitude on

\[
\operatorname{Re}_\Sigma(s)\ge1+\delta.
\]

Indeed,

\[
\sup_{\operatorname{Re}_\Sigma(s)\ge1+\delta}
\left|
\sum_{n\ge2^K}n^{-s}
\right|_\Sigma
\le
\frac{2^{-K\delta}}{1-2^{-\delta}}.
\]

---

## 3. Logarithmic moment convergence

### Lemma 3.1 — Dyadic logarithm bound

For `n in D_k`,

\[
\operatorname{Log}_\Sigma(n)
\le
(k+1)\operatorname{Log}_\Sigma(2).
\]

### Proof

Because `n<2^{k+1}`, strict monotonicity and the logarithmic power law give the
result. ∎

### Lemma 3.2 — Polynomial-geometric convergence

For every radial `0<q<1` and every fixed natural `r`,

\[
\sum_{k=0}^{\infty}(k+1)^r q^k
\]

converges in `R_Sigma`.

### Proof

Choose a native rational `q<rho<1`. For sufficiently large `k`,

\[
(k+2)^r q^{k+1}
\le
\rho (k+1)^r q^k.
\]

This follows because

\[
q\left(1+\frac1{k+1}\right)^r
\longrightarrow q<\rho
\]

by finite binomial expansion and the Archimedean order. The tail is then
bounded by a geometric series of ratio `rho`. ∎

### Theorem 3.3 — Native logarithmic moment series

For every fixed natural `r>=0`,

\[
\sum_{n=1}^{\infty}
\operatorname{Log}_\Sigma(n)^r n^{-s}
\]

converges absolutely and uniformly on every half-plane

\[
\operatorname{Re}_\Sigma(s)\ge1+\delta.
\]

### Proof

On `D_k`, the absolute block sum is bounded by

\[
(k+1)^r
\operatorname{Log}_\Sigma(2)^r
2^{-k\delta}.
\]

Apply Lemma 3.2. ∎

---

## 4. Native differentiability of zeta

For each natural `n`,

\[
\partial_\Sigma n^{-s}
=-\operatorname{Log}_\Sigma(n)n^{-s}.
\]

This follows from the native Euler equation and chain rule.

### Theorem 4.1 — Native zeta derivative

On `Re_Sigma(s)>1`, the native derivative exists and

\[
\boxed{
\zeta_\Sigma'(s)
=-
\sum_{n=1}^{\infty}
\operatorname{Log}_\Sigma(n)n^{-s}.
}
\]

### Proof

Fix `s_0` with

\[
\operatorname{Re}_\Sigma(s_0)>1.
\]

Choose `delta>0` so that

\[
\operatorname{Re}_\Sigma(s_0)
\ge1+2\delta.
\]

For native `h` with `|h|_Sigma<delta`,

\[
\frac{n^{-(s_0+h)}-n^{-s_0}}{h}
=
n^{-s_0}
\frac{
\operatorname{Exp}_\Sigma(-h\operatorname{Log}_\Sigma n)-1
}{h}.
\]

Subtract

\[
-\operatorname{Log}_\Sigma(n)n^{-s_0}.
\]

The factorial-tail estimate for `Exp_Sigma` bounds the remainder by

\[
|h|_\Sigma
\operatorname{Log}_\Sigma(n)^2
n^{-(1+\delta)}
\operatorname{Exp}_\Sigma
(|h|_\Sigma\operatorname{Log}_\Sigma n).
\]

Since

\[
\operatorname{Exp}_\Sigma
(|h|_\Sigma\operatorname{Log}_\Sigma n)
=n^{|h|_\Sigma}
\le n^\delta,
\]

the remainder is bounded by

\[
|h|_\Sigma
\operatorname{Log}_\Sigma(n)^2
n^{-(1+\delta)}.
\]

The majorant series converges by Theorem 3.3. Summing the remainder and then
letting `h->0` proves the displayed derivative formula directly. No imported
uniform-limit differentiation theorem is used. ∎

Repeated use of the same argument gives

\[
\boxed{
\zeta_\Sigma^{(r)}(s)
=(-1)^r
\sum_{n=1}^{\infty}
\operatorname{Log}_\Sigma(n)^r n^{-s}
}
\]

for every finite natural `r`.

---

## 5. Infinitude of native primes

### Theorem 5.1 — Native Euclid theorem

There are infinitely many native primes.

### Proof

Suppose the complete prime set were finite:

\[
p_1,\ldots,p_m.
\]

Put

\[
N=p_1p_2\cdots p_m+1.
\]

Then `N>1`, so F00-H gives a prime divisor `q|N`. By completeness of the list,
`q=p_j` for some `j`. But `p_j` divides the product and also `N`, so it divides

\[
N-p_1\cdots p_m=1,
\]

contradicting `p_j>1`. ∎

The native primes may therefore be listed increasingly as

\[
p_1<p_2<p_3<\cdots
\]

using the least-element property of the natural order.

---

## 6. Native Dirichlet convolution series

Let `a,b` be native arithmetic functions. Suppose

\[
\sum_{n\ge1}|a(n)|_\Sigma n^{-\sigma}
\]

and

\[
\sum_{n\ge1}|b(n)|_\Sigma n^{-\sigma}
\]

converge for some radial `sigma>1`.

Define finite divisor convolution

\[
(a*b)(n)
=
\sum_{d|n}a(d)b(n/d).
\]

### Theorem 6.1 — Native Dirichlet multiplication

For `Re_Sigma(s)>=sigma`,

\[
\boxed{
\left(
\sum_{m\ge1}a(m)m^{-s}
\right)
\left(
\sum_{n\ge1}b(n)n^{-s}
\right)
=
\sum_{k\ge1}(a*b)(k)k^{-s}.
}
\]

### Proof

For finite rectangles of indices, distributivity and

\[
(mn)^{-s}=m^{-s}n^{-s}
\]

give the identity after grouping by `k=mn`.

The unrestricted double tail is bounded by the product of the two absolute
series tails. Hence the finite identities pass to the native Cauchy limit.
Every coefficient group for fixed `k` is finite because the divisor set is
finite. ∎

---

## 7. Finite Euler products

For a native prime `p` and `Re_Sigma(s)>1`,

\[
|p^{-s}|_\Sigma=p^{-\sigma}<1.
\]

Thus the native geometric identity gives

\[
\boxed{
(1-p^{-s})^{-1}
=
\sum_{j=0}^{\infty}p^{-js}.
}
\]

For the first `m` primes, define

\[
Q_m(s)
=
\prod_{j=1}^{m}(1-p_j^{-s})^{-1}.
\]

### Theorem 7.1 — Finite prime-factor expansion

\[
\boxed{
Q_m(s)
=
\sum_{\substack{n\ge1\\
\nu_n(p)=0\text{ for }p>p_m}}
n^{-s}.
}
\]

### Proof

Expand the finite product of geometric series. A term is specified by one
nonnegative exponent for each prime `p_1,...,p_m`, hence by the natural

\[
n=p_1^{a_1}\cdots p_m^{a_m}.
\]

Unique factorization from F00-H makes this correspondence bijective. Absolute
convergence of the finite product of geometric series permits the finite-stage
Cauchy limit in each exponent. ∎

---

## 8. Infinite Euler product

### Theorem 8.1 — Native Euler product

For every `s` with `Re_Sigma(s)>1`,

\[
\boxed{
\zeta_\Sigma(s)
=
\prod_{p\in\mathcal P_\Sigma}
(1-p^{-s})^{-1}.
}
\]

The product means the native limit of `Q_m(s)`.

### Proof

The finite expansion contains exactly those natural numbers whose prime factors
are at most `p_m`. Every omitted natural has a prime factor greater than `p_m`
and is therefore itself greater than `p_m`.

Hence

\[
|\zeta_\Sigma(s)-Q_m(s)|_\Sigma
\le
\sum_{n>p_m}n^{-\sigma}.
\]

The native Dirichlet tail tends to zero by Theorem 2.2. ∎

The convergence is uniform on every native half-plane

\[
\operatorname{Re}_\Sigma(s)\ge1+\delta.
\]

---

## 9. Native nonvanishing

Define the finite inverse products

\[
P_m(s)=\prod_{j=1}^{m}(1-p_j^{-s}).
\]

### Lemma 9.1 — Product-tail estimate

For native scalars `a_j`,

\[
\left|
\prod_{j=r}^{m}(1-a_j)-1
\right|_\Sigma
\le
\operatorname{Exp}_\Sigma
\left(
\sum_{j=r}^{m}|a_j|_\Sigma
\right)-1.
\]

### Proof

Expand the finite product. The absolute sum of all nonconstant monomials is at
most

\[
\prod_{j=r}^{m}(1+|a_j|_\Sigma)-1.
\]

For positive radial `u`, the factorial exponential satisfies

\[
1+u\le\operatorname{Exp}_\Sigma(u).
\]

Therefore

\[
\prod_{j=r}^{m}(1+|a_j|_\Sigma)
\le
\operatorname{Exp}_\Sigma
\left(
\sum_{j=r}^{m}|a_j|_\Sigma
\right).
\]

∎

### Theorem 9.2 — Native zero-free half-plane

For `Re_Sigma(s)>1`,

\[
\boxed{
\zeta_\Sigma(s)\ne0.
}
\]

### Proof

Because

\[
\sum_p|p^{-s}|_\Sigma
\le
\sum_{n\ge2}n^{-\sigma}<\infty,
\]

Lemma 9.1 shows that `P_m(s)` is Cauchy. Let its limit be `P(s)`.

For every `m`,

\[
P_m(s)Q_m(s)=1.
\]

Theorem 8.1 gives `Q_m(s)->zeta_Sigma(s)`. Continuity of multiplication in the
completed cut field gives

\[
P(s)\zeta_\Sigma(s)=1.
\]

Thus `zeta_Sigma(s)` is invertible and nonzero. ∎

---

## 10. Möbius reciprocal

Because

\[
|\mu_\Sigma(n)|_\Sigma\le1,
\]

the series

\[
M_\Sigma(s)
=
\sum_{n=1}^{\infty}
\mu_\Sigma(n)n^{-s}
\]

converges absolutely for `Re_Sigma(s)>1`.

### Theorem 10.1 — Native reciprocal series

\[
\boxed{
\frac{1}{\zeta_\Sigma(s)}
=
\sum_{n=1}^{\infty}
\mu_\Sigma(n)n^{-s}.
}
\]

### Proof

Apply native Dirichlet multiplication to the constant arithmetic function
`1(n)=1` and `mu_Sigma`. F00-H proves

\[
(1*\mu_\Sigma)(n)
=
\begin{cases}
1,&n=1,\\
0,&n>1.
\end{cases}
\]

Therefore

\[
\zeta_\Sigma(s)M_\Sigma(s)=1.
\]

Use Theorem 9.2. ∎

---

## 11. Native von Mangoldt series

The series

\[
A_\Sigma(s)
=
\sum_{n=1}^{\infty}
\Lambda_\Sigma(n)n^{-s}
\]

converges absolutely for `Re_Sigma(s)>1` because

\[
0\le\Lambda_\Sigma(n)
\le\operatorname{Log}_\Sigma(n)
\]

and Theorem 3.3 applies.

### Theorem 11.1 — Native logarithmic derivative

For `Re_Sigma(s)>1`,

\[
\boxed{
-
\frac{\zeta_\Sigma'(s)}{\zeta_\Sigma(s)}
=
\sum_{n=1}^{\infty}
\Lambda_\Sigma(n)n^{-s}.
}
\]

### Proof

F00-H gives the finite divisor identity

\[
\operatorname{Log}_\Sigma(n)
=
\sum_{d|n}\Lambda_\Sigma(d).
\]

Native Dirichlet multiplication therefore yields

\[
\begin{aligned}
\zeta_\Sigma(s)A_\Sigma(s)
&=
\sum_{n=1}^{\infty}
\left(
\sum_{d|n}\Lambda_\Sigma(d)
\right)n^{-s}\\
&=
\sum_{n=1}^{\infty}
\operatorname{Log}_\Sigma(n)n^{-s}\\
&=-\zeta_\Sigma'(s).
\end{aligned}
\]

Multiply by the native inverse of `zeta_Sigma(s)` from Theorem 9.2. ∎

### Corollary 11.2 — Prime-power expansion

\[
\boxed{
-
\frac{\zeta_\Sigma'(s)}{\zeta_\Sigma(s)}
=
\sum_{p\in\mathcal P_\Sigma}
\sum_{k=1}^{\infty}
\operatorname{Log}_\Sigma(p)p^{-ks}.
}
\]

### Proof

By definition `Lambda_Sigma(n)` is nonzero exactly on prime powers, where its
value is `Log_Sigma(p)`. Unique factorization makes the indexing disjoint. ∎

This is the native arithmetic source later used by the prime-Euler translation
operator.

---

## 12. Finite clock and prime-exponent chart

Define the native logarithmic clock on the finite arithmetic span by

\[
H_{\log,\Sigma}e_n
=
\operatorname{Log}_\Sigma(n)e_n.
\]

The prime-exponent vector from F00-H satisfies

\[
\operatorname{Log}_\Sigma(n)
=
\sum_p\nu_n(p)\operatorname{Log}_\Sigma(p).
\]

Thus any later prime-torus or multicircle chart is forced to carry the native
clock to the weighted prime generator. It is a representation of this arithmetic
identity, not the source of zeta.

For `Re_Sigma(s)>1`, the native formal trace on the arithmetic basis is

\[
\sum_{n\ge1}
\operatorname{Exp}_\Sigma
(-sH_{\log,\Sigma})_{nn}
=
\zeta_\Sigma(s).
\]

Operator trace-class language is postponed until the native operator bridge is
applied.

---

## 13. Coordinate shadow

Under a later faithful scalar chart preserving the cut exponential, logarithm
and natural unit,

\[
\kappa(\zeta_\Sigma(s))
=
\sum_{n=1}^{\infty}n^{-\kappa(s)}
\]

for `Re kappa(s)>1`. The native Euler product, Möbius reciprocal and von
Mangoldt derivative map to the familiar coordinate identities.

The coordinate function is therefore a shadow of `zeta_Sigma`; it is not an
input to its construction.

---

## 14. Claim boundary

Proved here on `Re_Sigma(s)>1`:

```text
native convergence of sum n^{-s};
uniform dyadic tail bounds;
native differentiability and all finite derivatives;
infinitude of native primes;
Dirichlet-series multiplication under absolute convergence;
finite prime-factor Euler expansions;
infinite Euler product;
zero-free half-plane;
Möbius reciprocal series;
von Mangoldt logarithmic derivative;
prime-power expansion;
native arithmetic logarithmic clock.
```

Not proved here:

```text
continuation beyond Re_Sigma(s)>1;
a pole at s=1;
Gamma factor;
pi_Sigma;
Gaussian Fourier self-duality;
Poisson summation;
theta inversion;
functional equation;
completed xi_Sigma;
zero-sum explicit formula;
Weil criterion;
K0>=0;
RH.
```

No classical zeta theorem, Euler product, p-series test or analytic continuation
is consumed. Continuation begins only after the native Fourier–Gaussian–Poisson
chain is derived.
