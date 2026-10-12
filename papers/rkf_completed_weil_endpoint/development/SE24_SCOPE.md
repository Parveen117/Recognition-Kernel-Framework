# SE24 audit and verification scope

12 October 2026. Owner: Monty.

| Result | Evidence | Scope |
| --- | --- | --- |
| Three independent weights | SE24.2--SE24.6; separate exact weighted squares for Gamma, prime and pole | Same complete complex odd source and native graph metric |
| Executed pole row and budget | SE24.5; <v,q_F>=31/210 exact, 4 int v^2/tau=1 | Pole read by a saturating density; constant bound b_c not used |
| Four-exponent prime row | SE24.4; signed combination, cell upper/lower bounds, masses p_{5/2}..p_{11/2} | Every prime power through 2^18; integral tails all below 10^-6 |
| Row domination | Lemma in section 3; W_k<=W_1 | Exterior reduced to SE16.19 at M=262144 |
| All-position lower bound | 1214 full cells on [1/512,1], depth<=12, and the infinite exterior | Q>=1/1000 at eta=14/25; exterior lower 0.0812929 |
| Global source invariant | SE24.8; native floor 1/7380 | Actual global negative count and nullity zero for eta>=0.56; implied shift 20659/36900 |
| Cut-point control | SE24.9; exact complete point enclosure | SE17's weights with the q_0 pole row fail at x=0 at eta=0.56 (upper -0.03601); pass at 0.59 |

## Reproducible verification

```text
python -m proof_lab.endpoint_three_weight_certificate --check
python -m unittest proof_lab.test_endpoint_three_weight_certificate proof_lab.test_mathematics_index -v
```

The replay builds the 2^18 prime-power catalogue (23150 prime powers,
catalogue SHA256 1a61a19f05f30f45f03f776667c1060b0a137973a74c3fe26f75e9b15d9186ad),
its four exponent rows, the degree-61 Gamma numerator, 1214 cells and the
exterior, in about four minutes. Python 3.13.16 was the available runtime
here; the repository's declared 3.11/3.12 runtimes were not available in
this session and are not claimed as run. No new dependency or arithmetic
engine is introduced: exact Fractions and the inherited 90-digit outward
Decimal intervals. Earlier source pins and archives are not regenerated.

## Executed evidence

The generating replay passes all 24 scalar, endpoint and coverage
conditions, and the fresh read-only `--check` replay matches the archive
byte for byte. The 13 independent controls pass: pole pairing against
direct exponential integrals; budget saturation and detection of a scaled
inadmissible density; the pole row against rank-one Cauchy--Schwarz and
the SE18.8 q_0 row; the Gamma numerator against separately integrated
exponentials and the vanishing cut-point row; rows against a direct
three-event catalogue including the +log n constant; W_k<=W_1 at sample
points; weight positivity slopes and refusal of a too-wide cell; the
prime row at z=1 against 2 sum c_k p; a planted anchor 11/20 failing at
the certified cell near x=0.325; the SE17 cut-point control; and the
constant-pole exterior value eta-b_c against the row's eta.

Exploratory floating-point searches over exponential-sum weight families
(up to eleven coefficients, exponents 1/2..7/2) were used to choose the
weights; their smallest pointwise floors were 0.5496--0.5775. They are
not inputs to the replay and are not evidence.

## Not run

```text
earlier proof_lab replays (SE14--SE17)   not rerun; archives byte-preserved
node operator_foundation/verify_all      not run (known pin mismatch unchanged)
Lean                                     not applicable
Python 3.11/3.12                         unavailable in this session
```

## Boundary and preservation

The shift is a native spectral parameter, distinct from the physical
aperture radius. Nothing below 14/25 is certified. The weakest interval
cells lie at x in [0.23,0.41]; they locate enclosure loss and are not a
route-floor claim (SE19 audit, section 1). The anchor improves SE23's
113/200 by a different mechanism; SE22--SE23 remain valid and preserved.
Eta=1/2, the cofinal eta-zero sign, global critical contractivity, the
historical five-label endpoint, K0 and RH remain open. The positive local
aperture remains 21/25.

See the [theorems](SE24_THREE_INDEPENDENT_WEIGHTS_AND_POLE_ROW.md) and
[sources](SE24_SOURCE_RECORD.md).
