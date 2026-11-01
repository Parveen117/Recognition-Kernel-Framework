# The Pronominal Adverbs Compiled

2 November 2026. tataḥ, tatra, tadā, yataḥ, yatra, yadā, kutaḥ, kutra, kadā, iha, ataḥ, atra, sarvataḥ, sarvatra, sarvadā by tasil / tral / dā / haḥ (5.3.7, 5.3.10, 5.3.15, 5.3.11) with 2.4.71, 7.2.102 + 6.1.97, 7.2.103, 7.2.104, 5.3.3, 5.3.5, 8.2.66 / 8.3.15. Each rule shown load-bearing on exactly the forms it governs (the certificate's `broken` record lists every ablation set).

## 1. Sources (quoted)

```text
1.1.38 taddhitaś cāsarvavibhaktiḥ
1.3.3 halantyam
1.3.8 laśakv ataddhite
2.4.71 supo dhātuprātipadikayoḥ
5.3.1 prāg diśo vibhaktiḥ
5.3.10 saptamyās tral
5.3.11 idamo haḥ
5.3.15 sarvaikānyakiṁyattadaḥ kāle dā
5.3.2 kiṁsarvanāmabahubhyo 'dvyādibhyaḥ
5.3.3 idama iś
5.3.5 etado 'n
5.3.7 pañcamyās tasil
6.1.97 ato guṇe
7.2.102 tyadādīnām aḥ
7.2.103 kimaḥ kaḥ
7.2.104 ku tihoḥ
8.2.66 sasajuṣo ruḥ
8.3.15 kharavasānayor visarjanīyaḥ
```

## 2. Results

- fifteen adverbs from six sarvanāma stems with tasil, tral, dā (and haḥ for idam) by 5.3.7 / 5.3.10 / 5.3.15 / 5.3.11 with 2.4.71, 7.2.102 + 6.1.97, 7.2.103, 7.2.104, 5.3.3, 5.3.5, 8.2.66, 8.3.15; each rule breaks exactly the words stated

## 3. Certificate

```text
python -m proof_lab.pronominal_taddhita_adverbs_compiled
python -m unittest proof_lab.test_pronominal_taddhita_adverbs_compiled -v
```
Status `PASS_PRONOMINAL_TADDHITA_ADVERBS_COMPILED_CANDIDATE`, SHA-256 `ca3e9059981c53bf1c444a1f33e61913847fa71a0ab0f9341a606e3c5d8033b2` (`proof_lab/PRONOMINAL_TADDHITA_ADVERBS_COMPILED_EXPECTED.sha256`).

## 4. Claim boundary

PROVED: as in §2.

NOT CLAIMED:
- the i of tasil is read as uccāraṇārtha (declared); in kim / idam / etad the sarvādeśa (1.1.55) replaces stem and sup together, so 2.4.71 is masked there (its ablation set is the eleven tad / yad / sarva words)
- the sense (pañcamī / saptamī / kāla) is declared from the vidhi sūtra; thāl (tathā, 5.3.24), the diś affixes 5.3.27 ff., the optional forms of 5.3.4 (idam → eta), the accent
- RH, YM untouched
