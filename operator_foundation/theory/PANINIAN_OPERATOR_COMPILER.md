# Pāṇinian operator compiler: native presentation, proof, and formal flow

Monty Dabas | Development edition 0.3 | 26 September 2026

## 0. Source contract

The starting field is the framework's exact cut field, with its already established scalar relation iota^2=-1 and scalar dagger. Objects, typed generators, admissible composition and declared relations are inputs. No ordinary Hilbert space, positive pairing, metric, physical clock or probability measure is a primitive of this construction.

This module connects the Morphic Algebra A-0 generation map and G-0 meta-rule architecture, Morphic Operator Geometry's rewrite/diamond layer, and RKF T58/T60/T61/T77. It does not replace those sources or identify all of their distinct products. In particular, sequential native composition, overlay, rule priority and normalization are not silently one operation. Only the specified sequential cut-linear presentation is compiled here.

The linguistic source engines remain separate. This is a Pāṇinian-inspired symbolic operator compiler using ordered rules, explicit applicability, memory capture and refusal of unresolved choices, not a complete Aṣṭādhyāyī implementation or a re-certification of historical Sanskrit derivations.

## PC1. Typed expressions and admissible rules

Fix finitely many named objects and an ordered finite alphabet of arrows. Every token has a source, a target and a declared integer residue charge. A word is composable only when every recovered middle object matches. A product is written in operator order: the rightmost arrow acts first. There is a distinct empty identity word at each object.

An expression is a finite cut-linear combination of words in one Hom(source,target). Cross-Hom addition and noncomposable products are rejected, rather than silently evaluated on an invented domain. This is a category-algebra presentation, not a claim that every native carrier is finite or linear.

A rule is a named relation w -> f where w is a nonempty word and f is a finite polynomial of the same arrow type. Each nonzero word of f has the same integer charge as w and is strictly smaller than w in degree-lexicographic order. All rules carry an explicit source/contract identifier. The leading coefficient is one; exact field arithmetic handles every other coefficient.

A zero right side declares a zero relation in the specified typed sector. It is not a memory-preserving bijection or a physical erasure operation. Its scope is the declared algebra quotient.

## PC2. Termination and the diamond criterion

**Proposition.** Every reduction of a finite polynomial terminates mathematically when every rule decreases degree-lex order.

**Proof.** Degree-lex on words over a finite ordered alphabet is well-founded and preserved by adding the same contexts on both sides. Replacing a monomial by the contextual right side introduces only smaller words. Recursion on words therefore defines finite reductions. For polynomials use the corresponding well-founded multiset order; collection and cancellation of coefficients cannot introduce a larger word. QED.

A computation still has step and term budgets. Budget exhaustion produces an incomplete result, not a claim that the mathematical reduction does not terminate.

**Theorem.** If every overlap and inclusion ambiguity of the finite rule set admits checked reductions of its two branches to the same polynomial, then every typed finite polynomial has a unique normal form. The irreducible words form a cut-field basis of the quotient by the declared contextual relations.

**Proof.** Define the normal form of a word by induction in degree-lex order. Two possible first reductions are either on disjoint subwords, on overlapping subwords, or one occurrence contains the other. Disjoint reductions commute by substitution and distributivity. Every overlapping or containing pair is a context of a checked critical ambiguity; after its first steps all involved words are smaller than the original word. The induction hypothesis transports the checked equality through those contexts and makes their normal forms equal. Extend the result linearly to finite polynomials. Every reduction changes the expression by a contextual relation, so each expression is congruent to its normal form. Conversely the normal form annihilates every contextual relation, giving uniqueness and linear independence of irreducible words in the quotient. QED.

The implemented audit enumerates both overlaps and inclusions, including distinct rules with the same leading word. It stores and replays the complete reductions of both branches. A nonzero difference between irreducible branches is a witness that this rule presentation is not confluent. A priority policy choosing one branch does not repair the algebraic equality problem.

This is the established Diamond-Lemma/noncommutative-rewriting mechanism, specialized and implemented on the native typed cut presentation. No general priority claim is made for that mathematical method. The native derivation is algebraic; it has no Hilbert-space premise.

## PC3. Derived completion without new axioms

Suppose a checked critical word gives two reduced branches L and R. Their difference d=L-R belongs to the old contextual relation ideal, since both came from the same word. Write d=c w + lower terms with c nonzero and w the greatest word. Add the decreasing rule

    w -> -(lower terms)/c.

This is a derived relation, not a new physical or mathematical axiom. The presented quotient is unchanged. The added rule is accompanied by the original presentation snapshot, critical fork, both replayable derivations and exact coefficient calculation. The completion verifier reconstructs the rule from that data; a newly supplied relation without this derivation is rejected.

The audit is repeated after every added rule. Completion itself need not finish for every finite noncommutative presentation. A declared rule budget bounds the algorithm. It returns COMPLETE only after the new full critical-pair audit passes. A derived nonzero scalar identity would collapse the local unit and is refused as LOCAL_UNIT_COLLAPSE rather than silently turning the user's algebra into the zero algebra.

On the explicit test presentation AB=C and BC=D, ABC initially has irreducible outputs CC and AD. The compiler derives AD=CC from this fork, then verifies all critical pairs of the extended presentation. Rule priority alone did not establish that equality.

