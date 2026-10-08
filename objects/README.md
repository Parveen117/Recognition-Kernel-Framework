# Native Object Certification Catalogue

**Repository:** `Parveen117/Recognition-Kernel-Framework`

**Package:** `objects/`

**Edition:** `O15-v0.1`

**Author:** Monty Dabas

**Source draft:** `NEW maths objects(1).tex`

**Source SHA-256:** `68316205bd169a7b6592dadef3e0d1f909b6240e29e2b8a6ad94e7297bdf21ea`

This folder promotes the fifteen proposed cut/seam objects into the framework's
fail-closed certification discipline.  It does **not** turn every sentence of
the source draft into a theorem.  It separates:

1. a well-typed definition;
2. a universal proof;
3. a finite exact audit of proof-critical algebra;
4. a conditional bridge requiring additional hypotheses; and
5. an open or refuted-as-stated claim.

The governing order is the repository's native order:

```text
typed cut data
-> native scalar/algebraic object
-> proved identity
-> optional analytic or classical chart
-> physical or spectral adapter only under a separate theorem.
```

## Files

- `O15_NATIVE_OBJECT_CERTIFICATION.md` — definitions, repaired theorems,
  proofs, and claim boundaries for all fifteen objects.
- `STATUS_LEDGER.json` — machine-readable object-by-object verdicts.
- `certificates/O15_FOUNDATIONAL_AUDIT_V0_1/spec.json` — immutable audit
  specification.
- `certificates/O15_FOUNDATIONAL_AUDIT_V0_1/verify.py` — Python 3.11/3.12,
  standard-library-only exact verifier.
- `certificates/O15_FOUNDATIONAL_AUDIT_V0_1/result.json` — canonical result
  produced by the verifier.
- `tests/test_o15_objects.py` — regression and negative-control tests.

## Status vocabulary

| Status | Meaning |
|---|---|
| `PROVED` | Universal statement proved from the declared hypotheses. |
| `PROVED_REPAIRED` | The source idea survives after an explicit correction. |
| `PROVED_ABSTRACT` | Proved for the declared algebraic/chain object; a geometric adapter is separate. |
| `PROVED_FINITE` | Proved for a finite carrier; no infinite determinant claim is implied. |
| `CONDITIONAL` | Correct implication with hypotheses, but the hypotheses are not established here. |
| `OPEN` | No proof is claimed. |
| `REFUTED_AS_STATED` | The original statement has a direct counterargument. |

## Reproduce

From the repository root:

```text
python3 objects/certificates/O15_FOUNDATIONAL_AUDIT_V0_1/verify.py \
  --output objects/certificates/O15_FOUNDATIONAL_AUDIT_V0_1/result.json
python3 -m unittest objects.tests.test_o15_objects
```

Expected status:

```text
PASS_O15_NATIVE_OBJECT_FOUNDATIONAL_AUDIT
```

This is a **Class F foundational audit** under
`certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md`.  It checks exact finite
identities, source pins, the ledger, and negative controls.  It is not a Class N
certificate and does not prove RH, a new prime functional equation, modularity,
or a physical interpretation.
