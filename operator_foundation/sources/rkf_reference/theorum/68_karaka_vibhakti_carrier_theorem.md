# Kāraka → Vibhakti Carrier (1.4 + 2.3) — the form/meaning bridge, on the Gāyatrī

Carrier: sentence frame = verb (voice, person) + nominals with a semantic
relation. Layer 1, kāraka saṃjñā (1.4.24/32/42/45/49/54): relation → saṃjñā.
Layer 2, vibhakti-artha (2.3) under the **abhihita ledger**: 3.4.69 — the tiṅ
*expresses* the kartā in kartari, the karma in karmaṇi; 2.3.1 *anabhihite* —
a 2.3 kāraka-vibhakti applies only to a kāraka not already expressed; 2.3.2
dvitīyā, 2.3.18 tṛtīyā, 2.3.13, 2.3.28, 2.3.36, 2.3.46 prathamā, 2.3.50 ṣaṣṭhī
śeṣe; attribute agreement (samānādhikaraṇya) declared.
The abhihita ledger is the same two-channel shape as 1.1.62's memory: what the
tiṅ has expressed is invisible to the 2.3 rules.

## T1 Gāyatrī
```text
line 1  bhargas karma → 2 (2.3.2)   tad, vareṇya attr → 2   savitṛ, deva śeṣa → 6 (2.3.50)
        (vayam) kartā abhihita by dhīmahi (3.4.69) → NO pada
line 2  yad kartā abhihita → 1 (2.3.46)   dhī karma → 2   asmad śeṣa → 6
```
= exactly the vibhaktis the padas carry in theorum/63/65/67 (tat 2, savituḥ 6,
vareṇyam 2, bhargaḥ 2, devasya 6 | yaḥ 1, dhiyaḥ 2, naḥ 6). The text has no
"vayam" — and the ledger says why.

## T2 Voice switch
karmaṇi (*bhargaḥ dhīyate asmābhiḥ*): bhargas → 1 (2.3.46, abhihita), asmad →
3 (2.3.18). The ledger flips, the rules don't change.

## T3 2.3.1 load-bearing
Without the anabhihite guard the passive gives karma dvitīyā (\*bhargam) — refused.

## T4 Conflict-freeness
Exactly one 2.3 rule fires per nominal on all frames.

## What is input and what is derived — stated plainly
The semantic relations (who is agent/patient/śeṣa) are **input**, declared
from the traditional anvaya. What is derived: saṃjñā, abhihita status,
vibhakti, and the agreement between that and the actual padas. No meaning of
any word is claimed. This is the carrier on which the Mīmāṃsā layer (vidhi /
niṣedha / obligation) will sit.

## Certificate
```text
python proof_lab/karaka_vibhakti_carrier.py
python -m unittest proof_lab.test_karaka_vibhakti_carrier -v
```
`PASS_KARAKA_VIBHAKTI_CARRIER_CANDIDATE`, SHA-256 `d6f1a3fabb69b71c4888290a9b6f62c720522498fd7657795e6976e00d573fd3`.

## Claim boundary
```text
KĀRAKA + 2.3 UNDER ABHIHITA LEDGER = PADA VIBHAKTIS OF THE GĀYATRĪ        PROVED
IMPLICIT KARTĀ EXPRESSED BY tiṅ, NO PADA                                   PROVED
VOICE SWITCH FLIPS LEDGER; 2.3.1 LOAD-BEARING                              PROVED
SEMANTIC RELATIONS ARE INPUT (traditional anvaya)                          DECLARED
WORD MEANING; MĪMĀṂSĀ OBLIGATION; DVIKARMAKA; UPAPADA; SAMĀSA              NOT CLAIMED
RH, YM                                                                     UNTOUCHED
```
