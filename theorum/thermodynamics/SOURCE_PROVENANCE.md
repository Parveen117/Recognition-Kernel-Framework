# Source Provenance

## Repository lineage

The theorem capsules in this folder were extracted from the private proof laboratory:

```text
repository: Parveen117/MP
primary PRs: #239 and #243
primary source branch: agent/clock-free-recognition-proof
```

The source files remain in MP. This RKF folder is a clean theorem-level transfer, not a deletion of the original laboratory history.

## Foundational thermodynamic provenance: PR #239

```text
papers/rh_initial_journey/THERMO_CURVATURE_TO_SEAM_INDEX_BRIDGE.md
blob: 918a7a14cfb68caf907e0dcabee6c64d3935a31e

papers/rh_initial_journey/sections/07b0_thermo_curvature_lambda_provenance.tex
blob: cce8cb1dbb086d811046a01c32566bbb994ad1bd
```

Extracted results:

- signed \((C_p,C_v,C_s,C_t)\) response tetrad;
- entropy-scaled coordinates \(\lambda_X^{\mathrm{th}}=-ST/C_X\);
- flat closure \(\Gamma_c\Gamma_m=1\);
- response one-form and curvature;
- scalar-to-integer type obstruction;
- curvature-path / seam-index spectral-flow law;
- quantitative no-crossing criterion.

## Thermodynamic response and no-leakage laboratory: PR #243

```text
proof_lab/clock_free_recognition/CANONICAL_RESPONSE_COUPLING_AND_CURVATURE_GATE.md
blob: 5d64f8e505305cc7c3528456683abc5572bff718

proof_lab/clock_free_recognition/THERMODYNAMIC_RESPONSE_FIRST_RAMANUJAN_GATE.md
blob: d7bdcfb4b04aada3b2ec9e5244e0cb39949c9c3e

proof_lab/clock_free_recognition/THERMO_RAMANUJAN_JACOBIAN_COUPLING.md
blob: f5ba420ee26898edcbee4bf1822a2e077e334840

proof_lab/clock_free_recognition/NATIVE_THERMODYNAMIC_PROJECTION_DEFECT_THEOREM.md
blob: 852c876319c201fde3dfedf02ad7ded9213e8e1a

proof_lab/clock_free_recognition/NATIVE_THERMO_SOURCE_OVERLAP_IDENTITY.md
blob: e2fd9a23632e22d18ffac422e804537323e4a899

proof_lab/clock_free_recognition/NATIVE_EVENT_RESOLVED_THERMO_SOURCE_OVERLAP.md
blob: 40d4618ffd979274cc7484a9a413d0c22d5252c8

proof_lab/clock_free_recognition/NATIVE_ONSAGER_COMPASS_CURVATURE_INTERTWINER.md
blob: c86ed3b0e8dcb9b27f621a5d3caf0439463c034b

proof_lab/clock_free_recognition/NATIVE_ONSAGER_CONSTITUTIVE_PATH_NO_GO.md
blob: e6cb588fb400a9d245607f0c1b08c2fd5fb98979

proof_lab/clock_free_recognition/NATIVE_ONSAGER_HODGE_NO_LEAKAGE_THEOREM.md
blob: 7a21d7ae9f33bc49ccb6354d8176ae7703c58bbf

proof_lab/clock_free_recognition/THERMO_WEIL_PROVENANCE_INPUT_CONTRACT.md
blob: 66d98e6b1cbf214a277f0e7cd15ec5890e3e5b44

proof_lab/clock_free_recognition/THERMO_WEIL_FIVE_SOURCE_IDENTIFICATION.md
blob: 3ff34c728abfac224d3454a11d43453c79294a97

proof_lab/clock_free_recognition/THERMO_WEIL_BOUNDARY_SCHUR_REALIZATION.md
blob: 535d0fde891f15647a616ef90245f1343c68d57f

proof_lab/clock_free_recognition/NATIVE_CANONICAL_CONNECTION_PHYSICAL_FLUX_INTERTWINER.md
blob: c8160175207fd9b4ab58d690a491ba04414f8305

proof_lab/clock_free_recognition/ONSAGER_GEOMETRIC_O1_O2_AUDIT.md
blob: 456827539ed384a7227e76059860a3aef1d6dc36
```

## Transfer rule

Each RKF capsule retains only:

1. typed definitions;
2. theorem statements;
3. finite or abstract proofs actually supported by the source;
4. explicit hypotheses;
5. exact claim boundaries.

Numerical fits, speculative physical extensions, and RH conclusions are not promoted by this transfer.

## Current RKF transfer branch

```text
repository: Parveen117/Recognition-Kernel-Framework
branch: agent/thermodynamic-theorem-archive
base: main
folder: theorum/thermodynamics/
```
