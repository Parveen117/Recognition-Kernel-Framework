# SE39 claim and validation scope

12 October 2026 (UTC). Owner: Monty.

## Written mathematics

The [derivation](SE39_DIRECT_RH_BRIDGE_AND_ZERO_SECTORS.md) contains three
theorem groups:

1. A branch-independent entire H with H(w^2)=xi(1/2+w), its genus-zero
   product, and the complete zero-sector expansion of the actual source
   response. Critical-line sectors are positive rank one; a nonreal
   conjugate sector has an explicitly negative two-probe determinant.
2. RH is equivalent to positivity of the actual full odd source, to
   every integer-rate Gram being nonnegative, and to operator
   monotonicity of its real response. The proof uses SE21's identity
   and density plus explicitly cited classical analytic theorems.
3. The actual negative diagonal branch E_-=0 and exact observer norm
   one are equivalent to RH. If RH fails, some finite rational mixed
   reading is strictly negative; no size bound or actual witness is
   provided.

This is a written proof of equivalences and decomposition statements.
It is not a proof of the equivalent universal positivity condition.
Classical inputs and the normalization translation are listed in the
[source record](SE39_SOURCE_RECORD.md). No formal proof-assistant
verification, independent review or priority claim is made.

## Exact executed model readings

The standard-library Python 3.12 application evaluates two supplied
polynomial models with exact Fraction arithmetic. Its saved readings
are decoded for a negative mixed direction, sector separation and
finite masking. The rational response computed directly from a
degree-22 polynomial is checked against independently summed sectors.
All ten scoped controls pass, and read-only replay matches the archive.

These controls do not use numerical zeta zeros, enclose an infinite
arithmetic operator, or certify RH. Finite examples check normalization
and demonstrate the stated failure of a finite acceptance inference;
the analytic theorems are supported by their written arguments.

## Repository validation

Commands executed from the repository root:

```bash
python3.12 -m proof_lab.endpoint_rh_bridge_controls --write
python3.12 -m proof_lab.endpoint_rh_bridge_controls --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The first two commands pass. All eight navigation tests pass after
syncing four already-published SE34--SE37 scope files that were missing
from the local checkout. The initial navigation failure was solely those
missing files; their exact parent blobs were restored without changing
their published contents. The full engine check fails at the inherited
`tests/verify.cjs --check` pin mismatch:

```text
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
```

No engine file or old pin is changed to suppress this failure. It is
separate from the ten successful new model controls. No global engine
PASS is claimed.

## Unchanged endpoint

SE27 remains the strongest inherited global certified anchor:
S_b+(1079/2000)I_X >= (1/492000)I_X. This implies nonnegativity at
the sufficient shift 265433/492000, without locating the optimal shift.
SE21 proves eta-zero positivity only on V_16. SE29's curvature norm
and essential norm remain 1/2; curvature does not determine its
negative branch. The historical five-label identification remains
open, though the SE39 direct route does not require it.

RH, global eta zero and the all-order source sign remain unproved.
SE38's formal unit-depth results and the separately published certificate
at `8fd344204e486daac91fddfd8e11ee075625a80d` are preserved. Its 25
scoped checks, including 8 negative controls, do not assert an RH
application. No claim identifies Lambda with eta, or a formal cut with
an analytic spectral limit.
