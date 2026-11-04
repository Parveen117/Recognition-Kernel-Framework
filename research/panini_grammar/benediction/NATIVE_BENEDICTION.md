# PG20 — Native benediction, dependent choices and marker refinement

Author: Monty. 2 November 2026.

## N1. Full carrier and old-sector inclusion

Start from the canonical cut field C_Σ, its derived iota and scalar
dagger. Extend PG19's source-labelled event alphabet by the new āśīs,
class override, kit/ṅit, s-ownership, ciṇvat, tātaṅ and sound events:

\[
 B_{20}=C_Σ\langle z_e,z_e^*:e\in E_{\le20}\rangle.
\]

These are finite ordered residue words; dagger reverses the word and
stars its letters. The empty word is 1. This declaration supplies no
primitive Hilbert space, scalar clock, positivity or physical realization.

Let H_old be the retained PG19/predecessor histories, H_new the histories
of D/E/B/C/L. A history includes the interpreted input, exact lexical
identity, source policy, expression/controller, actual lakāra, original
and current affix owners, teaching markers and overrides, augment origins,
rule-specific query views, branch choices and obligations. Define

\[
 M_{20,\lambda}=\bigoplus_{h\in H_{old}\sqcup H_{new}}e_hB_{20},
 \qquad M_{20,0}=\bigoplus_he_hC_Σ.
\]

Both are finite-support right modules. Matching grades govern composition:
interpreted input, mood/class selection, role/pada/controller, root formation,
ending/augment ownership, addressed marker/stem query, completed morphology,
phonetic readout and Accepted/Excluded/Open outcome. The new meaning does
not overwrite an old initial frame.

Old coefficients embed in B_20; old operators extend by zero on H_new.
Their local identity is P_old, not the total identity. The new construction
is an admitted grammatical family on the canonical home, not another engine.

## N2. Pairing, cuts and licensed operators

The native pairing is

\[
 \langle x,y\rangle_B=\sum_hx_h^*y_h.
\]

It is sesquilinear and algebraically nondegenerate: pairing with a basis
vector detects its coordinate. No analytic or positive metric is assumed.

For each addressed source query r on its typed domain, let P_r^T,
P_r^F and P_r^? be the coordinate cuts for true, false and unresolved
evidence. They are self-adjoint orthogonal idempotents and sum to that
domain's identity. The guard reads h and its queried owner q, never the
residue coefficient. Different source-licensed alternatives create distinct
positive histories; unresolved evidence creates Open obligations.

For each licensed event e:h→h′ define

