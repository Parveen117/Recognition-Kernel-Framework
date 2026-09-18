# Morphic Recognition Theorem Spine

This folder is the canonical development surface for morphism-first, clock-free recognition theorems derived from the Recognition-Seam / morphic programme.

The order is deliberately theorem-first:

```text
source manuscripts and existing RSC theorems
-> exact mathematical statement
-> proof with declared assumptions
-> RNKE proof-obligation manifest
-> exact executable negative controls / calibration
-> only then domain adapters such as AI actions or Proof of Work.
```

No application is allowed to upgrade a theorem's status merely because the application works.

## Current theorem chain

1. `01_typed_residue_non_cancellation.md`
   - global closure as a typed direct-sum residual;
   - exact criterion for when an aggregate/score is faithful;
   - explicit hidden-residual witness for lossy aggregation.

2. `02_path_blindness_minimal_memory_repair.md`
   - endpoint/path target faithfulness criterion;
   - path-blind quotient;
   - exact minimum number of scalar memory channels needed to repair endpoint blindness;
   - presented as a path-space specialization/extension of the existing minimal-observer theorem.

3. `03_cocycle_lifted_path_recognition.md`
   - clock-free abelian memory lift of a morphism category;
   - associativity iff the memory defect obeys the cocycle law;
   - same projected morphism can retain distinct lawful memory;
   - path memory is independent of parenthesization.

## Future memory development: MR-04–MR-07

The [first memory development package](MEMORY_DEVELOPMENT.md) adds:

4. [Future-complete linear Recognition](04_future_complete_linear_recognition.md):
   finite future-row closure, induced updates, and minimum linear memory.
5. [Seam memory gluing](05_seam_memory_gluing.md): finite typed graph closure,
   local factorization, exact repair rank, and backward memory propagation.
6. [Guarded Lopa future equivalence](06_guarded_lopa_future_equivalence.md):
   finite partial-rule quotients preserving outputs and rule availability.
7. [Holonomy area scaling](07_holonomy_area_scaling.md): a finite-matrix
   correction with explicit remainder bounds and exact shear calibration.

Use [MEMORY_VERIFICATION.md](MEMORY_VERIFICATION.md) for actual run evidence
and [MEMORY_CERTIFICATE.json](MEMORY_CERTIFICATE.json) for the source-pinned
finite obligations. The earlier MR-01–03 verifier remains a separate package.

## Proof-status discipline (all capsules)

Each theorem has two separate evidence layers:

```text
GENERAL PROOF
    ordinary mathematical proof under explicit assumptions

RNKE PROOF CONTRACT
    assumptions, dependencies, proof obligations, negative controls,
    and executable calibration checked fail-closed.
```

A passing executable calibration is **not** called a proof of the universal theorem. It verifies the declared proof contract and catches implementation/statement mismatches. A formal proof-assistant certificate would be a stronger additional layer and is not silently claimed here.

## Dependencies inside Recognition-Kernel-Framework

The present spine consumes, rather than duplicates:

- `../24_clock_free_recognition_seam_cut_calculus.md`;
- `../27_rsc_primitive_to_completion_hierarchy.md`;
- `../31_cut_variational_minimal_observer_theorem.md`;
- `../32_cut_covariance_event_realization_theorem.md`.

The new contribution is the explicit theorem chain from typed non-cancellation to path blindness to lawful path-memory lifting.

## Domain boundary

The theorem files contain no AI, blockchain, RH, physics, or device assumptions. Those are later adapters.

The intended downstream map is:

```text
morphism recognition theorem
        |
        +-- mathematical proof transition
        +-- AI action transition
        +-- work-bearing blockchain transition
        +-- ledger/provenance transition
```

The application inherits the theorem obligations; it does not redefine them.
