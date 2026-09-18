# MR-06 — Guarded Lopa and Minimal Future-Recognition Quotients

## Evidence and scope

| Evidence layer | Status |
|---|---|
| Mathematical theorem | PROVED UNDER THE FINITE DETERMINISTIC HYPOTHESES BELOW |
| Executable contract | Source-bound result in [MEMORY_CERTIFICATE.json](MEMORY_CERTIFICATE.json); actual Python 3.12 evidence in [MEMORY_VERIFICATION.md](MEMORY_VERIFICATION.md) |
| Formal proof assistant | NOT FORMALIZED |
| External review / novelty | NOT CLAIMED |

This is a finite Recognition/Smriti theorem: a visible marker may disappear
under Lopa only while its future-relevant effect survives. It develops the
retained-effect distinction in [T58](../58_paninian_seam_calculus_theorem.md)
and the conflict/enabling distinction in
[T61](../61_rewrite_rules_as_cut_module_operators_theorem.md).

The construction has an explicit interface to finite deterministic behavioral
equivalence and automaton minimization. Its presence here does not certify a
new discovery in automata theory. The contribution of this capsule is the
precise guarded Lopa contract, minimum finite state representation, constructive
failure witness, and the separation of information sufficiency from update
sufficiency. It does not certify the whole Sanskrit grammar or a smooth theory.

## 1. Declared carrier, target, and guards

Let `X` be a finite nonempty state set, `A` a finite action alphabet (possibly
empty), and `o: X -> Y` a visible Recognition output. Equality in `Y` is a
specified equivalence relation. For every `a in A`, let

\[
f_a:D_a\longrightarrow X,\qquad D_a\subseteq X,
\]

be a deterministic partial rule. Its guard is `x in D_a`; define
`G(x) = {a : x in D_a}`. A word `w = a_1 ... a_k` acts left to right,
`F_w(x) = f_{a_k}(... f_{a_1}(x))`, whenever every step is enabled. The empty
word is always admissible and acts as identity. Write `L(x)` for all admissible
words from `x`.

The target contains both **admissibility** and **the final recognized output**:

\[
x\sim y
\iff
L(x)=L(y)
\quad\text{and}\quad
o(F_w(x))=o(F_w(y))\quad(w\in L(x)).
\]

Since every prefix is itself a word, intermediate outputs are also preserved.
This relation is an equivalence relation directly from equality of the language
and all its output values. The carrier is all declared states. For a task with
specified initial states, first restrict to their successor-closed reachable
carrier; no conclusion about a smaller reachable carrier is silently assumed.

## 2. Coarsest stable partition theorem

Call a partition `P` **guarded stable** when `x,y` in one block implies:

1. `o(x) = o(y)`;
2. `G(x) = G(y)`;
3. for each `a in G(x)`, `f_a(x), f_a(y)` lie in one block of `P`.

**Theorem 2.1.** The future-equivalence classes `X/~` form the unique coarsest
guarded stable partition.

**Proof.** If `x ~ y`, the empty word gives output equality and the length-one
words give guard equality. For a common enabled action `a`, a continuation `v`
is admissible from `f_a(x)` exactly when `av` is admissible from `x`. The same
holds for `y`, and final output equality for `av` gives
`f_a(x) ~ f_a(y)`. Thus `X/~` is guarded stable.

Conversely, suppose `x,y` share a block of any guarded stable partition.
Induct on word length. The empty word has the same output. For a word `av`,
the first action is enabled on both sides or neither. In the enabled case its
successors share a block, so the induction hypothesis gives the same
admissibility and output for `v`. Consequently `x ~ y`. Every guarded stable
partition therefore refines `X/~`, proving both coarseness and uniqueness. ∎

**Theorem 2.2 (terminating construction).** Begin with the partition `P_0`
by `(o(x), G(x))`. At each round retain the old block label and split states
according to the blocks of all enabled successors. Stop when no block splits.
The process terminates after at most `|X| - |P_0|` strict refinements and its
result is exactly `X/~`.

