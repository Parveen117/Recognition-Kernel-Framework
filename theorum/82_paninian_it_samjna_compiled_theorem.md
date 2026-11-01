# The It-Saṁjñā Layer Compiled — 1.3.2–1.3.9 as one interpreter, augment placement by marker, the aṅga

1 November 2026. Second batch of the all-sūtra programme (ledger:
[ASTADHYAYI_LEDGER.md](../proof_lab/astadhyayi/ASTADHYAYI_LEDGER.md)).
theorum/58 and theorum/63 each hand-wrote an `it_lopa` for the affixes they
needed; theorum/80's compiled rules read markers (śit, kit, ṭit) from the
memory channel without saying where the markers come from. This capsule
compiles the marker layer itself from the quoted sūtras, on IAST teaching
forms (upadeśa), and certifies that the hand-coded functions are instances
of it, that the exceptions Pāṇini states are each load-bearing on named
forms, and that the augment placement and the aṅga are read off the same
markers.

## 1. Sources (quoted)

```text
1.3.1    bhūvādayo dhātavaḥ                          bhū and the rest are dhātu
1.3.2    upadeśe 'janunāsika it                      in the teaching form a nasal vowel is an it
1.3.3    halantyam                                   a final consonant is an it
1.3.4    na vibhaktau tusmāḥ                         not, in a vibhakti, a ta-varga sound, s or m
1.3.5    ādir ñiṭuḍavaḥ                              initial ñi, ṭu, ḍu (of a dhātu) are it
1.3.6    ṣaḥ pratyayasya                             initial ṣ of an affix is an it
1.3.7    cuṭū                                        initial ca-varga / ṭa-varga sound of an affix is an it
1.3.8    laśakv ataddhite                            initial l, ś, ka-varga sound of a non-taddhita affix is an it
1.3.9    tasya lopaḥ                                 the it is elided
1.1.60   adarśanaṁ lopaḥ                             elision is non-appearance
1.1.46   ādyantau ṭakitau                            a ṭ-marked augment is prefixed, a k-marked one suffixed
1.1.47   mid aco 'ntyāt paraḥ                        an m-marked augment goes after the last vowel
3.1.1    pratyayaḥ ; 3.1.2 paraś ca                  (adhikāra) ... is an affix, and it comes after
1.4.13   yasmāt pratyayavidhis tadādi pratyaye 'ṅgam from the item conditioning the affix up to the affix: aṅga
6.4.1    aṅgasya                                     (adhikāra) of the aṅga
1.4.104  vibhaktiś ca                                sup and tiṅ are also vibhakti
```

Jñāpaka exceptions, declared from the sūtras the tradition reads them off:
**7.1.3** *jho 'ntaḥ* (jh of jha/jhi is not an it), **7.3.50** *ṭhasyekaḥ*
(ṭh of ṭhak/ṭhañ is not), **7.1.2** *āyaneyīnīyiyaḥ phaḍhakhacchaghāṁ
pratyayādīnām* (ch, ḍh of cha/ḍhak are not). Cited, not compiled: **6.1.64**
*dhātvādeḥ ṣaḥ saḥ*, **6.1.65** *ṇo naḥ* (dhātu-initial ṣ, ṇ are replaced,
not elided). The *u* of tuk, num, matup, ṇamul, tumun, suṭ, yāsuṭ, muk is
the anunāsika pronunciation vowel of the upadeśa and falls under 1.3.2; so is the
vowel of each lakāra (la~ṭ, li~ṅ …), whose *l* is the affix itself that **3.4.77**
*lasya* replaces — 1.3.8 cannot take it, since an affix must leave a remainder
(correction after external review of the first pinned run, f66f651b…6dc,
which had listed the *l* as an it).

## 2. The interpreter

