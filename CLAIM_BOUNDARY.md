# Claim Boundary

## Current certified scope

The first public reviewer cartridge contains two implemented foundational certificate packages.

### F00 / F00-E

Certified declared obligations include:

```text
exact cut-scalar multiplication;
quarter-turn relation and dagger;
exact norm-square identities;
factorial/binomial coefficient identities;
explicit factorial-tail bounds;
Euler circular residual enclosure;
flow composition and generator sign;
source-order policy checks;
adversarial negative controls.
```

### F00-G / F00-H / F00-I

Certified declared obligations include:

```text
positive logarithm series packets and exact tails;
Exp(Log(x)) enclosure packets;
logarithmic product-law packets;
division, gcd, and Bezout packets;
prime-factor reconstruction packets;
Mobius and von Mangoldt coefficient identities;
dyadic zeta convergence bounds;
finite Euler products with omitted-tail bounds;
nonvanishing product-tail obligations;
adversarial negative controls.
```

## Meaning of certificate status

### PASS

Every declared computational obligation in that package passed, required source pins matched, and all required negative controls behaved as specified.

### INCONCLUSIVE

At least one obligation was incomplete, unavailable, stale, not strictly enclosed, or failed to produce a lawful final result. `INCONCLUSIVE` is not silently promoted to PASS.

### FAIL

A required declared obligation was rigorously contradicted or a required negative control was not detected.

### STALE

One or more source pins or immutable inputs no longer match the package specification.

## What is not established by this release

This repository does not claim that the current certificates establish:

```text
all universal mathematical statements appearing in every related manuscript;
Fourier or Poisson reconstruction;
Gamma and completed-xi continuation;
Hadamard factorization;
the explicit prime–Gamma–zero formula;
the completed-Weil sign;
active-band source positivity;
eta-zero endpoint positivity;
K0 >= 0;
the Riemann Hypothesis.
```

These remain `NOT CERTIFIED`, `OPEN`, or subject to later audit packages.

## Manuscript status versus certificate status

The repository keeps distinct labels for:

```text
manuscript theorem classification;
computational certificate status;
external independent review status.
```

A manuscript theorem may be classified `PROVED` while its executable audit is `NOT IMPLEMENTED` or `INCONCLUSIVE`. Conversely, a computational PASS certifies only the finite obligations declared by its reduction and package specification.

## Recognition Kernel interpretation

The current public cartridge demonstrates the RNKE pattern on mathematical proof transport:

```text
declared state and theorem dependency
-> lawful derivation step
-> exact or outward audit
-> residue classification
-> certificate
```

The difficult number-theory application is the demonstrator. The public claim is the reproducible recognition-kernel architecture and the declared verified obligations, not an RH solution.
