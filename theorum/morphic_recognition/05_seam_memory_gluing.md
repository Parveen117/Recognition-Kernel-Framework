# MR-05 — Typed Seam Memory Closure and Minimal Linear Gluing

## 1. Native question and evidence boundary

A local Recognition may preserve every current observation and still erase
Smriti required after a seam transition. This theorem constructs compatible
linear Recognition quotients on a finite typed graph and gives the exact
one-seam memory deficit before global backward closure.

Here **gluing** means that each declared edge induces a well-defined linear
map between Recognition quotients, and that these maps preserve observations
along every typed finite path. It does not assert equality of distinct paths,
commutativity of cycles, topological manifold gluing, or smooth extension
across singularities.

| Evidence axis | Status |
|---|---|
| Mathematical theorem | **PROVED UNDER HYPOTHESES**, by the ordinary proofs below |
| Executable certificate | Source-bound result in [MEMORY_CERTIFICATE.json](MEMORY_CERTIFICATE.json); the finite contract is in Section 9 and run evidence is in [MEMORY_VERIFICATION.md](MEMORY_VERIFICATION.md) |
| Formal proof assistant | **NOT FORMALIZED** |
| External review | **NONE CLAIMED** |
| Relation to prior theory | Typed finite-graph extension of MR-04 and one-seam specialization of MR-02; no novelty claim for linear minimization |

## 2. Finite typed seam datum

Let \(\mathbb F\in\{\mathbb Q,\mathbb R,\mathbb C\}\). Let
\(\mathcal G=(V,\mathcal E)\) be a finite directed multigraph. Node \(i\)
carries \(X_i=\mathbb F^{d_i}\) and a linear observation
\(E_i:X_i\to\mathbb F^{p_i}\). An edge \(e:i\to j\) carries a total linear
map \(F_e:X_i\to X_j\). Zero-dimensional carriers and observations are
allowed. The graph can have cycles, loops, parallel edges, and isolated nodes.

The current node label and chosen edge identity are retained. Path legality
depends only on the graph, not on a hidden state-dependent guard. In
particular, node labels are discrete side information and are not counted as
scalar linear Smriti channels.

For a chronological path \(p=e_1\cdots e_k:i\to j\), put

\[
F_p=F_{e_k}\cdots F_{e_1},\qquad F_{\epsilon_i}=I_{X_i}.
\]

Its response is \(E_jF_px\). Observations at intermediate nodes are included
by taking the corresponding path prefixes. Two states in the same node are
future-equivalent when every path starting at that node gives equal response.
No equivalence across different node types is asserted.

Define the nodewise future response space and future-blind Cut by

\[
W_i=\operatorname{span}\{\text{rows of }E_jF_p:
                            p:i\to j\},
\qquad
N_i=\bigcap_{p:i\to j}\ker(E_jF_p).
\]

Empty paths ensure \(\operatorname{row}E_i\subseteq W_i\). The completed
Recognition state at node \(i\) is the quotient \(X_i/N_i\).

## 3. Simultaneous backward closure

### Theorem MR05.1 — Finite closure across all typed futures

Starting with \(W_i^0=\operatorname{row}E_i\), update all nodes
**simultaneously** by

\[
\boxed{W_i^{n+1}=W_i^n+
       \sum_{e:i\to j}W_j^nF_e.}
\]

Then:

1. \(W_i^n\) is the span of all response rows for paths of length at most
   \(n\) starting at \(i\).
2. Equality \(W_i^{n+1}=W_i^n\) for every node implies full stationarity:
   \(W_i^n=W_i\) for every \(i\).
3. At most
   \[
   B=\sum_{i\in V}(d_i-\operatorname{rank}E_i)
   \]
   strict simultaneous rounds occur, followed by one equality check. Paths
   of length at most \(B\) span every \(W_i\).
4. \(N_i\) is the annihilator of \(W_i\), and
   \(F_eN_i\subseteq N_j\) for every edge \(e:i\to j\).

