from __future__ import annotations

"""Exact certificate (theorum/151, 152): THE KṚT RULE-TABLE ENGINE — eight kṛt affixes (kta, ktavatu, tavya, anīya,
tumun, ktvā, tṛc, ṇvul) and, from theorum/152, śatṛ / śānac (the laṭ aṅga as the verbal table builds it) on every root the verbal engine declares, as one ordered table of sūtras over a segmented
state (root | iṭ | affix), read against the independent generator's cells (research/independent_oracle/VIDYUT_KRT_LANE.json).

The table is a third table beside theorum/125's nominal and theorum/129's verbal one: the aṅga rows it shares with the
verbal table (the iṭ of 7.2.35, the guṇa of 7.3.84 / 7.3.86, the vṛddhi of 7.2.115 / 7.2.116, the ir / ur of 7.1.100 /
7.1.102, the samprasāraṇa of 6.1.15 / 6.1.16, the tripādī) are written again here as rows of the same sūtras over the
smaller state; the kernel (theorum/142) counts them as the one sūtra. The root's dhātupāṭha entry supplies its accent
(7.2.10) and its its through theorum/129's loader.

Every row is a sūtra quoted in SOURCES; no float, no classical import.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab.paninian_it_samjna_compiled import its
from proof_lab.sup_rule_table_engine import V, tok
from proof_lab import ting_rule_table_engine as TIN
from proof_lab.ting_rule_table_engine import (CAR, DEASP, GANA, GHU, GUNA, HRASVA, IN, JAS_ALL, JHAL, NASAL, PU_LIST, ROOTS, SAMPRASARANA, VAL, VRDDHI, anudatta, dhatu_entry)

SOURCES = {
    "3.1.96": "tavyattavyānīyaraḥ", "3.1.133": "ṇvultṛcau", "3.2.102": "niṣṭhā", "3.3.10": "tumunṇvulau kriyāyāṁ kriyārthāyām", "3.4.21": "samānakartṛkayoḥ pūrvakāle",
    "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "1.1.5": "kṅiti ca", "1.1.26": "ktaktavatū niṣṭhā", "1.2.18": "na ktvā seṭ", "1.2.19": "niṣṭhā śīṅsvidimidikṣvididhṛṣaḥ",
    "1.2.26": "ralo vyupadhād dhalādeḥ saṁś ca", "7.1.1": "yuvor anākau", "2.4.36": "ado jagdhir lyap ti kiti", "2.4.52": "aster bhūḥ", "2.4.53": "bruvo vaciḥ",
    "6.1.50": "mīnātiminotidīṅāṁ lyapi ca", "7.2.10": "ekāca upadeśe 'nudāttāt", "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.11": "śryukaḥ kiti",
    "7.2.14": "śvīdito niṣṭhāyām", "7.2.15": "yasya vibhāṣā", "7.2.16": "āditaś ca", "7.2.44": "svaratisūtisūyatidhūñūdito vā",
    "7.2.56": "udito vā", "7.2.37": "graho 'liṭi dīrghaḥ", "7.2.38": "vṝto vā",
    "7.3.84": "sārvadhātukārdhadhātukayoḥ", "7.3.86": "pugantalaghūpadhasya ca", "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "7.3.34": "nodāttopadeśasya māntasyānācameḥ",
    "7.3.32": "hanas to 'ciṇṇaloḥ", "7.3.54": "ho hanter ñṇinneṣu", "6.1.78": "eco 'yavāyāvaḥ", "7.1.100": "ṝta id dhātoḥ", "7.1.102": "udoṣṭhyapūrvasya", "8.2.77": "hali ca",
    "6.4.37": "anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti", "6.1.15": "vacisvapiyajādīnāṁ kiti", "6.1.16": "grahijyāvayivyadhivaṣṭivicativṛścatipṛcchatibhṛjjatīnāṁ ṅiti ca",
    "6.4.66": "ghumāsthāgāpājahātisāṁ hali", "7.4.40": "dyatisyatimāsthām it ti kiti", "7.4.42": "dadhāter hiḥ", "7.4.46": "do dad ghoḥ", "6.4.64": "āto lopa iṭi ca",
    "6.4.63": "dīṅo yuḍ aci kṅiti", "6.4.24": "aniditāṁ hala upadhāyāḥ kṅiti",
    "8.2.42": "radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ", "8.2.43": "saṁyogāder āto dhātor yaṇvataḥ", "8.2.44": "lvādibhyaḥ", "8.2.45": "oditaś ca", "8.2.46": "kṣiyo dīrghāt",
    "8.2.52": "paco vaḥ", "8.2.56": "nudavidondatrāghrāhrībhyo 'nyatarasyām", "8.2.57": "na dhyākhyāpṝmūrchimadām",
    "8.2.30": "coḥ kuḥ", "8.2.31": "ho ḍhaḥ", "8.2.32": "dāder dhātor ghaḥ", "8.2.36": "vraścabhrasjasṛjamṛjayajarājabhrājacchaśāṁ ṣaḥ", "8.2.40": "jhaṣas tathor dho 'dhaḥ",
    "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade", "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "8.4.41": "ṣṭunā ṣṭuḥ", "8.4.53": "jhalāṁ jaś jhaśi",
    "3.1.25": "satyāpapāśarūpavīṇātūlaślokasenālomatvacavarmavarṇacūrṇacurādibhyo ṇic", "6.4.51": "ṇer aniṭi", "6.4.52": "niṣṭhāyāṁ seṭi", "7.1.58": "idito nuṁ dhātoḥ", "8.3.24": "naś cāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ",
    "6.4.19": "cchvoḥ śūḍ anunāsike ca", "6.1.77": "iko yaṇ aci", "6.4.2": "halaḥ", "7.4.43": "jahāteś ca ktvi", "7.3.33": "āto yuk ciṇkṛtoḥ", "6.1.101": "akaḥ savarṇe dīrghaḥ", "1.2.8": "rudavidamuṣagrahisvapipracchaḥ sa~ś ca",
    "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "6.1.65": "ṇo naḥ", "7.3.85": "jāgro 'viciṇṇalṅitsu", "7.2.114": "mṛjer vṛddhiḥ", "6.4.42": "janasanakhanāṁ sañjhaloḥ", "6.4.15": "anunāsikasya kvijhaloḥ kṅiti", "7.1.64": "labheś ca",
    "3.2.124": "laṭaḥ śatṛśānacāv aprathamāsamānādhikaraṇe", "3.4.113": "tiṅśit sārvadhātukam", "7.2.82": "āne muk", "7.2.83": "īdāsaḥ", "7.4.21": "śīṅaḥ sārvadhātuke guṇaḥ", "6.1.97": "ato guṇe",
    "8.3.13": "ḍho ḍhe lopaḥ", "6.3.111": "ḍhralope pūrvasya dīrgho 'ṇaḥ", "8.4.56": "vāvasāne",
}
LANE_FILE = Path(__file__).resolve().parent.parent / "research" / "independent_oracle" / "VIDYUT_KRT_LANE.json"
AFFIX = {   # the affix after its its (1.3.2–1.3.8): the sounds that stand
    "kta": ("ta", True), "ktavatu": ("tavat", True), "ktvā": ("tvā", True), "tavya": ("tavya", False), "anīya": ("anīya", False), "tumun": ("tum", False), "tṛc": ("tṛ", False), "ṇvul": ("vu", False),
    "śatṛ": ("at", False), "śānac": ("āna", False),   # theorum/152: śit (3.4.113 sārvadhātuka), apit → ṅidvat (1.2.4); the laṭ aṅga stands before them
}
SARVA_KRT = ("śatṛ", "śānac")
NISTHA = ("kta", "ktavatu")   # 1.1.26 ktaktavatū niṣṭhā
NIT_KRT = ("ṇvul",)           # ṇit: vṛddhi by 7.2.115 / 7.2.116
NATVA_PASS = set(V) | {"k", "kh", "g", "gh", "ṅ", "p", "ph", "b", "bh", "m", "h", "y", "v", "ṁ"}
ODIT = {"o~hāk", "o~vrascū~", "o~lajī~", "o~lasjī~", "o~bhrasjī~", "ṭuo~śvi", "o~vijī~"}   # the odit roots in the table (the upadeśa carries o; read by its)


class K:
    def __init__(self, root: str, affix: str):
        if root in NASAL:
            up, g, _, _ = NASAL[root]
        else:
            up, _ = ROOTS[root]; g = GANA.get(root, 1)
        r = its(up, "dhatu")["remaining"]
        if up.endswith("aṣ") and r.endswith("a"):
            r = r[:-1]
        self.r = tok(r); self.up_root = up; self.gana = g; self.root = root; self.affix = affix
        pd0 = NASAL[root][2] if root in NASAL else ROOTS[root][1]
        self.pada = {"śatṛ": "P", "śānac": "A"}.get(affix, pd0 if pd0 in ("P", "A") else "P")   # 3.2.124 under 1.3.78 / 1.3.12: śatṛ with the parasmaipada, śānac with the ātmanepada
        self.it: list[str] = []
        self.aff = tok(AFFIX[affix][0]); self.kit0 = AFFIX[affix][1]
        self.flags: set[str] = set(); self.done: set[str] = set(); self.path: list[str] = []
        self.odit = any(k == "o" and v == "1.3.2" for k, v in its(up, "dhatu")["its"].items())
        self.udit = any(k in ("u", "ū") and v == "1.3.2" for k, v in its(up, "dhatu")["its"].items())
        self.idit = any(k == "i" and v == "1.3.2" for k, v in its(up, "dhatu")["its"].items()) and up.endswith("i~")
        self.adit = any(k == "ā" and v == "1.3.2" for k, v in its(up, "dhatu")["its"].items())
        self.iidit = any(k == "ī" and v == "1.3.2" for k, v in its(up, "dhatu")["its"].items())

    def form(self): return "".join(self.r + self.it + self.aff)
    def nxt(self): return (self.it + self.aff)[:1]
    def kit(self):   # 1.1.5 kṅiti ca: the kit affix withholds guṇa / vṛddhi — unless 1.2.18 (the seṭ ktvā is not kit) or 1.2.19 (the niṣṭhā after śī, svid, mid, kṣvid, dhṛṣ is not kit)
        if not self.kit0:
            return False
        if self.affix == "ktvā" and self.up_root in ("rudi~r", "vida~", "muṣa~", "graha~", "ñiṣvapa~", "pracha~"):
            return True   # 1.2.8 rudavidamuṣagrahisvapipracchaḥ saṁś ca
        if self.affix == "ktvā" and self.it and not ("1.2.26" in self.flags):
            return False   # 1.2.18 na ktvā seṭ
        if self.affix in NISTHA and self.up_root in ("śīṅ", "ñiṣvidā~", "ñimidā~", "ñikṣvidā~", "ñidhṛṣā~") and "aniṭ" not in self.flags and (self.it or self.set_()):
            return False   # 1.2.19: the seṭ niṣṭhā after śī, svid, mid, kṣvid, dhṛṣ is not kit (śayita; dhṛṣṭa is aniṭ by 7.2.16)
        return True
    def nit(self): return self.affix in NIT_KRT
    def set_(self):   # the root is seṭ (7.2.10 ekāca upadeśe 'nudāttāt: the anudātta upadeśa is aniṭ)
        return anudatta(self.up_root, self.gana) is not True
    def laghu_upadha(self):
        return len(self.r) >= 2 and self.r[-1] not in V and self.r[-2] in ("a", "i", "u", "ṛ") and self.r[-1] != "kṣ"


Rule = tuple[str, Callable[[K], bool], Callable[[K], Any], str]


def _conj_init(s: K) -> bool:
    return len(s.r) >= 2 and s.r[0] not in V and s.r[1] not in V


def rules() -> list[Rule]:
    R: list[Rule] = []
    def add(n, g, a, note): R.append((n, g, a, note))
    # ---- phase 0: śatṛ / śānac — the laṭ aṅga as theorum/129's verbal table builds it (3.2.124; 3.4.113) ------
    add("3.2.124", lambda s: s.affix in SARVA_KRT, lambda s: _lat_anga(s), "śatṛ / śānac for laṭ: the aṅga before the 3p sārvadhātuka of laṭ, built by the verbal table (bhavat, juhvat, krīṇat, sunvat, kurvat, ghnat, sat, yat; bruvāṇa, dadāna, kurvāṇa)")
    add("7.4.21", lambda s: s.affix == "śānac" and s.up_root == "śīṅ", lambda s: setattr(s, "r", tok("śay")), "guṇa of śī before the sārvadhātuka, ay before the vowel (śayāna; the ruṭ of 7.1.6 is jha's)")
    add("7.2.83", lambda s: s.affix == "śānac" and s.up_root == "āsa~", lambda s: setattr(s, "aff", tok("īna")), "īna for āna after ās (āsīna)")
    add("6.1.97", lambda s: s.affix == "śatṛ" and s.r[-1] == "a" and s.aff[:1] == ["a"], lambda s: s.r.pop(), "pararūpa: the a of the aṅga and the a of at are one a (bhavat, adat, tudat, corayat)")
    add("7.2.82", lambda s: s.affix == "śānac" and s.r[-1] == "a" and s.aff == tok("āna"), lambda s: setattr(s, "aff", tok("māna")), "muk to the a-final aṅga before āna (bhavamāna, edhamāna, labhamāna, corayamāṇa)")
    # ---- phase 1: the root before the ārdhadhātuka kṛt (2.4, 6.1) ----------------------------------------
    add("2.4.52", lambda s: s.up_root == "asa~" and s.r == tok("as"), lambda s: (setattr(s, "r", tok("bhū")), setattr(s, "up_root", "bhū"), setattr(s, "gana", 1)), "bhū for as before the ārdhadhātuka (bhūta, bhavitum)")
    add("2.4.53", lambda s: s.up_root == "brūñ" and s.r == tok("brū"), lambda s: (setattr(s, "r", tok("vac")), setattr(s, "up_root", "vaca~"), setattr(s, "gana", 2)), "vac for brū before the ārdhadhātuka (ukta, vaktum)")
    add("2.4.36", lambda s: s.up_root == "ada~" and s.kit0 and s.aff[:1] == ["t"], lambda s: setattr(s, "r", tok("jagdh")), "jagdh for ad before the t-initial kit (jagdha, jagdhvā)")
    add("6.1.64", lambda s: s.r[0] == "ṣ", lambda s: (s.r.__setitem__(0, "s"), s.r.__setitem__(1, {"ṭ": "t", "ṭh": "th", "ḍ": "d", "ḍh": "dh", "ṇ": "n"}[s.r[1]]) if len(s.r) > 1 and s.r[1] in ("ṭ", "ṭh", "ḍ", "ḍh", "ṇ") else None, s.r.__setitem__(-1, "n") if s.r[-1] == "ṇ" and s.r[0] == "s" else None), "s for the initial ṣ of the upadeśa, with the ṭu and the ṇ it had conditioned read back as tu and n (stotum, snātum, sanitum: the Kāśikā's reading of 6.1.64 — declared)")
    add("6.1.65", lambda s: s.r[0] == "ṇ", lambda s: s.r.__setitem__(0, "n"), "n for the initial ṇ of the upadeśa (netum, nayanīya)")
    add("7.3.85", lambda s: s.up_root == "jāgṛ" and s.r[-1] == "ṛ", lambda s: setattr(s, "r", s.r[:-1] + tok("ar")), "guṇa of jāgṛ before all but vi, ciṇ, ṇal, ṅit (jāgarita, jāgaritum, jāgaraka)")
    add("7.2.114", lambda s: s.up_root == "mṛjū~" and not s.kit() and s.r == tok("mṛj"), lambda s: setattr(s, "r", tok("mārj")), "vṛddhi of mṛj before the non-kit (mārjitum, mārjaka; mṛṣṭa)")
    add("7.1.64", lambda s: s.up_root == "ḍulabhaṣ" and s.r == tok("labh") and (s.aff[0] in V or s.affix == "ṇvul"), lambda s: setattr(s, "r", tok("lambh")), "num to labh before the vowel-initial ārdhadhātuka (lambhanīya, lambhaka)")
    add("3.1.25", lambda s: s.gana == 10 and "ṇic" not in s.flags, lambda s: (s.flags.add("ṇic"), s.r.append("i")), "ṇic to the curādi root; the ṇic-ending is the dhātu (3.1.32)")
    add("7.1.1", lambda s: s.affix == "ṇvul" and s.aff == tok("vu"), lambda s: setattr(s, "aff", tok("aka")), "aka for vu (ṇvul)")
    add("7.1.58", lambda s: s.idit and "7.1.58" not in s.done, lambda s: s.r.insert(max(i for i, x in enumerate(s.r[:-1] if "ṇic" in s.flags else s.r) if x in V) + 1, "n"), "nuṁ to the idit root (hiṁs, kaṁs, dambh)")
    add("6.1.50", lambda s: s.up_root in ("ḍumiñ", "mīñ", "dīṅ") and s.r[-1] in ("i", "ī") and not s.kit0, lambda s: s.r.__setitem__(-1, "ā"), "ā for mi, mī, dī before the non-kit ārdhadhātuka (mātum, mātavya; mita by 7.4.40)")
    # ---- phase 2: the aṅga ----------------------------------------------------------------------------------
    add("7.3.86c", lambda s: "ṇic" in s.flags and s.r[-1] == "i" and len(s.r) >= 3 and s.r[-2] not in V and s.r[-3] in ("i", "u", "ṛ") and "7.3.86c" not in s.done, lambda s: s.r.__setitem__(-3, GUNA[s.r[-3]]) if s.r[-3] != "ṛ" else s.r.__setitem__(slice(-3, -2), tok("ar")), "guṇa of the laghu upadhā before ṇic (cor, cint …)")
    add("6.4.51", lambda s: "ṇic" in s.flags and s.r[-1] == "i" and (s.aff[0] in V or s.affix == "ṇvul"), lambda s: s.r.pop(), "the ṇi dropped before the aniṭ ārdhadhātuka (coraṇīya, coraka)")
    add("6.4.52", lambda s: "ṇic" in s.flags and s.r[-1] == "i" and s.affix in NISTHA, lambda s: s.r.pop(), "the ṇi dropped before the seṭ niṣṭhā (corita)")
    add("7.2.11", lambda s: s.kit() and (s.r[-1] in ("u", "ū", "ṛ", "ṝ") or s.up_root == "śriñ"), lambda s: s.flags.add("aniṭ"), "no iṭ for the kit affix after śri and the u- / ṛ-final root (bhūta, kṛta, śrita)")
    add("7.2.14", lambda s: s.affix in NISTHA and (s.iidit or s.up_root == "ṭuo~śvi"), lambda s: s.flags.add("aniṭ"), "no iṭ in the niṣṭhā after śvi and the īdit root (dīpta, śūna)")
    add("7.2.16", lambda s: s.affix in NISTHA and s.adit, lambda s: s.flags.add("aniṭ"), "no iṭ in the niṣṭhā after the ādit root (svinna, kṣāma)")
    add("7.2.15", lambda s: s.affix in NISTHA and s.udit and s.set_(), lambda s: s.flags.add("aniṭ"), "no iṭ in the niṣṭhā after the root whose iṭ is optional (7.2.44 ūdito vā: the udit; dhūta, gūḍha)")
    add("7.2.56", lambda s: s.affix == "ktvā" and s.udit, lambda s: s.flags.add("aniṭ"), "the udit root's iṭ before ktvā is optional: the aniṭ branch realised (dyutvā; dyutitvā recorded)")
    add("1.2.26", lambda s: s.affix == "ktvā" and s.r[0] not in V and len(s.r) >= 2 and s.r[-2] in ("i", "u") and s.r[-1] not in V and s.r[-1] not in ("h", "y", "v") and "aniṭ" not in s.flags and s.set_(), lambda s: s.flags.add("1.2.26"), "the seṭ ktvā after the hal-initial ral-final root with an i / u upadhā is optionally kit: the kit branch realised (gudhitvā, kuṣitvā; godhitvā recorded)")
    add("7.2.35", lambda s: not s.it and s.aff[0] in VAL and "aniṭ" not in s.flags and ("seṭ" in s.flags or "ṇic" in s.flags or s.set_()), lambda s: setattr(s, "it", ["i"]), "iṭ to the valādi ārdhadhātuka after the seṭ root (bhavitum, patita, devitvā)")
    add("7.2.37", lambda s: s.up_root == "graha~" and s.it == ["i"], lambda s: setattr(s, "it", ["ī"]), "the iṭ of grah long (gṛhīta, gṛhītvā, grahītum)")
    add("6.4.42", lambda s: s.kit() and s.nxt() and s.nxt()[0] in JHAL and s.up_root in ("janī~", "ṣaṇu~", "khanu~") and s.r[-1] == "n", lambda s: s.r.__setitem__(slice(-2, None), ["ā"]), "ā for the n of jan, san, khan before the jhal-initial kit, merged with the a by 6.1.101 (jāta, sāta, khāta, sātvā)")
    add("6.4.37", lambda s: s.kit() and s.r[-1] in ("n", "m", "ṇ") and s.nxt() and s.nxt()[0] in JHAL and (anudatta(s.up_root, s.gana) is True or s.up_root in ("vana~", "tanu~", "kṣaṇu~", "kṣiṇu~", "ṛṇu~", "tṛṇu~", "ghṛṇu~", "vanu~", "manu~")), lambda s: s.r.pop(), "the anunāsika of the anudāttopadeśa / van / the tanādi dropped before the jhal-initial kit (gata, hata, mata, tata)")
    add("6.4.15", lambda s: s.kit() and s.r[-1] in ("n", "m") and s.nxt() and s.nxt()[0] in JHAL and "6.4.37" not in s.done and len(s.r) >= 2 and s.r[-2] in ("a", "i", "u"), lambda s: s.r.__setitem__(-2, {"a": "ā", "i": "ī", "u": "ū"}[s.r[-2]]), "the vowel before the anunāsika-final root long before the jhal-initial kit (śānta, kānta, dānta)")
    add("6.1.15", lambda s: s.kit() and (s.r in (tok("vac"), tok("svap"), tok("yaj"), tok("vad"), tok("vap"), tok("vah"), tok("ve"), tok("vye"), tok("hve")) or (s.r == tok("vas") and s.gana == 1)), lambda s: setattr(s, "r", tok({"vac": "uc", "svap": "sup", "yaj": "ij", "vad": "ud", "vap": "up", "vah": "uh", "vas": "us", "ve": "u", "vye": "vī", "hve": "hū"}["".join(s.r)])), "samprasāraṇa of vac, svap, yaj, vad, vap, vah, vas before the kit (ukta, supta, iṣṭa, udita, uṣita)")
    add("6.1.16", lambda s: s.kit() and s.up_root in SAMPRASARANA and "".join(s.r) in ("grah", "jyā", "vyadh", "prach", "bhrasj"), lambda s: setattr(s, "r", tok({"grah": "gṛh", "jyā": "ji", "vyadh": "vidh", "prach": "pṛch", "bhrasj": "bhṛj"}["".join(s.r)])), "samprasāraṇa of grah, jyā, vyadh, prach before the kit (gṛhīta, jīta, viddha, pṛṣṭa)")
    add("6.4.24", lambda s: s.kit() and not s.idit and len(s.r) >= 3 and s.r[-2] == "n" and s.r[-1] not in V and s.r[-3] in V, lambda s: s.r.pop(-2), "the n upadhā of the non-idit root dropped before the kit (grathita, mathita, baddha, skabhita)")
    add("6.4.19", lambda s: s.kit() and s.r[-1] == "v" and s.r[-2] in ("i", "u") and s.nxt() and s.nxt()[0] in JHAL, lambda s: s.r.__setitem__(-1, "ū"), "ūṭh for the v before the jhal-initial kit (dyūta, syūta)")
    add("6.1.77", lambda s: "6.4.19" in s.done and s.r[-2] in ("i", "u") and s.r[-1] == "ū", lambda s: s.r.__setitem__(-2, {"i": "y", "u": "v"}[s.r[-2]]), "yaṇ for the ik before the vowel (dyūta)")
    add("7.4.43", lambda s: s.affix == "ktvā" and s.up_root == "o~hāk" and s.r == tok("hā"), lambda s: setattr(s, "r", tok("hi")), "hi for hā before ktvā (hitvā)")
    add("7.4.40", lambda s: s.kit() and s.aff[:1] == ["t"] and s.up_root in ("do~", "ṣo~", "mā", "ṣṭhā") and s.r[-1:] == ["ā"], lambda s: s.r.__setitem__(-1, "i"), "i for do, so, mā, sthā before the t-initial kit (dita, sita, mita, sthita)")
    add("7.4.42", lambda s: s.kit() and s.aff[:1] == ["t"] and s.up_root == "ḍudhāñ" and s.r == tok("dhā"), lambda s: setattr(s, "r", tok("hi")), "hi for dhā before the t-initial kit (hita, hitvā)")
    add("7.4.46", lambda s: s.kit() and s.aff[:1] == ["t"] and s.up_root == "ḍudāñ" and s.r == tok("dā"), lambda s: setattr(s, "r", tok("dad")), "dad for dā of ghu before the t-initial kit (datta, dattvā)")
    add("6.4.2", lambda s: "6.1.16" in s.done and s.r[-1] in ("i", "u") and len(s.r) >= 2 and s.r[-2] not in V, lambda s: s.r.__setitem__(-1, {"i": "ī", "u": "ū"}[s.r[-1]]), "the samprasāraṇa vowel long after the hal (jīta, jītvā)")
    add("6.4.66", lambda s: s.kit() and s.r[-1:] == ["ā"] and s.nxt() and s.nxt()[0] not in V and (s.root in GHU or s.up_root in ("māṅ", "ṣṭhā", "gā", "pā~", "o~hāk", "ṣo~")), lambda s: s.r.__setitem__(-1, "ī"), "ī for ghu, mā, sthā, gā, pā, hā, sā before the hal-initial kit (pīta, gīta, hīna)")
    add("6.4.64", lambda s: s.r[-1:] == ["ā"] and s.it and not s.kit(), lambda s: s.r.pop(), "the ā dropped before iṭ (dātā … not here: the ārdhadhātuka iṭ after ā — jāgaritum-type; recorded)")
    add("7.1.100", lambda s: s.r[-1] == "ṝ" and s.kit(), lambda s: setattr(s, "r", s.r[:-1] + tok("ir")), "ir for the ṝ-final root before the kit (kīrṇa, tīrṇa)")
    add("7.1.102", lambda s: s.r[-2:] == ["i", "r"] and "7.1.100" in s.done and len(s.r) >= 3 and s.r[-3] in ("p", "ph", "b", "bh", "m", "v"), lambda s: s.r.__setitem__(-2, "u"), "ur after the labial (pūrṇa, mūrṇa)")
    add("8.2.77", lambda s: "7.1.100" in s.done and s.r[-1] == "r" and s.r[-2] in ("i", "u") and s.nxt() and s.nxt()[0] not in V, lambda s: s.r.__setitem__(-2, {"i": "ī", "u": "ū"}[s.r[-2]]), "the i / u long before r + hal (kīrṇa, pūrṇa)")
    add("7.3.86", lambda s: not s.kit() and s.laghu_upadha() and not s.nit() and "7.3.86" not in s.done, lambda s: s.r.__setitem__(-2, GUNA.get(s.r[-2], s.r[-2])) if s.r[-2] != "ṛ" else s.r.__setitem__(slice(-2, -1), tok("ar")), "guṇa of the laghu upadhā before the non-kit ārdhadhātuka (bhettum, bodhanīya, kartum)")
    add("7.3.32", lambda s: s.nit() and s.up_root == "hana~" and s.r == tok("han"), lambda s: setattr(s, "r", tok("ghāt")), "ghāt for han before ṇvul (7.3.54: ghātaka)")
    add("7.2.116", lambda s: s.nit() and len(s.r) >= 2 and s.r[-1] not in V and s.r[-1] != "kṣ" and s.r[-2] == "a" and "7.3.85" not in s.done and not (s.r[-1] == "m" and anudatta(s.up_root, s.gana) is not True), lambda s: s.r.__setitem__(-2, "ā"), "vṛddhi of the upadhā a before the ṇit (pācaka, gāmaka; 7.3.34 withholds it from the m-final udāttopadeśa: śamaka; not across kṣ: jakṣaka)")
    add("7.2.115", lambda s: s.nit() and s.r[-1] in VRDDHI, lambda s: setattr(s, "r", s.r[:-1] + tok(VRDDHI[s.r[-1]])), "vṛddhi of the final vowel before the ṇit (kāraka, nāyaka)")
    add("7.3.86n", lambda s: s.nit() and s.laghu_upadha() and s.r[-2] in ("i", "u", "ṛ") and "7.3.86" not in s.done, lambda s: s.r.__setitem__(-2, GUNA.get(s.r[-2], s.r[-2])) if s.r[-2] != "ṛ" else s.r.__setitem__(slice(-2, -1), tok("ar")), "guṇa of the laghu upadhā before ṇvul (bhedaka, bodhaka, kartaka)")
    add("7.3.84", lambda s: not s.kit() and not s.nit() and s.r[-1] in GUNA, lambda s: setattr(s, "r", s.r[:-1] + tok(GUNA[s.r[-1]])), "guṇa of the final ik before the non-kit ārdhadhātuka (bhavitum, netavya, kartṛ, śayita, devitvā)")
    add("7.2.38", lambda s: s.it == ["i"] and (s.r[-2:] == ["a", "r"] and s.up_root.endswith("ṝ") or s.up_root == "vṛṅ"), lambda s: setattr(s, "it", ["ī"]), "the iṭ after the ṝ-final root and vṛ long: one branch (karītum; karitum recorded)")
    add("7.3.33", lambda s: s.nit() and s.r[-1] == "ā", lambda s: s.r.append("y"), "yuk to the ā-final root before the ṇit kṛt (dāyaka, bhāyaka)")
    add("6.1.101", lambda s: s.r[-1] in ("a", "ā") and s.aff[:1] == ["a"], lambda s: (s.r.pop(), s.aff.__setitem__(0, "ā")), "savarṇadīrgha at the junction (dānīya, bhānīya)")
    add("6.1.78", lambda s: s.r[-1] in ("e", "ai", "o", "au") and s.nxt() and s.nxt()[0] in V, lambda s: setattr(s, "r", s.r[:-1] + tok({"e": "ay", "ai": "āy", "o": "av", "au": "āv"}[s.r[-1]])), "ay / av for the final ec before the vowel (nayanīya, bhavanīya, nāyaka, bhāvaka)")
    # ---- phase 3: the niṣṭhā's own rows (8.2.42–8.2.57, read as the ādeśa of the affix's t) --------------------
    add("8.2.57", lambda s: s.affix in NISTHA and s.up_root in ("dhyai", "khyā", "pṝ", "murcchā~", "madī~"), lambda s: s.flags.add("no-na"), "no n for dhyā, khyā, pṝ, mūrch, mad (dhyāta, khyāta, pūrta, mūrta, matta)")
    add("8.2.42", lambda s: s.affix in NISTHA and "no-na" not in s.flags and "7.4.46" not in s.done and s.aff[:1] == ["t"] and not s.it and s.r[-1] in ("r", "d"), lambda s: (s.aff.__setitem__(0, "n"), s.r.__setitem__(-1, "n") if s.r[-1] == "d" else None), "n for the niṣṭhā's t after r / d, and for that d (bhinna, chinna, kīrṇa, tīrṇa)")
    add("8.2.43", lambda s: s.affix in NISTHA and "no-na" not in s.flags and s.aff[:1] == ["t"] and not s.it and s.r[-1] == "ā" and _conj_init(s) and s.r[0] not in V and any(x in ("y", "v", "r", "l") for x in s.r[:2]), lambda s: s.aff.__setitem__(0, "n"), "n after the conjunct-initial ā-final root with a yaṇ (glāna, mlāna)")
    add("8.2.44", lambda s: s.affix in NISTHA and "no-na" not in s.flags and s.aff[:1] == ["t"] and not s.it and s.gana == 9 and s.up_root in ("lūñ", "dhūñ", "jyā") and s.r[-1] in ("ū", "ī"), lambda s: s.aff.__setitem__(0, "n"), "n after the lvādi (lūna, pūna, dhūna, śīna)")
    add("8.2.45", lambda s: s.affix in NISTHA and "no-na" not in s.flags and s.aff[:1] == ["t"] and not s.it and s.odit, lambda s: s.aff.__setitem__(0, "n"), "n after the odit root (hīna, lagna, vinna)")
    add("8.2.52", lambda s: s.affix in NISTHA and s.aff[:1] == ["t"] and s.up_root == "ḍupacaṣ", lambda s: (setattr(s, "r", tok("pak")), s.aff.__setitem__(0, "v")), "pakva (nipātana: the k and the v)")
    add("8.2.56", lambda s: s.affix in NISTHA and s.aff[:1] == ["t"] and not s.it and s.up_root in ("ṇuda~", "vida~", "undī~", "trai", "ghrā", "hrī"), lambda s: s.aff.__setitem__(0, "n"), "n optionally after nud, vid, und, trā, ghrā, hrī: the n branch realised (nunna, vinna, unna; nutta recorded)")
    # ---- phase 4: the tripādī (8.2.1 order) --------------------------------------------------------------------
    add("8.3.24", lambda s: "n" in s.r[:-1] and any(s.r[i] == "n" and s.r[i + 1] in JHAL for i in range(len(s.r) - 1)) or (s.r[-1] in ("n", "m") and s.nxt() and s.nxt()[0] in JHAL), lambda s: [s.r.__setitem__(i, "ṁ") for i in range(len(s.r)) if s.r[i] in ("n", "m") and (s.r + s.it + s.aff)[i + 1] in JHAL], "anusvāra for the n / m before jhal (hiṁsita, gaṁtavya → gantavya)")
    add("8.2.36", lambda s: s.nxt() and s.nxt()[0] in JHAL and ("".join(s.r) in ("vraśc", "bhrasj", "bhṛj", "sṛj", "mṛj", "yaj", "ij", "rāj", "bhrāj", "mṛś", "dṛś", "spṛś", "viś", "diś", "riś", "liś", "kṛś", "kruś", "daṁś", "paś", "naś") or s.r[-1] in ("ś", "ch")), lambda s: s.r.__setitem__(-1, "ṣ"), "ṣ for the final of vraśc, bhrasj, sṛj, mṛj, yaj, rāj, bhrāj and of the ch- / ś-final root before jhal (dṛṣṭa, iṣṭa, mṛṣṭa, naṣṭa)")
    add("8.2.30", lambda s: s.r[-1] in ("c", "ch", "j", "jh") and s.nxt() and s.nxt()[0] in JHAL and "8.2.36" not in s.done, lambda s: s.r.__setitem__(-1, {"c": "k", "ch": "k", "j": "g", "jh": "g"}[s.r[-1]]), "ku for the cu before jhal (ukta, pakta, bhukta, yukta)")
    add("8.2.31", lambda s: s.r[-1] == "h" and s.nxt() and s.nxt()[0] in JHAL and not (s.r[0] in ("d",) and len(s.r) >= 2), lambda s: s.r.__setitem__(-1, "ḍh"), "ḍh for h before jhal (līḍha, rūḍha, gūḍha)")
    add("8.2.32", lambda s: s.r[-1] == "h" and s.nxt() and s.nxt()[0] in JHAL and s.r[0] == "d", lambda s: s.r.__setitem__(-1, "gh"), "gh for the h of the d-initial root (dagdha, dugdha, digdha)")
    add("8.2.40", lambda s: s.r[-1] in ("jh", "bh", "gh", "ḍh", "dh") and s.aff[:1] in (["t"], ["th"]) and not s.it, lambda s: s.aff.__setitem__(0, "dh"), "dh for the t after a jhaṣ (labdha, buddha, dagdha, līḍha)")
    add("8.4.41", lambda s: s.r[-1] in ("ṣ", "ṭ", "ṭh", "ḍ", "ḍh") and s.aff[:1] in (["t"], ["th"], ["dh"]) and not s.it, lambda s: s.aff.__setitem__(0, {"t": "ṭ", "th": "ṭh", "dh": "ḍh"}[s.aff[0]]), "ṣṭutva: the t after ṣ / ṭu (dṛṣṭa, iṣṭa, līḍha)")
    add("8.3.13", lambda s: s.r[-1] == "ḍh" and s.aff[:1] == ["ḍh"], lambda s: (s.r.pop(), s.flags.add("ḍh-lopa")), "the ḍh before ḍh dropped (līḍha, leḍhum)")
    add("6.3.111", lambda s: "ḍh-lopa" in s.flags and "6.3.111" not in s.done and s.r[-1] in ("a", "i", "u"), lambda s: s.r.__setitem__(-1, {"a": "ā", "i": "ī", "u": "ū"}[s.r[-1]]), "the aṇ before the dropped ḍh long (līḍha, rūḍha, gūḍha)")
    add("8.4.53", lambda s: s.r[-1] in JAS_ALL and s.r[-1] in ("bh", "gh", "dh", "jh", "ḍh", "b", "g", "d", "j") and s.aff[:1] and s.aff[0] in ("dh", "ḍh", "d", "b", "g", "j"), lambda s: s.r.__setitem__(-1, JAS_ALL[s.r[-1]]), "jaś before jhaś (labdha, buddha, dagdha, dugdha)")
    add("8.4.53c", lambda s: s.r[-1] in ("bh", "gh", "dh", "jh", "ḍh", "b", "g", "d", "j") and s.aff[:1] and s.aff[0] in ("t", "th", "ṭ") and not s.it, lambda s: s.r.__setitem__(-1, CAR.get(s.r[-1], s.r[-1])), "car before khar (8.4.55: yuktvā-type cells where the root ends in a voiced stop before t)")
    add("8.4.58", lambda s: "ṁ" in s.r, lambda s: [s.r.__setitem__(i, {"k": "ṅ", "kh": "ṅ", "g": "ṅ", "gh": "ṅ", "c": "ñ", "ch": "ñ", "j": "ñ", "jh": "ñ", "ṭ": "ṇ", "ṭh": "ṇ", "ḍ": "ṇ", "ḍh": "ṇ", "t": "n", "th": "n", "d": "n", "dh": "n", "p": "m", "ph": "m", "b": "m", "bh": "m"}.get((s.r + s.it + s.aff)[i + 1], "ṁ")) for i in range(len(s.r)) if s.r[i] == "ṁ"], "parasavarṇa for the anusvāra before yay (gantavya, dambhita, kaṁsita keeps ṁ)")
    add("8.4.1", lambda s: (s.aff[:1] == ["n"] and s.r[-1] in ("r", "ṣ")) or (s.r[-1] == "n" and "8.2.42" in s.done and len(s.r) >= 3 and (s.r[-2] in ("r", "ṛ", "ṝ", "ṣ") or (s.r[-2] in V and (s.r[-3] in ("r", "ṛ", "ṝ", "ṣ") or s.r[-3].endswith("ṣ"))))), lambda s: (s.r.__setitem__(-1, "ṇ") if s.r[-1] == "n" else None, s.aff.__setitem__(0, "ṇ") if s.aff[:1] == ["n"] else None), "ṇ for the n after r / ṣ, across a vowel too (8.4.2), in the same pada: kīrṇa, tīrṇa, pūrṇa; the nn of 8.2.42 after ṛ / kṣ both ṇ (chṛṇṇa, kṣuṇṇa — the Kāśikā's forms, declared)")
    add("8.4.2", lambda s: _natva_site(s) is not None, lambda s: _natva_set(s), "ṇ for the n after r / ṛ / ṣ across vowels, ku, pu (karaṇīya, śravaṇīya, kṣīṇa, hariṇīya)")
    return R


def _natva_site(s: K):
    seq = s.r + s.it + s.aff
    for i, x in enumerate(seq):
        if x != "n" or i < len(s.r) + len(s.it):
            continue
        nxt = seq[i + 1] if i + 1 < len(seq) else None
        if nxt is None or nxt in JHAL:
            continue
        j = i - 1
        while j >= 0:
            if seq[j] in ("r", "ṛ", "ṝ", "ṣ") or seq[j].endswith(("ṣ", "r")):
                return i
            if seq[j] not in NATVA_PASS and not all(ch in NATVA_PASS for ch in seq[j]):
                break
            j -= 1
    return None


def _natva_set(s: K) -> None:
    i = _natva_site(s); s.aff[i - len(s.r) - len(s.it)] = "ṇ"


RULES = rules()
IDS = [r[0] for r in RULES]
SARVA_ROWS = {"3.2.124", "7.4.21", "7.2.83", "7.2.82", "6.1.97", "6.1.101", "8.4.2"}   # the rows that read the śatṛ / śānac state; the aṅga itself is the verbal table's


def _lat_anga(s: K) -> None:
    """The laṭ 3p form of the verbal table with its ending removed: anti / ati (7.1.3 / 7.1.4) in parasmaipada, ante / ate in ātmanepada."""
    form = TIN.conjugate(s.root, "laṭ", "3p", pada=s.pada)[0]
    for end in ("anti", "ati", "ante", "ate", "nti"):
        if form.endswith(end):
            stem = form[: -len(end)] + ("a" if end in ("anti", "ante") else "")
            break
    else:
        raise ValueError(f"{s.root}: the laṭ 3p ending not read ({form})")
    s.r = tok(stem); s.flags.add("laṭ-aṅga")
    if s.gana == 3 or s.up_root in TIN.JAKSADI:
        s.flags.add("abhyasta")
    if s.up_root in TIN.KSUBHNADI:
        s.flags.add("kṣubhnādi")   # 8.4.39: read by the nominal table's ṇatva   # 6.1.5 ubhe abhyastam: read by 7.1.78 for the śatṛ's num
    if TIN.conjugate(s.root, "laṭ", "3s", pada=s.pada)[0].endswith(("ati", "āti", "ate", "āte")):
        s.flags.add("aṅga-a")   # the aṅga before the sārvadhātuka ends in a / ā (śap, śa, śyan, śnā, the ā-root): read by 7.1.80 / 7.1.81 for the feminine and the neuter dual


def norm_id(rid: str) -> str:
    return rid.rstrip("abcdefghijklmnopqrstuvwxyz")
HOOK = None


def derive(root: str, affix: str, off=()) -> tuple[str, list[str]]:
    s = derive_state(root, affix, off)
    return s.form(), s.path


def derive_state(root: str, affix: str, off=()) -> K:
    s = K(root, affix)
    s.path.append(f"{root} ({s.up_root}) + {affix} → {''.join(s.aff)}")
    for n, guard, action, note in RULES:
        if n in off or (s.affix in SARVA_KRT and n not in SARVA_ROWS):
            continue
        before = (s.form(), frozenset(s.flags))
        if guard(s):
            action(s)
            after = (s.form(), frozenset(s.flags))
            if after != before:
                s.done.add(n); s.path.append(f"{n} {note}: {s.form()}")
    return s


def lane_oracle() -> dict[str, list[str]]:
    if not LANE_FILE.exists():
        return {}
    return json.loads(LANE_FILE.read_text(encoding="utf-8"))["cells"]


def t1_lane() -> dict[str, Any]:
    O = lane_oracle(); rows = {}
    for key, forms in O.items():
        r, _, a = key.split("|")
        try:
            ours = derive(r, a)[0]
        except Exception as e:  # noqa: BLE001
            ours = f"ENGINE_ERROR {e}"
        rows[key] = {"ours": ours, "vidyut": forms, "agree": ours in forms}
    by_aff = {a: [sum(1 for k, x in rows.items() if k.endswith("|" + a) and x["agree"]), sum(1 for k in rows if k.endswith("|" + a))] for a in AFFIX}
    return {"cells": len(rows), "agree": sum(1 for x in rows.values() if x["agree"]), "by_affix": by_aff, "disagree": {k: x for k, x in rows.items() if not x["agree"]}, "agreeing_keys": [k for k, x in rows.items() if x["agree"]]}


def t2_load_bearing(agreeing: list[str]) -> dict[str, Any]:
    O = lane_oracle(); dead = []
    for n in IDS:
        changed = False
        for key in agreeing:
            r, _, a = key.split("|")
            try:
                if derive(r, a, off=(n,))[0] != derive(r, a)[0]:
                    changed = True; break
            except Exception:  # noqa: BLE001
                changed = True; break
        if not changed:
            dead.append(n)
    return {"rows": len(IDS), "not_load_bearing": dead}


def build_certificate() -> dict[str, Any]:
    t1 = t1_lane(); t2 = t2_load_bearing(t1["agreeing_keys"])
    checks = {"t1_lane_read": t1["cells"] > 0, "t2_every_row_load_bearing_on_an_agreeing_cell": not t2["not_load_bearing"]}
    status = "PASS_KRT_RULE_TABLE_ENGINE_CANDIDATE" if all(checks.values()) else "FAIL_KRT_RULE_TABLE_ENGINE_CANDIDATE"
    return {"schema": "rkf.krt_rule_table_engine_candidate.v1", "status": status, "checks": checks, "rows": [(n, note) for n, _, _, note in RULES], "sources": SOURCES,
            "lane": {k: t1[k] for k in ("cells", "agree", "by_affix", "disagree")}, "load_bearing": t2,
            "claim_boundary": {"proved_by_exact_finite_certificate": ["every agreeing lane cell is derived by the rows in table order; every row is load-bearing on an agreeing cell"],
                               "declared": ["the lane (vidyut-prakriya) as an oracle of implementation grade; the disagreeing cells are listed, each with the engine's form"],
                               "NOT_claimed": ["the disagreeing cells; lyuṭ, ghañ, ṇini, kvip, the taddhita; the declension of the kṛdanta; accent; RH, YM"]}}


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", default=None); a = ap.parse_args()
    cert = build_certificate()
    print(cert["status"]); print("    lane:", cert["lane"]["cells"], cert["lane"]["agree"], cert["lane"]["by_affix"]); print("    not load-bearing:", cert["load_bearing"]["not_load_bearing"])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
