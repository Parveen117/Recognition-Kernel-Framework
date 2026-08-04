# Native Common-Chart Source-Domination and Decoder-Transfer Theorem

## 1. Purpose

Stage 3A showed that source-cell energies and boundary masses do not, by
themselves, determine a boundary functional.  Relative phase and event lineage
matter if one attempts to reconstruct a decoder coefficient by coefficient.

That observation is correct, but it does not force a 78,734-event phase
reconstruction.

There is a stronger native route:

```text
actual source and actual boundary in one cut chart
-> Loewner lower source symbol
-> boundary/source relative bound
-> canonical decoder on the complete event range
-> cut covariance.
```

Once the boundary density is the actual density in the same chart as the source
lower symbol, its phase is already part of the density.  A scalar floor may then
be used outwardly without forgetting orientation.

The actual unresolved issue is therefore not every event phase.  It is the
single common-chart identity.

---

## 2. Native common-chart datum

Let

\[
\Xi:\mathcal H_{\rm src}\longrightarrow\mathcal Y_\Sigma
\]

be a complete native event analysis and put

\[
S=\Xi^*\Xi.
\]

Let

\[
J:\mathcal H_{\rm src}\longrightarrow
L^2(X,\mu;\mathbb C^d)
\]

be a declared native cut chart.  Let \(A(x)\) be a measurable positive
semidefinite matrix field and assume the actual source dominates its charted
energy:

\[
\boxed{
\|\Xi f\|_{\Sigma}^2
\ge
\int_X
\langle Jf(x),A(x)Jf(x)\rangle\,d\mu(x).
}
\tag{2.1}
\]

Let \(b:X\to\mathbb C^d\) be the actual boundary density in that same chart:

\[
\boxed{
L(f)
=
\int_X
\langle b(x),Jf(x)\rangle\,d\mu(x).
}
\tag{2.2}
\]

Equation (2.2) is the orientation statement.  It may not be replaced by a list
of numbers \(\|b(x)\|^2\) detached from the chart map \(J\).

---

## 3. Matrix-symbol decoder theorem

Let \(A(x)^\dagger\) be the Moore--Penrose inverse.  Assume

\[
b(x)\in\operatorname{Ran}A(x)^{1/2}
\quad\text{for almost every }x
\]

and

\[
\boxed{
\beta_A
=
\int_X
\langle b(x),A(x)^\dagger b(x)\rangle\,d\mu(x)
<\infty.
}
\tag{3.1}
\]

### Theorem 3.1 (Common-chart source domination)

For every \(f\in\mathcal H_{\rm src}\),

\[
\boxed{
|L(f)|^2
\le
\beta_A\,\|\Xi f\|_\Sigma^2.
}
\tag{3.2}
\]

#### Proof

Put

\[
c_A(x)=A(x)^{\dagger/2}b(x).
\]

The range hypothesis gives

\[
b(x)=A(x)^{1/2}c_A(x).
\]

Therefore

\[
L(f)
=
\int_X
\langle c_A(x),A(x)^{1/2}Jf(x)\rangle\,d\mu(x).
\]

Cauchy--Schwarz gives

\[
|L(f)|^2
\le
\left(
\int_X\|c_A(x)\|^2d\mu(x)
\right)
\left(
\int_X\|A(x)^{1/2}Jf(x)\|^2d\mu(x)
\right).
\]

The first factor is \(\beta_A\); the second is bounded by
\(\|\Xi f\|_\Sigma^2\) through (2.1). ∎

---

## 4. Canonical decoder on the complete event range

The preceding theorem proves more than an inequality.

### Theorem 4.1 (Decoder transfer by recognition completion)

Under Theorem 3.1, define on \(\operatorname{Ran}\Xi\)

\[
\widetilde L(\Xi f)=L(f).
\]

Then \(\widetilde L\) is well-defined and bounded, and there exists a unique

\[
c_\partial\in\overline{\operatorname{Ran}\Xi}
\]

such that

\[
\boxed{
L(f)=\langle c_\partial,\Xi f\rangle_\Sigma
\qquad(f\in\mathcal H_{\rm src}).
}
\tag{4.1}
\]

Moreover,

\[
\boxed{
\|c_\partial\|_\Sigma^2
=\beta_{\rm cut}
\le\beta_A.
}
\tag{4.2}
\]

#### Proof

If \(\Xi f=0\), (3.2) gives \(L(f)=0\), so \(\widetilde L\) is well-defined.
Again by (3.2),

\[
|\widetilde L(y)|
\le\sqrt{\beta_A}\,\|y\|_\Sigma
\qquad(y\in\operatorname{Ran}\Xi).
\]

It extends continuously to \(\overline{\operatorname{Ran}\Xi}\).  The Riesz
representation theorem gives a unique vector \(c_\partial\) there.  Its squared
norm is the sharp source-relative burden, hence is at most \(\beta_A\). ∎

This is not a decoder fitted from the terminal normal equation.  The bound is
proved first from the common cut chart.  The decoder is then forced by
completion.

---

## 5. Cut covariance and relative reserve

From (4.1),

\[
L^*L
\le
\beta_A S.
\]

Therefore

\[
\boxed{
S-L^*L
\ge
(1-\beta_A)S.
}
\tag{5.1}
\]

If \(\beta_A<1\), the signed cut form is nonnegative.  If, in addition,
\(\ker\Xi=\{0\}\), then it is strictly positive on every nonzero source state.

The unit-boundary-state construction from Stage 3A then gives an event carrier
on which

\[
S-L^*L
=
\widehat\Xi^*(I-p_\partial p_\partial^*)\widehat\Xi.
\]

Thus common-chart domination generates the completed cut covariance without a
coefficientwise decoder reconstruction.

---

## 6. Scalar-floor corollary

