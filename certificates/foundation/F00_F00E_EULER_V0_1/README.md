# F00/F00-E Rigorous Computational Certificate v0.1

## Scope

This package is a Class F foundational computational certificate for:

```text
F00    cut scalar, quarter-turn, dagger and radial square;
F00-E  native exponential, Euler equation, circular factors and Euler flow.
```

It does not prove these universal theorems by sampling. It machine-checks the
finite algebra, executable implementation, exact coefficient identities,
quantitative proof bounds, source-order policy and verifier sensitivity on which
the line-by-line proofs rely.

## Authoritative sources

```text
src/rh_framework/native_summability.py
theorems/foundation/F00E_NATIVE_EULER_FROM_IOTA_COMPLEX.md
certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md
```

The verifier hashes these files at execution time. The result records the actual
hashes rather than silently trusting names.

## Obligations

```text
C00-01  NativeCutScalar implementation is importable.
C00-02  one and iota satisfy the exact multiplication table.
C00-03  multiplication is associative and commutative on the scalar basis.
C00-04  dagger is involutive and reverses multiplication.
C00-05  radial square is nonnegative on the declared exact audit lattice.
C00-06  the scalar product/norm identity agrees with exact rational arithmetic.

C00E-01 factorial coefficients and binomial convolution identities are exact.
C00E-02 declared factorial-tail bounds are strict on the audit packet.
C00E-03 the unit-tangent remainder bound is strict on the audit packet.
C00E-04 even/odd factorial splitting reproduces cosine and sine coefficients.
C00E-05 the finite Euler/Pythagorean residual is enclosed by declared tails.
C00E-06 flow composition and sign convention are consistent.
C00E-07 classical `-i r d/dr` appears only after the native Euler construction.
C00E-08 every negative control is detected.
```

## Arithmetic

All scalar identities and bound calculations use `fractions.Fraction`. No
floating-point value is used in a proof margin. SHA-256 uses canonical UTF-8
bytes. A later v0.2 may add Arb boxes for wider complex domains, but v0.1 is
already exact for its declared obligations.

## Run

From a repository checkout:

```bash
python certificates/foundation/F00_F00E_EULER_V0_1/verify.py \
  --output certificates/foundation/F00_F00E_EULER_V0_1/result.json
```

In Jupyter:

```python
%run certificates/foundation/F00_F00E_EULER_V0_1/verify.py \
    --output certificates/foundation/F00_F00E_EULER_V0_1/result.json
```

## Passing status

```text
PASS_F00_F00E_RIGOROUS_COMPUTATIONAL_AUDIT
```

A passing result confirms alignment of the executable foundation and the
quantitative proof obligations. It does not promote any still-open numerical
sign claim.
