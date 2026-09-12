# Source Provenance - Recognition Topology Audit

Two uploaded source notes motivated this theorem audit. Their original personal
labels are intentionally not propagated into the repository terminology.

The source notes are evidence prompts, not theorem authority.

## Source A

```text
role: compact winding / curvature-memory note
SHA-256: bd0343d2676da7fcc5d1a911f8499001e72ff809289947e88f14cc19b424f848
```

Useful prompts extracted:

- winding number as a topological invariant;
- a proposed curvature/memory detector;
- closed-loop phase/holonomy language;
- discrete graph analogues;
- proposed integer sector-change diagnostics.

Audit result:

```text
WINDING / SECTOR IDEA                    RETAINED
CURVATURE-MEMORY INTERPRETATION          RETAINED ONLY THROUGH PROVED BRIDGES
CALIBRATED THREE-TERM THRESHOLD DETECTOR NOT PROMOTED AS FOUNDATIONAL OPERATOR
THRESHOLD => INTEGER JUMP                NOT PROMOTED
```

## Source B

```text
role: holonomy / spectrum / winding note
SHA-256: fc72600c220fb2c3f24fde3d94714c96bdad694a255e1f08e2378657ac71a12a
```

Useful prompts extracted:

- \(U(1)\) connection and curvature;
- loop-family holonomy;
- \(iU^{-1}\dot U\) as holonomy-rate generator;
- curvature contraction under loop deformation;
- logarithm/branch structure;
- winding and eigenphase-crossing relation;
- directed-graph phase transport.

Audit result:

```text
ABELIAN HOLONOMY RATE                    RETAINED AND PROVED
CURVATURE TRANSGRESSION                  RETAINED AND PROVED
LOGARITHM BRANCH MEMORY                  ALREADY STRONGER IN EXISTING FRAMEWORK
WINDING / UNITARY PHASE CROSSING         RETAINED WITH PRECISE TYPE BOUNDARY
GENERIC RATE-GENERATOR SPECTRAL FLOW     NOT PROMOTED
MODEL-SPECIFIC ENTROPY/SKEW CONNECTION   NOT PROMOTED AS CANONICAL
```

## Existing framework overlap

Before this audit the repository already contained:

```text
thermodynamics/02_curvature_to_seam_spectral_flow.md
thermodynamics/lambda_geometry/10_lambda_holonomy_and_branch_memory.md
thermodynamics/lambda_geometry/15_curvature_flux_no_collapse.md
thermodynamics/lambda_geometry/16_primitive_flux_spectrum_and_obstruction.md
morphic_recognition/02_path_blindness_minimal_memory_repair.md
morphic_recognition/03_cocycle_lifted_path_recognition.md
```

Therefore the uploaded notes are not imported wholesale. Only the
domain-independent topological bridge that was not yet isolated as its own
theorem layer is added here.
