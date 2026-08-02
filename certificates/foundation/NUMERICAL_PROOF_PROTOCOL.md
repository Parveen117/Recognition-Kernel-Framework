# RH-Framework Rigorous Computational Proof Protocol

## Purpose

RH-Framework uses computation in two mathematically distinct ways. They must not
be conflated.

```text
FOUNDATIONAL COMPUTATIONAL CERTIFICATE
    machine-checks exact algebra, finite identities, analytic bound formulas,
    source-order constraints, dependency hashes, and negative controls;

PROOF-BEARING NUMERICAL CERTIFICATE
    proves a mathematical claim after a proved reduction converts it to finite
    exact or directed-interval obligations with rigorous tail bounds.
```

Ordinary floating-point sampling, fitted curves, favourable plots, centre
values, or repeated agreement are calibration only. They cannot promote a
mathematical claim.

---

## 1. Admissible arithmetic

A proof-bearing computation may use only:

```text
exact integer or rational arithmetic;
exact finite-field or symbolic coefficient arithmetic;
directed interval or ball arithmetic;
validated linear algebra with outward residual bounds;
explicit analytic tail bounds;
immutable source and input hashes.
```

Nearest-rounding floating point may be used to choose subdivisions or initial
centres, but every reported proof margin must be enclosed outward afterward.

---

## 2. Required proof chain

A numerical result counts as proof only through the chain

\[
\boxed{
\text{proved reduction theorem}
\to
\text{finite computational obligations}
\to
\text{exact/interval execution}
\to
\text{tail and residual enclosure}
\to
\text{immutable certificate}.
}
\]

Every certificate must identify the reduction theorem it consumes. A numerical
packet without a reduction theorem is evidence, not proof.

---

## 3. Certificate classes

### Class F — Foundational audit

Used for F00 through the symbolic foundations. It checks:

```text
exact multiplication and dagger tables;
finite coefficient identities;
proof-bound arithmetic;
source-order and no-import constraints;
dependency and source hashes;
negative controls that must fail.
```

A Class F certificate does not replace the line-by-line universal proof. It
confirms that the executable foundation and the quantitative proof obligations
match the theorem text.

### Class N — Proof-bearing numerical enclosure

Used when a theorem reduces the remaining claim to explicit inequalities,
spectral bounds, matrix inertia, or tail estimates. It requires:

```text
directed interval arithmetic;
complete domain subdivision or a proved monotonicity reduction;
explicit omitted-tail bounds;
validated solves and residual propagation;
strict outward margins;
negative controls;
reproducible immutable evidence.
```

A passing Class N certificate may promote the reduced mathematical claim.

### Class P — Provenance certificate

Hashes exact theorem sources, code, parameters, dependencies and generated
artifacts. Class P proves identity and immutability, not mathematical truth.

---

## 4. Mandatory output fields

Every certificate result must contain:

```text
schema and version;
certificate class;
theorem or gate ID;
classification before execution;
reduction theorem;
source commit and blob hashes;
input hashes;
parameter packet;
exact/interval arithmetic engine and version;
obligations and individual results;
tail and residual ledgers;
negative-control results;
final status;
scientific claim boundary;
SHA-256 of the canonical result JSON.
```

Canonical JSON uses sorted keys, UTF-8 encoding and no insignificant whitespace.

---

## 5. Promotion rule

A theorem or gate may be promoted by computation only when:

```text
1. the reduction theorem is already PROVED;
2. every required computational obligation is complete;
3. every proof margin is strict after outward rounding;
4. all tails and residuals are included;
5. all realistic negative controls fail as expected;
6. the source and input hashes match immutable pins;
7. an independent reviewer can reproduce the canonical result.
```

Missing dependencies, unavailable interval engines, hash mismatches, non-strict
margins or incomplete tails return `INCONCLUSIVE`, never `PASS`.

---

## 6. Current certificate order

```text
C00    scalar genesis foundational certificate;
C00E   Euler exponential and flow foundational certificate;
C00GI  logarithm, prime arithmetic and half-plane zeta certificate;
C06-08 native operator foundation certificate;
C09-10 Fourier, Gamma and xi completion certificate;
C11    explicit formula and native Weil criterion certificate;
C16N   active-band directed interval proof certificate;
CENDN  eta-zero endpoint outward certificate.
```

The first implementation package is `F00_F00E_EULER_V0_1`.

---

## 7. Claim boundary

Cryptographic hashes prove provenance. Exact and interval computations prove only
the obligations covered by their reduction theorem and declared domain. No
certificate in this protocol presently proves the sign of the completed-Weil
operator, `K0 >= 0`, or the Riemann Hypothesis.