#### Proof

At stage zero only empty paths occur. A path of length at most \(n+1\)
starting at \(i\) is either empty or consists of an initial edge \(e:i\to j\)
followed by a path \(q\) of length at most \(n\) from \(j\). Its response
row is a row of \(E_kF_qF_e\), where \(k\) is the endpoint of \(q\).
Taking spans gives exactly the displayed recursion, proving assertion 1.

If every node is unchanged by an update, each pullback
\(W_j^nF_e\) is contained in \(W_i^n\). The next simultaneous update then
also changes nothing, and induction proves permanent stationarity.
Assertion 1 identifies the stationary spaces with \(W_i\). Before that
point, at least one node strictly increases its dimension. The sum of all
dimensions starts at \(\sum_i\operatorname{rank}E_i\) and is at most
\(\sum_i d_i\). This proves the round and path-length bounds.

The annihilator statement follows immediately from the definition of a span.
For \(x\in N_i\), any future path \(q:j\to k\) after edge \(e\) satisfies
\(E_kF_qF_ex=0\), because \(eq\) is a future path from \(i\).
Therefore \(F_ex\in N_j\). ∎

The bound counts global simultaneous rounds, not the number of individual
node updates in an arbitrary asynchronous implementation.

## 4. Compatible quotient transitions and minimality

### Theorem MR05.2 — Unique induced edges and all-path Recognition

For each node choose a full-row-rank basis matrix
\(R_i:X_i\to\mathbb F^{r_i}\) for \(W_i\), where \(r_i=\dim W_i\).
There are unique matrices \(C_i\) and \(\widehat F_e\) satisfying

\[
\boxed{E_i=C_iR_i,\qquad
R_jF_e=\widehat F_eR_i\quad(e:i\to j).}
\]

For every typed path \(p:i\to j\),

\[
R_jF_p=\widehat F_pR_i,\qquad
E_jF_p=C_j\widehat F_pR_i.
\]

Thus \(R_ix=R_iy\) exactly when \(x,y\) are future-equivalent at node
\(i\). Any linear observation \(Q_i\) faithful to all paths from \(i\)
has rank at least \(r_i\). The quotients attain these minima at every node
simultaneously and admit all the required induced edges.

#### Proof

The closure relation gives \(W_jF_e\subseteq W_i\). Hence each row of
\(R_jF_e\) has a unique expansion in the basis rows of \(R_i\); these
coefficients define \(\widehat F_e\). Since
\(\operatorname{row}E_i\subseteq W_i\), the same argument defines \(C_i\).
Each \(R_i\) is surjective, so the expansions and induced maps are unique.
Induction on path length proves both intertwining identities in the declared
chronological order.

The kernel of \(R_i\) is \(N_i\), since both are the annihilator of
\(W_i\). This proves the equivalence statement. If a linear map \(Q_i\)
is faithful to all paths, applying faithfulness to \(x=k,y=0\) gives
\(\ker Q_i\subseteq N_i\). Every row of \(W_i\) therefore vanishes on
\(\ker Q_i\), so it factors linearly through \(Q_i\), by the elementary
factorization argument in MR04.3. It follows that
\(W_i\subseteq\operatorname{row}Q_i\), and
\(\operatorname{rank}Q_i\ge r_i\). The matrices \(R_i\) attain the bounds
and already satisfy all edge identities. ∎

If the original \(E_i\) must remain explicitly stored, the minimum number
of additional scalar linear Smriti channels at node \(i\) is

\[
\boxed{r_i-\operatorname{rank}E_i.}
\]

Indeed, each added row increases rank by at most one, giving the lower bound;
extending a basis of \(\operatorname{row}E_i\) to one of \(W_i\) attains it.
As in MR04.3, redundant stored observations do not increase this number, and
the corresponding induced edges are unique on the stored image.

## 5. A local seam criterion and its exact deficit

