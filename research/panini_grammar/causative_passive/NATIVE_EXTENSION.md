# PG15 — Native extension, causal cuts and an explicit memory repair

Author: Monty. 2 November 2026.

This construction extends the admitted operator instance of
[PG14 N1–N7](../grammar_construction/NATIVE_OPERATOR_LIFT.md). Its native
cut field, typed cuts, residue paths and pairing precede the word reading.
The shared `operator_foundation/` engine and its established theorems are
unchanged. Lambda names the full operator carrier below, not a scalar,
derivative order or clock.

## N1. Conservative extension of the carrier and its grades

Let C be PG14's native cut field, with its derived iota and scalar dagger.
Let E₁₄ be its source-bearing event labels. Add a disjoint family E₊ of
PG15's typed events: causal-role designation; expressed-karman selection;
case/discourse decisions; owned yak introduction; ṇic-lopa; the selected
visibility queries; and the written finishing/observation events.
When a PG14 operation is reused inside a new causal history, its rule
schema and source are retained, with the new history's own event instance.

Construct

\[
 B_{15}=C\langle z_e,z_e^*:e\in E_{14}\sqcup E_+\rangle,
 \qquad \iota_B:B_{14}\hookrightarrow B_{15}.
\]

Elements are finite cut-linear sums of ordered residue words. Dagger
reverses words and interchanges each generator with its formal adjoint.
The inclusion is injective and unital: the old words remain a subset of
the free word basis. No equation makes distinct source events commute.

Define ε₁₅ by retaining only the empty-word coefficient. Then

\[
 \epsilon_{15}(uv)=\epsilon_{15}(u)\epsilon_{15}(v),\qquad
 \epsilon_{15}(u^*)=\overline{\epsilon_{15}(u)},\qquad
 \epsilon_{15}\iota_B=\epsilon_{14}.
\]

Let H₊ be the new finite histories on the domains in K1/K6 and L1. Their
initial types include the formation request and the whole causal/basic
frame. Let H₁₅=H₁₄ ⊔ H₊. No old completed history is given a new outgoing
rewrite merely because its word happens to match a new word. Extending a
domain is accomplished by new typed initial histories, not by revising
the old accepted labels.

The right modules and their zero-readings are

\[
 M_{15,\lambda}=\bigoplus_{h\in H_{15}}e_hB_{15},\qquad
 M_{15,0}=\bigoplus_{h\in H_{15}}e_hC,
 \qquad
 \pi_{0,M}(e_hb)=e_h\epsilon_{15}(b).
\]

Use finite support and the explicit algebra-valued pairing

\[
 \langle x,y\rangle_{15}=\sum_h x_h^*y_h.
\]

This pairing is sesquilinear and algebraically nondegenerate. It does
not assume a positive norm, Hilbert representation or probability. The
grammatical source/target type grades and complementary histories remain
part of each summand. Zero-reading does not erase the causee, source,
deleted i, variant choice or sequence of rule applications.

For precision, the old sector inside this module is the base extension
\(M_{14,\lambda}\otimes_{B_{14}}B_{15}\). Its pairing is
\(\langle x\otimes a,y\otimes b\rangle
=a^*\iota_B(\langle x,y\rangle)b\).
Old operators extend by base change there and by zero on H₊. Their sums,
products and adjoints are preserved, and their action on old inputs is
unchanged. The identity of this old sector becomes the aperture P_old,
**not the identity of the entire enlarged module**. This is the correct
corner embedding; claiming a unital embedding of old operators by this
zero extension would be false. The coefficient inclusion above is unital
and is a different map.

## N2. New cuts, local operators and exact zero-recovery

For every declared semantic/formation predicate S, retain its history
coordinates with the cut P_S and preserve the complement Q_S=1−P_S.
Use separate true/false/open cuts when the source question is unresolved.
These cuts are self-adjoint idempotents for the declared pairing.

Each admitted edge e:h→h′ has the right-B₁₅-linear action

