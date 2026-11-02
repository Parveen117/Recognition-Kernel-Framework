# PG17 — Native branching before classical word observation

Author: Monty. 2 November 2026.

## N1. Carrier, old corner and pairing

Start from the canonical native cut field C=C_Σ with its derived iota
and scalar dagger. Extend PG16's event labels by the newly constructed
semantic, pada, iṭ, causal-continuation and phonetic events. Set

\[
 B_{17}=C\langle z_e,z_e^*:e\in E_{\leq17}\rangle,
\]

the algebra of finite cut-linear combinations of ordered residue words.
The empty word is 1, multiplication concatenates in operator order and
dagger reverses words while swapping each letter with its starred partner.
There is no imposed commutation, scalar-time interpretation, positive
metric or analytic completion.

Let H_old be PG16's histories and H_new the new basic/causal future
histories, each with its full starting frame, original source/marker data,
owned sounds, branch witnesses, intermediate states and open obligations.
Construct finite-support right modules

\[
 M_{17,\lambda}=\bigoplus_{h\in H_{old}\sqcup H_{new}}e_h B_{17},
 \qquad M_{17,0}=\bigoplus_{h\in H_{old}\sqcup H_{new}}e_h C.
\]

Grades distinguish frame, derived dhātu, selected pada, augmented affix,
ending, phonetic word and accepted/excluded/open outcome types. Only
matching source/target grades compose. Different iṭ or pada choices are
different histories even if a later word observer identifies them.

The old algebra embeds by preserving old residue words. Extend its
coefficients and include its histories as a direct summand. Extend old
operators by zero on the new sector: the old identity maps to P_old,
not the identity on the enlarged module. This preserves old products
and adjoints and does not create a second shared operator engine.

Declare the algebra-valued pairing

\[
 \langle x,y\rangle_B=\sum_h x_h^*y_h.
\]

The finite sum is sesquilinear and algebraically nondegenerate, since
pairing with each e_h detects its coordinate. No positivity or physical
probability claim is added. This is the same explicit pairing construction
as PG14–PG16, now on the larger typed carrier.

## N2. Guard cuts and dependent branches

A reviewed guard partitions its history domain into true, false and
unknown sets. Their coordinate cuts are orthogonal, self-adjoint and
sum to the identity of that domain. Unknown is not the false channel;
a selected grammatical option is not an unknown guard.

For each licensed e:h→h′ use the right-linear operator

