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

## Query a word or its full history

The calculator's [factored evaluator](https://github.com/Parveen117/quantum-classical-provisional/blob/68c900d58347ed1f308e0901b631cc997645f16d/native_relational_qc/FACTORED.md)
follows the dependencies of a requested observation. Its
[streaming contraction](https://github.com/Parveen117/quantum-classical-provisional/blob/68c900d58347ed1f308e0901b631cc997645f16d/native_relational_qc/STREAMING_CONTRACTION.md)
releases intermediates when their contribution has been consumed. Both ideas apply to
the declared PG77 finite relation without introducing quantum arithmetic.

From the repository root, select the outputs that the caller needs. Each line
of the result is keyed by profile, lakāra and person-number slot.

```sh
python3.12 -B research/panini_grammar/kram_observation/compare.py --query words --profile PARA_EFFORT --slot 1sg
python3.12 -B research/panini_grammar/kram_observation/compare.py --query history --profile PARA_EFFORT --slot 1sg --lakara lrng
```

The first command returns ordinary future `parākraṃsye`, non-today future
`parākrantāhe`, and conditional `parākraṃsye`. The second returns the full
conditional row and its nine ordered stages. A query outside the selected
domain, such as first singular for the luminous-rise panel, exits with an error.

**Word projection.** Restrict requests first by the panel's certified slots and
lakāras. Given their admitted profile p, lakāra l and slot s, the final observer
in PG77 H05–H08 returns the concatenation of three factors: the surface prefix
(including lṛṅ augment junction), the root/affix factor determined by iṭ and the
sya/tās choice, and the ending selected by (l, pada, s). The first two factors are
constant for this p and l. The full grid has 21 such groups. A query for one admitted
cell forms only its one stem. The word query returns this terminal projection and
its key. A caller requesting subsequent rule application or provenance uses the
history route. In particular the surface alone would collapse two keys in the example.

**Full history and typed recovery.** Let W be the keyed terminal word observer and
T the PG77 operator on the PG14 history module. On each admitted indexed basis
history, the three factors above give exactly W after T at the unit-start
zero-reading, by H05–H08. The existing PG77 typed specialization commutes with T.
Selecting whole request keys restricts to their labelled summands and commutes with
specialization because the profile, context and slot are retained at zero. A stream
visits each selected summand with the same T and order of events. Reassembling by
key recovers the full finite family, hence the same coefficients and pairing on
that family by the existing typed law. The program's word output is a terminal
reading. Full histories and their alternative labels are checked on the other route.

**Input and CI.** Queries read a pinned 6,074-byte [input file](query_inputs.json)
with the certified profiles, panel membership and temporal contracts. The full
547,996-byte PG77 state supplies the independent reference in CI. The check derives
the compact declarations from the pinned state and compares them field by field.
It then streams the direct history, the history evaluated from compact declarations
and the terminal word together for every request. Each row is compared with the
frozen reference. The key set detects missing, duplicate and extra records.

On local x86-64 Python 3.12.14 the following measurements used preloaded inputs.
The timing comparison returns the same dictionary of 171 keyed words, with the
history-based route already using shared iṭ and streaming. Twenty-four blocks per
mode each timed 24 grids, alternating which ran first. Python startup, JSON I/O and
printing are outside the timing. Peak allocations were observed separately using
`tracemalloc` while the same consumer validated one complete grid of full rows and
history stage order. The input and reference dictionary were loaded before tracing.

| Workload | Previous route | New route |
|---|---:|---:|
| 171 keyed words, median | 0.6975 ms | 0.0378 ms |
| Validate a complete generated history grid, peak Python allocations | 797,622 bytes | 24,726 bytes |

Runtime and byte measurements are observations. CI requires exact results, stage
order and operation counts. In the project-wide written-register check, only the
three available census fields need to cross a stage boundary. The checker still
reads all 815 state records and validates the same 1,328 deltas, including corrections.
A local pair of traced runs measured 13,045,258 and 12,245,029 peak Python bytes
before and after that change. These figures describe Python allocations during the
specified checks. They do not measure operating-system memory or overall CI duration.
