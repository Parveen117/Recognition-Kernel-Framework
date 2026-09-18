# MR-07 — Finite-Matrix Holonomy Area Scaling

## 1. Scope and normative erratum

This capsule corrects the discrete-to-continuous holonomy scaling in the
[Morphic Calculus manuscript](../morphic_calculus/main.tex), subsection
**Convergence of Discrete Holonomy** (lines 1192–1198 at repository commit
`86198d29cbf30390059079f38675c952e506ea9c`). The subsequent **Accumulated Residue**
paragraph, lines 1200–1202, must also be read with the scaling restriction below.
Those historical passages are preserved for provenance; this capsule supersedes
their claim that repeated loops of step `T/n` yield a nontrivial commutator flow.

The finite representation is declared explicitly. A matrix representation does
not identify every native Morphisum, Cut, or Recognition object with a matrix.
The loop order below is fixed; reversing it reverses the leading commutator.

For a loop with leading residue `h² K`, the accumulated scale is **area** `n h²`.
Keeping total edge parameter `n h = T` fixed instead makes this area vanish.
Nonzero `K` alone does not guarantee a nonidentity limit at every chosen area:
the matrix exponential can return to identity. Unbounded operators, varying
generators, infinite carriers, and physical identification are excluded.

This is an explicit matrix-analysis correction and bridge, not a claim that the
matrix product-limit method is new. It does not certify surrounding manuscript
claims. In particular, the neighboring **Finite-Step BCH Effective Generator**
and **Symmetric Composition** formulas for Euler steps have separate quadratic
terms and require their own correction; they are not used here.

## 2. Declared finite matrix datum

Let `H_h` and `K` be real or complex `d × d` matrices. Use a submultiplicative
matrix norm with `||I|| = 1`. Assume constants `h_0 > 0` and `C >= 0` satisfy

\[
H_h=I+h^2K+R_h,\qquad
\|R_h\|\le C h^3\quad(0\le h\le h_0).
\]

In particular, `H_0 = I`. Put `k = ||K||`. No invertibility assumption is needed
for the following product-limit estimate; an invertible commutator loop is one
way to realize the datum.

### Lemma 2.1 — One-step and repeated-step bounds

For every positive integer `n` and `0 <= h <= h_0`,

\[
\boxed{
\|H_h^n-e^{nh^2K}\|
\le
n\left(C h^3+\frac{h^4k^2}{2}e^{h^2k}\right)
e^{nh^2(k+Ch)}.
}
\tag{1}
\]

### Proof

The exponential series and `j! >= 2 (j-2)!` for `j >= 2` give

\[
\|e^{h^2K}-I-h^2K\|
\le \frac{h^4k^2}{2}e^{h^2k}.
\]

Consequently `||H_h-e^{h²K}||` is bounded by the parenthesis in (1), while

\[
\|H_h\|\le1+h^2(k+Ch)\le e^{h^2(k+Ch)},\qquad
\|e^{h^2K}\|\le e^{h^2k}.
\]

For arbitrary matrices `A,B`, including noncommuting matrices,

\[
A^n-B^n=\sum_{j=0}^{n-1}A^{n-1-j}(A-B)B^j.
\]

Set `A=H_h`, `B=e^{h²K}`. Each summand is bounded by the one-step error times
`exp((n-1)h²(k+Ch))`, which is at most the factor in (1). Finally
`(e^{h²K})^n=e^{nh²K}`. ∎

## 3. Area-scaled convergence theorem

### Theorem 3.1 — Fixed area and explicit rate

Fix `tau >= 0`, and let `h_n = sqrt(tau/n)`. For every positive integer
`n >= tau/h_0²`,

\[
\boxed{
\|H_{\sqrt{\tau/n}}^n-e^{\tau K}\|
\le e^{\tau(k+C\sqrt{\tau/n})}
\left(
\frac{C\tau^{3/2}}{\sqrt n}
+\frac{\tau^2k^2}{2n}e^{\tau k/n}
\right).
}
\tag{2}
\]

In particular,

\[
H_{\sqrt{\tau/n}}^n\longrightarrow e^{\tau K}.
\]

A uniform explicit `O(n^{-1/2})` estimate on those integers is

\[
\|H_{\sqrt{\tau/n}}^n-e^{\tau K}\|
\le\frac{e^{\tau(k+Ch_0)}}{\sqrt n}
\left(C\tau^{3/2}+\frac{\tau^2k^2}{2}e^{h_0^2k}\right).
\tag{3}
\]

### Proof

Substitute `h_n` into (1). The condition on `n` ensures the remainder hypothesis
is available. Bound `h_n <= h_0`, `tau/n <= h_0²`, and `1/n <= 1/sqrt(n)` to
obtain (3). For `tau=0`, both sides of the asserted limit are exactly `I`. ∎

