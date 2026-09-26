# Native Completed-Weil Cut-Event Co-Generation Gate

## 1. Purpose

The generalized cut-covariance theorem is now passed.  The first RH-specific
step is therefore not another spectral computation.  It is to construct the
odd completed-Weil source and boundary on one oriented event carrier.

The source material fixes the odd carrier and the two terminal objects:

\[
L_\partial f=\sqrt2\,\widehat f(i/2),
\]

\[
W_3^-
=S_{0,-}^{\rm full}-L_\partial^*L_\partial,
\]

and states that a complete prime--Gamma cut-event analysis satisfies

\[
\Xi_0^*\Xi_0=S_{0,-}^{\rm full}.
\]

These statements do not yet prove that the boundary functional is a first
moment of the same event analysis.  That orientation identity is the exact gate
addressed here.

The lawful order is

```text
prime / Gamma / diagonal-debt cut events
-> one coefficientwise event analysis Xi_N
-> one boundary decoder c_partial,N on that same orientation
-> recovered refinement identity
-> Recognition-Cauchy and Smriti-tail completion
-> continuum first/second-moment identity
-> cut covariance and odd positivity.
```

---

## 2. Finite oriented event packet

Let \(\mathfrak E_N\) be a finite declared event family.  For each event
\(e\in\mathfrak E_N\), let

\[
\zeta_{N,e}:X_{3,\rm core}^-\longrightarrow\mathbb C
\]

be its oriented source channel, let \(s_{N,e}>0\) be its source energy, and let
\(a_{N,e}\in\mathbb C\) be its boundary amplitude.

Define

\[
\boxed{
(\Xi_N f)_e
=\sqrt{s_{N,e}}\,\zeta_{N,e}(f),
}
\]

and

\[
\boxed{
L_{\partial,N}f
=\sum_{e\in\mathfrak E_N}
\overline{a_{N,e}}\,\zeta_{N,e}(f).
}
\]

The oriented decoder is

\[
\boxed{
(c_{\partial,N})_e
=\frac{a_{N,e}}{\sqrt{s_{N,e}}}.
}
\]

Then

\[
\boxed{
L_{\partial,N}f
=\langle c_{\partial,N},\Xi_N f\rangle,
}
\]

and

\[
\boxed{
\beta_N
=\|c_{\partial,N}\|^2
=\sum_{e\in\mathfrak E_N}
\frac{|a_{N,e}|^2}{s_{N,e}}.
}
\]

This formula is valid only when the coefficients and source channels have one
recovered event orientation.  A list of positive numbers \(s_e\) and masses
\(|a_e|^2\) does not determine the boundary functional.

---

## 3. Constructive first/second-moment realization

### Theorem 3.1 (Contractive decoder is equivalent to co-generation)

Suppose

\[
\|c_{\partial,N}\|\le1.
\]

Enlarge the event carrier by one orthogonal completion coordinate and put

\[
\widehat\Xi_N f=(\Xi_N f,0),
\]

\[
\boxed{
p_{\partial,N}
=\left(c_{\partial,N},
\sqrt{1-\|c_{\partial,N}\|^2}\right).
}
\]

Then \(\|p_{\partial,N}\|=1\) and

\[
\boxed{
S_N=\widehat\Xi_N^*\widehat\Xi_N,
}
\]

\[
\boxed{
L_{\partial,N}=p_{\partial,N}^*\widehat\Xi_N,
}
\]

so that

\[
\boxed{
S_N-L_{\partial,N}^*L_{\partial,N}
=\widehat\Xi_N^*
\left(I-p_{\partial,N}p_{\partial,N}^*\right)
\widehat\Xi_N
\ge0.
}
\]

#### Proof

The added coordinate does not change the source Gram.  The first-moment identity
follows because its event-lift coordinate is zero.  The norm of
\(p_{\partial,N}\) is one by construction.  The cut-covariance identity is then
Theorem 3.1 of the universal cut-covariance stage. ∎

