# Certificate Index

## Campaign

| Field | Value |
|---|---|
| Campaign | Native foundation proof-transport campaign |
| Source commit | `c588ded973a395b5fce37c82f670616160979a2e` |
| Implemented packages | `2` |
| Status | `PASS_IMPLEMENTED_FOUNDATION_CERTIFICATE_CAMPAIGN` |
| Canonical summary SHA-256 | `8728ab0319afe5fb6e6329deaee479cfa93f50bb4422ee863aaaf4f911dd9582` |
| RH status | `OPEN` |

Archived summary:

```text
certificates/foundation/campaign_result.json
```

## Package F00_F00E_EULER_V0_1

| Field | Value |
|---|---|
| Certificate class | Foundational computational audit |
| Scope | cut scalar and native Euler derivation |
| Status | `PASS_F00_F00E_RIGOROUS_COMPUTATIONAL_AUDIT` |
| Package canonical result SHA-256 | `edc07e6bed39874251c0b75bb0e806a393a9b61343351fb40d70034fa66a2af5` |
| Archived result file SHA-256 | `c8db07cc20bb532ddf483bb56483ab43e3d717b765e7f9525fd8dafc2f380a41` |

Files:

```text
certificates/foundation/F00_F00E_EULER_V0_1/README.md
certificates/foundation/F00_F00E_EULER_V0_1/spec.json
certificates/foundation/F00_F00E_EULER_V0_1/verify.py
certificates/foundation/F00_F00E_EULER_V0_1/result.json
```

Authoritative mathematical and executable sources:

```text
src/rh_framework/native_summability.py
theorems/foundation/F00E_NATIVE_EULER_FROM_IOTA_COMPLEX.md
certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md
```

## Package F00GHI_LOG_ARITHMETIC_ZETA_V0_1

| Field | Value |
|---|---|
| Certificate class | exact and rational-interval foundational audit |
| Scope | native logarithm, arithmetic, prime factorization, and half-plane zeta |
| Status | `PASS_F00GHI_LOG_ARITHMETIC_ZETA_AUDIT` |
| Package canonical result SHA-256 | `672865d994b1111a876b160a80858f78d3133f400351f0792715a8d8bee142bd` |
| Archived result file SHA-256 | `b5eff18191bc1834d57b8783a0f35c7214123d544d0ba6431d241e4227e150b6` |

Files:

```text
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/README.md
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/spec.json
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/verify.py
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/result.json
```

Authoritative theorem sources:

```text
theorems/foundation/F00G_NATIVE_LOGARITHM_AND_POWERS.md
theorems/foundation/F00H_NATIVE_NATURAL_ARITHMETIC_AND_PRIME_FACTORIZATION.md
theorems/foundation/F00I_NATIVE_DIRICHLET_ZETA_EULER_PRODUCT.md
certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md
```

## Theorem 45 directed arithmetic-analytic closure packet

| Field | Value |
|---|---|
| Certificate class | Exact finite arithmetic / enclosure algebra audit |
| Scope | finite-decimal exact rationalization, zero-radius exact embedding, outward threshold composition, refinement identity, certified-ball overlap |
| Status | `PASS_DIRECTED_ARITHMETIC_ANALYTIC_CLOSURE_CANDIDATE` |
| Canonical result SHA-256 | `294f5da69567086e869953ee0374fced3b4ea5f745138673b8025fb6d615ca5a` |
| Branch proof-lab CI | `PASS` |

Files:

```text
theorum/45_directed_arithmetic_analytic_closure_theorem.md
proof_lab/directed_arithmetic_analytic_closure.py
proof_lab/test_directed_arithmetic_analytic_closure.py
proof_lab/DIRECTED_ARITHMETIC_ANALYTIC_CLOSURE_EXPECTED.sha256
```

This packet is intentionally exact and finite. It proves the arithmetic/enclosure identities used by Theorem 45. Correctness of an arbitrary external interval/ball implementation remains a separate dependency and raw nearest-rounded floating point without an outward enclosure remains non-proof-bearing.

Theorem lineage:

```text
theorum/43_bilateral_jet_flow_recognition_capstone_theorem.md
theorum/44_madhava_smriti_bilateral_jet_flow_closure_theorem.md
theorum/45_directed_arithmetic_analytic_closure_theorem.md
theorum/28_recognition_complete_finite_to_infinite_cut_theorem.md
certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md
```

## Theorem 46 first-visible-jet seam quotient packet

| Field | Value |
|---|---|
| Certificate class | Exact finite-jet indeterminate-limit classification audit |
| Scope | raw division-by-zero rejection, first-visible-order classification, equal-order seam quotient, regular reparameterization invariance, denominator separation, exact quotient enclosure |
| Status | `PASS_FIRST_VISIBLE_JET_SEAM_QUOTIENT_CANDIDATE` |
| Canonical result SHA-256 | `9d4ad6ef6ff7a798d2e169b09dda170e166d13ec5b233801c9c8cf7e20a2d1ad` |
| Branch proof-lab CI | `PASS` on Python 3.11 and 3.12 |

Files:

```text
theorum/46_first_visible_jet_seam_quotient_theorem.md
proof_lab/first_visible_jet_seam_quotient.py
proof_lab/test_first_visible_jet_seam_quotient.py
proof_lab/FIRST_VISIBLE_JET_SEAM_QUOTIENT_EXPECTED.sha256
```

The packet verifies the exact finite algebra used by Theorem 46. It deliberately rejects raw algebraic `1/0` and `0/0`; it treats all-zero finite denominator jets as unresolved; and it verifies the explicit denominator-separation quotient radius with exact rational arithmetic. Flat-function or genuinely different-seam cases remain outside this finite-jet certificate.

Theorem lineage:

```text
theorum/42_cut_graded_lambda_jacobian_tower_theorem.md
theorum/43_bilateral_jet_flow_recognition_capstone_theorem.md
theorum/44_madhava_smriti_bilateral_jet_flow_closure_theorem.md
theorum/45_directed_arithmetic_analytic_closure_theorem.md
theorum/46_first_visible_jet_seam_quotient_theorem.md
```

## Planned but not certified

The following package names describe intended future audits. Their absence or design status must not be counted as a PASS:

```text
F06_08_OPERATOR_FOUNDATION_V0_1
F09_10_FOURIER_GAMMA_XI_V0_1
F11_EXPLICIT_WEIL_V0_1
F12_15_WEIL_OPERATOR_REDUCTION_V0_1
F16_ACTIVE_BAND_OUTWARD_V0_1
ENDPOINT_K0_OUTWARD_V0_1
```

## Verification rule

A package is considered reproducibly verified only when:

```text
its source pins match;
its verifier exits with code 0;
its result JSON reports a PASS status;
all mandatory obligations are present;
all negative controls behave as specified;
the result is reproducible from a clean checkout.
```
