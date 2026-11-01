# Avyayībhāva and Dvigu Compiled

2 November 2026. upakumbham, pratidinam (2.4.83 am), adhihari, yathāśakti (2.4.82 luk), trilokī, pañcamūlī (4.1.21 + 6.4.148), pañcagavam (5.4.92 + 6.1.78 + 2.4.17 + 7.1.24), tripadam — the two compound kinds theorum/104 left out. Each rule shown load-bearing on exactly the forms it governs (the certificate's `broken` record lists every ablation set).

## 1. Sources (quoted)

```text
1.1.41 avyayībhāvaś ca
1.2.43 prathamānirdiṣṭaṁ samāsa upasarjanam
2.1.5 avyayībhāvaḥ
2.1.51 taddhitārthottarapadasamāhāre ca
2.1.52 saṁkhyāpūrvo dviguḥ
2.1.6 avyayaṁ vibhaktisamīpasamṛddhivyṛddhyarthābhāvātyayāsampratiśabdaprādurbhāvapaścādyathānupūrvyayaugapadyasādṛśyasampattisākalyāntavacaneṣu
2.1.7 yathā 'sādṛśye
2.2.30 upasarjanaṁ pūrvam
2.4.1 dvigur ekavacanam
2.4.17 sa napuṁsakam
2.4.18 avyayībhāvaś ca
2.4.71 supo dhātuprātipadikayoḥ
2.4.82 avyayād āpsupaḥ
2.4.83 nāvyayībhāvād ato 'm tv apañcamyāḥ
4.1.21 dvigoḥ
5.4.92 gor ataddhitaluki
6.1.78 eco 'yavāyāvaḥ
6.4.148 yasyeti ca
7.1.24 ato 'm
```

## 2. Results

- four avyayībhāvas (upakumbham, pratidinam by 2.4.83; adhihari, yathāśakti by 2.4.82) and four samāhāra dvigus (trilokī, pañcamūlī by 4.1.21 + 6.4.148; pañcagavam by 5.4.92 + 6.1.78 + 2.4.17 + 7.1.24; tripadam) in the nominative; each rule breaks exactly the words stated (2.4.71 all eight)

## 3. Certificate

```text
python -m proof_lab.avyayibhava_dvigu_compiled
python -m unittest proof_lab.test_avyayibhava_dvigu_compiled -v
```
Status `PASS_AVYAYIBHAVA_DVIGU_COMPILED_CANDIDATE`, SHA-256 `58653d425c4c29a2f3c1a1b5f60a6df82de242dbdf74b6704a91d676e6082f57` (`proof_lab/AVYAYIBHAVA_DVIGU_COMPILED_EXPECTED.sha256`).

## 4. Claim boundary

PROVED: as in §2.

NOT CLAIMED:
- the sense of each avyayībhāva (samīpa, vīpsā, adhikaraṇa, sādṛśya) declared from 2.1.6 / 2.1.7; the ṅīp / neuter option of 4.1.21 (tripadam kept neuter) declared; the other cases of the avyayībhāva (2.4.84 tṛtīyāsaptamyor bahulam), the dvigu's taddhita sense, the non-samāhāra dvigu, the accent
- RH, YM untouched

## 5. Note (2 November 2026, from theorum/118)

The pinned sūtrapāṭha reads 2.1.7 as *yathāsādṛśye* = *yathā + a-sādṛśye*: *yathā* compounds in a sense **other than** similarity. The sense of *yathāśakti* is therefore yogyatā / anativṛtti, not "sādṛśya" as this capsule's claim-boundary sentence labelled it; the derivation (2.1.7, 2.4.82) and the certificate are unaffected (the sense is a declared input), so the pin stands. See theorum/118 §1.