### Theorem 3.2 — Fixed edge scale collapses to identity

Fix `T >= 0`. For every positive integer `n >= T/h_0`,

\[
\boxed{
\|H_{T/n}^n-I\|
\le a_n e^{a_n},\qquad
a_n=\frac{T^2}{n}\left(k+\frac{CT}{n}\right).
}
\tag{4}
\]

Thus `H_{T/n}^n -> I`, with the explicit bound

\[
\|H_{T/n}^n-I\|
\le\frac{T^2(k+Ch_0)e^{T^2(k+Ch_0)}}{n}.
\tag{5}
\]

### Proof

Telescope against `I`, using `||H_h-I|| <= h²(k+Ch)` and
`||H_h|| <= exp(h²(k+Ch))`. This gives
`||H_h^n-I|| <= n h²(k+Ch) exp(n h²(k+Ch))`.
Substitution proves (4). The assumptions `h<=h_0` and `n>=1` give (5).
The case `T=0` is exact identity. ∎

## 4. Exact noncommuting calibration

Take the rational nilpotent generators

\[
X=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

Since `X²=Y²=0`, the Euler steps `I+hX`, `I+hY` have exact inverses `I-hX`,
`I-hY` for every real `h`. Direct polynomial multiplication proves

\[
\begin{aligned}
H_h&=(I+hX)(I+hY)(I-hX)(I-hY)\\
&=\begin{pmatrix}1+h^2+h^4&-h^3\\h^3&1-h^2\end{pmatrix}\\
&=I+h^2K+h^3L+h^4Q,
\end{aligned}
\]

where

\[
K=[X,Y]=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
L=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
Q=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The determinant polynomial is identically one:

\[
(1+h^2+h^4)(1-h^2)+h^6=1.
\]

For the maximum absolute row-sum norm, `k=1` and

\[
\|h^3L+h^4Q\|_\infty=h^3+h^4\le2h^3\quad(0\le h\le1).
\]

Therefore (2) applies with `C=2`, `h_0=1`, and yields
`diag(e^tau,e^{-tau})`. Swapping `X,Y` changes the quadratic coefficient to
`-K`. Taking `Y=X` gives an exactly identity loop. These are orientation and
commuting controls, not physical identifications.

## 5. Exact rejection of the wrong scaling

For the preceding calibration take `T=1`. Then

\[
a_n=\frac1n\left(1+\frac2n\right).
\]

For `0 <= a < 1`, the exponential series gives `e^a <= 1/(1-a)`. Thus for
every `n>=8`,

\[
\|H_{1/n}^n-I\|_\infty
\le\frac{a_n}{1-a_n}\le\frac5{27}.
\]

But `||e^K-I||_infinity=e-1>1`, since the exponential series gives `e>2`.
The reverse triangle inequality therefore implies, for every `n>=8`,

\[
\|H_{1/n}^n-e^K\|_\infty>1-\frac5{27}=\frac{22}{27}.
\]

This is an analytic and exact-rational negative control. A long numerical
iteration is not used to establish or refute a limit.

## 6. RNKE proof contract and certificate boundary

The standard-library verifier is
[`proof_lab/morphic_recognition/holonomy.py`](../../proof_lab/morphic_recognition/holonomy.py).
It uses exact rational matrix-polynomial arithmetic, not floating-point limits.
For nonnegative rational `x`, it majorizes exponentials by choosing integer
`m=floor(x)+1` and using

\[
e^x=(e^{x/m})^m\le(1-x/m)^{-m}.
\]

Every bound evaluator checks `0<=h<=h_0`, `h_0>0`, positive integer `n`, and
nonnegative norm/remainder constants. The caller must supply a proved remainder
contract; a numeric bound evaluation cannot establish that hypothesis.

```text
MR07-O1  nilpotent generators and exact inverse polynomials
MR07-O2  exact loop polynomial and determinant-one identity
MR07-O3  coefficient norms supply C=2, h_0=1 remainder contract
MR07-O4  exact rational area-scale bound evaluations and n h²=1
MR07-O5  zero-area / zero-commutator controls
MR07-N1  wrong fixed-edge scaling separated from exp(K) by >22/27
MR07-N2  reversed generator order rejects the original commutator sign
```

The general proofs are Sections 2–3; Sections 4–5 provide exact witnesses.
Finite certificate evaluations test the implementation and these witnesses,
not the generality of a convergence theorem.

| Evidence axis | Status / boundary |
|---|---|
| Mathematical theorem | PROVED UNDER DECLARED FINITE-MATRIX HYPOTHESES |
| Computational certificate | Exact rational contract; recorded by the campaign |
| Formal proof assistant | NOT FORMALIZED |
| Provenance | Historical manuscript preserved; subsection superseded as stated |
| External review | NOT CLAIMED |
| Other manuscript claims | NOT CERTIFIED BY MR-07 |
