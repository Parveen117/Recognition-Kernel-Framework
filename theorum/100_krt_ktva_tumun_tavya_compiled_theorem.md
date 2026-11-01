# The Kṛt Affixes ktvā, tumun, tavya from the Pinned Roots — iṭ, guṇa and gam's nasal decided kit against non-kit; gantā realized

1 November 2026. Three kṛt affixes on six pinned roots, chosen so that every
decision is a contrast between a kit affix (ktvā) and the non-kit ones
(tumun, tavya): the iṭ (7.2.35 against 7.2.11), the guṇa (7.3.84 against
1.1.5), and the treatment of gam's nasal (6.4.37 against 8.3.24 / 8.4.58).
The last pair also realizes gantā, which theorum/97 had refused.

## 1. Sources (quoted)

```text
3.4.21 samānakartṛkayoḥ pūrvakāle   3.3.10 tumunṇvulau kriyāyāṁ kriyārthāyām   3.1.96 tavyattavyānīyaraḥ
7.2.35 ārdhadhātukasyeḍ valādeḥ     7.2.11 śryukaḥ kiti     7.2.10 ekāca upadeśe 'nudāttāt     1.1.5 kṅiti ca     7.3.84 ; 6.1.78
6.4.37 anudāttopadeśa… anunāsikalopo jhali kṅiti     8.3.24 naś cāpadāntasya jhali     8.4.58 anusvārasya yayi parasavarṇaḥ     1.2.46 ; 1.3.2–1.3.9
```

## 2. Results

**T1.** ktvā: bhūtvā, gatvā, kṛtvā, śrutvā, nītvā, hutvā; tumun: bhavitum,
gantum, kartum, śrotum, netum, hotum; tavya: bhavitavya, gantavya, kartavya,
śrotavya, netavya, hotavya — **18/18**. Removing 7.2.35 breaks exactly
bhavitum / bhavitavya; removing 7.2.11 exactly bhūtvā (it would take iṭ);
removing 1.1.5 exactly the five ik-final ktvā forms (*kartvā …); removing
7.3.84 exactly the ten ik-final tumun / tavya forms; 6.4.37 exactly gatvā;
8.3.24 and 8.4.58 exactly gantum / gantavya.

**T2.** gantā by 8.3.24 / 8.4.58 on theorum/97's 6.4.143 output.

## 3. Certificate

```text
python -m proof_lab.krt_ktva_tumun_tavya_compiled
python -m unittest proof_lab.test_krt_ktva_tumun_tavya_compiled -v
```
Status `PASS_KRT_KTVA_TUMUN_TAVYA_COMPILED_CANDIDATE`, SHA-256 `2f0229cf938ac80b60dc5e7b11904ede4275b8cb58eb8f3c52ab10cd6465ced9`
(`proof_lab/KRT_KTVA_TUMUN_TAVYA_COMPILED_EXPECTED.sha256`). Imports theorum/80, 82.

## 4. Claim boundary

```text
18 KṚT FORMS; EACH RULE BREAKS EXACTLY THE FORMS STATED (kit / non-kit CONTRASTS)   PROVED
gantā REALIZED (8.3.24 / 8.4.58)                                                     PROVED
bhū's seṭ STATUS DECLARED; lyap, anīyar, ṇvul, 7.2.56 OPTION, OTHER ROOTS            NOT CLAIMED
RH, YM                                                                              UNTOUCHED
```
