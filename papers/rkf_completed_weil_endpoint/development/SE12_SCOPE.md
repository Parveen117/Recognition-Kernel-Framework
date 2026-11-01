# SE12 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Exact support calibration | SE12.2--SE12.5; full complex polarization | The full source and form domain are unchanged by a finite support-zero marker |
| Complete high-frequency condition | SE12.8--SE12.11; certified covering plus monotone Gamma envelope | Xi(t)>3/5 for every abs(t)>=384 |
| Concrete input improvement | Enclosed marked/unmarked readings at t=24837/50 | The unmarked symbol is below zero; the marked symbol exceeds the chosen cap |
| Prime-5 crossing | SE12.12--SE12.19; 168 outward interval LDL pivots, quadrature and full tails | Source floor 1/500000000000000 through physical radius 161/200 |
| Native local observer | SE12.20--SE12.22 and native inclusion | Native floor 1/13925000000000001; squared reserve 2/153175000000000011 |

## Reproducible computation

```text
python proof_lab/endpoint_support_marker_certificate.py --check
python -m unittest proof_lab.test_endpoint_support_marker_certificate proof_lab.test_endpoint_precision_frontier_certificate proof_lab.test_endpoint_prime_power_certificate proof_lab.test_endpoint_prime_event_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Python 3.12.14 is the supported runtime used here. The certificate
depends only on the standard library and pinned local arithmetic.
The entire finite frequency corridor [384,4096] is covered by 4236
dyadic cells, with maximum subdivision depth six and minimum proved
lower bound above 0.6011227473. The exact covered length is 3712.
For all remaining frequencies the proved lower bound exceeds
0.6221563585. Evenness covers the negative half-line. The partition
hash is 28bb61357e1cd6bc60ad3a58ab0ba86caae1c847a2932da2cb90e74411469c30.

The candidate matrix SHA-256 is
fddf7903a5f086c69a676a1fdcd0dcd36f282c99ef09a46a0520f5604b66aa16.
Its errors have distinct sources:

| Error or bound | Executed enclosure |
| --- | --- |
| Signed node-evaluation operator error | <1.303e-25 |
| Final candidate and pole row-sum error | <1.265e-39 |
| Total leading-matrix operator error, including quadrature | <1.112e-21 |
| Infinite diagonal deviation | <2.694e-71 |
| Full head/complement coupling | <1.222e-32 |

All 168 candidate pivots remain positive after subtracting 4e-15 I.
After the leading error, its exact head floor is at least 3e-15;
the complete comparison and source floor is greater than 2e-15.
The endpoint is beyond log(5)/2; prime 5 is active and retained.

Five new independent controls check signed fixed-grid arithmetic,
Gamma against a different shift through the far-tail boundary, direct
j_1/j_3 formulas through z=192 and a wide node interval, every retained
Bessel order through the all-odd Parseval identity, and rejection of
the selected tail cap when the marker is removed. The inherited
Gauss moments, signed-Gram controls and other interval checks remain
separate from the full certificate replay.

## Verification and preservation record

The generating replay passed and wrote all 168 pivots and the complete
tail evidence. All 26 combined tests pass: five new controls, thirteen
inherited arithmetic controls and eight mathematics-navigation checks.
The separate full read-only replay reproduces both matrix and result
archives exactly, including the complete interval covering and its hash.

The required shared-engine check was attempted under Node v24.19.0
and failed the same existing runtime-sensitive pin:
actual 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e,
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The engine records process.version and documents Node 22.16.0, which
is unavailable here. This gate is not PASS; no pin is replaced and
no runtime version is spoofed.

All 66 unchanged local input pins and four new arithmetic pins match.
The 249 local links checked across the active navigation and new
documents resolve; all 22 equation tags are unique. The 1139 parent
blobs outside the four navigation edits remain byte-preserved.
Git whitespace checks pass. Earlier full certificates are not rerun
in this stage; their archived proofs and source pins are unchanged.

The shared operator engine and its pins are unchanged. Earlier source
files, theorem records and certificates are preserved; only four active
navigation files are updated. NSB1/NSB2 are pinned external provenance,
not execution dependencies or assumed RH theorems.

## Limits

The marker calibrates a known identity, so this is not acquisition of
unknown information from a zero reading. It improves the selected
comparison at the same cutoff, as the explicit rejection control shows.
Relative to SE11 the cutoff rises from 256 to 384 and the mode count
from 116 to 168; reduced total work is not demonstrated. No universal
marker selection, monotone improvement or convergence rate is proved.

The next event is prime 7 at radius log(7)/2. A cofinal family of
actual source signs, the global eta=0 sign, historical five-label
closure, K0 and RH remain open. No strict uniform global reserve,
record aperture, proof-assistant verification, external review or
remote CI success is claimed. See the
[proof](SE12_SUPPORT_MARKER_AND_PRIME_FIVE.md),
[source record](SE12_SOURCE_RECORD.md) and [pins](SE12_SOURCE_PINS.json).
