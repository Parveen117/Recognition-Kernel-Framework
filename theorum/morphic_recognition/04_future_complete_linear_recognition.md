# MR-04 — Future-Complete Linear Recognition and Minimum Smriti

## 1. Native question and evidence boundary

Recognition of a present observation does not by itself license Lopa of every
presently invisible direction. A lawful later transformation can make such a
direction visible. This theorem constructs precisely the linear Smriti needed
to preserve every declared finite future response.

The carrier, allowed actions, and observation are inputs to the theorem. It
does not infer them from data or certify the truth of an arbitrary observation.
All comparisons hold on the **whole declared carrier**, not merely on one
initial state or one observed trajectory.

| Evidence axis | Status |
|---|---|
| Mathematical theorem | **PROVED UNDER HYPOTHESES**, by the ordinary proofs below |
| Executable certificate | Source-bound result in [MEMORY_CERTIFICATE.json](MEMORY_CERTIFICATE.json); the finite contract is in Section 9 and run evidence is in [MEMORY_VERIFICATION.md](MEMORY_VERIFICATION.md) |
| Formal proof assistant | **NOT FORMALIZED** |
| External review | **NONE CLAIMED** |
| Relation to prior theory | Constructive linear future-response specialization of MR-02; no novelty claim for linear realization/minimization |

## 2. Declared linear Recognition datum

Fix a field \(\mathbb F\in\{\mathbb Q,\mathbb R,\mathbb C\}\), a carrier
\(X=\mathbb F^d\), a finite action alphabet \(\mathcal A\), total linear
actions \(A_a:X\to X\) for \(a\in\mathcal A\), and a linear observation
\(E:X\to\mathbb F^p\). Zero dimensions and an empty action alphabet are
allowed. Observation rows need not be independent.

Every word in \(\mathcal A^*\) is admissible from every state. The action label
remains available to the compressed system. There are no state-dependent
guards, partial maps, nonlinear updates, or stochastic transitions in this
datum.

For a chronological word \(w=a_1\cdots a_k\), the first action is \(a_1\),
and

\[
A_w=A_{a_k}\cdots A_{a_1},\qquad A_\epsilon=I_X.
\]

Its recognition target is the future response \(EA_wx\). Define

\[
x\sim y
\quad\Longleftrightarrow\quad
EA_wx=EA_wy\quad\text{for every }w\in\mathcal A^*.
\]

The future-blind Cut and the future response row space are

\[
N=\bigcap_{w\in\mathcal A^*}\ker(EA_w),
\qquad
W=\operatorname{span}\{\text{rows of }EA_w:w\in\mathcal A^*\}\subseteq X^*.
\]

Thus \(x\sim y\) exactly when \(x-y\in N\). The native completed state is
the Recognition quotient \(X/N\). A basis matrix for \(W\) gives coordinates
for this quotient; it does not replace the definition of the quotient.

Here and below, \(\operatorname{row}M\) denotes the linear row space, and
\(W A_a=\{\ell A_a:\ell\in W\}\).

## 3. Finite future closure

### Theorem MR04.1 — Closure and finite witness horizon

Set

\[
W^0=\operatorname{row}E,\qquad
W^{n+1}=W^n+\sum_{a\in\mathcal A}W^nA_a.
\]

Then:

1. \(W^n\) is exactly the span of rows of \(EA_w\) for words of length at
   most \(n\).
2. If \(W^{n+1}=W^n\), then \(W^n=W\), and every subsequent stage is equal.
3. There are at most \(d-\operatorname{rank}E\) strict rounds of growth.
   A sequential implementation stops after those rounds and one equality
   check. In particular, words of length at most
   \(d-\operatorname{rank}E\) span all future responses.
4. \(N\) is the annihilator of \(W\). It is invariant under every \(A_a\),
   and it is the largest common invariant subspace contained in \(\ker E\).

#### Proof

The first assertion holds at \(n=0\), since the only length-zero word is
\(\epsilon\). If a row has the form \(\ell EA_w\), its product with
\(A_a\) is \(\ell EA_wA_a=\ell EA_{aw}\): the letter \(a\) is applied
first. Every nonempty word of length at most \(n+1\) has that form with a
suffix of length at most \(n\). Linear spans therefore give assertion 1 by
induction.

If \(W^{n+1}=W^n\), then \(W^nA_a\subseteq W^n\) for every \(a\).
The defining recursion consequently gives equality at every later stage.
Assertion 1 then shows that all words belong to the stationary space, proving
assertion 2. Before stationarity each strict inclusion increases dimension by
at least one. The dimension starts at \(\operatorname{rank}E\) and is at most
\(d\). This proves assertion 3, including the separate final equality check.

By definition, a vector annihilated by every row of every \(EA_w\) is
annihilated by their span, and conversely. This proves the assertion about
\(N\). If \(x\in N\), then for every word \(w\),
\(EA_wA_ax=EA_{aw}x=0\); hence \(A_ax\in N\). The empty word gives
\(N\subseteq\ker E\). Finally, if \(L\subseteq\ker E\) is invariant under
every action, then \(A_wL\subseteq L\subseteq\ker E\) for every word, so
\(L\subseteq N\). This proves assertion 4. ∎

