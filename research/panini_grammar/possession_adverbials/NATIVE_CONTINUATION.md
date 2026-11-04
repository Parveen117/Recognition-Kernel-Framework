# PG37 — Addressed affix histories and compound fibres

Author: Monty. 4 November 2026.

## N1. Conservative extension of retained history

Continue [PG36](../taddhita_functional/NATIVE_CONTINUATION.md), with its
cut field \(C_\Sigma\), derived iota, dagger and finite-support history
carrier. Add event letters for the present relation/case decisions,
source clauses, original-affix selections, designations, addressed
substitutions, augmentations, insertions, deletions and compound extensions:

\[
B_{37}=C_\Sigma\langle z_e,z_e^*:e\in E_{\le37}\rangle,
\qquad
M_{37,\lambda}=(M_{36,\lambda}\otimes_{B_{36}}B_{37})
\oplus\bigoplus_{h\in H_{37}}e_hB_{37}.
\]

H contains histories, not merely words. Each retains the
[input](DOMAIN.md), adopted source policy, selected clause, compound tree,
affix token addresses, past/current scope and all unresolved obligations.
Histories from distinct branches are distinct coordinates even if a later
unaccented observer gives the same word.

The algebra map sending new event letters to zero and fixing old letters
retracts the old inclusion. Its induced map on scalar extension splits
\(m\mapsto m\otimes1\), so inherited vectors are not identified by this
extension. Extend the old pairing by scalar extension, make old/new summands
orthogonal, and on new coordinates use
\(\langle x,y\rangle=\sum_hx_h^*y_h\). Coordinate vectors prove
nondegeneracy on the new summand. No Hilbert positivity is assumed.

## N2. Evidence and current-view cuts

For each decisive gate g use mutually orthogonal coordinate cuts
\(P_g^T,P_g^F,P_g^?\), summing to I on its finite local domain. Missing
compound class, register, name identity, unit equality or policy is in
the ? cut. Residual selection requires affirmative admission and resolved
decisive exclusions. Thus losing evidence cannot promote Open into a
certified default branch. This is a property of the declared evidence
relation, not a proof that externally supplied annotations are true.

Scope transitions act on the current view while preserving past records.
For example, the 5.3.27 transition leaves the pre-direction designation
view. Its target lies in the direction cut; a selector requiring the old
current view has zero composition with it. Previously assigned designations
remain in history. The 5.4.54 ownership view similarly does not inherit
the old change-of-state च्वि branch merely because साति also appears there.

## N3. Address safety proposition

An operation is indexed by \((h,a,k)\): history h, token address a and
operation kind k. Augmentation includes whether a names the base or an
affix. Replacement retains the origin token with changed active value;
deletion marks that token inactive without deleting its provenance.

**Proposition.** On the declared domains, the ordinal and degree maps
cannot act on a different token with the same visible suffix name.

**Proof.** At 5.2.49/50/56–58, a is the selected डट् address; at 51–53
it is the base address. A map with either address is undefined on the
other fibre. At 5.2.77 the target is the inner ordinal token, not the outer
कन्. At 5.3.65 it is the inner विनि/मतुप्, not the outer degree suffix.
Replacing a history by a string loses a; retaining a preserves the
domain distinction. No operation is authorized by suffix-name equality
alone. □

This proposition concerns the written maps. It is not a claim that a
runtime implementation of these addresses already exists.

## N4. Dependent-clause and compound propositions

Write \(J(q)\) for the source-authorized clause set of admitted q. The
output carrier is the dependent disjoint union
\(\coprod_{j\in J(q)}(q,j,\operatorname{ops}(q,j))\).

**Proposition.** This carrier excludes cross-paired operations at 5.3.51
and wrong-class compound stipulations at 5.4.77, while preserving distinct
deleted histories with the same readout.

**Proof.** The sixth-of-measure clause in 51 owns कन्; the eighth-of-animal-
part clause owns deletion of a previously selected ञ/अन्. Swapping actions
does not produce an element of J(q). In 77, स्त्रीपुंस has the द्वन्द्व
clause but not the GEN तत्पुरुष clause; द्व्यायुष has the collective द्विगु
clause but not a GEN ownership clause. The different tree-labelled inputs
therefore cannot acquire one another's selected ending. Finally, two
deleted suffix histories occupy different coordinates because their origin
addresses differ, even when their unaccented strings coincide. □

At 5.3.8 the transfer domain additionally carries a proof of selected
तसि from 5.4.44/45. The map changes that token to तसिल् and retains
both rule events. At 5.4.22 the input similarly contains a source collective
selection witness. Neither map can manufacture its prerequisite from a
surface word or an Open input.

## N5. Typed zero-reading theorem

For a legal event \(e:h\to h'\), define
\(U_e(e_ha)=e_{h'}(1+z_e)a\). Different choices have distinct target
histories. Let \(\epsilon:B_{37}\to C_\Sigma\) take the empty-word
coefficient, and let \(\pi_0\) apply it coefficientwise while retaining
every history coordinate. Nonnegative word degree makes ε a unital dagger
homomorphism: a product contributes an empty word only from two empty words.

For a fixed finite family of admitted inputs and clauses of C1, let
\(S_{37,\lambda}\) denote the written selection map. Then

\[
\pi_{0,\mathrm{out}}S_{37,\lambda}
=S_{37,0}\pi_{0,\mathrm{in}},
\qquad
\epsilon\langle x,y\rangle_{B_{37}}
=\langle\pi_0x,\pi_0y\rangle_{C_\Sigma}.
\]

**Proof.** Evidence, clause, ownership and compound-class cuts depend on
retained history and commute with coefficient reading. Every legal event
factor has ε-value one. Multiplicativity/additivity preserve the finite
event compositions and dependent branch sums; dagger compatibility proves
the pairing identity. A unit-start path recovers its declared history
with coefficient one. Open stays Open. Arbitrary signed superpositions
can cancel, so universal support preservation is not asserted. □

The recovered object is exactly the bounded written selection relation,
not complete surface Sanskrit, semantic truth inference or an executed
grammar certificate. The construction gives no physical quantum-gate
performance result and no universal hallucination-free guarantee.
