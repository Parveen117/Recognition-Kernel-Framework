# Source and Development Index

This file maps the theorem capsules to their source PRs or native development branches. It is a provenance guide, not a substitute for the theorem statements, proof notes, certificates, or claim boundaries.

## Initial MP transfer

| Theorum capsule | MP PRs | Main source claim |
|---|---:|---|
| `01_positive_eta_path_independence.md` | 246 | actual eta-normalization rectangle and exact positive-eta family path independence |
| `02_seam_integer_single_sector_reduction.md` | 235, 242, 247, 255, 277 | seam integer, common five-matrix covariance, single-sector terminal focus |
| `03_m3_positive_accepted_block.md` | 181, 182, 196, 198, 199, 200, 202 | exact native `b3` signs, target-local `M3` positivity, positive accepted odd block |
| `04_zero_cut_t03_endpoint_completion.md` | 254, 256 | zero-cut quotient, five-label lift, source-Gram identity, projection-defect positivity |
| `05_transfer_boundary_and_next_gate.md` | all above | prevents reopening certified upstream theorems and records the next lawful gate |

Source branches named in that material include:

```text
agent/rh-rotation-metric-topology-reset
agent/native-x3-fixed-state-primal-spectral-transfer
agent/native-x3-parity-feshbach-complement-reduction
agent/native-seam-scale-convergence
agent/rh-journal-final-conditional-zero-closure
agent/rh-paper-single-sector-seam-closure
agent/t20-native-odd-single-sector-closure
```

The machine-readable `provenance.json` records this original `01`–`05` transfer. It is intentionally scoped to that packet and is not a complete history of later native theorem development.

## Native cut and completion chain

Files `21` through `40` were developed natively in this repository after the first transfer. Their exact dependencies, source pins, imported membranes, and status labels are stated inside each capsule and in the Git history.

The chain includes:

```text
cut-memory spectral isomorphism;
memory-cut rank gate;
native cut-generated object theorem;
clock-free recognition seam cut calculus;
primitive-to-completion hierarchy;
finite-to-infinite recognition completion;
minimal observer and covariance realization;
native source, decoder and boundary adapters;
strict odd source-kernel no-blindness;
odd/native classical-normalization interface.
```

No blanket claim is made that every file in this range has the same evidence status.

## Advanced native development branches

Before repository consolidation, the advanced theorem capsules were carried by the following branch tips:

| Theorum capsule or archive | Development branch | Pre-consolidation tip |
|---|---|---|
| `41_cut_graded_universal_generator_theorem.md` | `agent/cut-graded-universal-generator` | `01ee1d32ee704d97ea3e31811746ffdcb0ee221a` |
| `42_cut_graded_lambda_jacobian_tower_theorem.md` | `agent/cut-graded-lambda-jacobian-tower` | `9f5792ee62ce3a1a71d9ed242ff9cb10e6745f3e` |
| `43_bilateral_jet_flow_recognition_capstone_theorem.md` | `agent/bilateral-jet-flow-capstone` | `1e737c0f18d93fa69f5109a6fec426b7a69f2c1f` |
| `44_madhava_smriti_bilateral_jet_flow_closure_theorem.md` | `agent/madhava-smriti-jet-flow-closure` | `60b8bba2b4579d75c691af6589b00a764f24622b` |
| broader native theorem development | `agent/rkf-next-development` | `9d6bce5ac9cd2a7adeca228ff74901ae6bb6988a` |
| direct thermodynamic archive | `agent/thermodynamic-theorem-archive` | `191f2a424386394d9b4805239f742103604abe6a` |
| lambda-geometry expansion | `agent/broaden-thermodynamic-pr-archive` | `832d162077db2da7b33877f5755c55d1323c0c28` |
| thermodynamic cut-square specialization | `agent/thermodynamic-cut-square-theorem` | `b05b69bdd02bd3f230b12df996704661947e2b0f` |

On 2026-08-05 each branch was compared against `main`. Every branch had `ahead_by = 0`; therefore all theorem-bearing commits were already present in `main`. The stale refs were advanced by ordinary fast-forward without force or history deletion. The complete record is in `BRANCH_CONSOLIDATION_AUDIT.md`.

## Thermodynamic MP provenance

The thermodynamic archive under `theorum/thermodynamics/` is sourced primarily from:

```text
MP PR #239    thermodynamic response tetrad, entropy-scaled lambda coordinates,
              flat closure, response curvature and seam-index spectral flow;

MP PR #243    canonical response cost, projection/source overlap,
              Onsager compass and Hodge no-leakage, thermo-Weil provenance,
              physical-flux connection;

MP PRs #274-#275
              native cut-square event decoder and minimum-decoder burden,
              specialized as the thermodynamic cut-square theorem;

MP PRs #52-#61
              lambda holonomy, path ordering, admissible factorization,
              refinement-stable length, constrained descent,
              curvature-flux no-collapse and primitive flux witnesses.
```

Exact source file paths and blob hashes are preserved in `thermodynamics/SOURCE_PROVENANCE.md` and `thermodynamics/lambda_geometry/SOURCE_PROVENANCE.md`.

## Supersession rule

A claim-boundary statement may accurately describe the repository state at the time a theorem was written and later become historically stale. The principal example is Theorem 43's statement that a Madhava-named calculus was not yet present. Theorem 44 now supplies that extension. The earlier mathematical theorem remains valid; the later capsule supersedes only the repository-status sentence.

## Consolidated canonical branch

```text
repository: Parveen117/Recognition-Kernel-Framework
canonical branch: main
branch audit: theorum/BRANCH_CONSOLIDATION_AUDIT.md
complete theorem map: theorum/README.md
```

Future theorem development should branch from current `main`, preserve individual evidence labels, and return through a verified fast-forward or reviewed merge. Otherwise the repository will resume its natural ambition to become a maze.