This theorem makes the missing object explicit.  A successful direct cut burden
is not merely a number below one; it constructs a unit boundary-recognition
state after the same-event decoder has been proved.

---

## 4. Exact shifted-to-unshifted identity

For source energies \(s_e>0\), boundary masses \(m_e=|a_e|^2\), and \(\eta>0\),
put

\[
\beta_{0,N}=\sum_e\frac{m_e}{s_e},
\qquad
\beta_{\eta,N}=\sum_e\frac{m_e}{s_e+\eta}.
\]

### Theorem 4.1 (Cut-event endpoint identity)

\[
\boxed{
\beta_{0,N}-\beta_{\eta,N}
=\sum_e
\frac{m_e\eta}{s_e(s_e+\eta)}.
}
\]

This is the exact finite event identity used by the earlier endpoint refinement.
It is native only after the events, energies and boundary amplitudes are carried
on the same recovered orientation.

---

## 5. Coherent refinement and orientation memory

Suppose one parent event with channel \(\zeta\), source energy \(s\), and
boundary amplitude \(a\) is split into children with the same underlying
channel, energies \(s_j>0\), and amplitudes \(a_j\), where

\[
\sum_j s_j=s,
\qquad
\sum_j a_j=a.
\]

### Theorem 5.1 (Refinement burden monotonicity)

\[
\boxed{
\sum_j\frac{|a_j|^2}{s_j}
\ge
\frac{|a|^2}{s}.
}
\]

Equality holds exactly when

\[
\boxed{
\frac{a_j}{s_j}
\text{ is constant across the children.}
}
\]

#### Proof

Weighted Cauchy--Schwarz gives

\[
\left|\sum_j a_j\right|^2
\le
\left(\sum_j s_j\right)
\left(\sum_j\frac{|a_j|^2}{s_j}\right).
\]

Substitute the parent sums.  Equality is the equality condition for weighted
Cauchy--Schwarz. ∎

Thus a lawful refinement carries more than scalar masses.  It carries the
relative phase and orientation of the child boundary amplitudes.  Two
refinements can have identical source energies and identical masses but different
boundary functionals.

This is the Recognition-Seam meaning of cut memory at the decoder level.

---

## 6. Recognition-complete continuum gate

Let \(\Xi_N\) be transported to one recovered event carrier and let
\(c_{\partial,N}\) use one fixed orientation.  Assume

\[
\Xi_N\longrightarrow\Xi_0
\]

in operator norm after predeclared corrections and vanishing Smriti tails, and

\[
c_{\partial,N}\longrightarrow c_\partial
\]

in the event carrier.  Assume also

\[
L_{\partial,N}\longrightarrow L_\partial
\]

in source-dual norm.

### Theorem 6.1 (Recognition-complete event co-generation)

If

\[
L_{\partial,N}
=c_{\partial,N}^*\Xi_N
\]

for every refinement, then

\[
\boxed{
L_\partial=c_\partial^*\Xi_0.
}
\]

Moreover,

\[
\boxed{
\|c_\partial\|^2
=\lim_N\|c_{\partial,N}\|^2
}
\]

under norm convergence.  Hence a uniform or limiting burden bound below one
passes to the continuum cut-covariance realization.

The recovered-middle and Smriti hypotheses are essential.  A sequence of
coordinate vectors whose labels rotate or whose event channels change between
refinements does not satisfy this theorem merely because the scalar burdens
converge.

---

## 7. Robust approximate orientation theorem

Exact coefficientwise orientation may be approached through an outward residual.
Let \(c_N\) be a candidate decoder on the actual event analysis \(\Xi_0\), and
put

\[
r_N(f)
=L_\partial f-\langle c_N,\Xi_0f\rangle.
\]

Assume

\[
|r_N(f)|
\le
\delta_N\|\Xi_0f\|
\qquad(f\in X_{3,\rm core}^-).
\]

### Theorem 7.1 (Robust decoder orientation)

If

\[
\|c_N\|^2\le u_N,
\]

then the actual boundary burden satisfies