\[
 T_e(e_hb)=e_{h'}(1+z_e)b,
 \qquad T_e(e_kb)=0\quad(k\ne h).
\]

Its target history contains the actual state transition. For example,
the ṇic-lopa edge changes precisely the owned i to an unpronounced
occurrence while retaining its teaching form and cause. A selection
edge changes the expressed-karman/controller fields, not the root sounds.
Its pairing adjoint sends \(e_{h'}b\) to \(e_h(1+z_e)^*b\).

Every outgoing source choice here is finite. A complete history retains
its unique immediate prefix, so incoming events are finite as well.
Locally finite rule sums and their adjoints consequently act on finite
support. Domain restrictions, owner tests, pratyayalakṣaṇa queries,
Tripādī visibility and person/number guards read the retained state,
not coefficients of invisible residue words. This interaction law is
part of the admitted model.

Let Π₀,op apply ε₁₅ entrywise to the typed operator matrices. For every
generated finite expression A and finite-support x,

\[
 \boxed{\pi_{0,M}(Ax)=\Pi_{0,\mathrm{op}}(A)\pi_{0,M}(x)}.
\]

It preserves typed sums, products, the declared cuts and their complements,
adjoints and pairing. In particular

\[
 \epsilon_{15}(\langle x,y\rangle_{15})
 =\langle\pi_{0,M}x,\pi_{0,M}y\rangle_0.
\]

**Proof.** An edge reduces to
ε₁₅((1+z_e)b)=ε₁₅(b). A history cut has an unchanged membership indicator.
Adjoints use ε₁₅(u*)=overline{ε₁₅(u)}. Products and locally finite matrix
entries use only finite sums on an admitted input and the homomorphism
identity. Induction gives every expression; the pairing identity follows
coordinate by coordinate. The same argument applies to the old-sector
inclusion, because ε₁₅ι_B=ε₁₄. □

For a unit initial history, every accepted branch has coefficient
\((1+z_{e_n})\cdots(1+z_{e_1})\), with empty coefficient 1. It survives
zero-reading with its exact branch history. Conversely, every classical
branch constructed in K/L/D has exactly those lifted edges and the same
guards. Thus zero-reading recovers **all and only the labelled finite
branches of this presented construction**, including the alternatives
of K5. It is not only the forward inclusion of successful examples.

This support assertion concerns unit-start branches, not arbitrary signed
superpositions, which can cancel after specialization. Nor does it prove
that the source domain is the whole Sanskrit grammar. The source-policy
premises of K5 and the formation premises of L6 remain explicit.

## N3. Optional selection, multiplicity and the meaning of the adjoint

At a completed frame history h_F, let J(F)=B(F) be K3's dependent set of
branches. Construct the selection operator

\[
 S(e_{h_F}b)=\sum_{j\in J(F)}e_{h_{F,j}}U_jb,
 \qquad U_j=1+z_j.
\]

The target histories are distinct even if their future verbs are identical.
For the pairing above their cross terms vanish, giving

\[
 S^*S(e_{h_F}b)=e_{h_F}
       \left(\sum_{j\in J(F)}U_j^*U_j\right)b.
\]

After specialization,

\[
 S_0^*S_0(e_{h_F}c)=e_{h_F}\,m(F)c,
 \qquad m(F)=|J(F)|.
\]

| Frames on the stated causal domain | m(F) | Reason |
|---|---|---|
| bhū, sthā, gam, nī, pac, dā, kṛṣ | 1 | unique admitted (χ,q) |
| vid, budh, pā | 2 | either eligible karman, with χ=K fixed |
| kṛ, hṛ | 2 | dependent alternatives (K,b) and (Agt,c) |

This is an algebraic multiplicity formula. S is not a unitary operation,
and its adjoint is not an instruction to reverse Sanskrit rules. Two
grammatical alternatives do not acquire a 50/50 probability from their
presence in this sum. No probabilistic normalization has been admitted.

Within one root/formation fiber the stem path in L3 is the same for every
j; the later ending depends on slot(q). Reusing that stem *schema* is
legitimate. Merging the two histories before retaining q is not: D4 gives
one branch with 3pl and one with 3sg. Even when both slots coincide, the
different case assignments and source choices survive in the target types.

## N4. A surface-only causal selector cannot descend

D6 supplies two accepted histories with the same third-person singular
word *gamyate*: h_s for the simple passive and h_c for the causative
passive. Their different frames may be supplied independently; this
argument does not require one fully specified clause to have two meanings.

Restrict to their two summands

\[
 X=e_{h_s}B_{15}\oplus e_{h_c}B_{15}\cong B_{15}^2.
\]

The fixed word observer adds coefficients which print the same word:

\[
 O:X\to Y=e_{\textit{gamyate}}B_{15},\qquad
 O(a,b)=a+b.
\]

The native causal cut is P_c(a,b)=(0,b), with complement P_s. It is a
self-adjoint aperture for X's original orthogonal pairing.

**Theorem N4.** There is no right-B₁₅-linear D:Y→Y such that
\(OP_c=DO\). The obstruction also holds on the zero-reading over C.

**Proof.** The vector x=(1,−1) lies in ker O. But
\(OP_cx=O(0,-1)=-1\ne0\). If D existed, DOx=D0=0, a contradiction.
The same unit and nonzero −1 remain after ε₁₅, proving the second claim. □

At the set level this says the word alone does not determine whether
the retained derivation contains ṇic. At the module level the theorem
gives the exact failure of the kernel-invariance condition for descent.
It is an obstruction for this **specified observer**, not a theorem that
no richer surface context or semantics could distinguish the histories.

The obstruction is not repaired by taking lambda to zero. It already
exists between two classical histories. Conversely, retaining the
zero-history type is sufficient to preserve the causal cut. Thus word
erasure and zero-specialization are different operations.

## N5. One extra channel repairs this two-history observation

Keep the original word channel and add the causal coefficient:

\[
 R:X\to\widetilde Y=B_{15}\oplus B_{15},\qquad
 R(a,b)=(s,c)=(a+b,b).
\]

The first component is exactly O. The inverse is

\[
 R^{-1}(s,c)=(s-c,c).
\]

Both are right-B₁₅-linear; their coefficients 0,1,−1 are central, so no
commutation of residue words is assumed. This produces the descended
cuts explicitly:

\[
 \widetilde P_c=RP_cR^{-1},\quad
 \widetilde P_c(s,c)=(c,c),
 \qquad
 \widetilde P_s(s,c)=(s-c,0).
\]

They are complementary idempotents. Their meaning is that the causal
part contributes to both the observed word and the retained causal
channel; it is not merely the coordinate projection (s,c)↦(0,c).

Preserve the native pairing by transport:

\[
 \boxed{\langle(s,c),(t,d)\rangle_R
       =(s-c)^*(t-d)+c^*d.}
\]

For x,y∈X this gives ⟨Rx,Ry⟩_R=⟨x,y⟩_X. Nondegeneracy follows from
the inverse, and the transported causal/simple cuts are self-adjoint for
this pairing. Using the unqualified coordinate-orthogonal pairing on
\(\widetilde Y\) instead would change that claim: \(\widetilde P_c\)'s
matrix \(\begin{pmatrix}0&1\\0&1\end{pmatrix}\) is not its coordinate
conjugate transpose. Transport is therefore necessary, not decorative.

The matrices of R and R⁻¹ have constant coefficients, so

\[
 \pi_{0,\widetilde Y}R=R_0\pi_{0,X},\qquad
 \pi_{0,X}R^{-1}=R_0^{-1}\pi_{0,\widetilde Y}.
\]

Applying ε₁₅ to the transported pairing gives the same formula over C.
The repair, its cuts, its inverse and its pairing all recover their
declared classical counterparts exactly.

Zero extra channels with the fixed O fail by N4; this one extra B₁₅-valued
channel succeeds on X. That is the stated minimality: between **no added
channel** and this explicit **one-channel augmentation**, with O retained.
No general rank theorem for free noncommutative modules, no universal
minimal observer for all grammar histories, and no claim against arbitrary
alternative encodings into B₁₅ is needed or asserted.

## N6. Equal pronunciation need not give equal ordered operators

The local nī schedules in L4 use ayādi and lopa events.
When both schedules are admitted with their stated visibility queries,
they have the same final owned pronunciation nāy|∅|ya. They still have
different full histories. Write A₁,L₁ for the events of the first
schedule and L₂,A₂ for those of the second. Their source/target histories
are different, so their typed event instances are distinct. Even
identifying their visible endpoint would not equate their native residue
coefficients:

\[
 (1+z_{L_1})(1+z_{A_1})
 -(1+z_{A_2})(1+z_{L_2})\ne0.
\]

For example the first product's word z_L₁z_A₁ has coefficient 1 and is
absent from the second. The nonzero claim uses the free residue-word
basis without identifying distinct typed edges by their rule name. Both coefficients
have empty coefficient 1, but zero-reading still retains the different
history labels. Only an additional observation can forget the schedule.
PG15 does not impose an unwarranted commuting square on the full carrier
or infer global termination/confluence from this local endpoint equality.

Evolution in this packet means typed ordered composition with retained
events. The number of events does not represent elapsed physical time.
No physical clock, metric or dimensional constant is being selected.

## N7. Exact boundary of the new result

The packet constructs a conservative extension of PG14's admitted native
family; exact zero-recovery for its new source-policy branches; the
selection multiplicity formula; one genuine surface no-descent instance;
and an explicit finite observation repair preserving the pairing.

Runtime integration with existing Python sound records, extra native
relations, infinite completions and a minimum sufficient observer for
the full grammar remain separate obligations. The new written construction
does not replace them by a certificate count or alter the canonical engine.
