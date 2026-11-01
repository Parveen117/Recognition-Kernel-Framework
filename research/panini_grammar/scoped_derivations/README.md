# PG4 — Executable inherited scopes and further root derivations

Author: Monty. 1 November 2026.

PG4 makes the scope review operational and extends the PG3 root pipeline.
Inherited terms now control whether a reviewed record can compile. The new
phonetic profile handles existing root nasals, tuk, ścutva/ṣṭutva with explicit
prohibitions, voicing, and the original-root domain of 8.2.78. Root sounds,
marker units, augmentation identities and ordered history remain available.

**Grammar is incomplete.** This is a source-reviewed linguistic adapter. The
canonical operator engine and quantum calculator are unchanged. The result
is not a new physical theorem, a general Sanskrit parser or a validity oracle.
Earlier PG1–PG3 and T81/T82 packets retain their original bytes.

## Inherited scope now affects execution

[scope.py](scope.py) parses all **3,983 source records**, **23,589 inherited
term annotations** and **9,653 padaccheda annotations**. It applies the six PG2
adjudications to their 346 flagged edges, plus a new commentary exclusion at
8.2.78. All raw terms, references and rejected components remain traceable.

| Policy | Affected raw edges | Effective view |
| --- | ---: | --- |
| 4.1.82 after 5.2.140 | 279 | Quarantine the inherited compound condition; do not infer uniform optionality or its opposite |
| 6.2.111 after 6.2.137 | 60 | Retain उत्तरपदस्य; exclude the expired आदि component |
| 6.1.135 through 6.1.157 | 3 | Accept the longer commentary-supported endpoint |
| 6.1.84 through 6.1.111 | 2 | Accept the longer ekādeśa scope |
| 4.2.92 at 4.3.23 | 1 | Accept the commentary's śeṣe heading despite the missing AD tag |
| अन्तः at 6.2.144 | 1 | Adopt source 6.2.143 while retaining the raw 6.2.14 reference |
| पदस्य at 8.2.78 | 1 | Exclude the publisher's inherited term under the adopted Tattvabodhinī reading |

The effective view has 23,309 inherited terms. This count describes the
adopted annotation view; it does not certify every unflagged inheritance.
The parser preserves 293 annotations whose additional fields it does not
interpret, including finite-verb annotations, and one nonstandard field layout
at 7.2.34. These are not 294 automatically diagnosed grammatical errors.

The [19 reviewed records](RULE_RECORDS.json) bind each own/inherited term to
its source and its explicitly reviewed role. Removing `धात्वादेः` from 6.1.65
or inherited `न` from 8.4.43 stops compilation. A record never imports a
source rule's whole action merely because it inherits one expression.
`कर्तरि` is a semantic condition, while `अचः` in 1.1.47 is partitive; neither
is assigned an action from its case number alone.

The input is the publisher's annotated padaccheda/anuvṛtti/adhikāra data.
**Raw Sanskrit scope inference remains open.**

## What the rule records do

| Records | Current executable or review role |
| --- | --- |
| 1.1.47 | Source-bound ordinary mit placement review; PG3 placement reused |
| 3.1.68 | Semantic śap candidate gate; competing vikaraṇas are not resolved |
| 6.1.64–65, 7.1.58 | Bind the inherited conditions of the reused PG3 root operations |
| 6.1.73–76 | tuk licensing and local alternatives, with the identified āṅ/māṅ prescription overriding the option |
| 7.3.84 | Source-bound domain review only; no new general guṇa derivation |
| 8.2.78 | Lengthen i/u/ṛ before original root-upadhā r/v followed by a consonant; preserve unsupported visibility/ḷ cases as unresolved |
| 8.3.24 | Read non-pada-final n or m as anusvāra before jhal, including existing root sounds |
| 8.4.40–44 | Palatal/retroflex contact substitutions and their three explicit prohibitions |
| 8.4.53 | Voicing before jhaś on the admitted sound table |
| 8.4.58 | Parasavarṇa before admitted varga sounds; semivowel and pada-final alternatives remain outside the profile |

