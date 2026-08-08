# MR-03 — Cocycle-Lifted Path Recognition

## 1. Purpose

Endpoint equality need not determine path identity when lawful memory is created by composition.

A controlled way to retain such memory is to lift the native morphism category by an abelian memory coordinate whose composition defect is governed by a cocycle.

This construction is standard extension/cohomology mathematics. Its role here is to supply a rigorous **clock-free recognition carrier for path memory**.

---

## 2. Native category and memory group

Let `C` be a small category. Write

\[
a:x\to y,
\qquad
b:y\to z
\]

for composable arrows.

Let `M` be an abelian group written additively.

Let

\[
\omega(b,a)\in M
\]

be defined on composable pairs.

### Definition 2.1 — Normalized memory cocycle

`omega` is normalized when

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

This is exactly the equality required by the two bracketings of a three-arrow composition.

---

## 3. Memory-lifted category

Define a lifted arrow over `a:x->y` to be a pair

\[
(m,a),
\qquad
m\in M.
\]

Define

\[
\widetilde{\operatorname{id}}_x
=(0,\operatorname{id}_x)
\]

and composition

\[
\boxed{
(n,b)\star(m,a)
=
\bigl(n+m+\omega(b,a),\,b\circ a\bigr).
}
\]

### Theorem 3.1 — Cocycle-Lifted Associativity

The operation `star` is associative if and only if `omega` obeys the cocycle identity.

When `omega` is normalized, `(0,id_x)` is a two-sided identity. Therefore the lifted structure is a category, denoted

\[
\widetilde{\mathcal C}_\omega.
\]

### Proof

For a composable triple, the memory coordinate of

\[
(p,c)\star((n,b)\star(m,a))
\]

is

\[
p+n+m+\omega(b,a)+\omega(c,b\circ a).
\]

The memory coordinate of

\[
((p,c)\star(n,b))\star(m,a)
\]

is

\[
p+n+m+\omega(c,b)+\omega(c\circ b,a).
\]

The projected arrow is `c o b o a` in both cases. Hence the lifted compositions agree for every triple if and only if the cocycle identity holds.

Normalization gives the identity laws directly. ∎

---

## 4. Forgetful projection

Define

\[
\pi:\widetilde{\mathcal C}_\omega\to\mathcal C,
\qquad
\pi(m,a)=a.
\]

### Proposition 4.1

`pi` is a functor.

### Proof

It preserves identities and

\[
\pi((n,b)\star(m,a))
=b\circ a
=\pi(n,b)\circ\pi(m,a).
\]

∎

### Corollary 4.2 — Same projection, different recognition memory

For any arrow `a` and `m != n`,

\[
\pi(m,a)=\pi(n,a)=a,
\]

while

\[
(m,a)\neq(n,a).
\]

Thus projection equality is strictly weaker than equality in the memory-lifted recognition carrier whenever nonzero memory is admitted.

---

## 5. Memory of a path

Let

\[
\gamma=a_k\cdots a_2a_1
\]

be a composable path and lift each elementary arrow with zero initial memory:

\[
\widetilde a_j=(0,a_j).
\]

By associativity there is a unique

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

If `omega` is a normalized cocycle, the accumulated memory

\[
\Omega_\omega(\gamma)
\]

is independent of parenthesization.

### Proof

Every parenthesization gives the same lifted composite because `star` is associative by Theorem 3.1. Therefore its memory coordinate is unique. ∎

For two arrows,

\[
\Omega_\omega(ba)=\omega(b,a).
\]

For three arrows,

\[
\Omega_\omega(cba)
=
\omega(b,a)+\omega(c,b\circ a)
=
\omega(c,b)+\omega(c\circ b,a).
\]

---

## 6. Path-recognition equivalence

Suppose two composable histories `gamma` and `eta` have the same projected composite:

\[
\gamma=\eta
\qquad\text{in }\mathcal C.
\]

### Definition 6.1 — Memory-complete path equivalence

