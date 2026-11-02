# PG13 — Causative presents with owned root constituents

Author: Monty. 2 November 2026.

PG13 develops **12 identified roots / 12 parasmaipada paradigms / 108
causative present cells**. It uses the useful derivation pattern in
the theorem branch's T105 as a starting point, binds explicit lexical identities and
primary sources, and extends the three displayed cells per root to all
nine person-number cells. The implementation retains root substitutions,
augment ownership and the composite ṇijanta dhātu.

| Root | Lexical ID | Third-person singular | New operation or distinction |
| --- | --- | --- | --- |
| bhū | 1010001 | bhāvayati | ū → au → āv, then separate ṇic i → e → ay |
| kṛ | 1080010 | kārayati | Vṛddhi with retained r accompaniment |
| nī | 1011049 | nāyayati | Root y and ṇic y retain different owners |
| hṛ | 1011046 | hārayati | Vṛddhi with retained r accompaniment |
| pac | 1011151 | pācayati | Penultimate-a vṛddhi |
| gam | 1011137 | gamayati | Intermediate gām, then licensed mit shortening |
| sthā | 1011077 | sthāpayati | Root-final puk |
| dā | 1030010 | dāpayati | Root-final puk; no simple-present reduplication |
| pā, drinking | 1011074 | pāyayati | Yuk defeats puk; protecting pā is excluded |
| vid, knowing | 1020059 | vedayati | Guṇa before actual ṇic |
| budh, understanding | 1040068 | bodhayati | Original A root, licensed causative P; 1.3.86 |
| kṛṣ | 1060006 | karṣayati | Guṇa with retained r accompaniment |

Every request supplies the exact listed root meaning, an independent
prayojaka causative license and a contextual parasmaipada license. The
adapter does not infer these licenses from spelling. Original-root pada
and gaṇa remain source facts; they are not copied onto the derived dhātu
to select its endings or vikaraṇa. Ātmanepada, prefixed and nested
causatives remain outside this packet.

## Owned construction

The root and ṇic keep separate teaching forms and sound identities. Puk
and yuk are separate augments and final members of the root constituent
under 1.1.46. Their **k is an it marker; u is pronunciation-only**, following
the selected Bālamanoramā. No nasal u is invented and no 1.3.2 operation is
applied to that u.

3.1.32 designates the full root constituent plus ṇic as a derived dhātu.
Śap is prescribed after that composite. Its guṇa query targets the final
i owned by ṇic, after which e → ay is recorded. The earlier root changes
and any augment remain unchanged. Ending substitution, final-a lengthening,
junction and pause readout then complete the word.

The [finite construction contract](CONTRACT.md) gives the stage domains,
ownership argument and boundaries. This is a linguistic adapter; full
native operator lifting and typed zero-specialization compatibility remain
open.

## Evidence and coverage

[Validation](VALIDATION.md) records **11 literal-word cases, 31 expected
refusals and 74 direct controls**, plus a separate **108-cell comparison
with zero differences**. The **36 T105 expected examples** also agree;
these are companion expectations, not independent primary evidence.
Kṛṣ 1060006 has lexical/rule evidence and comparison agreement but no
separate exact-word witness in the selected primary passages.

[Coverage](COVERAGE_STATUS.json) keeps PG12's **228 simple-present roots /
2,610 cells** unchanged and records the **108 causative cells separately**.
There are **2,718 cells when formation is included in the cell identity**.
The 12 causative roots must not be added to 228 as if they were all new
simple-present entries. PG4–PG13 contain 223 bounded definitions / 161
distinct sūtra IDs, without an overall grammar-completion percentage.

[Concurrent review](CONCURRENT_REVIEW.json) records the T89 repair as
statically confirmed: all eight stage-removal keys are now active, and
`trc_agent` rejects unadmitted IDs. It also records the T105 pronunciation
distinction and a T107 final-l citation correction. No companion suite or
certificate was replayed, and no companion runtime dependency was added.

## Run locally

Use the primary checkout pinned in [SOURCE_PINS.json](SOURCE_PINS.json):

```sh
python3.12 -m research.panini_grammar.causative_present.verify \
  --source-root /path/to/ashtadhyayi-data

python3.12 -m research.panini_grammar.causative_present.cli \
  --source-root /path/to/ashtadhyayi-data \
  --lexical-id 1011074 --sense 'पाने' --pada P \
  --pada-licensed --causative-licensed --all-forms
```

`--trace` exposes the retained derivation. The verifier's `--write` option
updates only PG13's result and coverage files. Ordinary `Request` objects
continue through PG12; `CausativeRequest` selects this new formation.

PG1–PG12 remain frozen. [Remaining work](REMAINING.md) includes further
causative exceptions, semantic pada contexts, other formation families
and native integration. Hosted CI and main merging remain deferred.
