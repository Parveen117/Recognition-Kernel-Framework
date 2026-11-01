# PG11 — Lexical present paths, owned ending augments and substitutions

Author: Monty. 1 November 2026.

PG11 completes another **40 identified roots, 45 licensed pada paradigms,
405 present cells and 420 derivation branches**. Thirty-nine adādi roots
contribute 396 cells / 411 branches. The sole-vowel juhotyādi root ṛ
contributes nine cells / nine branches under an explicit classical-use
license. Requests retain lexical identity, meaning, supplied pada license,
person, number and register.

The cumulative [coverage register](COVERAGE_STATUS.json) now contains
**131 / 2,229 root entries, 166 paradigms, 1,494 present cells and 1,643
branches**. PG4–PG11 contain 186 bounded rule definitions referring to 142
distinct sūtra IDs. These counts describe the admitted unaccented,
unprefixed classical kartari laṭ profiles; they are not an overall grammar
completion percentage or a claim about every context of these roots.

## Added paths

| Roots or source group | Entries | Main additions |
| --- | ---: | --- |
| han | 1 | Distinct weak jhal n-lopa and vowel-triggered a-lopa, then h → gh |
| dviṣ, duh, dih, lih | 4 | Both padas; h-final changes, bhaṣ and licensed lih lengthening |
| cakṣ, īr, īḍ, īś, ās, vas | 6 | Retained cakṣ marker disagreement, se/dhve iṭ and local s-lopa |
| 1020014–1020024 | 11 | Distinct nasal-marker identities, num, palatal contact and root ownership |
| sū, śī | 2 | Root-vowel junctions; śī guṇa and ruṭ on the actual jh substitute |
| brū, iṇ, vī, vac, vid, mṛj | 6 | Optional present ending substitutions, mandatory brū īṭ, iṇ exception and mṛj vṛddhi |
| rud, svap, śvas, an | 4 | iṭ before val-initial sārvadhātuka endings |
| jakṣ, jāgṛ, daridrā, cakās, śās | 5 | Lexical abhyasta designation without a physical copy; further lexical strength rules |
| ṛ, 1030017 | 1 | Owned sole-vowel copy, r-accompanied replacement memory and ordered iy/yaṇ junctions |

[LEXICAL_ENTRIES.json](LEXICAL_ENTRIES.json) records every exact source ID,
teaching form, meaning, pada and admitted profile. Similar headwords are
not merged. In particular the two kas and two vṛj entries retain their
different source markers and num behavior.

## State and evidence

The [grammar](grammar.py) extends PG10 through a separate class and new
records. It does not read expected forms or the external conjugation table.
An ending substitute retains the original ending, its features and the
present lakāra. Thus vid's optional veda path does not silently become a
perfect-tense request. Brū's first five parasmaipada endings have a coupled
āh substitution; its other endings cannot borrow that option.

iṭ and īṭ belong to the following ending. Ruṭ belongs specifically to
the already-created jh → at component of śī's plural ending. Each augment
retains its teaching sounds, marker evidence and ordered membership.
The five lexically designated abhyasta roots retain one root constituent;
only ṛ receives a new copied constituent in this stage.

[Scope compilation](scope.py) binds individual source occurrences. The two
bruvaḥ tokens in 3.4.84 have different cases and cannot be interchanged
merely because their spelling matches. The 43 new records and ten local
scope overlays retain the source frame and reviewed roles. Lih's two
visibility permissions are local, identity-bound edges, not a reversal of
the Tripādī or a general asiddha solver.

[Source review](SOURCE_REVIEW.md) and six
[adjudications](SOURCE_ADJUDICATIONS.json) preserve disagreements between
the pinned source fields. [Validation](VALIDATION.md) separates 245 literal
word-membership cases across 39 roots, 40 refusals and 107 direct controls
from the independent implementation comparison of 405 cells / 420 branches.
All pass with zero comparison differences. New pṛj has no separate exact
full-word witness in the selected passages; the six earlier PG10 witness
gaps also remain open.

## Run locally

Use the `ashtadhyayi-com/data` checkout pinned by
[SOURCE_PINS.json](SOURCE_PINS.json), commit
`5744762f010d677cfb43f347a42d02796cf615d6`:

```sh
python3.12 -m research.panini_grammar.lexical_present.verify \
  --source-root /path/to/ashtadhyayi-data

python3.12 -m research.panini_grammar.lexical_present.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1020039 --sense 'व्यक्तायां वाचि' \
  --pada P --pada-licensed --all-forms
```

Add `--trace` to inspect retained derivations and readout history.
`--write` regenerates only PG11's two result files when deliberately
refreshing this stage. The verifier reads frozen PG10 coverage for the
cumulative totals and checks predecessor file hashes; it does not replay
their suites or regenerate their certificates.

[Remaining work](REMAINING.md) includes prefix/context-sensitive class-2
entries, tagged roots, wider tense and voice systems, nominal grammar and
the native operator lift. PG1–PG10 remain unchanged. Full native lifting,
typed zero-specialization compatibility and quantum-calculator integration
are still open; hosted CI and main merging remain deferred.