**Proof.** Old labels are retained, so blocks never merge. Every strict round
increases the number of blocks, which cannot exceed `|X|`. The fixed partition
is guarded stable, hence refines `X/~` by Theorem 2.1. Conversely, equivalent
states share `P_0` labels. If equivalent states share the round-`k` labels,
their equivalent enabled successors share those labels too, so they remain
together at round `k+1`. Thus the process never separates equivalent states.
Both refinements hold at termination, giving equality. ∎

No fixed word length is used as a substitute for all-future faithfulness.

## 3. Unique minimum faithful deterministic quotient

A **faithful quotient representation** consists of a surjection `r: X -> Z`,
an output `o_hat: Z -> Y`, and deterministic partial actions `f_hat_a`, with

\[
o=\widehat o\circ r,
\qquad
x\in D_a\iff r(x)\in\widehat D_a,
\qquad
r(f_a(x))=\widehat f_a(r(x))\quad(x\in D_a).
\]

Both directions of guard preservation are required. Removing one direction
would allow spurious actions or lost lawful actions.

**Theorem 3.1.** Such a representation has `|Z| >= |X/~|`. Equality is attained
by `q(x)=[x]`. Every representation attaining equality is isomorphic to this
quotient by a bijection preserving outputs, guards, and actions.

**Proof.** States in a fiber of `r` have equal output and guards, and their
enabled successors again have equal retained labels. Thus the fiber partition
is guarded stable and refines `X/~` by Theorem 2.1. It has at least as many
blocks. On `X/~`, define output and guards by any representative and define
`f_hat_a([x])=[f_a(x)]`. Theorem 2.1 makes each definition independent of the
representative, so `q` is a faithful quotient attaining the bound. If another
fiber partition has the same number of blocks, its refinement of `X/~` must
be equality. The map `r(x) -> [x]` is therefore a bijection. The displayed
identities make it preserve all the structure. ∎

This minimizes **the number of retained states** on this finite carrier. It
does not minimize a number of real-valued channels, bits under arbitrary
encodings, or execution time. In particular it is distinct from the linear
channel-rank minimum in [MR-02](02_path_blindness_minimal_memory_repair.md).

## 4. Safe Lopa and the extra-label obstruction

**Theorem 4.1 (replacement).** A Lopa operation `ell: X -> X`, used as an
internal replacement of a state, preserves every declared future experiment
if and only if `ell(x) ~ x` for every state where it is applied.

**Proof.** The preservation requirement is exactly equality of admissible
continuations and all their recognized outputs, which is the definition of
`~`. Subsequent lawful actions preserve `~` by Theorem 2.1, so the replacement
can be interleaved with further actions. ∎

**Theorem 4.2 (retained record).** For any map `R: X -> M`, the retained record
determines all future admissibility and recognized outputs if and only if

\[
R(x)=R(y)\implies x\sim y.
\]

Equivalently, there is a unique decoder `d: R(X) -> X/~` with `q=dR`.

**Proof.** If two states with the same record have different future behavior,
that record cannot determine both behaviors. Conversely, under the displayed
condition define `d(R(x))=[x]`; equal records give equal classes, making `d`
well defined. It is unique on `R(X)`, and that class determines all the
specified future experiments by definition. ∎

**Important boundary.** This information criterion alone does not ensure that
the original labels in `M` can themselves be updated deterministically. To
have maps `R(f_a(x)) = f_hat_a(R(x))`, the fibers of `R` must also be successor
stable. Output and guard agreement already follow from Theorem 4.2, so this
additional condition is necessary and sufficient by direct definition on each
fiber. A record may decode the minimum quotient yet contain redundant labels
whose updates require distinctions that the record discarded.

**Explicit obstruction.** Let all four states `x,y,u,v` have output zero; let
the only action be enabled everywhere and send `x -> u`, `y -> v`, `u -> u`,
`v -> v`. All states are future equivalent. Retain `R(x)=R(y)=start`,
`R(u)=left`, `R(v)=right`. The record is information-sufficient, but a
deterministic update of `start` would have to equal both `left` and `right`.
Decoding to the single canonical future class removes this inconsistency.

