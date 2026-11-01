# The Ṛ-Stem (tṛc) Sup Paradigm Compiled — kartṛ and the agent nouns, with sarvanāmasthāna load-bearing

1 November 2026. theorum/65 had the ṛ-stem in two cells (savitā, savituḥ).
This capsule gives the whole masculine tṛc paradigm from the quoted sūtras
on theorum/82's it-layer, with kartṛ as the oracle, and declines the four
other agent nouns that theorum/89 built from the pinned roots.

## 1. Sources (quoted)

```text
1.1.42  śi sarvanāmasthānam ; 1.1.43 suḍ anapuṁsakasya          7.1.94  ṛd uśanaspurudaṁso 'nehasāṁ ca (anaṅ) ; 1.1.53 ṅic ca
6.4.8   sarvanāmasthāne cāsambuddhau                               6.4.11  aptṛntṛcsvasṛnaptṛneṣṭṛtvaṣṭṛkṣattṛhotṛpotṛpraśāstṝṇām
7.3.110 ṛto ṅi sarvanāmasthānayoḥ ; 1.1.51 ur aṇ raparaḥ           6.1.111 ṛta ut ; 8.2.24 rāt sasya
6.1.102 prathamayoḥ pūrvasavarṇaḥ ; 6.1.103 tasmāc chaso naḥ puṁsi  6.1.77 iko yaṇ aci
7.1.54  hrasvanadyāpo nuṭ ; 6.4.3 nāmi ; 8.4.1 raṣābhyāṁ no ṇaḥ samānapade (+ vārttika ṛvarṇāc ca)
6.1.68 ; 8.2.7 nalopaḥ prātipadikāntasya ; 8.3.57 / 8.3.59 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9
```

## 2. Results

**T1 kartṛ.** kartā, kartārau, kartāraḥ; kartāram, kartārau, kartṝn; kartrā,
kartṛbhyām, kartṛbhiḥ; kartre, …; kartuḥ, …; kartuḥ, kartroḥ, kartṝṇām; kartari,
kartroḥ, kartṛṣu; he kartaḥ — 22/22. Each stage breaks exactly its cells:
the **sarvanāmasthāna saṁjñā** (1.1.42–43) {1s, 1d, 1p, 2s, 2d, 8s}; 7.1.94
{1s}; 7.3.110 {1d, 1p, 2s, 2d, 7s, 8s}; 6.4.11 {1d, 1p, 2s, 2d} (not 8s:
*asambuddhau*); 6.4.8 and 8.2.7 {1s}; 6.1.111 and 8.2.24 {5s, 6s}; 6.1.102
{2p}; 7.1.54, 6.4.3, 8.4.1 {6p}; 8.3.59 {7p}.

**T2 The agents.** śrotṛ, hotṛ, cetṛ, sotṛ (theorum/89, from śru, hu, ciñ,
ṣuñ by tṛc with theorum/80's guṇa) give 88 forms equal to the exchanged
paradigm (hotṝṇām, cetāraḥ, sotṛṣu …).

## 3. Certificate

```text
python -m proof_lab.r_stem_sup_compiled
python -m unittest proof_lab.test_r_stem_sup_compiled -v
```
Status `PASS_R_STEM_SUP_COMPILED_CANDIDATE`, SHA-256
`81f511f69ff7fbb714257449fa620d440b31fdc85345e44eb7b9f958ef447dcd`
(`proof_lab/R_STEM_SUP_COMPILED_EXPECTED.sha256`). Imports theorum/82, 89.

## 4. Claim boundary

```text
kartṛ: 22 FORMS; SARVANĀMASTHĀNA AND EACH STAGE BREAK EXACTLY THEIR CELLS        PROVED
śrotṛ hotṛ cetṛ sotṛ: 88 FORMS                                                   PROVED
KINSHIP ṛ-STEMS (pitṛ), 6.4.11's OTHER MEMBERS, NEUTERS                           NOT CLAIMED
8.4.1 ON ṛ-VARṆA                                                                 VĀRTTIKA, CITED
STAGE ORDER                                                                      DECLARED PIPELINE
RH, YM                                                                           UNTOUCHED
```
