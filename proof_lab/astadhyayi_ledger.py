from __future__ import annotations

"""Aṣṭādhyāyī sūtra ledger: the ONE place in this repository that records which
sūtras have been realized, at what evidence level, and where.

    python -m proof_lab.astadhyayi_ledger            # rebuild proof_lab/astadhyayi/ASTADHYAYI_LEDGER.json + .md
    python -m unittest proof_lab.test_astadhyayi_ledger -v

Levels (strict order):
  compiled    the rule is a case-structured record read by the paribhāṣā interpreter (theorum/80 and later)
  hand_coded  the rule is an exact finite function in a certified proof_lab packet (theorum/58–68, 77)
  meta        a saṁjñā / paribhāṣā / adhikāra sūtra the interpreter implements (theorum/58, 62, 78, 80)
  cited       quoted in a theorem as context or scope, not executed
  misnumbered a number that an owner canvas used for a different sūtra; the correct number is given

The quoted IAST text is curated here.  An entry without text is a citation whose
wording has not yet been entered; it is reported, never invented.  Nothing in
this ledger is a claim that the whole grammar is realized: the counts are the
claim boundary.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "proof_lab" / "astadhyayi"
SUTRAPATHA = ROOT / "research" / "panini_grammar" / "SUTRAPATHA.tsv"   # PG1's pinned edition (ashtadhyayi.com record ids), Devanagari


def load_sutrapatha() -> dict[str, str]:
    """sūtra number → Devanagari text from the pinned PG1 inventory (3,983 numbered records)."""
    out: dict[str, str] = {}
    if not SUTRAPATHA.exists():
        return out
    for line in SUTRAPATHA.read_text(encoding="utf-8").splitlines()[1:]:
        sid, _rec, skt = line.split("\t")
        out[sid] = skt
    return out


# ---------------------------------------------------------------- Devanagari → IAST (for the cross-check of the curated texts only)
_V = {"अ": "a", "आ": "ā", "इ": "i", "ई": "ī", "उ": "u", "ऊ": "ū", "ऋ": "ṛ", "ॠ": "ṝ", "ऌ": "ḷ", "ॡ": "ḹ", "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au"}
_M = {"ा": "ā", "ि": "i", "ी": "ī", "ु": "u", "ू": "ū", "ृ": "ṛ", "ॄ": "ṝ", "ॢ": "ḷ", "ॣ": "ḹ", "े": "e", "ै": "ai", "ो": "o", "ौ": "au"}
_C = {"क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ṅ", "च": "c", "छ": "ch", "ज": "j", "झ": "jh", "ञ": "ñ", "ट": "ṭ", "ठ": "ṭh", "ड": "ḍ", "ढ": "ḍh", "ण": "ṇ",
      "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n", "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m", "य": "y", "र": "r", "ल": "l", "व": "v", "श": "ś", "ष": "ṣ", "स": "s", "ह": "h"}


def deva_to_iast(s: str) -> str:
    out, i = [], 0
    while i < len(s):
        ch = s[i]
        if ch in _C:
            out.append(_C[ch])
            nxt = s[i + 1] if i + 1 < len(s) else ""
            if nxt == "्":
                i += 2
                continue
            if nxt in _M:
                out.append(_M[nxt])
                i += 2
                continue
            out.append("a")
        elif ch in _V:
            out.append(_V[ch])
        elif ch == "ं":
            out.append("ṁ")
        elif ch == "ः":
            out.append("ḥ")
        elif ch == "ऽ":
            out.append("'")
        elif ch == "ँ":
            out.append("~")
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def _norm(s: str) -> str:
    return re.sub(r"[\s'’\-]", "", s).replace("ṃ", "ṁ").replace("ṁ", "n").replace("m", "n").replace("ñ", "n").replace("ṇ", "n").replace("ṅ", "n").lower()

# ---------------------------------------------------------------- curated texts (IAST); blank = not yet entered
TEXT = {
    "7.1.58": "idito num dhātoḥ",
    "2.4.54": "cakṣiṅaḥ khyāñ", "2.4.55": "vā liṭi", "3.4.83": "vido laṭo vā",
    "7.3.78": "pāghrādhmāsthāmnādāṇdṛśyarttisarttiśadasadāṁ pibajighradhamatiṣṭhamanayacchapaśyarcchadhauśīyasīdāḥ",
    "1.3.93": "luṭi ca kḷpaḥ", "7.2.60": "tāsi ca kḷpaḥ", "7.3.92": "tṛṇaha im", "8.2.18": "kṛpo ro laḥ",
    "7.4.10": "ṛtaś ca saṁyogāder guṇaḥ",
    "1.3.92": "vṛdbhyaḥ syasanoḥ",
    "6.4.117": "ā ca hau",
    "6.4.35": "śā hau", "6.4.74": "na māṅyoge", "7.2.44": "svaratisūtisūyatidhūñūdito vā", "7.2.57": "se 'sici kṛtacṛtacchṛdatṛdanṛtaḥ", "8.3.79": "vibhāṣeṭaḥ",
    "7.1.35": "tuhyos tātaṅṅ āśiṣy anyatarasyām",
    "1.2.50": "id goṇyāḥ", "2.4.64": "yañañoś ca", "4.1.36": "pūtakrator ai ca", "4.1.38": "manor au vā", "4.1.73": "śārṅgaravādyaño ṅīn", "4.1.74": "yaṅaś cāp", "4.1.78": "aṇiñor anārṣayor gurūpottamayoḥ ṣyaṅ gotre", "4.1.96": "bāhvādibhyaś ca", "4.1.104": "anṛṣyānantarye bidādibhyo 'ñ",
    "3.4.84": "bruvaḥ pañcānām ādita āho bruvaḥ", "7.2.114": "mṛjer vṛddhiḥ", "3.1.82": "stanbhustunbhuskanbhuskunbhuskuñbhyaḥ śnuś ca", "7.3.95": "turustuśamyamaḥ sārvadhātuke", "7.3.90": "ūrṇoter vibhāṣā", "6.4.115": "bhiyo 'nyatarasyām", "6.4.116": "jahāteś ca", "8.4.65": "jharo jhari savarṇe",
    "4.1.1": "ṅyāpprātipadikāt", "4.1.3": "striyām", "4.1.4": "ajādyataṣ ṭāp", "4.1.5": "ṛnnebhyo ṅīp", "4.1.6": "ugitaś ca", "7.1.80": "ācchīnadyor num", "7.1.81": "śapśyanor nityam", "7.3.44": "pratyayasthāt kāt pūrvasyāta id āpy asupaḥ", "7.1.78": "nābhyastāc chatuḥ", "7.1.79": "vā napuṁsakasya", "6.1.5": "ubhe abhyastam", "1.1.39": "kṛn mejantaḥ", "1.1.40": "ktvātosunkasunaḥ", "8.4.39": "kṣubhnādiṣu ca",
    "3.2.124": "laṭaḥ śatṛśānacāv aprathamāsamānādhikaraṇe", "3.4.113": "tiṅśit sārvadhātukam", "7.2.82": "āne muk", "7.2.83": "īdāsaḥ", "7.4.21": "śīṅaḥ sārvadhātuke guṇaḥ", "6.1.97": "ato guṇe",
    "3.1.96": "tavyattavyānīyaraḥ", "3.1.133": "ṇvultṛcau", "3.2.102": "niṣṭhā", "3.3.10": "tumunṇvulau kriyāyāṁ kriyārthāyām", "3.4.21": "samānakartṛkayoḥ pūrvakāle", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "1.1.5": "kṅiti ca", "1.1.26": "ktaktavatū niṣṭhā", "1.2.18": "na ktvā seṭ", "1.2.19": "niṣṭhā śīṅsvidimidikṣvididhṛṣaḥ", "1.2.26": "ralo vyupadhād dhalādeḥ saṁś ca", "7.1.1": "yuvor anākau", "2.4.36": "ado jagdhir lyap ti kiti", "2.4.52": "aster bhūḥ", "2.4.53": "bruvo vaciḥ", "6.1.50": "mīnātiminotidīṅāṁ lyapi ca", "7.2.10": "ekāca upadeśe 'nudāttāt", "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.11": "śryukaḥ kiti", "7.2.14": "śvīdito niṣṭhāyām", "7.2.15": "yasya vibhāṣā", "7.2.16": "āditaś ca", "7.2.44": "svaratisūtisūyatidhūñūdito vā", "7.2.56": "udito vā", "7.2.37": "graho 'liṭi dīrghaḥ", "7.2.38": "vṝto vā", "7.3.84": "sārvadhātukārdhadhātukayoḥ", "7.3.86": "pugantalaghūpadhasya ca", "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "7.3.34": "nodāttopadeśasya māntasyānācameḥ", "7.3.32": "hanas to 'ciṇṇaloḥ", "7.3.54": "ho hanter ñṇinneṣu", "6.1.78": "eco 'yavāyāvaḥ", "7.1.100": "ṝta id dhātoḥ", "7.1.102": "udoṣṭhyapūrvasya", "8.2.77": "hali ca", "6.4.37": "anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti", "6.1.15": "vacisvapiyajādīnāṁ kiti", "6.1.16": "grahijyāvayivyadhivaṣṭivicativṛścatipṛcchatibhṛjjatīnāṁ ṅiti ca", "6.4.66": "ghumāsthāgāpājahātisāṁ hali", "7.4.40": "dyatisyatimāsthām it ti kiti", "7.4.42": "dadhāter hiḥ", "7.4.46": "do dad ghoḥ", "6.4.64": "āto lopa iṭi ca", "6.4.63": "dīṅo yuḍ aci kṅiti", "6.4.24": "aniditāṁ hala upadhāyāḥ kṅiti", "8.2.42": "radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ", "8.2.43": "saṁyogāder āto dhātor yaṇvataḥ", "8.2.44": "lvādibhyaḥ", "8.2.45": "oditaś ca", "8.2.46": "kṣiyo dīrghāt", "8.2.52": "paco vaḥ", "8.2.56": "nudavidondatrāghrāhrībhyo 'nyatarasyām", "8.2.57": "na dhyākhyāpṝmūrchimadām", "8.2.30": "coḥ kuḥ", "8.2.31": "ho ḍhaḥ", "8.2.32": "dāder dhātor ghaḥ", "8.2.36": "vraścabhrasjasṛjamṛjayajarājabhrājacchaśāṁ ṣaḥ", "8.2.40": "jhaṣas tathor dho 'dhaḥ", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade", "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.4.41": "ṣṭunā ṣṭuḥ", "8.4.53": "jhalāṁ jaś jhaśi", "3.1.25": "satyāpapāśarūpavīṇātūlaślokasenālomatvacavarmavarṇacūrṇacurādibhyo ṇic", "6.4.51": "ṇer aniṭi", "6.4.52": "niṣṭhāyāṁ seṭi", "7.1.58": "idito nuṁ dhātoḥ", "8.3.24": "naś cāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ", "6.4.19": "cchvoḥ śūḍ anunāsike ca", "6.1.77": "iko yaṇ aci", "6.4.2": "halaḥ", "7.4.43": "jahāteś ca ktvi", "7.3.33": "āto yuk ciṇkṛtoḥ", "6.1.101": "akaḥ savarṇe dīrghaḥ", "1.2.8": "rudavidamuṣagrahisvapipracchaḥ sa~ś ca", "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "6.1.65": "ṇo naḥ", "7.3.85": "jāgro 'viciṇṇalṅitsu", "7.2.114": "mṛjer vṛddhiḥ", "6.4.42": "janasanakhanāṁ sañjhaloḥ", "6.4.15": "anunāsikasya kvijhaloḥ kṅiti", "7.1.64": "labheś ca", "8.3.13": "ḍho ḍhe lopaḥ", "6.3.111": "ḍhralope pūrvasya dīrgho 'ṇaḥ", "8.4.56": "vāvasāne",
    "1.2.27": "ūkālo 'j jhrasvadīrghaplutaḥ",
    "1.3.62": "pūrvavat sanaḥ", "7.4.55": "āpjñapyṛdhām īt", "7.2.49": "sanīvantardhabhrasjadambhuśrisvṛyūrṇubharajñapisanām", "7.2.12": "sani grahaguhoś ca", "2.4.47": "sani ca", "1.2.10": "halantāc ca", "1.2.8": "rudavidamuṣagrahisvapipracchaḥ sa~ś ca", "7.2.38": "vṝto vā", "6.1.2": "ajāder dvitīyasya", "8.3.61": "stautiṇyor eva ṣaṇy abhyāsāt",
    "1.3.74": "ṇicaś ca", "2.4.46": "ṇau gamir abodhane", "6.1.48": "krīṅjīnāṁ ṇau", "7.1.64": "labheś ca", "7.3.37": "śācchāsāhvāvyāvepāṁ yuk",
    "7.4.22": "ayaṅ yi kṅiti", "6.4.44": "tanoter yaki", "6.4.43": "ye vibhāṣā", "6.4.42": "janasanakhanāṁ sañjhaloḥ", "3.1.66": "ciṇ bhāvakarmaṇoḥ",
    "8.2.28": "iṭa īṭi", "7.2.3": "vadavrajahalantasyācaḥ", "7.2.4": "neṭi", "7.2.5": "hmyantakṣaṇaśvasajāgṛṇiśvyeditām", "7.2.7": "ato halāder laghoḥ", "3.1.57": "irito vā", "3.1.52": "asyativaktikhyātibhyo 'ṅ", "7.4.20": "vaca um", "2.4.37": "luṅsanor ghasḷ", "7.3.73": "lug vā duhadihalihaguhām ātmanepade dantye", "2.4.45": "iṇo gā luṅi", "7.2.73": "yamaramanamātāṁ sak ca", "8.2.27": "hrasvād aṅgāt", "1.2.17": "sthāghvor ic ca", "3.1.48": "ṇiśridrusrubhyaḥ kartari caṅ", "6.1.11": "caṅi", "7.4.1": "ṇau caṅy upadhāyā hrasvaḥ", "7.4.93": "sanvallaghuni caṅpare 'naglope", "7.4.94": "dīrgho laghoḥ", "7.3.72": "ksasyāci", "3.4.110": "ātaḥ", "7.2.72": "stusudhūñbhyaḥ parasmaipadeṣu",
    "3.3.139": "liṅnimitte lṛṅ kriyātipattau", "3.4.81": "liṭas tajhayor eśirec", "3.1.35": "kāspratyayād ām amantre liṭi", "3.1.36": "ijādeś ca gurumato 'nṛcchaḥ", "3.1.37": "dayāyāsaś ca", "3.1.38": "uṣavidajāgṛbhyo 'nyatarasyām", "3.1.39": "bhīhrībhṛhuvāṁ śluvac ca", "3.1.40": "kṛñ cānuprayujyate liṭi", "7.4.70": "ata ādeḥ", "7.4.72": "aśnoteś ca", "7.4.71": "tasmān nuḍ dvihalaḥ", "6.4.78": "abhyāsasyāsavarṇe", "7.4.69": "dīrgha iṇaḥ kiti", "7.1.34": "āta au ṇalaḥ", "6.1.17": "liṭy abhyāsasyobhayeṣām", "7.4.67": "dyutisvāpyoḥ samprasāraṇam", "7.3.55": "abhyāsāc ca", "6.4.120": "ata ekahalmadhye 'nādeśāder liṭi", "6.4.121": "thali ca seṭi", "6.4.123": "rādho hiṁsāyām", "6.4.126": "na śasadadavādiguṇānām", "7.2.61": "acas tāsvat thaly aniṭo nityam", "7.2.62": "upadeśe 'tvataḥ", "7.2.63": "ṛto bhāradvājasya", "2.4.40": "liṭy anyatarasyām", "7.3.58": "vibhāṣā ceḥ", "7.4.11": "ṛcchatyṝtām", "7.4.12": "śṝdṝprāṁ hrasvo vā",
    "2.4.52": "aster bhūḥ", "2.4.53": "bruvo vaciḥ", "7.2.70": "ṛddhanoḥ sye", "6.1.50": "mīnātiminotidīṅāṁ lyapi ca", "6.1.45": "ādeca upadeśe 'śiti", "7.2.57": "se 'sici kṛtacṛtacchṛdatṛdanṛtaḥ", "7.4.25": "akṛtsārvadhātukayor dīrghaḥ", "7.4.28": "riṅ śayagliṅkṣu", "7.4.29": "guṇo 'rtisaṁyogādyoḥ", "7.3.85": "jāgro 'viciṇṇalṅitsu", "2.4.42": "hano vadha liṅi", "6.4.48": "ato lopaḥ", "6.4.2": "halaḥ", "8.3.78": "iṇaḥ ṣīdhvaṁluṅliṭāṁ dho 'ṅgāt", "8.3.79": "vibhāṣeṭaḥ", "6.4.51": "ṇer aniṭi", "1.2.11": "liṅsicāv ātmanepadeṣu", "1.2.12": "uś ca",
    "8.2.73": "tipy anasteḥ", "8.2.74": "sipi dhāto rurvā", "8.2.25": "dhi ca", "6.4.36": "hanter jaḥ", "6.4.22": "asiddhavad atrābhāt", "7.3.88": "bhūsuvos tiṅi", "7.3.91": "guṇo 'pṛkte",
    "7.1.25": "adḍ ḍatarādibhyaḥ pañcabhyaḥ",
    "6.4.109": "ye ca", "6.4.118": "lopo yi", "7.3.87": "nābhyastasyāci piti sārvadhātuke", "8.4.37": "padāntasya",
    "6.1.96": "usy apadāntāt", "6.4.101": "hujhalbhyo her dhiḥ", "6.4.119": "ghvasor ed dhāv abhyāsalopaś ca", "7.3.83": "jusi ca", "8.2.24": "rāt sasya", "7.3.100": "adaḥ sarveṣām", "3.1.83": "halaḥ śnaḥ śānaj jhau", "6.4.106": "utaś ca pratyayād asaṁyogapūrvāt",
    "7.2.76": "rudādibhyaḥ sārvadhātuke",
    "6.1.6": "jakṣityādayaḥ ṣaṭ", "7.3.98": "rudaś ca pañcabhyaḥ", "7.2.77": "īśaḥ se", "7.2.78": "īḍajanor dhve ca", "7.3.93": "bruva īṭ", "7.2.114": "mṛjer vṛddhiḥ", "7.4.21": "śīṅaḥ sārvadhātuke guṇaḥ", "7.1.6": "śīṅo ruṭ", "6.4.34": "śāsa id aṅhaloḥ", "6.4.114": "id daridrasya", "6.4.37": "anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti", "7.3.54": "ho hanter ñṇinneṣu", "8.2.36": "vraścabhrasjasṛjamṛjayajarājabhrājacchaśāṁ ṣaḥ", "8.3.60": "śāsivasighasīnāṁ ca", "8.2.31": "ho ḍhaḥ", "8.2.32": "dāder dhātor ghaḥ", "8.2.37": "ekāco baśo bhaṣ jhaṣantasya sdhvoḥ", "8.3.13": "ḍho ḍhe lopaḥ", "6.3.111": "ḍhralope pūrvasya dīrgho 'ṇaḥ",
    "7.3.89": "uto vṛddhir luki hali", "7.3.90": "ūrṇoter vibhāṣā", "7.3.95": "turustuśamyamaḥ sārvadhātuke", "6.4.81": "iṇo yaṇ", "6.4.82": "er anekāco 'saṁyogapūrvasya", "7.4.60": "halādiḥ śeṣaḥ", "7.4.75": "nijāṁ trayāṇāṁ guṇaḥ ślau", "7.4.76": "bhṛñām it", "7.4.77": "artipipartyoś ca", "7.1.102": "ud oṣṭhyapūrvasya", "8.2.41": "ṣaḍhoḥ kaḥ si", "8.3.57": "iṇkoḥ", "6.4.115": "bhiyo 'nyatarasyām", "6.4.116": "jahāteś ca",
    "3.1.82": "stanbhustunbhuskanbhuskunbhuskuñbhyaḥ śnuś ca", "6.4.24": "aniditāṁ hala upadhāyāḥ kṅiti", "7.3.79": "jñājanor jā", "6.1.16": "grahijyāvayivyadhivaṣṭivicativṛścatipṛcchatibhṛjjatīnāṁ ṅiti ca", "1.1.45": "ig yaṇaḥ samprasāraṇam", "6.1.108": "samprasāraṇāc ca", "8.4.40": "stoḥ ścunā ścuḥ", "8.4.44": "śāt", "8.4.39": "kṣubhnādiṣu ca",
    "2.4.72": "adiprabhṛtibhyaḥ śapaḥ", "2.4.75": "juhotyādibhyaḥ śluḥ", "6.1.10": "ślau", "3.1.78": "rudhādibhyaḥ śnam", "6.4.111": "śnasor allopaḥ", "7.1.4": "ad abhyastāt", "7.1.58": "idito num dhātoḥ", "6.4.23": "śnān nalopaḥ", "8.2.38": "dadhas tathoś ca", "8.2.30": "coḥ kuḥ", "8.3.24": "naś cāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ", "1.1.20": "dādhā ghv adāp",
    "3.1.25": "satyāpapāśarūpavīṇātūlaślokasenālomatvacavarmavarṇacūrṇacurādibhyo ṇic", "3.1.32": "sanādyantā dhātavaḥ", "3.1.69": "divādibhyaḥ śyan", "3.1.73": "svādibhyaḥ śnuḥ", "3.1.74": "śruvaḥ śṛ ca", "3.1.77": "tudādibhyaḥ śaḥ", "3.1.79": "tanādikṛñbhya uḥ", "3.1.81": "kryādibhyaḥ śnā", "1.3.72": "svaritañitaḥ kartrabhiprāye kriyāphale", "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "7.3.86": "pugantalaghūpadhasya ca", "8.2.77": "hali ca", "7.3.74": "śamām aṣṭānāṁ dīrghaḥ śyani", "7.3.80": "pvādīnāṁ hrasvaḥ", "6.4.110": "ata ut sārvadhātuke", "6.4.108": "nityaṁ karoteḥ", "6.4.107": "lopaś cāsyānyatarasyāṁ mvoḥ", "6.4.77": "aci śnudhātubhruvāṁ yvor iyaṅuvaṅau", "6.4.87": "huśnuvoḥ sārvadhātuke", "6.4.112": "śnābhyastayor ātaḥ", "6.4.113": "ī halyaghoḥ", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade",
    "3.2.115": "parokṣe liṭ", "3.4.115": "liṭ ca", "3.4.82": "parasmaipadānāṁ ṇalatususthalathusaṇalvamāḥ", "1.2.5": "asaṁyogāl liṭ kit", "1.1.56": "sthānivad ādeśo 'nalvidhau", "6.1.8": "liṭi dhātor anabhyāsasya", "6.1.1": "ekāco dve prathamasya", "6.1.4": "pūrvo 'bhyāsaḥ", "7.4.59": "hrasvaḥ", "7.4.62": "kuhoś cuḥ", "7.4.66": "ur at", "7.4.73": "bhavater aḥ", "8.4.54": "abhyāse car ca", "7.2.13": "kṛsṛbhṛvṛstudrusruśruvo liṭi", "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "6.4.98": "gamahanajanakhanaghasāṁ lopaḥ kṅity anaṅi",
    "3.1.33": "syatāsī lṛluṭoḥ", "3.1.43": "cli luṅi", "3.1.44": "cleḥ sic", "2.4.77": "gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu", "3.1.55": "puṣādidyutādyḷditaḥ parasmaipadeṣu", "2.4.85": "luṭaḥ prathamasya ḍāraurasaḥ", "3.4.109": "sijabhyastavidibhyaś ca", "7.1.5": "ātmanepadeṣv anataḥ", "3.4.107": "suṭ tithoḥ", "7.3.96": "astisico 'pṛkte", "6.4.88": "bhuvo vug luṅliṭoḥ", "7.4.50": "tāsas tyor lopaḥ", "7.4.51": "ri ca", "7.4.52": "ha eti", "8.2.29": "skoḥ saṁyogādyor ante ca", "3.3.13": "lṛṭ śeṣe ca", "3.3.15": "anadyatane luṭ", "3.2.110": "luṅ", "3.4.116": "liṅāśiṣi", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "3.4.104": "kid āśiṣi", "8.3.55": "apadāntasya mūrdhanyaḥ",
    "3.4.85": "loṭo laṅvat", "3.4.86": "er uḥ", "3.4.87": "ser hy apic ca", "3.4.89": "mer niḥ", "3.4.90": "ām etaḥ", "3.4.91": "savābhyāṁ vāmau", "3.4.92": "āḍ uttamasya pic ca", "3.4.93": "eta ai", "3.4.105": "jhasya ran", "3.4.106": "iṭo 't", "3.4.108": "jher jus", "6.4.72": "āḍ ajādīnām", "6.1.90": "āṭaś ca", "7.2.79": "liṅaḥ salopo 'nantyasya", "7.2.80": "ato yeyaḥ", "6.4.105": "ato heḥ", "6.1.65": "ṇo naḥ", "3.3.161": "vidhinimantraṇāmantraṇādhīṣṭasaṁpraśnaprārthaneṣu liṅ", "3.3.162": "loṭ ca", "3.2.111": "anadyatane laṅ",
    "1.1.52": "alo 'ntyasya", "1.1.55": "anekālśit sarvasya", "4.1.4": "ajādyataṣ ṭāp", "6.1.97": "ato guṇe", "7.1.11": "nedamadasor akoḥ", "7.2.103": "kimaḥ kaḥ", "7.2.106": "tadoḥ saḥ sāvanantyayoḥ", "7.2.108": "idamo maḥ", "7.2.109": "daś ca", "7.2.110": "yaḥ sau", "7.2.111": "ido 'y puṁsi", "7.2.112": "anāpyakaḥ", "7.2.113": "hali lopaḥ",
    "1.1.24": "ṣṇāntā ṣaṭ", "1.1.47": "midaco 'ntyāt paraḥ", "1.1.63": "na lumatāṅgasya", "6.4.4": "na tisṛcatasṛ", "6.4.7": "nopadhāyāḥ", "7.1.21": "aṣṭābhya auś", "7.1.22": "ṣaḍbhyo luk", "7.1.53": "tres trayaḥ", "7.1.55": "ṣaṭcaturbhyaś ca", "7.1.98": "caturanaḍuhor ām udāttaḥ", "7.2.84": "aṣṭana ā vibhaktau", "7.2.99": "tricaturoḥ striyāṁ tisṛcatasṛ", "7.2.100": "aci ra ṛtaḥ", "7.2.102": "tyadādīnām aḥ", "8.4.41": "ṣṭunā ṣṭuḥ", "8.4.45": "yaro 'nunāsike 'nunāsiko vā", "8.4.56": "vāvasāne",
    "6.1.104": "nādici", "6.1.105": "dīrghāj jasi ca", "7.3.118": "aut", "7.3.119": "ac ca gheḥ", "7.3.120": "āṅo nāstriyām", "8.2.24": "rāt sasya", "6.4.11": "aptṛntṛcsvasṛnaptṛneṣṭṛtvaṣṭṛkṣattṛhotṛpotṛpraśāstṝṇām", "6.4.10": "sāntamahataḥ saṁyogasya", "6.1.114": "haśi ca", "1.4.6": "ṅiti hrasvaś ca", "8.3.36": "vā śari",
    "7.2.86": "yuṣmadasmador anādeśe", "7.2.87": "dvitīyāyāṁ ca", "7.2.88": "prathamāyāś ca dvivacane bhāṣāyām", "7.2.89": "yo 'ci", "7.2.90": "śeṣe lopaḥ", "7.2.91": "maparyantasya", "7.2.92": "yuvāvau dvivacane", "7.2.93": "yūyavayau jasi", "7.2.94": "tvāhau sau", "7.2.95": "tubhyamahyau ṅayi", "7.2.96": "tavamamau ṅasi", "7.2.97": "tvamāv ekavacane", "7.1.27": "yuṣmadasmadbhyāṁ ṅaso 'ś", "7.1.28": "ṅe prathamayor am", "7.1.29": "śaso na", "7.1.30": "bhyaso bhyam", "7.1.31": "pañcamyā at", "7.1.32": "ekavacanasya ca", "7.1.33": "sāma ākam",
    "6.4.7": "nopadhāyāḥ", "6.4.12": "inhanpūṣāryamṇāṁ śau", "6.4.13": "sau ca", "7.1.19": "napuṁsakāc ca", "5.2.115": "ata iniṭhanau", "5.2.121": "asmāyāmedhāsrajo viniḥ", "3.2.78": "supy ajātau ṇinis tācchīlye", "5.1.122": "pṛthvādibhya imanij vā",
    "3.4.102": "liṅaḥ sīyuṭ", "3.4.107": "suṭ tithoḥ", "3.4.105": "jhasya ran", "3.4.106": "iṭo 't",
    "3.1.43": "cli luṅi", "3.1.44": "cleḥ sic", "6.4.72": "āḍ ajādīnām", "6.1.90": "āṭaś ca", "8.2.26": "jhalo jhali", "7.1.5": "ātmanepadeṣv anataḥ",
    "3.3.173": "āśiṣi liṅloṭau", "3.4.116": "liṅāśiṣi", "3.4.103": "yāsuṭ parasmaipadeṣūdātto ṅic ca", "3.4.104": "kid āśiṣi", "7.2.79": "liṅaḥ salopo 'nantyasya", "6.4.67": "er liṅi", "3.4.108": "jher jus",
    "2.1.6": "avyayaṁ vibhaktisamīpasamṛddhivyṛddhyarthābhāvātyayāsampratiśabdaprādurbhāvapaścādyathānupūrvyayaugapadyasādṛśyasampattisākalyāntavacaneṣu", "2.1.7": "yathā 'sādṛśye", "2.1.5": "avyayībhāvaḥ", "1.1.41": "avyayībhāvaś ca", "2.4.18": "avyayībhāvaś ca", "2.4.82": "avyayād āpsupaḥ", "2.4.83": "nāvyayībhāvād ato 'm tv apañcamyāḥ", "2.1.52": "saṁkhyāpūrvo dviguḥ", "2.1.51": "taddhitārthottarapadasamāhāre ca", "2.4.17": "sa napuṁsakam", "2.4.1": "dvigur ekavacanam", "4.1.21": "dvigoḥ", "5.4.92": "gor ataddhitaluki", "7.1.24": "ato 'm",
    "5.3.1": "prāg diśo vibhaktiḥ", "5.3.2": "kiṁsarvanāmabahubhyo 'dvyādibhyaḥ", "5.3.7": "pañcamyās tasil", "5.3.10": "saptamyās tral", "5.3.15": "sarvaikānyakiṁyattadaḥ kāle dā", "5.3.11": "idamo haḥ", "5.3.3": "idama iś", "5.3.5": "etado 'n", "7.2.102": "tyadādīnām aḥ", "7.2.103": "kimaḥ kaḥ", "7.2.104": "ku tihoḥ", "1.1.38": "taddhitaś cāsarvavibhaktiḥ",
    "3.4.80": "thāsaḥ se", "7.4.52": "ha eti",
    "4.1.3": "striyām", "4.1.1": "ṅyāpprātipadikāt", "4.1.4": "ajādyataṣ ṭāp", "7.3.44": "pratyayasthāt kāt pūrvasyāta id āpy asupaḥ", "4.1.6": "ugitaś ca", "7.1.81": "śapśyanor nityam", "4.1.15": "ṭiḍḍhāṇañdvayasajdaghnañmātractayapṭhakṭhañkañkvarapaḥ", "4.1.16": "yañaś ca", "6.4.150": "halas taddhitasya", "4.1.41": "ṣidgaurādibhyaś ca", "1.3.6": "ṣaḥ pratyayasya",
    "3.1.67": "sārvadhātuke yak", "3.4.69": "laḥ karmaṇi ca bhāve cākarmakebhyaḥ", "1.3.13": "bhāvakarmaṇoḥ", "6.4.66": "ghumāsthāgāpājahātisāṁ hali", "6.1.15": "vacisvapiyajādīnāṁ kiti", "6.1.108": "samprasāraṇāc ca", "1.1.45": "ig yaṇaḥ samprasāraṇam",
    "7.1.70": "ugidacāṁ sarvanāmasthāne 'dhātoḥ", "1.1.47": "mid aco 'ntyāt paraḥ", "6.4.14": "atvasantasya cādhātoḥ", "8.2.23": "saṁyogāntasya lopaḥ", "5.2.94": "tad asyāsty asminn iti matup", "8.2.9": "mād upadhāyāś ca mator vo 'yavādibhyaḥ", "1.1.42": "śi sarvanāmasthānam", "1.1.43": "suḍ anapuṁsakasya",
    "3.1.22": "dhātor ekāco halādeḥ kriyāsamabhihāre yaṅ", "7.4.82": "guṇo yaṅlukoḥ", "7.4.83": "dīrgho 'kitaḥ", "7.4.85": "nugato 'nunāsikāntasya", "7.4.27": "rīṅ ṛtaḥ",
    "3.1.91": "dhātoḥ", "3.1.93": "kṛd atiṅ", "3.3.18": "bhāve", "3.3.16": "padarujaviśaspṛśo ghañ", "3.3.115": "lyuṭ ca", "3.1.133": "ṇvultṛcau", "3.4.67": "kartari kṛt", "3.2.124": "laṭaḥ śatṛśānacāv aprathamāsamānādhikaraṇe", "7.1.1": "yuvor anākau", "7.3.52": "cajoḥ ku ghiṇṇyatoḥ",
    "3.1.7": "dhātoḥ karmaṇaḥ samānakartṛkād icchāyāṁ vā", "6.1.9": "sanyaṅoḥ", "7.4.79": "sanyataḥ", "7.2.10": "ekāca upadeśe 'nudāttāt", "7.2.58": "gamer iṭ parasmaipadeṣu", "1.2.9": "iko jhal", "6.4.16": "ajjhanagamāṁ sani", "7.1.100": "ṝta id dhātoḥ", "8.2.77": "hali ca", "8.3.57": "iṇkoḥ", "8.2.30": "coḥ kuḥ", "7.4.54": "sani mīmāghurabhalabhaśakapatapadām aca is", "7.4.49": "saḥ syārdhadhātuke", "7.4.58": "atra lopo 'bhyāsasya", "1.3.57": "jñāśrusmṛdṛśāṁ sanaḥ",
    "3.1.26": "hetumati ca", "3.1.32": "sanādyantā dhātavaḥ", "6.4.92": "mitāṁ hrasvaḥ", "7.3.36": "artihrīvlīrīknūyīkṣmāyyātāṁ puṅ ṇau", "7.3.37": "śācchāsāhvāvyāvepāṁ yuk", "7.3.86": "pugantalaghūpadhasya ca", "1.4.13": "yasmāt pratyayavidhis tadādi pratyaye 'ṅgam",
    "2.1.3": "prāk kaḍārāt samāsaḥ", "2.1.4": "saha supā", "2.1.22": "tatpuruṣaḥ", "2.1.24": "dvitīyā śritātītapatitagatātyastaprāptāpannaiḥ", "2.1.36": "caturthī tadarthārthabalihitasukharakṣitaiḥ", "2.1.37": "pañcamī bhayena", "2.1.40": "saptamī śauṇḍaiḥ", "2.2.8": "ṣaṣṭhī", "1.2.42": "tatpuruṣaḥ samānādhikaraṇaḥ karmadhārayaḥ", "2.2.23": "śeṣo bahuvrīhiḥ", "2.2.24": "anekam anyapadārthe", "2.2.29": "cārthe dvandvaḥ", "1.2.43": "prathamānirdiṣṭaṁ samāsa upasarjanam", "2.2.30": "upasarjanaṁ pūrvam", "2.2.34": "alpāctaram", "2.4.71": "supo dhātuprātipadikayoḥ", "2.4.26": "paraval liṅgaṁ dvandvatatpuruṣayoḥ", "6.3.46": "ān mahataḥ samānādhikaraṇajātīyayoḥ", "5.4.91": "rājāhaḥsakhibhyaṣ ṭac", "6.4.144": "nas taddhite", "1.2.48": "gostriyor upasarjanasya", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade",
    "4.1.76": "taddhitāḥ", "4.1.82": "samarthānāṁ prathamād vā", "4.1.83": "prāg dīvyato 'ṇ", "4.1.92": "tasyāpatyam", "4.1.95": "ata iñ", "4.1.105": "gargādibhyo yañ", "4.3.120": "tasyedam", "7.2.117": "taddhiteṣv acām ādeḥ", "7.2.118": "kiti ca", "6.4.146": "or guṇaḥ", "6.4.148": "yasyeti ca", "7.3.50": "ṭhasyekaḥ",
    "3.2.115": "parokṣe liṭ", "3.4.82": "parasmaipadānāṁ ṇalatususthalathusaṇalvamāḥ", "1.2.5": "asaṁyogāl liṭ kit", "6.1.8": "liṭi dhātor anabhyāsasya", "6.1.1": "ekāco dve prathamasya", "6.1.4": "pūrvo 'bhyāsaḥ", "7.4.59": "hrasvaḥ", "7.4.60": "halādiḥ śeṣaḥ", "7.4.62": "kuhoś cuḥ", "7.4.66": "ur at", "7.4.73": "bhavater aḥ", "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "6.4.98": "gamahanajanakhanaghasāṁ lopaḥ kṅity anaṅi", "7.2.13": "kṛsṛbhṛvṛstudrusruśruvo liṭi",
    "3.2.110": "luṅ", "3.1.43": "cli luṅi", "3.1.44": "cleḥ sic", "3.1.55": "puṣādidyutādyḷditaḥ parasmaipadeṣu", "2.4.77": "gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu", "6.4.88": "bhuvo vug luṅliṭoḥ", "7.2.1": "sici vṛddhiḥ parasmaipadeṣu", "7.3.96": "astisico 'pṛkte", "8.4.41": "ṣṭunā ṣṭuḥ", "3.4.109": "sijabhyastavidibhyaś ca",
    "3.4.21": "samānakartṛkayoḥ pūrvakāle", "3.3.10": "tumunṇvulau kriyāyāṁ kriyārthāyām", "3.1.96": "tavyattavyānīyaraḥ", "7.2.11": "śryukaḥ kiti", "8.3.24": "naś cāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ",
    "6.4.72": "āḍ ajādīnām", "6.1.90": "āṭaś ca", "3.4.90": "ām etaḥ", "3.4.91": "savābhyāṁ vāmau", "3.4.93": "eta ai", "3.4.102": "liṅaḥ sīyuṭ", "3.4.105": "jhasya ran", "3.4.106": "iṭo 't", "3.4.107": "suṭ tithoḥ", "3.4.79": "ṭita ātmanepadānāṁ ṭer e", "3.4.80": "thāsaḥ se", "7.2.81": "āto ṅitaḥ", "1.3.12": "anudāttaṅita ātmanepadam",
    "7.3.114": "sarvanāmnaḥ syāḍ ḍhrasvaś ca",
    "3.3.13": "lṛṭ śeṣe ca", "3.3.15": "anadyatane luṭ", "3.1.33": "syatāsī lṛluṭoḥ", "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.58": "gamer iṭ parasmaipadeṣu", "2.4.85": "luṭaḥ prathamasya ḍāraurasaḥ", "6.4.143": "ṭeḥ", "7.4.50": "tāsastyor lopaḥ", "7.4.51": "ri ca",
    "3.3.162": "loṭ ca", "3.3.161": "vidhinimantraṇāmantraṇādhīṣṭasampraśnaprārthaneṣu liṅ", "3.4.85": "loṭo laṅvat", "3.4.86": "er uḥ", "3.4.87": "ser hy apic ca", "3.4.89": "mer niḥ", "3.4.92": "āḍ uttamasya pic ca", "6.4.105": "ato heḥ", "3.4.103": "yāsuṭ parasmaipadeṣūdātto ṅic ca", "3.4.108": "jher jus", "7.2.79": "liṅaḥ salopo 'nantyasya", "7.2.80": "ato yeyaḥ", "6.1.66": "lopo vyor vali",
    "3.2.111": "anadyatane laṅ", "1.3.78": "śeṣāt kartari parasmaipadam", "3.4.100": "itaś ca", "3.4.101": "tasthasthamipāṁ tāṁtaṁtāmaḥ", "3.4.99": "nityaṁ ṅitaḥ", "8.2.23": "saṁyogāntasya lopaḥ", "3.1.68": "kartari śap",
    "7.1.17": "jasaḥ śī", "7.1.14": "sarvanāmnaḥ smai", "7.1.15": "ṅasiṅyoḥ smātsminau", "7.1.52": "āmi sarvanāmnaḥ suṭ",
    "7.1.24": "ato 'm", "7.1.19": "napuṁsakāc ca", "7.1.20": "jaśśasoḥ śiḥ", "7.1.72": "napuṁsakasya jhalacaḥ", "7.1.73": "iko 'ci vibhaktau", "7.1.13": "ṅer yaḥ",
    "1.4.17": "svādiṣv asarvanāmasthāne", "1.4.18": "yaci bham", "8.2.8": "na ṅisambuddhyoḥ", "6.4.129": "bhasya", "6.4.134": "allopo 'naḥ", "6.4.136": "vibhāṣā ṅiśyoḥ",
    "6.4.137": "na saṁyogād vamantāt", "8.4.55": "khari ca",
    "1.2.45": "arthavad adhātur apratyayaḥ prātipadikam", "1.4.7": "śeṣo ghy asakhi", "7.3.111": "gher ṅiti", "7.3.119": "ac ca gheḥ", "7.3.120": "āṅo nāstriyām",
    "7.3.108": "hrasvasya guṇaḥ", "7.3.109": "jasi ca", "6.1.110": "ṅasiṅasoś ca", "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.4.37": "padāntasya",
    "1.1.53": "ṅic ca", "6.4.8": "sarvanāmasthāne cāsambuddhau", "6.4.11": "aptṛntṛcsvasṛnaptṛneṣṭṛtvaṣṭṛkṣattṛhotṛpotṛpraśāstṝṇām", "7.3.110": "ṛto ṅi sarvanāmasthānayoḥ",
    "6.1.103": "tasmāc chaso naḥ puṁsi", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade",
    "1.4.3": "yū stryākhyau nadī", "4.1.5": "ṛnnebhyo ṅīp", "3.1.133": "ṇvultṛcau", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "7.3.112": "āṇ nadyāḥ", "7.3.107": "ambārthanadyor hrasvaḥ",
    "6.1.105": "dīrghāj jasi ca", "8.3.57": "iṇkoḥ",
    "4.1.4": "ajādyataṣ ṭāp", "7.1.18": "auṅ āpaḥ", "7.3.116": "ṅer ām nadyāmnībhyaḥ", "7.3.113": "yāḍ āpaḥ", "7.3.105": "āṅi cāpaḥ", "7.3.106": "sambuddhau ca",
    "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "6.1.69": "eṅhrasvāt sambuddheḥ", "1.1.56": "sthānivad ādeśo 'nalvidhau",
    "8.4.53": "jhalāṁ jaś jhaśi",
    "8.2.44": "lvādibhyaḥ", "2.4.36": "ado jagdhir lyap ti kiti", "8.2.30": "coḥ kuḥ", "8.2.40": "jhaṣas tathor dho 'dhaḥ", "8.2.42": "radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ",
    "3.1.91": "dhātoḥ", "3.1.93": "kṛd atiṅ", "1.1.26": "ktaktavatū niṣṭhā", "3.2.102": "niṣṭhā", "1.2.46": "kṛttaddhitasamāsāś ca", "4.1.1": "ṅyāpprātipadikāt",
    "6.4.37": "anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti", "7.2.10": "ekāca upadeśe 'nudāttāt", "1.4.57": "cādayo 'sattve", "1.4.58": "prādayaḥ", "1.4.59": "upasargāḥ kriyāyoge",
    "1.3.4": "na vibhaktau tusmāḥ", "1.3.5": "ādir ñiṭuḍavaḥ", "1.3.6": "ṣaḥ pratyayasya", "1.1.60": "adarśanaṁ lopaḥ", "1.1.47": "mid aco 'ntyāt paraḥ",
    "1.4.13": "yasmāt pratyayavidhis tadādi pratyaye 'ṅgam", "1.4.104": "vibhaktiś ca", "7.3.50": "ṭhasyekaḥ", "7.1.2": "āyaneyīnīyiyaḥ phaḍhakhacchaghāṁ pratyayādīnām",
    "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "6.1.65": "ṇo naḥ", "6.4.71": "luṅlaṅlṛṅkṣv aḍ udāttaḥ", "7.1.70": "ugidacāṁ sarvanāmasthāne 'dhātoḥ", "7.2.35": "ārdhadhātukasyeḍ valādeḥ",
    "1.1.1": "vṛddhir ādaic", "1.1.2": "adeṅ guṇaḥ", "1.1.3": "iko guṇavṛddhī", "1.1.4": "na dhātulopa ārdhadhātuke",
    "1.1.5": "kṅiti ca", "1.1.6": "dīdhīvevīṭām", "1.1.7": "halo 'nantarāḥ saṁyogaḥ", "1.1.8": "mukhanāsikāvacano 'nunāsikaḥ",
    "1.1.9": "tulyāsyaprayatnaṁ savarṇam", "1.1.10": "nājjhalau", "1.1.11": "īdūdeddvivacanaṁ pragṛhyam",
    "1.1.15": "ot", "1.1.27": "sarvādīni sarvanāmāni", "1.1.35": "svam ajñātidhanākhyāyām", "1.1.42": "śi sarvanāmasthānam",
    "1.1.43": "suḍ anapuṁsakasya", "1.1.44": "na veti vibhāṣā", "1.1.46": "ādyantau ṭakitau", "1.1.49": "ṣaṣṭhī sthāneyogā",
    "1.1.50": "sthāne 'ntaratamaḥ", "1.1.51": "ur aṇ raparaḥ", "1.1.52": "alo 'ntyasya", "1.1.54": "ādeḥ parasya",
    "1.1.55": "anekāl śit sarvasya", "1.1.56": "sthānivad ādeśo 'nalvidhau", "1.1.62": "pratyayalope pratyayalakṣaṇam",
    "1.1.63": "na lumatāṅgasya", "1.1.64": "aco 'ntyādi ṭi", "1.1.65": "alo 'ntyāt pūrva upadhā", "1.1.66": "tasminn iti nirdiṣṭe pūrvasya",
    "1.1.67": "tasmād ity uttarasya", "1.1.69": "aṇudit savarṇasya cāpratyayaḥ", "1.1.70": "taparas tatkālasya", "1.1.71": "ādir antyena sahetā",
    "1.1.72": "yena vidhis tadantasya", "1.2.4": "sārvadhātukam apit", "1.2.45": "arthavad adhātur apratyayaḥ prātipadikam",
    "1.2.46": "kṛttaddhitasamāsāś ca", "1.3.2": "upadeśe 'janunāsika it", "1.3.3": "halantyam", "1.3.7": "cuṭū", "1.3.8": "laśakv ataddhite",
    "1.3.9": "tasya lopaḥ", "1.3.10": "yathāsaṅkhyam anudeśaḥ samānām", "1.3.12": "anudāttaṅita ātmanepadam", "1.4.2": "vipratiṣedhe paraṁ kāryam",
    "1.4.10": "hrasvaṁ laghu", "1.4.14": "suptiṅantaṁ padam", "1.4.23": "kārake", "1.4.24": "dhruvam apāye 'pādānam", "1.4.32": "karmaṇā yam abhipraiti sa sampradānam",
    "1.4.42": "sādhakatamaṁ karaṇam", "1.4.45": "ādhāro 'dhikaraṇam", "1.4.49": "kartur īpsitatamaṁ karma", "1.4.54": "svatantraḥ kartā",
    "1.4.99": "laḥ parasmaipadam", "1.4.101": "tiṅas trīṇi trīṇi prathamamadhyamottamāḥ", "2.3.1": "anabhihite", "2.3.2": "karmaṇi dvitīyā",
    "2.3.13": "caturthī sampradāne", "2.3.18": "kartṛkaraṇayos tṛtīyā", "2.3.28": "apādāne pañcamī", "2.3.36": "saptamy adhikaraṇe ca",
    "2.3.46": "prātipadikārthaliṅgaparimāṇavacanamātre prathamā", "2.3.50": "ṣaṣṭhī śeṣe", "2.4.76": "", "3.1.1": "pratyayaḥ", "3.1.2": "paraś ca",
    "3.1.68": "kartari śap", "3.1.85": "", "3.2.123": "vartamāne laṭ", "3.3.14": "", "3.4.6": "", "3.4.69": "laḥ karmaṇi ca bhāve cākarmakebhyaḥ",
    "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "3.4.79": "ṭita ātmanepadānāṁ ṭere", "3.4.80": "thāsas se",
    "3.4.113": "tiṅśit sārvadhātukam", "4.1.2": "svaujasamauṭchaṣṭābhyāmbhisṅebhyāmbhyasṅasibhyāmbhyasṅasosāṅṅyossup",
    "6.1.66": "lopo vyor vali", "6.1.68": "halṅyābbhyo dīrghāt sutisy apṛktaṁ hal", "6.1.69": "eṅhrasvāt sambuddheḥ", "6.1.71": "hrasvasya piti kṛti tuk",
    "6.1.72": "saṁhitāyām", "6.1.73": "che ca", "6.1.77": "iko yaṇ aci", "6.1.78": "eco 'yavāyāvaḥ", "6.1.84": "ekaḥ pūrvaparayoḥ",
    "6.1.85": "antādivac ca", "6.1.87": "ād guṇaḥ", "6.1.88": "vṛddhir eci", "6.1.97": "ato guṇe", "6.1.101": "akaḥ savarṇe dīrghaḥ",
    "6.1.102": "prathamayoḥ pūrvasavarṇaḥ", "6.1.103": "tasmāc chaso naḥ puṁsi", "6.1.107": "ami pūrvaḥ", "6.1.111": "ṛta ut",
    "6.1.113": "ato ror aplutād aplute", "6.1.114": "haśi ca", "6.1.125": "plutapragṛhyā aci nityam", "6.4.1": "aṅgasya", "6.4.3": "nāmi",
    "6.4.11": "", "6.4.66": "ghumāsthāgāpājahātisāṁ hali", "6.4.77": "aci śnudhātubhruvāṁ yvor iyaṅuvaṅau", "7.1.3": "jho 'ntaḥ", "7.1.5": "",
    "7.1.9": "ato bhisa ais", "7.1.12": "ṭāṅasiṅasām inātsyāḥ", "7.1.13": "ṅer yaḥ", "7.1.23": "svamor napuṁsakāt", "7.1.54": "hrasvanadyāpo nuṭ",
    "7.1.94": "ṛd uśanaspurudaṁso 'nehasāṁ ca", "7.2.81": "āto ṅitaḥ", "7.2.102": "tyadādīnām aḥ", "7.2.106": "", "7.3.77": "iṣugamiyamāṁ chaḥ",
    "7.3.84": "sārvadhātukārdhadhātukayoḥ", "7.3.101": "ato dīrgho yañi", "7.3.102": "supi ca", "7.3.103": "bahuvacane jhaly et", "7.3.104": "osi ca",
    "8.1.21": "bahuvacanasya vasnasau", "8.2.1": "pūrvatrāsiddham", "8.2.7": "nalopaḥ prātipadikāntasya", "8.2.24": "rāt sasya", "8.2.26": "jhalo jhali",
    "8.2.37": "ekāco baśo bhaṣ jhaṣantasya sdhvoḥ", "8.2.39": "jhalāṁ jaśo 'nte", "8.2.66": "sasajuṣo ruḥ", "8.3.7": "naś chavy apraśān",
    "8.3.15": "kharavasānayor visarjanīyaḥ", "8.3.23": "mo 'nusvāraḥ", "8.3.32": "ṅamo hrasvād aci ṅamuṇ nityam", "8.3.33": "maya uño vo vā",
    "8.3.57": "iṇkoḥ", "8.3.59": "ādeśapratyayayoḥ", "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.4.37": "padāntasya", "8.4.40": "stoḥ ścunā ścuḥ",
    "8.4.45": "yaro 'nunāsike 'nunāsiko vā", "8.4.48": "cayo dvitīyāḥ śari pauṣkarasādeḥ", "8.4.53": "jhalāṁ jaś jhaśi", "8.4.54": "abhyāse car ca",
    "8.4.55": "khari ca", "8.4.56": "vāvasāne", "8.4.58": "anusvārasya yayi parasavarṇaḥ", "8.4.62": "jhayo ho 'nyatarasyām", "8.4.64": "halo yamāṁ yami lopaḥ",
    "8.4.65": "jharo jhari savarṇe", "1.2.26": "ral o vyupadhād dhalādeḥ saṁś ca", "3.1.45": "śala igupadhād aniṭaḥ ksaḥ", "7.4.61": "śarpūrvāḥ khayaḥ",
    "6.1.94": "eṅi pararūpam", "1.3.1": "bhūvādayo dhātavaḥ", "1.1.68": "svaṁ rūpaṁ śabdasyāśabdasaṁjñā",
}

# numbers that an owner canvas attached to another sūtra (theorum/56 B2); kept so the trail stays, corrected here
# quotations of theorum/118 (samāsa construction), each verified against the pinned edition by
# research/samasa_construction/verify_quotes.py; they fill texts the curated table lacks, never override it
_Q = Path(__file__).resolve().parents[1] / "research/samasa_construction/QUOTES_VERIFIED.json"
if _Q.exists():
    for _n, _e in json.loads(_Q.read_text(encoding="utf-8"))["entries"].items():
        if _e.get("match") and _n not in TEXT:
            TEXT[_n] = _e["quoted"]

EDITION_DIFFERS = {  # numbers whose text in the pinned PG1 edition is a different rule (other editions count a Kāśikā / vārttika rule here)
    "8.4.48": "cayo dvitīyāḥ śari pauṣkarasādeḥ is a vārttika in the pinned edition, where 8.4.48 = nādinyākrośe putrasya; cited with the Siddhānta-kaumudī number",
}
TYPOGRAPHY = {  # pinned text prints a consonant without virāma where the sūtra has a bare consonant; the curated IAST is kept
    "3.4.102": "pinned text prints the saṁhitā form liṅassīyuṭ (visarga → s before s); the sūtra is cited in its pada form liṅaḥ sīyuṭ",
    "5.4.91": "pinned text prints the saṁhitā form rājāhassakhibhyaṣ ṭac (visarga → s before s); the sūtra is cited in its pada form rājāhaḥsakhibhyaṣ ṭac",
    "7.1.18": "pinned text prints औङ without virāma; the sūtra reads auṅ āpaḥ",
    "7.4.49": "pinned text prints the doubled form syārddhadhātuke (dh doubled after r, 8.4.46); the sūtra is cited as saḥ syārdhadhātuke",
}
MISNUMBERED = {"1.1.6": "1.3.9 tasya lopaḥ", "1.1.15": "1.3.9 tasya lopaḥ"}

# the executed layers: which sūtras each certified packet realizes, and how
COMPILED = {  # theorum/80 record compiler
    "80": ["6.1.77", "6.1.78", "6.1.87", "6.1.88", "6.1.101", "7.3.77", "6.1.73", "6.1.71", "8.4.40", "7.3.84"],
}
META = {  # interpreter / saṁjñā / paribhāṣā sūtras implemented by a certificate
    "162": ["2.4.55", "3.4.83"],
    "161": ["1.3.93"],
    "160": ["1.3.92"],
    "155": ["1.1.49", "1.1.66", "1.1.67", "3.4.115", "3.4.116"],
    "154": ["3.4.84", "7.3.95", "6.4.115", "6.4.116", "8.4.65"],
    "153": ["4.1.1", "4.1.3", "1.1.26", "1.1.39", "1.1.40", "7.1.79", "6.1.5"],
    "152": ["1.3.78"],
    "151": ["3.1.96", "3.2.102", "3.3.10", "3.4.21", "3.4.114", "1.1.26", "1.2.18", "1.2.19", "1.2.8", "3.1.32", "7.3.34"],
    "150": ["1.1.50", "1.1.61", "3.1.32"],
    "149": ["1.2.8", "1.2.10"],
    "148": ["3.1.32"],
    "147": ["3.4.69"],
    "146": ["1.2.11", "1.2.12"],
    "145": ["3.3.139"],
    "144": ["1.2.11", "1.2.12"],
    "143": ["6.4.22"],
    "134": ["1.1.45"],
    "133": ["1.1.20", "1.1.47"],
    "132": ["3.1.32", "1.3.72"],
    "131": ["3.2.115", "3.4.115", "1.2.5", "1.1.56"],
    "130": ["3.3.13", "3.3.15", "3.2.110", "3.4.116", "3.4.114", "3.1.43", "8.3.55"],
    "129": ["3.2.111", "3.3.162", "3.3.161", "3.4.77", "1.3.78", "1.2.4"],
    "128": ["1.1.52", "1.1.55"],
    "127": ["1.1.24", "1.1.47", "6.4.4"],
    "126": ["6.4.10", "6.1.114", "8.3.24"],
    "125": ["6.1.104", "1.1.42", "1.1.43", "1.4.17", "1.4.18", "1.4.7", "1.4.3", "1.1.27", "1.1.47", "1.1.46"],
    "124": ["7.2.91", "1.1.52", "1.1.27"],
    "123": ["6.4.7", "1.4.17", "1.1.42", "5.2.115", "5.2.121", "3.1.134", "3.2.78", "5.1.122"],
    "117": ["3.3.173", "3.4.116"],
    "116": ["3.1.43", "3.4.114"],
    "115": ["3.3.173", "3.4.116"],
    "114": ["2.1.6", "2.1.7", "2.1.5", "1.1.41", "2.4.18", "2.1.52", "2.1.51", "2.4.1", "1.2.43"],
    "113": ["5.3.1", "5.3.2", "5.3.7", "5.3.10", "5.3.15", "1.1.38"],
    "112": ["3.4.114"],
    "111": ["4.1.3", "4.1.1", "4.1.6", "4.1.15", "4.1.16", "4.1.41", "1.4.18", "1.3.6"],
    "110": ["3.1.67", "1.3.13", "1.1.45"],
    "109": ["1.1.47", "5.2.94", "1.1.42", "1.1.43", "1.4.17"],
    "108": ["3.1.22", "3.1.32"],
    "107": ["3.1.91", "3.1.93", "1.2.46", "3.3.18", "3.3.16", "3.3.115", "3.4.67", "3.2.124"],
    "106": ["3.1.7", "3.1.32", "3.4.114", "8.3.57", "1.3.57", "1.3.78"],
    "105": ["3.1.26", "3.1.32", "1.3.78", "1.4.13"],
    "104": ["2.1.3", "2.1.4", "2.1.22", "2.1.24", "2.1.36", "2.1.37", "2.1.40", "2.2.8", "1.2.42", "2.2.23", "2.2.24", "2.2.29", "1.2.43", "1.2.46", "2.4.26"],
    "103": ["4.1.76", "4.1.82", "4.1.83", "4.1.92", "4.1.95", "4.1.105", "4.3.120", "6.4.129", "1.4.18", "1.2.46"],
    "102": ["3.2.115", "1.2.5"],
    "101": ["3.2.110", "3.1.43", "7.2.10"],
    "100": ["3.4.21", "3.3.10", "3.1.96", "7.2.10", "1.2.46"],
    "99": ["1.3.12", "3.4.78"],
    "98": ["1.1.27", "7.1.9"],
    "97": ["3.3.13", "3.3.15", "3.4.114", "1.1.64"],
    "96": ["3.3.162", "3.3.161", "1.1.46"],
    "95": ["3.2.111", "3.4.78", "1.3.78", "1.1.46"],
    "94": ["1.1.27"],
    "93": ["1.1.42"],
    "87": ["8.2.1", "1.1.26"],
    "88": ["1.1.46", "1.1.56", "1.1.52", "1.1.55"],
    "89": ["1.4.3", "3.4.114", "8.3.57", "1.1.46", "1.1.56"],
    "90": ["1.1.42", "1.1.43", "1.1.53", "8.3.57"],
    "91": ["1.2.45", "1.4.7"],
    "92": ["1.4.14", "1.4.17", "1.4.18", "1.1.42", "1.1.43", "6.4.129"],
    "85": ["1.2.46", "3.1.93", "1.4.14"],
    "82": ["1.3.1", "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8", "1.3.9", "1.1.60", "1.1.46", "1.1.47", "3.1.1", "3.1.2", "1.4.13", "6.4.1", "1.4.104"],
    "81": ["1.1.7", "1.1.8", "1.1.9", "1.1.10", "1.1.11", "6.1.125", "1.1.64", "1.1.65", "1.1.72"],
    "58": ["1.1.1", "1.1.2", "1.1.3", "1.1.62", "1.3.3", "1.3.8", "1.3.9", "1.4.2", "3.4.113"],
    "62": ["8.2.1"],
    "78": ["1.1.71", "1.1.69"],
    "79": ["1.1.69"],
    "80": ["1.1.49", "1.1.66", "1.1.67", "6.1.84", "6.1.72", "1.1.69", "1.1.70", "1.1.52", "1.1.55", "1.1.46", "1.3.10", "1.1.50", "1.1.51", "1.4.2", "1.1.1", "1.1.2", "6.4.1"],
}
HAND_CODED = {  # exact finite functions in certified packets: the numbers each packet's source actually carries
    "162": ["2.4.54"],
    "161": ["7.3.78", "7.3.92", "8.2.18", "7.2.60", "7.3.37"],
    "160": ["7.2.59", "7.4.10"],
    "158": ["6.4.35"],
    "155": ["8.4.1", "8.4.2"],
    "153": ["4.1.4", "4.1.5", "4.1.6", "7.1.80", "7.1.81", "7.3.44", "7.1.78", "8.4.39"],
    "152": ["3.2.124", "7.2.82", "7.2.83", "7.4.21", "6.1.97"],
    "151": ["1.2.26", "2.4.36", "2.4.52", "2.4.53", "3.1.25", "6.1.15", "6.1.16", "6.1.50", "6.1.64", "6.1.65", "6.1.77", "6.1.78", "6.1.101", "6.3.111", "6.4.2", "6.4.15", "6.4.19", "6.4.24", "6.4.37", "6.4.42", "6.4.51", "6.4.52", "6.4.64", "6.4.66", "7.1.1", "7.1.58", "7.1.64", "7.1.100", "7.1.102", "7.2.11", "7.2.14", "7.2.15", "7.2.16", "7.2.35", "7.2.37", "7.2.38", "7.2.56", "7.2.114", "7.2.115", "7.2.116", "7.3.32", "7.3.33", "7.3.84", "7.3.85", "7.3.86", "7.4.40", "7.4.42", "7.4.43", "7.4.46", "8.2.30", "8.2.31", "8.2.32", "8.2.36", "8.2.40", "8.2.42", "8.2.43", "8.2.44", "8.2.45", "8.2.52", "8.2.56", "8.2.57", "8.2.77", "8.3.13", "8.3.24", "8.4.1", "8.4.2", "8.4.41", "8.4.53", "8.4.58"],
    "150": ["1.1.46", "1.1.47", "1.1.52", "1.1.55", "1.1.60", "1.1.65", "1.1.1", "1.1.2", "1.2.27", "6.1.1"],
    "149": ["3.1.7", "1.3.62", "6.1.9", "6.1.2", "7.4.79", "6.4.16", "7.4.54", "7.4.55", "7.4.49", "7.4.58", "7.2.49", "7.2.11", "7.2.12", "7.2.38", "2.4.47", "8.3.61"],
    "148": ["3.1.26", "1.3.74", "7.3.36", "7.3.32", "2.4.46", "6.4.92", "6.1.48", "7.1.64", "7.3.86"],
    "147": ["3.1.67", "1.3.13", "7.4.22", "6.4.44", "6.4.43", "6.4.42"],
    "146": ["8.2.28", "7.2.3", "7.2.4", "7.2.5", "7.2.7", "3.1.57", "3.1.52", "7.4.20", "2.4.37", "3.1.45", "7.3.73", "2.4.45", "7.2.73", "8.2.27", "1.2.17", "3.1.48", "6.1.11", "7.4.1", "7.4.93", "7.4.94", "7.3.72", "3.4.110", "7.2.72", "3.1.55", "2.4.77"],
    "145": ["3.4.81", "3.1.35", "3.1.36", "3.1.37", "3.1.38", "3.1.39", "3.1.40", "7.4.70", "7.4.71", "7.4.72", "6.4.78", "7.4.69", "7.4.61", "7.1.34", "6.4.64", "6.1.17", "7.4.67", "7.3.55", "6.4.120", "6.4.121", "6.4.123", "6.4.126", "7.2.61", "7.2.62", "7.2.63", "7.4.11", "7.4.12"],
    "144": ["2.4.52", "2.4.53", "2.4.42", "6.4.48", "7.2.70", "7.2.37", "6.1.50", "6.1.45", "6.4.67", "6.4.66", "6.4.51", "7.3.85", "7.4.29", "7.4.28", "7.4.25", "6.1.15", "6.4.2", "8.3.78", "8.3.79", "6.4.24"],
    "143": ["6.1.68", "8.2.39", "8.4.56", "8.2.73", "8.2.74", "8.2.25", "6.4.36", "7.3.88", "7.3.91", "7.1.100"],
    "141": ["7.1.25"],
    "140": ["6.4.109", "6.4.118", "7.3.87", "7.3.98", "8.4.37"],
    "139": ["6.1.96", "6.4.101", "6.4.119", "7.3.83", "7.3.100", "3.1.83", "6.4.106"],   # 8.2.24 withdrawn by theorum/143 (6.1.68 is the apṛkta rule)
    "137": ["7.2.76", "8.4.40", "3.4.107"],
    "136": ["6.1.6", "7.2.76", "7.2.77", "7.2.78", "7.3.93", "7.2.114", "7.4.21", "7.1.6", "6.4.34", "6.4.114", "6.4.37", "7.3.54", "8.2.36", "8.3.60", "8.2.31", "8.2.32", "8.2.37", "8.3.13", "6.3.111"],
    "135": ["7.3.89", "7.3.90", "6.4.81", "6.4.82", "7.4.60", "7.4.75", "7.4.76", "7.4.77", "7.1.102", "8.2.41", "8.3.57"],
    "134": ["3.1.82", "6.4.24", "7.3.79", "6.1.16", "8.4.40", "8.4.39", "8.4.44"],
    "133": ["2.4.72", "2.4.75", "6.1.10", "3.1.78", "6.4.111", "7.1.4", "7.1.58", "6.4.23", "8.2.38", "8.2.30", "8.3.24", "8.4.58"],
    "132": ["3.1.25", "3.1.69", "3.1.73", "3.1.74", "3.1.77", "3.1.79", "3.1.81", "6.1.64", "7.3.86", "8.2.77", "7.3.74", "7.3.80", "6.4.110", "6.4.108", "6.4.107", "6.4.77", "6.4.87", "6.4.112", "6.4.113", "8.4.2"],
    "131": ["3.4.82", "6.1.8", "7.4.59", "7.4.62", "7.4.66", "7.4.73", "8.4.54", "7.2.13", "7.2.115", "7.2.116", "6.4.98", "6.1.77"],
    "130": ["3.1.33", "3.1.44", "2.4.77", "3.1.55", "2.4.85", "3.4.109", "7.1.5", "3.4.107", "7.2.35", "7.2.1", "7.3.96", "6.4.88", "8.2.26", "8.2.40", "8.4.53", "8.4.55", "6.4.143", "7.4.50", "7.4.51", "7.4.52", "8.2.29", "8.3.59", "8.4.41"],
    "129": ["3.1.68", "3.4.79", "3.4.80", "3.4.86", "3.4.87", "3.4.89", "3.4.90", "3.4.91", "3.4.92", "3.4.93", "3.4.99", "3.4.100", "3.4.101", "3.4.102", "3.4.103", "3.4.105", "3.4.106", "3.4.108", "7.1.3", "7.3.77", "6.1.73", "7.3.84", "6.1.78", "6.1.65", "6.4.71", "6.4.72", "6.1.90", "7.2.79", "7.2.80", "7.2.81", "6.4.105", "7.3.101", "6.1.87", "6.1.97", "6.1.101", "6.1.88", "6.1.66", "8.2.23", "8.2.66", "8.3.15"],
    "128": ["4.1.4", "6.1.97", "7.1.11", "7.2.103", "7.2.106", "7.2.108", "7.2.109", "7.2.110", "7.2.111", "7.2.112", "7.2.113"],
    "127": ["7.1.21", "7.1.22", "7.1.53", "7.1.55", "7.1.98", "7.2.84", "7.2.99", "7.2.100", "7.2.102", "6.4.7", "8.4.41", "8.4.45", "8.4.56"],
    "125": ["7.1.24", "7.1.23", "7.1.19", "7.1.20", "7.1.73", "7.1.72", "7.1.17", "7.1.14", "7.1.15", "7.1.52", "7.1.9", "7.1.12", "7.1.13", "7.1.18", "7.1.54", "6.4.3", "7.3.120", "7.3.118", "7.3.119", "7.3.111", "7.3.112", "7.3.114", "7.3.113", "7.3.116", "7.3.105", "7.3.106", "7.3.107", "7.3.108", "7.3.109", "7.3.110", "7.1.94", "6.4.11", "7.3.102", "7.3.103", "7.3.104", "7.1.70", "6.4.14", "6.4.13", "6.4.12", "6.4.8", "6.1.68", "6.1.69", "6.4.134", "8.4.40", "6.1.107", "6.1.103", "6.1.102", "6.1.110", "6.1.111", "6.1.88", "6.1.87", "6.1.101", "6.1.78", "6.1.77", "8.2.7", "8.2.23", "8.2.24", "8.2.39", "8.4.55", "8.3.59", "8.4.2", "8.2.66", "8.3.15"],
    "124": ["7.2.86", "7.2.87", "7.2.88", "7.2.89", "7.2.90", "7.2.92", "7.2.93", "7.2.94", "7.2.95", "7.2.96", "7.2.97", "7.1.27", "7.1.28", "7.1.29", "7.1.30", "7.1.31", "7.1.32", "7.1.33", "6.1.107", "6.1.101", "6.1.97", "8.2.66", "8.3.15"],
    "123": ["6.4.13", "6.4.12", "6.1.68", "8.2.7", "8.2.8", "7.1.23", "7.1.20", "8.3.59", "8.4.2", "8.2.66", "8.3.15"],
    "117": ["3.4.102", "3.4.107", "3.4.105", "3.4.106", "6.1.66", "7.2.35", "7.2.10", "8.4.55", "8.3.59", "8.4.41"],
    "116": ["3.1.44", "6.4.71", "6.4.72", "6.1.90", "7.2.35", "7.2.10", "8.2.26", "8.2.40", "8.4.53", "8.4.55", "8.3.59", "8.4.41", "7.1.3", "7.1.5", "8.2.66", "8.3.15"],
    "115": ["3.4.103", "3.4.104", "7.2.79", "6.4.67", "3.4.100", "3.4.101", "3.4.108", "8.2.66", "8.3.15"],
    "114": ["2.4.71", "2.4.82", "2.4.83", "2.4.17", "4.1.21", "6.4.148", "5.4.92", "6.1.78", "7.1.24"],
    "113": ["2.4.71", "7.2.102", "6.1.97", "7.2.103", "7.2.104", "5.3.3", "5.3.5", "5.3.11", "8.2.66", "8.3.15"],
    "112": ["3.1.33", "7.2.35", "7.2.10", "8.4.55", "8.2.40", "8.4.53", "8.3.59", "3.4.79", "3.4.80", "7.1.3", "7.2.81", "6.1.66", "6.1.97", "7.3.101", "2.4.85", "6.4.143", "7.4.51", "7.4.50", "7.4.52", "8.2.66", "8.3.15"],
    "111": ["7.3.44", "7.1.81", "6.4.150", "6.4.148"],
    "110": ["1.1.5", "6.4.66", "6.1.15", "6.1.108", "7.1.3", "6.1.97", "3.4.79"],
    "109": ["7.1.70", "6.4.14", "8.2.23", "8.2.9"],
    "108": ["7.4.27", "6.1.9", "7.4.59", "7.4.60", "7.4.62", "8.4.54", "7.4.82", "7.4.83", "7.4.85", "8.3.24", "8.4.58", "1.1.5", "3.4.79"],
    "107": ["7.1.1", "7.2.115", "7.2.116", "7.3.52", "7.3.84", "7.3.86", "1.1.51", "6.1.78", "8.4.2", "6.1.97"],
    "106": ["6.1.9", "7.4.79", "7.4.59", "7.4.60", "7.4.62", "7.4.66", "8.4.54", "7.2.35", "7.2.10", "7.2.58", "1.2.9", "6.4.16", "7.1.100", "8.2.77", "8.3.59", "8.2.30", "7.4.54", "7.4.49", "7.4.58", "3.4.79"],
    "105": ["7.2.115", "7.2.116", "6.4.92", "7.3.36", "7.3.37", "7.3.86", "1.1.51", "7.3.84", "6.1.78", "7.1.3", "6.1.97", "7.3.101"],
    "104": ["2.4.71", "2.2.30", "2.2.34", "6.3.46", "5.4.91", "6.4.144", "8.2.7", "1.2.48", "6.1.101", "6.1.87", "1.1.51", "8.4.1"],
    "103": ["7.2.117", "7.2.118", "6.4.146", "6.4.148", "7.3.50", "6.1.78"],
    "102": ["3.4.82", "6.1.8", "6.1.1", "6.1.4", "7.4.59", "7.4.60", "7.4.62", "7.4.66", "7.4.73", "8.4.54", "6.4.88", "7.2.115", "7.2.116", "6.4.98", "7.2.13", "7.2.35", "1.1.5", "6.1.77", "6.1.78", "8.2.66", "8.3.15"],
    "101": ["3.1.44", "3.1.55", "2.4.77", "6.4.88", "7.2.1", "7.3.96", "8.3.59", "8.4.41", "3.4.109", "6.4.71", "3.4.100", "3.4.101", "3.4.99", "7.1.3", "8.2.23", "7.3.101", "8.2.66", "8.3.15"],
    "100": ["7.2.35", "7.2.11", "1.1.5", "7.3.84", "6.1.78", "6.4.37", "8.3.24", "8.4.58"],
    "99": ["6.4.71", "6.4.72", "6.1.90", "7.2.81", "6.1.66", "6.1.97", "6.1.87", "7.1.3", "7.3.101", "3.4.79", "3.4.80", "3.4.90", "3.4.91", "3.4.92", "3.4.93", "3.4.102", "3.4.105", "3.4.106", "3.4.107", "7.2.79", "8.2.66", "8.3.15"],
    "98": ["7.3.114", "7.1.52", "7.2.102", "7.2.106", "4.1.4", "7.1.18", "7.3.116", "7.3.105", "7.3.106", "6.1.68", "6.1.69", "6.1.87", "6.1.88", "6.1.101", "6.1.107", "6.1.78", "6.1.97", "8.2.66", "8.3.15"],
    "97": ["3.1.33", "7.2.35", "7.2.58", "7.3.84", "6.1.78", "8.3.59", "2.4.85", "6.4.143", "7.4.50", "7.4.51", "7.1.3", "7.3.101", "8.2.66", "8.3.15"],
    "96": ["3.4.85", "3.4.86", "3.4.87", "3.4.89", "3.4.92", "6.4.105", "3.4.103", "3.4.108", "7.2.79", "7.2.80", "6.1.66", "6.1.97", "3.4.100", "3.4.101", "3.4.99", "7.1.3", "8.2.66", "8.3.15"],
    "95": ["6.4.71", "3.4.100", "3.4.101", "3.4.99", "7.1.3", "8.2.23", "7.3.101", "8.2.66", "8.3.15"],
    "94": ["7.1.17", "7.1.14", "7.1.15", "7.1.52", "7.3.103", "8.3.59", "7.2.102", "7.2.106", "6.1.97", "6.1.87", "7.1.9", "7.1.12", "7.1.13", "7.3.102", "6.1.102", "6.1.103", "6.1.107", "6.1.78", "8.4.2", "8.2.66", "8.3.15"],
    "93": ["7.1.23", "7.1.24", "7.1.19", "7.1.20", "7.1.72", "7.1.73", "6.4.8", "6.1.87", "7.1.9", "7.1.12", "7.1.13", "7.3.102", "7.3.103", "7.1.54", "6.4.3", "8.4.2", "8.3.59", "7.3.108", "6.1.69", "8.2.66", "8.3.15"],
    "85": ["6.4.37", "7.2.10"],
    "86": ["6.1.64", "6.4.37", "7.2.10"],
    "87": ["8.2.30", "8.2.40", "8.2.42", "8.2.44", "8.4.53"],
    "92": ["6.4.8", "6.1.68", "8.2.7", "8.2.8", "6.4.134", "6.4.136", "6.4.137", "8.4.40", "8.2.39", "8.4.55", "8.4.56", "8.2.66", "8.3.15"],
    "91": ["7.3.111", "7.3.119", "7.3.120", "7.3.108", "7.3.109", "6.1.110", "6.1.102", "6.1.103", "6.1.107", "6.1.77", "6.1.78", "6.1.88", "7.1.54", "6.4.3", "8.4.1", "8.4.2", "8.4.37", "6.1.69", "8.3.59", "8.2.66", "8.3.15"],
    "90": ["7.1.94", "6.4.8", "6.4.11", "7.3.110", "1.1.51", "6.1.111", "8.2.24", "6.1.102", "6.1.103", "6.1.77", "7.1.54", "6.4.3", "8.4.1", "8.3.59", "6.1.68", "8.2.7", "8.2.66", "8.3.15"],
    "89": ["4.1.5", "3.1.133", "7.3.84", "1.1.51", "6.1.64", "7.3.112", "7.3.116", "7.1.54", "7.3.107", "6.1.68", "6.1.69", "6.1.77", "6.1.102", "6.1.105", "6.1.107", "6.1.88", "6.1.101", "8.3.59", "8.2.66", "8.3.15"],
    "88": ["4.1.4", "7.1.18", "7.3.116", "7.3.113", "7.1.54", "7.3.105", "7.3.106", "6.1.68", "6.1.69", "6.1.87", "6.1.88", "6.1.101", "6.1.107", "6.1.78", "8.2.66", "8.3.15"],
    "58": ["6.1.77", "6.1.78", "6.1.87", "6.1.88", "6.1.101", "7.3.77", "6.1.73", "8.4.40", "7.3.84", "1.3.8", "1.3.3", "1.3.9", "3.4.113"],
    "63": ["1.3.2", "1.3.3", "1.3.7", "1.3.8", "1.3.9", "1.4.2", "1.4.14", "4.1.2", "6.1.69", "6.1.78", "6.1.87", "6.1.88", "6.1.97", "6.1.101", "6.1.102", "6.1.103", "6.1.107", "6.4.3", "7.1.9", "7.1.12", "7.1.13", "7.1.54", "7.3.102", "7.3.103", "7.3.104", "8.2.1", "8.2.66", "8.3.15", "8.3.59", "8.4.2", "8.4.37"],
    "64": ["1.1.62", "1.3.3", "1.3.8", "1.3.9", "1.4.99", "1.4.101", "3.1.68", "3.2.123", "3.4.78", "3.4.113", "6.1.73", "6.1.78", "6.1.97", "6.1.101", "7.1.3", "7.3.77", "7.3.84", "7.3.101", "8.2.1", "8.2.66", "8.3.15", "8.4.40"],
    "65": ["1.1.51", "1.1.63", "3.4.6", "6.1.68", "6.1.97", "6.1.111", "6.1.113", "6.4.11", "7.1.23", "7.1.94", "7.2.102", "8.2.1", "8.2.7", "8.2.24", "8.2.39", "8.3.15", "8.4.56"],
    "66": ["1.3.3", "1.3.9", "1.3.12", "2.4.76", "3.1.68", "3.1.85", "3.4.78", "3.4.79", "3.4.80", "3.4.113", "6.1.66", "6.1.78", "6.1.87", "6.1.97", "6.1.101", "6.4.66", "7.1.3", "7.1.5", "7.2.81", "7.3.84", "7.3.101", "8.2.1"],
    "67": ["6.1.87", "6.1.113", "6.1.114", "6.4.77", "7.2.102", "7.2.106", "8.1.21", "8.2.1", "8.2.66", "8.3.15", "8.3.23"],
    "68": ["1.1.62", "1.4.23", "1.4.24", "1.4.32", "1.4.42", "1.4.45", "1.4.49", "1.4.54", "2.3.1", "2.3.2", "2.3.13", "2.3.18", "2.3.28", "2.3.36", "2.3.46", "2.3.50", "3.4.69"],
}
PACKET_OF = {"58": "paninian_seam_calculus", "63": "sup_vibhakti_resolver_ladder", "64": "ting_lat_parasmaipada", "65": "stem_classes_gayatri_coverage", "66": "lat_atmanepada", "67": "pada_to_line_external_sandhi", "68": "karaka_vibhakti_carrier", "80": "paninian_instruction_format", "81": "paninian_samjna_sound_layer", "82": "paninian_it_samjna_compiled", "85": "nirukta_nama_akhyatajani", "86": "nirukta_dhatupatha_nama", "87": "tripadi_nishtha_compiled", "88": "ap_stem_sup_compiled", "89": "ngi_stem_sup_compiled", "90": "r_stem_sup_compiled", "91": "ghi_stem_sup_compiled", "92": "hal_stem_sup_compiled", "93": "napumsaka_sup_compiled", "94": "sarvanama_sup_compiled", "95": "lan_parasmaipada_compiled", "96": "lot_lin_parasmaipada_compiled", "97": "lrt_lut_parasmaipada_compiled", "98": "sarvanama_ap_sup_compiled", "99": "atmanepada_lan_lot_lin_compiled", "100": "krt_ktva_tumun_tavya_compiled", "101": "lun_parasmaipada_compiled", "102": "lit_parasmaipada_compiled", "103": "taddhita_an_in_yan_compiled", "104": "samasa_compiled", "105": "nic_causative_compiled", "106": "san_desiderative_compiled", "107": "krt_ghan_lyut_nvul_satr_compiled", "108": "yan_intensive_compiled", "109": "ugit_at_stem_sup_compiled", "110": "passive_yak_compiled", "111": "stri_pratyaya_compiled", "112": "atmanepada_lrt_lut_compiled", "113": "pronominal_taddhita_adverbs_compiled", "114": "avyayibhava_dvigu_compiled", "115": "asirlin_parasmaipada_compiled", "116": "atmanepada_lun_compiled", "117": "asirlin_atmanepada_compiled", "123": "in_stem_sup_compiled", "124": "yusmad_asmad_sup_compiled", "125": "sup_rule_table_engine", "126": "sup_rule_table_engine", "127": "sup_rule_table_engine", "128": "sup_rule_table_engine", "129": "ting_rule_table_engine", "130": "ting_rule_table_engine", "131": "ting_rule_table_engine", "132": "ting_rule_table_engine", "133": "ting_rule_table_engine", "134": "ting_rule_table_engine", "135": "ting_rule_table_engine", "136": "ting_rule_table_engine", "137": "ting_rule_table_engine", "138": "ting_rule_table_engine", "139": "ting_rule_table_engine", "140": "ting_rule_table_engine", "141": "sup_rule_table_engine", "142": "panini_kernel", "143": "ting_rule_table_engine", "144": "ting_rule_table_engine", "145": "ting_rule_table_engine", "146": "ting_rule_table_engine", "147": "ting_rule_table_engine", "148": "ting_rule_table_engine", "149": "ting_rule_table_engine", "150": "panini_isa", "151": "krt_rule_table_engine", "152": "krt_rule_table_engine", "153": "krdanta_sup", "154": "pg_replay", "155": "pg_written_replay", "156": "pg_modal_registers", "157": "pg_modal_registers_ii", "158": "ting_rule_table_engine", "159": "pg_modal_registers_iii", "160": "ting_rule_table_engine", "161": "ting_rule_table_engine", "162": "ting_rule_table_engine", "163": "ting_rule_table_engine"}
THEOREM_FILE = {
    "56": "theorum/56_canvas_operators_nativized_theorem.md", "58": "theorum/58_paninian_seam_calculus_theorem.md",
    "60": "theorum/60_seam_compensated_confluence_verdict_theorem.md", "61": "theorum/61_rewrite_rules_as_cut_module_operators_theorem.md",
    "62": "theorum/62_silence_vibration_sutra_flow_theorem.md", "63": "theorum/63_sup_vibhakti_resolver_ladder_theorem.md",
    "64": "theorum/64_ting_lat_parasmaipada_theorem.md", "65": "theorum/65_stem_classes_gayatri_coverage_theorem.md",
    "66": "theorum/66_lat_atmanepada_theorem.md", "67": "theorum/67_pada_to_line_external_sandhi_theorem.md",
    "68": "theorum/68_karaka_vibhakti_carrier_theorem.md", "77": "theorum/77_semantic_paninian_typed_claim_normal_form.md",
    "78": "theorum/78_shaiva_sources_maheshvara_spanda_pratyabhijna_theorem.md", "79": "theorum/79_shaiva_sources_varga_grid_crystal_theorem.md",
    "80": "theorum/80_paninian_instruction_format_theorem.md",
    "81": "theorum/81_paninian_samjna_sound_layer_theorem.md",
    "82": "theorum/82_paninian_it_samjna_compiled_theorem.md",
    "85": "theorum/85_nirukta_nama_akhyatajani_theorem.md",
    "86": "theorum/86_nirukta_dhatupatha_nama_theorem.md",
    "87": "theorum/87_tripadi_nishtha_compiled_theorem.md",
    "88": "theorum/88_ap_stem_sup_compiled_theorem.md",
    "89": "theorum/89_ngi_stem_sup_compiled_theorem.md",
    "90": "theorum/90_r_stem_sup_compiled_theorem.md",
    "91": "theorum/91_ghi_stem_sup_compiled_theorem.md",
    "92": "theorum/92_hal_stem_sup_compiled_theorem.md",
    "93": "theorum/93_napumsaka_sup_compiled_theorem.md",
    "94": "theorum/94_sarvanama_sup_compiled_theorem.md",
    "95": "theorum/95_lan_parasmaipada_compiled_theorem.md",
    "96": "theorum/96_lot_lin_parasmaipada_compiled_theorem.md",
    "97": "theorum/97_lrt_lut_parasmaipada_compiled_theorem.md",
    "98": "theorum/98_sarvanama_ap_sup_compiled_theorem.md",
    "99": "theorum/99_atmanepada_lan_lot_lin_compiled_theorem.md",
    "100": "theorum/100_krt_ktva_tumun_tavya_compiled_theorem.md",
    "101": "theorum/101_lun_parasmaipada_compiled_theorem.md",
    "102": "theorum/102_lit_parasmaipada_compiled_theorem.md",
    "103": "theorum/103_taddhita_an_in_yan_compiled_theorem.md",
    "104": "theorum/104_samasa_compiled_theorem.md",
    "105": "theorum/105_nic_causative_compiled_theorem.md",
    "106": "theorum/106_san_desiderative_compiled_theorem.md",
    "107": "theorum/107_krt_ghan_lyut_nvul_satr_compiled_theorem.md",
    "108": "theorum/108_yan_intensive_compiled_theorem.md",
    "109": "theorum/109_ugit_at_stem_sup_compiled_theorem.md",
    "110": "theorum/110_passive_yak_compiled_theorem.md",
    "111": "theorum/111_stri_pratyaya_compiled_theorem.md",
    "112": "theorum/112_atmanepada_lrt_lut_compiled_theorem.md",
    "113": "theorum/113_pronominal_taddhita_adverbs_compiled_theorem.md",
    "114": "theorum/114_avyayibhava_dvigu_compiled_theorem.md",
    "115": "theorum/115_asirlin_parasmaipada_compiled_theorem.md",
    "116": "theorum/116_atmanepada_lun_compiled_theorem.md",
    "117": "theorum/117_asirlin_atmanepada_compiled_theorem.md",
    "118": "theorum/118_samasa_mathematical_construction_theorem.md",
    "119": "theorum/119_samasa_construction_ii_uttarapada_aluk_samasanta_theorem.md",
    "120": "theorum/120_krt_mathematical_construction_theorem.md",
    "121": "theorum/121_taddhita_mathematical_construction_theorem.md",
    "122": "theorum/122_krt_samasa_source_repairs_theorem.md",
    "123": "theorum/123_in_stem_sup_compiled_theorem.md",
    "124": "theorum/124_yusmad_asmad_sup_compiled_theorem.md",
    "125": "theorum/125_sup_rule_table_engine_theorem.md",
    "126": "theorum/126_sup_rule_table_engine_s_i_u_r_classes_theorem.md",
    "127": "theorum/127_sup_rule_table_engine_numerals_theorem.md",
    "128": "theorum/128_sup_rule_table_engine_pronouns_theorem.md",
    "129": "theorum/129_ting_rule_table_engine_theorem.md",
    "130": "theorum/130_ting_rule_table_engine_ardhadhatuka_theorem.md",
    "131": "theorum/131_ting_rule_table_engine_lit_theorem.md",
    "132": "theorum/132_ting_rule_table_engine_vikarana_classes_theorem.md",
    "133": "theorum/133_ting_rule_table_engine_luk_slu_snam_theorem.md",
    "134": "theorum/134_ting_rule_table_engine_nasal_breadth_theorem.md",
    "135": "theorum/135_ting_rule_table_engine_adadi_juhotyadi_breadth_theorem.md",
    "136": "theorum/136_ting_rule_table_engine_adadi_consonant_roots_theorem.md",
    "137": "theorum/137_independent_oracle_audit_theorem.md",
    "138": "theorum/138_generalisation_test_theorem.md",
    "139": "theorum/139_ting_rule_table_engine_open_lane_theorem.md",
    "140": "theorum/140_ting_rule_table_engine_open_lane_ii_theorem.md",
    "141": "theorum/141_sup_generalisation_test_theorem.md",
    "142": "theorum/142_panini_kernel_theorem.md",
    "143": "theorum/143_ting_rule_table_engine_open_lane_closed_theorem.md",
    "144": "theorum/144_ting_rule_table_engine_ardhadhatuka_lane_theorem.md",
    "145": "theorum/145_ting_rule_table_engine_lit_breadth_lrn_theorem.md",
    "146": "theorum/146_ting_rule_table_engine_lun_breadth_theorem.md",
    "147": "theorum/147_ting_rule_table_engine_karmani_theorem.md",
    "148": "theorum/148_ting_rule_table_engine_nic_theorem.md",
    "149": "theorum/149_ting_rule_table_engine_san_theorem.md",
    "150": "theorum/150_panini_isa_theorem.md",
    "151": "theorum/151_krt_rule_table_engine_theorem.md",
    "152": "theorum/152_krt_rule_table_engine_satr_sanac_theorem.md",
    "153": "theorum/153_krdanta_declension_theorem.md",
    "154": "theorum/154_written_construction_replay_theorem.md",
    "155": "theorum/155_written_construction_replay_ii_theorem.md",
    "156": "theorum/156_written_modal_registers_replay_theorem.md",
    "157": "theorum/157_written_modal_registers_replay_ii_theorem.md",
    "158": "theorum/158_ting_rule_table_engine_sas_correction_theorem.md",
    "159": "theorum/159_written_modal_registers_replay_iii_theorem.md",
    "160": "theorum/160_ting_rule_table_engine_written_roots_theorem.md",
    "161": "theorum/161_ting_rule_table_engine_rows_for_written_roots_theorem.md",
    "162": "theorum/162_ting_rule_table_engine_vid_anj_caks_theorem.md",
    "163": "theorum/163_gana_sweep_adadi_juhotyadi_rudhadi_tanadi_theorem.md",
}
SCAN = [THEOREM_FILE[k] for k in THEOREM_FILE] + ["theorum/70_angatva_pramana_ladder_theorem.md", "theorum/74_lopa_ledger_contraction_theorem.md"]
NUM = re.compile(r"\b([1-8])\.([1-4])\.([0-9]{1,3})\b")


def key(n: str) -> tuple[int, int, int]:
    a, p, s = n.split(".")
    return (int(a), int(p), int(s))


def build() -> dict:
    cited: dict[str, set[str]] = {}
    for rel in SCAN:
        p = ROOT / rel
        if not p.exists():
            continue
        for m in NUM.finditer(p.read_text(encoding="utf-8")):
            n = ".".join(m.groups())
            cited.setdefault(n, set()).add(rel)
    for rel in sorted((ROOT / "proof_lab").glob("*.py")):
        if rel.name.startswith("astadhyayi_ledger") or rel.name.startswith("test_"):
            continue
        txt = rel.read_text(encoding="utf-8")
        if "theorum" not in txt and "sūtra" not in txt and "sutra" not in txt.lower():
            continue
        for m in NUM.finditer(txt):
            cited.setdefault(".".join(m.groups()), set()).add(rel.relative_to(ROOT).as_posix())
    entries: dict[str, dict] = {}
    deva = load_sutrapatha()
    numbers = set(cited) | set(TEXT) | set(MISNUMBERED)
    for layer, table in (("compiled", COMPILED), ("meta", META), ("hand_coded", HAND_CODED)):
        for t, nums in table.items():
            numbers |= set(nums)
    for n in sorted(numbers, key=key):
        levels = []
        where = []
        for layer, table in (("compiled", COMPILED), ("meta", META), ("hand_coded", HAND_CODED)):
            for t, nums in table.items():
                if n in nums:
                    levels.append(layer)
                    where.append(f"T{t}")
        if n in MISNUMBERED:
            level = "misnumbered"
        elif "compiled" in levels:
            level = "compiled"
        elif "meta" in levels:
            level = "meta"
        elif "hand_coded" in levels:
            level = "hand_coded"
        else:
            level = "cited"
        skt = deva.get(n, "")
        curated = TEXT.get(n, "")
        entries[n] = {
            "text": curated,
            "text_devanagari": skt,
            "in_pinned_edition": n in deva,
            "iast_matches_pinned_edition": (_norm(curated) == _norm(deva_to_iast(skt))) if (curated and skt and n not in EDITION_DIFFERS and n not in TYPOGRAPHY) else None,
            **({"edition_note": EDITION_DIFFERS[n]} if n in EDITION_DIFFERS else {}),
            **({"typography_note": TYPOGRAPHY[n]} if n in TYPOGRAPHY else {}),
            "level": level,
            "theorems": sorted(set(where), key=lambda s: int(s[1:])),
            "cited_in": sorted(cited.get(n, set())),
            **({"canvas_meant": MISNUMBERED[n]} if n in MISNUMBERED else {}),
        }
    counts = {lvl: sum(1 for e in entries.values() if e["level"] == lvl) for lvl in ("compiled", "meta", "hand_coded", "cited", "misnumbered")}
    counts["entries"] = len(entries)
    counts["text_missing"] = sum(1 for e in entries.values() if not e["text"] and e["level"] != "misnumbered")
    counts["astadhyayi_total"] = len(deva) if deva else 3959
    counts["not_in_pinned_edition"] = sum(1 for e in entries.values() if not e["in_pinned_edition"])
    counts["iast_mismatch_with_pinned_edition"] = sum(1 for e in entries.values() if e["iast_matches_pinned_edition"] is False)
    return {"schema": "rkf.astadhyayi_ledger.v2", "pinned_edition": "research/panini_grammar/SUTRAPATHA.tsv (PG1; ashtadhyayi.com record ids)", "levels": ["compiled", "meta", "hand_coded", "cited", "misnumbered"], "counts": counts, "sutras": entries}


def render_md(ledger: dict) -> str:
    c = ledger["counts"]
    lines = [
        "# Aṣṭādhyāyī sūtra ledger",
        "",
        "Generated by `python -m proof_lab.astadhyayi_ledger`; the JSON next to this file is the record, this table is its view.",
        f"Entries {c['entries']} of {c['astadhyayi_total']} sūtras (PG1's pinned edition, `research/panini_grammar/SUTRAPATHA.tsv`): compiled {c['compiled']}, meta {c['meta']}, hand-coded {c['hand_coded']}, cited only {c['cited']}, canvas-misnumbered {c['misnumbered']}; curated IAST texts still to enter {c['text_missing']}; numbers absent from the pinned edition {c['not_in_pinned_edition']}; curated texts disagreeing with the pinned edition {c['iast_mismatch_with_pinned_edition']}.",
        "A level is the strongest evidence present: `compiled` (record read by the theorum/80 interpreter) > `meta` (saṁjñā/paribhāṣā implemented) > `hand_coded` (exact finite function in a certified packet) > `cited`.",
        "This ledger is the claim boundary for the grammar-as-language programme: every sūtra not listed is unrealized.",
        "",
        "| Sūtra | Pinned text | Text (IAST) | Level | Theorems | Note |",
        "|---|---|---|---|---|---|",
    ]
    for n, e in ledger["sutras"].items():
        note = e.get("canvas_meant", "")
        if not e["text"] and e["level"] != "misnumbered":
            note = "text to be entered"
        if e["level"] == "misnumbered":
            note = f"canvas number; meant {note}"
        if e.get("edition_note"):
            note = (note + "; " if note else "") + "edition numbering differs"
        if e["iast_matches_pinned_edition"] is False:
            note = (note + "; " if note else "") + "IAST differs from pinned text"
        if not e["in_pinned_edition"]:
            note = (note + "; " if note else "") + "not in pinned edition"
        lines.append(f"| {n} | {e['text_devanagari']} | {e['text']} | {e['level']} | {', '.join(e['theorems'])} | {note} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ledger = build()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "ASTADHYAYI_LEDGER.json").write_text(json.dumps(ledger, indent=2, ensure_ascii=False, sort_keys=False) + "\n", encoding="utf-8")
    (OUT_DIR / "ASTADHYAYI_LEDGER.md").write_text(render_md(ledger), encoding="utf-8")
    print(json.dumps(ledger["counts"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
