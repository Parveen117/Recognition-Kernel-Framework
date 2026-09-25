# SC-16 — General Normal-Crossing Jump-Complex Theorem

## 1. Purpose

SC-12 through SC-15 establish the first two nontrivial compatibility levels for
transverse seam intersections. This theorem replaces the case-by-case pattern by
a single finite normal-crossing complex.

Let the seam labels be the totally ordered set

\[
N=\{1,\ldots,n\}.
\]

For every ordered subset

\[
I=\{i_0<\cdots<i_k\}\subseteq N
\]

let \(A_I\) be an abelian coefficient group assigned to the codimension-\(|I|\)
stratum. For every \(j\notin I\), assume a jump/restriction map

\[
\Delta_j:A_I\to A_{I\cup\{j\}}.
\]

Whenever \(i,j\notin I\), assume the normal-crossing square commutes:

\[
\boxed{\Delta_i\Delta_j=\Delta_j\Delta_i.}
\]

This is the algebraic form of compatible transverse one-sided traces.

## 2. Cochain groups

Define

\[
\boxed{
C^k_\Delta
=\bigoplus_{|I|=k} A_I.
}
\]

For \(c\in C^k_\Delta\) and an ordered \((k+1)\)-subset

\[
I=\{i_0<\cdots<i_k\},
\]

define

\[
\boxed{
(D_\Delta c)_I
=
\sum_{r=0}^{k}
(-1)^r
\Delta_{i_r}
 c_{I\setminus\{i_r\}}.
}
\]

Thus

\[
D_\Delta:C^k_\Delta\to C^{k+1}_\Delta.
\]

For codimension one data \(\beta=(\beta_i)\),

\[
(D_\Delta\beta)_{ij}
=
\Delta_i\beta_j-\Delta_j\beta_i,
\]

so SC-13's \(J_{ij}\) is exactly \((D_\Delta\beta)_{ij}\).

For codimension two data \(J\),

\[
(D_\Delta J)_{ijk}
=
\Delta_iJ_{jk}-\Delta_jJ_{ik}+\Delta_kJ_{ij},
\]

so SC-14's \(T_{ijk}\) is exactly \((D_\Delta J)_{ijk}\).

## Theorem 2.1 — Nilpotence of the normal-crossing jump differential

Under the commuting-square hypothesis,

\[
\boxed{D_\Delta^2=0.}
\]

### Proof

Let \(c\in C^k_\Delta\), and fix an ordered \((k+2)\)-subset

\[
I=\{i_0<\cdots<i_{k+1}\}.
\]

Expanding \((D_\Delta^2c)_I\) produces one term for every ordered choice of two
distinct deleted indices. Fix \(r<s\). The coefficient involving

\[
\Delta_{i_r}\Delta_{i_s}
 c_{I\setminus\{i_r,i_s\}}
\]

appears twice.

Deleting \(i_s\) first and then \(i_r\) gives sign

\[
(-1)^s(-1)^r=(-1)^{r+s}.
\]

Deleting \(i_r\) first shifts the later position of \(i_s\) down by one and gives

\[
(-1)^r(-1)^{s-1}=-(-1)^{r+s}.
\]

The two operator compositions agree by

\[
\Delta_{i_r}\Delta_{i_s}
=
\Delta_{i_s}\Delta_{i_r}.
\]

Hence the pair cancels. Every term belongs to exactly one such pair, so

\[
(D_\Delta^2c)_I=0.
\]

Since \(I\) was arbitrary, \(D_\Delta^2=0\). ∎

## Corollary 2.2 — Every derived obstruction satisfies the next compatibility law

If

\[
c^{(k+1)}=D_\Delta c^{(k)},
\]

then

\[
\boxed{D_\Delta c^{(k+1)}=0.}
\]

Thus every compatible lower-stratum realization automatically closes at the next
normal-crossing compatibility level.

## Corollary 2.3 — SC-13 and SC-14 are low-degree instances

For \(k=1\),

\[
\beta\mapsto J=D_\Delta\beta.
\]

For \(k=2\),

\[
J\mapsto T=D_\Delta J.
\]

Therefore

\[
\boxed{T=D_\Delta^2\beta=0}
\]

is not a separate accidental identity; it is the degree-two instance of the
general complex law.

## 3. Recognition interpretation

The normal-crossing hierarchy is a typed cochain complex:

\[
\boxed{
C^0_\Delta
\xrightarrow{D_\Delta}
C^1_\Delta
\xrightarrow{D_\Delta}
C^2_\Delta
\xrightarrow{D_\Delta}
\cdots
\xrightarrow{D_\Delta}
C^n_\Delta.
}
\]

The theorem says the boundary of a compatible boundary is zero. No scalar
aggregation is permitted to replace the individual codimension channels.

## 4. Claim boundary

The theorem assumes a finite transverse normal-crossing system with commuting
jump squares. It does not claim:

- nontransverse seam calculus;
- infinite seam families;
- global exactness of the jump complex;
- that every \(D_\Delta\)-closed cochain is \(D_\Delta\)-exact;
- a physical interpretation of the cochain groups;
- a topological transition merely from nonzero local data.

## Status

```text
GENERAL FINITE NORMAL-CROSSING COCHAIN GROUPS  DEFINED
ALTERNATING JUMP DIFFERENTIAL D_DELTA          DEFINED
D_DELTA^2 = 0                                  PROVED
SC-13 J_ij AS DEGREE-2 IMAGE                   RECOVERED
SC-14 T_ijk AS DEGREE-3 IMAGE                  RECOVERED
GLOBAL EXACTNESS / REALIZABILITY               NOT CLAIMED
```