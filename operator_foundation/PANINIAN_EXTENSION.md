> Rehomed 26 September 2026: this document records its original v0.2/v0.3 scope. The active repository and migration scope are defined by README.md and CANONICAL_HOME.json in this package. Historical private snapshots are not exported.

# Native operator foundation v0.3: Pāṇinian symbolic frontend

Monty Dabas | 26 September 2026 | Additive private development on v0.2

The existing v0.2 files and certificate remain unchanged. This extension adds a typed symbolic operator frontend, a Publications/Morphic source audit, exact proof replay and a separate certificate. Its native inputs are cut scalars, typed composition, declared relations and retained residue information. No ordinary Hilbert space is a primitive premise.

## Source reading

Start with `audit/PUBLICATIONS_MORPHIC_AUDIT.md` and `audit/PANINIAN_SOURCE_REGISTER.json`. Publications contains actual operator-related LaTeX, including the T41 generator manuscript and collected-volume fragments. The complete named Morphic Algebra and Morphic Operator Geometry manuscripts examined here are in the corrected RKF source tree; the public book assembler omits those nested manuscript directories. The audit distinguishes inspected text, file/branch inventories, inherited source results and new development.

## Run

From `operator_foundation_native`:

```text
node tests/verify.cjs --check
node tests/verify_paninian.cjs --check
node tests/mutate_paninian.cjs
node examples/paninian_demo.cjs
```

The first command preserves and verifies the v0.2 certificate. The second regenerates the new symbolic results and compares source hashes and certificate bytes without changing them. An intentional reviewed revision uses `--write`. The mutation runner uses temporary copies and does not change the original sources or pins.

No package installation is needed. Node's built-in BigInt supports exact rational cut pairs. Every operator coefficient is an integer, rational string, or native Cut value; approximate floating-point coefficients are rejected.

## Available operations

`Presentation` constructs a typed finite rule presentation. `reduce(...,{witness:true})` returns a normal expression and a replayable proof. `audit()` checks every finite overlap/inclusion ambiguity. `complete()` adds only explicitly derived critical-pair rules within a declared budget. `replayCompletion()` verifies those derivations.

`proveEquality()` separates equality, distinct normal forms in the declared quotient, and an uncertified presentation. `solveCoefficients()` finds exact operator-template coefficients, including affine solution families. Dagger and derivation gates verify that the chosen transformations preserve relations. Formal exponential/logarithm tools compute bounded-depth series without analytic or clock assumptions.

The operational priority/Lopa helpers are deliberately separate: selecting a rule by priority is not an algebraic equality proof; erasing a surface marker does not erase its stored derivation feature.

## Demonstrated outputs

- R^2=-I, K^2=I, KR=-RK: four checked ambiguities and normal basis I,R,K,RK.
- KRKR=I with a replayable derivation.
- [R,K]=2RK, solved as unknown coefficients in a declared four-element template.
- The commuting subspace of K in that EMK algebra is span(I,K).
- A nonconfluent two-rule fixture is repaired by a new relation derived from its own critical fork, not by a new axiom.
- A formal cut-loop calculation reproduces T41's first two coefficients and computes its cubic coefficient without a matrix or Hilbert-space premise.
- The existing v0.2 nilpotent jet action is a checked backend for the symbolic relation N^2=0.

The finite tests and replay machinery are not proof-assistant verification of the implementation. The general confluence and descent arguments, assumptions and method lineage are written in `theory/PANINIAN_OPERATOR_COMPILER.md`.

## Limits and preservation

This is a Pāṇinian-inspired operator compiler, not the whole Aṣṭādhyāyī engine. It consumes the source's precedence/feature/ledger discipline while leaving linguistic validity to its own source-specific programme. It does not assert an unrestricted completion algorithm, universal physical model, or superiority to every existing theorem prover.

Original LaTeX, historical theorem ledgers, source branches and physical adapters are unchanged. Selected sources are registered by immutable commit/blob and exact reviewed ranges; they are not all copied into this companion. No private source text is exported into the public Publications or RKF repositories. The existing private integration folder remains the development location.
