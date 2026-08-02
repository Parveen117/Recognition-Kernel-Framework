# Reviewer Guide

## Purpose

This repository is organized for independent review of a Recognition–Null Kernel Engine mathematical proof-transport cartridge.

The reviewer is not asked to accept a broad framework claim from terminology alone. The reviewer can inspect:

```text
pinned theorem sources;
executable implementation;
package specifications;
exact and interval obligations;
negative controls;
archived result JSON;
canonical hashes;
clean-run workflow.
```

## Recommended review order

### 1. Scope and terminology

Read:

```text
README.md
TERMINOLOGY_AND_FILING_ALIGNMENT.md
CLAIM_BOUNDARY.md
```

Confirm that the public umbrella is the Recognition Kernel Framework, the operational engine is RNKE, and the current cartridge has a limited declared mathematical scope.

### 2. Provenance

Read:

```text
SOURCE_PROVENANCE.md
certificates/foundation/campaign_result.json
```

Verify the source commit and canonical campaign hash.

### 3. Foundational source package

Inspect:

```text
src/rh_framework/native_summability.py
theorems/foundation/F00E_NATIVE_EULER_FROM_IOTA_COMPLEX.md
certificates/foundation/F00_F00E_EULER_V0_1/spec.json
certificates/foundation/F00_F00E_EULER_V0_1/verify.py
certificates/foundation/F00_F00E_EULER_V0_1/result.json
```

Questions to ask:

```text
Are source pins exact?
Are all required obligations present?
Are exact identities checked without ordinary floating-point proof margins?
Do negative controls detect wrong quarter-turn, dagger, factorial, exponential, and flow-sign constructions?
Does the scientific claim boundary remain limited?
```

### 4. Logarithm, arithmetic, and zeta package

Inspect:

```text
theorems/foundation/F00G_NATIVE_LOGARITHM_AND_POWERS.md
theorems/foundation/F00H_NATIVE_NATURAL_ARITHMETIC_AND_PRIME_FACTORIZATION.md
theorems/foundation/F00I_NATIVE_DIRICHLET_ZETA_EULER_PRODUCT.md
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/spec.json
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/verify.py
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/result.json
```

Questions to ask:

```text
Are logarithm intervals outward and accompanied by explicit tails?
Are finite arithmetic identities exact?
Are prime-factor and coefficient obligations finite and deterministic?
Are dyadic and Euler-product tails explicit?
Are invalid rearrangement or arithmetic controls rejected?
Does the package avoid claiming analytic continuation or RH?
```

### 5. Reproduce

Follow `REPRODUCE.md` on a clean clone.

Required final output:

```text
PASS_IMPLEMENTED_FOUNDATION_CERTIFICATE_CAMPAIGN
F00GHI_LOG_ARITHMETIC_ZETA_V0_1 PASS_F00GHI_LOG_ARITHMETIC_ZETA_AUDIT 0
F00_F00E_EULER_V0_1 PASS_F00_F00E_RIGOROUS_COMPUTATIONAL_AUDIT 0
```

### 6. Adversarial review

A serious review should attempt at least one controlled mutation in a disposable clone:

```text
change iota^2 sign;
change dagger orientation;
remove a factorial;
change the Euler-flow sign;
change a source file without updating its pin;
remove a required policy statement;
replace a rigorous tail with an unsupported truncation.
```

The relevant verifier should return a non-PASS status.

## Reporting review findings

A useful review report should distinguish:

```text
source/provenance defect;
verifier implementation defect;
incomplete obligation set;
mathematical theorem gap;
claim-boundary overstatement;
reproducibility defect;
documentation issue.
```

Do not report a theorem contradiction when the actual finding is a path, newline, serialization, or source-pin issue. Likewise, do not dismiss a mathematical failure as infrastructure merely because the package is intended to pass.

## Current reviewer conclusion supported by the archived run

The archived source set passed every declared obligation in both implemented packages with no failed checks. This supports the implemented foundation certificate campaign only. It is not an independent expert validation of every later theorem in the wider research programme.
