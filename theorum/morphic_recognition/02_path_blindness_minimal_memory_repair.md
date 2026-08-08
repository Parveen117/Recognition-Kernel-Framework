# MR-02 — Path Blindness and Minimal Memory Repair

## 1. Purpose

Two histories may have the same visible endpoint while differing in a target-relevant path property. An endpoint-only verifier is then blind to part of the morphic carrier.

This theorem gives:

1. the exact endpoint-faithfulness criterion;
2. the path-blind quotient;
3. the exact minimum number of scalar linear memory channels required to repair the blindness.

It is a finite-dimensional path-space specialization of the existing Cut-Variational Minimal Observer Theorem, stated directly in morphic language.

---

## 2. Linear path datum

Let

\[
\mathbb F\in\{\mathbb R,\mathbb C\},
\]

and let `P` be a finite-dimensional vector space of path descriptors or finite morphic histories.

Let

\[
E:\mathcal P\to Y
\]

be the visible endpoint observation and

\[
\Pi:\mathcal P\to Z
\]

be a declared linear path target.

Define

\[
K:=\ker E.
\]

A vector in `K` changes the path descriptor while leaving the endpoint observation unchanged.

### Definition 2.1 — Path-target faithfulness

The endpoint observation is target-faithful when

\[
\boxed{
\ker E\subseteq\ker\Pi.
}
\]

### Definition 2.2 — Path-blind quotient

Define

\[
\boxed{
\mathcal B_{\rm path}(E,\Pi)
:=
\ker E/(\ker E\cap\ker\Pi).
}
\]

This quotient retains exactly the endpoint-invisible directions that remain visible to the declared target.

---

## 3. Blind quotient representation

### Proposition 3.1

The map

\[
\widetilde\Pi:
\mathcal B_{\rm path}(E,\Pi)
\to
\Pi(\ker E),
\qquad
[k]\mapsto\Pi k,
\]

is a linear isomorphism. Hence

\[
\boxed{
\dim\mathcal B_{\rm path}(E,\Pi)
=
\operatorname{rank}(\Pi|_{\ker E}).
}
\]

### Proof

If `k-k'` lies in `ker E cap ker Pi`, then `Pi k = Pi k'`, so the map is well defined.

It is surjective by construction.

Its kernel consists of classes `[k]` with `k in ker E` and `Pi k = 0`, exactly the zero class of the quotient. Therefore it is injective. ∎

---

## 4. Endpoint decoder criterion

### Theorem 4.1

The following are equivalent:

1. `E` is path-target faithful;
2. there exists a unique linear map
   \[
   D:\operatorname{ran}E\to Z
   \]
   satisfying
   \[
   \boxed{\Pi=DE;}
   \]
3. \(\mathcal B_{\rm path}(E,\Pi)=\{0\}\).

### Proof

If `Pi = D E`, then `E k = 0` implies `Pi k = D0 = 0`, so `ker E subseteq ker Pi`.

Conversely assume `ker E subseteq ker Pi`. Define

\[
D(Ep):=\Pi p.
\]

If `Ep = Eq`, then `p-q in ker E subseteq ker Pi`, hence `Pi p = Pi q`; therefore `D` is well defined. Linearity follows from linearity of `E` and `Pi`, and uniqueness is forced on `ran E`.

The equivalence with the zero blind quotient is immediate from Definition 2.2. ∎

### Corollary 4.2 — Endpoint-only no-go

If

\[
\mathcal B_{\rm path}(E,\Pi)\neq\{0\},
\]

then no linear endpoint-only decoder can recover `Pi` on all of `P`.

Indeed, there exist `p,q` such that

\[
Ep=Eq
\]

but

\[
\Pi p\neq\Pi q.
\]

### Proof

Choose `k in ker E` with `Pi k != 0`. For any `p`, set `q=p+k`. Then `Eq=Ep` while `Pi q=Pi p+Pi k != Pi p`. ∎

This is the exact linear form of:

```text
same endpoint does not imply same recognized path.
```

---

## 5. Supplemental memory probes

Let

\[
G:\mathcal P\to\mathbb F^m
\]

be a bank of `m` scalar linear path-memory channels and define the repaired observation

\[
F=(E,G):\mathcal P\to Y\oplus\mathbb F^m.
\]

### Definition 5.1 — Target-complete memory

`G` is target-complete when

