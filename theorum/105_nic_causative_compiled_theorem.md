# ṇic Causatives Compiled — 3.1.26 hetumati ca on twelve roots in laṭ (7.2.115 / 7.2.116 vṛddhi, 6.4.92 mitāṁ hrasvaḥ, puk / yuk, 7.3.86 laghūpadha guṇa, 7.3.84 + 6.1.78 before śap)

2 November 2026. The first derived-root (sanādyanta) theorem. Twelve roots
take ṇic and are conjugated in laṭ parasmaipada (3s, 3p, 1s): 36 forms, each
rule shown load-bearing on exactly the forms it governs.

## 1. Sources (quoted)

```text
3.1.26 hetumati ca   3.1.32 sanādyantā dhātavaḥ   1.3.3 / 1.3.7 / 1.3.9 (ṇic → i)
7.2.115 aco ñṇiti   7.2.116 ata upadhāyāḥ   6.4.92 mitāṁ hrasvaḥ (gaṇasūtra janī-jṝṣ-knasu-rañjo 'mantāś ca)
7.3.36 artihrīvlīrīknūyīkṣmāyyātāṁ puṅ ṇau   7.3.37 śācchāsāhvāvyāvepāṁ yuk   7.3.86 pugantalaghūpadhasya ca   1.1.51 ur aṇ raparaḥ
3.1.68 kartari śap   3.4.113   1.3.78   7.3.84 sārvadhātukārdhadhātukayoḥ   6.1.78 eco 'yavāyāvaḥ
3.4.78   7.1.3 jho 'ntaḥ   6.1.97 ato guṇe   7.3.101 ato dīrgho yañi   1.4.13
```

## 2. Results

**T1.** bhāvayati (bhau → bhāv by 6.1.78 before ṇic's i), kārayati, nāyayati,
hārayati (7.2.115, 1.1.51), pācayati (7.2.116), gamayati (7.2.116 then 6.4.92
on the mit root), sthāpayati, dāpayati (7.3.36 puk), pāyayati (7.3.37 yuk),
vedayati, bodhayati, karṣayati (7.3.86, 1.1.51) — each in 3s / 3p / 1s: 36/36.
Without 7.2.115 exactly the 12 forms of bhū, kṛ, nī, hṛ break; 7.2.116 the 3
of pac; 6.4.92 the 3 of gam; 7.3.36 the 6 of sthā, dā; 7.3.37 the 3 of pā;
7.3.86 the 9 of vid, budh, kṛṣ; 1.1.51 the 9 of kṛ, hṛ, kṛṣ; 7.3.84 and 6.1.78
all 36; 7.1.3 and 6.1.97 the twelve 3p; 7.3.101 the twelve 1s.

## 3. Certificate

```text
python -m proof_lab.nic_causative_compiled
python -m unittest proof_lab.test_nic_causative_compiled -v
```
Status `PASS_NIC_CAUSATIVE_COMPILED_CANDIDATE`, SHA-256 `c194911675d12b32db4c70365d36cdfc522253b94ac3f3a398d236726c307c03`
(`proof_lab/NIC_CAUSATIVE_COMPILED_EXPECTED.sha256`). Imports theorum/80, 82.

## 4. Claim boundary

```text
36 CAUSATIVE FORMS; EACH RULE BREAKS EXACTLY THE FORMS STATED                        PROVED
mit STATUS OF gam (gaṇasūtra), THE ROOT LISTS OF 7.3.36 / 7.3.37                   DECLARED
VṚDDHI OF ā (VACUOUS), ĀTMANEPADA, OTHER LAKĀRAS, 6.4.51 ṇer aniṭi, KṚT OF ṇijanta   NOT CLAIMED
RH, YM                                                                             UNTOUCHED
```
