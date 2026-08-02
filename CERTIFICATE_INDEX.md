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
