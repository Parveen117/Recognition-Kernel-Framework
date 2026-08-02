# F00-G/H/I Rigorous Computational Certificate v0.1

## Scope

This Class F package audits the native derivation chain

```text
F00-G  positive logarithm and native powers;
F00-H  natural arithmetic, prime factorization, Mobius and von Mangoldt;
F00-I  half-plane zeta, Euler product and logarithmic derivative.
```

It does not prove the universal theorems by random sampling. It checks exact finite arithmetic, rigorous rational interval enclosures for the native logarithm/exponential inverse packet, the proof inequalities used in dyadic convergence and Euler-product passage, source-order policy, immutable source pins and adversarial negative controls.

## Arithmetic

```text
fractions.Fraction       exact rational arithmetic;
integer trial division   exact finite factorization audit;
rational intervals       outward series and tail enclosures;
SHA-1 / SHA-256          source identity and canonical result hashing.
```

No floating-point number is used in a proof margin.

## Main obligations

### Logarithm and powers

```text
C00G-01 Cayley contraction on the exact rational packet;
C00G-02 odd logarithm tails and Exp(Log x)=x enclosures;
C00G-03 multiplicative logarithm packet and exact derivative identity;
C00G-04 exponent-addition and product-base interval consistency.
```

### Arithmetic

```text
C00H-01 exhaustive division algorithm packet;
C00H-02 Euclidean gcd and Bezout reconstruction;
C00H-03 exhaustive Euclid lemma packet;
C00H-04 prime factor reconstruction and primality audit;
C00H-05 Mobius divisor cancellation;
C00H-06 formal-prime-log von Mangoldt divisor identity;
C00H-07 Euclid prime construction on increasing prime prefixes.
```

### Half-plane zeta

```text
C00I-01 exact dyadic block estimates;
C00I-02 geometric and polynomial-geometric tail bounds;
C00I-03 finite Dirichlet-convolution coefficients;
C00I-04 finite Euler products and rigorous zeta-tail enclosure;
C00I-05 product-tail inequality supporting nonvanishing;
C00I-06 Mobius reciprocal coefficient identity;
C00I-07 von Mangoldt logarithmic-derivative coefficient identity.
```

## Negative controls

The verifier must reject:

```text
noncontracting Cayley coordinate;
a composite number treated as prime in Euclid's lemma;
wrong Mobius signs;
omission of prime powers from Lambda;
the wrong dyadic exponent;
an Euler product truncated to first prime powers only;
classical logarithm/zeta inserted as a primitive source.
```

## Run

From the repository root:

```bash
python certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/verify.py \
  --output certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/result.json
```

Jupyter:

```python
%run certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/verify.py \
    --output certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/result.json
```

Passing status:

```text
PASS_F00GHI_LOG_ARITHMETIC_ZETA_AUDIT
```

## Claim boundary

A PASS confirms the declared exact/interval obligations and their alignment with the pinned theorem sources. It does not certify analytic continuation, the completed-Weil sign, `K0 >= 0`, or RH.
