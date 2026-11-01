# SE9 audit and verification scope

12 October 2026. Owner: Monty Dabas.

| Result | Evidence | Scope |
| --- | --- | --- |
| Fixed catalogue through an event | SE9.3--SE9.4; exact support identity | Same full-source equation before, at and after prime-3 activation |
| L2 overlap obstruction | SE9.5--SE9.6; symmetric and antisymmetric reflection states | New prime term has norm Lambda(n)/sqrt(n) on every nonempty near-threshold overlap |
| Native event continuity | SE9.7--SE9.10; exact frequency-band multiplier bound | Full pulled-back source is native norm-continuous on compact scale ranges; continuity alone does not prove positivity |
| Smooth lower comparison | SE9.11--SE9.13; common catalogue and a uniform envelope | Operator-norm real analyticity through the event; only its final scale is certified positive |
| Executed prime-3 crossing | SE9.14--SE9.21; 52 interval LDL pivots, quadrature and complete tails | Source floor 1/500000 on every complex odd state of radius 9/16 |
| Native observer segment | SE9.22--SE9.24 and physical subspace inclusion | Native floor 1/9906251 and squared reserve 2/108968761 on every smaller aperture |

The 52 comparison coordinates are neither the historical five-label
Feshbach matrix nor SE6's fifteen native moments. Every mixed matrix
entry and the full discarded coupling enter the certificate. The two
primes and the complete negative odd pole are included in one source.
The positive result is for the entire aperture, not only 52 test vectors.

## Verification

Commands:

```text
python proof_lab/endpoint_prime_event_certificate.py --check
python -m unittest proof_lab.test_endpoint_prime_event_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The read-only SE9 replay regenerates the complete matrix and result,
checks all prime/Gamma/pole budgets, proves all 52 LDL pivots positive,
and includes analytic quadrature and infinite-tail errors. Its candidate
matrix SHA-256 is
9fc703f05cc4166dbff5ee5f44299741d842181460f8144b4a47c58db9b47665.
The total leading-matrix error is below 7.011e-8; the certified source
floor is 2e-6. The matrix archive stores exact rational decimals rather
than using a floating-point eigenvalue as the sign test.

Under Python 3.12.14, the complete read-only replay reproduces its matrix
and every result exactly. All fourteen tests pass: six arithmetic
controls (two new and four inherited) and eight navigation checks.
Thirty-seven parent-source pins and four new arithmetic pins match.
The 1,113 parent blobs outside the four active navigation edits are
preserved byte for byte, including all earlier proof files and pins.

The required operator-engine check was attempted and failed the same
existing runtime-sensitive pin under Node v24.19.0:
actual 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e,
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The engine includes process.version and documents Node 22.16.0, which
is unavailable here. This engine check is not PASS; its pins are not
changed to hide the mismatch. No remote CI success is inferred.

## Remaining obligations

The certified range is now 1<=c<=9/8 in the radius-1/2 reference chart,
and hence includes c=log 3. The next event is the prime power 4 at
c=log 4. No certificate for that event or every later event is supplied.
The event-continuity modulus does not guarantee that the source avoids
a zero crossing, nor that the lower comparison stays positive.

A proved cofinal family of complete source certificates, or another
all-scale sign-preserving rule, is still needed. No global norm-one
observer, global eta=0 sign, historical five-source closure, K0, RH
proof, formal proof-assistant verification or external review is claimed.
The earlier SE7 and SE8 floors remain valid on their smaller apertures.

See the [proof](SE9_PRIME_EVENT_AND_NATIVE_CONTINUITY.md),
[source record](SE9_SOURCE_RECORD.md) and [pins](SE9_SOURCE_PINS.json).
