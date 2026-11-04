# PG47 — Addressed transition interface for written grammar

Author: Monty. 4 November 2026.

Continue [PG46](../independent_written_closure/README.md). Both tracked ID
sets already contain 3,983 entries. This packet constructs an interface and
worked histories for selected interactions among those clauses. It adds zero
catalogue IDs and no new agreement positions. It is a written construction,
not a parser, running scheduler or complete grammar implementation.

## I1. Full carrier before the grammar observation

The primitive remains the full operator/history carrier with typed cuts, cut
field, derived iota, pairing, dagger, tensor types, complementary channels and
ordered history. [Native continuation](NATIVE_CONTINUATION.md) supplies its
conservative extension and typed zero-reading. A grammar state is an annotation
of a history coordinate; it does not replace that carrier with a word string,
scalar parameter or Hilbert-space representation.

On the finite domains of this packet, write a supplied annotated state as

\[
q=(r,T,O,E,D,V,P,H,\Omega).
\]

|Coordinate|Meaning and required invariant|
|---|---|
|r|Revision identity of this annotated state; it is not physical time|
|T|Typed root, base, affix, augment and sound tokens, with active versions and retained origins|
|O|Ownership/constituent relations; an inner affix remains distinct from its host and an outer suffix|
|E|Supplied evidence, source witnesses and T/F/? gate values, with their dependency addresses|
|D|Designation records containing bearer, originating rule and clause, policy, cause, domain and admitted consumers|
|V|The current query's view: active surface, retained provenance or a specifically licensed earlier view|
|P|Declared edition, commentary policy, register and optional-branch identity|
|H|Ordered event and decision history, including alternatives and reasons for exclusion|
|Ω|Named unresolved admission, realization, accent, lexical and integration obligations|

The supplied domain has finite token sets and well-formed ownership. A token
identifier is not a Sanskrit spelling. A substitution retains its constituent
identity and origin record, creates the appropriate current value and fresh
sound-version addresses, and records how those sounds descend from the old
value. Whole-token lopa makes the addressed token inactive; it does not erase
its origin. A historical query can address an inactive token when its consumer
licenses that view. Ordinary active-sound adjacency cannot do so automatically.

Lexical entries, semantic relations, accent, syllable weight and source-policy
choices are supplied only where stated. This interface does not infer them
from spelling. In particular, अर्थवत् supplies signification, not external
truth or existence.

## I2. Instruction and consumer records

Before asking whether an action applies, form an instruction record

\[
\mathsf{Instr}=(s,p,a_t,a_e,k,x,c,v,\Delta,\mathcal G).
\]

|Field|Content|
|---|---|
|s,p|Source rule and adopted interpretation policy|
|a_t,a_e|Target and environment addresses, including constituent and sound versions|
|k,x|Operation kind and extent: whole constituent, final sound, initial sound, टि, उपधा, insertion or read-only query|
|c,v|Consumer and the view it is allowed to use|
|Δ|Dependency footprint: inspected tokens, meanings, designations, scope, adjacency and competing admissions|
|𝒢|Necessary positive gates and decisive exclusion gates, each with evidence and owner|

The case expression in the grammatical prescription is interpreted before
mutation. It is distinct from a sentence constituent's case ending. A fixed
part–whole genitive is not converted into replacement merely because it is
genitive; 1.1.49 applies in its declared undetermined-relation domain.
1.1.55 and the marker-specific controls decide replacement extent. 1.1.66/67
decide direction and adjacency under the admitted interpretation. The
[A histories](INSTRUCTION_HISTORIES.md) instantiate these distinctions.

A designation query has the additional record

\[
d=(a,\text{label},\text{origin},\text{cause},\text{domain},c,v).
\]

Origin here includes the **rule, clause and adopted commentary policy**;
a sūtra number alone can be too coarse. Equal labels do not imply equal
permissions. Thus the main एकविभक्ति clause's 1.2.44 उपसर्जन record
cannot be consumed by 2.2.30 as though it came from 1.2.43. Nyāsa's separate
च supplement within 1.2.44 can license the prefix's ordering designation;
that is a different clause record. A deleted affix's
designation can remain queryable without reviving a prohibited base operation.
The [B histories](DESIGNATION_HISTORIES.md) make both distinctions concrete.

## I3. Admission, atomic application and Open exits

For one fixed instruction, request, revision and policy, evaluate only its
necessary gates and decisive exclusions. A necessary gate known false, or an
applicable exclusion known true, supplies a local denial. In the absence of
such a decisive denial, an unresolved required gate gives Open. Admission
requires every necessary gate T and every decisive exclusion F, together with
resolved ownership, view, extent and required competition evidence.

