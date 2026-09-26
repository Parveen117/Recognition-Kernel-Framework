# SC-18 — General Realizability Obstruction and Jump Cohomology Theorem

## 1. Derived versus independently declared data

Let

\[
(C^\bullet_\Delta,D_\Delta)
\]

be the finite normal-crossing jump complex of SC-16.

A codimension-\((k+1)\) packet \(c\in C^{k+1}_\Delta\) is **lower-stratum
realizable** if there exists \(b\in C^k_\Delta\) such that

\[
\boxed{c=D_\Delta b.}
\]

## Theorem 1.1 — General fail-closed realizability obstruction

If \(c\) is lower-stratum realizable, then

\[
\boxed{D_\Delta c=0.}
\]

Consequently,

\[
\boxed{
D_\Delta c\neq0
\Longrightarrow
c\notin\operatorname{im}D_\Delta.
}
\]

### Proof

If \(c=D_\Delta b\), SC-16 gives

\[
D_\Delta c
=D_\Delta^2b
=0.
\]

The second statement is the contrapositive. ∎

This single theorem contains SC-15's

\[
T_{123}\neq0
\Longrightarrow
\text{no compatible lower-stratum realization}
\]

as the degree-three case.

## 2. Closed is not necessarily exact

Define the jump cohomology groups

\[
\boxed{
H^k_\Delta
=
\frac{\ker(D_\Delta:C^k_\Delta\to C^{k+1}_\Delta)}
{\operatorname{im}(D_\Delta:C^{k-1}_\Delta\to C^k_\Delta)}.
}
\]

## Theorem 2.1 — Two-stage realizability test

For independently declared \(c\in C^k_\Delta\):

1. if \(D_\Delta c\neq0\), then \(c\) is definitely not realizable from degree
   \(k-1\);
2. if \(D_\Delta c=0\), then \(c\) passes the local compatibility gate, but a
   nonzero class
   \[
   [c]\neq0\in H^k_\Delta
   \]
   is an obstruction to exact lower-stratum realization.

### Proof

Part 1 is Theorem 1.1. For Part 2, by definition \([c]=0\) exactly when
\(c\in\operatorname{im}D_\Delta\). Thus a nonzero cohomology class cannot be
exact. ∎

## 3. Total-complex version

Let \((\operatorname{Tot}^\bullet,\mathbb D)\) be the total stratified complex of
SC-17 and define

\[
\boxed{
H^r_{\mathbb D}
=
\frac{\ker(\mathbb D:\operatorname{Tot}^r\to\operatorname{Tot}^{r+1})}
{\operatorname{im}(\mathbb D:\operatorname{Tot}^{r-1}\to\operatorname{Tot}^r)}.
}
\]

Then exactly the same fail-closed logic holds:

\[
\boxed{
\mathbb D c\neq0
\Longrightarrow
c\text{ is not a total boundary},
}
\]

while

\[
\mathbb D c=0
\]

is only the first gate. Global total realizability requires vanishing of the
relevant cohomology class.

## 4. Recognition packet

The theorem suggests the general typed recognition object

\[
\boxed{
\mathfrak C_{\rm strat}
=
\bigoplus_{k=0}^{n} c^{(k)},
}
\]

with compatibility obligations

\[
\boxed{
D_\Delta c^{(k)}=0
}
\]

for every independently supplied stratum packet whose lower realization is
claimed.

If a total differential model is used, the stronger obligation is

\[
\boxed{\mathbb D\mathfrak C_{\rm strat}=0.}
\]

These conditions are typed. Cancellation between different codimensions does not
constitute closure.

## 5. Claim boundary

This theorem deliberately does not claim that the normal-crossing complex is
acyclic. In particular,

\[
D_\Delta c=0
\]

does not by itself imply

\[
c=D_\Delta b.
\]

Similarly, \(\mathbb D c=0\) does not imply global potential reconstruction.
Such conclusions require an exactness, contractibility, Poincare-type, or domain-
specific reconstruction theorem.

## Status

```text
LOWER-STRATUM REALIZABILITY c=D_DELTA b         DEFINED
D_DELTA c != 0 => NO LOWER REALIZATION          PROVED
JUMP COHOMOLOGY H_DELTA                         DEFINED
CLOSED BUT NONEXACT AS GLOBAL OBSTRUCTION       PROVED BY DEFINITION
TOTAL-COMPLEX FAIL-CLOSED VERSION               PROVED
ACYCLICITY / GLOBAL RECONSTRUCTION              NOT CLAIMED
```