## 5. Constructive refusal witnesses

**Theorem 5.1.** A breadth-first traversal of paired successor states decides
whether `x ~ y`. If not, it returns a shortest distinguishing word. A word
distinguishes either by final output or by being admissible on exactly one
side.

**Proof.** Start at `(x,y)` with the empty word. At each pair compare current
outputs. For every action, enqueue the successor pair if both steps exist;
if exactly one exists enqueue an explicit disabled-side terminal; if neither
exists, no distinction occurs on that action. Process pairs in breadth-first
order and visit each pair once. There are at most `|X|^2` nonterminal pairs,
so the search terminates. A repeated pair has the same possible future
distinctions as its first occurrence, which was reached by a no-longer word;
discarding repetitions therefore loses neither completeness nor a shortest
witness. A returned output/guard mismatch is by construction a valid witness.
If none is found, the reached pairs have equal outputs and guards and are
closed under common enabled successors; the induction of Theorem 2.1 gives
future equivalence. FIFO traversal ensures a shortest witness. ∎

The disabled-side terminal is queued rather than immediately returned, since
another current-depth pair may have a shorter output witness. This detail is
covered by a dedicated regression test.

## 6. Guard semantics and the T61 interface

T61 explicitly uses **identity if inapplicable** in its free-module adapter.
MR-06 instead treats an inapplicable rule as **disabled**. These are distinct
experiments and must not be silently identified.

For example, take two states with the same constant output. Let `a` be an
identity action at the first state and disabled at the second. They are
distinguished by the word `a`. Replacing the disabled rule by an unmarked
identity makes the two states indistinguishable. To totalize without changing
the target, add an explicit, observed disabled-action signal (for example a
failure sink with a fresh observation). An unobserved failure or identity does
not preserve the contract.

Consequently, marker deletion is safe only when any Smriti tail needed to
preserve later applicability as well as later recognized output survives.

## 7. Executable obligations and boundary

Implementation: [guarded.py](../../proof_lab/morphic_recognition/guarded.py).
Independent tests: [test_guarded_lopa.py](../../proof_lab/test_guarded_lopa.py).

| Contract ID | Exact executable obligation |
|---|---|
| MR06-O1 | Partition refinement agrees with independent pair-graph search on all 5,912 ordered state pairs in 844 systems |
| MR06-O2 | Every returned word independently replays to different admissibility or final outputs |
| MR06-O3 | All 844 constructed quotients preserve outputs, guards, and every declared source transition |
| MR06-N1 | Constant-output guard-only erasure is rejected with witness `a` |
| MR06-N2 | Silent identity totalization changes equivalence in the declared counterexample |
| MR06-N3 | Marker deletion retaining its tail is safe; erasing the tail has witness `a` |
| MR06-N4 | A finer information-sufficient record can fail direct deterministic update |

The systematic collection exhausts all labeled binary-output partial systems
with (one state, two actions), (two states, two actions), or (three states, one
action): `8 + 324 + 512 = 844` systems. These counts describe the finite
calibration, not the domain of the general theorem. Additional tests cover
delayed distinctions, empty action alphabets, cyclic equivalent states,
shortest-witness ordering, immutable inputs, and malformed carrier rejection.

```sh
python3.12 -m unittest proof_lab.test_guarded_lopa -v
```

`verify_guarded_contract()` returns the theorem ID, each obligation's exact
evidence counts and pass/fail status, and an aggregate fail-closed status.
Its `RNKE_CONTRACT_VERIFIED` result refers to this executable contract. The
proofs above establish the mathematical statements under their hypotheses;
tests do not replace those proofs. Infinite carriers, nondeterministic or
probabilistic rules, continuous/smooth extension, Sanskrit completeness,
physical identification, RH, and Yang–Mills remain outside this theorem.
