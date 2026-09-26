# Recognition Kernel Framework

Author: Monty Dabas

## Canonical operator development

The single active operator-engine source is [operator_foundation/](operator_foundation/README.md), on this repository's `main` branch. Version 0.5 combines the native cut-field core, residue paths, Laurent/jet backend, Pāṇinian symbolic compiler, automatic faithful regular models, weighted infinite completion, proofs, jobs and verification. No other repository checkout is required for this engine.

```text
cd operator_foundation
node verify_all.cjs --check
node cli.cjs solve examples/emk_job.json emk-result.json
node examples/weighted_completion_demo.cjs
```

The engine's [canonical-home contract](operator_foundation/CANONICAL_HOME.json), [regular-action theory](operator_foundation/theory/AUTOMATIC_REGULAR_MODEL.md), [weighted completion and response calculus](operator_foundation/theory/WEIGHTED_OPERATOR_COMPLETION.md), [source map](operator_foundation/SOURCE_INDEX.md), and [master evidence](operator_foundation/audit/MASTER_CERTIFICATE.json) specify its scope. Previous MP/RKF development branches are historical snapshots, not parallel active homes.

The new WC1-WC7 chapter constructs a class of infinite normal-word algebras from finite weighted rewrite contracts. It proves convergent functional calculus, two-sided inverse and perturbation bounds, source-preserving hidden-sector elimination, certified response errors, and nonlinear fixed-point existence and uniqueness in an explicit ball. These statements require their declared presentation, weight and bound hypotheses. The [mathematical programme](operator_foundation/MATHEMATICAL_PROGRAMME.md) records the next integration obligations.

Native cuts, cut scalars, typed operations and retained residue come before any representation. An ordinary Hilbert space, a metric or physical time is not a primitive premise of the symbolic, regular-module or weighted-completion constructions. Representation-specific theorems retain their own hypotheses.

## Framework mathematics and provenance

Start with the [current mathematics index](MATHEMATICS_INDEX.md). The complete earlier subject/theorem register is preserved byte-for-byte in [the framework index archive](MATHEMATICS_INDEX_2026_09_16.md). The prior framework overview is preserved in [README_FRAMEWORK.md](README_FRAMEWORK.md). Existing theorem and paper source paths remain intact.

The corrected public reference tree, including the Morphic Algebra and Morphic Operator Geometry LaTeX and the Pāṇinian theorem line, is retained in `operator_foundation/sources/rkf_reference`. It is read-only provenance. Historical source inclusion does not upgrade a conditional claim to a theorem. Private historical research/patent source trees are not included.

Local execution covered 557 named exact finite checks and 13 mathematical mutation controls. This is not proof-assistant verification, a rerun of every historical scientific suite, or physical quantum-gravity identification. See the [0.5 development validation](operator_foundation/audit/DEVELOPMENT_V0_5.md) and [original migration limits](OPERATOR_MIGRATION_2026_09_26.md). The requested Python 3.11/3.12 navigation suite was not executed because that runtime was unavailable.