|Result|Exact meaning|
|---|---|
|APPLIED|The admitted instruction was carried out at its named scope; a pure query produces a decision record without a token mutation|
|BLOCKED|The particular request has a decisive source-grounded denial; this does not declare the whole word impossible|
|OPEN|Required evidence or policy is missing or unresolved; no requested grammatical mutation is licensed|

For APPLIED, retain the pre-state, instruction, evidence dependencies and
chosen branch in the event record, make the owned change, assign the next
revision, and record the post-state and remaining obligations. A coupled
instruction is admitted as a unit: one may not keep its stem alteration while
discarding its required suffix, or pair one branch's operation with another
branch's suffix. Logical atomicity does not collapse its grammatical substeps;
the written history still gives their order and ownership.

BLOCKED and OPEN may append a decision/obligation record; they do not carry
out the denied or unresolved mutation. Every recorded decision, including a
pure query and an OPEN/BLOCKED result, creates a new history node and revision
when appended, even if all active tokens are unchanged. A locally APPLIED step can still leave
accent, later morphology or lexical decisions in Ω. A source's displayed word
is marked as a witness until the specified realization steps have been given.
An unaccented stem result does not certify its declined paradigm or Vedic accent.

## I4. Freshness and competition

An admission record is tied to revision r and its dependency footprint Δ.
After a grammatical mutation, reassess every subsequent instruction against
the new revision. This packet uses explicit reassessment, not an implicit
cache. Reusing a historical feature requires its own source permission;
retaining a fact in H alone does not make every consumer eligible to use it.

Competition records contain the candidate instructions, their independent
admissions at the same revision, collision evidence, strength or exception
relation, visibility, policy and the eventual decision. Conflict is not
limited to two writes at the same sound address. A change to an affix can
remove a stem operation's environmental trigger: the read dependencies matter.
Conversely, different rule numbers alone establish no competition.

Invoke 1.4.2 only for the admitted simultaneous equal-strength collision.
Source-qualified exception, nitya and visibility relations retain their own
domains. Unknown strength is not silently treated as equality. After choosing
an action, retain the losing candidate and reason; do not replay it with an
old admission record. The source's जाति/द्रव्य reapplication accounts remain
separate policies, not an optional pair of output forms. See
[Competition histories](COMPETITION_HISTORIES.md).

## I5. Dependent branches and realization obligations

For supplied input q and fixed policy p, let J(q,p) contain only admitted
grammatical branches, and retain their dependent output family

\[
\coprod_{j\in J(q,p)}(q,p,j,H_j,\Omega_j).
\]

The family carries each branch's owned operations. It is not the Cartesian
product of independent lists of stem changes and suffix choices. In 4.1.38
the three admitted branches retain their specified coupling. At 4.1.78 the
replacement addresses the qualifying inner अण्/इञ्, and the outer feminine
suffix remains separately owned. An अञ् origin or an unknown origin cannot
be replaced by guessing from a similar surface. Ordered precursor changes
must be established before testing a later syllable-weight gate. See
[Realization histories](REALIZATION_HISTORIES.md).

Mutually incompatible commentary policies label different supplied inputs;
they do not automatically create optional Sanskrit variants. A policy-sensitive
request without a chosen or otherwise resolved policy stays Open at that
decision. Unresolved obligations remain attached to the exact branch that
needs them, even if two branches later have equal visible words.

## I6. Three bounded preservation statements

**Address safety.** An admitted instruction cannot mutate another constituent
merely because the two have equal surface strings. Its map is defined on the
resolved address and extent in q; a different address is outside that map's
domain. Retaining origin and sound-version maps preserves this distinction
after replacement. This proves a property of the declared maps, not correctness
of an external parser's supplied addresses.

**No promotion by evidence loss.** Fix q's structural history/revision,
instruction, request and policy, and order evidence by replacing T or F with ?.
A clause that was not admitted cannot become admitted solely through this
loss of evidence. Proof: admission is the conjunction of required T values
and required F exclusions; replacing either by ? cannot make that conjunction
true. A previous denial may become Open. The statement does not compare
different revisions, policies or newly supplied source facts.

**Legal finite composition.** If each event is admitted against the post-state
of its predecessor, their concatenation retains address, cause, policy and
obligation records. Proof is induction on the given finite path: each next
step has its own checked domain and appends rather than erases its record.
Parenthesizing this same ordered path does not change its composition.
Swapping steps is a different assertion and is not established here. An
append-only history does not prove that a general derivation terminates, that
all paths agree, or that every Sanskrit form has a path.