\[
\boxed{
\ker(E,G)\subseteq\ker\Pi.
}
\]

Equivalently, after endpoint and memory are observed together, no remaining invisible direction may affect the target.

---

## 6. Minimal Memory Repair Theorem

### Theorem 6.1

Let

\[
r
:=
\dim\mathcal B_{\rm path}(E,\Pi)
=
\operatorname{rank}(\Pi|_{\ker E}).
\]

Among all scalar linear memory banks

\[
G:\mathcal P\to\mathbb F^m,
\]

the minimum number of channels required for target completeness is

\[
\boxed{m_{\min}=r.}
\]

### Proof — lower bound

Let `K=ker E`. Target completeness gives

\[
\ker(G|_K)\subseteq K\cap\ker\Pi.
\]

Therefore

\[
\dim\ker(G|_K)
\le
\dim(K\cap\ker\Pi).
\]

By rank-nullity,

\[
\operatorname{rank}(G|_K)
=
\dim K-\dim\ker(G|_K)
\ge
\dim K-\dim(K\cap\ker\Pi)
=r.
\]

Since

\[
\operatorname{rank}(G|_K)\le m,
\]

we obtain

\[
\boxed{m\ge r.}
\]

### Proof — attainability

Let

\[
q:K\to K/(K\cap\ker\Pi)
\]

be the quotient map. The quotient has dimension `r`, so choose an isomorphism

\[
J:K/(K\cap\ker\Pi)\to\mathbb F^r
\]

and put

\[
G_K:=Jq:K\to\mathbb F^r.
\]

Then

\[
\ker G_K=K\cap\ker\Pi.
\]

Because `P` is finite-dimensional, extend `G_K` linearly from `K` to a map

\[
G:\mathcal P\to\mathbb F^r.
\]

Now

\[
\ker(E,G)
=
K\cap\ker G
=
K\cap\ker\Pi
\subseteq\ker\Pi.
\]

Thus `r` channels suffice. Combined with the lower bound,

\[
\boxed{m_{\min}=r.}
\]

∎

---

## 7. Relation to the existing minimal-observer theorem

Theorem 31 proves that the minimum faithful observer rank equals the dimension of the target-relevant cut-memory range.

MR-02 identifies the corresponding path-memory object explicitly:

\[
\mathcal B_{\rm path}
\cong
\Pi(\ker E).
\]

Thus the endpoint-blind path quotient is the morphic source from which the minimum repair rank is computed.

MR-02 should therefore be read as a specialization/bridge theorem, not as a replacement for Theorem 31.

---

## 8. Exact calibration model

Take

\[
\mathcal P=\mathbb Q^3,
\]

with

\[
E(x_1,x_2,x_3)=x_1
\]

and

\[
\Pi(x_1,x_2,x_3)=(x_2,x_3).
\]

Then

\[
\ker E=\operatorname{span}\{e_2,e_3\},
\]

and

\[
\Pi|_{\ker E}
\]

has rank two. Therefore

\[
\boxed{m_{\min}=2.}
\]

The one-channel memory

\[
G_1(x)=x_2
\]

misses the target-visible blind direction `e_3`, while

\[
G_2(x)=(x_2,x_3)
\]

is target-complete.

This is a calibration witness, not the universal proof.

---

## 9. RNKE proof contract

```text
MR02-O1  path-blind quotient is isomorphic to Pi(ker E)
MR02-O2  endpoint decoder exists iff ker E subseteq ker Pi
MR02-O3  target-complete memory implies rank(G|kerE) >= blind dimension
MR02-O4  quotient coordinates construct a memory bank attaining that dimension
MR02-N1  same endpoint / different target witness exists when blind quotient is nonzero
MR02-N2  one-channel calibration fails for a rank-two blind quotient
MR02-N3  two-channel calibration repairs the exact rank-two quotient
```

## 10. Status

```text
GENERAL FINITE-DIMENSIONAL LINEAR PROOF    PROVED
RELATION TO THEOREM 31                     SPECIALIZATION / BRIDGE
DEPENDENCE ON CLOCK                        NONE
RNKE PROOF-CONTRACT CALIBRATION             SEE proof_lab/morphic_recognition
INFINITE-DIMENSIONAL MINIMUM-RANK VERSION   REQUIRES SEPARATE TOPOLOGICAL HYPOTHESES
FORMAL PROOF-ASSISTANT CERTIFICATE          NOT CLAIMED
```
