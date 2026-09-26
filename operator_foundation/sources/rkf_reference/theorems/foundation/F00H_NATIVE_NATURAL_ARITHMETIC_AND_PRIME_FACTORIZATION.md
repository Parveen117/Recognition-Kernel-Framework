# F00-H — Native Natural Arithmetic and Prime Factorization

## Classification

`PROVED`

## Purpose

F00-G defines `Log_Sigma(n)` and `n^s` for every positive natural scalar. The
Euler product for native zeta additionally requires a unique prime decomposition
of the natural multiplicative semigroup.

This theorem derives that decomposition inside the repeated-unit subsemiring of
the ordered radial cut field. It does not cite

```text
the ordinary fundamental theorem of arithmetic;
Euclid's lemma;
Bezout's theorem;
the Euclidean algorithm;
ordinary integer factorization.
```

Each required statement is reconstructed below from finite induction, ordered
addition and multiplication.

---

## 1. Native natural scalars

Let `1_Sigma` be the multiplicative unit of `R_Sigma`. Define

\[
0_\Sigma=0,
\qquad
n_\Sigma=\underbrace{1_\Sigma+\cdots+1_\Sigma}_{n\text{ terms}}
\]

for an external finite counting index `n`. The set

\[
\mathbb N_\Sigma
=
\{0_\Sigma,1_\Sigma,2_\Sigma,\ldots\}
\]

is the native natural subsemiring.

Because `R_Sigma` is ordered and has characteristic zero,

\[
m_\Sigma<n_\Sigma
\quad\Longleftrightarrow\quad
m<n
\]

at the finite counting level. We suppress the subscript when no confusion is
possible.

The induction principle used below is the defining recursive principle of this
repeated-unit construction:

```text
P(0) and [P(n) implies P(n+1)]
=> P(n) for every native natural n.
```

Strong induction follows by applying ordinary induction to the finite statement
that `P(k)` holds for every `k<=n`.

---

## 2. Divisibility

For `a,b in N_Sigma`, say

\[
a\mid b
\]

when there exists `c in N_Sigma` such that

\[
b=ac.
\]

A positive natural `u` is a unit in `N_Sigma` exactly when `u=1`.

### Lemma 2.1 — Cancellation

If `a>0` and

\[
ab=ac,
\]

then

\[
b=c.
\]

### Proof

The equality holds in the ambient field `R_Sigma`, where nonzero `a` has an
inverse. Multiply by `a^{-1}`. ∎

### Lemma 2.2 — Finiteness below a natural

For every `a in N_Sigma`, the set

\[
\{n\in\mathbb N_\Sigma:n\le a\}
\]

contains exactly the finite repeated-unit elements

\[
0,1,\ldots,a.
\]

In particular, every nonempty subset of this interval has a least and a greatest
element.

### Proof

This is immediate from the recursive construction and finite induction. No
completeness or choice principle is required. ∎

---

## 3. Division with remainder

### Theorem 3.1 — Native division algorithm

Let `a,b in N_Sigma` with `b>0`. There exist unique natural scalars `q,r` such
that

\[
\boxed{
a=qb+r,
\qquad
0\le r<b.
}
\]

### Proof: existence

Consider

\[
S=\{k\in\mathbb N_\Sigma:kb\le a\}.
\]

The set is nonempty because `0 in S`. Also `k<=a` for every `k in S`, since
`b>=1` gives `k<=kb<=a`. Hence `S` is a finite subset of `[0,a]` and has a
greatest element `q`.

Put

\[
r=a-qb.
\]

Then `r>=0`. If `r>=b`, then

\[
(q+1)b=qb+b\le a,
\]

contradicting maximality of `q`. Thus `r<b`.

### Proof: uniqueness

Suppose

\[
a=qb+r=q'b+r',
\qquad
0\le r,r'<b.
\]

If `q>q'`, then `q>=q'+1`, so

