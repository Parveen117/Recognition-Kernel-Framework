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
EDITION_DIFFERS = {  # numbers whose text in the pinned PG1 edition is a different rule (other editions count a Kāśikā / vārttika rule here)
    "8.4.48": "cayo dvitīyāḥ śari pauṣkarasādeḥ is a vārttika in the pinned edition, where 8.4.48 = nādinyākrośe putrasya; cited with the Siddhānta-kaumudī number",
}
TYPOGRAPHY = {  # pinned text prints a consonant without virāma where the sūtra has a bare consonant; the curated IAST is kept
    "7.1.18": "pinned text prints औङ without virāma; the sūtra reads auṅ āpaḥ",
}
MISNUMBERED = {"1.1.6": "1.3.9 tasya lopaḥ", "1.1.15": "1.3.9 tasya lopaḥ"}

# the executed layers: which sūtras each certified packet realizes, and how
COMPILED = {  # theorum/80 record compiler
    "80": ["6.1.77", "6.1.78", "6.1.87", "6.1.88", "6.1.101", "7.3.77", "6.1.73", "6.1.71", "8.4.40", "7.3.84"],
}
META = {  # interpreter / saṁjñā / paribhāṣā sūtras implemented by a certificate
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
PACKET_OF = {"58": "paninian_seam_calculus", "63": "sup_vibhakti_resolver_ladder", "64": "ting_lat_parasmaipada", "65": "stem_classes_gayatri_coverage", "66": "lat_atmanepada", "67": "pada_to_line_external_sandhi", "68": "karaka_vibhakti_carrier", "80": "paninian_instruction_format", "81": "paninian_samjna_sound_layer", "82": "paninian_it_samjna_compiled", "85": "nirukta_nama_akhyatajani", "86": "nirukta_dhatupatha_nama", "87": "tripadi_nishtha_compiled", "88": "ap_stem_sup_compiled", "89": "ngi_stem_sup_compiled", "90": "r_stem_sup_compiled", "91": "ghi_stem_sup_compiled", "92": "hal_stem_sup_compiled", "93": "napumsaka_sup_compiled", "94": "sarvanama_sup_compiled"}
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
