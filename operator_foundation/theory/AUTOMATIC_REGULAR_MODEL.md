# Automatic native normal basis and faithful regular action

Monty Dabas | Operator Workbench 0.4 | 26 September 2026

## Scope and source order

The input is the cut-field presentation described in `PANINIAN_OPERATOR_COMPILER.md`: finitely many typed generators, strictly degree-lex decreasing monic relations, and a complete checked overlap/inclusion audit. The automatic finite-dimensional backend in this edition handles one object. The symbolic frontend still handles multiple object types; an unsupported backend is reported rather than flattening their identities.

The native field, object signatures, composition and admitted relations come first. No ordinary Hilbert space, physical clock, metric, positive pairing, or preferred finite matrix realization is an input. Matrices below are output coordinates of a proved finite free-module construction. Algebraic faithfulness is not a physical validation or automatic preservation of a native dagger as conjugate transpose.

## WB1. A complete basis test, not a depth guess

Let F be the finite set of left-hand words of the admitted rules. A word is irreducible precisely when it contains no element of F as a contiguous subword. Construct a finite automaton whose states are the proper prefixes of words in F, including the empty prefix. After appending a generator, reject a transition if a forbidden word has just been completed; otherwise retain the longest suffix that is a proper prefix. Restrict to states reachable from the empty prefix. Every retained state is accepting.

**Lemma.** This automaton accepts exactly the irreducible words.

**Proof.** Induct on word length. The maintained suffix contains exactly the information needed to detect the next forbidden suffix. Any newly appearing forbidden subword ends at the appended generator. The longest matching prefix suffix retains all shorter potential prefix suffixes as its own suffixes. Previously forbidden substrings were already rejected. QED.

**Theorem.** The irreducible language is infinite if and only if the reachable accepting-transition graph has a directed cycle.

**Proof.** A path reaching a cycle can repeat its nonempty cycle label arbitrarily often, giving arbitrarily long accepted words. Conversely a sufficiently long accepted path in a finite graph repeats a state and hence contains a reachable cycle. With no cycle, the graph is finite and acyclic and every accepted path has bounded length. QED.

In the acyclic case, set c(v)=1+sum c(w), summed over all labelled outgoing edges v->w. The 1 counts stopping at v. Reverse-topological evaluation gives exactly c(start) irreducible words. The count uses integers without floating-point rounding. Exceeding the requested allocation budget reports a finite dimension with `FINITE_BASIS_BUDGET_EXHAUSTED`; it does not report an infinite algebra. Automaton-resource exhaustion is a third, separate outcome.

The checked diamond theorem in the local compiler document then makes these irreducible words a basis of the presented quotient. A finite word search alone would not establish this conclusion: confluence plus exhaustive language analysis is required. Nonconfluent presentations are rejected before a quotient basis is certified.

## WB2. Constructing a faithful action from the basis

Let b_0=1,b_1,...,b_(d-1) be the resulting complete basis. For every generator g, define a d-by-d coordinate matrix by

    (L_g)_(i,j) = coefficient of b_i in NF(g b_j).

For an arbitrary presented element a define L_a the same way. This construction is cut-linear.

**Theorem.** L_(ab)=L_a L_b, L_1=I, and L_a=0 implies a=0.

**Proof.** On each basis vector b_j, associativity and the unique quotient normal form give NF((ab)b_j)=NF(a NF(b b_j)). This is the matrix product identity. The identity statement is immediate. Finally L_a applied to the coordinate vector of b_0 is exactly the coordinate vector of a. If L_a=0, every coefficient of a is zero. QED.

This gives a **faithful algebra representation** without guessing a physical state space or an external matrix model. The implementation checks the defining relations on the constructed action and checks the identity-column witness for every basis element. Independent finite tests additionally verify every basis-pair multiplication on the EMK example.

