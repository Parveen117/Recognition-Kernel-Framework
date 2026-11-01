# Taddhita Affixes aṇ, iñ, yañ, ṭhak Compiled — first-vowel vṛddhi (7.2.117 / 7.2.118), the bha operations 6.4.146 / 6.4.148, ṭhasyekaḥ

2 November 2026. The secondary derivation. Eight classical derivatives from
declared prātipadikas: the affix is taken from the quoted sense sūtra, its
markers read by theorum/82, the vṛddhi of the first vowel computed by
theorum/80's antaratama, and the bha-operations of 6.4 applied — each rule
breaking exactly the derivations it governs.

## 1. Sources (quoted)

```text
4.1.76 taddhitāḥ   4.1.82 samarthānāṁ prathamād vā   4.1.83 prāg dīvyato 'ṇ   4.1.92 tasyāpatyam   4.1.95 ata iñ   4.1.105 gargādibhyo yañ   4.3.120 tasyedam
7.2.117 taddhiteṣv acām ādeḥ   7.2.118 kiti ca   6.4.146 or guṇaḥ   6.4.148 yasyeti ca   7.3.50 ṭhasyekaḥ   6.4.129 bhasya ; 1.4.18 yaci bham ; 6.1.78 ; 1.2.46 ; 1.3.2–1.3.9
```

## 2. Results

**T1.** upagu + aṇ → **aupagava** (7.2.117, 6.4.146, 6.1.78); kuru + aṇ →
**kaurava**; daśaratha + iñ → **dāśarathi** (7.2.117, 6.4.148); dakṣa + iñ →
**dākṣi**; garga + yañ → **gārgya**; śiva + aṇ → **śaiva**; buddha + aṇ →
**bauddha**; purāṇa + ṭhak → **paurāṇika** (7.2.118 for the kit affix, 7.3.50,
6.4.148) — 8/8. Removing 7.2.117 breaks the seven ñit / ṇit derivations and
7.2.118 exactly paurāṇika; 6.4.146 and 6.1.78 exactly the two u-stems; 6.4.148
exactly the six a-final bhas (including before yañ: the rule reads *taddhite*,
not a vowel-initial one); 7.3.50 exactly paurāṇika.

## 3. Certificate

```text
python -m proof_lab.taddhita_an_in_yan_compiled
python -m unittest proof_lab.test_taddhita_an_in_yan_compiled -v
```
Status `PASS_TADDHITA_AN_IN_YAN_COMPILED_CANDIDATE`, SHA-256 `b155be373ef472d8b22663dea569cb8e1b23b856db4bf9831a479cd6df170d60`
(`proof_lab/TADDHITA_AN_IN_YAN_COMPILED_EXPECTED.sha256`). Imports theorum/80, 82.

## 4. Claim boundary

```text
8 TADDHITA DERIVATIONS; EACH RULE BREAKS EXACTLY THE DERIVATIONS STATED                 PROVED
AFFIX CHOICE PER STEM DECLARED FROM THE SENSE SŪTRA / GAṆA (gargādi, purāṇa's ṭhak)    DECLARED
FEMININES, 1.1.73 vṛddha, EXCEPTIONS, DECLENSION                                       NOT CLAIMED
RH, YM                                                                                 UNTOUCHED
```
