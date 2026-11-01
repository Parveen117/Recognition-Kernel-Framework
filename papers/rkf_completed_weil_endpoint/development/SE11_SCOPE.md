# SE11 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Signed-Gram error bound | SE11.5--SE11.7; exact integer sums, Bessel inequality and absolute signed weights | Node errors are bounded in operator norm without rounding every matrix accumulation |
| Radius-4/5 source certificate | SE11.2--SE11.14; 116 interval LDL pivots, analytic quadrature and complete tails | Full complex odd source floor 1/250000000000000 |
| Native joint observer | SE11.15--SE11.17 and nested native inclusion | Native floor 1/6600000000000001; squared reserve 2/72600000000000011 |
| Actual fixed-cutoff obstruction | SE11.18--SE11.19; rational 32-mode scalar witness | At radius 0.8047, catalogue {2,3,4} and T=256, mode/precision refinement alone cannot restore comparison positivity |
| Dormant-catalogue cancellation | SE11.20--SE11.22; exact support identity and a second scalar reading | Same full source, changed band reading; no certified minorant for the modified catalogue |

## Verification commands

```text
python proof_lab/endpoint_precision_frontier_certificate.py --check
python proof_lab/endpoint_cutoff_obstruction.py --check
python -m unittest proof_lab.test_endpoint_precision_frontier_certificate proof_lab.test_endpoint_prime_power_certificate proof_lab.test_endpoint_prime_event_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The new arithmetic controls check all forty-eight Gauss moments,
an independent shift-2048 complex-digamma enclosure, direct j_1/j_3
formulas through z=128, and positive/negative rank-one measures against
exact rational corner matrices. These test distinct analytic and
arithmetic risks rather than merely mirroring the matrix assembler.

The main certificate has total leading matrix error below 8.077e-22,
including signed-Gram node error below 2.959e-22. Its full infinite
coupling bound is below 5.477e-25. The candidate matrix hash is
b16fb99b197b4a6afa3f17bc37bad206eec4940186b5670e2607145fe361924f.

The cutoff witness is a negative value of a proved lower comparison,
not of the full source. Its dormant-prime modified reading is positive
only on the specified trial. No sign for the entire modified matrix,
no suitable tail envelope for that modification, and no prime-5
crossing are inferred.

## Runtime and preservation boundary

Python 3.12.14 is the supported runtime used here. The required shared
engine check was attempted under Node v24.19.0 and failed the same
existing runtime-sensitive pin:
actual 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e,
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The engine includes process.version and documents Node 22.16.0, which
is unavailable here. This gate is not PASS. No engine code or pin is
changed, and no remote CI success is inferred.

Both complete read-only replays reproduce their archives exactly under
Python 3.12.14. All twenty-one tests pass: four new arithmetic controls,
nine inherited controls and eight mathematics-navigation checks.
Fifty-three parent-source pins and six new arithmetic pins match;
224 local links resolve and all twenty-two equation tags are unique.
The 1,129 parent blobs outside the four active navigation edits remain
byte-preserved, including all earlier theorem and arithmetic files.

The original comparison's enclosed trial quotient lies between
-0.000037535056 and -0.000037531330. The same trial's dormant-prime
modified reading lies between 0.000137008218 and 0.000137011945.
These enclosures include analytic quadrature error; they are not
floating-point eigensolver outputs.

## Remaining obligations

The certified radius is now 0.8. Prime 5 at log(5)/2 remains outside.
SE10 completeness requires the freedom to refine frequency as well
as modes and arithmetic: SE11 now supplies an explicit obstruction
to holding the present cutoff fixed near that event.

A larger frequency band or a different fully bounded comparison is
needed for the next step. Neither the obstruction nor the better
arithmetic supplies a cofinal family of actual source signs. The global
eta=0 sign, historical five-label endpoint, K0 and RH remain open.
No formal proof-assistant verification or external review is claimed.

See the [proof](SE11_PRECISION_FRONTIER_AND_CUTOFF_OBSTRUCTION.md),
[sources](SE11_SOURCE_RECORD.md) and [pins](SE11_SOURCE_PINS.json).
