# PG10 — Actual validation

Author: Monty. 1 November 2026.

Executed under Python 3.12 against the pinned primary checkout:

```sh
python3.12 -m research.panini_grammar.present_expansion.verify \
  --source-root /path/to/ashtadhyayi-data --write
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The verifier writes only PG10's new result and coverage files. It reads
the frozen PG9 coverage for cumulative accounting without replaying its
suite or regenerating its certificate. Navigation validation is required
for the two updated repository entry points.

| Direct check | Result |
| --- | --- |
| Literal primary Sanskrit word membership | 153 witnesses pass, covering 32 new roots |
| Unsupported requests | 35 expected refusals pass |
| Source drift, ownership, options, ordering and dispatch | 94 controls pass |
| Literal citation anchors | 444 references / 416 unique anchors match |
| Pinned external source files | 8 unchanged |
| Historical repository files | 86 unchanged |
| Pinned Vidyut comparison | 396 cells / 438 branches, zero differences |
| Mathematics navigation | 8 tests pass |

The CLI was invoked for all nine ru parasmaipada cells and all nine stu
ātmanepada cells with their exact meanings and supplied pada licenses.
Each returned the PG10 complete-domain status, retaining 17 and 14
branches respectively. A nine-cell prā invocation also completed and
preserved the dental n in `prānti`.

The controls cover copying the hr cluster without mutating the root,
retaining generated rapara-r before its copy lopa, and separating copy
guṇa from root strength. They distinguish long pṝ from short pṛ, the two
hā identities, class-2 mā from class-3 māṅ, and dāp from class-3 dā.
Bhī/hāk optional branches, cluster-sensitive iy, root-u junctions,
ūrṇu's strong options and consonant readout order are checked directly.

The īṭ controls require the lexical, tiṅ, sārvadhātuka and hal conditions,
reject an artificial pit restriction, preserve the teaching marker,
reject insertion twice or into the wrong host, and reject reversed
constituent membership. They inspect the ending-substitution → īṭ →
strength → vowel-junction order, including stu's apit ātmanepada cases.

Across every new branch, the verifier checks resolved obligations,
unique visible sound identities, retained copy-to-root links, ending
ownership of īṭ and equality between branch forms and reported forms.
Repeated readout cannot mutate, alias or feed back into its source.
Source wording, inherited conditions, lexical length and register drift
are also challenged. Only six inherited dispatch examples are invoked;
untouched predecessor suites are not replayed.

The generator and CLI read neither expected-form cases nor the external
comparison table. Six entries lack a separate full-word witness in the
selected primary passages, as documented in [SOURCE_REVIEW.md](SOURCE_REVIEW.md).
Their lexical/rule checks and implementation agreement are not relabelled
as word attestations. The report establishes only the declared finite
contracts, not a universal proof of Sanskrit validity.

No new companion theorem certificate was replayed. Hosted CI, the
untouched operator-engine suite and main merge were not run. Full native
operator lifting, zero-specialization compatibility and quantum-calculator
integration remain open.