`its(upadeśa, kind ∈ {pratyaya, dhātu, āgama}, vibhakti, taddhita)`: 1.3.2
marks every nasal vowel; 1.3.3 marks the final consonant unless 1.3.4
(vibhakti and the consonant in ta-varga ∪ {s, m}); 1.3.5 marks an initial
ñi/ṭu/ḍu of a dhātu; for an affix, 1.3.6 marks an initial ṣ, 1.3.7 an initial
ca-/ṭa-varga sound (minus the jñāpaka table), 1.3.8 an initial l/ś/ka-varga
sound unless taddhita; 1.3.9 removes the marked sounds and keeps them as the
recorded its (theorum/58's memory channel, 1.1.62).

## 3. Results

### T1 One interpreter reproduces the tradition on 116 teaching forms

On the 21 sup (+ sambodhana), 18 tiṅ, 10 lakāras, the vikaraṇas, 25 kṛt and
taddhita affixes, 13 dhātus and 8 augments listed in the certificate, the
compiled it-set **and** remainder equal the traditional ones (Siddhānta-
kaumudī listings) on every form. The exceptions are each load-bearing
exactly where Pāṇini puts them: dropping 1.3.4 changes exactly the vibhaktis
with a ta-varga/s/m final (`am, tas, thas, mas, jas, śas, bhis, bhyas, bhyām,
ṅas, os, ām, vas, dhvam, thās, ātām, āthām`); dropping *ataddhite* changes
exactly `kha, gha, kan`; treating a dhātu as an affix changes exactly
`ṣṭhā, ṇīñ, gamḷ~, ḍukṛñ, ḍudāñ, ṭunadi~, ṭuvepṛ~, ñimidā~`; dropping the
jñāpaka overrides changes exactly `jhi, jha, ṭhak, ṭhañ, cha, ḍhak`; the
remainder guard on 1.3.8 is what keeps the *l* of the ten lakāras.

### T2 The hand-coded lopa functions are instances

theorum/58's `it_lopa` on gam+śap+tip and nī+śap+tip equals the compiled
1.3.9 on śap (`ś` 1.3.8, `p` 1.3.3) and tip (`p` 1.3.3) in phones and in
recorded its; theorum/63's `it_lopa` equals it on all 22 sup entries.

### T3 Augment placement and the aṅga are read off the markers

1.1.46/1.1.47 from the its alone: tuk after (`a + tuk → at`), aṭ/āṭ/iṭ before
(`aṭ + gam → agam`, `iṭ + tā → itā`), num after the last vowel (`bhavat + num
→ bhavant`). 1.4.13 gives the aṅga of an affix as the prefix of the word
before it; on **all 40 reachable states** of theorum/60's gam/nī graph the
trigger of theorum/80's compiled 7.3.84 equals "aṅga(affix) ends in ik and
the affix is sārvadhātuka/ārdhadhātuka", and 3.1.2 holds on every state.

## 4. Certificate

```text
python -m proof_lab.paninian_it_samjna_compiled
python -m unittest proof_lab.test_paninian_it_samjna_compiled -v
```
Status `PASS_PANINIAN_IT_SAMJNA_COMPILED_CANDIDATE`, SHA-256
`094d38e1fcb4b3cd97bba95ca066472af05719f4f4045f9c0a45b643db8665cf`
(`proof_lab/PANINIAN_IT_SAMJNA_COMPILED_EXPECTED.sha256`). Consumes
theorum/58's words and `it_lopa`, theorum/63's `SUP` and `it_lopa`,
theorum/60's `explore`, theorum/79's vargas, theorum/80's pratyāhāra
expansion. Exact; no floating point, no Hilbert structure.

## 5. Claim boundary

```text
1.3.2–1.3.9 ONE INTERPRETER = TRADITION ON 116 FORMS                          PROVED
1.3.4, ataddhite, pratyayasya, JÑĀPAKA OVERRIDES EACH LOAD-BEARING, NAMED FORMS PROVED
theorum/58, 63 it_lopa ARE INSTANCES (śap, tip; 22 sup)                       PROVED
1.1.46 / 1.1.47 PLACEMENT FROM ITS; 1.4.13 AṄGA = 7.3.84 TRIGGER ON 40 STATES  PROVED
JÑĀPAKA EXCEPTIONS                                                            DECLARED FROM 7.1.3 / 7.3.50 / 7.1.2, NOT DERIVED
6.1.64 / 6.1.65 (dhātu-initial ṣ, ṇ)                                          CITED
ir-it (vārttika), ACCENT ITS 1.3.12 / 1.3.72, WHOLE DHĀTUPĀṬHA                NOT ON THE CARRIER
LEDGER AFTER THIS BATCH: 171 OF 3959 (10 compiled, 46 meta, 70 hand-coded, 43 cited)  CLAIM BOUNDARY, NOT COVERAGE
RH, YM                                                                        UNTOUCHED
```
