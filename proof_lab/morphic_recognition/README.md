# Morphic Recognition RNKE Verification

This folder verifies the proof contracts for the theorem spine in:

```text
theorum/morphic_recognition/
```

The vocabulary and pre-foundational ordering of the Morphic framework are retained:

```text
Ś-0 Emptiness Guard
N-0 Nāgārjuna / Catuṣkoṭi
Morphic / Morphisum
collapse / Śūnya
cocycle / holonomy
clock recovery as representation
```

The executable verifier does not replace those terms with generic software vocabulary.

## What is verified

`verify.py` performs exact integer/rational-style calibration for:

- MR-01 Typed Residue Non-Cancellation and aggregator blindness;
- MR-02 Path Blindness and exact two-channel repair calibration;
- MR-03 Cocycle-Lifted Path Recognition, associativity, gauge/coboundary sign, and non-cocycle failure.

Every theorem includes at least one negative control.

## What is not claimed

A finite executable campaign is not a universal proof over an infinite mathematical domain. The universal proofs live in the theorem files. The executable layer checks the declared RNKE proof contract and guards against statement/implementation drift.

No formal proof-assistant certificate is currently claimed.

## Run

```bash
python -m unittest -v proof_lab.test_morphic_recognition
python -m proof_lab.morphic_recognition.verify \
  --output proof_lab/morphic_recognition/MORPHIC_RECOGNITION_ACTUAL.json
```

Expected top-level status:

```text
RNKE_CONTRACT_VERIFIED
```

The generated certificate is hash-bound and records the claim boundary explicitly.

## MR-04–MR-07: future memory, guarded Lopa, and holonomy scaling

The separate [memory development package](../../theorum/morphic_recognition/MEMORY_DEVELOPMENT.md)
uses `memory.py`, `guarded.py`, and `holonomy.py`. Its source manifest binds
the exact theorem, implementation, and test files. It rejects stale sources,
missing obligations, failed negative controls, and changed archived evidence.

```bash
python3.12 -m unittest -v proof_lab.test_morphic_memory proof_lab.test_guarded_lopa proof_lab.test_holonomy_scaling proof_lab.test_memory_certificate proof_lab.test_mathematics_index
python3.12 -m proof_lab.morphic_recognition.certify_memory --check-archive
```

The certificate records finite exact-arithmetic obligations. The universal
statements under declared hypotheses are supported by the ordinary proofs in
the capsules; no Lean/kernel or external peer-review status is claimed.
