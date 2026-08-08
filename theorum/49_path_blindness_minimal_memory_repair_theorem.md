# Path Blindness and Minimal Memory Repair Theorem

## 1. Purpose

Two admissible histories may have the same displayed endpoint while differing in
a target property that depends on the path. Any verifier that sees only the
endpoint is then blind to a target-relevant direction.

This note gives the exact finite-dimensional linear criterion for endpoint
faithfulness and the minimum number of supplemental scalar memory channels
required to repair endpoint blindness.

It is the path-space specialization of the target-relative recognition/blindness
principle. It is stated here because the path object, rather than the endpoint,
is the primitive morphic carrier needed by dynamic Recognition-Kernel systems.

---

## 2. Linear path sector

Let \(\mathbb F\in\{\mathbb R,\mathbb C\}\). Let

\[
\mathcal P
\]

be a finite-dimensional vector space of path descriptors or finite morphic
histories. Let

\[
E:\mathcal P\to Y
\]

be the endpoint/visible observation map and let

\[
\Pi:\mathcal P\to Z
\]

be the declared path target.

The target may encode any linear path property whose preservation matters after
the endpoint is forgotten: accumulated memory, signed transport, authorization
history, winding class in a linearized sector, or another declared quantity.

Define the endpoint-blind kernel

\[
K:=\ker E.
\]

Directions in \(K\) change the path descriptor without changing the visible
endpoint observation.

### Definition 2.1 (Path-target faithfulness)

The endpoint observation \(E\) is path-target faithful when

\[
\boxed{
\ker E\subseteq\ker\Pi.
}
\]

Equivalently, every endpoint-invisible path difference is also irrelevant to
the declared target.

### Definition 2.2 (Path-blind quotient)

Define

\[
\boxed{
\mathcal B_{\rm path}(E,\Pi)
:=
\ker E/(\ker E\cap\ker\Pi).
}
\]

This quotient removes endpoint-blind directions that are also target-null and
retains exactly the endpoint-blind directions visible to the path target.

---

## 3. Exact path-blind representation

### Proposition 3.1 (Path-blind quotient representation)

The map

\[
\widetilde\Pi:
\mathcal B_{\rm path}(E,\Pi)
\to
\Pi(\ker E),
\qquad
[k]\mapsto\Pi k,
\]

is a linear isomorphism. Consequently,

\[
\boxed{
\dim\mathcal B_{\rm path}(E,\Pi)
=
\operatorname{rank}(\Pi|_{\ker E}).
}
\]

### Proof

If \(k-k'\in\ker E\cap\ker\Pi\), then \(\Pi k=\Pi k'\), so the map is well
defined. It is surjective by construction. Its kernel consists of classes
\([k]\) with \(k\in\ker E\cap\ker\Pi\), hence only the zero class. ∎

---

## 4. Endpoint-only impossibility criterion

### Theorem 4.1 (Endpoint Decoder Criterion)

The following are equivalent:

1. \(E\) is path-target faithful;
2. there exists a unique linear map
   \[
   D:\operatorname{ran}E\to Z
   \]
   such that
   \[
   \boxed{\Pi=DE;}
   \]
3. \(\mathcal B_{\rm path}(E,\Pi)=\{0\}\).

### Proof

If \(\Pi=DE\), then \(Ek=0\) implies \(\Pi k=D0=0\), so
\(\ker E\subseteq\ker\Pi\).

Conversely, assume \(\ker E\subseteq\ker\Pi\). Define

\[
D(Ep):=\Pi p.
\]

If \(Ep=Eq\), then \(p-q\in\ker E\subseteq\ker\Pi\), so
\(\Pi p=\Pi q\). Thus \(D\) is well defined and linear. Uniqueness is forced on
\(\operatorname{ran}E\). The equivalence with the zero quotient follows from
the definition of \(\mathcal B_{\rm path}\). ∎

### Corollary 4.2 (Exact endpoint-only no-go)

If

\[
\mathcal B_{\rm path}(E,\Pi)\ne\{0\},
\]

then no linear endpoint-only verifier/decoder can recover the declared path
target on all of \(\mathcal P\).

Moreover, there exist \(p,q\in\mathcal P\) such that

\[
Ep=Eq
\]

but

\[
\Pi p\ne\Pi q.
\]

### Proof

Choose \(k\in\ker E\) with \(\Pi k\ne0\). For any \(p\), put \(q=p+k\).
Then \(Eq=Ep\) while \(\Pi q=\Pi p+\Pi k\ne\Pi p\). ∎

This is the exact mathematical form of

```text
same endpoint does not imply same recognized path.
```

---

## 5. Supplemental path memory

Let

\[
G:\mathcal P\to\mathbb F^m
\]

be a bank of \(m\) scalar path-memory probes. Define the repaired observation

\[
F=(E,G):\mathcal P\to Y\oplus\mathbb F^m.
\]

