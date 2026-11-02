from __future__ import annotations

"""Exact certificate (theorum/125): THE SUP RULE-TABLE ENGINE — one table in which
every sūtra of the nominal declension is a record (number, guard, action), one
driver that applies the table in the Aṣṭādhyāyī's own phase order (affix
substitution → aṅga operations → augments → junction sandhi → tripādī), and
fifteen certified paradigms as its ORACLES: rāma (theorum/63), bālā (88), nadī
(89), kartṛ (90), hari / guru (91), rājan / marut / ātman (92), phala / vāri (93),
sarva (94), sarvā (98), bhavat (109), daṇḍin (123) — 330 cells reproduced exactly from the
earlier pinned packets, and each table row shown load-bearing on at least one
cell of the suite (the per-row broken sets are recorded).

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
    "4.1.2": "svaujasamauṭchaṣṭābhyāmbhisṅebhyāmbhyasṅasibhyāmbhyasṅasosāṅṅyossup", "1.1.42": "śi sarvanāmasthānam", "1.1.43": "suḍ anapuṁsakasya", "1.4.17": "svādiṣv asarvanāmasthāne", "1.4.18": "yaci bham", "1.4.7": "śeṣo ghy asakhi", "1.4.3": "yū stryākhyau nadī", "1.1.27": "sarvādīni sarvanāmāni",
    "7.1.9": "ato bhisa ais", "7.1.12": "ṭāṅasiṅasām inātsyāḥ", "7.1.13": "ṅer yaḥ", "7.1.14": "sarvanāmnaḥ smai", "7.1.15": "ṅasiṅyoḥ smātsminau", "7.1.17": "jasaḥ śī", "7.1.19": "napuṁsakāc ca", "7.1.20": "jaśśasoḥ śiḥ", "7.1.23": "svamor napuṁsakāt", "7.1.24": "ato 'm",
    "7.1.52": "āmi sarvanāmnaḥ suṭ", "7.1.54": "hrasvanadyāpo nuṭ", "7.1.70": "ugidacāṁ sarvanāmasthāne 'dhātoḥ", "7.1.72": "napuṁsakasya jhalacaḥ", "7.1.94": "ṛd uśanaspurudaṁso 'nehasāṁ ca",
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
JAS = {"t": "d", "k": "g", "p": "b", "ṭ": "ḍ", "c": "j"}
CAR = {v: k for k, v in JAS.items()}
AT_KU_PU = set(V) | {"h", "y", "v", "r", "k", "kh", "g", "gh", "ṅ", "p", "ph", "b", "bh", "m", "ṁ"}
MULTI = ("kh", "gh", "ch", "jh", "ṭh", "ḍh", "th", "dh", "ph", "bh", "ai", "au", "kṣ")
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"), ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
SNS = {"1s", "1d", "1p", "2s", "2d", "8s"}


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
        self.sns = code in SNS
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
    def r_(self): return "tṛ" in self.flags
    def pada(self):
        # 1.4.17: before the consonant-initial sup (not sns) ; and when the sup has been deleted (1.1.62)
        return (not self.sns and bool(self.aff) and self.aff[0] not in V) or (not self.aff)
    def bha(self): return not self.sns and self.vinit()


Rule = tuple[str, Callable[[S], bool], Callable[[S], None], str]


def rules() -> list[Rule]:
    R: list[Rule] = []
    def add(n, guard, action, note): R.append((n, guard, action, note))
    # ---- phase 1: affix substitutions (7.1, 7.3) -------------------------------------------
    add("7.1.24", lambda s: s.g == "n" and s.a_final() and s.code in ("1s", "2s"), lambda s: setattr(s, "aff", ["a", "m"]), "su / am → am after the neuter a-stem")
    add("7.1.23", lambda s: s.g == "n" and not s.a_final() and s.code in ("1s", "2s"), lambda s: setattr(s, "aff", []), "su / am deleted after the neuter (luk)")
    add("7.1.19", lambda s: s.g == "n" and s.code in ("1d", "2d"), lambda s: setattr(s, "aff", ["ī"]), "au → śī after the neuter")
    add("7.1.20", lambda s: s.g == "n" and s.code in ("1p", "2p"), lambda s: (setattr(s, "aff", ["i"]), s.flags.add("śi"), setattr(s, "sns", True)), "jas / śas → śi after the neuter (1.1.42: sarvanāmasthāna)")
    add("7.1.73", lambda s: s.g == "n" and s.final() in ("i", "u", "ṛ") and s.vinit() and "num" not in s.flags and s.up != "ām", lambda s: _num(s), "num to the ik-final neuter before a vowel-initial vibhakti")
    add("7.1.72", lambda s: s.g == "n" and "śi" in s.flags and (s.final() in V or s.final() not in ("n", "m")), lambda s: _num(s), "num to the neuter jhal / ac stem before śi")
    add("7.1.17", lambda s: s.sarva() and s.a_final() and s.up == "jas" and s.g != "n", lambda s: setattr(s, "aff", ["ī"]), "jas → śī after an a-final sarvanāma (ataḥ continuing from 7.1.9)")
    add("7.1.14", lambda s: s.sarva() and s.a_final() and s.up == "ṅe", lambda s: setattr(s, "aff", ["s", "m", "ai"]), "ṅe → smai after a sarvanāma")
    add("7.1.15", lambda s: s.sarva() and s.a_final() and s.up in ("ṅasi~", "ṅi"), lambda s: setattr(s, "aff", ["s", "m", "ā", "t"] if s.up == "ṅasi~" else ["s", "m", "i", "n"]), "ṅasi / ṅi → smāt / smin")
    add("7.1.52", lambda s: s.sarva() and s.final() in ("a", "ā") and s.up == "ām", lambda s: setattr(s, "aff", ["s", "ā", "m"]), "suṭ to ām after a sarvanāma")
    add("7.1.9", lambda s: s.a_final() and s.up == "bhis" and "7.1.9" not in s.done, lambda s: setattr(s, "aff", ["ai", "s"]), "bhis → ais after a")
    add("7.1.12", lambda s: s.a_final() and s.up in ("ṭā", "ṅasi~", "ṅas") and "7.1.15" not in s.done, lambda s: setattr(s, "aff", {"ṭā": ["i", "n", "a"], "ṅasi~": ["ā", "t"], "ṅas": ["s", "y", "a"]}[s.up]), "ṭā / ṅasi / ṅas → ina / āt / sya after a")
    add("7.1.13", lambda s: s.a_final() and s.up == "ṅe" and s.aff == ["e"], lambda s: setattr(s, "aff", ["y", "a"]), "ṅe → ya after a")
    add("7.1.18", lambda s: s.ap() and s.up == "auṭ", lambda s: setattr(s, "aff", ["ī"]), "au → śī after an āp")
    add("7.1.54", lambda s: s.up == "ām" and s.aff == ["ā", "m"] and (s.final() in SHORT or s.nadi() or s.ap()), lambda s: setattr(s, "aff", ["n", "ā", "m"]), "nuṭ to ām after a short vowel / nadī / āp")
    add("6.4.3", lambda s: s.aff[:3] == ["n", "ā", "m"] and s.final() in SHORT, lambda s: s.st.__setitem__(-1, LONG[s.final()]), "the aṅga's short final lengthened before nām")
    add("7.3.120", lambda s: s.ghi() and s.g != "f" and s.up == "ṭā", lambda s: setattr(s, "aff", ["n", "ā"]), "ṭā → nā after a ghi (not feminine)")
    add("7.3.118", lambda s: s.ghi() and s.up == "ṅi", lambda s: setattr(s, "aff", ["au"]), "ṅi → au after i / u")
    add("7.3.119", lambda s: s.ghi() and s.up == "ṅi" and s.aff == ["au"], lambda s: s.st.__setitem__(-1, "a"), "… and the ghi's final → a")
    add("7.3.111", lambda s: s.ghi() and s.ngit() and s.up != "ṅi", lambda s: s.st.__setitem__(-1, GUNA[s.final()]), "guṇa of the ghi before a ṅit")
    add("7.3.112", lambda s: s.nadi() and s.ngit(), lambda s: _set_final(s, [YAN[s.final()], "ā"]), "āṭ before the ṅit after a nadī (ṭit → initial, 1.1.46; ī → y before it, 6.1.77)")
    add("7.3.114", lambda s: s.sarva() and s.ap() and s.ngit(), lambda s: (s.st.__setitem__(-1, "a"), setattr(s, "st", s.st + ["s", "y", "ā"])), "syāṭ before the ṅit after a feminine sarvanāma, with hrasva of the ā")
    add("7.3.113", lambda s: s.ap() and s.ngit() and "7.3.114" not in s.done, lambda s: setattr(s, "st", s.st + ["y", "ā"]), "yāṭ before the ṅit after an āp")
    add("7.3.116", lambda s: (s.nadi() or s.ap()) and s.up == "ṅi", lambda s: setattr(s, "aff", s.aff[:-1] + ["ā", "m"]), "ṅi → ām after nadī / āp")
    add("7.3.105", lambda s: s.ap() and s.up in ("ṭā", "os"), lambda s: s.st.__setitem__(-1, "e"), "ā → e before ṭā / os")
    add("7.3.106", lambda s: s.ap() and s.samb, lambda s: s.st.__setitem__(-1, "e"), "ā → e in the sambuddhi")
    add("7.3.107", lambda s: s.nadi() and s.samb, lambda s: s.st.__setitem__(-1, "i"), "nadī shortened in the sambuddhi")
    add("7.3.108", lambda s: s.samb and s.final() in ("i", "u") and "7.3.107" not in s.done, lambda s: s.st.__setitem__(-1, GUNA[s.final()]), "guṇa of the short final in the sambuddhi")
    add("7.3.109", lambda s: s.final() in ("i", "u") and s.up == "jas", lambda s: s.st.__setitem__(-1, GUNA[s.final()]), "guṇa before jas")
    add("7.3.110", lambda s: s.final() == "ṛ" and (s.up == "ṅi" or (s.sns and not s.samb and s.up != "su~")) and not s.flags & {"7.1.94"}, lambda s: _set_final(s, ["a", "r"]), "ṛ → ar before ṅi and sarvanāmasthāna (1.1.51)")
    add("7.3.110s", lambda s: s.final() == "ṛ" and s.samb, lambda s: _set_final(s, ["a", "r"]), "ṛ → ar in the sambuddhi (7.3.110 with 8.2.24 below)")
    add("7.1.94", lambda s: s.r_() and s.final() == "ṛ" and s.code == "1s", lambda s: (_set_final(s, ["a", "n"]), s.flags.add("7.1.94")), "anaṅ to the tṛ-stem before su")
    add("6.4.11", lambda s: s.r_() and s.sns and not s.samb and s.st[-2:] == ["a", "r"], lambda s: s.st.__setitem__(-2, "ā"), "upadhā dīrgha of the tṛc-stem before sarvanāmasthāna")
    add("7.3.102", lambda s: s.a_final() and s.aff and s.aff[0] in ("bh", "y") and s.up in ("bhyām", "ṅe"), lambda s: s.st.__setitem__(-1, "ā"), "a → ā before the yañ-initial sup (bhyām)")
    add("7.3.103", lambda s: s.a_final() and (s.up in ("bhyas", "sup") or (s.aff[:1] == ["s"] and s.num == "p")), lambda s: s.st.__setitem__(-1, "e"), "a → e before bhyas / su")
    add("7.3.104", lambda s: s.a_final() and s.up == "os", lambda s: s.st.__setitem__(-1, "e"), "a → e before os")
    # ---- phase 2: augments and aṅga operations --------------------------------------------
    add("7.1.70", lambda s: s.ugit() and s.sns, lambda s: _num(s), "num to the ugit stem before sarvanāmasthāna")
    add("6.4.14", lambda s: s.ugit() and s.code == "1s" and s.st[-2:] == ["n", "t"], lambda s: s.st.__setitem__(-3, "ā"), "upadhā dīrgha of the at-stem before su")
    add("6.4.13", lambda s: s.in_() and s.code == "1s", lambda s: s.st.__setitem__(-2, "ī"), "in-stem lengthened before su")
    add("6.4.12", lambda s: s.in_() and "śi" in s.flags, lambda s: s.st.__setitem__(-2, "ī"), "in-stem lengthened before śi")
    add("6.4.8", lambda s: (s.an() or (s.g == "n" and "num" in s.flags and s.st[-1] == "n")) and s.sns and not s.samb and not s.in_(), lambda s: s.st.__setitem__(-2, LONG.get(s.st[-2], s.st[-2])), "upadhā dīrgha of the n-stem before sarvanāmasthāna")
    add("6.1.68", lambda s: s.code in ("1s", "8s") and s.aff == ["s"] and (s.final() not in V or s.final() in ("ī", "ā")) and not (s.samb and s.final() in ("ī", "ā")), lambda s: setattr(s, "aff", []), "su dropped after a consonant / ī / ā")
    add("6.1.69", lambda s: s.samb and s.aff == ["s"] and (s.final() in ("e", "o") or s.final() in SHORT or s.st[-2:] == ["a", "r"]), lambda s: setattr(s, "aff", []), "sambuddhi su dropped after eṅ / a short vowel")
    add("6.4.134", lambda s: s.an() and s.bha() and not (s.up == "ṅi" and "6.4.136" in s.flags) and not (len(s.st) >= 4 and s.st[-3] in ("v", "m") and s.st[-4] not in V), lambda s: s.st.__delitem__(-2), "a of an dropped in the bha (6.4.137: not after a cluster ending in v / m)")
    add("8.4.40", lambda s: s.st[-1] == "n" and len(s.st) >= 2 and s.st[-2] in ("j", "c", "ch", "jh"), lambda s: s.st.__setitem__(-1, "ñ"), "n → ñ after j")
    # ---- phase 3: junction sandhi ----------------------------------------------------------
    add("6.1.107", lambda s: s.final() in ("a", "ā", "i", "ī", "u", "ū") and s.aff[:2] == ["a", "m"] and s.code in ("2s", "1s"), lambda s: setattr(s, "aff", s.aff[1:]), "ak + am → the pūrva")
    add("6.1.103", lambda s: s.g == "m" and s.up == "śas" and s.final() in ("a", "i", "u", "ṛ") and s.aff == ["a", "s"], lambda s: (s.st.__setitem__(-1, LONG[s.final()]), setattr(s, "aff", ["n"])), "ak + śas → pūrvasavarṇa dīrgha (6.1.102) and s → n in the masculine")
    add("6.1.102", lambda s: s.up in ("jas", "auṭ", "śas") and s.final() in ("a", "i", "u", "ṛ", "ī", "ū") and s.aff and s.aff[0] in V and not (s.final() in ("a", "ā") and s.aff[0] not in ("a", "ā")) and s.g != "n" and not (s.final() in ("ī", "ū") and s.up != "śas"), lambda s: (s.st.__setitem__(-1, LONG.get(s.final(), s.final())), setattr(s, "aff", s.aff[1:])), "ak + a-initial 1st / 2nd ending → pūrvasavarṇa dīrgha (6.1.104 nādici: not after a before ic; 6.1.105 dīrghāj jasi ca: not after a long vowel before jas — both prohibitions live in this guard)")
    add("6.1.110", lambda s: s.final() in ("e", "o") and s.up in ("ṅasi~", "ṅas") and s.aff[:1] == ["a"], lambda s: setattr(s, "aff", s.aff[1:]), "eṅ + as → pūrvarūpa")
    add("6.1.111", lambda s: s.final() == "ṛ" and s.up in ("ṅasi~", "ṅas") and s.aff[:1] == ["a"], lambda s: (_set_final(s, ["u", "r"]), setattr(s, "aff", s.aff[1:])), "ṛ + as → ur")
    add("6.1.88", lambda s: s.final() in ("a", "ā") and s.aff[:1] in (["au"], ["ai"], ["e"], ["o"]), lambda s: (_set_final(s, [{"au": "au", "ai": "ai", "e": "ai", "o": "au"}[s.aff[0]]]), setattr(s, "aff", s.aff[1:])), "a + ec → vṛddhi")
    add("6.1.87", lambda s: s.final() in ("a", "ā") and s.aff[:1] in (["i"], ["u"], ["ī"], ["ū"]), lambda s: (_set_final(s, [GUNA[s.aff[0]]]), setattr(s, "aff", s.aff[1:])), "a + ik → guṇa")
    add("6.1.101", lambda s: s.final() in ("a", "ā") and s.aff[:1] in (["a"], ["ā"]), lambda s: (_set_final(s, ["ā"]), setattr(s, "aff", s.aff[1:])), "a + a → ā")
    add("6.1.78", lambda s: s.final() in AYADI and s.vinit(), lambda s: _set_final(s, AYADI[s.final()]), "ec → ay / av / āy / āv before a vowel")
    add("6.1.77", lambda s: s.final() in YAN and s.vinit() and not (s.final() in ("i", "u") and s.aff[0] == s.final()), lambda s: _set_final(s, [YAN[s.final()]]), "ik → yaṇ before a vowel")
    # ---- phase 4: the tripādī (8.2.1 order) -------------------------------------------------
    add("8.2.7", lambda s: s.pada() and s.final() == "n" and not (s.samb and s.flags & {"an", "in"} or s.samb and s.st[-2] in ("a", "i")), lambda s: s.st.pop(), "pada-final n dropped")
    add("8.2.23", lambda s: s.pada() and s.st[-2:] == ["n", "t"], lambda s: s.st.pop(), "pada-final cluster loses its last sound")
    add("8.2.24", lambda s: s.st[-1] == "r" and s.aff == ["s"], lambda s: setattr(s, "aff", []), "s dropped after r at the pada end (kartur-s → kartur)")
    add("8.2.39", lambda s: s.pada() and s.final() in JAS and s.aff, lambda s: s.st.__setitem__(-1, JAS[s.final()]), "pada-final jhal → jaś")
    add("8.4.55", lambda s: s.pada() and s.final() in CAR and s.aff and s.aff[0] in ("s", "k", "t", "p", "c", "ṭ", "ś", "ṣ"), lambda s: s.st.__setitem__(-1, CAR[s.final()]), "jaś → car before khar")
    add("8.3.59", lambda s: s.aff[:1] == ["s"] and s.final() in ("i", "ī", "u", "ū", "ṛ", "ṝ", "e", "o", "ai", "au", "r") and (s.code == "7p" or s.aff[:3] == ["s", "ā", "m"]), lambda s: s.aff.__setitem__(0, "ṣ"), "s of sup → ṣ after iṇ")
    add("8.4.2", lambda s: True, lambda s: _natva(s), "n → ṇ after r / ṣ / ṛ across aṭ / ku / pu (not pada-final: 8.4.37)")
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
        if x != "n" or i == len(w) - 1:
            continue
        j = i - 1
        while j >= 0 and w[j] in AT_KU_PU and w[j] not in ("r", "ṛ", "ṝ"):
            j -= 1
        if j >= 0 and w[j] in ("r", "ṣ", "ṛ", "ṝ"):
            w[i] = "ṇ"
    n = len(s.st); s.st, s.aff = w[:n], w[n:]


RULES = rules()
IDS = [r[0] for r in RULES]


def decline(stem, code, up, gender="m", flags=(), off=()) -> tuple[str, list[str]]:
    s = S(stem, code, up, gender, flags)
    for n, guard, action, note in RULES:
        if n in off:
            continue
        before = ("".join(s.st), "".join(s.aff))
        if guard(s):
            action(s)
            after = ("".join(s.st), "".join(s.aff))
            if after != before:
                s.done.add(n); s.path.append(f"{n} {note}: {after[0]}-{after[1]}")
    return "".join(s.st + s.aff), s.path


def paradigm(stem, gender="m", flags=(), off=()) -> dict[str, str]:
    return {c: decline(stem, c, up, gender, flags, off)[0] for c, up in SUP}


SUITE = {  # name: (stem, gender, flags, oracle source)
    "rāma": ("rāma", "m", (), "theorum/63"), "bālā": ("bālā", "f", ("āp",), "theorum/88"), "nadī": ("nadī", "f", ("nadī",), "theorum/89"),
    "kartṛ": ("kartṛ", "m", ("tṛ",), "theorum/90"), "hari": ("hari", "m", (), "theorum/91"), "guru": ("guru", "m", (), "theorum/91"),
    "rājan": ("rājan", "m", ("an",), "theorum/92"), "marut": ("marut", "m", (), "theorum/92"), "phala": ("phala", "n", (), "theorum/93"), "vāri": ("vāri", "n", (), "theorum/93"),
    "sarva": ("sarva", "m", ("sarvanāma",), "theorum/94"), "sarvā": ("sarvā", "f", ("sarvanāma", "āp"), "theorum/98"), "ātman": ("ātman", "m", ("an",), "theorum/92"), "bhavat": ("bhavat", "m", ("ugit",), "theorum/109"), "daṇḍin": ("daṇḍin", "m", ("in",), "theorum/123"),
}
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
    return o


def t1_suite() -> dict[str, Any]:
    O = oracles()
    forms = {n: paradigm(*SUITE[n][:3]) for n in SUITE}
    mism = {n: {c: (forms[n][c], O[n][c]) for c, _ in SUP if forms[n][c] != O[n][c]} for n in SUITE}
    cells = sum(len(SUP) for _ in SUITE)
    broken = {}
    for rid in IDS:
        b = []
        for n in SUITE:
            p = paradigm(*SUITE[n][:3], off=(rid,))
            b += [f"{n}.{c}" for c, _ in SUP if p[c] != O[n][c]]
        broken[rid] = b
    vacuous = [r for r in IDS if not broken[r]]
    checks = {"all_330_cells_equal_the_certified_oracles": all(not mism[n] for n in SUITE),
              "every_rule_row_is_load_bearing_on_the_suite": not vacuous}
    return {"checks": checks, "cells": cells, "mismatches": {n: m for n, m in mism.items() if m}, "broken_counts": {r: len(b) for r, b in broken.items()}, "broken": broken, "vacuous_rows": vacuous,
            "paths": {"rāma.3s": decline("rāma", "3s", "ṭā")[1], "nadī.4s": decline("nadī", "4s", "ṅe", "f", ("nadī",))[1], "kartṛ.1s": decline("kartṛ", "1s", "su~", "m", ("tṛ",))[1], "vāri.1p": decline("vāri", "1p", "jas", "n")[1]}}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_suite": t1_suite()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE" if all(checks.values()) else "FAIL_SUP_RULE_TABLE_ENGINE_CANDIDATE"
    return {
        "schema": "rkf.sup_rule_table_engine_candidate.v1", "status": status, "sources": SOURCES, "rule_order": IDS,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                f"one rule table of {len(IDS)} rows (each a quoted sūtra as guard + action) and one driver reproduce the 330 cells of fifteen certified paradigms exactly from the earlier pinned packets (theorum/63, 88, 89, 90, 91, 92, 93, 94, 98, 109, 123), and every row is load-bearing on at least one cell of the suite (per-row broken sets recorded)",
                "6.1.105 dīrghāj jasi ca is a prohibition and is realised as a clause of 6.1.102's guard (no separate row): after a long vowel the jas takes 6.1.101 / 6.1.77 instead",
                "the two option cells (rājan 7s by 6.4.136, vāri 8s) are compared on their first alternative; the engine realises one branch and records the option as the earlier packet's",
            ],
            "NOT_claimed": ["feminine sarvanāma (sarvā: theorum/98), ātman (6.4.137), the an-stem option 6.4.136 as a set-valued output, the 58-code carrier of theorum/63 (its ORACLE is transliterated to IAST for comparison), the resolver ladder of theorum/63 (this driver applies rows in a fixed phase order, not by the ladder's conflict resolution — the ladder remains the certified account of rule conflict on rāma)", "RH, YM untouched"],
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