They are recognition-equivalent under the cocycle lift when

\[
\boxed{
\gamma\sim_\omega\eta
\iff
\gamma=\eta
\text{ in }\mathcal C
\text{ and }
\Omega_\omega(\gamma)=\Omega_\omega(\eta).
}
\]

### Theorem 6.2 — Endpoint/projected equality is insufficient

If

\[
\gamma=\eta
\]

in the projected category but

\[
\Omega_\omega(\gamma)\neq\Omega_\omega(\eta),
\]

then the two paths are distinct in the lifted recognition category.

### Proof

Their lifted composites are

\[
(\Omega_\omega(\gamma),\gamma)
\]

and

\[
(\Omega_\omega(\eta),\eta).
\]

The second coordinates agree but the first do not, so the lifted arrows are unequal. ∎

This is the categorical form of:

```text
same visible morphism does not imply same recognized history.
```

---

## 7. Clock independence

No clock, duration, infinitesimal parameter, norm, or Hilbert basis appears in Sections 2–6.

A clock may later label or measure a path,

\[
\tau:\operatorname{Mor}(\mathcal C)\to T,
\]

but the cocycle law and the lifted composition are already defined.

Therefore the memory class is **clock-free at the algebraic level**. A later clocked rate or representation is a shadow of the lifted morphism, not its definition.

---

## 8. Gauge/coboundary change

Let

\[
\alpha:\operatorname{Mor}(\mathcal C)\to M
\]

be a normalized 1-cochain and define

\[
\omega'(b,a)
=
\omega(b,a)
+\alpha(b\circ a)-\alpha(b)-\alpha(a).
\]

Then the map

\[
\Phi_\alpha(m,a)
=
(m-\alpha(a),a)
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
(n+m+\omega(b,a)-\alpha(b\circ a),b\circ a),
\end{aligned}
\]

while

\[
\begin{aligned}
\Phi_\alpha(n,b)\star_{\omega'}\Phi_\alpha(m,a)
&=
(n-\alpha(b)+m-\alpha(a)+\omega'(b,a),b\circ a)\\
&=
(n+m+\omega(b,a)-\alpha(b\circ a),b\circ a).
\end{aligned}
\]

Thus composition is preserved, and the inverse is obtained using `-alpha`. ∎

So a coboundary changes the memory coordinate convention, not the isomorphism class of the lifted recognition structure.

---

## 9. Exact calibration monoid

Use a one-object category whose arrows are integers under addition:

\[
a\circ b=a+b.
\]

Take

\[
M=\mathbb Z
\]

and

\[
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

so the cocycle law holds exactly.

A deliberately bad rule such as

\[
\omega_{\rm bad}(b,a)=ba^2
\]

fails the cocycle identity for suitable triples and therefore produces a non-associative lift. This is used as an RNKE negative control.

---

## 10. Relation to the source manuscripts and RSC

The source Morphic Algebra develops twisted traces, cocycles, central extensions and holonomy. MR-03 extracts only the algebraically standard extension theorem required for Recognition-Kernel path memory.

Theorem 24 supplies clock-free composition residues; Theorem 27 requires path holonomy/recovered middle identity in recognition completion. MR-03 supplies a clean carrier in which such lawful path memory can be stored without making a clock primitive.

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
MR03-N2  omega_bad(b,a)=ba^2 produces an explicit associativity-failure witness
```

## 12. Status

```text
GENERAL CATEGORY/COCYCLE PROOF              PROVED
CONSTRUCTION NOVELTY                         NOT CLAIMED; STANDARD EXTENSION MATHEMATICS
RECOGNITION-KERNEL ROLE                      NEW FRAMEWORK SPECIALIZATION / INTEGRATION
DEPENDENCE ON CLOCK                          NONE
RNKE PROOF-CONTRACT CALIBRATION              SEE proof_lab/morphic_recognition
FORMAL PROOF-ASSISTANT CERTIFICATE           NOT CLAIMED
```