\[
 T_{e,\lambda}(e_h a)=e_{h'}(1+z_e)a,
\]

zero on other source coordinates. The updated h′ contains the actual
change, not a wordless label. Its pairing adjoint sends
\(e_{h'}a\mapsto e_h(1+z_e)^*a\); that adjoint is not automatically
a licensed reverse Sanskrit rule. Finite sums and matching typed
composition give the admitted operator family. The finite choice sets
and retained immediate prefixes ensure the relevant maps/adjoints act
on finite support.

The basic branch structure is the dependent sequence

\[
 F\longrightarrow L\longrightarrow P
   \longrightarrow I(P,L,\ell)\longrightarrow W,
\]

where L is the selected future and I is the **fibre of licensed iṭ
choices over the actual pada/affix/root state**. In the causal sector
the derived-dhātu formation is retained before outer iṭ; role/pada
selection follows the inherited causal relation. These are typed source
dependencies, not a claim that all grammar is one universal pipeline.

## N3. Typed zero-specialization and exact recovery

Let ε:B_17→C take the empty-word coefficient. Nonempty words remain
nonempty under multiplication, so ε is a unital dagger-preserving algebra
homomorphism. Set

\[
 \pi_{0,M}(\sum_h e_h a_h)=\sum_h e_h\epsilon(a_h),
 \qquad \Pi_{0,op}(A)=(\epsilon(A_{kh}))_{k,h}.
\]

Frames, source choices, original sound identities and history labels are
unchanged. Pairing scalars specialize by ε. Calendar information is the
PG16 input adapter; neither ε nor a residue generator defines elapsed time.

**Theorem N3.** Every admitted finite operator construction A satisfies

\[
 \pi_{0,M}(Ax)=\Pi_{0,op}(A)\pi_{0,M}(x),
 \qquad
 \epsilon(\langle x,y\rangle_B)
   =\langle\pi_{0,M}x,\pi_{0,M}y\rangle_C.
\]

Specialization preserves typed products, sums, adjoints, cuts and their
complements. The unit-start accepted derivation relation of P4 is recovered
exactly, with the same conditional, Excluded and Open classifications.

**Proof.** For each event, ε((1+z_e)a)=ε(a). A guard cut depends on
retained history/evidence, so it selects the same coordinates on both
sides. The adjoint uses ε((1+z_e)*)=1. Algebra-homomorphism properties
give finite products and sums, and the dagger property gives the pairing
identity coordinatewise. Induction proves the composite statement.

Every unit-start finite path has constant coefficient 1 in the ordered
product of its event payloads, so it survives specialization with its
history. Every classical edge in the presented relation has exactly the
same guarded native edge. Thus there is recovery in both directions,
including separate negative/open outcomes. Distinct licensed choices
occupy distinct history coordinates and do not cancel. □

The support statement does not extend to arbitrary signed combinations
of inputs, which may cancel under ε. The algebraic compatibility identity
does. Source policies depending on invisible residue, infinite grammar
search and new relations on B would need additional proofs.

## N4. A three-branch future operator, not four independent options

Fix one completed kṛp lṛṭ frame and one agreement slot. Let T_P
create its two source-licensed pada histories h_P,h_A. Then the
dependent iṭ operation acts with fibres {0} over P and {0,1} over A.
Writing U_e=1+z_e gives

\[
 T_I T_P e_h
 =e_{P0}U_{0|P}U_P
  +e_{A0}U_{0|A}U_A
  +e_{A1}U_{1|A}U_A.
\]

There is no accepted e_P1 branch. Both A alternatives are positively
licensed by 7.2.44; the absent P1 is prohibited by 7.2.60, not merely
unobserved. At zero the output is exactly e_P0+e_A0+e_A1. No factor
of 1/2, normalized probability or empirical frequency is implied.

To describe a search space separately, introduce four **hypothesis**
labels P0,P1,A0,A1. They are candidate states, not four derived words.
The admissibility cut on this space is diag(1,0,1,1); its complementary
P1 channel carries the source-exclusion witness. Only after that typed
decision may an accepted grammar edge be constructed. Keeping a candidate
list is lawful; reporting all four as accepted alternatives is not.

**Proposition N4.** The dependent composition has exactly the licensed
joint support, and its admissibility/complement cuts commute with ε.
In particular it cannot be replaced by independent pada and iṭ menus
without an additional compatibility relation.

**Proof.** Each term in the displayed composite corresponds to one member
of its actual iṭ fibre, and every fibre member is included. P1 has no
licensed source edge. The hypothesis-space cut has constant 0/1 entries,
so ε preserves it and its complement. The independent Cartesian product
contains P1, proving strict inequality of supports. □

For vṛt the analogous joint support is {P0,A1}; for syand it is
{P0,A0,A1}. For svṛ the sya fibre is {1} but the tās fibre is {0,1}.
These source-derived examples show why a root's unqualified “veṭ” label
is not the whole native state. They do not make optionality a physical
superposition or establish a universal grammar priority order.

## N5. A whole P paradigm can still conceal lexical identity

Take the two exact basic root objects vṛt 1010862 and vṛdh 1010863,
the same future-general/controller conditions and the licensed P choice.
R5 and P2 prove that both give the full tuple L_P(vartsy). Define the
word observer O_P to return all nine P spellings, forgetting the root
entry and its derivation. Then

\[
 O_P(vṛt)=O_P(vṛdh),\qquad vṛt\ne vṛdh.
\]

**Proposition N5.** No function of this complete P tuple alone can
recover the correct root identity on the two-element domain. Asking
more of these same nine P positions cannot repair the loss. A forward
query for the licensed A third singular separates this pair.

**Proof.** If a decoder d existed, applying it to the common tuple would
give both distinct root IDs, a contradiction. Any selection or repetition
of its components remains equal for the two roots. Under the independent
forward A query, the outputs are vartiṣyate and vardhiṣyate, distinct
by R5. Thus the augmented observation distinguishes exactly this pair. □

The A query is a fresh forward derivation from the retained initial
frame, using 1.3.92's allowed alternative. It is not a reverse linguistic
rule that reconstructs an unknown root from vartsyati. Nor does this
two-root result provide a universal Sanskrit recognition decoder.

The native module never identified the two initial roots or their char
histories. Its zero-reading retains them too. It is the later word-only
observer, not zero-specialization, that loses this lexical information.
This gives a new grammar-specific instance of the established recognition
boundary while preserving the existing operator and pairing assumptions.

## N6. Unconstructed interfaces

No executable adapter from the old Python record structures to this
extended native family is supplied. No infinite completion, probabilistic
semantics for optionality, accent reconstruction or universal source
resolver is proved. The shared operator engine remains unchanged, and
its old evidence is neither rerun nor promoted by this written extension.
