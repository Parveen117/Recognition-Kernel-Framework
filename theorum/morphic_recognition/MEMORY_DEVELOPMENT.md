# Morphic Memory Development — first certified scope

This package develops the state/memory/transformation proposal as four precisely
scoped theorem capsules. The mathematical proof, finite executable evidence,
formal status, provenance, and external review are separate axes. The capsule
proofs apply under their hypotheses; the certificate checks its listed finite
instances and negative controls.

## Reading order

| ID | Capsule | Question answered |
|---|---|---|
| MR-04 | [Future-complete linear Recognition](04_future_complete_linear_recognition.md) | Which linear distinctions must survive every allowed future action? |
| MR-05 | [Seam memory gluing](05_seam_memory_gluing.md) | When does memory transfer across typed regimes, and how much additional memory is required? |
| MR-06 | [Guarded Lopa future equivalence](06_guarded_lopa_future_equivalence.md) | Which deletions preserve both future outputs and future rule availability? |
| MR-07 | [Holonomy area scaling](07_holonomy_area_scaling.md) | How must small commutator loops be scaled to have a nontrivial continuous limit? |

MR-04/05 concern total linear maps on declared finite-dimensional carriers.
MR-06 separately concerns finite deterministic partial rules and counts
behavioral classes, not scalar linear coordinates. MR-07 is a finite-matrix
norm theorem with a stated remainder bound. None silently identifies those
different carriers.

## Evidence register

The final run evidence and review findings are recorded in
`MEMORY_VERIFICATION.md` and `DEVELOPMENT_REVIEW.md`. Source hashes and exact
obligation IDs are frozen in `MEMORY_SOURCE_MANIFEST.json`; reproducible finite
results are in `MEMORY_CERTIFICATE.json`.

All four capsules contain ordinary mathematical proofs. No proof-assistant
formalization or external peer review is claimed. Internal AI review is an
adversarial development check and is not external validation. A certificate
hash binds evidence to content; a hash itself is not a mathematical proof.

## Native development and established interfaces

The development consumes [MR-02](02_path_blindness_minimal_memory_repair.md)
and [T61](../61_rewrite_rules_as_cut_module_operators_theorem.md). Recognition
defines the declared target, Smriti retains future-relevant distinctions, and
Lopa is lawful only under the applicable capsule's preservation conditions.
The explicit matrix and finite-rule carriers supply the representation bridge.

Future-equivalence quotients, row-space realization, and matrix product limits
have established mathematical antecedents. In particular, compare Stefan
Kiefer's [Notes on Equivalence and Minimization of Weighted Automata](https://arxiv.org/abs/2009.01217).
This package makes those finite interfaces explicit within the native theorem
spine and provides checkable contracts; it does not establish historical
priority or claim a new universal foundation from familiar identities.

## What remains open

1. Gluing smooth local quotients through arbitrary singular strata. Finite
   typed graph closure is not a theorem about unrestricted smooth spaces.
2. Nonlinear or infinite-dimensional minimum memory and computable closure.
3. Robust reconstruction and error bounds under noisy physical observations.
4. A thermodynamic TVSP adapter with declared state variables, units,
   constitutive relations, and measured history dependence.
5. A theorem relating memory dimension to geometric curvature. They are
   different quantities here and are not declared equal.
6. Whole-manuscript repair/formalization and external assessment of novelty.

Differential rank loss alone does not establish exact blindness: for example,
the injective map x -> x^3 has zero derivative at zero. Smooth jets alone also
need not determine a function. Those obstructions must be addressed before
extending the present finite package to a singular geometry.

## Reproduce on Python 3.12

From the repository root:

```bash
python3.12 -m unittest -v proof_lab.test_morphic_memory proof_lab.test_guarded_lopa proof_lab.test_holonomy_scaling proof_lab.test_memory_certificate proof_lab.test_mathematics_index
python3.12 -m proof_lab.morphic_recognition.certify_memory --check-archive
```

No third-party dependency, simulation campaign, hardware run, or LaTeX build
is required for this package. Source changes make the archived certificate
stale; review the changes before deliberately issuing new source pins.
