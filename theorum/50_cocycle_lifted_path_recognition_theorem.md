# Cocycle-Lifted Path Recognition Theorem

## 1. Purpose

Endpoint equality does not determine path identity when lawful memory is created
by composition. A mathematically controlled way to retain that memory is to
lift the original morphism category by an abelian memory coordinate whose
composition defect is governed by a cocycle.

This note proves the associative memory lift, shows that the endpoint projection
forgets path information, and identifies the exact condition under which two
projected-equivalent histories remain distinct after recognition memory is
restored.

The construction is standard in the language of extensions/cohomology. Its role
here is foundational: it supplies a rigorous Recognition-Kernel carrier for
path memory without making the clock, endpoint, or a particular representation
primitive.

---

## 2. Native category and memory group

Let \(\mathcal C\) be a small category. Write

\[
a:x\to y,
\qquad
b:y\to z
\]

for composable arrows.

Let \(M\) be an abelian group written additively. Let

\[
\omega(b,a)\in M
\]

be defined on composable pairs.

### Definition 2.1 (Normalized memory cocycle)

The map \(\omega\) is a normalized memory cocycle when

\[
\omega(\mathrm{id}_y,a)=0,
\qquad
\omega(a,\mathrm{id}_x)=0,
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

This identity is exactly the compatibility required by the two bracketings of a
three-arrow composition.

---

## 3. Memory-lifted category

Define a category candidate \(\widetilde{\mathcal C}_\omega\) with the same
objects as \(\mathcal C\). A lifted arrow over \(a:x\to y\) is a pair

\[
(m,a),
\qquad
m\in M.
\]

Define identity arrows by

\[
\widetilde{\mathrm{id}}_x=(0,\mathrm{id}_x)
\]

and composition by

\[
\boxed{
(n,b)\star(m,a)
=
\bigl(n+m+\omega(b,a),\,b\circ a\bigr).
}
\]

### Theorem 3.1 (Cocycle-Lifted Associativity)

The operation \(\star\) is associative if and only if \(\omega\) satisfies the
memory cocycle identity.

When \(\omega\) is normalized, \((0,\mathrm{id}_x)\) is a two-sided identity.
Hence \(\widetilde{\mathcal C}_\omega\) is a category.

### Proof

For a composable triple of lifted arrows,

\[
(p,c)\star\bigl((n,b)\star(m,a)\bigr)
\]

has memory coordinate

\[
p+n+m+\omega(b,a)+\omega(c,b\circ a).
\]

The other bracketing

\[
\bigl((p,c)\star(n,b)\bigr)\star(m,a)
\]

has memory coordinate

\[
p+n+m+\omega(c,b)+\omega(c\circ b,a).
\]

The projected arrow is \(c\circ b\circ a\) in both cases by associativity in
\(\mathcal C\). Therefore the lifted compositions agree exactly when

\[
\omega(c,b\circ a)+\omega(b,a)
=
\omega(c\circ b,a)+\omega(c,b).
\]

Normalization gives

\[
(0,\mathrm{id}_y)\star(m,a)=(m,a)
\]

and

\[
(m,a)\star(0,\mathrm{id}_x)=(m,a).
\]

∎

---

## 4. Forgetful projection and hidden path memory

Define

\[
\pi:\widetilde{\mathcal C}_\omega\to\mathcal C,
\qquad
\pi(m,a)=a.
\]

### Proposition 4.1 (Forgetful projection)

The map \(\pi\) is a functor.

### Proof

It preserves identities, and

\[
\pi\bigl((n,b)\star(m,a)\bigr)
=b\circ a
=\pi(n,b)\circ\pi(m,a).
\]

∎

The projection therefore preserves the visible/native arrow while discarding
the memory coordinate.

### Corollary 4.2 (Same projection, different recognition state)

For any arrow \(a\) and any \(m\ne n\) in \(M\),

\[
\pi(m,a)=\pi(n,a)=a
\]

but

\[
(m,a)\ne(n,a).
\]

Thus endpoint/projected equality is strictly weaker than equality in the
memory-lifted recognition category whenever nonzero memory is admitted.

---

## 5. Memory of a composable path

Let

\[
\gamma=a_k\cdots a_2a_1
\]

be a composable path in \(\mathcal C\). Lift each elementary arrow with zero
initial memory:

\[
\widetilde a_j=(0,a_j).
\]

Define the lifted path

\[
\widetilde\gamma
=
\widetilde a_k\star\cdots\star\widetilde a_1.
\]

There is a unique memory element \(\Omega_\omega(\gamma)\in M\) such that

\[
\boxed{
\widetilde\gamma
=
\bigl(\Omega_\omega(\gamma),\,\gamma\bigr).
}
\]

Associativity makes \(\Omega_\omega(\gamma)\) independent of parenthesization.
It records the accumulated lawful composition memory of the path.

### Proposition 5.1 (Two-step path memory)

For a two-step path \(ba\),

\[
\boxed{
\Omega_\omega(ba)=\omega(b,a).
}
\]

For a three-step path \(cba\), either bracketing gives

\[
\boxed{
\Omega_\omega(cba)
=
\omega(b,a)+\omega(c,ba)
=
\omega(c,b)+\omega(cb,a).
}
\]

The equality is exactly the cocycle law.

---

## 6. Path-recognition equivalence

Suppose two paths \(\gamma\) and \(\eta\) have the same projected composite:

\[
\gamma=\eta
\qquad\text{as arrows of }\mathcal C.
\]

They may nevertheless accumulate different recognition memories.

### Definition 6.1 (Cocycle-complete path equivalence)

Define

\[
\boxed{
\gamma\sim_\omega\eta
\iff
\gamma=\eta\text{ in }\mathcal C
\quad\text{and}\quad
\Omega_\omega(\gamma)=\Omega_\omega(\eta).
}
\]

### Theorem 6.2 (Path Recognition Separation)

Let \(\gamma\) and \(\eta\) be paths with the same projected composite. Then

\[
\boxed{
\widetilde\gamma=\widetilde\eta
\iff
\Omega_\omega(\gamma)=\Omega_\omega(\eta).
}
\]

Consequently, if

\[
\Omega_\omega(\gamma)-\Omega_\omega(\eta)\ne0,
\]

then no endpoint-only equality in \(\mathcal C\) can identify the two histories
inside the lifted recognition category.

### Proof

The paths have a common projection \(a\). Therefore

\[
\widetilde\gamma=(\Omega_\omega(\gamma),a),
\qquad
\widetilde\eta=(\Omega_\omega(\eta),a).
\]

Equality of ordered pairs is equivalent to equality of their memory coordinates.
∎

This is the exact form of

```text
same endpoint + different lawful memory = different recognized path.
```

---

## 7. Loop holonomy

Let \(\gamma:x\to x\) be a loop whose projection is the identity arrow:

\[
\gamma=\mathrm{id}_x
\qquad\text{in }\mathcal C.
\]

Its lifted value is

\[
\widetilde\gamma
=
\bigl(\Omega_\omega(\gamma),\mathrm{id}_x\bigr).
\]

### Definition 7.1 (Memory holonomy)

Define

\[
\operatorname{Hol}_\omega(\gamma)
:=
\Omega_\omega(\gamma).
\]

### Corollary 7.2 (Visible return does not imply recognition return)

If

\[
\operatorname{Hol}_\omega(\gamma)\ne0,
\]

then the projected loop returns to the visible identity while the lifted
recognition state does not:

\[
\pi(\widetilde\gamma)=\mathrm{id}_x,
\qquad
\widetilde\gamma\ne(0,\mathrm{id}_x).
\]

This is a categorical path-memory obstruction requiring no external clock.

---

## 8. Gauge change

Let

\[
\alpha:\operatorname{Mor}(\mathcal C)\to M
\]

be a normalized 1-cochain with \(\alpha(\mathrm{id})=0\). Define a new cocycle

\[
\boxed{
\omega'(b,a)
=
\omega(b,a)
+\alpha(b\circ a)-\alpha(b)-\alpha(a).
}
\]

Define

\[
\Phi_\alpha:
\widetilde{\mathcal C}_\omega
\to
\widetilde{\mathcal C}_{\omega'},
\qquad
\Phi_\alpha(m,a)
=
(m-\alpha(a),a).
\]

### Theorem 8.1 (Gauge-Equivalent Memory Lifts)

The map \(\Phi_\alpha\) is an isomorphism of categories over \(\mathcal C\).
Hence cohomologous memory cocycles define equivalent lifted recognition
categories.

### Proof

For composable \((n,b),(m,a)\),

\[
\Phi_\alpha\bigl((n,b)\star_\omega(m,a)\bigr)
\]

has memory coordinate

\[
n+m+\omega(b,a)-\alpha(ba).
\]

On the other hand,

\[
\Phi_\alpha(n,b)\star_{\omega'}\Phi_\alpha(m,a)
\]

has coordinate

\[
n-\alpha(b)+m-\alpha(a)+\omega'(b,a),
\]

which becomes the same quantity after substituting the definition of
\(\omega'\). The inverse is obtained using \(-\alpha\). ∎

The absolute memory coordinate depends on gauge, but the lifted category up to
isomorphism and the distinction between gauge-equivalent path classes are
presentation-stable.

---

## 9. Recognition-Kernel interpretation

The theorem supplies a native pattern for lawful history retention:

```text
base morphism                     a
lawful accumulated memory         Omega_omega(path)
lifted recognized morphism        (Omega_omega(path), a)
```

A commitment system that verifies only the projection \(a\) is complete only
when the memory coordinate is irrelevant to the declared target or when a
separate theorem proves that the relevant holonomy vanishes.

Otherwise the memory lift is required before endpoint equality may be promoted
to recognition equality.

This construction is compatible with the Recognition-Seam principle that
visible return and state/recognition return are different statements.

---

## 10. Relation to the Path Blindness Theorem

The cocycle lift is nonlinear/categorical at the primitive level. In a declared
finite-dimensional linearized path sector, its memory coordinate can be
observed by a linear bank. The Path Blindness and Minimal Memory Repair Theorem
then determines the minimum number of scalar channels needed to preserve the
target-relevant part of that path memory.

Thus the two theorems have different jobs:

```text
Theorem 50: construct lawful compositional memory without a clock.
Theorem 49: determine how much of a linearized memory sector must be observed.
```

---

## 11. Claim boundary

```text
associativity iff cocycle identity             PROVED
forgetful projection is functor                PROVED
same endpoint may carry different memory       PROVED
path-recognition separation                    PROVED
visible-return / memory-holonomy separation    PROVED
gauge-equivalent cocycles give isomorphic lifts PROVED

claim that every physical/history effect is a cocycle NOT MADE
claim that the construction is novel cohomology       NOT MADE
application-specific memory cocycle existence          NOT MADE
```

The mathematical role is foundational and reusable. Any stronger novelty claim
requires comparison with the existing theory of categorical/group extensions,
cohomology, holonomy and provenance systems.