# Source Repairs to Theorems 119–120 (the PG17 companion review): candidate vs licensed histories, 7.2.15 as a prohibition, the initial-k marker under 1.3.8, the exact 7.3.52 guard, and the admissible-sense relation

2 November 2026. Additive. Resolves C2 – C5 of
`research/panini_grammar/future_extension/COMPANION_REVIEW.md` (PG17) in
place; theorum/119 and 120 are not edited, their earlier statements are
withdrawn **here** with the correct witness, and the quotation check
(`research/samasa_construction/verify_quotes.py`) covers this capsule.
Nothing was already fixed in an earlier commit: C2 – C5 are first
addressed in this packet.

---

## 1. C2 — an unresolved order is a candidate, not a licensed option

theorum/119 §3 kept both orders of a 2.2.33-vs-2.2.34 pair "as labelled
branches until a source is pinned". That sentence conflated two statuses.
The construction now has **three** output channels, as PG17 N4 provides
for the verbal carrier:

```
LICENSED   : a terminal history whose every event carries positive source evidence
             (a quoted clause, or a quoted vā / vibhāṣā / anyatarasyām for an optional branch)
CANDIDATE  : a history admitted by the guard but with one event whose source decision is open
             (an unpinned conflict, an unpinned gaṇa membership, an unpulled sandhi clause)
EXCLUDED   : a history refused by a quoted prohibition (na, or a sense guard that fails)
```