Assume

\[
A(x)\ge s(x)I_d,
\qquad
s(x)>0.
\]

Then

\[
A(x)^\dagger\le s(x)^{-1}I_d
\]

on the relevant range, so

\[
\boxed{
\beta_A
\le
\int_X\frac{\|b(x)\|^2}{s(x)}\,d\mu(x).
}
\tag{6.1}
\]

This is why a scalar lower branch is sufficient.  It may be less sharp than the
full matrix symbol, but it is orientation-safe once (2.2) has been proved.

The distinction is exact:

```text
before common-chart identity:
  masses alone do not determine the boundary;

after common-chart identity:
  norm masses give a lawful outward burden independent of coordinate phase.
```

---

## 7. Cellwise cut theorem

Let \(X\) be partitioned into cells \(I_j\).  Suppose

\[
A(x)\ge s_j^- I
\quad(x\in I_j)
\]

and

\[
\int_{I_j}\|b(x)\|^2d\mu(x)
\le m_j^+.
\]

Then

\[
\boxed{
\beta_{I_j}
\le
\frac{m_j^+}{s_j^-}
}
\]

and

\[
\boxed{
\beta_A
\le
\sum_j\frac{m_j^+}{s_j^-}.
}
\tag{7.1}
\]

No phase reconstruction is needed in (7.1), because \(m_j^+\) bounds the norm
of the actual common-chart density.

A negative control is mandatory: if the source chart observes one coordinate
while the boundary reads a source-blind coordinate, no finite mass/floor table
proves a decoder.

---

## 8. First-cut cancellation

On the first symmetric cell \(|\xi|\le h\), suppose

\[
s(\xi)\ge c\xi^2,
\qquad
\|b(\xi)\|\le M_1|\xi|.
\]

Then the apparent zero denominator is removed by the odd boundary zero:

\[
\boxed{
\int_{-h}^{h}\frac{\|b(\xi)\|^2}{s(\xi)}d\xi
\le
\frac{2hM_1^2}{c}.
}
\tag{8.1}
\]

This is zero-as-cut in analytic form: the source opens quadratically, the odd
boundary opens linearly, and their quotient retains a finite first-cut memory.

---

## 9. Completed-Weil source pins

The transferred source manuscript records:

```text
Xi_0^* Xi_0 = S_(0,-)^full;
Omega_0(xi) has a directed scalar lower branch s_0(xi);
the full boundary Riesz state gives
  |b_partial(xi)| <= min(|xi|/9, 1/(3 sqrt(2)));
the direct T21 cut ledger gives
  beta_envelope <= 0.8290856201657449.
```

The corresponding reserve is

\[
\boxed{
1-0.8290856201657449
=0.1709143798342551.
}
\]

If the following exact common-chart identity is proved,

\[
\boxed{
L_\partial(f)
=
\int_{\mathbb R}
\langle b_\partial(\xi),J_{\rm Weil}f(\xi)\rangle\,d\xi,
}
\tag{9.1}
\]

and the actual source satisfies

\[
\boxed{
\|\Xi_0f\|_\Sigma^2
\ge
\int_{\mathbb R}
\langle J_{\rm Weil}f(\xi),
\Omega_0(\xi)J_{\rm Weil}f(\xi)\rangle\,d\xi,
}
\tag{9.2}
\]

then Theorems 3.1--5.1 give

\[
\beta_\partial^{\rm cut}
\le0.8290856201657449<1
\]

and

\[
S_{0,-}^{\rm full}-L_\partial^*L_\partial
\ge
0.1709143798342551\,S_{0,-}^{\rm full}.
\]

No 78,734-event phase reconstruction would then be required.

---

## 10. What remains after Stage 3B

Stage 3A described the missing object as a coefficientwise orientation packet.
Stage 3B sharpens that target.

The minimal remaining theorem is:

### Native two-sheet boundary-pairing theorem

Construct the actual cut chart

\[
J_{\rm Weil}:X_3^-\to L^2(\mathbb R;\mathbb C^2)
\]

from the already declared prime--Gamma two-sheet analysis and prove (9.1)--(9.2)
on the native generator core.  Then prove Recognition-Cauchy/Smriti-tail
extension to the completed carrier.

The chart must be derived from the source construction.  It may not be chosen
post hoc to make (9.1) true.

---

## 11. Exact calibration

The Stage 3B rational calibration uses

\[
\Xi=\operatorname{diag}(3,4),
\qquad
S=\operatorname{diag}(9,16),
\]

with common-chart lower symbol

\[
A=\operatorname{diag}(4,9)
\]

and positive source remainder

\[
R=\operatorname{diag}(5,7).
\]

For boundary density \(b=(1,2)\),

\[
\beta_A=b^*A^{-1}b=\frac{25}{36},
\]

while the exact sharp burden is

\[
\beta_{\rm cut}=b^*S^{-1}b=\frac{13}{36}.
\]

The canonical complete-event decoder is

\[
c_\partial=\left(\frac13,\frac12\right),
\]

with energy \(13/36\).  This verifies that source domination constructs a
lawful, possibly nonsharp, decoder certificate.

---

## 12. Claim boundary

```text
common-chart matrix-symbol domination theorem          PROVED
canonical decoder transfer to complete event range     PROVED
scalar-floor orientation-safe corollary                PROVED
cellwise cut burden theorem                            PROVED
first-cut quadratic/linear cancellation               PROVED
mismatched-chart negative control                      PROVED
T21 arithmetic audit                                   PASSED

actual J_Weil and b_partial common-chart identity      OPEN / NEXT
Recognition-complete chart transport                   OPEN / NEXT
actual completed-Weil decoder and covariance           OPEN UNTIL ABOVE
RH                                                      NOT CLAIMED
```
