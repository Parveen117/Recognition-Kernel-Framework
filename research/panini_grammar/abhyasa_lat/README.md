# PG9 — Owned abhyāsa and hu/dā/dhā present forms

Author: Monty. 1 November 2026.

PG9 adds **three identified juhotyādi roots, five licensed pada profiles,
45 laṭ cells and 45 branches**. Each path copies the pre-strength root into
a separately owned abhyāsa, retains the deleted śap-ślu unit, and designates
the two occurrences collectively as abhyasta. Guṇa or ā-lopa then follows
the actual tiṅ features. The generator never reads a conjugation table.

| Pinned root | Profiles | Examples | New operation |
| --- | --- | --- | --- |
| 1030001 हु | P | जुहोति, जुहुतः, जुह्वति, जुहुवः | Copy h→jh, late jh→j; strong root guṇa, weak root yaṇ before a vowel |
| 1030010 डुदाञ् | P, A | ददाति, दत्तः, ददति, दत्ते | Short abhyāsa a; weak root ā-lopa; ghusañjñā excludes ī substitution |
| 1030011 डुधाञ् | P, A | दधाति, धत्तः, धत्से, धद्ध्वे | The same weak deletion plus dhā's lexical bhaṣ and visibility exception |

The copied sounds have new UIDs and explicit `copied_from` links. Copy
shortening cannot change the original root, and markers removed during root
preprocessing never enter the copy. `--trace` exposes these identities,
source spans, deleted units, substitutions, blocked alternatives and the
local visibility query.

## Use

From the repository root, with the pinned ashtadhyayi-com/data checkout:

```sh
python3.12 -m research.panini_grammar.abhyasa_lat.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1030011 --sense धारणपोषणयोः --pada A \
  --pada-licensed --all-forms
```

For dā use `1030010`, `दाने`, and P or A. For hu use `1030001`,
`दानादानयोः आदाने प्रीणने च`, and P. A contextual pada license remains an
explicit input. Existing PG5–PG8 routes remain available. Prefixes, other
lakāras, other voices, accent and Vedic usage are outside this profile.

## Evidence and limits

[Verification](VERIFICATION_RESULT.json) records **38 literal commentary
word witnesses, 18 expected refusals, 63 direct controls and 112 citation
anchors**. Eight external source files and 71 historical files retain their
pinned hashes. All 45 cells separately agree with the pinned Vidyut output;
that comparison is not an independent traditional authority or a soundness
proof. [Validation](VALIDATION.md) lists the checks actually run.

[Coverage](COVERAGE_STATUS.json) now records **53 / 2,229 root entries,
693 present cells, 77 paradigms and 785 branches** across PG5–PG9. There
remain **2,176 root entries without this complete present profile**.
PG4–PG9 contain 114 bounded record definitions referring to 99 distinct
sūtra IDs. Neither this lexical count nor the 3,983-record text catalogue
is an overall grammar-completion percentage. Class 3 has 3 of its 26 pinned
entries admitted here; its other entries require further source review.

[Source review](SOURCE_REVIEW.md) explains the eight scope overlays and
Kāśikā's specific 8.2.38 permission. A generic reduplicator or universal
asiddha scheduler has not been constructed.

[Claude's T89 review](CONCURRENT_REVIEW.json) preserves the useful shared hu
identity while separating hotrī nominal forms from juhoti present forms.
Static inspection found that an inline comment hides five of the eight
claimed stage-removal dictionary entries. Full paradigm equality remains
checked by that module, but those five removal checks do not execute.
The companion certificate was not replayed or merged.

[Remaining work](REMAINING.md) identifies the next linguistic packages.
This is a bounded classical linguistic adapter, not a new native operator
theorem. The full operator-family carrier, its specialization maps and
`pi_0(Construct_lambda(inputs)) = Construct_0(pi_0(inputs))` compatibility
remain open for this adapter, as does quantum-calculator integration.
Hosted CI and main merging remain deferred by the owner.
