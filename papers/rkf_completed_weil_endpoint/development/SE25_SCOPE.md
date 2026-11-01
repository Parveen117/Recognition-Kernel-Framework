# SE25 scope and validation boundary

12 October 2026. Owner: Monty.

The [written proof](SE25_SECTORAL_GAMMA_RECOVERY.md) attaches one
complementary Gamma-event observation to the corrected RH source.
The executed interval certificate proves
S_b+(27/50)I_X >= (1/369000)I_X on the entire complex odd native X.
Consequently the global negative count and nullity are zero for all
eta>=27/50. The sufficient nonnegative shift is 199259/369000;
only nonnegativity is claimed at that smaller value.

| Evidence | Scope |
| --- | --- |
| Rational Gamma and prime weights | Strict positivity proved algebraically on the whole half-line |
| One normalized coordinate of sixteen Gamma event sheets | Exact source attachment; all four trial directions and mixed terms retained |
| Whole-cell recovery integral | 18713 cells, depth at most 15; complete [1/512,1] coverage |
| Prime contributions | 23150 prime-power events through 2^18 plus complete analytic tails |
| Infinite spatial exterior | Entire z in (0,1/512], seed lower greater than 0.07913231042791518 |
| Source recovery burden | Less than 199/200, including the observation cost |
| Diagonal-only failure control | Greater than 1.344847295361361411 at the same parameters; not a negative source witness |
| Native norm conversion | Exact floor 1/369000; no change to the graph norm |
| Finite SS1 signal packet | Motivation and projection identity only; its toy model is not the RH carrier |

The interval computation uses exact Fractions and 90-digit outward
Decimal arithmetic. Exploratory floating-point optimization selected
rational witnesses but is not consumed by the certificate. Whole-cell
upper sums, complete tails and the event energy authorize acceptance.
The partition hash and exact rational coefficients are archived in
the result. Source pins bind the consumed modules and proof records.

The eta-zero source sign, eta=1/2, historical five-label attachment/K0,
RH completion and an infinite sequence of certified shifts approaching
zero are not established. A decreasing finite list of anchors supplies
no convergence theorem. SE21's finite V16 zero-shift certificate and
the local radius 21/25 are unchanged. No general orientation-free
index theorem or removal of the actual critical essential spectrum
is claimed.

## Validation commands and status

Use Python 3.12.14 and Node v24.19.0 for the recorded environment.

```bash
python -m proof_lab.endpoint_sectoral_recovery_certificate --check --progress
python -m unittest proof_lab.test_endpoint_sectoral_recovery_certificate -v
python -m unittest proof_lab.test_mathematics_index -v
node research/sectoral_signal/verify.cjs --check
node operator_foundation/verify_all.cjs --check
```

The SE25 replay has sixteen conditions; eleven separate controls test
the weight identities, independent kernel symmetry, sixteen event
energies, full four-direction Gram, null trial, resonance rejection,
target interference, exterior catalogue, eta range and native floor.
The fresh read-only replay reproduced the archive exactly and verified
all 44 source pins. All eight navigation checks and SS1's 24 exact
checks (including eight negative controls) passed. The 32 inherited
pinned blobs match the publication parent byte-for-byte; all twelve
transitive Python replay modules are pinned.

The required unchanged engine command was executed and fails its
pre-existing first-suite pin mismatch at `tests/verify.cjs --check`:

- actual: `35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`
- expected: `f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`

Later engine suites do not run after that failure. No engine file or
pin is changed, and no whole-engine PASS is asserted. The SE25 Python
source replay does not import that JavaScript engine. This packet is
a written proof with rational/interval computational evidence, not
formal proof-assistant certification or external mathematical review.

