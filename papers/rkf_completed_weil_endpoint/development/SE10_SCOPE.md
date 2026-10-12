# SE10 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Supported form-domain identification | SE10.2--SE10.4; inward dilation and even mollification | No hidden boundary condition when passing from the native core to the local form domain |
| Recovery of the local lower edge | SE10.5--SE10.9; monotone comparisons, compactness and retained weak mass | ell_(c,T) increases to min(b,lambda_c) at a fixed finite scale |
| Completeness for strict local positivity | SE10.10--SE10.12, using SE5/MP Gold 06 | At finite rational c, a positive full-source margin is equivalent to existence of a sufficiently refined positive finite certificate |
| Prime-power-4 crossing | SE10.13--SE10.21; 88 enclosed LDL pivots and all errors | Full odd source floor 1/20000000000 on physical radius 7/10 |
| Exact local observer | SE10.22--SE10.24 and native inclusion | Native floor 1/466500000001 and squared reserve 2/5131500000011 on every smaller aperture |

The completeness theorem does not provide an unproved premise that
every local source is positive. It also requires frequency, mode count
and numerical accuracy to be adjustable: increasing only the matrix
dimension at one failed frequency cap need not succeed. This stage
implements one fixed finite certificate, not a universal stopping
algorithm or an all-scale resource estimate.

## Verification

Commands:

```text
python proof_lab/endpoint_prime_power_certificate.py --check
python -m unittest proof_lab.test_endpoint_prime_power_certificate proof_lab.test_endpoint_prime_event_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The complete replay encloses every matrix entry, including its
forty-digit candidate rounding, verifies all 88 LDL pivots and checks
the analytic quadrature and infinite-tail budgets. The matrix hash is
1fdeac57db7fdb689c0c8c5d50f44d95da0df0ffc9e66dae4d0ca5ffae983b2a.
Its total leading error is below 1.148e-13; the full-source floor is
5e-11. The infinite mixed-block error is below 1e-17.

Under Python 3.12.14, the complete read-only replay reproduces the
archived matrix and every result exactly. All seventeen tests pass:
three new arithmetic controls, six inherited controls and eight
navigation checks. The new controls cover forty Gauss moments, a
separate shifted-complex digamma computation and direct trigonometric
Bessel formulas through z=96. Forty-five parent-source pins and four
new arithmetic pins match. The 1,121 parent blobs outside the four
active navigation edits are unchanged, including every earlier proof
and certificate pin.

The required operator-engine check was attempted and failed the same
existing runtime-sensitive pin under Node v24.19.0:
actual 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e,
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The engine includes process.version and documents Node 22.16.0, which
is unavailable here. This engine check is not PASS. No engine pin is
changed and no remote CI success is inferred.

## Remaining obligations

The certified range is 1<=c<=7/5 in the radius-1/2 reference chart.
It crosses c=log 4; prime 5 at c=log 5 remains outside. No positive
sign for every intermediate lower comparison is asserted; coverage
of the full source follows from native subspace inclusion.

A cofinal family of actual source signs, or another all-scale proof,
is still needed. Local certificate completeness does not supply
those signs. The global eta=0 sign, global norm-one observer,
historical five-label endpoint, K0 and RH remain open. No formal
proof-assistant verification or external mathematical review is claimed.
The smaller-aperture SE7--SE9 constants remain valid.

See the [proof](SE10_PRIME_POWER_AND_CERTIFICATE_COMPLETENESS.md),
[sources](SE10_SOURCE_RECORD.md) and [pins](SE10_SOURCE_PINS.json).
