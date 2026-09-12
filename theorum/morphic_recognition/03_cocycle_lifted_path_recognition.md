# MR-03 — Cocycle-Lifted Path Recognition

## 1. Purpose

Endpoint equality need not determine path identity when lawful memory is created by composition.

A controlled way to retain such memory is to lift the native morphism category by an abelian memory coordinate whose composition defect is governed by a cocycle.

This construction is standard extension/cohomology mathematics. Its role here is to supply a rigorous **clock-free recognition carrier for path memory** while remaining bound by the Ś-0 Emptiness Guard of the Morphic framework.

---

## 2. Native category and memory group

Let \(\mathcal C\) be a small category and let \(M\) be an abelian group written additively. For composable arrows

\[
a:x\to y,
\qquad
b:y\to z,
\]

let

\[
\omega(b,a)\in M.
\]

### Definition 2.1 — Normalized memory cocycle

The map \(\omega\) is normalized when

\[
\omega(\operatorname{id}_y,a)=0,
\qquad
\omega(a,\operatorname{id}_x)=0,
\]

and for every composable triple

\[
x\xrightarrow{a}y\xrightarrow{b}z\xrightarrow{c}w
\]

one has

\[
\boxed{
\omega(c,b\circ a)+\omega(b,a)
=
\omega(c\circ b,a)+\omega(c,b).
}
\]

---

## 3. Memory-lifted category

A lifted arrow over \(a:x\to y\) is a pair

\[
(m,a),\qquad m\in M.
\]

Define

\[
\widetilde{\operatorname{id}}_x=(0,\operatorname{id}_x)
\]

and

\[
\boxed{
(n,b)\star(m,a)
=
\bigl(n+m+\omega(b,a),\,b\circ a\bigr).
}
\]

### Theorem 3.1 — Cocycle-Lifted Associativity

The operation \(\star\) is associative if and only if \(\omega\) obeys the cocycle identity. If \(\omega\) is normalized, \((0,\operatorname{id}_x)\) is a two-sided identity, so the lift is a category \(\widetilde{\mathcal C}_\omega\).

### Proof

The memory coordinate of

\[
(p,c)\star((n,b)\star(m,a))
\]

is

\[
p+n+m+\omega(b,a)+\omega(c,b\circ a),
\]

while the memory coordinate of

\[
((p,c)\star(n,b))\star(m,a)
\]

is

\[
p+n+m+\omega(c,b)+\omega(c\circ b,a).
\]

The projected composite is \(c\circ b\circ a\) in both cases. Thus associativity is equivalent exactly to the cocycle identity. Normalization gives the identity laws. ∎

---

## 4. Forgetful projection and path blindness

Define

\[
\pi:\widetilde{\mathcal C}_\omega\to\mathcal C,
\qquad
\pi(m,a)=a.
\]

### Proposition 4.1

\(\pi\) is a functor.

### Proof

It preserves identities and

\[
\pi((n,b)\star(m,a))
=b\circ a
=\pi(n,b)\circ\pi(m,a).
\]

∎

### Corollary 4.2 — Same projection, different recognition memory

For any arrow \(a\) and \(m\neq n\),

\[
\pi(m,a)=\pi(n,a)=a,
\]

but

\[
(m,a)\neq(n,a).
\]

Thus projected equality is strictly weaker than equality in the memory-lifted recognition carrier whenever nonzero memory is admitted.

---

## 5. Memory of a composable path

Let

\[
\gamma=a_k\cdots a_2a_1
\]

be a composable path and lift each elementary arrow as \(\widetilde a_j=(0,a_j)\). By associativity there is a unique

\[
\Omega_\omega(\gamma)\in M
\]

such that

\[
\boxed{
\widetilde a_k\star\cdots\star\widetilde a_1
=
(\Omega_\omega(\gamma),\gamma).
}
\]

### Proposition 5.1 — Parenthesization independence

If \(\omega\) is a normalized cocycle, \(\Omega_\omega(\gamma)\) is independent of parenthesization.

### Proof

Every parenthesization gives the same lifted composite by Theorem 3.1, hence the same memory coordinate. ∎

For two arrows,

\[
\Omega_\omega(ba)=\omega(b,a),
\]

and for three,

\[
\Omega_\omega(cba)
=
\omega(b,a)+\omega(c,b\circ a)
=
\omega(c,b)+\omega(c\circ b,a).
\]

---

## 6. Memory-complete path recognition

### Definition 6.1

For two histories \(\gamma,\eta\) with the same projected composite, define

\[
\boxed{
\gamma\sim_\omega\eta
\iff
\gamma=\eta\text{ in }\mathcal C
\quad\text{and}\quad
\Omega_\omega(\gamma)=\Omega_\omega(\eta).
}
\]

### Theorem 6.2 — Projected equality is insufficient

If