## 4. Exact induced transformations

### Theorem MR04.2 — Recognition intertwining and uniqueness

Let \(r=\dim W\), and choose \(R\in\mathbb F^{r\times d}\) whose rows form
a basis of \(W\). Then \(R\) is surjective onto \(\mathbb F^r\),
\(\ker R=N\), and there are unique matrices

\[
\widehat A_a\in\mathbb F^{r\times r},\qquad
C\in\mathbb F^{p\times r}
\]

such that

\[
\boxed{RA_a=\widehat A_aR,\qquad E=CR.}
\]

Consequently, with \(\widehat A_w\) in the same chronological convention,

\[
RA_w=\widehat A_wR,
\qquad
EA_w=C\widehat A_wR
\quad\text{for every finite word }w.
\]

Thus \(Rx=Ry\) if and only if \(x\sim y\). Applying an action before
Recognition or applying its induced action after Recognition gives the same
result.

#### Proof

Full row rank makes \(R\) surjective. Its kernel is the annihilator of its
row space, which is \(N\) by Theorem MR04.1. The rows of \(RA_a\) belong
to \(W\) by invariance, so each has a unique expansion in the basis rows of
\(R\). Their coefficients form \(\widehat A_a\). The same argument applies
to the rows of \(E\) and defines \(C\). Alternatively, uniqueness follows
from surjectivity: \(UR=VR\) implies \(U=V\).

The word identities follow by induction using the declared product order.
If \(Rx=Ry\), the decoder identity makes every future output equal.
Conversely, equality of every future output means \(x-y\in N=\ker R\).
This proves all assertions, also when \(r=0\). ∎

Any other basis matrix \(R'=SR\), with \(S\) invertible, produces
\(\widehat A'_a=S\widehat A_aS^{-1}\) and \(C'=CS^{-1}\), directly by
substitution into the unique intertwining identities. Hence the basis changes
coordinates, not the recognized state.

## 5. Minimality and retained original observations

### Theorem MR04.3 — Minimum linear realization and Smriti size

A linear map \(Q:X\to\mathbb F^q\) is called future-faithful if

\[
Qx=Qy\Longrightarrow EA_wx=EA_wy
\quad\text{for all }x,y\in X\text{ and all words }w.
\]

Then every such \(Q\) satisfies

\[
\ker Q\subseteq N,
\qquad
W\subseteq\operatorname{row}Q,
\qquad
\operatorname{rank}Q\ge r.
\]

The map \(R\) attains this lower bound and supports the exact induced
transformations of Theorem MR04.2. Thus the minimum linear state dimension
for future faithfulness is \(r\).

If the existing observation \(E\) must remain as an explicit part of the
state and only scalar linear Smriti channels \(G:X\to\mathbb F^m\) may be
added, the exact minimum is

\[
\boxed{m_{\min}=r-\operatorname{rank}E.}
\]

This is the number of **additional channels**. If \(E\) has redundant rows,
the stored vector \((Ex,Gx)\) has \(p+m\) entries but only \(r\) independent
coordinates at the minimum.

#### Proof

Apply future faithfulness to \(x=k\), \(y=0\), with \(k\in\ker Q\).
It gives \(k\in N\), proving the kernel inclusion. A functional \(\ell\)
vanishes on \(\ker Q\) if and only if it belongs to \(\operatorname{row}Q\):
indeed define \(D(Qx)=\ell x\) on \(\operatorname{ran}Q\); vanishing on the
kernel makes \(D\) well defined and linear, and extending it to
\(\mathbb F^q\) expresses \(\ell\) as a row combination of \(Q\).
Applying this fact to every row in \(W\) proves row inclusion and the rank
bound. Theorem MR04.2 establishes attainability by \(R\).

For \(Q=(E,G)\),
\[
r\le\operatorname{rank}(E,G)
\le\operatorname{rank}E+m,
\]
so \(m\ge r-\operatorname{rank}E\). To attain equality, extend a basis of
\(\operatorname{row}E\) to a basis of \(W\), and let the new basis rows be
the rows of \(G\). Then \(\operatorname{row}(E,G)=W\), so its kernel is
\(N\), and it is future-faithful. ∎

The minimally augmented observation also supports induced actions because
its kernel \(N\) is invariant. These actions are unique **on its image**.
When the stored coordinates are redundant, extensions to the whole ambient
\(\mathbb F^{p+m}\) need not be unique.

Taking the finite target \(\Pi=R\) in
[MR-02](02_path_blindness_minimal_memory_repair.md) gives the same memory
count. Explicitly, \(\ker R=N\subseteq\ker E\), so

\[
\operatorname{rank}(R|_{\ker E})
=(d-\operatorname{rank}E)-(d-r)
=r-\operatorname{rank}E.
\]

Although MR-02 states its abstract carrier over \(\mathbb R\) or
\(\mathbb C\), its finite-dimensional algebraic proof also applies over
\(\mathbb Q\); the independent proof above covers all three fields directly.

## 6. Constructive refusal of insufficient Lopa

### Corollary MR04.4 — A finite distinguishing continuation

If \(Q\) is not future-faithful, there are \(k\in\ker Q\), an observation
coordinate, and a word \(w\) of length at most
\(d-\operatorname{rank}E\) such that \(EA_wk\ne0\). Thus the states
\(0,k\) have the same proposed compressed state and different future outputs.

#### Proof

Failure of faithfulness means \(\ker Q\not\subseteq N\). Choose
\(k\in\ker Q\setminus N\). Theorem MR04.1 says rows for words within the
stated horizon span \(W\). Since some member of \(W\) does not annihilate
\(k\), at least one of those generating rows does not annihilate it.
That row supplies the word and observation coordinate. ∎

For rational input matrices, Gaussian elimination and exact kernel
calculations construct all these objects over \(\mathbb Q\). Keeping the
word attached to each candidate row before basis reduction makes a witness
word recoverable. Numerical rank thresholds over inexact input require a
separate error analysis and do not provide this exact certificate.

## 7. Calibration and negative controls

### Present equality can lose an enabling effect

Let
\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
B=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad E=(1\;0).
\]
The states \(x=(1,0)^T\) and \(y=Bx=(1,1)^T\) have \(Ex=Ey=1\),
but \(EAx=1\) and \(EAy=2\). Consequently present-only Lopa is refused.
The rows \(E=(1,0)\) and \(EA=(1,1)\) span \(\mathbb F^2\), so the
minimum completion retains two independent coordinates, one more than \(E\).
The Smriti channel \(G=(0\;1)\) attains the bound.