The next result concerns **arbitrary proposed local Recognition maps**, before
the global closure above. Write them as \(L_i:X_i\to\mathbb F^{q_i}\) and
\(L_j:X_j\to\mathbb F^{q_j}\), so they are not confused with the completed
maps \(R_i,R_j\). Their rows may be redundant.

### Theorem MR05.3 — Local transition factorization

For one edge \(e:i\to j\), the following are equivalent:

1. There is a well-defined linear map
   \(T_e:\operatorname{ran}L_i\to\operatorname{ran}L_j\) with
   \(T_eL_i=L_jF_e\).
2. \(\ker L_i\subseteq\ker(L_jF_e)\).
3. \(\operatorname{row}(L_jF_e)\subseteq\operatorname{row}L_i\).

When it exists, \(T_e\) is unique on \(\operatorname{ran}L_i\). If one may
add only scalar linear memory at the source while keeping the target map
\(L_j\) fixed, the exact minimum number is

\[
\boxed{m_e=
\operatorname{rank}\begin{pmatrix}L_i\\L_jF_e\end{pmatrix}
-\operatorname{rank}L_i.}
\]

For proposed maps denoted by \(R_i,R_j\), this is equivalently the criterion
\(\ker R_i\subseteq\ker(R_jF_e)\) and the rank increment
\(\operatorname{rank}[R_i;R_jF_e]-\operatorname{rank}R_i\).

#### Proof

If \(T_e\) exists, \(L_ix=0\) implies \(L_jF_ex=T_e0=0\), proving
the kernel condition. Conversely, under that condition define
\(T_e(L_ix)=L_jF_ex\). Two representatives with the same \(L_i\)-image
differ by an element of \(\ker L_i\), which \(L_jF_e\) annihilates.
Thus the map is well defined, linear, valued in \(\operatorname{ran}L_j\),
and uniquely forced there. The row-space equivalence follows from the same
kernel/factorization argument as MR04.3.

Let \(U=\operatorname{row}L_i+\operatorname{row}(L_jF_e)\). A repaired map
\((L_i,G)\) can support the edge if and only if its row space contains
\(\operatorname{row}(L_jF_e)\), and therefore contains \(U\). With \(m\)
new rows, its rank is at most \(\operatorname{rank}L_i+m\), giving
\(m\ge\dim U-\operatorname{rank}L_i\). Extending a basis of
\(\operatorname{row}L_i\) to one of \(U\) and taking the added basis rows
as \(G\) attains equality. The dimension of \(U\) is the displayed stacked
rank. ∎

This is also the MR-02 formula
\(m_e=\operatorname{rank}((L_jF_e)|_{\ker L_i})\). The two ranks agree
because the difference of the stacked rank and \(\operatorname{rank}L_i\)
is

\[
\dim\ker L_i-
\dim\bigl(\ker L_i\cap\ker(L_jF_e)\bigr).
\]

The formula repairs one source with a **fixed target observation**. It is not
a one-pass algorithm for a whole network: repairing the target later can
increase what must be retained upstream.

## 6. Three-node counterexample to a single local pass

Let the only edges be \(0\xrightarrow{e}1\xrightarrow{f}2\), with
\(X_0=X_1=X_2=\mathbb Q^2\), all current observations
\(E_i=(1\;0)\), and

