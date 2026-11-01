# The Tripādī Niṣṭhā Rules Compiled in Asiddha Order — Theorem 86's four refusals realized, 8.2.1 load-bearing

1 November 2026. theorum/86 refused pac, labh, tud and lū by name because
pakta, labdha, tunna and lūna need rules of the Tripādī. This capsule
realizes those rules and applies them the way 8.2.1 prescribes — in sūtra
order, each rule seeing only what the earlier ones produced — and shows on
labdha that this order is not decoration.

## 1. Sources (quoted)

```text
8.2.1   pūrvatrāsiddham                          (adhikāra) what follows is as if not done for what precedes
8.2.30  coḥ kuḥ                                  a ca-varga sound becomes its ka-varga sound
8.2.40  jhaṣas tathor dho 'dhaḥ                  after gh jh ḍh dh bh, the t / th of an affix becomes dh
8.2.42  radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ   after r / d the niṣṭhā t becomes n, and a preceding d too
8.2.44  lvādibhyaḥ                               after lū and the lvādi roots (t → n)
8.4.53  jhalāṁ jaś jhaśi                         a jhal becomes jaś before a jhaś
1.1.26  ktaktavatū niṣṭhā
Pinned Dhātupāṭha entries (PG5): 1011151 डुपचँष्, 1011130 डुलभँष्, 1060001 तुदँ, 1090016 लूञ्
```

## 2. Results

**T1 The four nouns.** From the pinned teaching forms through theorum/82's its:
pac + ta → **pakta** (8.2.30); labh + ta → **labdha** (8.2.40, then 8.4.53);
tud + ta → **tunna** (8.2.42, both clauses); lū + ta → **lūna** (8.2.44).

**T2 8.2.1 is load-bearing.** With the five rules applied in reverse order,
labh + ta stays *labhdha*: 8.4.53 finds no voiced stop to act before, and is
then "not done" for the dh that only 8.2.40 creates. The other three
derivations are order-independent on their inputs. The lawful order is the
sūtra order.

**T3 88 sup forms.** theorum/63's pinned ladder derives all 22 forms of each
of the four nouns.

## 3. Certificate

```text
python -m proof_lab.tripadi_nishtha_compiled
python -m unittest proof_lab.test_tripadi_nishtha_compiled -v
```
Status `PASS_TRIPADI_NISHTHA_COMPILED_CANDIDATE`, SHA-256
`8b8f597b42a56b26a643e5359c3ca6dad036bcc100ee1305dfa62de0324426c9`
(`proof_lab/TRIPADI_NISHTHA_COMPILED_EXPECTED.sha256`). Imports theorum/82,
86 (entry loader), 63, 79; no pin is changed.

## 4. Claim boundary

```text
pakta, labdha, tunna, lūna FROM THE PINNED TEACHING FORMS BY 8.2.30 / 8.2.40 + 8.4.53 / 8.2.42 / 8.2.44   PROVED
8.2.1 LOAD-BEARING ON labdha (REVERSE ORDER → labhdha), OTHERS ORDER-INDEPENDENT                          PROVED
88 SUP FORMS BY theorum/63's PINNED LADDER                                                                PROVED
8.2.1 IN GENERAL; 6.4.22; THE REST OF THE TRIPĀDĪ                                                         NOT CLAIMED
LVĀDI GAṆA BEYOND lū; 8.2.30 AT PADA END                                                                  NOT CLAIMED
ANIṬ STATUS                                                                                               DECLARED
RH, YM                                                                                                    UNTOUCHED
```
