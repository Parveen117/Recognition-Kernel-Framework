# Recognition Kernel Operator Workbench

**Canonical repository:** `Parveen117/Recognition-Kernel-Framework`  
**Canonical branch:** `main`  
**Canonical working folder:** `operator_foundation/`  
**Version:** 0.5, 26 September 2026  
**Author:** Monty Dabas

This is the single active home of the operator engine developed in this conversation. Native cut arithmetic, residue paths, Laurent/jet algebra, the Pāṇinian symbolic frontend, automatic regular models, proofs, jobs and tests live together. No MP checkout, Publications checkout, database, network service or package installation is required to run the engine or replay the included jobs.

The historical MP/RH/Publication source names in provenance records are attribution, not runtime imports. Existing source manuscripts are not erased or wholesale re-certified. Unpublished private/patent snapshots are not included in this public migration. This is a consolidation of the developed operator engine and its public framework references, not a claim that every branch of every application repository has been migrated.

## Run without installing dependencies

Tested environment: Node v22.16.0, using only built-in modules and exact BigInt rational cut pairs.

```text
node verify_all.cjs --check
node cli.cjs solve examples/emk_job.json emk-result.json
node cli.cjs replay emk-result.json EXPECTED_INPUT_SHA256
```

The first command runs all five exact regression suites plus the mathematical mutation controls and checks the master source/output pin. The supplied example's trusted input hash is recorded in `audit/EXAMPLE_INPUTS.json`. Replay deliberately requires that expected hash; it does not trust a replacement input inside an arbitrary packet. Output-file creation refuses to overwrite an existing file.

A second complete example, `examples/jet_job.json`, constructs the three-level nilpotent algebra and recovers its inverse and future-observation repair. `examples/infinite_job.json` deliberately demonstrates an infinite irreducible language instead of pretending that a finite-depth search found a complete finite algebra.

## Mathematical reading order

1. `theory/NATIVE_PRIMITIVE_ORDER.md`: native objects before representations.
2. `theory/01_NATIVE_ALGEBRA.md`: algebra versus state observation, ideals, minimal repair and compression memory.
3. `theory/02_COMPLETION_AND_MEMORY.md`: a specified mass completion, resolvents, memory and conditional representations.
4. `theory/NATIVE_LAURENT_JET_REPAIR.md`: formal principal packets, jet modules and retained sheet memory.
5. `theory/PANINIAN_OPERATOR_COMPILER.md`: typed rewriting, checked diamonds, proof replay and formal flow.
6. `theory/AUTOMATIC_REGULAR_MODEL.md`: automatic complete bases, faithful regular action, center/inverse solvers and job contracts.
7. `theory/WEIGHTED_OPERATOR_COMPLETION.md`: infinite normal-word completion, inverse and functional-calculus bounds, source-preserving elimination and nonlinear recognition equations.

`SOURCE_INDEX.md` links the public Morphic/EMK/Pāṇinian source archive stored in this same repository. The operative proofs above are included in the standalone ZIP as well. Historical identifiers and prior counts are not substitutes for the current master verification result.

## Native foundation order

Typed cuts, cut scalars, derived iota, admissible composition, declared residue and target come first. The new symbolic and regular-module constructions require no primitive Hilbert space or positive metric. A native pairing or representation is used only under its own declared result. In particular the automatically constructed regular action is algebra-faithful, but its coordinate transpose is **not automatically the native dagger**.

An exact finite result proves the specified computation. Written general arguments, proof-assistant verification, source integrity and physical measurement remain distinct evidence classes. No physical clock, universal gravitational coupling or solved open conjecture is asserted by this package.

## Current capabilities

The common arithmetic core implements exact cut scalars, matrices, ranks, inverses and finite action/observer calculations. The symbolic frontend normalizes typed operator polynomials and records replayable derivations; it audits critical pairs, performs bounded derived completion and solves coefficient templates. The Laurent/jet backend constructs finite local modules while retaining integer sheet memory separately.

The new workbench discovers the complete irreducible-word basis when finite, or produces a repeatable infinite-language witness. It then derives the faithful left regular action and solves centers, centralizers, inverses and future-observer repair without a supplied matrix representation. Allocation exhaustion is not confused with mathematical infinitude or nonexistence.

## Mathematics development 0.5

The new WC1-WC7 chapter derives a complete weighted native algebra directly from checked rewrite relations. An infinite irreducible-word language is now usable when the finite weight contract holds; it is not replaced by an arbitrarily truncated matrix. Native dagger extension, convergent series, two-sided inverse certificates, ordered response derivatives, source-preserving Schur elimination and nonlinear fixed points share that completion.

Run the infinite noncommutative example and the new tests:

```text
node examples/weighted_completion_demo.cjs
node tests/verify_weighted.cjs --check
```

The example certifies an inverse of `I-(X+Y)/4` with `YX=(1/2)XY`. Its 45 retained monomials approximate an infinite element, with explicit rational tail bounds. `core/weighted_completion.cjs` also certifies block-source responses and unique fixed points in a specified ball for noncommuting quadratic maps. All gates are sufficient contracts, not universal nonexistence tests.

See `MATHEMATICAL_PROGRAMME.md` for the next proof obligations. The old finite JSON CLI is unchanged; the new infinite-completion API and demonstration are separate from that finite-job schema. No new physical model is selected by these mathematical constructions.

## Canonical-source policy

New shared engine work goes here. Earlier RKF research branches and MP PR #282 are historical development snapshots, not parallel active releases. Publications provides a pointer to this home rather than another code copy. `CANONICAL_HOME.json` identifies the authority and scope. The `audit/history` directory retains prior evidence for traceability; only the current master pin controls this release.

The same-repository `sources/rkf_reference` Git tree preserves the corrected public RKF source snapshot. It is read-only provenance, not a second editable engine. Private historical source trees were deliberately excluded. The standalone companion contains the complete executable engine and operative proofs, while that optional historical manuscript archive is in the canonical repository.

## Verification limits

No historical Python scientific suite, full Lean build or physical experiment was rerun in this migration. Python 3.11/3.12 settings were not changed; the available system Python was used only for file packaging, never to claim scientific regression success. The root mathematics-navigation test is documented separately when its requested Python runtime is unavailable. No GitHub Actions PASS is asserted merely because local tests pass.