\[
F_e=I_2,\qquad
F_f=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Initially \(E_1F_e=E_0\), so the seam \(e\) needs no repair relative to
the original target observation. The seam \(f\) requires the second
coordinate at node 1, since \(E_2F_f=(0\;1)\).

After adding that coordinate at node 1, the edge \(e\) also needs the second
coordinate at node 0. The simultaneous closure dimensions are

\[
(\dim W_0^0,\dim W_1^0,\dim W_2^0)=(1,1,1),
\]
\[
(\dim W_0^1,\dim W_1^1,\dim W_2^1)=(1,2,1),
\qquad
(\dim W_0^2,\dim W_1^2,\dim W_2^2)=(2,2,1).
\]

The next update is equal. At node 0 the states \(0\) and \(e_2\) have
equal current observations and equal observations after the first edge, but
\(E_2F_fF_ee_2=1\). This supplies an exact length-two witness against
one-pass local repair. It does not contradict Theorem MR05.3: that theorem's
target map was subsequently enlarged.

## 7. Sharp refusal witnesses and type discipline

If a proposed \(Q_i\) is not faithful to all paths, then
\(\ker Q_i\not\subseteq N_i\). Choose
\(k\in\ker Q_i\setminus N_i\). Theorem MR05.1 spans \(W_i\) by paths of
length at most \(B\); at least one such response row does not annihilate
\(k\). Hence a distinguishing path of length at most \(B\) exists, and
\(0,k\) are a same-compression/different-future witness. This proves the
finite witness assertion without assuming the graph is acyclic.

A certificate must also preserve parallel edge identities. For example, two
edges from \(\mathbb Q\) to \(\mathbb Q\), one acting as \(+I\) and one as
\(-I\), give different recognized outputs for input 1 when the target
observation is identity. Identifying those edges loses a permitted future
distinction even though the source and destination types are the same.

With state-dependent guards the graph alone does not encode admissibility.
For example, let a one-dimensional source have zero present observation and
an edge with identity action and identity target observation that is allowed
only when the source coordinate is positive. States \(+1\) and \(-1\) have
the same current observation but different legal actions. This guarded datum
is outside the total-edge hypotheses and must be refused, not silently
certified by the unguarded algorithm. No guard-compilation theorem is asserted.

## 8. Relations and exclusions

[MR-04](04_future_complete_linear_recognition.md) is recovered by taking a
single node with one loop for every action. The one-seam memory formula is a
specialization of [MR-02](02_path_blindness_minimal_memory_repair.md).
[T61](../61_rewrite_rules_as_cut_module_operators_theorem.md) supplies a
possible exact finite rule-matrix carrier. Its distinction between conflict
and enabling effects remains necessary; preserving memory does not assert
that all actions commute.

For the established linear equivalence/minimization baseline, see Stefan
Kiefer's [Notes on Equivalence and Minimization of Weighted Automata](https://arxiv.org/abs/2009.01217).
The present capsule makes a typed Recognition/Smriti construction and its
one-seam versus network obligations explicit. It does not claim that linear
minimization itself is new.

This theorem does not identify a typed graph with a manifold, derive a smooth
or singular connection, infer thermodynamic laws, or solve nonlinear,
infinite-dimensional, guarded, stochastic, or adversarial observation
selection problems. Arbitrary states at every node are covered; restricting
to one reachable orbit is a different minimization problem. RH and
Yang–Mills endpoint claims are untouched.

## 9. RNKE certification obligations

```text
MR05-O1  simultaneous nodewise closure spans exactly the typed future path rows
MR05-O2  strict-round count is bounded by sum(d_i-rank(E_i)), plus equality check
MR05-O3  full-row-rank R_i admit unique exact output and edge intertwiners
MR05-O4  every nodewise future-faithful linear map has rank at least rank(R_i)
MR05-O5  local seam factorization is equivalent to the kernel and row conditions
MR05-O6  minimum one-seam repair equals the stacked-rank increment
MR05-N1  three-node example rejects one-pass local repair and exhibits length-two loss
MR05-N2  too few local repair channels leave a target-visible blind direction
MR05-N3  erasing a parallel edge identity merges distinct future responses
MR05-N4  state-dependent guarded edges are refused as outside the declared datum
```

Executable evidence must additionally cover cycles, dimension-changing
rectangular edges, isolated nodes, zero observations, redundant observation
rows, the finite distinguishing-path bound, and consistent typed path order.
It must identify finite fixtures and source hashes. A finite PASS checks
these contracts; the ordinary proofs establish the quantified linear
statements under their hypotheses.
