# RH-Framework Native Verification Campaign

## Decision

New foundational theorem development is frozen while the existing native chain is audited in dependency order.

A theorem is not declared computationally verified merely because it has a script. A package advances only after:

```text
obligations frozen;
authoritative sources pinned;
exact or outward execution passes;
negative controls fail as intended;
result artifact is archived;
ledger evidence field is updated without changing the theorem claim boundary.
```

## Current campaign state

| Package | Scope | State |
|---|---|---|
| `F00_F00E_EULER_V0_1` | cut scalar and Euler derivation | `IMPLEMENTED / RUN_PENDING` |
| `F00GHI_LOG_ARITHMETIC_ZETA_V0_1` | logarithm, prime arithmetic and half-plane zeta | `IMPLEMENTED / RUN_PENDING` |
| `F06_08_OPERATOR_FOUNDATION_V0_1` | operator algebra, Riesz and compactness | `DESIGNED` |
| `F09_10_FOURIER_GAMMA_XI_V0_1` | Fourier, Poisson, Gamma and xi | `DESIGNED` |
| `F11_EXPLICIT_WEIL_V0_1` | zero geometry, explicit formula and Weil criterion | `DESIGNED` |
| `F12_15_WEIL_OPERATOR_REDUCTION_V0_1` | completed-Weil and spectral reduction | `DESIGNED` |
| `F16_ACTIVE_BAND_OUTWARD_V0_1` | active-band source positivity | `DESIGNED` |
| `ENDPOINT_K0_OUTWARD_V0_1` | eta-zero endpoint | `DESIGNED` |

The master runner `certificates/foundation/run_campaign.py` executes every implemented package containing `verify.py`. Missing planned packages are never counted as passes.

## Verification classes

| Class | Meaning | Admissible engines |
|---|---|---|
| F-Exact | Exact foundational identities and finite proof-bound arithmetic | integers, fractions, symbolic coefficients |
| F-Interval | Analytic identities reduced to compact interval and tail obligations | Arb/ball arithmetic, exact tails |
| O-Residual | Operator claims reduced to validated residual, graph-domain and finite-aperture obligations | interval linear algebra, exact Gram identities |
| N-Proof | Proof-bearing numerical theorem after a proved reduction | directed intervals, immutable tails, validated inertia |
| P-Policy | Provenance, source order, no-import and negative-control audit | hashes, static dependency checks |

## Campaign order

### C00/C00-E — Scalar genesis and Euler

**Package:** `F00_F00E_EULER_V0_1`

**Class:** `F-Exact + P-Policy`

**Current state:** `IMPLEMENTED / RUN_PENDING`.

### C00-G/H/I — Logarithm, arithmetic and half-plane zeta

**Package:** `F00GHI_LOG_ARITHMETIC_ZETA_V0_1`

**Class:** `F-Exact + rational F-Interval + P-Policy`

**Current state:** `IMPLEMENTED / RUN_PENDING`.

Implemented obligations:

```text
positive logarithm series and exact rational tail bounds;
Exp_Sigma(Log_Sigma x)=x on outward rational intervals;
Log_Sigma(xy)=Log_Sigma x+Log_Sigma y packets;
exact derivative and native-power consistency packets;
Euclidean division, gcd and Bezout identities;
Euclid lemma and prime factor reconstruction;
Mobius cancellation and formal-prime-log Mangoldt identity;
Euclid prime-prefix construction;
exact dyadic zeta convergence bounds;
finite Euler products plus rigorous omitted tails;
product-tail inequality supporting nonvanishing;
Mobius reciprocal and logarithmic-derivative coefficient identities;
adversarial negative controls.
```

### C06/C07/C08 — Native operator foundation

**Planned package:** `F06_08_OPERATOR_FOUNDATION_V0_1`

Obligations:

```text
adjoint identities on exact finite path cores;
energy bounds and nondegeneracy;
Riesz reconstruction residuals on exhaustive finite apertures;
form/operator sign equivalence;
compact aperture tail estimates;
negative controls for lost residue, wrong dagger and nonfaithful quotient.
```

### C09/C10 — Fourier, Poisson, Gamma and xi completion

**Planned package:** `F09_10_FOURIER_GAMMA_XI_V0_1`

**Class:** `F-Interval + P-Policy`

Obligations:

```text
Gaussian integral enclosure;
Gaussian Fourier self-duality;
approximate-identity error bounds;
Poisson finite window plus explicit tails;
theta inversion enclosure;
Gamma recursion and reciprocal-product tails;
Mellin continuation identity on overlapping domains;
xi functional-equation residual enclosure;
negative controls for wrong pi, Fourier sign and omitted Gamma factor.
```

### C11 — Cauchy, zero geometry, explicit formula and Weil

**Planned package:** `F11_EXPLICIT_WEIL_V0_1`

**Class:** `F-Interval + O-Residual + P-Policy`

Obligations:

```text
contour discretization and residue balance with outward error;
Jensen zero-count bounds;
canonical-product tail bounds;
prime-Gamma-zero explicit-formula residual;
on-seam positivity finite packets;
off-seam constructive negative witness with rigorous tail domination;
negative controls for missing residues, unsymmetrized zeros and sign reversal.
```

This is an audit-critical package and cannot be reduced to random evaluations of zeta zeros.

### C12/C13/C14/C15 — Completed-Weil and spectral reduction

**Planned package:** `F12_15_WEIL_OPERATOR_REDUCTION_V0_1`

**Class:** `O-Residual + F-Interval`

Obligations:

```text
completed-Weil form boundedness budgets;
Riesz representative reconstruction;
cut covariance and block reconstruction;
finite-aperture compactness;
positive square-root residuals;
Feshbach congruence identities;
Birman-Schwinger inertia agreement;
target-faithful kernel identity;
negative controls for lost blind residue and wrong Schur sign.
```

### C16-N — Active-band source positivity

**Planned package:** `F16_ACTIVE_BAND_OUTWARD_V0_1`

**Class:** `N-Proof`

This package is proof-bearing. It must prove the actual interval inequalities, complete prime tails, Gamma derivative bounds, source observability and virial error budget.

### CEND-N — Eta-zero endpoint

**Planned package:** `ENDPOINT_K0_OUTWARD_V0_1`

**Class:** `N-Proof`

This package must validate source regularity, inverse-half domains, norm descent, the exact five-label matrix and a lawful outward certificate for or against `K0 >= 0`.

## Master status meanings

```text
DESIGNED       obligations and package layout exist;
IMPLEMENTED    deterministic verifier exists;
RUN_PENDING    authoritative execution not archived;
PASS           all mandatory obligations and negative controls pass;
INCONCLUSIVE   at least one obligation is unproved or enclosure overlaps zero;
FAIL           a claimed identity or required margin is rigorously contradicted;
STALE          source pins no longer match.
```

## Scientific boundary

A PASS foundational certificate strengthens confidence and catches implementation/proof-bound errors. It does not replace universal reasoning that was never reduced to the checked obligations.

A PASS proof-bearing numerical certificate can promote a theorem only when its reduction theorem, domain coverage, tails and residuals are all part of the certified package.