\[
 T_e(e_ha)=e_{h'}(1+z_e)a.
\]

The adjoint has coefficient (1+z_e)^* on the reversed pair of history
coordinates. It is an algebraic adjoint, not a licensed reverse grammar
rule. Prefix-retaining histories and finite local branching give finite
incoming/outgoing event supports, so the admitted finite operator sums,
products and adjoints preserve finite support.

The important new views are:

| Query | Retained premise |
|---|---|
| 3.4.116 | liṅ plus actual āśīs; overrides rather than accumulates the affix class |
| 3.4.104 | P ending; kit replaces this ṅit prescription |
| 1.2.11–13 | exact root and actual jhal-initial A ending after augmentation |
| 7.2.35 | actual initial y versus s, and the addressed basic/derived boundary |
| 8.2.29 | which s belongs to yāsuṭ, suṭ or the original ending; final versus internal conjunct |
| 6.4.51 | ordinary versus ciṇvat augment origin and the declared local visibility |
| 8.3.78–79 | actual constituent before ṣīdhvam or iṭ; no global invisibility of i_cv |
| 7.1.35 | actual owned tu/hi; āśīs; whole substitute and marker override |
| 6.4.105/106 | actual hi after the ending choice, not every historical substitute |

## N3. Typed zero-recovery

Let ε:B_20→C_Σ select the empty-word coefficient. No product of
nonempty free words is empty, hence ε is a unital dagger algebra
homomorphism. Define the separately typed maps

\[
 \pi_{0,M}(\sum_he_ha_h)=\sum_he_h\epsilon(a_h),\qquad
 \Pi_{0,op}(A)=(\epsilon(A_{kh}))_{k,h}.
\]

Use ε also on pairing values. Histories, owner labels, source choices
and unresolved obligations remain in h after specialization.

**Theorem N3.** Every admitted finite PG20 construction satisfies

\[
 \pi_{0,M}(Ax)=\Pi_{0,op}(A)\pi_{0,M}(x),\qquad
 \epsilon\langle x,y\rangle_B
 =\langle\pi_{0,M}x,\pi_{0,M}y\rangle_{C_Σ}.
\]

Typed products/sums, adjoints, cuts and their complements specialize
compatibly. Forward unit-start grammatical paths recover exactly the
declared finite relation, including its complementary outcomes.

**Proof.** For an event, ε((1+z_e)a)=ε(a). Query guards are unchanged
because h/q survive. The coefficient homomorphism proves the product and
pairing identities; dagger commutes with ε. Finite induction gives the
general operator statement. Each forward grammar history has constant
coefficient 1 at its separate terminal coordinate, and each zero path has
the same guarded native edge sequence. This proves both directions of
the stated relation recovery. □

The relational statement does not license adjoint reverse edges or promise
support preservation for arbitrary signed combinations. Those combinations
can cancel. There is no infinite-search or universal-scheduler theorem here.

## N4. Dependent choice refinement, not independent switches

For a completed input F and fixed slot p, define a finite branch fibre
in this order, with absent queries represented by one **not-applicable**
value rather than duplicated branches:

1. Select the admitted lakāra and its affix class.
2. In eligible Bhāva/Karma āśīrliṅ select O or the coupled (C,i_cv).
   Within causal C and mit, select short/long; elsewhere length is fixed.
3. Resolve only the source-licensed marker/augmentation route at that
   branch. Basic Karma gam offers kit/non-kit; P kit is forced; a
   visible A i_val or i_cv removes a jhal premise. Augment origin is
   selected before that addressed marker query, with the source-specific
   visibility kept explicit. The rules do not supply every combination.
4. On blessing-loṭ P tu/hi select ordinary or tātaṅ; otherwise that
   query is not applicable. Apply the new marker view before its stem query.
5. At A āśīrliṅ 2pl only, select E6's δ relation on the resulting
   owned constituent/augment. Other slots have no δ fork.

Different applicable stages are placed at their proper grades; this list
specifies dependencies, not an instruction to transport a future stage's
phonetic result into an earlier source query. C's local visibility remains
the declared PG18 policy.

**Proposition N4.** Successive finite refinements produce exactly P7's
branch relation. Their typed cuts retain all excluded/open alternatives,
and the relation commutes with N3's zero-specialization.

**Proof.** At each grade the true/false/unknown partition is exhaustive.
Only the stated true options get forward grammatical edges. The next
fibre is indexed by the already retained branch history, so O cannot
acquire a C-only length choice, i_cv cannot be independently omitted,
and a non-2pl slot cannot acquire a second δ reading. Induction on the
finite grades proves soundness and exhaustion of the constructed fibre.
P2–P6 enumerate those fibres; summing their cardinalities proves P7's
counts. The same guards and history labels survive N3, proving recovery. □

For causal śam Karma 2pl the fibre has four leaves: two O sound
readings and one each for C-short/C-long. It does not have the eight
leaves of three unrelated binary switches. All four leaf histories
retain the same selected q. This is a finite construction from supplied
source predicates, not a theory that all Sanskrit options are independent.

## N5. A weak/not-weak observer loses an active distinction

Consider the source-attested jāgṛ contexts just before their root-guṇa
query: ordinary vidhiliṅ with the prescribed ṅit ending, and āśīrliṅ
with its overriding kit ending. Their pre-query root phones and yāsuṭ
display agree. An observer retaining only that root/display and
`weak := kit or ṅit`, while forgetting the specific marker and modal
history, identifies the two contexts.

But 7.3.85's exclusion tests **ṅit**, not that disjunction. Its special
guṇa is excluded on the first context and admitted on the second,
giving jāgṛyāt versus jāgaryāt. Vac supplies an independent controlled
witness: 6.1.15 tests kit and gives vacyāt versus ucyāt.

**Theorem N5.** This coarsened observer cannot support either displayed
marker-sensitive query on its respective two-context fibre.

**Proof.** On the jāgṛ pair write q(e_N)=q(e_K)=e_w. The special
guṇa admission cut is D=diag(0,1). Then qD(e_K−e_N)=e_w, whereas
q(e_K−e_N)=0, so D cannot descend to the quotient observation.
The vac argument uses the corresponding kit-only cut. N3 retains the
two context coordinates and their cuts: zero-specialization is not the
cause of this information loss. □

Retaining the actual marker/override tag repairs these particular queries.
A linear injective repair of either two-coordinate span needs two output
coordinates and the labelled pair attains it. This is a local rank bound,
not a universal memory lower bound or a parser of unseen utterances.

## N6. Ending refinement cannot be postponed past a fixed stem query

Let h be the kṛ P 3sg blessing input. Let S perform the appropriate
stem query at its current owned ending. Let T choose the licensed tātaṅ
ending and its marker override **before** that query. Let D_t be the
proposed adapter that substitutes only the printed ending after S, leaving
the already selected root/vikaraṇa unchanged.

Then the two final readouts are

\[
 \operatorname{read}(S T h)=kurutāt,\qquad
 \operatorname{read}(D_t S h)=karotāt.
\]

The second is the failed adapter's prediction, not an admitted word in
this register. Krī similarly gives krīṇītāt versus that adapter's
krīṇātāt. The ordinary branches remain karotu/krīṇātu.

**Proposition N6.** No ending-only adapter D_t preserving the previously
selected strong stem makes this square commute on the displayed inputs.

**Proof.** T changes the actual marker premise of the stem query from
pit to ṅit with displaced pitness. L4 consequently changes kṛ's kar/o
to kur/u, and krī's śnā vowel to ī. An ending-only D_t cannot change
those constituents, so the readouts differ. The discrepancy is present
already at the zero-reading and is retained by N3. □

Re-running the correct addressed stem query after an ending update can
repair an implementation; the proposition specifically excludes that
recomputation from D_t. It does not prohibit every implementation order
or prove a universal rule of grammatical precedence.

## N7. Tātaṅ preserves person in history despite word syncretism

Choose two otherwise appropriate kṛ blessing frames whose expressed
controllers differ: third singular and second singular. Choose the
tātaṅ branch in each. Both standalone words are **kurutāt**, but their
original tu/hi, controller and person remain different in the histories.

Let W retain the root, formation, mood and final word while forgetting
the controller/person and original-ending owners. Then W(h_3)=W(h_2).
The second-person admission cut has different values on them.

**Proposition N7.** That person cut cannot factor through W on this
pair. Retaining either an adequate controller/person record or the
source-qualified original-ending distinction repairs this displayed query.

**Proof.** Any factorization would assign two values to the same W-output.
Equivalently q(e_3)=q(e_2), while the corresponding diagonal person cut
does not preserve ker(q). The two native coordinates and their pairing
remain distinct under π_0, so N3 preserves the full construction. □

External pronouns or discourse may disambiguate a real utterance; W
explicitly omits them. This is an exact finite observation boundary,
not a claim that Sanskrit speakers cannot recover person in context.

## N8. Remaining obligations

No executable bridge to the historical rule tables is constructed here.
The table adapters must preserve addressed kit/ṅit/pit conditions,
owned s cancellations, the selected visibility policy and the dependent
sound options. A complete conflict/visibility scheduler, wider lexical
domains, semantic parsing, accent and software/proof-assistant validation
remain separate work. The canonical operator engine is unchanged.