### Definition 5.1 (Target-complete path memory)

The memory bank \(G\) is target-complete when

\[
\boxed{
\ker(E,G)\subseteq\ker\Pi.
}
\]

---

## 6. Minimum memory theorem

### Theorem 6.1 (Path Blindness and Minimal Memory Repair)

Let

\[
r
:=
\dim\mathcal B_{\rm path}(E,\Pi)
=
\operatorname{rank}(\Pi|_{\ker E}).
\]

Among all arbitrary scalar linear memory banks

\[
G:\mathcal P\to\mathbb F^m,
\]

the minimum number of channels required to make \((E,G)\) target-complete is

\[
\boxed{m_{\min}=r.}
\]

### Proof

Let \(K=\ker E\).

**Lower bound.** Suppose \(G:\mathcal P\to\mathbb F^m\) is target-complete.
Then

\[
\ker(G|_K)
\subseteq
K\cap\ker\Pi.
\]

Therefore \(G|_K\) induces an injective linear map

\[
\overline G:
K/(K\cap\ker\Pi)
\hookrightarrow
\mathbb F^m.
\]

Hence

\[
m\ge\dim K/(K\cap\ker\Pi)=r.
\]

**Achievability.** Choose a linear map

\[
G_K:K\to\mathbb F^r
\]

with

\[
\ker G_K=K\cap\ker\Pi.
\]

Such a map exists by choosing coordinates on the quotient
\(K/(K\cap\ker\Pi)\). Extend \(G_K\) linearly from \(K\) to all of
\(\mathcal P\). If \(Ep=0\) and \(Gp=0\), then \(p\in K\) and

\[
p\in\ker G_K=K\cap\ker\Pi.
\]

Thus \(\Pi p=0\), so \((E,G)\) is target-complete with exactly \(r\) scalar
channels. ∎

### Corollary 6.2 (No unnecessary full-history storage)

Full path reconstruction is not required when the target sees only an
\(r\)-dimensional image of the endpoint-blind kernel. Exactly \(r\) arbitrary
scalar memory channels suffice and, in general, fewer cannot suffice.

Thus the minimum lawful memory is target-relative rather than equal to the full
dimension of path history.

---

## 7. Stable decoder version

Assume now that \(\mathcal P,Y,Z\) are normed spaces, with \(\mathcal P\)
finite-dimensional for the minimal-rank conclusion, and let

\[
F=(E,G).
\]

If there exists \(c>0\) such that

\[
\|Fp\|\ge c\,\operatorname{dist}(p,\ker\Pi)
\qquad(p\in\mathcal P),
\]

then the induced target decoder on \(\operatorname{ran}F\) is bounded. In the
special case that \(F\) is injective and

\[
\|Fp\|\ge c\|p\|,
\]

one has

\[
\|\Pi p\|
\le
\frac{\|\Pi\|}{c}\|Fp\|.
\]

This separates two obligations:

```text
rank completeness   -> no exact path-blind escape;
stability margin    -> no arbitrarily amplified near-blind escape.
```

---

## 8. Relationship to morphic recognition

The theorem applies after a finite path sector has been linearized. It does not
claim that every path space is naturally linear.

In a nonlinear recognition category, one first defines admissible paths and a
typed endpoint observation. A lawful linear/abelian recognition fiber may then
represent the path differences relevant to the declared target. Only inside
that declared sector is the quotient above taken.

The operational lesson is nevertheless representation independent:

```text
if the endpoint forgets a target-relevant distinction,
that distinction must be retained by a faithful memory/observer channel
before commitment.
```

---

## 9. Exact finite calibration

Take

\[
\mathcal P=\mathbb R^3,
\qquad
E(x,y,z)=x,
\qquad
\Pi(x,y,z)=(y,z).
\]

Then

\[
\ker E=\{0\}\times\mathbb R^2,
\]

and

\[
\Pi|_{\ker E}
\]

has rank two. Therefore

\[
\boxed{m_{\min}=2.}
\]

No endpoint-only decoder can recover \((y,z)\). The memory bank

\[
G(x,y,z)=(y,z)
\]

is minimal and target-complete.

If instead the target is

\[
\Pi_1(x,y,z)=y,
\]

then the minimum memory rank drops to one. The full hidden path has dimension
two, but the target-relevant blind quotient has dimension one.

---

## 10. Claim boundary

```text
path-blind quotient representation              PROVED
endpoint decoder criterion                       PROVED
endpoint-only no-go in the declared linear sector PROVED
minimum scalar path-memory rank                   PROVED
stable lower-bound implication                    PROVED

nonlinear universal path linearization            NOT CLAIMED
application-specific path semantics                NOT CLAIMED
novelty relative to all sampling/control literature NOT CLAIMED HERE
```

The theorem is intended as a reusable Recognition-Kernel foundation. AI-agent,
blockchain, proof, and device histories are later specializations, not part of
the proof.