## PC4. Proof objects and observational meaning

Every rewrite witness binds the presentation hash, typed input, applied rule, exact coefficient, location and final normal form. Replay checks each substitution and requires an irreducible declared output. It uses no execution of user-provided code and no string eval.

Different original words can have the same normal form in a supplied quotient. Their proof records are retained separately. This is not an assertion that their complete native histories or physical paths were identical. Integer sheet residues are part of the declared signatures and cannot be dropped by a nonzero relation with a different charge.

The operational Lopa lane captures erased markers in an append-only ledger before removing their surface occurrence. It is a generic implementation of the memory-retention discipline used in T58 and T77, not a replacement for the full source grammar. The priority resolver assumes an already supplied finite applicable candidate set; it refuses ties. It makes no Sanskrit-validity or algebraic-confluence claim.

## PC5. Dagger and derivations descend only when relations allow

A candidate dagger sends each token to an expression with reversed source/target and reversed integer charge, conjugates cut coefficients and reverses word order. It descends to the quotient when it squares to identity on generators modulo the relations and sends every defining relation to zero normal form. These conditions make the relation ideal dagger-stable and define an involutive anti-homomorphism of the quotient.

Similarly, assign a same-typed polynomial delta(g) to every generator and extend by

    delta(g1 ... gn) = sum_i g1 ... delta(gi) ... gn.

**Theorem.** This cut-linear free derivation descends to the presented quotient if the derivative of each defining relation has zero normal form.

**Proof.** Leibniz shows that the derivative of a contextual relation u r v is delta(u) r v + u delta(r) v + u r delta(v). Every term lies in the relation ideal when delta(r) does. Linear combinations give stability of the whole ideal. Conversely a descended derivation must annihilate every zero relation. QED.

For the EMK presentation R^2=-I, K^2=I, KR=-RK, the source dagger R^dagger=-R, K^dagger=K passes. The inner derivation delta(X)=[K,X] passes; the arbitrary assignment delta(R)=I, delta(K)=0 fails because it does not preserve R^2=-I. No positive metric is used in this distinction.

## PC6. Solving for unknown operator coefficients

For a confluent presentation, reduce a target T and templates B1,...,Bm into the irreducible word basis. Their coefficients form an exact finite cut-field linear system for

    T = sum_j c_j Bj.

Row reduction returns no solution, a unique solution, or an affine family with nullspace directions. The reconstructed particular solution is independently normalized and its equality witness replayed. Template selection remains an input; a missing direction is not invented.

For [R,K] in the template (I,R,K,RK), the result is (0,0,0,2). Applying the same solver to [K,sum c_j Bj]=0 recovers a two-dimensional commuting space spanned by I and K in this declared EMK algebra.

## PC7. Formal cut-loop calculus with no clock premise

Let J^2=I, JE=EJ, JO=-OJ and G=E+O. The compiler works in formal power series in a central indeterminate t, truncated modulo a supplied power. Factorial coefficients, products and log(I+X) are expanded with exact cut-field arithmetic. This is coefficient algebra; no analytic convergence or interpretation of t as physical time is claimed.

Direct symbolic multiplication and formal logarithm give

    log(J exp(tG) J exp(tG))
       = 2 t E + t^2 [E,O] - (t^3/3) [O,[E,O]] + O_formal(t^4).

Here O_formal(t^4) means equality modulo the ideal (t^4), not a numerical norm estimate. The first two coefficients reproduce the source's T41 algebraic expansion. The cubic coefficient is generated by the same reusable engine. It is a verification/extension in this implementation, not a claim that this known formal-series mechanism is a new law of physics.

For E=0 the formal cut loop is identity to every tested order, consistent with the general cut-odd inverse identity. A separate representation-specific analytic theorem is necessary before converting the formal truncation into an error bound at a measured time or distance.

## PC8. Connection to the existing v0.2 jet module

The v0.2 local module for A(t)=t^2 has a nilpotent continuation N^2=0. The symbolic presentation with relation N N -> 0 reduces every formal exponential to I+tN. The exact matrix backend checks that the already constructed jet action satisfies the relation. Thus the new symbolic frontend consumes the old jet carrier rather than replacing or re-deriving it.

A representation satisfying the relations is not automatically faithful. For the EMK calibration, all irreducible words are I,R,K,RK, and their supplied matrix images are linearly independent, which establishes faithfulness for that finite presentation. The backend reports only relation compatibility and image rank unless a spanning-basis argument is also supplied.

## Scope and external method references

This is a working compiler for finite typed monic presentations with a decreasing rule order. It is not an unrestricted natural-language theorem prover, a complete Sanskrit grammar, a promise that completion always terminates, or an automatic operator selector for nature. Historical analytic and physical adapters keep their hypotheses. Source manuscript files are preserved and are not wholesale re-certified by this implementation.

Method lineage: George M. Bergman, The Diamond Lemma for Ring Theory, Advances in Mathematics 29 (1978), 178-218; the author's corrections/history page at math.berkeley.edu/~gbergman/papers/updates/diamond.html also credits the earlier Shirshov/Bokut line. Vladimir Dotsenko and Pedro Tamaroff, Tangent complexes and the Diamond Lemma, arXiv:2010.14792, provides a later research treatment. These are method references, not primitive-space assumptions.
