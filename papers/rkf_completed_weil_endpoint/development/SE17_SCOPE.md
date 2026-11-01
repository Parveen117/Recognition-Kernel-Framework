# SE17 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Independent comparison weights | SE17.3--SE17.11; separate exact weighted squares | Same complete complex odd source and native graph metric |
| Regular odd boundary | SE17.5--SE17.6; exact degree-62 polynomial over 1+z+z^2+z^3 | No division through zero or imposed trace condition |
| Continuous weight family | SE17.12; affine inequality before division | Every alpha in [21/40,53/100], including nonconvergent replay choices |
| All-position lower bound | SE17.13--SE17.16; 485 full cells, two endpoint weights and the infinite exterior | Q>=1/1000 at eta=59/100; all primes and Gamma remainders accounted for |
| Global source invariant | SE17.17--SE17.18; native shifted floor 1/7380 | Actual global negative count and nullity zero for eta>=0.59 |
| Shape-loss control | SE17.19; exact complete point enclosure | Unshaped comparison fails at the same eta; no negative actual-source witness |

## Reproducible verification

```text
python proof_lab/endpoint_weight_family_certificate.py --check
python proof_lab/endpoint_signed_return_certificate.py --check
python -m unittest proof_lab.test_endpoint_weight_family_certificate proof_lab.test_endpoint_signed_return_certificate proof_lab.test_endpoint_global_eta_certificate proof_lab.test_endpoint_full_aperture_certificate proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Python 3.12.14 is used. No new dependency or arithmetic engine is
introduced. A replay recomputes every cell, source constant and tail,
then compares the entire archive. Earlier source pins are never
regenerated to repair a failed check.

## Executed evidence

The generating replay passes all 14 scalar, endpoint and coverage
conditions. The unchanged base catalogue contains 604 prime powers
through 4096, with SHA256
62bf603131d628d5bd67ad767f04882fcef6894a46bdcaa0ae3ff48c56e485ef.
The new exponent-11/2 mass lies in
(0.01856052946444597008,0.01856052946444607544), with its complete
omitted tail below 1.054e-16.

The 485 cells cover [1/64,1] in z=exp(-abs(x)/2), with exactly adjacent
rational endpoints and maximum depth 13. All 970 endpoint-weight
inequalities exceed 1/1000. The smallest enclosed lower value is
above 0.00100621309; the full infinite-exterior lower is above
0.34436233708. The written convex-family theorem covers every
intermediate alpha, without assuming that the quotient is affine.

Erasing the prime-weight shape while retaining the new Gamma weight
gives an upper comparison below -0.10164567760 at x=log3. This is a
complete point enclosure with the proper lower prime row, not merely
a negative lower estimate. It does not demonstrate source negativity.

The fresh full read-only SE17 replay passes all 14 conditions and
matches the entire archive. The preceding SE16 full replay also
passes its 13 conditions and matches its unchanged archive. The
combined suite passes all 38 tests: nine new controls, eight SE16
controls, nine SE15 controls, four inherited interval/certificate
controls and eight mathematics-navigation checks. Earlier expensive
local-aperture matrix replays were not repeated; their source and
archives are byte-preserved.

The required Node engine gate was executed under Node 24.19.0 and
failed at the same unchanged tests/verify.cjs pin comparison as SE16.
Actual hash:
35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e.
Expected hash:
f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
No engine source or pin was modified. The documented Node 22.16.0
run and remote CI are not claimed as executed. This stage does not
claim an engine-gate PASS.

## Boundary and preservation

The shift is a native spectral parameter, distinct from the physical
aperture radius. The implied nonnegative shift is 10883/18450; the
positive margin and nullity certificate are stated at 0.59. No exact
source edge, sharpness or rate toward eta zero is established.

The weight family releases a choice inside an exact decomposition;
it does not remove the source, metric, odd relation or complementary
readings. Arbitrary pointwise switching and arbitrary lossy measurement
are excluded. Faithful transport carries all maps and pairings.

Eta=1/2, the cofinal eta-zero sign, global critical contractivity,
historical five-label endpoint, K0 and RH remain open. The positive
local aperture remains 21/25. General proofs, exact finite controls,
analytic tail bounds, provenance and independent external review are
distinct evidence categories.

The final packet contains seven new files and four navigation updates.
All 1180 parent blobs outside those four navigation files are preserved
byte-for-byte, including the complete prior proofs, source pins,
preserved register and shared engine. Source pins bind 110 inherited
inputs, three new arithmetic artifacts and the new theorem. All 19
equation tags are unique and ordered; added links resolve and
whitespace checking passes. The prior 1184-blob published tree was
also checked against the local source before navigation was edited.

See the [theorems](SE17_INDEPENDENT_WEIGHTS_AND_GLOBAL_FAMILY.md),
[sources](SE17_SOURCE_RECORD.md) and [pins](SE17_SOURCE_PINS.json).