\[
\gamma=\eta\text{ in }\mathcal C
\]

but

\[
\Omega_\omega(\gamma)\neq\Omega_\omega(\eta),
\]

then the histories are distinct in \(\widetilde{\mathcal C}_\omega\).

### Proof

Their lifted composites have the same second coordinate and different first coordinates, hence are unequal. ∎

---

## 7. Clock independence

No clock, duration, infinitesimal parameter, norm, or Hilbert basis occurs in the construction above. A clock may later measure or label a path, but the cocycle law and memory lift already exist.

Thus path memory is clock-free at the algebraic level. A clocked rate is a later representation of the morphism, not its definition.

---

## 8. Gauge / coboundary change

Let

\[
\alpha:\operatorname{Mor}(\mathcal C)\to M
\]

be a normalized 1-cochain and define

\[
\boxed{
\omega'(b,a)
=
\omega(b,a)
+\alpha(b\circ a)-\alpha(b)-\alpha(a).
}
\]

### Theorem 8.1 — Coboundary Gauge Isomorphism

The map

\[
\boxed{
\Phi_\alpha(m,a)
=
(m+\alpha(a),a)
}
\]

is an isomorphism

\[
\widetilde{\mathcal C}_\omega
\cong
\widetilde{\mathcal C}_{\omega'}.
\]

### Proof

For composable lifted arrows,

\[
\begin{aligned}
\Phi_\alpha((n,b)\star_\omega(m,a))
&=
(n+m+\omega(b,a)+\alpha(b\circ a),b\circ a).
\end{aligned}
\]

On the other hand,

\[
\begin{aligned}
\Phi_\alpha(n,b)\star_{\omega'}\Phi_\alpha(m,a)
&=
(n+\alpha(b)+m+\alpha(a)+\omega'(b,a),b\circ a)\\
&=
(n+m+\omega(b,a)+\alpha(b\circ a),b\circ a).
\end{aligned}
\]

Thus composition is preserved. The inverse uses the coordinate change \((m,a)\mapsto(m-\alpha(a),a)\). ∎

The sign in this theorem is part of the verified statement: for the displayed convention for \(\omega'\), the forward coordinate change is \(+\alpha\), not \(-\alpha\).

---

## 9. Exact calibration monoid

Use a one-object category whose arrows are integers under addition and set

\[
M=\mathbb Z,
\qquad
\omega(b,a)=ba.
\]

Then

\[
\omega(c,b+a)+\omega(b,a)
=cb+ca+ba
\]

and

\[
\omega(c+b,a)+\omega(c,b)
=ca+ba+cb,
\]

so the cocycle identity holds exactly.

The deliberately bad rule

\[
\omega_{\rm bad}(b,a)=ba^2
\]

fails the cocycle identity for suitable triples and therefore gives a non-associative lift.

---

## 10. Relation to Śūnya, Nāgārjuna and Morphic Algebra

This theorem remains governed by the Ś-0 Emptiness Guard: the lifted category and its memory coordinate are conditional mathematical constructions, not ontological claims.

The N-0 Nāgārjuna / Catuṣkoṭi layer is retained unchanged in the framework vocabulary. MR-03 does not require a truth-value reduction of the memory group and therefore does not silently collapse the Catuṣkoṭi layer into Boolean semantics.

The source Morphic Algebra develops cocycles, twisted trace, holonomy and central extensions. MR-03 isolates the theorem-grade categorical core needed by Recognition-Kernel path memory.

---

## 11. RNKE proof contract

```text
MR03-O1  cocycle identity is necessary and sufficient for lifted associativity
MR03-O2  normalized cocycle gives two-sided identities
MR03-O3  forgetful projection is functorial
MR03-O4  accumulated path memory is parenthesization independent
MR03-O5  same projection with different memory is not lifted equality
MR03-O6  coboundary-related cocycles give isomorphic lifted categories
MR03-N1  omega(b,a)=ba satisfies the cocycle identity on the exact integer calibration domain
MR03-N2  omega_bad(b,a)=ba^2 gives an explicit associativity-failure witness
MR03-N3  the wrong-sign coboundary coordinate change fails an exact calibration case
```

## 12. Status

```text
GENERAL CATEGORY/COCYCLE PROOF              PROVED_ALGEBRAICALLY
COBOUNDARY SIGN                              CORRECTED BY EXACT PROOF/NEGATIVE CONTROL
CONSTRUCTION NOVELTY                         NOT CLAIMED; STANDARD EXTENSION MATHEMATICS
RECOGNITION-KERNEL ROLE                      FRAMEWORK SPECIALIZATION / INTEGRATION
DEPENDENCE ON CLOCK                          NONE
RNKE PROOF-CONTRACT CALIBRATION              SEE proof_lab/morphic_recognition
FORMAL PROOF-ASSISTANT CERTIFICATE           NOT CLAIMED
```
