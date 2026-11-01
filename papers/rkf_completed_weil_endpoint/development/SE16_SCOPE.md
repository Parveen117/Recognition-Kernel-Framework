# SE16 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Faithful odd return | SE16.4--SE16.6; exact half-line folding and complete Gamma series | Opposite-half kernel is subtracted before estimation; no arbitrary lossy measurement |
| Weighted return squares | SE16.7--SE16.12; complex square expansion and full prime translations | Exact nonnegative comparison defects, including every prime power |
| Full-source decomposition | SE16.13--SE16.16; native graph terms and positive remainders retained | Complete scalar lower bound returns to the native source with its metric factor |
| All-position certificate | SE16.17--SE16.20; 44 complete cells and an infinite exterior estimate | Q_(69/100)>=1/250 for every spatial position; no sample substitution |
| Global invariant | SE16.1 and SE16.21; native floor 1/1845 | Global kappa_eta=0 and nullity zero for eta>=69/100; implied nonnegative shift 25441/36900 |
| Loss-of-return control | SE16.22 and complete point enclosure at x=log3 | This comparison fails after erasing the odd-reflection cancellation; not a negative actual-source witness |

## Reproducible verification

```text
python proof_lab/endpoint_signed_return_certificate.py --check
python proof_lab/endpoint_global_eta_certificate.py --check
python -m unittest proof_lab.test_endpoint_signed_return_certificate proof_lab.test_endpoint_global_eta_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Python 3.12.14 is used. The executable uses the standard library and
unchanged earlier interval, logarithm, square-root and constant routines.
The archive contains every accepted rational cell and its enclosed
lower value. No source matrix or sampled eigenvalue is a proof input.

## Executed evidence

The generating replay and a fresh full read-only replay pass all 13
scalar/coverage conditions and agree exactly with the archive. The
prime catalogue has 604 nonzero prime-power entries through 4096,
with SHA256
62bf603131d628d5bd67ad767f04882fcef6894a46bdcaa0ae3ff48c56e485ef.
The complete exponent-5/2 prime mass lies in
(0.28873815,0.28876101). Its entire omitted tail is below 0.000022849.

The 44 cells cover [1/64,1] in z=exp(-abs(x)/2), with exactly matching
endpoints and maximum bisection depth nine. Their smallest enclosed
lower value exceeds 0.00425727944. The separate full-exterior lower
bound exceeds 0.44436234456. Both exceed the chosen uniform floor
1/250. Native conversion gives the shifted floor 1/1845 at eta=0.69.

At x=log3, the retained-return comparison has lower bound above
0.00697609. The erased-return comparison has upper bound below
-0.04362828. The latter is an upper enclosure using the exact prime
row formula and a lower prime-mass bound, not merely a negative
lower estimate. It establishes failure of the selected comparison,
not negativity of the original source.

The combined run passes all 29 tests: eight new independent controls,
nine SE15 controls, four inherited interval/certificate controls and
eight mathematics-navigation checks. The preceding SE15 full scalar
replay separately passes all 39 conditions and matches its archive.
Earlier expensive local-aperture matrix replays are not repeated;
their source and archives are preserved.

The required Node engine gate was executed and again failed at the
unchanged tests/verify.cjs pin comparison under installed Node 24.19.0.
Actual hash:
35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e.
Expected hash:
f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The documented Node 22.16.0 runtime is unavailable. Existing pins were
not regenerated. Engine-gate and remote-CI success are not claimed.

## Boundary and preservation

The positive margin belongs to the source shifted by 0.69 times the
native identity. It is not a strict reserve for the unshifted critical
observer. The implied shift 25441/36900 follows by subtracting the
certified native floor; it is not a measurement of the exact edge.

The comparison weight is not a physical intervention or an added
native primitive. Odd folding is faithful only because the full
carrier already obeys the odd relation. Source, involution, domains,
weights and pairing must travel together under observer transport.
There is no theorem that arbitrary information loss preserves kappa.

Eta=1/2, the cofinal eta-zero condition, global critical contractivity,
historical five-label endpoint, K0 and RH remain open. The local
positive aperture stays 21/25. No formal proof-assistant verification,
external review or general optimizer is claimed.

The final packet verifies seven new files and four navigation updates.
All 1173 parent blobs outside those navigation files are byte-preserved,
including earlier proofs, source records, pins, the preserved register
and the shared engine. Source pins verify 103 inherited inputs, three
new arithmetic artifacts and the new theorem note. All 22 equation
tags are unique and ordered; added local links resolve and whitespace
checking passes.

See the [theorems](SE16_SIGNED_RETURN_AND_GLOBAL_SHIFT.md),
[sources](SE16_SOURCE_RECORD.md) and [pins](SE16_SOURCE_PINS.json).