The printed-word *set* of theorum/118 D4 is the image of the LICENSED
channel only. A 2.2.33 / 2.2.34 pair without a pinned conflict example
therefore yields **one** licensed order only if one clause applies, and
**two candidates** (neither licensed) if both apply — never "two licensed
alternatives", because a licensed option needs a quoted option word and
2.2.30 – 2.2.38 contain none for that pair. The same applies to every
"open" row of theorum/119 §7 and theorum/120 §5 (goda, duṣkara's ṣ,
lagna's s, śiṣya's ṣatva, śreṣṭha's order, …): those forms are
**candidates with an open obligation**, printed as attested forms of the
commentary, not licensed outputs of the construction. theorum/119 §6.6's
pair stokānmukta / stokādmukta is licensed on both branches because
8.4.45 carries *vā* — the contrast the review asked for.

---

## 2. C3 — 7.2.15 *yasya vibhāṣā* is a prohibition, not a root

theorum/120 K21 read 7.2.15 as a root *yas* with {yastaḥ, yasitaḥ}. That
reading is **withdrawn**. The pinned clauses:

> 7.2.14 *śvīdito niṣṭhāyām* ; 7.2.15 *yasya vibhāṣā* ; 7.2.16 *āditaś ca* ; 7.2.17 *vibhāṣā bhāvādikarmaṇoḥ*

7.2.14 withholds iṭ before niṣṭhā from śvi and īdit roots; 7.2.15
continues the prohibition: *yasya* is the relative "of which [root]" —
**a root for which iṭ has been taught as optional** (7.2.44 *svaratisūti-
sūyatidhūñūdito vā*, 7.2.56 *udito vā*, 7.2.59 *na vṛdbhyaś caturbhyaḥ*
and their context) **takes no iṭ before niṣṭhā**; 7.2.16 adds the ādit
roots; 7.2.17 reopens the option only in bhāva and ādikarman. Kāśikā's
witnesses (commentary): *vidhūtaḥ / vidhūtavān* (dhūñ, optional iṭ by
7.2.44 → none in niṣṭhā), *gūḍhaḥ* (guh, ūdit), *vṛddhaḥ* (vṛdh of the
7.2.59 group), with its own qualification on *patita*.

Consequence for the iṭ table of theorum/120 D3: the niṣṭhā column is

```
root class                                    iṭ before kta / ktavatu          clause
seṭ (udātta-upadeśa), not in the lists        yes                              7.2.35
aniṭ (anudātta-upadeśa)                        no                               7.2.10
śvi, īdit                                      no                               7.2.14
roots with an OPTIONAL iṭ elsewhere (7.2.44 …) no                               7.2.15   ← the repaired row
ādit                                           no                               7.2.16
the two rows above, in bhāva / ādikarman       optional                         7.2.17
```

and the K21 line *yastaḥ / yasitaḥ* has **no witness** and is struck;
the *svinnam / sveditam* cell stands (7.2.16 + 7.2.17). The same row is
the boundary with PG17: a root's *future* iṭ option (sya / tās) does not
carry into niṣṭhā — 7.2.15 says the opposite — so no global "veṭ" flag
is admitted in either lane.

---

## 3. C4 — two marker guards with exact ownership

**3.1 The initial k of kta / ktavatu.** theorum/120 L3 cited 1.3.3
*halantyam* for the k of kta. 1.3.3 names a **final** consonant of the
teaching form; the k of *kta* is **initial**. The witness is

> 1.3.8 *laśakv ataddhite*

(initial l, ś and the ku-class are its in a non-taddhita affix; Kāśikā's
examples under it include bhukta / bhuktavat). theorum/82's `its` already
returns `{"k": "1.3.8"}` for *kta* (it did so for śatṛ's ś, tral's l,
ṇvul's l in theorum/107 / 113); the error was in the written witness, not
in the reading function. Corrected: kta is kit **by 1.3.8**, hence 1.1.5.

**3.2 The guard of 7.3.52.** theorum/120 D3 / L5 stated the ku of 7.3.52
for "ghit / ṇit / ṇyat". The pinned clause is

> 7.3.52 *cajoḥ ku ghiṇṇyatoḥ*

— **ghit or ṇyat**, two named conditions; there is no generic ṇit
condition. The expansion would have turned the c of *pac* into k before
the ṇit ṇvul and produced **pākaka* instead of theorum/107's certified
*pācakaḥ*; theorum/107's code applied ku only under `ghit` (its docstring
"c / j → k / g before ghañ (ghit)") and so was never wrong — the written
guard in 120 was. Corrected row of D3:

```
ghit (ghañ, gha) or ṇyat + root in c / j   →   ku   (7.3.52; exceptions 7.3.53–69)      pāka, tyāga, yoga, bhogya, vākya
ṇit (ṇvul, ṇini, aṇ)                       →   vṛddhi only (7.2.115 / 116), NO ku        pācaka, grāhī, kumbhakāra
```

This keeps the two marker classes separate in any shared adapter, which
is the review's point for the ṇic lane as well.

---

## 4. C5 — the sense is an admissible relation, selected by the frame

theorum/120 L1 said the certified affixes "required no declared σ". The
precise statement, replacing it:

> For each affix the text supplies an **admissible-sense relation**
> `ADM(α) ⊆ Senses` (D2 of 120: kta ∈ {bhāva, karman, kartṛ (3.4.71 / 72),
> adhikaraṇa (3.4.76)}, lyuṭ ∈ {bhāva, karaṇa, adhikaraṇa}, ghañ ∈ {bhāva,
> non-agent kāraka in a name}). The **selected** sense is an input from the
> completed meaning-to-form frame F (PG14 S2): the affix string does not
> choose it, and a word printed once may be the image of several
> histories differing only in σ ∈ ADM(α) (theorum/120 K13).

So "no declared σ" was true only in the weak sense that the certified
packets fixed σ by their claim boundary (kta as bhāva / karman in 86,
tavya as bhāva / karman in 100, lyuṭ as bhāva in 107); it is not a
property of the affixes. Several labelled interpretations of one printed
word are **not** several optional forms of one sense — the former lives
in F, the latter in the LICENSED channel of §1. theorum/121's D2 table is
already stated as a relation ("σ is an input"), so no repair is needed
there.

---

## 5. What stands, what is withdrawn

| statement | status |
|---|---|
| theorum/119 §3 "both orders retained as labelled branches" | re-typed: CANDIDATE, not licensed (§1) |
| theorum/119 §7 / 120 §5 "open" forms | CANDIDATE channel, attested by commentary (§1) |
| theorum/120 K21 *yastaḥ / yasitaḥ* | **withdrawn**; 7.2.15 is a prohibition (§2) |
| theorum/120 L3 "k it 1.3.3" | corrected to 1.3.8 (§3.1) |
| theorum/120 D3 / L5 "ghit / ṇit / ṇyat" | corrected to ghit / ṇyat (§3.2); theorum/107's certificate unaffected |
| theorum/120 L1 "no declared σ" | replaced by the admissible-sense relation (§4) |
| theorum/119 §6.6 stokānmukta / stokādmukta | stands, both branches licensed by 8.4.45's *vā* |

---

## A. Sources (quoted from the pinned sūtrapāṭha; IAST by the ledger's transliteration)

```text
7.2.14 śvīdito niṣṭhāyām · 7.2.15 yasya vibhāṣā · 7.2.16 āditaśca · 7.2.17 vibhāṣā bhāvādikarmaṇoḥ · 7.2.44 svaratisūtisūyatidhūñūdito vā · 7.2.56 udito vā · 7.2.59 na vṛdbhyaścaturbhyaḥ · 7.2.35 ārdhadhātukasyeḍ valādeḥ · 7.2.10 ekāca upadeśe'nudāttāt
1.3.3 halantyam · 1.3.8 laśakvataddhite · 1.1.5 kṅiti ca · 7.3.52 cajoḥ ku ghiṇṇyatoḥ · 7.2.115 aco ñṇiti · 7.2.116 ata upadhāyāḥ · 1.4.2 vipratiṣedhe paraṁ kāryam · 2.2.33 ajādyadantam · 2.2.34 alpāctaram · 8.4.45 yaro'nunāsike'nunāsiko vā
```

Commentary (marked): Kāśikā on 7.2.15 (vidhūta, gūḍha, vṛddha; patita), on 1.3.8 (bhukta, bhuktavat), on 7.3.52. The review is `research/panini_grammar/future_extension/COMPANION_REVIEW.md`.
