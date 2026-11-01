# PG12 — Actual validation

Author: Monty. 2 November 2026.

Executed under Python 3.12 against the checkout pinned in
[SOURCE_PINS.json](SOURCE_PINS.json):

```sh
python3.12 -m research.panini_grammar.nasal_present.verify \
  --source-root /path/to/ashtadhyayi-data --write
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The final verifier writes only PG12's result and coverage files. It binds
the four Python module hashes and the coverage object. Cumulative counts
read the frozen PG11 report; predecessor suites and certificates are not
replayed. An initial implementation comparison and first formal run also
passed; the final run includes two additional negative controls for
kṣubh's exact retained-śnā permission.

| Check | Result |
| --- | --- |
| Literal primary-word membership | 109 cases pass across 73 new roots |
| Unsupported requests | 37 expected refusals pass |
| Source, occurrence, ownership, branch and order controls | 124 pass |
| Literal source anchors | 717 references / 673 unique anchors match |
| External source files | 8 unchanged |
| Historical repository files | 115 unchanged |
| Pinned Vidyut comparison | 1,116 cells / 1,316 branches, zero differences |
| Mathematics navigation | 8 tests pass |

Five independent CLI invocations exercised all nine cells with the exact
listed meanings and supplied pada licenses:

| Lexical ID | Profile | Cells | Summed cell form count |
| --- | --- | ---: | ---: |
| 1080005, ṛṇ | P | 9 | 20 |
| 1080004, kṣiṇ | A | 9 | 22 |
| 1090007, stambh | P | 9 | 18 |
| 1090068, khav | P | 9 | 9 |
| 1090034, jyā | P | 9 | 9 |

Every cell returned `COMPLETE_IN_REVIEWED_NASAL_PRESENT_DOMAIN`.

The source controls reject missing śnā inheritance, wrong grammatical
case, unbound aṇ at 6.4.2, duplicate occurrences, wording/condition drift,
loss of kṣi's Vedic tag and erasure of the udhras disagreement. Source
inputs remain unchanged after construction and derivation.

Root controls distinguish penultimate n from final n and other nasals,
exclude idit and non-kit/ṅit triggers, and retain the deleted root UID.
The five 3.1.82 roots keep both affix choices. Sku can combine śnu with
optional u-lopa; the stambh cluster cannot. An affix from the wrong source
class is rejected.

Saṃprasāraṇa controls inspect both source sounds of the pūrvarūpa merger,
require the actual trigger and reject repetition. They distinguish grah's
nonfinal vowel from jyā's final vowel, check jyā's merger → lengthening →
shortening order, and prevent jñā from borrowing that path. The explicit
pvādi endpoint, class-5/class-9 dhū distinction, śit requirement and svṝ's
labiodental/r-accompaniment/late-lengthening sequence are checked directly.

Khav controls retain the ūṭh teaching marker separately from its visible
vowel and original v. Wrong ownership, an invented UID, an ordinary long
ū, a nonnasal affix, a non-kit/ṅit trigger and repeated substitution or
merger cannot produce the licensed vṛddhi path.

Root-strength and affix-strength stages reject wrong order and repetition.
The four tanādi options remain available even before weak endings because
the root trigger is u. The actual guṇa-created rṇ cluster blocks only the
affected u-loss branches; kṣiṇ's four-way option remains distinct. Ending
substitution must precede śnā's weak vowel deletion.

The ṇatva checks cover guttural, labial and mixed permitted interveners;
dental/l barriers, unreviewed num intervention, word boundaries and missing
exception review are rejected or excluded. Tṛp and kṣubh retain their
prohibitions. Kṣubh's identity query survives both weak śnā changes, but
cannot use the wrong retained affix or restore deleted sounds. Late dental
ending n remains separate from the earlier retroflex affix n.

All 1,316 branches are checked for resolved obligations, unique visible
sound IDs, one root/affix/ending, retained teaching forms, distinct branch
IDs, agreement between branch and reported forms, and root ownership of
ūṭh. Readout is repeatable, immutable with respect to its source, free of
mutable aliasing and unable to feed back into morphology.

Only six inherited dispatch examples are invoked: su, kṛ, krī, brū, ṛ and
rudh. These are small integration checks, not a replay of their stage
certificates. No untouched operator-engine suite or companion theorem
certificate was run. Hosted CI and main merging remain deferred.

The 24 new exact-word evidence gaps and seven inherited gaps remain
explicit. Literal membership, source/rule evidence and software agreement
are distinct claims. The report establishes only the declared finite
contracts; full grammar validity, native operator lifting, typed
zero-specialization compatibility and quantum-calculator integration remain
open.
