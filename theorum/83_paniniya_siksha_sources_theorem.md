# The Śikṣā Vedāṅga — the Pāṇinīya Śikṣā quoted; Theorem 79's manner rows and Theorem 81's place table derived from its verses

1 November 2026. Vedāṅga status in this repository before this capsule: Chandas
(theorum/71), Kalpa/Śulba (theorum/72), Jyotiṣa (theorum/73), Vyākaraṇa
(theorum/58–68, 80–82) — and no Śikṣā. theorum/81 had to *declare* its
sthāna/prayatna table and a "proportion" attribute to keep *e* from *ai*;
theorum/79 *declared* its five manner rows. This capsule quotes the Pāṇinīya
Śikṣā (60-verse Yajus recension; two independent printed texts agree on every
verse used) and derives both from it.

## 1. Sources (quoted)

```text
PŚ 3   triṣaṣṭiś catuḥṣaṣṭir vā varṇāḥ sambhavato matāḥ / prākṛte saṁskṛte cāpi svayaṁ proktāḥ svayambhuvā
PŚ 4   svarā viṁśatir ekaś ca sparśānāṁ pañcaviṁśatiḥ / yādayaś ca smṛtā hy aṣṭau catvāraś ca yamāḥ smṛtāḥ
PŚ 5   anusvāro visargaś ca ×k ×pau cāpi parāśritau / duḥspṛṣṭaś ceti vijñeyo ḷkāraḥ pluta eva ca
PŚ 11  udāttaś cānudāttaś ca svaritaś ca svarās trayaḥ / hrasvo dīrghaḥ pluta iti kālato niyamā aci
PŚ 13  aṣṭau sthānāni varṇānām uraḥ kaṇṭhaḥ śiras tathā / jihvāmūlaṁ ca dantāś ca nāsikoṣṭhau ca tālu ca
PŚ 17  kaṇṭhyāv ahāv icuyaśās tālavyā oṣṭhajāv upū / syur mūrdhanyā ṛṭuraṣā dantyā ḷtulasāḥ smṛtāḥ
PŚ 18  jihvāmūle tu kuḥ prokto dantyoṣṭhyo vaḥ smṛto budhaiḥ / e ai tu kaṇṭhatālavyā o au kaṇṭhoṣṭhajau smṛtau
PŚ 21  svarāṇām ūṣmaṇāṁ caiva vivṛtaṁ karaṇaṁ smṛtam / tebhyo 'pi vivṛtāv eṅau tābhyām aicau tathaiva ca
PŚ 38  aco 'spṛṣṭā yaṇas tv īṣan nemaspṛṣṭāḥ śalaḥ smṛtāḥ / śeṣāḥ spṛṣṭā halaḥ proktā nibodhānupradānataḥ
PŚ 39  ñamo 'nunāsikā nahro nādino hajhaṣaḥ smṛtāḥ / īṣannādā yaṇo jaś ca śvāsinas tu khaphādayaḥ
PŚ 40  īṣacchvāsāṁś caro vidyād ...
A 1.1.9 tulyāsyaprayatnaṁ savarṇam ; 1.1.10 nājjhalau ; 1.1.8 mukhanāsikāvacano 'nunāsikaḥ
```

## 2. Results

**T1 The count.** Verse 4's 21 + 25 + 8 + 4 = 58 is reproduced by enumeration:
21 vowels = {a, i, u, ṛ} × {hrasva, dīrgha, pluta} + ḷ + {e, ai, o, au} ×
{dīrgha, pluta}; the 25 stops are theorum/79's grid; the eight yādi are
theorum/78's tokens y r l v ś ṣ s h. Verse 5's six additions give verse 3's
63 / 64. Verse 13 names eight places.

**T2 The place table is derived.** Verses 13, 17, 18 give theorum/81's STHANA
table on every carrier sound except the ka-varga, which the Śikṣā puts at
*jihvāmūla* (18) where the Siddhānta-kaumudī puts it at *kaṇṭha*. The 1.1.9
savarṇa classes computed from the Śikṣā table are **identical** to
theorum/81's, so the difference is invisible to savarṇa.

**T3 The manner rows are derived.** Verses 39–40's anupradāna classes —
anunāsika ñ m ṅ ṇ n; nādin h + jhaṣ; īṣannāda yaṇ + jaś; śvāsin kh ph ch ṭh
th; īṣacchvāsa car — are disjoint, cover all 33 consonants, and restricted
to the 25 stops are **exactly** theorum/79's five manner rows; verse 39's
nasals are theorum/81's 1.1.8 set.

**T4 The ai/au gap closes; the 1.1.10 verdict is a reading.** Verse 21 grades
openness (vowels and ūṣman vivṛta; eṅ more open; aic more open still). With
this grade as the internal effort, *e/ai* and *o/au* separate **from the
text** — theorum/81's declared proportion attribute is no longer needed —
and a vowel and an ūṣman of one place share the effort, so 1.1.10 is
load-bearing (without it: {a ā h}, {i ī ś}, {ṛ ṝ ṣ}, {ḷ ḹ s} would merge).
With verse 38's four contact grades instead (aspṛṣṭa / īṣat / nema / spṛṣṭa),
the same classes result but 1.1.10 is redundant. Both are computed; the
Kāśikā's reading (shared vivṛta) is the one under which 1.1.10 does work.

## 3. Certificate

```text
python -m proof_lab.paniniya_siksha_sources
python -m unittest proof_lab.test_paniniya_siksha_sources -v
```
Status `PASS_PANINIYA_SIKSHA_SOURCES_CANDIDATE`, SHA-256
`473bcf775c05db5253310b94e9fd818d6e22eb20a4f9ed6d2342a836e80b2de5`
(`proof_lab/PANINIYA_SIKSHA_SOURCES_EXPECTED.sha256`). Consumes theorum/78's
tokens, theorum/79's grid, theorum/81's table and class function. Exact.

## 4. Claim boundary

```text
PŚ 3–5 COUNTS REPRODUCED ON THE CARRIER (58; 63 / 64)                          PROVED
PŚ 13/17/18 = theorum/81 STHANA EXCEPT ka-varga; 1.1.9 CLASSES IDENTICAL        PROVED
PŚ 39–40 ANUPRADĀNA ON STOPS = theorum/79 MANNER ROWS; NASALS = 1.1.8 SET        PROVED
PŚ 21 SEPARATES e/ai, o/au FROM THE TEXT (theorum/81's DECLARED ATTRIBUTE RETIRED) PROVED
1.1.10 LOAD-BEARING UNDER THE KARAṆA READING, REDUNDANT UNDER THE SPARŚA READING PROVED (both computed; reading not decided)
YAMAS, ANUSVĀRA, VISARGA, JIHVĀMŪLĪYA, UPADHMĀNĪYA, DUḤSPṚṢṬA ḷ, PLUTA          COUNTED, NOT CARRIED
ACCENT (PŚ 11), MĀTRĀ DURATIONS (PŚ 19–20)                                      CITED, NOT MODELLED
RH, YM                                                                          UNTOUCHED
```
