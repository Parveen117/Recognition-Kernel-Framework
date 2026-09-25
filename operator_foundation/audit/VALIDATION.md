# Validation record

Executed in this development pass:

```text
Runtime: Node v22.16.0
node --check core/native_operator.cjs
node --check tests/verify.cjs
node tests/verify.cjs --write
node tests/verify.cjs --check
```

The two syntax checks succeeded. The exact finite suite contains 122 named checks, including 625 scalar products. Results are regenerated from code and source-hashed. The explicit write creates the evidence; read-only verification separately compares it with the pinned bytes.

The native field arithmetic uses normalized BigInt fractions and cut-complex pairs. Number values are used only for finite dimensions, indexes, safe integers and deterministic enumeration, not floating-point field calculations.

The broad historical Python suites, infinite limits, formal proof assistants, and physical experiments were not rerun here. The system Python available during this pass was 3.13; no scientific tests were run with it. Existing requested Python 3.11/3.12 workflows were left unchanged. No account settings or repository visibility were changed.

The GitHub source snapshot is a recursive tree copy with its original tree hash. Source transfer integrity is a different check from a mathematical proof. The downloadable new-core companion does not contain that historical snapshot.