\[
r'=a-q'b=(q-q')b+r\ge b,
\]

contradicting `r'<b`. Similarly `q'<q` is impossible. Hence `q=q'`, and then
`r=r'`. ∎

The theorem defines native quotient and remainder operations

\[
q=\operatorname{quo}_b(a),
\qquad
r=\operatorname{rem}_b(a).
\]

---

## 4. Greatest common divisors

For positive `a,b`, a common divisor is `d` with `d|a` and `d|b`.

### Definition 4.1

The native greatest common divisor `gcd_Sigma(a,b)` is the greatest common
divisor in the natural order.

It exists because every common divisor is at most `min(a,b)` and the set of
common divisors is a nonempty finite set containing `1`.

### Lemma 4.2 — Remainder invariance

If

\[
a=qb+r,
\]

then the common divisors of `(a,b)` are exactly the common divisors of `(b,r)`.
Consequently

\[
\boxed{
\gcd_\Sigma(a,b)=\gcd_\Sigma(b,r).
}
\]

### Proof

If `d|a` and `d|b`, then `d|(a-qb)=r`. Conversely, if `d|b` and `d|r`, then
`d|(qb+r)=a`. ∎

### Theorem 4.3 — Native Euclidean algorithm

Repeated division

\[
a=q_0b+r_0,
\]

\[
b=q_1r_0+r_1,
\]

and so on terminates at a final nonzero remainder `r_k`, and

\[
\boxed{
\gcd_\Sigma(a,b)=r_k.
}
\]

### Proof

The positive remainders form a strictly decreasing sequence

\[
b>r_0>r_1>\cdots>0.
\]

No infinite strictly decreasing sequence of native naturals exists: after at
most `b` decreases the sequence must stop. Remainder invariance propagates the
gcd to the last nonzero remainder. ∎

---

## 5. Native Bezout identity

### Theorem 5.1 — Bezout representation

For positive naturals `a,b`, there exist native integers `u,v` in the signed
repeated-unit ring

\[
\mathbb Z_\Sigma
=
\mathbb N_\Sigma-\mathbb N_\Sigma
\]

such that

\[
\boxed{
\gcd_\Sigma(a,b)=ua+vb.
}
\]

### Proof

Every remainder in the Euclidean algorithm is an integer-linear combination of
`a` and `b`.

The first remainder is

\[
r_0=a-q_0b.
\]

If

\[
r_{j-1}=u_{j-1}a+v_{j-1}b,
\qquad
r_j=u_ja+v_jb,
\]

then

\[
r_{j+1}=r_{j-1}-q_{j+1}r_j
\]

is also such a combination. Induction reaches the last nonzero remainder, which
is the gcd by Theorem 4.3. ∎

### Corollary 5.2 — Coprime inverse relation

If

\[
\gcd_\Sigma(a,b)=1,
\]

then there exist `u,v in Z_Sigma` with

\[
ua+vb=1.
\]

---

## 6. Native primes

### Definition 6.1

A natural scalar `p>1` is **native prime** when its only positive natural
divisors are `1` and `p`.

A natural `n>1` that is not prime is **composite**.

### Lemma 6.2 — Composite splitting

If `n>1` is composite, then

\[
n=ab
\]

for naturals `a,b` satisfying

\[
1<a<n,
\qquad
1<b<n.
\]

### Proof

A nontrivial divisor `a` obeys `1<a<n`. Write `n=ab`. Since `a>1`, cancellation
and order give `b<n`; since `a<n`, one also has `b>1`. ∎

### Theorem 6.3 — Native Euclid lemma

If `p` is native prime and

\[
p\mid ab,
\]

then

\[
\boxed{p\mid a\quad\text{or}\quad p\mid b.}
\]

### Proof

If `p|a`, there is nothing to prove. Suppose `p` does not divide `a`.

Every common divisor of `p` and `a` divides `p`; since `p` is prime and does not
divide `a`, the gcd is `1`. Bezout gives

\[
up+va=1.
\]

Multiply by `b`:

\[
ubp+vab=b.
\]

The first term is divisible by `p`, and the second is divisible by `p` because
`p|ab`. Therefore `p|b`. ∎

### Corollary 6.4 — Prime divides a finite product

If

\[
p\mid a_1a_2\cdots a_m,
\]

then `p` divides at least one factor.

### Proof

Induct on `m` using Theorem 6.3. ∎

---

## 7. Existence of prime factorization

### Theorem 7.1 — Native prime-factor existence

Every natural scalar `n>1` is a finite product of native primes.

### Proof

Use strong induction on `n`.

If `n` is prime, the one-factor product suffices. If `n` is composite, Lemma 6.2
gives

\[
n=ab
\]

with `1<a,b<n`. By the induction hypothesis, both `a` and `b` are finite prime
products. Concatenating those products gives a prime factorization of `n`. ∎

The proof terminates because every composite split strictly decreases both
factors in the native natural order.

---

## 8. Uniqueness of prime factorization

### Theorem 8.1 — Native fundamental theorem of arithmetic

Suppose

\[
n=p_1p_2\cdots p_r
=q_1q_2\cdots q_s,
\]

where all `p_i` and `q_j` are native primes. Then

\[
r=s
\]

and, after a permutation,

\[
p_i=q_i
\qquad(1\le i\le r).
\]

### Proof

The prime `p_1` divides the product `q_1\cdots q_s`. By Corollary 6.4 it divides
some `q_j`. Since `q_j` is prime and `p_1>1`, the only possibility is

\[
p_1=q_j.
\]

Reorder the `q` factors and cancel this common nonzero factor. Repeat by finite
induction. Every factor on one side is matched with exactly one factor on the
other, so the lengths agree. ∎

### Corollary 8.2 — Exponent-vector form

For every `n>=1`, there is a unique finitely supported function

\[
\nu_n:\mathcal P_\Sigma\to\mathbb N_\Sigma
\]

on the native prime set such that

\[
\boxed{
n=\prod_{p\in\mathcal P_\Sigma}p^{\nu_n(p)}.}
\]

Moreover,

\[
\boxed{
\nu_{mn}(p)=\nu_m(p)+\nu_n(p).
}
\]

This is the native prime-exponent vector consumed by the later prime-torus
chart, but no torus is introduced here.

---

## 9. Divisor sums and finite Euler identities

### Definition 9.1

For `n>=1`, let

\[
\operatorname{Div}_\Sigma(n)
=
\{d\in\mathbb N_\Sigma:d|n\}.
\]

This set is finite because every divisor satisfies `1<=d<=n`.

For a native arithmetic function `f`, define the finite divisor sum

\[
\sum_{d|n}f(d).
\]

### Lemma 9.2 — Multiplicative divisor decomposition

If `gcd_Sigma(m,n)=1`, then every divisor of `mn` has a unique form

\[
d=ab,
\qquad a|m,
\qquad b|n.
\]

### Proof

Use the disjoint prime supports supplied by Corollary 8.2. A divisor chooses an
exponent between `0` and the exponent of each prime. Splitting those choices
between the prime supports of `m` and `n` gives the unique pair `(a,b)`. ∎

### Corollary 9.3

Finite divisor convolution

\[
(f*g)(n)=\sum_{d|n}f(d)g(n/d)
\]

is associative and commutative on native arithmetic functions.

### Proof

All sums are finite. Reindex by the unique factorization of ordered divisor
triples. ∎

---

## 10. Native Möbius function

The logarithmic derivative of zeta can be developed without Möbius inversion,
but the exact arithmetic extraction is useful later.

### Definition 10.1

Define `mu_Sigma(n)` by the prime exponent vector:

\[
\mu_\Sigma(1)=1,
\]

\[
\mu_\Sigma(n)=0
\quad\text{if some }\nu_n(p)\ge2,
\]

and otherwise

\[
\mu_\Sigma(n)=(-1)^k
\]

when `n` is a product of `k` distinct primes.

### Theorem 10.2 — Native Möbius cancellation

For every natural `n`,

\[
\boxed{
\sum_{d|n}\mu_\Sigma(d)
=
\begin{cases}
1,&n=1,\\
0,&n>1.
\end{cases}
}
\]

### Proof

If

\[
n=\prod_{j=1}^{r}p_j^{a_j},
\]

then only square-free divisors contribute. Choosing a subset of the `r` distinct
prime factors gives

\[
\sum_{d|n}\mu_\Sigma(d)
=
\sum_{k=0}^{r}\binom{r}{k}(-1)^k
=(1-1)^r.
\]

For `n=1`, `r=0` and the value is `1`. The binomial identity is finite algebra
inside the native integer ring. ∎

### Corollary 10.3 — Native Möbius inversion

If native arithmetic functions satisfy

\[
F(n)=\sum_{d|n}f(d),
\]

then

\[
\boxed{
f(n)=\sum_{d|n}\mu_\Sigma(d)F(n/d).}
\]

### Proof

Substitute the divisor sum for `F`, regroup the finite double sum by the product
of the two divisor variables, and apply Theorem 10.2. ∎

---

## 11. Native von Mangoldt arithmetic weight

### Definition 11.1

Using the native logarithm of F00-G, define

\[
\boxed{
\Lambda_\Sigma(n)
=
\begin{cases}
\operatorname{Log}_\Sigma(p),
&n=p^k\text{ for a native prime }p\text{ and }k\ge1,\\
0,&\text{otherwise}.
\end{cases}
}
\]

### Theorem 11.2 — Native logarithmic divisor identity

For every positive natural `n`,

\[
\boxed{
\operatorname{Log}_\Sigma(n)
=
\sum_{d|n}\Lambda_\Sigma(d).
}
\]

### Proof

Write

\[
n=\prod_{j=1}^{r}p_j^{a_j}.
\]

The prime powers dividing `n` are `p_j^k` for `1<=k<=a_j`. Therefore

\[
\sum_{d|n}\Lambda_\Sigma(d)
=
\sum_{j=1}^{r}a_j\operatorname{Log}_\Sigma(p_j)
=
\operatorname{Log}_\Sigma(n)
\]

by the logarithmic product law. ∎

### Corollary 11.3 — Native pressure extraction

Let

\[
\ell_\Sigma(n)=\operatorname{Log}_\Sigma(n).
\]

Then under divisor convolution,

\[
\boxed{
\ell_\Sigma*\mu_\Sigma
=
\Lambda_\Sigma.
}
\]

### Proof

Apply Möbius inversion to Theorem 11.2. ∎

This recovers the arithmetic identity used in MP without importing the ordinary
Möbius or von Mangoldt functions.

---

## 12. Coordinate shadow

Under a later faithful scalar chart preserving the repeated unit,

\[
n_\Sigma\mapsto n,
\]

native divisibility, gcd, primes, exponent vectors, `mu_Sigma` and
`Lambda_Sigma` map to their ordinary arithmetic counterparts. The chart is
forced by the finite recursive construction and unique factorization proved
above.

No ordinary prime theorem is used to construct the native objects.

---

## 13. Claim boundary

Proved here:

```text
native natural and integer subrings;
divisibility and cancellation;
division with remainder;
gcd and terminating Euclidean algorithm;
Bezout identity;
native primes and composite splitting;
Euclid lemma;
existence and uniqueness of prime factorization;
prime-exponent vectors;
finite divisor convolution;
native Möbius function and inversion;
native von Mangoldt function;
Log_Sigma(n)=sum_{d|n} Lambda_Sigma(d);
Log_Sigma * mu_Sigma = Lambda_Sigma.
```

Not proved here:

```text
infinitude of primes;
Dirichlet-series convergence;
Euler product as an infinite limit;
nonvanishing of zeta in Re(s)>1;
prime number theorem;
analytic continuation;
completed zeta;
explicit formula;
Weil criterion;
K0>=0;
RH.
```

Infinitude of primes and the analytic identities belong to F00-I. No external
fundamental theorem of arithmetic is consumed.
