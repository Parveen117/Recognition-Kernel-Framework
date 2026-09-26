# Recognition Kernel Framework

Author: Monty Dabas

## Canonical operator development

The single active operator-engine source is [operator_foundation/](operator_foundation/README.md), on this repository's `main` branch. Version 0.4 combines the native cut-field core, residue paths, Laurent/jet backend, Pāṇinian symbolic compiler, automatic faithful regular models, proofs, jobs and verification. No other repository checkout is required for this engine.

```text
cd operator_foundation
node verify_all.cjs --check
node cli.cjs solve examples/emk_job.json emk-result.json
```

The engine's [canonical-home contract](operator_foundation/CANONICAL_HOME.json), [operative theory](operator_foundation/theory/AUTOMATIC_REGULAR_MODEL.md), [source map](operator_foundation/SOURCE_INDEX.md), and [master evidence](operator_foundation/audit/MASTER_CERTIFICATE.json) specify its scope. Previous MP/RKF development branches are historical snapshots, not parallel active homes.

Native cuts, cut scalars, typed operations and retained residue come before any representation. An ordinary Hilbert space, a metric or physical time is not a primitive premise of the symbolic or regular-module construction. Representation-specific theorems retain their own hypotheses.

## Framework mathematics and provenance

Start with the [current mathematics index](MATHEMATICS_INDEX.md). The complete earlier subject/theorem register is preserved byte-for-byte in [the framework index archive](MATHEMATICS_INDEX_2026_09_16.md). The prior framework overview is preserved in [README_FRAMEWORK.md](README_FRAMEWORK.md). Existing theorem and paper source paths remain intact.

The corrected public reference tree, including the Morphic Algebra and Morphic Operator Geometry LaTeX and the Pāṇinian theorem line, is retained in `operator_foundation/sources/rkf_reference`. It is read-only provenance. Historical source inclusion does not upgrade a conditional claim to a theorem. Private historical research/patent source trees are not included.

Local execution covered 498 named exact finite checks and 10 mathematical mutation controls. This is not proof-assistant verification, a rerun of every historical scientific suite, or physical quantum-gravity identification. See [migration and validation limits](OPERATOR_MIGRATION_2026_09_26.md).
