# RNKE Proof Protocol for Morphic Recognition Theorems

## 1. Purpose

RNKE is used here as a **proof-obligation closure protocol**, not as a substitute for mathematics or a formal proof assistant.

For each theorem the proof packet declares:

```text
claim
assumptions
dependencies
proof obligations
negative controls
executable calibration
status boundary
```

RNKE may admit the proof packet only when every mandatory obligation closes and every declared negative control behaves as expected.

## 2. Decision states

```text
ADMIT       all declared proof obligations close
REJECT      a mandatory proof obligation is false
INCOMPLETE  an obligation is unresolved or evidence is missing
INVALID     the proof contract itself is malformed/inconsistent
```

A theorem's mathematical proof remains the proof. `ADMIT` means the declared proof contract is internally closed under the verifier implemented for this folder.

## 3. Proof packet schema

Every theorem packet contains:

```text
theorem_id
statement_version
assumptions[]
dependencies[]
obligations[]
negative_controls[]
calibration_domain
claim_boundary
```

No verifier is allowed to invent an assumption after observing a failed obligation.

## 4. Typed closure rule

Mandatory proof obligations are kept as typed coordinates:

\[
\mathbf r
=
\bigoplus_i r_i.
\]

The packet is admitted only when every required coordinate closes.

An aggregate scalar may be emitted for display only after its faithfulness on the adverse proof sector has been established.

## 5. Negative-control rule

Each theorem must include at least one exact negative control that would fail if the theorem were implemented incorrectly.

Examples:

```text
MR-01  sum aggregator hides (1,-1)
MR-02  one endpoint-memory channel misses a rank-two blind quotient
MR-03  a non-cocycle memory rule breaks associativity
```

A verifier that only checks positive examples is incomplete.

## 6. Calibration versus proof

Executable checks may verify:

- exact arithmetic identities on a declared finite domain;
- counterexamples to weakened hypotheses;
- schema/manifest integrity;
- dependency closure;
- consistency between theorem statement and implementation.

They do **not** by themselves establish a universal theorem over an infinite domain. Universal validity comes from the mathematical proof in the theorem file unless a formal proof-assistant certificate is added later.

## 7. Source independence

The theorem verifier must not consume the desired answer as evidence. In particular:

```text
no fitted residual cancellation;
no post-hoc ledger chosen after failure;
no target label inserted into an observer construction unless declared;
no endpoint equality promoted to path equality without a faithfulness theorem;
no clock degeneration promoted to native closure.
```

## 8. Current status language

Use only the following labels:

```text
PROVED_ALGEBRAICALLY
RNKE_CONTRACT_VERIFIED
COMPUTATIONALLY_CALIBRATED
FORMAL_ASSISTANT_VERIFIED
INCOMPLETE
REJECTED
```

`FORMAL_ASSISTANT_VERIFIED` is reserved for an actual external formal proof artifact and is not currently claimed.

## 9. Promotion gate

A theorem may be consumed by a domain adapter when:

```text
GENERAL PROOF                       PROVED_ALGEBRAICALLY
RNKE PROOF CONTRACT                 RNKE_CONTRACT_VERIFIED
NEGATIVE CONTROLS                   PASS
SOURCE / CLAIM BOUNDARY             DECLARED
```

A domain adapter may add new obligations, but may not remove theorem-level obligations.