Order must remain explicit: \(EABx=2\) while \(EBAx=1\). Under the
chronological convention these are the responses to words \(BA\) and \(AB\),
respectively. A certificate that reverses this convention is invalid.

### One-step checking can miss the next distinction

Let
\[
A=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},\quad E=(1\;0\;0).
\]
For \(k=e_3\), \(Ek=EAk=0\), but \(EA^2k=1\). The row-space dimensions
are \(1,2,3\), so both strict rounds are necessary. A stopping rule that
checks only immediate outputs is rejected.

### Degenerate and redundant observations

If \(E=0\), every future output is zero, \(W=N^\perp=\{0\}\), and the
minimum recognized state has dimension zero. If \(\mathcal A\) is empty,
\(W=\operatorname{row}E\), so no extra Smriti is needed. Repeating an
observation row changes its storage count but neither its rank nor the
minimum number of additional channels. These cases must be accepted rather
than forcing a positive memory dimension.

## 8. Relation and scope

[T61](../61_rewrite_rules_as_cut_module_operators_theorem.md) realizes a
declared finite rewrite carrier by total rule matrices, with identity action
when a rule is inapplicable. Such a fixed linear realization can be supplied
as the datum here. The original rewrite applicability semantics must be
preserved by that realization; arbitrary state-dependent guards are not
silently added to MR-04. The T61 conflict/enabling distinction explains why
an invisible marker can still carry a future enabling effect.

Classical linear equivalence and minimization supply a baseline, documented
in Stefan Kiefer's primary exposition,
[Notes on Equivalence and Minimization of Weighted Automata](https://arxiv.org/abs/2009.01217).
The present theorem is a Recognition/Smriti specialization with an explicit
retained-observation memory count. No novelty claim for the underlying
linear-algebraic minimization principle is made.

The following are outside this theorem: nonlinear or infinite-dimensional
minimality; arbitrary real-number encodings; a fixed-initial-state reachable
quotient; state-dependent legality; singular/smooth gluing; physical TVSP
identification; RH and Yang–Mills endpoint gates. None is promoted by a finite
PASS.

## 9. RNKE certification obligations

```text
MR04-O1  row closure equals all future rows and stabilizes within the rank bound
MR04-O2  R is full-row-rank and satisfies exact action/output intertwining
MR04-O3  future-faithful linear observations have rank at least rank(R)
MR04-O4  retained E requires and admits exactly rank(R)-rank(E) new channels
MR04-O5  failed compression admits a distinguishing word within the finite horizon
MR04-O6  word composition and induced dynamics use the same chronological order
MR04-N1  current-output equality is rejected as sufficient in the shear example
MR04-N2  one-step-only closure is rejected by the length-two shift witness
MR04-N3  erasing the necessary supplemental coordinate loses a future response
MR04-N4  swapping noncommuting action order changes the declared shear response
```

Executable evidence must additionally cover zero observation, empty action
alphabet, redundant observation rows, and exact rational basis changes. It
must identify its finite fixtures and source hashes. These checks exercise
the statements; the ordinary proofs above establish the quantified theorem.
