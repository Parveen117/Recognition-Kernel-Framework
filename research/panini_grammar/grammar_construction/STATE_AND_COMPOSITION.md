# PG14 — The state that a grammatical rule acts on

Author: Monty. 2 November 2026.

## S1. Primitive order and the declared construction

The coefficient scalars come from the already constructed native cut field
\(C_\Sigma\), including its derived \(\iota\) and scalar dagger. The full
operator carrier, cuts, pairing and specialization used here are constructed
in [N1–N6](NATIVE_OPERATOR_LIFT.md). No Hilbert space, positive metric,
physical clock or scalar interpretation of lambda is presumed.

The present chapter specifies the grammar labels and lawful arrows in that
carrier. A finite semantic frame is an input object; its interpretation is
not inferred from arbitrary prose. A mathematical grammar construction must
retain that distinction even after every morphology table has been filled.

Use the types

\[
 F \longrightarrow K \longrightarrow V \longrightarrow P
   \longrightarrow A \longrightarrow W.
\]

Here \(F\) is an interpreted lexical/event frame, \(K\) a kāraka assignment,
\(V\) a choice of what the lakāra expresses, \(P\) a pada and agreement
assignment, \(A\) an owned affix/constituent state, and \(W\) a word state
with an optional surface observation. These are relations, not necessarily
functions. A later formation may have a different dependency graph; the
display is the particular active/causative/passive construction below.

## S2. State and event types

A state is

\[
 s=(L,F,K,V,P,M,O,H,Q),
\]

where:

- \(L\): exact lexical IDs, teaching forms, selected senses and register;
- \(F\): event(s), participants, intentional result, participant identity,
  semantic-role evidence, prefixes/upapadas, and stated exclusions;
- \(K,V,P\): role assignments, expressed role, pada and agreement decisions;
- \(M\): constituent tree with stable owners for root, copied abhyāsa,
  augment, affix, ending and replacement sounds;
- \(O\): original forms and immutable source/interpretation records;
- \(H\): the ordered applied-event and branch history;
- \(Q\): unresolved predicates and local obligations.

A sound occurrence is an identity, owner, current value and ancestry, not
only a letter. An event records rule ID, source occurrence, inherited scope,
guard evidence, branch label, affected occurrences, old/new values,
visibility interpretation and the earlier events it consumes. It-lopa adds
an event and changes the observation of a marker; it does not remove its
owner or turn it into whole-affix lopa. Substitution and augment insertion
are different constructors.

The observation \(\operatorname{surf}(s)\) reads surviving sounds in order.
It is many-to-one. The two states whose visible ending is *te* can differ in
active A versus karma-passive, root identity, causal formation and agreement
role. Neither meaning nor rule applicability factors through surface text
in general.

## S3. Applicability, prohibition and optionality

A reviewed rule occurrence is

\[
 r=(\text{source},D_r,g_r,\operatorname{view}_r,
       \{(b,a_{r,b})\},\operatorname{priority}_r).
\]

\(D_r\) is its typed domain. Its guard has values **true**, **false**, or
**unknown**, with evidence. A positive application requires true; a known
prohibition supplies false; unknown carries the missing predicate into
\(Q\). A rule-relative view is a typed query on original/current/history
data. It never mutates the actual record to make an earlier event disappear.

Each licensed branch \(b\) has an action \(a_{r,b}\) preserving the state
invariants. If two readings are permitted, both are edges. If a source
conflict is unadjudicated, neither an arbitrary branch nor a largest-sūtra
number becomes a grammatical decision. The rule relations carry specific
exception/prohibition evidence; 1.4.2 is not a universal sorting algorithm.

There are three distinct outcome types:

| Outcome | Meaning |
|---|---|
| `Derived(s, history)` | A licensed branch has been constructed |
| `Excluded(reason, source)` | A stated request contradicts a known condition in this domain |
| `Open(obligations)` | Meaning, lexical scope, priority or a needed construction is missing |

Inapplicability is not a silent identity derivation. An explicit stop/accept
event identifies a finished word. This differs deliberately from the total
identity-on-inapplicability convention in the finite T61 presentation.

## S4. Composition theorem

Let \(R_i\subseteq X_{i-1}\times B_i\times X_i\) be a local relation,
where \(B_i\) contains rule/source/branch witnesses. Suppose that every edge
has a well-typed witness for its declared source interpretation and preserves
stable identities, ownership, immutable original records and append-only
history. Define the composite by relational composition, retaining the
ordered witness tuple \((b_1,\ldots,b_n)\).

**Proposition S4a.** Every edge of the composite has a derivation consisting
of precisely those locally licensed edges, and preserves those invariants.

**Proof.** For one edge this is the hypothesis. A witness for a composite of
\(n+1\) edges consists of an intermediate state, a witness for its first
\(n\) edges and a witness for the last edge. Apply induction, concatenate
histories, and use the last action's invariant preservation. Matching
intermediate types prevent a role-selection output from being consumed as
a sound string, or an unlicensed pada from being treated as an ending. □

This is a compositional theorem **relative to the adopted local readings**.
It does not establish those readings merely because a relation was written.
The following chapters supply their source arguments on the stated domains.

**Proposition S4b.** Suppose each \(R_i\) contains every branch licensed by
its adopted source interpretation on the admitted states, and every such
derivation in the domain factors through this same sequence of types. The
composite contains every such derivation.

**Proof.** Take an admitted derivation and its factorization. Local
completeness gives its first edge, then its second edge on the actual first
output, and so on. Composition therefore contains the complete witness.
Conversely S4a supplies local soundness. □

The factorization premise matters: an omitted karmakartṛ construction,
nested causative, accented rule or lakāra cannot be recovered by a complete
table inside a different formation. No universal termination or confluence
statement about all of Pāṇini follows from S4.

## S5. Knowledge refinement and residual obligations

A partial frame denotes its possible completed frames under the declared
domain conditions. Refining it adds consistent evidence and shrinks that
set. Define a branch as **stable** only when its guard and priority proof
hold for every completion currently admitted. If a feature is needed to
distinguish two outcomes, return both as *conditional alternatives* with an
open obligation, not as two already licensed optional Sanskrit forms.

**Proposition S5.** Stable positive branches survive any consistent
refinement; a universally excluded branch stays excluded. A merely
possible branch need not survive.

**Proof.** A universal statement on a set remains true on a subset. An
existential possibility can lose all its witnesses when that set shrinks. □

For example, an unspecified principal beneficiary of causative *kṛ* does
not license free *kārayati/kārayate* variation. It asks for semantic evidence.
With the 1.3.77 upapada condition positively established, the two outcomes
are genuinely licensed branches. These are different relations.

## S6. Ownership and visibility are compositional interfaces

The next rule receives the whole typed constituent state, not only the
previous rule's output string. In causatives the root's vṛddhi precedes the
derived-dhātu boundary, while guṇa before śap targets ṇic's own *i*. In a
yak passive its *k* continues to supply the kit trigger after marker lopa.
Both statements require affix ownership and original-marker queries.

The rules 6.4.22 and 8.2.1 keep PG1/PG2's distinct, query-relative contracts.
PG14 does not propose a universal visibility formula. A later operator lift
must commute with each declared query; it cannot erase history and claim
commutation from agreement of final spellings.