Nineteen bound records do not mean nineteen universally completed sūtras.
Some reuse earlier operations, two are domain/placement reviews, and the śap
gate returns a candidate rather than a selected final affix.

In addition, [34 lexical witnesses](LEXICAL_WITNESSES.json) support withdrawal
of conditioned teaching retroflexion after the same initial ṣ has undergone
6.1.64. This is an attributed teaching convention, not a general inverse of
8.4.41 or a universal rule-rollback operation. Unknown lexical identities in
this context are refused. The ṣṭhivu exceptions remain unchanged.

## Derivation examples and blocked alternatives

| Supplied input | Earlier root state | Separate phonetic query | Relevant evidence |
| --- | --- | --- | --- |
| ष्टभिँ | stambh after source-supported dental restoration and num | stambh, with n → ṃ → m retained in history | 6.1.64, 7.1.58, 8.3.24, 8.4.58; Bālamanoramā 6.4.122 |
| ऋछँ | ṛtch, with tuk attached to the vowel's UID | ṛcch | 6.1.73, 8.4.40 |
| उछिँ | unch | uñch; num interrupts vowel–ch contact, so no tuk | Kāśikā 7.1.58's teaching-stage num; 8.3.24, 8.4.58 |
| टुमस्जोँ | masj | majj through maśj | 8.4.40, 8.4.53 |
| हुर्छाँ | hurch | hūrch | 8.2.78; the earlier root state stays hurch |
| Long pada-final vowel before ch | Supplied junction | Both tuk and no-tuk branches | 6.1.76 |
| Identified āṅ/māṅ before ch | Supplied identity and licensed sense | Mandatory tuk | 6.1.74, despite the later-numbered optional rule |
| प्रश्नः | Supplied local phonetic span | n retained after ś | 8.4.44 blocks the relevant 8.4.40 proposal |

All results are local stage readings. The supplied phonetic-span controls do
not derive their inputs or claim that the selected rules form an exhaustive
phonetic normalizer. Schematic nām/navati controls check the target sound
only; they do not assert complete ṣaṇṇām/ṣaṇṇavati derivations.

## Whole-witness root comparison

| Stage | Exact source-headword agreement | Different projection | Unresolved teaching convention |
| --- | ---: | ---: | ---: |
| PG2 marker-only | 1,703 | 524 | 2 |
| PG3 num phonetic query | 2,081 | 146 | 2 |
| PG4 admitted root/phonetic profile | **2,219** | **8** | **2** |

There are **138 additional agreements** and no lost agreements on this
witness. Thirty gaṇasūtra directives remain separate from the 2,229 roots.
This compares lexical spellings; it is not a percentage of Sanskrit grammar
verified, a complete derivation count or an independent correctness score.

[REMAINING.md](REMAINING.md) lists every remaining difference and the broader
grammar obligations. Nasal teaching flags and lexical classification are
supplied assumptions of the source audit, not independently established facts
for every entry. Expected headwords never enter the derivation API.

## Reproduce

Use the primary data checkout at `5744762f010d677cfb43f347a42d02796cf615d6`:

```sh
python3.12 research/panini_grammar/scoped_derivations/verify.py --source-root /path/to/ashtadhyayi-data
```

The default command reproduces [VERIFICATION_RESULT.json](VERIFICATION_RESULT.json).
`--write` writes only this stage's report. [VALIDATION.md](VALIDATION.md)
records 71 local cases, 52 structural controls, 167 literal citation checks
and the separately counted navigation checks. Eleven intentional unresolved
or partial fixture outcomes are reported explicitly.

See [SOURCE_REVIEW.md](SOURCE_REVIEW.md) for the new scope correction,
commentary attribution, restricted priority/visibility decisions and source
variants. CI and main-branch merging remain deferred.
