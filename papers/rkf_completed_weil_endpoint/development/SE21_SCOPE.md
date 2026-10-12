# SE21 certificate scope and remaining endpoint

12 October 2026. The user's global eta-zero target remains open.

| Layer | Actual result |
| --- | --- |
| Written mathematics | Exact complete Laplace source matrix, native density, complete derivative-tail bound |
| Executed source certificate | Strict eta=0 positivity on V_16=span_C{sgn(x)e^(-j|x|)/sqrt(2): j=1,...,16} |
| Spatial scope | Entire real line for these states; no spatial cutoff |
| Arithmetic scope | All prime powers, all Gamma modes and the full pole, with proved infinite remainders |
| Mixed observations | All 256 entries and every complex combination in V_16 |
| Unobserved complement | Not certified; global eta=0 does not follow |
| Global numerical frontier | Unchanged: SE17 shift 59/100 with native floor 1/7380, implied shift 10883/18450 |
| Positive support aperture | Unchanged: SE14 radius 21/25 |
| Formal/external evidence | Not formalized; not externally reviewed |

## Executed arithmetic and controls

Python 3.12.14. The new replay retains 320 Euler-transform terms with
the exact derivative remainders 2/2^320, 4/2^320 and 16/2^320.
These bound the complete analytic remainder, not just the last sample.
Euler's constant is enclosed through Bernoulli order 64 at M=1024;
pi and logarithms use the unchanged inherited series and tails.

All sixteen interval LDL pivots are strictly positive. The smallest
lower endpoint is

```text
1.600502732205724433398574184408846055248879087674646666595665686264948079834941189846e-42
```

The last pivot interval width is about 1.49123e-50. A pivot is not
an eigenvalue or native source floor. The full matrix, derivative
jets, constants, remainders, six replay checks and pivots are in the
[result](../../../proof_lab/ENDPOINT_ZERO_SHIFT_LAPLACE_RESULT.json).

The earlier 256-term attempt certified the twelve-direction matrix but
was inconclusive at the sixteenth pivot. Its zero-straddling interval
was resolved by the proved 320-term remainder. No negative-source
conclusion is drawn from that arithmetic failure.

Ten independent tests pass. They compare accelerated zeta values with
even-zeta formulas, derivative jets with ordinary Dirichlet tails,
Gamma entries with a separate full-mode bound, and the SE20 reference
and pole identities with exact rational integrations. Controls reject
wrong cancellation signs, positive-diagonal-only reasoning, an
unobserved negative direction and zero-straddling interval pivots.
The read-only replay also verifies the supplied SHA-256 source pins.
The existing eight mathematics-navigation tests pass.

## Required engine gate: unchanged failure

The required read-only command was run under Node v24.19.0:

```text
node operator_foundation/verify_all.cjs --check
FAIL at tests/verify.cjs --check: Pin mismatch
actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
```

This is the same previously recorded mismatch. No engine file or pin
is edited. The new Python source certificate has its own passing
replay; the repository-wide engine gate is not reported as PASS.

## Exact missing result

The dense-family theorem requires M_N>=0 **for every N**, or a proof
controlling the whole complement and its coupling to the observed
subspace. Sixteen successful pivots supply neither induction nor that
infinite Schur bound. The equivalent SE20 arithmetic inequality is
still unresolved. Eta=0 on all X, critical full-source recovery,
historical five-label attachment, K0 and RH are not established.

The user's requested completion cannot honestly be reported from
this packet. See the [proof](SE21_COMPLETE_LAPLACE_GRAM.md) and
[source record](SE21_SOURCE_RECORD.md).
