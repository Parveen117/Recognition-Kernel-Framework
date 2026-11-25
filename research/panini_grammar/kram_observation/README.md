# Sharing the root-facing iṭ decision in √kram

This executable comparison covers the 171 previously written finite positions of PG77.
The seven admitted profiles supply the lexical identity, exact sense, prefix, agent
frame, pada and cause of its selection. The experiment compares two evaluation orders
for one decision. Both perform the same per-request ending, augment, phonetic and word
operations. The request language consists of the published cells in these profiles.
PG77 retains complementary and open channels outside that enumeration.

The reference is [PG77 STATE.json](../kram_future/STATE.json) at commit
`a3c988f3d4e0795c2c3de6d0551d8292b440890f`, SHA-256
`94a6ee65fb2042480823239444bbc86b45cfdd4ea4d49c514f830db6e0e847df`.
The evaluator takes its inputs from the profile, panel and temporal-context declarations.
The frozen per-form rows serve only as the comparison oracle.
[H01–H04](../kram_future/SOURCE_DECISIONS.md) give the source decisions,
[H05–H08](../kram_future/DERIVATIONS.md) the affix and ending schedules and
[the written paradigms](../kram_future/PARADIGMS.md) the readings.
The upstream Sanskrit archive is pinned in [PG77's source record](../kram_future/SOURCE_PINS.json)
at `5744762f010d677cfb43f347a42d02796cf615d6`.

## Why the decision can be shared

In PG77's basic kartari future-affix domain, H02 decides whether the root-facing iṭ
is admitted from the selected pada and its actual cause on the qualified root.
The bare residual P profile admits iṭ by 7.2.35. Six root-dependent A profiles
block it under 7.2.36. Both sya and tās meet the same relevant affix precondition.
Each request retains its own temporal certificate. The luminous-rise profile
admits three person-number slots in this packet, the others nine. Agent nouns,
derived stems and missing cause certificates cannot acquire the finite result here.

Use the full [PG14 operator/history modules](../grammar_construction/NATIVE_OPERATOR_LIFT.md)
and [PG77's typed extension](../kram_future/DOMAIN_AND_NATIVE.md).
For each admitted request q in profile p and its original history h, let g(p) be
the H02 decision. Direct evaluation computes g(p) at the request. Shared evaluation
computes it at the profile and applies that same value at q's original affix event.
Thus both select the same labelled successor of h and the same factor 1+z at that
event. Induction along the unchanged request-specific operators gives the same
terminal labelled history and coefficient for every input basis vector. Right-linearity
gives equality on their finite-support module. Complementary channels inherit their
original maps. Applying PG77's typed input and output specialization maps therefore
commutes with either evaluation, and both induce the same specialized pairing.
Evaluating the Boolean earlier changes no grammatical event order. The executable
compares the reported zero-readings and the recorded nine-stage history contract.

For example, parā + √kram yields **parākraṃsye** in both the ordinary future and
the conditional, A first singular. The future uses ending i→e followed by 6.1.97.
The conditional retains ending i and uses 6.1.87, with aṭ after the prefix.
Caching a whole result by spelling would lose this distinction.

## Reproduce

From the repository root, run

```sh
python3.12 -B research/panini_grammar/kram_observation/compare.py --benchmark
```

The correctness check compares both evaluated grids with every field of the
171 frozen rows, including accepted readings, source policies, original and
substitute owners, and path labels. It checks the ordered stages against the
archived contract and compares the two traces including their payloads. It also
checks the equal-spelling case and rejection of an unknown pada cause.

| Per 171-position grid | Direct | Shared |
|---|---:|---:|
| Root-facing iṭ decisions evaluated | 171 | 7 |
| Finite positions rendered and checked | 171 | 171 |
| Selected readings and labelled paths | 171 | 171 |

On a local x86-64 Python 3.12.14 run, medians were **0.8286 ms** direct and
**0.8078 ms** shared per grid. The respective interquartile ranges were
0.8088–0.9107 ms and 0.7884–0.8766 ms. The median paired direct/shared ratio
was 1.0332. After one warm-up per mode, 24 paired blocks each timed 24 fresh
grids per mode, alternating which ran first. Timing includes row and history
construction and disposal, with reference loading and comparison outside the
timed interval. The 164 avoided calls are reproducible. Timings vary by host
and the intervals overlap. CI enforces equivalence and call counts and reports
timing as an observation. This comparison adds zero grammatical positions or readings.