\[
\boxed{
\sqrt{\beta_\partial^{\rm cut}}
\le
\sqrt{u_N}+\delta_N,
}
\]

and therefore

\[
\boxed{
\beta_\partial^{\rm cut}
\le
(\sqrt{u_N}+\delta_N)^2.
}
\]

In particular,

\[
\boxed{
\delta_N<1-\sqrt{u_N}
}
\]

is sufficient for strict odd positivity.

#### Proof

For every source state,

\[
|L_\partial f|
\le
|\langle c_N,\Xi_0f\rangle|
+|r_N(f)|
\le
(\|c_N\|+\delta_N)\|\Xi_0f\|.
\]

Take the supremum over nonzero event images. ∎

This theorem converts event orientation into a quantitative target.  It does not
require exact equality before useful progress can be certified.

---

## 8. Direct unshifted T21 scalar ledger

The imported source packet records

```text
first-cell upper       0.00007670975092815261
active-band upper      0.2976678523563374
outside upper          0.5313410580584792
reported beta upper    0.8290856201657449
reported reserve       0.1709143798342551
active cells           2400
prime-power events     78734
```

The exact decimal sum of the three displayed components is

\[
0.82908562016574475261,
\]

so the reported value is outward and strictly below one.

If this scalar bound is attached to a decoder on the actual event orientation,
then the robust orientation theorem leaves the residual budget

\[
\boxed{
1-\sqrt{0.8290856201657449}
=0.0894586115031646185\ldots
}
\]

in the source norm.

For example, an outward orientation residual of \(0.08\) would give

\[
(\sqrt{0.8290856201657449}+0.08)^2
=0.98117224232523856\ldots<1.
\]

This is a large and useful reserve.  But the scalar ledger alone does not prove
that its cell masses form the actual decoder of \(L_\partial\).  The next stage
must build or enclose that same-event orientation residual.

---

## 9. RH specialization contract

The actual odd completed-Weil gate is now precise.

### Already declared

```text
native odd carrier X3^-;
boundary formula L_partial f = sqrt(2) f-hat(i/2);
positive odd source S_(0,-)^full;
source analysis statement Xi_0^* Xi_0 = S_(0,-)^full;
direct unshifted scalar envelope from T21.
```

### Still required in RKF

```text
1. coefficientwise prime/Gamma/diagonal-debt event map Xi_Weil,N;
2. boundary coefficients on those same oriented events;
3. recovered identity between successive event refinements;
4. Recognition-Cauchy and Smriti-tail convergence to Xi_0 and L_partial;
5. exact or outward orientation residual delta_N;
6. actual boundary-line no-blindness for Q_partial Xi_0.
```

Only after these gates close may one write

\[
S_{0,-}^{\rm full}-L_\partial^*L_\partial
=Z_{\rm Weil,-}^*Q_\partial Z_{\rm Weil,-}
\ge0
\]

as a theorem about the completed-Weil object.

---

## 10. Exact executable calibrations

The Stage-3A packet verifies:

```text
finite first/second-moment co-generation;
constructive unit boundary-state enlargement;
cut covariance and no-blindness;
exact shifted endpoint identity;
coherent refinement equality;
same-mass opposite-orientation negative control;
nonproportional refinement burden increase;
T21 decimal arithmetic and orientation-residual budget;
fail-closed RH contract.
```

The exact code is

```text
proof_lab/native_weil_cut_event_cogeneration.py
proof_lab/test_native_weil_cut_event_cogeneration.py
```

---

## 11. Claim boundary

```text
finite oriented event theorem                     PROVED
contractive decoder <=> unit-state co-generation  PROVED CONSTRUCTIVELY
shifted endpoint difference identity              PROVED
refinement burden monotonicity                     PROVED
Recognition-complete co-generation implication    PROVED
robust orientation residual theorem               PROVED
T21 scalar arithmetic                             AUDITED

actual prime/Gamma/debt event orientation          NEXT
actual orientation residual                        NEXT
actual completed-Weil cut covariance               NOT YET PROVED HERE
RH                                                  NOT CLAIMED
```
