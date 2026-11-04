from __future__ import annotations

"""Exact certificate (theorum/125): THE SUP RULE-TABLE ENGINE — one table in which
every sūtra of the nominal declension is a record (number, guard, action), one
driver that applies the table in the Aṣṭādhyāyī's own phase order (affix
substitution → aṅga operations → augments → junction sandhi → tripādī), and
fifteen certified paradigms as its ORACLES: rāma (theorum/63), bālā (88), nadī
(89), kartṛ (90), hari / guru (91), rājan / marut / ātman (92), phala / vāri (93),
sarva (94), sarvā (98), bhavat (109), daṇḍin (123) — 330 cells — plus six
declared classes (manas, mati, dhenu, madhu, pitṛ, mātṛ: 132 cells; theorum/126)
and the numerals dvi, tri, catur, pañcan, ṣaṣ, aṣṭan in their three genders
(84 cells; theorum/127) and the pronouns tad, etad, yad, tyad, kim, idam in
three genders (315 cells; theorum/128) reproduced exactly, and each table row shown
load-bearing on at least one cell of the suite (the per-row broken sets are recorded).

This is the "shared engine" that replaces per-theorem engines for every later
nominal packet: a new stem class is a few new rows plus an oracle, not a new
module.  The rules are quoted in SOURCES; the guards read only the state
(stem, affix, code, gender, declared class) — never a residue coefficient
(theorum/119 §6.5).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "4.1.2": "svaujasamauṭchaṣṭābhyāmbhisṅebhyāmbhyasṅasibhyāmbhyasṅasosāṅṅyossup", "1.1.42": "śi sarvanāmasthānam", "1.1.43": "suḍ anapuṁsakasya", "6.4.10": "sāntamahataḥ saṁyogasya", "6.1.113": "ato ror aplutād aplute", "6.1.114": "haśi ca", "8.3.24": "naś cāpadāntasya jhali", "8.3.36": "vā śari", "1.4.6": "ṅiti hrasvaś ca", "1.4.17": "svādiṣv asarvanāmasthāne", "1.4.18": "yaci bham", "1.4.7": "śeṣo ghy asakhi", "1.4.3": "yū stryākhyau nadī", "1.1.27": "sarvādīni sarvanāmāni",
    "1.1.52": "alo'ntyasya", "1.1.55": "anekālśitsarvasya", "4.1.4": "ajādyataṣṭāp", "6.1.97": "ato guṇe", "7.1.11": "nedamadasorakoḥ", "7.2.103": "kimaḥ kaḥ", "7.2.106": "tadoḥ saḥ sāvanantyayoḥ", "7.2.108": "idamo maḥ",
    "7.2.109": "daśca", "7.2.110": "yaḥ sau", "7.2.111": "ido'y puṁsi", "7.2.112": "anāpyakaḥ", "7.2.113": "hali lopaḥ",
    "7.1.25": "adḍ ḍatarādibhyaḥ pañcabhyaḥ",
    "1.1.24": "ṣṇāntā ṣaṭ", "1.1.47": "midaco'ntyātparaḥ", "1.1.63": "na lumatāṅgasya", "6.4.4": "na tisṛcatasṛ", "6.4.7": "nopadhāyāḥ", "7.1.21": "aṣṭābhya auś", "7.1.22": "ṣaḍbhyo luk", "7.1.53": "trestrayaḥ", "7.1.55": "ṣaṭcaturbhyaśca",
    "7.1.98": "caturanaḍuhorāmudāttaḥ", "7.2.84": "aṣṭana ā vibhaktau", "7.2.99": "tricaturoḥ striyāṁ tisṛcatasṛ", "7.2.100": "aci ra ṛtaḥ", "7.2.102": "tyadādīnāmaḥ", "8.4.41": "ṣṭunā ṣṭuḥ", "8.4.45": "yaro'nunāsike'nunāsiko vā",
    "7.1.9": "ato bhisa ais", "7.1.12": "ṭāṅasiṅasām inātsyāḥ", "7.1.13": "ṅer yaḥ", "7.1.14": "sarvanāmnaḥ smai", "7.1.15": "ṅasiṅyoḥ smātsminau", "7.1.17": "jasaḥ śī", "7.1.19": "napuṁsakāc ca", "7.1.20": "jaśśasoḥ śiḥ", "7.1.23": "svamor napuṁsakāt", "7.1.24": "ato 'm",
    "7.1.52": "āmi sarvanāmnaḥ suṭ", "7.1.54": "hrasvanadyāpo nuṭ", "8.4.39": "kṣubhnādiṣu ca", "7.1.78": "nābhyastāc chatuḥ", "7.1.79": "vā napuṁsakasya", "7.1.80": "ācchīnadyor num", "7.1.81": "śapśyanor nityam", "7.1.70": "ugidacāṁ sarvanāmasthāne 'dhātoḥ", "7.1.72": "napuṁsakasya jhalacaḥ", "7.1.94": "ṛd uśanaspurudaṁso 'nehasāṁ ca",
    "7.3.102": "supi ca", "7.3.103": "bahuvacane jhaly et", "7.3.104": "osi ca", "7.3.105": "āṅi cāpaḥ", "7.3.106": "sambuddhau ca", "7.3.107": "ambārthanadyor hrasvaḥ", "7.3.108": "hrasvasya guṇaḥ", "7.3.109": "jasi ca", "7.3.110": "ṛto ṅisarvanāmasthānayoḥ",
    "7.3.111": "gher ṅiti", "7.3.112": "āṇ nadyāḥ", "7.3.113": "yāḍ āpaḥ", "7.3.114": "sarvanāmnaḥ syāḍ ḍhrasvaś ca", "6.4.137": "na saṁyogād vamantāt", "7.3.116": "ṅer ām nadyāmnībhyaḥ", "7.3.118": "aut", "7.3.119": "ac ca gheḥ", "7.3.120": "āṅo nāstriyām",
    "6.4.3": "nāmi", "6.4.8": "sarvanāmasthāne cāsambuddhau", "6.4.11": "aptṛntṛcsvasṛnaptṛneṣṭṛtvaṣṭṛkṣattṛhotṛpotṛpraśāstṝṇām", "6.4.12": "inhanpūṣāryamṇāṁ śau", "6.4.13": "sau ca", "6.4.14": "atvasantasya cādhātoḥ", "6.4.134": "allopo 'naḥ", "6.4.136": "vibhāṣā ṅiśyoḥ",
    "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "6.1.69": "eṅhrasvāt sambuddheḥ", "6.1.77": "iko yaṇ aci", "6.1.78": "eco 'yavāyāvaḥ", "6.1.87": "ād guṇaḥ", "6.1.88": "vṛddhir eci", "6.1.101": "akaḥ savarṇe dīrghaḥ", "6.1.102": "prathamayoḥ pūrvasavarṇaḥ", "6.1.103": "tasmāc chaso naḥ puṁsi", "6.1.104": "nādici", "6.1.105": "dīrghāj jasi ca", "6.1.107": "ami pūrvaḥ", "6.1.110": "ṅasiṅasoś ca", "6.1.111": "ṛta ut", "1.1.51": "ur aṇ raparaḥ",
    "8.2.7": "nalopaḥ prātipadikāntasya", "8.2.8": "na ṅisambuddhyoḥ", "8.2.23": "saṁyogāntasya lopaḥ", "8.2.24": "rāt sasya", "8.2.39": "jhalāṁ jaśo 'nte", "8.4.55": "khari ca", "8.4.56": "vāvasāne", "8.3.59": "ādeśapratyayayoḥ", "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade", "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.4.37": "padāntasya", "8.4.40": "stoḥ ścunā ścuḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
    "1.1.62": "pratyayalope pratyayalakṣaṇam", "1.4.14": "suptiṅantaṁ padam", "1.1.47": "mid aco 'ntyāt paraḥ", "1.1.46": "ādyantau ṭakitau",
}
V = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
SHORT = {"a", "i", "u", "ṛ"}
LONG = {"a": "ā", "i": "ī", "u": "ū", "ṛ": "ṝ"}
GUNA = {"i": "e", "ī": "e", "u": "o", "ū": "o", "ṛ": "ar"}
YAN = {"i": "y", "ī": "y", "u": "v", "ū": "v", "ṛ": "r", "ṝ": "r"}
AYADI = {"e": ["a", "y"], "o": ["a", "v"], "ai": ["ā", "y"], "au": ["ā", "v"]}
JAS = {"t": "d", "k": "g", "p": "b", "ṭ": "ḍ", "c": "j", "ṣ": "ḍ"}
CAR = {"d": "t", "g": "k", "b": "p", "ḍ": "ṭ", "j": "c"}
AT_KU_PU = set(V) | {"h", "y", "v", "r", "k", "kh", "g", "gh", "ṅ", "p", "ph", "b", "bh", "m", "ṁ"}
MULTI = ("kh", "gh", "ch", "jh", "ṭh", "ḍh", "th", "dh", "ph", "bh", "ai", "au", "kṣ")
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"), ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
SNS = {"1s", "1d", "1p", "2s", "2d", "8s"}
DATARADI = {"anya", "anyatara", "itara", "katara", "katama", "yatara", "yatama", "tatara", "tatama"}   # 7.1.25 ḍatarādi (ḍatara / ḍatama with their realisations) and anya, anyatara, itara
JHAL = {"k", "kh", "g", "gh", "c", "ch", "j", "jh", "ṭ", "ṭh", "ḍ", "ḍh", "t", "th", "d", "dh", "p", "ph", "b", "bh", "ś", "ṣ", "s", "h"}


def tok(s: str) -> list[str]:
    out, i = [], 0
    while i < len(s):
        if s[i:i + 2] in MULTI:
            out.append(s[i:i + 2]); i += 2
        else:
            out.append(s[i]); i += 1
    return out


class S:
    """The state a sup rule acts on: stem, affix, code, upadeśa, gender, declared class flags, history."""
    def __init__(self, stem, code, up, gender, flags):
        self.st = tok(stem) if isinstance(stem, str) else list(stem)
        r = its(up, "pratyaya", vibhakti=True); self.aff = list(r["remaining_sounds"])
        if code == "7p":
            self.aff = ["s", "u"]
        self.code, self.up, self.g, self.flags = code, up, gender, set(flags)
        self.path: list[str] = [f"{''.join(self.st)} + {up} → {''.join(self.aff)} (its {r['its']})"]
        self.sns = code in SNS and gender != "n"   # 1.1.43 suḍ anapuṁsakasya: for the neuter only śi (1.1.42) is sarvanāmasthāna
        self.samb = code == "8s"
        self.done: set[str] = set()
        self.num = code[1]

    def final(self): return self.st[-1]
    def vinit(self): return bool(self.aff) and self.aff[0] in V
    def ngit(self): return self.up in ("ṅe", "ṅasi~", "ṅas", "ṅi")
    def a_final(self): return self.final() == "a"
    def ghi(self): return self.final() in ("i", "u") and "nadī" not in self.flags and self.g != "f_nadi"
    def nadi(self): return "nadī" in self.flags
    def ap(self): return "āp" in self.flags
    def sarva(self): return "sarvanāma" in self.flags
    def ugit(self): return "ugit" in self.flags
    def an(self): return self.st[-2:] == ["a", "n"]
    def in_(self): return self.st[-2:] == ["i", "n"]
    def r_(self): return "ṛ" in self.flags or "tṛ" in self.flags
    def s_stem(self): return self.final() == "s"
    def sat(self): return "ṣaṭ" in self.flags           # 1.1.24 ṣṇāntā ṣaṭ (the numerals in ṣ / n)
    def tisr(self): return "tisṛ" in self.flags
    def pada(self):
        # 1.4.17: before the consonant-initial sup (not sns) ; and when the sup has been deleted (1.1.62)
        return (not self.sns and bool(self.aff) and self.aff[0] not in V) or (not self.aff)
    def bha(self): return not self.sns and self.vinit()


Rule = tuple[str, Callable[[S], bool], Callable[[S], None], str]


def rules() -> list[Rule]:
    R: list[Rule] = []
    def add(n, guard, action, note): R.append((n, guard, action, note))
    # ---- phase 0: the numeral stems -------------------------------------------------------
    add("7.2.99", lambda s: s.g == "f" and "".join(s.st) in ("tri", "catur"), lambda s: (setattr(s, "st", tok({"tri": "tisṛ", "catur": "catasṛ"}["".join(s.st)])), s.flags.add("tisṛ")), "tri / catur → tisṛ / catasṛ in the feminine")
    add("7.2.84", lambda s: "".join(s.st) == "aṣṭan" and "7.2.84" not in s.done, lambda s: setattr(s, "st", tok("aṣṭā")), "aṣṭan → aṣṭā before a vibhakti (the ā-branch of the option)")
    add("7.1.21", lambda s: "".join(s.st) == "aṣṭā" and "ṣaṭ" in s.flags and s.up in ("jas", "śas"), lambda s: setattr(s, "aff", ["au"]), "jas / śas → auś after aṣṭā")
    add("7.1.22", lambda s: s.sat() and s.up in ("jas", "śas") and "7.1.21" not in s.done, lambda s: (setattr(s, "aff", []), setattr(s, "sns", False)), "jas / śas deleted (luk) after a ṣaṭ numeral; no sarvanāmasthāna operation on the aṅga (1.1.63 na lumatāṅgasya)")
    add("7.1.53", lambda s: "".join(s.st) == "tri" and s.up == "ām", lambda s: setattr(s, "st", tok("traya")), "tri → traya before ām")
    add("7.1.98", lambda s: "".join(s.st) == "catur" and (s.sns or (s.g == "n" and s.up in ("jas", "śas"))), lambda s: setattr(s, "st", tok("catvār")), "ām augment to catur before sarvanāmasthāna (after the last vowel, 1.1.47; u → v by 6.1.77)")
    add("7.1.55", lambda s: (s.sat() or "".join(s.st) in ("catur", "catasṛ")) and s.up == "ām", lambda s: setattr(s, "aff", ["n", "ā", "m"]), "nuṭ to ām after ṣaṭ and catur")
    # ---- phase 1: affix substitutions (7.1, 7.3) -------------------------------------------
    add("7.1.25", lambda s: s.g == "n" and "".join(s.st) in DATARADI and s.code in ("1s", "2s", "8s"), lambda s: (setattr(s, "aff", ["d"]), setattr(s, "samb", False)), "su / am → ad after the neuter anya, anyatara, itara, ḍatara, ḍatama (a + ad → anyad by 6.1.97; anyat by 8.4.56)")
    add("7.1.24", lambda s: s.g == "n" and s.a_final() and s.code in ("1s", "2s") and "7.1.25" not in s.done, lambda s: setattr(s, "aff", ["a", "m"]), "su / am → am after the neuter a-stem")
    add("7.1.23", lambda s: s.g == "n" and not s.a_final() and s.code in ("1s", "2s"), lambda s: setattr(s, "aff", []), "su / am deleted after the neuter (luk)")
    add("7.1.19", lambda s: s.g == "n" and s.code in ("1d", "2d"), lambda s: setattr(s, "aff", ["ī"]), "au → śī after the neuter")
    add("7.2.103", lambda s: "".join(s.st) == "kim" and bool(s.aff), lambda s: setattr(s, "st", tok("ka")), "kim → ka before a vibhakti (sarvādeśa, 1.1.55; not after the neuter luk: 1.1.63)")
    add("7.2.108", lambda s: "".join(s.st) == "idam" and s.up == "su~" and bool(s.aff) and not s.samb, lambda s: (s.st.__setitem__(-1, "m"), s.flags.add("7.2.108")), "m for the final of idam before su — m for m, stated to block 7.2.102's atva (so no ṭāp in the feminine: iyam)")
    add("7.2.111", lambda s: "7.2.108" in s.done and s.g == "m", lambda s: setattr(s, "st", ["a", "y"] + s.st[2:]), "id → ay before su in the masculine (ayam)")
    add("7.2.110", lambda s: "7.2.108" in s.done and s.g == "f", lambda s: setattr(s, "st", ["i", "y"] + s.st[2:]), "id → iy before su (the feminine: iyam)")
    add("7.2.102", lambda s: "tyadādi" in s.flags and bool(s.aff) and s.final() not in ("a", "ā") and "7.2.108" not in s.done, lambda s: s.st.__setitem__(-1, "a"), "the final of a tyadādi → a before a vibhakti (1.1.52; dvi → dva, tad → ta-a, idam → ida-a; not after a luk: 1.1.63)")
    add("6.1.97", lambda s: s.st[-2:] == ["a", "a"], lambda s: s.st.pop(), "a + a (the substitute a, a guṇa) → the single pararūpa in the aṅga (ta, ida)")
    add("4.1.4", lambda s: s.g == "f" and "tyadādi" in s.flags and s.a_final() and not s.ap() and (s.done & {"7.2.102", "7.2.103"}), lambda s: (s.st.__setitem__(-1, "ā"), s.flags.add("āp")), "ṭāp after the a-final (the atva-stem of tad / etad / yad / kim / idam: tā, kā, idā; 6.1.101 savarṇadīrgha)")
    add("7.2.106", lambda s: "tyadādi" in s.flags and s.up == "su~" and bool(s.aff) and not s.samb and "t" in s.st[:-1], lambda s: s.st.__setitem__(s.st.index("t"), "s"), "non-final t of tad / etad / tyad → s before su (saḥ, eṣaḥ, syaḥ; the d-case is adas, not claimed)")
    add("7.1.20", lambda s: s.g == "n" and s.code in ("1p", "2p"), lambda s: (setattr(s, "aff", ["i"]), s.flags.add("śi"), setattr(s, "sns", True)), "jas / śas → śi after the neuter (1.1.42: sarvanāmasthāna)")
    add("7.1.73", lambda s: s.g == "n" and s.final() in ("i", "u", "ṛ") and s.vinit() and "num" not in s.flags and s.up != "ām", lambda s: _num(s), "num to the ik-final neuter before a vowel-initial vibhakti")
    add("7.1.72", lambda s: s.g == "n" and "śi" in s.flags and (s.final() in V or s.final() in JHAL), lambda s: _num(s), "num to the neuter jhal / ac stem before śi")
    add("7.1.81", lambda s: "śatṛ" in s.flags and "aṅga-a" in s.flags and s.g == "n" and s.code in ("1d", "2d") and "num" not in s.flags, lambda s: _num(s), "num to the śatṛ stem after śap / śyan before the neuter dual śī — always (bhavantī, dīvyantī); after the other a / ā stems optionally by 7.1.80 ācchīnadyor num, the num branch realised (tudantī, krīṇantī)")
    add("7.1.17", lambda s: s.sarva() and s.a_final() and s.up == "jas" and s.g != "n", lambda s: setattr(s, "aff", ["ī"]), "jas → śī after an a-final sarvanāma (ataḥ continuing from 7.1.9)")
    add("7.1.14", lambda s: s.sarva() and s.a_final() and s.up == "ṅe", lambda s: setattr(s, "aff", ["s", "m", "ai"]), "ṅe → smai after a sarvanāma")
    add("7.1.15", lambda s: s.sarva() and s.a_final() and s.up in ("ṅasi~", "ṅi"), lambda s: setattr(s, "aff", ["s", "m", "ā", "t"] if s.up == "ṅasi~" else ["s", "m", "i", "n"]), "ṅasi / ṅi → smāt / smin")
    add("7.1.52", lambda s: s.sarva() and s.final() in ("a", "ā") and s.up == "ām", lambda s: setattr(s, "aff", ["s", "ā", "m"]), "suṭ to ām after a sarvanāma")
    add("7.1.9", lambda s: s.a_final() and s.up == "bhis" and "7.1.9" not in s.done and not (s.sarva() and s.st[:2] == ["i", "d"]), lambda s: setattr(s, "aff", ["ai", "s"]), "bhis → ais after a (not after idam / adas without ka: 7.1.11 nedamadasor akoḥ)")
    add("7.1.12", lambda s: s.a_final() and s.up in ("ṭā", "ṅasi~", "ṅas") and "7.1.15" not in s.done, lambda s: setattr(s, "aff", {"ṭā": ["i", "n", "a"], "ṅasi~": ["ā", "t"], "ṅas": ["s", "y", "a"]}[s.up]), "ṭā / ṅasi / ṅas → ina / āt / sya after a")
    add("7.1.13", lambda s: s.a_final() and s.up == "ṅe" and s.aff == ["e"], lambda s: setattr(s, "aff", ["y", "a"]), "ṅe → ya after a")
    add("7.1.18", lambda s: s.ap() and s.up == "auṭ", lambda s: setattr(s, "aff", ["ī"]), "au → śī after an āp")
    add("7.1.54", lambda s: s.up == "ām" and s.aff == ["ā", "m"] and (s.final() in SHORT or s.nadi() or s.ap()), lambda s: setattr(s, "aff", ["n", "ā", "m"]), "nuṭ to ām after a short vowel / nadī / āp")
    add("6.4.3", lambda s: s.aff[:3] == ["n", "ā", "m"] and s.final() in SHORT and not s.tisr(), lambda s: s.st.__setitem__(-1, LONG[s.final()]), "the aṅga's short final lengthened before nām (not tisṛ / catasṛ: 6.4.4)")
    add("7.3.120", lambda s: s.ghi() and s.g != "f" and s.up == "ṭā", lambda s: setattr(s, "aff", ["n", "ā"]), "ṭā → nā after a ghi (not feminine)")
    add("7.3.118", lambda s: s.ghi() and s.up == "ṅi", lambda s: setattr(s, "aff", ["au"]), "ṅi → au after i / u")
    add("7.3.119", lambda s: s.ghi() and s.up == "ṅi" and s.aff == ["au"], lambda s: s.st.__setitem__(-1, "a"), "… and the ghi's final → a")
    add("7.3.111", lambda s: s.ghi() and s.ngit() and s.up != "ṅi", lambda s: s.st.__setitem__(-1, GUNA[s.final()]), "guṇa of the ghi before a ṅit")
    add("7.3.112", lambda s: s.nadi() and s.ngit(), lambda s: _set_final(s, [YAN[s.final()], "ā"]), "āṭ before the ṅit after a nadī (ṭit → initial, 1.1.46; ī → y before it, 6.1.77)")
    add("7.3.114", lambda s: s.sarva() and s.ap() and s.ngit(), lambda s: (s.st.__setitem__(-1, "a"), setattr(s, "st", s.st + ["s", "y", "ā"])), "syāṭ before the ṅit after a feminine sarvanāma, with hrasva of the ā")
    add("7.2.112", lambda s: s.sarva() and s.st[:2] == ["i", "d"] and s.up in ("ṭā", "os"), lambda s: setattr(s, "st", ["a", "n"] + s.st[2:]), "id → an before the vowel-initial āp ending without ka (anena, anayoḥ, anayā)")
    add("7.2.113", lambda s: s.sarva() and s.st[:2] == ["i", "d"] and bool(s.aff) and (s.aff[0] not in V or "7.3.114" in s.done), lambda s: setattr(s, "st", s.st[2:]), "id of the sarvanāman idam dropped before a hal-initial vibhakti — the pronoun only, not any stem in id- (iddhaḥ, theorum/161) (asmai, asya, ābhyām, ebhiḥ, eṣām; with syāṭ: asyai)")
    add("7.2.109", lambda s: s.sarva() and s.st[:2] == ["i", "d"] and bool(s.aff) and s.aff[0] in V, lambda s: s.st.__setitem__(1, "m"), "d of idam → m before the remaining vowel-initial vibhakti (imau, ime, imam, imān, imāni, imāḥ)")
    add("7.3.113", lambda s: s.ap() and s.ngit() and "7.3.114" not in s.done, lambda s: setattr(s, "st", s.st + ["y", "ā"]), "yāṭ before the ṅit after an āp")
    add("7.3.116", lambda s: (s.nadi() or s.ap()) and s.up == "ṅi", lambda s: setattr(s, "aff", s.aff[:-1] + ["ā", "m"]), "ṅi → ām after nadī / āp")
    add("7.3.105", lambda s: s.ap() and s.up in ("ṭā", "os"), lambda s: s.st.__setitem__(-1, "e"), "ā → e before ṭā / os")
    add("7.3.106", lambda s: s.ap() and s.samb, lambda s: s.st.__setitem__(-1, "e"), "ā → e in the sambuddhi")
    add("7.3.107", lambda s: s.nadi() and s.samb, lambda s: s.st.__setitem__(-1, "i"), "nadī shortened in the sambuddhi")
    add("7.3.108", lambda s: s.samb and s.final() in ("i", "u") and "7.3.107" not in s.done, lambda s: s.st.__setitem__(-1, GUNA[s.final()]), "guṇa of the short final in the sambuddhi")
    add("7.3.109", lambda s: s.final() in ("i", "u") and s.up == "jas", lambda s: s.st.__setitem__(-1, GUNA[s.final()]), "guṇa before jas")
    add("7.3.110", lambda s: s.final() == "ṛ" and not s.tisr() and (s.up == "ṅi" or (s.sns and not s.samb and s.up != "su~")) and not s.flags & {"7.1.94"}, lambda s: _set_final(s, ["a", "r"]), "ṛ → ar before ṅi and sarvanāmasthāna (1.1.51)")
    add("7.3.110s", lambda s: s.final() == "ṛ" and s.samb, lambda s: _set_final(s, ["a", "r"]), "ṛ → ar in the sambuddhi (7.3.110 with 8.2.24 below)")
    add("7.1.94", lambda s: s.r_() and s.final() == "ṛ" and s.code == "1s", lambda s: (_set_final(s, ["a", "n"]), s.flags.add("7.1.94")), "anaṅ to the tṛ-stem before su")
    add("6.4.11", lambda s: "tṛ" in s.flags and s.sns and not s.samb and s.st[-2:] == ["a", "r"], lambda s: s.st.__setitem__(-2, "ā"), "upadhā dīrgha of the tṛc-stem before sarvanāmasthāna")
    add("7.3.102", lambda s: s.a_final() and s.aff and s.aff[0] in ("bh", "y") and s.up in ("bhyām", "ṅe"), lambda s: s.st.__setitem__(-1, "ā"), "a → ā before the yañ-initial sup (bhyām)")
    add("7.3.103", lambda s: s.a_final() and (s.up in ("bhyas", "sup") or (s.aff[:1] in (["s"], ["bh"]) and s.num == "p")), lambda s: s.st.__setitem__(-1, "e"), "a → e before bhyas / su")
    add("7.3.104", lambda s: s.a_final() and s.up == "os", lambda s: s.st.__setitem__(-1, "e"), "a → e before os")
    # ---- phase 2: augments and aṅga operations --------------------------------------------
    add("7.1.70", lambda s: s.ugit() and s.sns and "num" not in s.flags and not ("abhyasta" in s.flags and s.g != "n"), lambda s: _num(s), "num to the ugit stem before sarvanāmasthāna (one num: the neuter śi's of 7.1.72 is the same augment — bhūtavanti); not to the śatṛ after the abhyasta, 7.1.78 nābhyastāc chatuḥ (dadat, bibhrat; in the neuter optionally by 7.1.79, the num branch realised: dadanti)")
    add("6.4.14", lambda s: s.ugit() and s.code == "1s" and s.st[-2:] == ["n", "t"] and "śatṛ" not in s.flags, lambda s: s.st.__setitem__(-3, "ā"), "upadhā dīrgha of the at-stem before su")
    add("6.4.13", lambda s: s.in_() and s.code == "1s", lambda s: s.st.__setitem__(-2, "ī"), "in-stem lengthened before su")
    add("6.4.12", lambda s: s.in_() and "śi" in s.flags, lambda s: s.st.__setitem__(-2, "ī"), "in-stem lengthened before śi")
    add("6.4.7", lambda s: s.aff[:3] == ["n", "ā", "m"] and s.final() == "n" and s.st[-2] in SHORT, lambda s: s.st.__setitem__(-2, LONG[s.st[-2]]), "upadhā of the n-final aṅga lengthened before nām (6.4.7 nopadhāyāḥ with 6.4.3)")
    add("7.2.100", lambda s: s.tisr() and s.final() == "ṛ" and s.vinit(), lambda s: s.st.__setitem__(-1, "r"), "ṛ of tisṛ / catasṛ → r before a vowel")
    add("6.4.10", lambda s: s.s_stem() and "num" in s.flags and s.st[-2] == "n" and s.st[-3] == "a", lambda s: s.st.__setitem__(-3, "ā"), "upadhā dīrgha of the s-stem's cluster (num + s) before sarvanāmasthāna")
    add("6.4.8", lambda s: (s.an() or (s.g == "n" and "num" in s.flags and s.st[-1] == "n")) and s.sns and not s.samb and not s.in_(), lambda s: s.st.__setitem__(-2, LONG.get(s.st[-2], s.st[-2])), "upadhā dīrgha of the n-stem before sarvanāmasthāna")
    add("6.1.68", lambda s: s.code in ("1s", "8s") and s.aff == ["s"] and (s.final() not in V or s.final() in ("ī", "ā")) and not (s.samb and s.final() in ("ī", "ā")), lambda s: setattr(s, "aff", []), "su dropped after a consonant / ī / ā")
    add("6.1.69", lambda s: s.samb and s.aff == ["s"] and (s.final() in ("e", "o") or s.final() in SHORT or s.st[-2:] == ["a", "r"]), lambda s: setattr(s, "aff", []), "sambuddhi su dropped after eṅ / a short vowel")
    add("6.4.134", lambda s: s.an() and s.bha() and not (s.up == "ṅi" and "6.4.136" in s.flags) and not (len(s.st) >= 4 and s.st[-3] in ("v", "m") and s.st[-4] not in V), lambda s: s.st.__delitem__(-2), "a of an dropped in the bha (6.4.137: not after a cluster ending in v / m)")
    add("8.4.40", lambda s: s.st[-1] == "n" and len(s.st) >= 2 and s.st[-2] in ("j", "c", "ch", "jh"), lambda s: s.st.__setitem__(-1, "ñ"), "n → ñ after j")
    # ---- phase 3: junction sandhi ----------------------------------------------------------
    add("6.1.107", lambda s: s.final() in ("a", "ā", "i", "ī", "u", "ū") and s.aff[:2] == ["a", "m"] and s.code in ("2s", "1s"), lambda s: setattr(s, "aff", s.aff[1:]), "ak + am → the pūrva")
    add("6.1.103", lambda s: s.g == "m" and not s.tisr() and s.up == "śas" and s.final() in ("a", "i", "u", "ṛ") and s.aff == ["a", "s"], lambda s: (s.st.__setitem__(-1, LONG[s.final()]), setattr(s, "aff", ["n"])), "ak + śas → pūrvasavarṇa dīrgha (6.1.102) and s → n in the masculine")
    add("6.1.102", lambda s: not s.tisr() and s.up in ("jas", "auṭ", "śas") and s.final() in ("a", "i", "u", "ṛ", "ī", "ū") and s.aff and s.aff[0] in V and not (s.final() in ("a", "ā") and s.aff[0] not in ("a", "ā")) and s.g != "n" and not (s.final() in ("ī", "ū") and s.up != "śas"), lambda s: (s.st.__setitem__(-1, LONG.get(s.final(), s.final())), setattr(s, "aff", s.aff[1:])), "ak + a-initial 1st / 2nd ending → pūrvasavarṇa dīrgha (6.1.104 nādici: not after a before ic; 6.1.105 dīrghāj jasi ca: not after a long vowel before jas — both prohibitions live in this guard)")
    add("6.1.110", lambda s: s.final() in ("e", "o") and s.up in ("ṅasi~", "ṅas") and s.aff[:1] == ["a"], lambda s: setattr(s, "aff", s.aff[1:]), "eṅ + as → pūrvarūpa")
    add("6.1.111", lambda s: s.final() == "ṛ" and s.up in ("ṅasi~", "ṅas") and s.aff[:1] == ["a"], lambda s: (_set_final(s, ["u", "r"]), setattr(s, "aff", s.aff[1:])), "ṛ + as → ur")
    add("6.1.88", lambda s: s.final() in ("a", "ā") and s.aff[:1] in (["au"], ["ai"], ["e"], ["o"]), lambda s: (_set_final(s, [{"au": "au", "ai": "ai", "e": "ai", "o": "au"}[s.aff[0]]]), setattr(s, "aff", s.aff[1:])), "a + ec → vṛddhi")
    add("6.1.87", lambda s: s.final() in ("a", "ā") and s.aff[:1] in (["i"], ["u"], ["ī"], ["ū"]), lambda s: (_set_final(s, [GUNA[s.aff[0]]]), setattr(s, "aff", s.aff[1:])), "a + ik → guṇa")
    add("6.1.101", lambda s: s.final() in ("a", "ā") and s.aff[:1] in (["a"], ["ā"]), lambda s: (_set_final(s, ["ā"]), setattr(s, "aff", s.aff[1:])), "a + a → ā")
    add("6.1.78", lambda s: s.final() in AYADI and s.vinit(), lambda s: _set_final(s, AYADI[s.final()]), "ec → ay / av / āy / āv before a vowel")
    add("6.1.77", lambda s: s.final() in YAN and s.vinit() and not s.tisr() and not (s.final() in ("i", "u") and s.aff[0] == s.final()), lambda s: _set_final(s, [YAN[s.final()]]), "ik → yaṇ before a vowel (not the ṛ of tisṛ / catasṛ, whose r is 7.2.100's)")
    # ---- phase 4: the tripādī (8.2.1 order) -------------------------------------------------
    add("8.2.7", lambda s: s.pada() and s.final() == "n" and not (s.samb and s.flags & {"an", "in"} or s.samb and s.st[-2] in ("a", "i")), lambda s: s.st.pop(), "pada-final n dropped")
    add("8.2.23", lambda s: s.pada() and s.st[-2:] == ["n", "t"], lambda s: s.st.pop(), "pada-final cluster loses its last sound")
    add("8.2.24", lambda s: s.st[-1] == "r" and s.aff == ["s"], lambda s: setattr(s, "aff", []), "s dropped after r at the pada end (kartur-s → kartur)")
    add("8.2.66p", lambda s: s.pada() and s.s_stem() and s.aff, lambda s: s.st.__setitem__(-1, "r"), "pada-final s → ru before the consonant-initial sup (8.2.66)")
    add("6.1.114", lambda s: s.st[-2:] == ["a", "r"] and "8.2.66p" in s.done and s.aff and s.aff[0] in ("bh",), lambda s: setattr(s, "st", s.st[:-2] + ["o"]), "ru → u before haś, then a + u → o (6.1.114 haśi ca; 6.1.87)")
    add("8.3.24", lambda s: "num" in s.flags and s.st[-2:] == ["n", "s"] and s.aff[:1] == ["i"], lambda s: s.st.__setitem__(-2, "ṁ"), "n → anusvāra before the jhal, not pada-final (manāṁsi)")
    add("8.2.39", lambda s: s.pada() and s.final() in JAS and (s.aff or s.final() == "ṣ"), lambda s: s.st.__setitem__(-1, JAS[s.final()]), "pada-final jhal → jaś")
    add("8.4.41", lambda s: s.final() == "ḍ" and s.aff[:1] == ["n"], lambda s: s.aff.__setitem__(0, "ṇ"), "n → ṇ after the ṭu-class ḍ (ṣṭunā ṣṭuḥ)")
    add("8.4.45", lambda s: s.final() == "ḍ" and s.aff[:1] == ["ṇ"], lambda s: s.st.__setitem__(-1, "ṇ"), "ḍ → the nasal before a nasal (yaro 'nunāsike 'nunāsiko vā: the nasal branch realised)")
    add("8.4.55", lambda s: s.pada() and s.final() in CAR and s.aff and s.aff[0] in ("s", "k", "t", "p", "c", "ṭ", "ś", "ṣ"), lambda s: s.st.__setitem__(-1, CAR[s.final()]), "jaś → car before khar")
    add("8.4.56", lambda s: not s.aff and s.final() in CAR, lambda s: s.st.__setitem__(-1, CAR[s.final()]), "jaś → car at pause (vāvasāne: the car branch realised; ṣaṭ against ṣaḍ)")
    add("8.3.59", lambda s: s.aff[:1] == ["s"] and s.final() in ("i", "ī", "u", "ū", "ṛ", "ṝ", "e", "o", "ai", "au", "r") and (s.code == "7p" or s.aff[:3] == ["s", "ā", "m"]) and "8.2.66p" not in s.done, lambda s: s.aff.__setitem__(0, "ṣ"), "s of sup → ṣ after iṇ")
    add("8.3.59s", lambda s: "7.2.106" in s.done and "s" in s.st[:-1] and s.st[s.st.index("s") - 1] in ("e", "i", "y"), lambda s: s.st.__setitem__(s.st.index("s"), "ṣ"), "the ādeśa s after iṇ → ṣ, stem-internal (8.3.59: eṣaḥ, eṣā)")
    add("8.4.2", lambda s: True, lambda s: _natva(s), "n → ṇ after r / ṣ / ṛ across aṭ / ku / pu (not pada-final: 8.4.37)")
    add("8.3.15p", lambda s: s.st[-1] == "r" and "8.2.66p" in s.done and s.aff[:1] == ["s"], lambda s: s.st.__setitem__(-1, "ḥ"), "r → ḥ before the khar s (8.3.15; 8.3.36 vā śari: manassu optional, not realised)")
    add("8.2.66", lambda s: (s.st + s.aff)[-1] == "s", lambda s: _set_last(s, "r"), "s → ru")
    add("8.3.15", lambda s: (s.st + s.aff)[-1] == "r", lambda s: _set_last(s, "ḥ"), "r → ḥ at pause")
    return R


def _set_final(s: S, new: list[str]) -> None:
    s.st = s.st[:-1] + list(new)


def _set_last(s: S, c: str) -> None:
    if s.aff: s.aff[-1] = c
    else: s.st[-1] = c


def _num(s: S) -> None:
    k = max(i for i, x in enumerate(s.st) if x in V)
    s.st = s.st[:k + 1] + ["n"] + s.st[k + 1:]; s.flags.add("num")


def _natva(s: S) -> None:
    w = s.st + s.aff
    for i, x in enumerate(w):
        if x != "n" or i == len(w) - 1 or w[i + 1] in JHAL:   # the n before a jhal is not reached (granthaka, chṛndat, corayantī: the nasal there is 8.4.58's)
            continue
        if "kṣubhnādi" in s.flags and i < len(s.st):   # 8.4.39 kṣubhnādiṣu ca: the n of the kṣubhnādi stem keeps n (kṣubhnan, tṛpnuvan)
            continue
        j = i - 1
        while j >= 0 and w[j] in AT_KU_PU and w[j] not in ("r", "ṛ", "ṝ"):
            j -= 1
        if j >= 0 and (w[j] in ("r", "ṣ", "ṛ", "ṝ") or w[j].endswith("ṣ")):   # the kṣ token ends in ṣ (vṛkṣeṇa)
            w[i] = "ṇ"
    n = len(s.st); s.st, s.aff = w[:n], w[n:]


RULES = rules()
IDS = [r[0] for r in RULES]


HOOK = None   # theorum/150: an observer of every firing — HOOK(row_id, state_before, state_after); None in ordinary runs


def snapshot(s: S) -> dict:
    return {"st": list(s.st), "aff": list(s.aff), "flags": set(s.flags), "sns": s.sns, "samb": s.samb}


def decline(stem, code, up, gender="m", flags=(), off=()) -> tuple[str, list[str]]:
    s = S(stem, code, up, gender, flags)
    for n, guard, action, note in RULES:
        if n in off:
            continue
        before = ("".join(s.st), "".join(s.aff), frozenset(s.flags), s.sns)
        snap = snapshot(s) if HOOK else None
        if guard(s):
            action(s)
            after = ("".join(s.st), "".join(s.aff), frozenset(s.flags), s.sns)
            if after != before:
                s.done.add(n); s.path.append(f"{n} {note}: {after[0]}-{after[1]}")
                if HOOK:
                    HOOK(n, snap, snapshot(s))
    return "".join(s.st + s.aff), s.path


def paradigm(stem, gender="m", flags=(), off=(), cells=None) -> dict[str, str]:
    return {c: decline(stem, c, up, gender, flags, off)[0] for c, up in SUP if cells is None or c in cells}


def suite_paradigm(name, off=()):
    e = SUITE[name]
    return paradigm(e[0], e[1], e[2], off, e[4] if len(e) > 4 else None)


SUITE = {  # name: (stem, gender, flags, oracle source)
    "rāma": ("rāma", "m", (), "theorum/63"), "bālā": ("bālā", "f", ("āp",), "theorum/88"), "nadī": ("nadī", "f", ("nadī",), "theorum/89"),
    "kartṛ": ("kartṛ", "m", ("tṛ", "ṛ"), "theorum/90"), "hari": ("hari", "m", (), "theorum/91"), "guru": ("guru", "m", (), "theorum/91"),
    "rājan": ("rājan", "m", ("an",), "theorum/92"), "marut": ("marut", "m", (), "theorum/92"), "phala": ("phala", "n", (), "theorum/93"), "vāri": ("vāri", "n", (), "theorum/93"),
    "sarva": ("sarva", "m", ("sarvanāma",), "theorum/94"), "sarvā": ("sarvā", "f", ("sarvanāma", "āp"), "theorum/98"), "ātman": ("ātman", "m", ("an",), "theorum/92"), "bhavat": ("bhavat", "m", ("ugit",), "theorum/109"), "daṇḍin": ("daṇḍin", "m", ("in",), "theorum/123"),
}
DECLARED = {  # classical paradigms declared as oracles for the classes no earlier packet certified (sources: the quoted rules; forms as in the Siddhāntakaumudī)
    "manas": {"1s": "manaḥ", "1d": "manasī", "1p": "manāṁsi", "2s": "manaḥ", "2d": "manasī", "2p": "manāṁsi", "3s": "manasā", "3d": "manobhyām", "3p": "manobhiḥ", "4s": "manase", "4d": "manobhyām", "4p": "manobhyaḥ",
              "5s": "manasaḥ", "5d": "manobhyām", "5p": "manobhyaḥ", "6s": "manasaḥ", "6d": "manasoḥ", "6p": "manasām", "7s": "manasi", "7d": "manasoḥ", "7p": "manaḥsu", "8s": "manaḥ"},
    "mati": {"1s": "matiḥ", "1d": "matī", "1p": "matayaḥ", "2s": "matim", "2d": "matī", "2p": "matīḥ", "3s": "matyā", "3d": "matibhyām", "3p": "matibhiḥ", "4s": "mataye", "4d": "matibhyām", "4p": "matibhyaḥ",
             "5s": "mateḥ", "5d": "matibhyām", "5p": "matibhyaḥ", "6s": "mateḥ", "6d": "matyoḥ", "6p": "matīnām", "7s": "matau", "7d": "matyoḥ", "7p": "matiṣu", "8s": "mate"},
    "dhenu": {"1s": "dhenuḥ", "1d": "dhenū", "1p": "dhenavaḥ", "2s": "dhenum", "2d": "dhenū", "2p": "dhenūḥ", "3s": "dhenvā", "3d": "dhenubhyām", "3p": "dhenubhiḥ", "4s": "dhenave", "4d": "dhenubhyām", "4p": "dhenubhyaḥ",
              "5s": "dhenoḥ", "5d": "dhenubhyām", "5p": "dhenubhyaḥ", "6s": "dhenoḥ", "6d": "dhenvoḥ", "6p": "dhenūnām", "7s": "dhenau", "7d": "dhenvoḥ", "7p": "dhenuṣu", "8s": "dheno"},
    "madhu": {"1s": "madhu", "1d": "madhunī", "1p": "madhūni", "2s": "madhu", "2d": "madhunī", "2p": "madhūni", "3s": "madhunā", "3d": "madhubhyām", "3p": "madhubhiḥ", "4s": "madhune", "4d": "madhubhyām", "4p": "madhubhyaḥ",
              "5s": "madhunaḥ", "5d": "madhubhyām", "5p": "madhubhyaḥ", "6s": "madhunaḥ", "6d": "madhunoḥ", "6p": "madhūnām", "7s": "madhuni", "7d": "madhunoḥ", "7p": "madhuṣu", "8s": "madho"},
    "pitṛ": {"1s": "pitā", "1d": "pitarau", "1p": "pitaraḥ", "2s": "pitaram", "2d": "pitarau", "2p": "pitṝn", "3s": "pitrā", "3d": "pitṛbhyām", "3p": "pitṛbhiḥ", "4s": "pitre", "4d": "pitṛbhyām", "4p": "pitṛbhyaḥ",
             "5s": "pituḥ", "5d": "pitṛbhyām", "5p": "pitṛbhyaḥ", "6s": "pituḥ", "6d": "pitroḥ", "6p": "pitṝṇām", "7s": "pitari", "7d": "pitroḥ", "7p": "pitṛṣu", "8s": "pitaḥ"},
    "mātṛ": {"1s": "mātā", "1d": "mātarau", "1p": "mātaraḥ", "2s": "mātaram", "2d": "mātarau", "2p": "mātṝḥ", "3s": "mātrā", "3d": "mātṛbhyām", "3p": "mātṛbhiḥ", "4s": "mātre", "4d": "mātṛbhyām", "4p": "mātṛbhyaḥ",
             "5s": "mātuḥ", "5d": "mātṛbhyām", "5p": "mātṛbhyaḥ", "6s": "mātuḥ", "6d": "mātroḥ", "6p": "mātṝṇām", "7s": "mātari", "7d": "mātroḥ", "7p": "mātṛṣu", "8s": "mātaḥ"},
}
SUITE.update({"manas": ("manas", "n", (), "declared"), "mati": ("mati", "f", (), "declared"), "dhenu": ("dhenu", "f", (), "declared"), "madhu": ("madhu", "n", (), "declared"),
              "pitṛ": ("pitṛ", "m", ("ṛ",), "declared"), "mātṛ": ("mātṛ", "f", ("ṛ",), "declared")})
DECLARED.update({
    "dvi": {"1d": "dvau", "2d": "dvau", "3d": "dvābhyām", "4d": "dvābhyām", "5d": "dvābhyām", "6d": "dvayoḥ", "7d": "dvayoḥ"},
    "dvā": {"1d": "dve", "2d": "dve", "3d": "dvābhyām", "4d": "dvābhyām", "5d": "dvābhyām", "6d": "dvayoḥ", "7d": "dvayoḥ"},
    "dvi_n": {"1d": "dve", "2d": "dve", "3d": "dvābhyām", "4d": "dvābhyām", "5d": "dvābhyām", "6d": "dvayoḥ", "7d": "dvayoḥ"},
    "tri": {"1p": "trayaḥ", "2p": "trīn", "3p": "tribhiḥ", "4p": "tribhyaḥ", "5p": "tribhyaḥ", "6p": "trayāṇām", "7p": "triṣu"},
    "tri_f": {"1p": "tisraḥ", "2p": "tisraḥ", "3p": "tisṛbhiḥ", "4p": "tisṛbhyaḥ", "5p": "tisṛbhyaḥ", "6p": "tisṛṇām", "7p": "tisṛṣu"},
    "tri_n": {"1p": "trīṇi", "2p": "trīṇi", "3p": "tribhiḥ", "4p": "tribhyaḥ", "5p": "tribhyaḥ", "6p": "trayāṇām", "7p": "triṣu"},
    "catur": {"1p": "catvāraḥ", "2p": "caturaḥ", "3p": "caturbhiḥ", "4p": "caturbhyaḥ", "5p": "caturbhyaḥ", "6p": "caturṇām", "7p": "caturṣu"},
    "catur_f": {"1p": "catasraḥ", "2p": "catasraḥ", "3p": "catasṛbhiḥ", "4p": "catasṛbhyaḥ", "5p": "catasṛbhyaḥ", "6p": "catasṛṇām", "7p": "catasṛṣu"},
    "catur_n": {"1p": "catvāri", "2p": "catvāri", "3p": "caturbhiḥ", "4p": "caturbhyaḥ", "5p": "caturbhyaḥ", "6p": "caturṇām", "7p": "caturṣu"},
    "pañcan": {"1p": "pañca", "2p": "pañca", "3p": "pañcabhiḥ", "4p": "pañcabhyaḥ", "5p": "pañcabhyaḥ", "6p": "pañcānām", "7p": "pañcasu"},
    "ṣaṣ": {"1p": "ṣaṭ", "2p": "ṣaṭ", "3p": "ṣaḍbhiḥ", "4p": "ṣaḍbhyaḥ", "5p": "ṣaḍbhyaḥ", "6p": "ṣaṇṇām", "7p": "ṣaṭsu"},
    "aṣṭan": {"1p": "aṣṭau", "2p": "aṣṭau", "3p": "aṣṭābhiḥ", "4p": "aṣṭābhyaḥ", "5p": "aṣṭābhyaḥ", "6p": "aṣṭānām", "7p": "aṣṭāsu"},
})
DUAL = ["1d", "2d", "3d", "4d", "5d", "6d", "7d"]; PLUR = ["1p", "2p", "3p", "4p", "5p", "6p", "7p"]
SUITE.update({"dvi": ("dvi", "m", ("sarvanāma", "tyadādi"), "declared", DUAL), "dvā": ("dvā", "f", ("sarvanāma", "tyadādi", "āp"), "declared", DUAL), "dvi_n": ("dvi", "n", ("sarvanāma", "tyadādi"), "declared", DUAL),
              "tri": ("tri", "m", (), "declared", PLUR), "tri_f": ("tri", "f", (), "declared", PLUR), "tri_n": ("tri", "n", (), "declared", PLUR),
              "catur": ("catur", "m", (), "declared", PLUR), "catur_f": ("catur", "f", (), "declared", PLUR), "catur_n": ("catur", "n", (), "declared", PLUR),
              "pañcan": ("pañcan", "m", ("ṣaṭ",), "declared", PLUR), "ṣaṣ": ("ṣaṣ", "m", ("ṣaṭ",), "declared", PLUR), "aṣṭan": ("aṣṭan", "m", ("ṣaṭ",), "declared", PLUR)})

PRON = ["1s", "1d", "1p", "2s", "2d", "2p", "3s", "3d", "3p", "4s", "4d", "4p", "5s", "5d", "5p", "6s", "6d", "6p", "7s", "7d", "7p"]
def _tab(words: str) -> dict[str, str]:
    w = words.split(); assert len(w) == 21, len(w); return dict(zip(PRON, w))
DECLARED.update({
    "tad": _tab("saḥ tau te tam tau tān tena tābhyām taiḥ tasmai tābhyām tebhyaḥ tasmāt tābhyām tebhyaḥ tasya tayoḥ teṣām tasmin tayoḥ teṣu"),
    "tā": _tab("sā te tāḥ tām te tāḥ tayā tābhyām tābhiḥ tasyai tābhyām tābhyaḥ tasyāḥ tābhyām tābhyaḥ tasyāḥ tayoḥ tāsām tasyām tayoḥ tāsu"),
    "tad_n": _tab("tat te tāni tat te tāni tena tābhyām taiḥ tasmai tābhyām tebhyaḥ tasmāt tābhyām tebhyaḥ tasya tayoḥ teṣām tasmin tayoḥ teṣu"),
    "etad": _tab("eṣaḥ etau ete etam etau etān etena etābhyām etaiḥ etasmai etābhyām etebhyaḥ etasmāt etābhyām etebhyaḥ etasya etayoḥ eteṣām etasmin etayoḥ eteṣu"),
    "etā": _tab("eṣā ete etāḥ etām ete etāḥ etayā etābhyām etābhiḥ etasyai etābhyām etābhyaḥ etasyāḥ etābhyām etābhyaḥ etasyāḥ etayoḥ etāsām etasyām etayoḥ etāsu"),
    "etad_n": _tab("etat ete etāni etat ete etāni etena etābhyām etaiḥ etasmai etābhyām etebhyaḥ etasmāt etābhyām etebhyaḥ etasya etayoḥ eteṣām etasmin etayoḥ eteṣu"),
    "yad": _tab("yaḥ yau ye yam yau yān yena yābhyām yaiḥ yasmai yābhyām yebhyaḥ yasmāt yābhyām yebhyaḥ yasya yayoḥ yeṣām yasmin yayoḥ yeṣu"),
    "yad_n": _tab("yat ye yāni yat ye yāni yena yābhyām yaiḥ yasmai yābhyām yebhyaḥ yasmāt yābhyām yebhyaḥ yasya yayoḥ yeṣām yasmin yayoḥ yeṣu"),
    "tyad": _tab("syaḥ tyau tye tyam tyau tyān tyena tyābhyām tyaiḥ tyasmai tyābhyām tyebhyaḥ tyasmāt tyābhyām tyebhyaḥ tyasya tyayoḥ tyeṣām tyasmin tyayoḥ tyeṣu"),
    "kim": _tab("kaḥ kau ke kam kau kān kena kābhyām kaiḥ kasmai kābhyām kebhyaḥ kasmāt kābhyām kebhyaḥ kasya kayoḥ keṣām kasmin kayoḥ keṣu"),
    "kā": _tab("kā ke kāḥ kām ke kāḥ kayā kābhyām kābhiḥ kasyai kābhyām kābhyaḥ kasyāḥ kābhyām kābhyaḥ kasyāḥ kayoḥ kāsām kasyām kayoḥ kāsu"),
    "kim_n": _tab("kim ke kāni kim ke kāni kena kābhyām kaiḥ kasmai kābhyām kebhyaḥ kasmāt kābhyām kebhyaḥ kasya kayoḥ keṣām kasmin kayoḥ keṣu"),
    "idam": _tab("ayam imau ime imam imau imān anena ābhyām ebhiḥ asmai ābhyām ebhyaḥ asmāt ābhyām ebhyaḥ asya anayoḥ eṣām asmin anayoḥ eṣu"),
    "idā": _tab("iyam ime imāḥ imām ime imāḥ anayā ābhyām ābhiḥ asyai ābhyām ābhyaḥ asyāḥ ābhyām ābhyaḥ asyāḥ anayoḥ āsām asyām anayoḥ āsu"),
    "idam_n": _tab("idam ime imāni idam ime imāni anena ābhyām ebhiḥ asmai ābhyām ebhyaḥ asmāt ābhyām ebhyaḥ asya anayoḥ eṣām asmin anayoḥ eṣu"),
})
_T = ("sarvanāma", "tyadādi")
SUITE.update({"tad": ("tad", "m", _T, "declared", PRON), "tā": ("tad", "f", _T, "declared", PRON), "tad_n": ("tad", "n", _T, "declared", PRON),
              "etad": ("etad", "m", _T, "declared", PRON), "etā": ("etad", "f", _T, "declared", PRON), "etad_n": ("etad", "n", _T, "declared", PRON),
              "yad": ("yad", "m", _T, "declared", PRON), "yad_n": ("yad", "n", _T, "declared", PRON), "tyad": ("tyad", "m", _T, "declared", PRON),
              "kim": ("kim", "m", _T, "declared", PRON), "kā": ("kim", "f", _T, "declared", PRON), "kim_n": ("kim", "n", _T, "declared", PRON),
              "idam": ("idam", "m", _T, "declared", PRON), "idā": ("idam", "f", _T, "declared", PRON), "idam_n": ("idam", "n", _T, "declared", PRON)})
DECLARED.update({   # theorum/153: the śatṛ stem and the neuter ugit, as the generator derives them (research/independent_oracle/VIDYUT_KRDANTA_SUP_LANE.json; the first alternative)
    "bhavat_śatṛ": {"1s": "bhavan", "1d": "bhavantau", "1p": "bhavantaḥ", "2s": "bhavantam", "2d": "bhavantau", "2p": "bhavataḥ", "3s": "bhavatā", "3d": "bhavadbhyām", "3p": "bhavadbhiḥ", "4s": "bhavate", "4d": "bhavadbhyām", "4p": "bhavadbhyaḥ", "5s": "bhavataḥ", "5d": "bhavadbhyām", "5p": "bhavadbhyaḥ", "6s": "bhavataḥ", "6d": "bhavatoḥ", "6p": "bhavatām", "7s": "bhavati", "7d": "bhavatoḥ", "7p": "bhavatsu", "8s": "bhavan"},
    "bhavat_śatṛ_n": {"1s": "bhavat", "1d": "bhavantī", "1p": "bhavanti", "2s": "bhavat", "3s": "bhavatā", "4s": "bhavate", "6p": "bhavatām", "7s": "bhavati", "8s": "bhavat"},
    "tudat_śatṛ_n": {"1s": "tudat", "1d": "tudantī", "1p": "tudanti", "2s": "tudat", "3s": "tudatā", "4s": "tudate", "6p": "tudatām", "7s": "tudati", "8s": "tudat"},
    "bhūtavat_n": {"1s": "bhūtavat", "1d": "bhūtavatī", "1p": "bhūtavanti", "2s": "bhūtavat", "3s": "bhūtavatā", "4s": "bhūtavate", "6p": "bhūtavatām", "7s": "bhūtavati", "8s": "bhūtavat"}})
DECLARED["dadat_śatṛ"] = {"1s": "dadat", "1d": "dadatau", "1p": "dadataḥ", "2s": "dadatam", "2d": "dadatau", "2p": "dadataḥ", "3s": "dadatā", "3d": "dadadbhyām", "3p": "dadadbhiḥ", "4s": "dadate", "4d": "dadadbhyām", "4p": "dadadbhyaḥ", "5s": "dadataḥ", "5d": "dadadbhyām", "5p": "dadadbhyaḥ", "6s": "dadataḥ", "6d": "dadatoḥ", "6p": "dadatām", "7s": "dadati", "7d": "dadatoḥ", "7p": "dadatsu", "8s": "dadat"}
DECLARED["kṣubhnat_śatṛ"] = {"1s": "kṣubhnan", "1d": "kṣubhnantau", "1p": "kṣubhnantaḥ", "2s": "kṣubhnantam", "2d": "kṣubhnantau", "2p": "kṣubhnataḥ", "3s": "kṣubhnatā", "3d": "kṣubhnadbhyām", "3p": "kṣubhnadbhiḥ", "4s": "kṣubhnate", "4d": "kṣubhnadbhyām", "4p": "kṣubhnadbhyaḥ", "5s": "kṣubhnataḥ", "5d": "kṣubhnadbhyām", "5p": "kṣubhnadbhyaḥ", "6s": "kṣubhnataḥ", "6d": "kṣubhnatoḥ", "6p": "kṣubhnatām", "7s": "kṣubhnati", "7d": "kṣubhnatoḥ", "7p": "kṣubhnatsu", "8s": "kṣubhnan"}
N9 = ["1s", "1d", "1p", "2s", "3s", "4s", "6p", "7s", "8s"]
SUITE.update({"bhavat_śatṛ": ("bhavat", "m", ("ugit", "śatṛ"), "declared"), "bhavat_śatṛ_n": ("bhavat", "n", ("ugit", "śatṛ", "aṅga-a"), "declared", N9), "tudat_śatṛ_n": ("tudat", "n", ("ugit", "śatṛ", "aṅga-a"), "declared", N9), "bhūtavat_n": ("bhūtavat", "n", ("ugit",), "declared", N9), "dadat_śatṛ": ("dadat", "m", ("ugit", "śatṛ", "abhyasta"), "declared"), "kṣubhnat_śatṛ": ("kṣubhnat", "m", ("ugit", "śatṛ", "kṣubhnādi"), "declared")})
OPTIONAL_CELLS = {("rājan", "7s"), ("vāri", "8s")}   # the earlier packets print "a / b" there (6.4.136; 7.3.108's option): compared on the first alternative


def oracles() -> dict[str, dict[str, str]]:
    from proof_lab.ap_stem_sup_compiled import paradigm as ap
    from proof_lab.ghi_stem_sup_compiled import paradigm as ghi
    from proof_lab.hal_stem_sup_compiled import paradigm as hal
    from proof_lab.in_stem_sup_compiled import paradigm as ins
    from proof_lab.napumsaka_sup_compiled import paradigm as nap
    from proof_lab.ngi_stem_sup_compiled import paradigm as ngi
    from proof_lab.r_stem_sup_compiled import paradigm as rst
    from proof_lab.sarvanama_sup_compiled import paradigm as sv
    from proof_lab.sarvanama_ap_sup_compiled import paradigm as sva
    from proof_lab.sup_vibhakti_resolver_ladder import ORACLE as R63
    from proof_lab.ugit_at_stem_sup_compiled import paradigm as ug
    c58 = {"A": "ā", "N": "ṇ", "z": "ṣ", "H": "ḥ", "I": "ī", "U": "ū", "R": "ṛ"}
    rama = {c: "".join(c58.get(ch, ch) for ch in w) for c, w in R63.items()}
    o = {"rāma": rama, "bālā": ap(tuple(tok("bālā"))), "nadī": ngi(tuple(tok("nadī"))), "kartṛ": rst(tuple(tok("kartṛ"))), "hari": ghi(tuple(tok("hari"))), "guru": ghi(tuple(tok("guru"))),
         "rājan": hal(tuple(tok("rājan"))), "marut": hal(tuple(tok("marut"))), "phala": nap(tuple(tok("phala"))), "vāri": nap(tuple(tok("vāri"))), "sarva": sv(tuple(tok("sarva"))),
         "bhavat": ug("bhavat"), "daṇḍin": ins("daṇḍin"), "sarvā": sva(tuple(tok("sarvā"))), "ātman": hal(tuple(tok("ātman")))}
    for name, c in OPTIONAL_CELLS:
        o[name][c] = o[name][c].split(" / ")[0]
    o.update(DECLARED)
    return o


SUP_LANE_FILE = Path(__file__).resolve().parent.parent / "research" / "independent_oracle" / "VIDYUT_SUP_LANE.json"


def sup_lane_oracle() -> dict[str, Any]:
    """New stems of every declared class, every cell vidyut-prakriya derives (theorum/141): a DECLARED oracle of implementation grade."""
    if not SUP_LANE_FILE.exists():
        return {}
    return json.loads(SUP_LANE_FILE.read_text(encoding="utf-8"))["cells"]


def t2_sup_lane() -> dict[str, Any]:
    O = sup_lane_oracle(); rows = {}
    for key, x in O.items():
        stem, g, c = key.split("|"); flags = tuple(x["flags"])
        try:
            ours = decline(stem, c, dict(SUP)[c], g, flags)[0]
        except Exception as e:  # noqa: BLE001
            ours = f"ENGINE_ERROR {e}"
        rows[key] = {"ours": ours, "vidyut": x["forms"], "agree": ours in x["forms"]}
    return {"cells": len(rows), "agree": sum(1 for r in rows.values() if r["agree"]), "disagree": {k: r for k, r in rows.items() if not r["agree"]}, "agreeing_keys": [k for k, r in rows.items() if r["agree"]]}


def t1_suite() -> dict[str, Any]:
    O = oracles()
    forms = {n: suite_paradigm(n) for n in SUITE}
    mism = {n: {c: (forms[n][c], O[n][c]) for c in forms[n] if forms[n][c] != O[n][c]} for n in SUITE}
    cells = sum(len(forms[n]) for n in SUITE)
    broken = {}
    for rid in IDS:
        b = []
        for n in SUITE:
            p = suite_paradigm(n, off=(rid,))
            b += [f"{n}.{c}" for c in p if p[c] != O[n][c]]
        broken[rid] = b
    lane = t2_sup_lane(); O2 = sup_lane_oracle()
    for rid in IDS:
        if not broken[rid]:   # a row no suite cell loads may be loaded by an agreeing lane cell (theorum/141)
            for k in lane["agreeing_keys"]:
                stem, g, c = k.split("|")
                if decline(stem, c, dict(SUP)[c], g, tuple(O2[k]["flags"]), off=(rid,))[0] not in O2[k]["forms"]:
                    broken[rid].append("lane:" + k); break
    vacuous = [r for r in IDS if not broken[r]]
    checks = {"all_861_cells_equal_the_oracles": all(not mism[n] for n in SUITE),
              "every_rule_row_is_load_bearing_on_the_suite": not vacuous}
    return {"checks": checks, "cells": cells, "mismatches": {n: m for n, m in mism.items() if m}, "broken_counts": {r: len(b) for r, b in broken.items()}, "broken": broken, "vacuous_rows": vacuous, "sup_lane": {"cells": lane["cells"], "agree": lane["agree"], "disagree": lane["disagree"]},
            "paths": {"rāma.3s": decline("rāma", "3s", "ṭā")[1], "nadī.4s": decline("nadī", "4s", "ṅe", "f", ("nadī",))[1], "kartṛ.1s": decline("kartṛ", "1s", "su~", "m", ("tṛ",))[1], "vāri.1p": decline("vāri", "1p", "jas", "n")[1]}}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_suite": t1_suite()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE" if all(checks.values()) else "FAIL_SUP_RULE_TABLE_ENGINE_CANDIDATE"
    return {
        "schema": "rkf.sup_rule_table_engine_candidate.v1", "status": status, "sources": SOURCES, "rule_order": IDS,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                f"one rule table of {len(IDS)} rows (each a quoted sūtra as guard + action) and one driver reproduce the 330 cells of fifteen certified paradigms exactly from the earlier pinned packets (theorum/63, 88, 89, 90, 91, 92, 93, 94, 98, 109, 123) and the 132 cells of six further classes declared as oracles (manas, mati, dhenu, madhu, pitṛ, mātṛ: s-stems with 6.4.10 / 8.3.24 / 6.1.114, feminine i / u in the non-nadī branch, neuter u, kinship ṛ-stems without 6.4.11) and the 84 cells of the numerals dvi (dual, three genders), tri, catur, pañcan, ṣaṣ, aṣṭan (plural, with the feminine tisṛ / catasṛ: 1.1.24 ṣaṭ saṁjñā, 7.1.22 luk with 1.1.63, 7.1.55 nuṭ, 7.1.53, 7.1.98 with 1.1.47, 7.2.84 ā-branch, 7.2.99 / 7.2.100 / 6.4.4, 7.2.102, 8.4.41 / 8.4.45 ṣaṇṇām, 8.4.56 ṣaṭ) and the 315 cells of the pronouns tad, etad, yad, tyad (masculine, feminine, neuter; tyad masculine), kim and idam in three genders (7.2.102 atva with 6.1.97 pararūpa and 1.1.52, 7.2.103 sarvādeśa with 1.1.55, 4.1.4 ṭāp on the atva-stem, 7.2.106 with 8.3.59 stem-internal, 7.2.108–7.2.113 for idam with 7.1.11 as a clause of 7.1.9, 7.1.23 luk with 1.1.63 for tat / kim / idam, 8.4.56 for tat); every row is load-bearing on at least one cell of the suite (per-row broken sets recorded)",
                "6.1.105 dīrghāj jasi ca is a prohibition and is realised as a clause of 6.1.102's guard (no separate row): after a long vowel the jas takes 6.1.101 / 6.1.77 instead",
                "theorum/141: 48 new stems of every declared class (1,078 cells from vidyut-prakriya, kept as VIDYUT_SUP_LANE.json, a declared oracle of implementation grade) are reported as a fraction in sup_lane and load rows only where they agree; the test exposed the ṇatva scanner's blindness to the kṣ token (vṛkṣeṇa) and the missing 7.1.25 (anyat), both now rows",
                "the two option cells (rājan 7s by 6.4.136, vāri 8s) are compared on their first alternative; the engine realises one branch and records the option as the earlier packet's",
            ],
            "NOT_claimed": ["the vidyut-side cells of the lane (devīḥ, ekāya; the neuter vocative option)", "adas (7.2.107, 8.2.80), the d-case of 7.2.106, the ka-branch of 7.2.112 / 7.1.11 (akac), 6.1.132's sentence-level sulopa, and the vocative of the pronouns; the aṣṭan branch without 7.2.84 (aṣṭa, aṣṭabhiḥ, aṣṭānām by 6.4.7) and 8.4.45's non-nasal branch are not realised (first alternatives only); the 1.4.6 nadī option of mati / dhenu (matyai, matyāḥ, matyām) and 8.3.36's manassu are not realised (first alternatives only); the an-stem option 6.4.136 as a set-valued output, the 58-code carrier of theorum/63 (its ORACLE is transliterated to IAST for comparison), the resolver ladder of theorum/63 (this driver applies rows in a fixed phase order, not by the ladder's conflict resolution — the ladder remains the certified account of rule conflict on rāma)", "RH, YM untouched"],
        },
        "checks": checks, **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=None); args = parser.parse_args()
    payload = build_certificate(); data = canonical_bytes(payload)
    if args.output is not None:
        args.output.write_bytes(data)
    print(payload["status"])
    for name, v in payload.items():
        if isinstance(v, dict) and "checks" in v:
            for k, val in v["checks"].items():
                print(f"    {name}.{k}: {val}")
    print("sha256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