**Dagger warning.** If the quotient has an admitted algebraic dagger, it need not become coordinate conjugate transpose in this basis. For example K[N]/(N^2) admits the algebraic rule N^dagger=N. Left multiplication by N on (1,N) is a nonzero nilpotent lower shift, not a self-adjoint matrix for the ordinary Euclidean pairing. A compatible positive native pairing is a separate hypothesis, and cannot be inferred here. This example does not discard the framework's derived-pairing results; it prevents applying them where their premises were never supplied.

## WB3. Solving equations and commuting sectors

Once the complete basis is known, any finite operator equation linear in unknown scalar coefficients becomes an exact cut-field system. In particular, for supplied T_1,...,T_m, write X=sum_j x_j b_j and expand each [T_i,X]. The common nullspace of all coefficient rows is the full centralizer in this declared finite algebra. Taking T_i to be all generators gives the center. Every reconstructed nullspace direction is independently normalized and its equality proof replayed.

To find an inverse of a, solve aX=1 in the same complete basis. If there is no solution, a is not invertible in this algebra. If a solution is found, both aX=1 and Xa=1 are explicitly replayed. Failure to allocate a complete basis is never converted to `NOT_INVERTIBLE`.

For the EMK relations R^2=-1, K^2=1, KR=-RK, the computed results are:

    complete basis        1,R,K,RK
    center                span(1)
    centralizer of K      span(1,K)
    inverse of 1+R        (1-R)/2
    inverse of 1+K        does not exist in this algebra

For the declared three-level jet algebra N^3=0, the complete basis is 1,N,N^2 and (1-N)^-1=1+N+N^2. The program generates the basis; these lists are not passed as assumed bases to the solver.

## WB4. Future-complete observation on the regular carrier

On the constructed regular module, supply a linear observer C and an optional target L. Starting from W_0=row(C)+row(L), close under the declared generator actions on the right:

    W_(k+1)=W_k+sum_g W_k L_g.

This is the existing target-faithfulness/minimal-refinement theorem already written in `01_NATIVE_ALGEBRA.md` and used in the jet compiler. The present development supplies its carrier automatically. Stabilization gives the minimum future-complete readout rank. Extra channels are measured against rank(C), not against rank([C;L]). An observer of the identity coefficient on the EMK regular carrier needs three extra cut-complex channels. This is a four-coordinate regular module, not the older two-coordinate state calibration.

The action catalogue here contains the specified generators only. Native dagger closure is not requested by silently adjoining their coordinate transposes. An invariant partial observer can remain genuinely lossy if that is sufficient for the supplied target.

## WB5. Portable task and replay contracts

A JSON job fixes its presentation, budgets and tasks. The engine emits its original input, input SHA-256, exact basis/automaton, critical-pair witnesses, derived regular matrices and task results. Replay requires an **externally expected input hash** and re-executes the declared job. Checking only a hash supplied inside the same untrusted result would allow substitution of the problem itself; that is deliberately refused.

Recomputation uses the same audited implementation and is not an independent proof assistant. Finite tests compare the regular action against the symbolic multiplication, plant false dimensions/inverses and changed input jobs, and run CLI solve and replay in different processes. The whole companion is also tested from an isolated directory with network modules and fetch disabled.

## What is new in this implementation

Version 0.3 needed a supplied template/basis to interpret an image rank as faithfulness. Version 0.4 proves finite-basis completeness using the rule-language automaton, constructs a faithful regular action from it, and supplies end-to-end JSON solve/replay and a single-source verification command. The normal-form, automaton, regular-action and linear-elimination mechanisms are established mathematics, not claimed as new universal laws. Method lineage includes the Diamond-Lemma/Shirshov-Bokut family discussed in the compiler document; Bergman's own corrections page is https://math.berkeley.edu/~gbergman/papers/updates/diamond.html.

Not established: unrestricted completion termination; a finite backend for every typed category; arbitrary unbounded-operator domains; a canonical physical source, metric or detector; quantum gravity; superiority to every other operator tool. Those are not needed to execute the finite jobs specified here.
