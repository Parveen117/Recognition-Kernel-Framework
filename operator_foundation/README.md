# Recognition Kernel: canonical operator foundation

Monty Dabas | Working development edition 0.1 | 26 September 2026

This folder consolidates the **corrected native RKF corpus**, a focused operator-theory audit, new written algebra/completion bridges, and an independently executable exact finite kernel. It is not a declaration that all mathematics or all physical applications have been completed.

## Read in this order

1. `audit/DEVELOPMENT_AUDIT.md`: what is present, what is conditional, and what remains unbuilt.
2. `theory/01_NATIVE_ALGEBRA.md`: native field -> path algebra -> generated operator algebra -> state/module observation -> genuine algebra quotient -> compression memory.
3. `theory/02_COMPLETION_AND_MEMORY.md`: a concrete native mass completion, local resolvents, exact dynamical memory, stable observer completion, and an optional positive representation.
4. `core/native_operator.cjs` and `tests/verify.cjs`: exact arithmetic and finite regression controls.
5. `sources/rkf-2026-09-25/`: the actual unchanged corrected RKF snapshot, including its original mathematical index, manuscripts, theorem files, proof lab, certificates and other root contents.

The snapshot is copied as a Git tree, **not a submodule or a link-only list**. It is pinned to RKF commit `927cdb6ca98221c0b4285da953a2c8b689fb202c`, tree `1e6758a4b6d246403a3754e608d635e9ed9cb389`. Its historical source statuses remain historical statuses. Snapshot inclusion does not re-certify every statement, and executable programs in the snapshot keep their original dependencies and paths.

## One canonical development surface

New shared operator work goes in this folder. The source snapshot is read-only provenance. Existing root theorem files are preserved, so old references, certificate hashes and papers do not silently change. The public native mathematical language remains primary: a matrix, normed-space, Hilbert, or physical interpretation needs a declared representation contract.

Do not use the old `main` version of T50 as the current tensor-mass statement. The selected correction branch proves an inequality and retains the uniform gap; the strict mixed-phase counterexample is reproduced by the new independent core.

## New common interfaces

- `operatorAlgebra(generators)`: exact finite word-algebra saturation; optional dagger closure is enabled by default.
- `rowClosure(seed, generators)`: minimum future-complete module observation for a declared row seed. To include a target, stack its rows with C before calling. The function's `extra` is measured from that whole seed; total extra channels relative to C are final rank minus rank(C).
- `idealReadoutClosureFullMatrix(seed, generators)`: two-sided dagger repair on a **verified full matrix algebra**, with non-full generated algebras rejected.
- `descendedAction`, `resolvent`, `neumann`, native mass, energy, Cayley, dagger, and exact field operations.

Inputs to the finite core are integers or rational strings. A scalar `[a,b]` means `a+iota*b`. Floating-point field inputs are rejected. The implementation uses Node's built-in BigInt; it has no package dependencies.

## Reproduce the new evidence

From this folder:

```text
node tests/verify.cjs --check
```

This executes 122 named exact checks, including a 625-product exhaustive scalar grid. It compares fresh results and source hashes to `audit/FINITE_CERTIFICATE.json` and `audit/EXPECTED.sha256`. The read-only check never repairs a mismatching pin. An intentional reviewed evidence revision uses `--write`.

No new workflow was added, no full scientific benchmark was scheduled, and no remote-CI pass is asserted. The existing Python scientific suites were not rerun in this development pass. Their supported 3.11/3.12 execution requirements remain unchanged.

## Consolidation boundary

The **full corrected RKF tree** is physically included in the GitHub folder. Publications' live U/QG development, the RSC release repository and thermodynamic experimental repository were inspected as external related sources and are recorded in `audit/SOURCE_REGISTER.json`; their complete repositories were not copied in this pass. Private research and patent repositories were not exported into this public tree.

The downloadable companion ZIP contains the newly written core, proofs, audit and finite evidence, not the historical Git-tree snapshot. The GitHub canonical folder contains that snapshot.

## Immediate research direction

Use one source-selected operator family and one target through the same sequence:

    native algebra -> observation/ideal gate -> memory -> resolvent
    -> completion and decoder bound -> physical adapter -> held-out data.

The chi-to-EMK-two-jet map from QG v1.8 stays an explicitly declared constitutive adapter. It is not a native algebra axiom. The scalar chi is blind to common response amplitude and does not select a global warp. A gravity application must bring source amplitude, physical scale, propagation and probe coupling into the same tested operator contract.
