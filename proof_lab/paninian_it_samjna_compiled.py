from __future__ import annotations

"""Exact certificate (theorum/82): THE IT-SAṀJÑĀ LAYER COMPILED — 1.3.2–1.3.9
as one interpreter on upadeśa forms, augment placement by marker, the aṅga.

Second batch of the all-sūtra programme (ledger: proof_lab/astadhyayi).
Quoted sūtras:

 1.3.1   bhūvādayo dhātavaḥ               bhū and the rest (the listed roots) are dhātu
 1.3.2   upadeśe 'janunāsika it           in the teaching form a nasal vowel is an it
 1.3.3   halantyam                        a final consonant is an it
 1.3.4   na vibhaktau tusmāḥ              not, in a vibhakti, a ta-varga sound, s or m
 1.3.5   ādir ñiṭuḍavaḥ                   initial ñi, ṭu, ḍu (of a dhātu) are it
 1.3.6   ṣaḥ pratyayasya                  initial ṣ of an affix is an it
 1.3.7   cuṭū                             initial ca-varga / ṭa-varga sound of an affix is an it
 1.3.8   laśakv ataddhite                 initial l, ś, ka-varga sound of a non-taddhita affix is an it
 1.3.9   tasya lopaḥ                      the it is elided
 1.1.60  adarśanaṁ lopaḥ                  elision is non-appearance
 1.1.46  ādyantau ṭakitau                 a ṭ-marked augment is prefixed, a k-marked one suffixed
 1.1.47  mid aco 'ntyāt paraḥ             an m-marked augment goes after the last vowel
 3.1.1   pratyayaḥ                        (adhikāra) ... is an affix
 3.1.2   paraś ca                         and it comes after
 1.4.13  yasmāt pratyayavidhis tadādi pratyaye 'ṅgam
                                          from the item that conditions the affix, up to the affix: aṅga
 6.4.1   aṅgasya                          (adhikāra) of the aṅga
 1.4.104 vibhaktiś ca                     (sup and tiṅ) are also vibhakti

Jñāpaka exceptions the tradition reads off later sūtras (declared, cited,
and shown to be load-bearing — the compiled 1.3.7 alone would mark them):
 7.1.3   jho 'ntaḥ                        jh of jha / jhi is not an it
 7.3.50  ṭhasyekaḥ                        ṭh of ṭhak / ṭhañ is not an it
 7.1.2   āyaneyīnīyiyaḥ phaḍhakhacchaghāṁ pratyayādīnām
                                          ch, ḍh (ph, kh, gh) initial of those taddhita affixes are not it
Cited, not compiled: 6.1.64 dhātvādeḥ ṣaḥ saḥ, 6.1.65 ṇo naḥ (initial ṣ / ṇ of
a dhātu is not an it; it is replaced).

 T1  ONE INTERPRETER.  its(upadeśa, kind, flags) computed from 1.3.2–1.3.8
     with 1.3.9 equals the traditional it-set on every one of the 90
     teaching forms listed (sup 21, tiṅ 18, ten lakāras, vikaraṇas, kṛt and
     taddhita affixes, dhātus, augments); the exceptions 1.3.4 (vibhakti),
     'ataddhite' (1.3.8), 'pratyayasya' (1.3.6) and the remainder guard on
     1.3.8 (the l of a lakāra survives: 3.4.77 lasya) are each load-bearing on
     named forms; the three jñāpaka overrides are load-bearing on jhi, jha,
     ṭhak, cha, ḍhak and nowhere else.
 T2  THE HAND-CODED LOPA FUNCTIONS ARE INSTANCES.  theorum/58's it_lopa on
     gam+śap+tip and nī+śap+tip, and theorum/63's it_lopa on all 22 sup
     entries, equal the compiled 1.3.9 (phones and recorded its).
 T3  AUGMENT PLACEMENT AND AṄGA.  1.1.46 / 1.1.47 read the placement off the
     its (tuk after, aṭ / āṭ / iṭ before, num after the last vowel; the u of tuk, num, matup is the anunāsika it of 1.3.2);
     1.4.13 gives the aṅga of each affix as a prefix of the word; on every
     reachable state of theorum/60's gam / nī graph the trigger of
     theorum/80's compiled 7.3.84 equals "aṅga(affix) ends in ik and the
     affix is sārvadhātuka / ārdhadhātuka"; 3.1.2 holds on every state.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import IAST_TO_58, p58, savarna_expand
from proof_lab.paninian_seam_calculus import GAM, NI, it_lopa as it_lopa_58
from proof_lab.seam_compensated_confluence_verdict import explore, word_rules
from proof_lab.shaiva_sources_varga_crystal import VARGAS
from proof_lab.sup_vibhakti_resolver_ladder import SUP, it_lopa as it_lopa_63, st

SOURCES = {
    "1.3.1": "bhūvādayo dhātavaḥ", "1.3.2": "upadeśe 'janunāsika it", "1.3.3": "halantyam", "1.3.4": "na vibhaktau tusmāḥ",
    "1.3.5": "ādir ñiṭuḍavaḥ", "1.3.6": "ṣaḥ pratyayasya", "1.3.7": "cuṭū", "1.3.8": "laśakv ataddhite", "1.3.9": "tasya lopaḥ",
    "1.1.60": "adarśanaṁ lopaḥ", "1.1.46": "ādyantau ṭakitau", "1.1.47": "mid aco 'ntyāt paraḥ", "3.1.1": "pratyayaḥ", "3.1.2": "paraś ca", "3.4.77": "lasya",
    "1.4.13": "yasmāt pratyayavidhis tadādi pratyaye 'ṅgam", "6.4.1": "aṅgasya", "1.4.104": "vibhaktiś ca",
    "7.1.3": "jho 'ntaḥ", "7.3.50": "ṭhasyekaḥ", "7.1.2": "āyaneyīnīyiyaḥ phaḍhakhacchaghāṁ pratyayādīnām",
    "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "6.1.65": "ṇo naḥ",
}

VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
CONSONANTS = ("k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ", "t", "th", "d", "dh", "n",
              "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "ś", "ṣ", "s", "h")
SOUNDS = sorted(VOWELS + CONSONANTS, key=len, reverse=True)
KU, CU, TU_RETRO, TU_DENTAL = (tuple(VARGAS[k]) for k in ("ka", "ca", "ṭa", "ta"))
TUSMA = TU_DENTAL + ("s", "m")                      # 1.3.4
JNAPAKA = {"jh": "7.1.3", "ṭh": "7.3.50", "ch": "7.1.2", "ḍh": "7.1.2"}  # initial of an affix kept, by the cited sūtra


def parse(upadesa: str) -> tuple[tuple[str, bool], ...]:
    """IAST teaching form; a vowel followed by '~' is anunāsika (the nasal mark of the upadeśa)."""
    out: list[tuple[str, bool]] = []
    i = 0
    while i < len(upadesa):
        for s in SOUNDS:
            if upadesa.startswith(s, i):
                i += len(s)
                nasal = i < len(upadesa) and upadesa[i] == "~"
                if nasal:
                    i += 1
                out.append((s, nasal))
                break
        else:
            raise ValueError(upadesa[i:])
    return tuple(out)


def its(upadesa: str, kind: str, vibhakti: bool = False, taddhita: bool = False, jnapaka: bool = True) -> dict[str, Any]:
    """1.3.2–1.3.8 decide the its of a teaching form; 1.3.9 elides them.  kind ∈ {pratyaya, dhatu, agama}."""
    form = parse(upadesa)
    marks: dict[int, str] = {}
    for i, (s, nasal) in enumerate(form):                             # 1.3.2
        if s in VOWELS and nasal:
            marks[i] = "1.3.2"
    last = len(form) - 1
    if form[last][0] in CONSONANTS and not (vibhakti and form[last][0] in TUSMA):   # 1.3.3 with 1.3.4
        marks[last] = "1.3.3"
    first = form[0][0]
    if kind == "dhatu" and len(form) >= 2 and (first, form[1][0]) in (("ñ", "i"), ("ṭ", "u"), ("ḍ", "u")):  # 1.3.5
        marks[0] = "1.3.5"
        marks[1] = "1.3.5"
    if kind == "pratyaya":
        if first == "ṣ":                                              # 1.3.6
            marks[0] = "1.3.6"
        elif first in CU + TU_RETRO:                                  # 1.3.7
            if not (jnapaka and first in JNAPAKA):
                marks[0] = "1.3.7"
        elif first in ("l", "ś") + KU and not taddhita:               # 1.3.8
            if any(i not in marks for i in range(1, len(form))):     # an affix must leave a remainder (3.4.77 lasya: the l-affix is the l)
                marks[0] = "1.3.8"
    remaining = tuple(s for i, (s, _) in enumerate(form) if i not in marks)   # 1.3.9 / 1.1.60
    return {"form": "".join(s + ("~" if n else "") for s, n in form), "its": {form[i][0]: sid for i, sid in sorted(marks.items())},
            "remaining": "".join(remaining), "remaining_sounds": remaining}


# ---------------------------------------------------------------- the traditional it-sets (Siddhānta-kaumudī listings of the upadeśa forms)
# (upadeśa, kind, vibhakti, taddhita, expected remaining, expected its as sound→sūtra)
TRADITION: list[tuple[str, str, bool, bool, str, dict[str, str]]] = [
    # sup (4.1.2)
    ("su~", "pratyaya", True, False, "s", {"u": "1.3.2"}), ("auṭ", "pratyaya", True, False, "au", {"ṭ": "1.3.3"}), ("jas", "pratyaya", True, False, "as", {"j": "1.3.7"}),
    ("am", "pratyaya", True, False, "am", {}), ("śas", "pratyaya", True, False, "as", {"ś": "1.3.8"}),
    ("ṭā", "pratyaya", True, False, "ā", {"ṭ": "1.3.7"}), ("bhyām", "pratyaya", True, False, "bhyām", {}), ("bhis", "pratyaya", True, False, "bhis", {}),
    ("ṅe", "pratyaya", True, False, "e", {"ṅ": "1.3.8"}), ("bhyas", "pratyaya", True, False, "bhyas", {}),
    ("ṅasi~", "pratyaya", True, False, "as", {"ṅ": "1.3.8", "i": "1.3.2"}), ("ṅas", "pratyaya", True, False, "as", {"ṅ": "1.3.8"}),
    ("os", "pratyaya", True, False, "os", {}), ("ām", "pratyaya", True, False, "ām", {}), ("ṅi", "pratyaya", True, False, "i", {"ṅ": "1.3.8"}),
    ("sup", "pratyaya", True, False, "su", {"p": "1.3.3"}),
    # tiṅ (3.4.78)
    ("tip", "pratyaya", True, False, "ti", {"p": "1.3.3"}), ("tas", "pratyaya", True, False, "tas", {}), ("jhi", "pratyaya", True, False, "jhi", {}),
    ("sip", "pratyaya", True, False, "si", {"p": "1.3.3"}), ("thas", "pratyaya", True, False, "thas", {}), ("tha", "pratyaya", True, False, "tha", {}),
    ("mip", "pratyaya", True, False, "mi", {"p": "1.3.3"}), ("vas", "pratyaya", True, False, "vas", {}), ("mas", "pratyaya", True, False, "mas", {}),
    ("ta", "pratyaya", True, False, "ta", {}), ("ātām", "pratyaya", True, False, "ātām", {}), ("jha", "pratyaya", True, False, "jha", {}),
    ("thās", "pratyaya", True, False, "thās", {}), ("āthām", "pratyaya", True, False, "āthām", {}), ("dhvam", "pratyaya", True, False, "dhvam", {}),
    ("iṭ", "pratyaya", True, False, "i", {"ṭ": "1.3.3"}), ("vahi", "pratyaya", True, False, "vahi", {}), ("mahiṅ", "pratyaya", True, False, "mahi", {"ṅ": "1.3.3"}),
    # lakāras (3.2.110ff): the vowel is the anunāsika pronunciation vowel (1.3.2), the final ṭ/ṅ an it (1.3.3); the l itself is the
    # affix that 3.4.77 lasya replaces, so 1.3.8 cannot take it (an affix must leave a remainder) — corrected after external review
    ("la~ṭ", "pratyaya", False, False, "l", {"a": "1.3.2", "ṭ": "1.3.3"}), ("li~ṭ", "pratyaya", False, False, "l", {"i": "1.3.2", "ṭ": "1.3.3"}),
    ("lu~ṭ", "pratyaya", False, False, "l", {"u": "1.3.2", "ṭ": "1.3.3"}), ("lṛ~ṭ", "pratyaya", False, False, "l", {"ṛ": "1.3.2", "ṭ": "1.3.3"}),
    ("le~ṭ", "pratyaya", False, False, "l", {"e": "1.3.2", "ṭ": "1.3.3"}), ("lo~ṭ", "pratyaya", False, False, "l", {"o": "1.3.2", "ṭ": "1.3.3"}),
    ("la~ṅ", "pratyaya", False, False, "l", {"a": "1.3.2", "ṅ": "1.3.3"}), ("li~ṅ", "pratyaya", False, False, "l", {"i": "1.3.2", "ṅ": "1.3.3"}),
    ("lu~ṅ", "pratyaya", False, False, "l", {"u": "1.3.2", "ṅ": "1.3.3"}), ("lṛ~ṅ", "pratyaya", False, False, "l", {"ṛ": "1.3.2", "ṅ": "1.3.3"}),
    # vikaraṇa and other non-taddhita affixes
    ("śap", "pratyaya", False, False, "a", {"ś": "1.3.8", "p": "1.3.3"}), ("śyan", "pratyaya", False, False, "ya", {"ś": "1.3.8", "n": "1.3.3"}),
    ("śnu", "pratyaya", False, False, "nu", {"ś": "1.3.8"}), ("śa", "pratyaya", False, False, "a", {"ś": "1.3.8"}),
    ("śnam", "pratyaya", False, False, "na", {"ś": "1.3.8", "m": "1.3.3"}), ("u", "pratyaya", False, False, "u", {}),
    ("śnā", "pratyaya", False, False, "nā", {"ś": "1.3.8"}), ("yak", "pratyaya", False, False, "ya", {"k": "1.3.3"}),
    ("sya", "pratyaya", False, False, "sya", {}), ("tāsi~", "pratyaya", False, False, "tās", {"i": "1.3.2"}),
    ("ṇic", "pratyaya", False, False, "i", {"ṇ": "1.3.7", "c": "1.3.3"}), ("san", "pratyaya", False, False, "sa", {"n": "1.3.3"}),
    ("ktvā", "pratyaya", False, False, "tvā", {"k": "1.3.8"}), ("kta", "pratyaya", False, False, "ta", {"k": "1.3.8"}),
    ("ktavatu~", "pratyaya", False, False, "tavat", {"k": "1.3.8", "u": "1.3.2"}), ("śatṛ~", "pratyaya", False, False, "at", {"ś": "1.3.8", "ṛ": "1.3.2"}),
    ("śānac", "pratyaya", False, False, "āna", {"ś": "1.3.8", "c": "1.3.3"}), ("tṛc", "pratyaya", False, False, "tṛ", {"c": "1.3.3"}),
    ("ṇvul", "pratyaya", False, False, "vu", {"ṇ": "1.3.7", "l": "1.3.3"}), ("lyuṭ", "pratyaya", False, False, "yu", {"l": "1.3.8", "ṭ": "1.3.3"}),
    ("ghañ", "pratyaya", False, False, "a", {"gh": "1.3.8", "ñ": "1.3.3"}), ("ac", "pratyaya", False, False, "a", {"c": "1.3.3"}),
    ("ka", "pratyaya", False, False, "a", {"k": "1.3.8"}), ("tavya", "pratyaya", False, False, "tavya", {}), ("yat", "pratyaya", False, False, "ya", {"t": "1.3.3"}),
    ("ṇyat", "pratyaya", False, False, "ya", {"ṇ": "1.3.7", "t": "1.3.3"}), ("ṇvi", "pratyaya", False, False, "vi", {"ṇ": "1.3.7"}),
    ("kvip", "pratyaya", False, False, "vi", {"k": "1.3.8", "p": "1.3.3"}), ("ṇamu~l", "pratyaya", False, False, "am", {"ṇ": "1.3.7", "u": "1.3.2", "l": "1.3.3"}),
    ("tumu~n", "pratyaya", False, False, "tum", {"u": "1.3.2", "n": "1.3.3"}), ("ṭāp", "pratyaya", False, False, "ā", {"ṭ": "1.3.7", "p": "1.3.3"}),
    ("ṅīp", "pratyaya", False, False, "ī", {"ṅ": "1.3.8", "p": "1.3.3"}), ("cli", "pratyaya", False, False, "li", {"c": "1.3.7"}),
    ("sic", "pratyaya", False, False, "si", {"c": "1.3.3"}), ("ciṇ", "pratyaya", False, False, "i", {"c": "1.3.7", "ṇ": "1.3.3"}),
    # taddhita affixes
    ("ṣyañ", "pratyaya", False, True, "ya", {"ṣ": "1.3.6", "ñ": "1.3.3"}), ("ṣvun", "pratyaya", False, False, "vu", {"ṣ": "1.3.6", "n": "1.3.3"}),
    ("aṇ", "pratyaya", False, True, "a", {"ṇ": "1.3.3"}), ("ṭhak", "pratyaya", False, True, "ṭha", {"k": "1.3.3"}),
    ("ṭhañ", "pratyaya", False, True, "ṭha", {"ñ": "1.3.3"}), ("cha", "pratyaya", False, True, "cha", {}), ("ḍhak", "pratyaya", False, True, "ḍha", {"k": "1.3.3"}),
    ("phak", "pratyaya", False, True, "pha", {"k": "1.3.3"}), ("kha", "pratyaya", False, True, "kha", {}), ("gha", "pratyaya", False, True, "gha", {}),
    ("kan", "pratyaya", False, True, "ka", {"n": "1.3.3"}), ("matu~p", "pratyaya", False, True, "mat", {"u": "1.3.2", "p": "1.3.3"}),
    ("ḍmatu~p", "pratyaya", False, True, "mat", {"ḍ": "1.3.7", "u": "1.3.2", "p": "1.3.3"}), ("tal", "pratyaya", False, True, "ta", {"l": "1.3.3"}),
    ("tva", "pratyaya", False, True, "tva", {}), ("ini~", "pratyaya", False, True, "in", {"i": "1.3.2"}),
    # dhātus (1.3.1)
    ("gamḷ~", "dhatu", False, False, "gam", {"ḷ": "1.3.2"}), ("paṭha~", "dhatu", False, False, "paṭh", {"a": "1.3.2"}),
    ("ḍukṛñ", "dhatu", False, False, "kṛ", {"ḍ": "1.3.5", "u": "1.3.5", "ñ": "1.3.3"}), ("ṭunadi~", "dhatu", False, False, "nad", {"ṭ": "1.3.5", "u": "1.3.5", "i": "1.3.2"}),
    ("ñimidā~", "dhatu", False, False, "mid", {"ñ": "1.3.5", "i": "1.3.5", "ā": "1.3.2"}), ("bhū", "dhatu", False, False, "bhū", {}),
    ("ṇīñ", "dhatu", False, False, "ṇī", {"ñ": "1.3.3"}), ("ṣṭhā", "dhatu", False, False, "ṣṭhā", {}),
    ("iṣu~", "dhatu", False, False, "iṣ", {"u": "1.3.2"}), ("yama~", "dhatu", False, False, "yam", {"a": "1.3.2"}), ("edha~", "dhatu", False, False, "edh", {"a": "1.3.2"}),
    ("ḍudāñ", "dhatu", False, False, "dā", {"ḍ": "1.3.5", "u": "1.3.5", "ñ": "1.3.3"}), ("ṭuvepṛ~", "dhatu", False, False, "vep", {"ṭ": "1.3.5", "u": "1.3.5", "ṛ": "1.3.2"}),
    # augments (āgama)
    ("tu~k", "agama", False, False, "t", {"u": "1.3.2", "k": "1.3.3"}), ("aṭ", "agama", False, False, "a", {"ṭ": "1.3.3"}), ("āṭ", "agama", False, False, "ā", {"ṭ": "1.3.3"}),
    ("iṭ", "agama", False, False, "i", {"ṭ": "1.3.3"}), ("nu~m", "agama", False, False, "n", {"u": "1.3.2", "m": "1.3.3"}), ("yāsu~ṭ", "agama", False, False, "yās", {"u": "1.3.2", "ṭ": "1.3.3"}),
    ("su~ṭ", "agama", False, False, "s", {"u": "1.3.2", "ṭ": "1.3.3"}), ("mu~k", "agama", False, False, "m", {"u": "1.3.2", "k": "1.3.3"}),
]


def t1_one_interpreter() -> dict[str, Any]:
    mismatches = []
    for up, kind, vib, tad, exp_rem, exp_its in TRADITION:
        r = its(up, kind, vibhakti=vib, taddhita=tad)
        if r["remaining"] != exp_rem or r["its"] != exp_its:
            mismatches.append({"form": up, "got": r, "expected": {"remaining": exp_rem, "its": exp_its}})
    forms = [(row[0], row[1], row[2], row[3]) for row in TRADITION]
    # exceptions load-bearing
    without_1_3_4 = sorted(up for up, kind, vib, tad, exp_rem, _ in TRADITION if vib and its(up, kind, vibhakti=False, taddhita=tad)["remaining"] != exp_rem)
    without_ataddhite = sorted(up for up, kind, vib, tad, exp_rem, _ in TRADITION if tad and its(up, kind, vibhakti=vib, taddhita=False)["remaining"] != exp_rem)
    without_pratyayasya = sorted(up for up, kind, vib, tad, exp_rem, _ in TRADITION if kind == "dhatu" and its(up, "pratyaya", vibhakti=vib, taddhita=tad)["remaining"] != exp_rem)
    without_jnapaka = sorted(up for up, kind, vib, tad, exp_rem, _ in TRADITION if its(up, kind, vibhakti=vib, taddhita=tad, jnapaka=False)["remaining"] != exp_rem)
    checks = {
        "compiled_its_equal_tradition_on_every_listed_form": not mismatches,
        "forms_unique": len(set(forms)) == len(forms),
        "1_3_4_load_bearing_exactly_on_tusma_final_vibhaktis": without_1_3_4 == sorted(up for up, kind, vib, tad, _, _ in TRADITION if vib and parse(up)[-1][0] in TUSMA),
        "ataddhite_load_bearing_on_kha_gha_kan": without_ataddhite == ["gha", "kan", "kha"],
        "pratyayasya_load_bearing_on_dhatu_initial_ṣ_ṇ_g_and_ṭu_ḍu_ñi": without_pratyayasya == sorted(["ṣṭhā", "ṇīñ", "ṭunadi~", "ḍudāñ", "ṭuvepṛ~", "ñimidā~", "ḍukṛñ", "gamḷ~"]),
        "jnapaka_overrides_load_bearing_exactly_on_jhi_jha_thak_than_cha_dhak": without_jnapaka == sorted(["jhi", "jha", "ṭhak", "ṭhañ", "cha", "ḍhak"]),
    }
    return {"checks": checks, "forms": len(forms), "mismatches": mismatches, "without_1_3_4": without_1_3_4, "without_ataddhite": without_ataddhite,
            "without_pratyayasya": without_pratyayasya, "without_jnapaka": without_jnapaka,
            "table": {up: {"its": its(up, k, vibhakti=v, taddhita=t)["its"], "remaining": its(up, k, vibhakti=v, taddhita=t)["remaining"]} for up, k, v, t, _, _ in TRADITION}}


# ---------------------------------------------------------------- T2: the hand-coded lopa functions are instances
def to58(sounds: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(IAST_TO_58.get(s, s) for s in sounds)


def t2_hand_coded_are_instances() -> dict[str, Any]:
    # theorum/58: GAM = gam + śap + tip, NI = nī + śap + tip; it_lopa strips ś/l/k initial and the final consonant of affixes
    rows58 = []
    ok58 = True
    for name, W in (("gam", GAM), ("nI", NI)):
        W1 = it_lopa_58(W)
        for j, up in ((1, "śap"), (2, "tip")):
            c = its(up, "pratyaya", vibhakti=(up == "tip"))
            phones_ok = to58(c["remaining_sounds"]) == W1[j][0]
            mem_ok = all((to58((s,))[0] + "it") in W1[j][1] for s in c["its"])
            ok58 &= phones_ok and mem_ok
            rows58.append({"word": name, "affix": up, "compiled": c["remaining"], "hand_coded": "".join(W1[j][0]), "memory": sorted(W1[j][1]), "equal": phones_ok and mem_ok})
    # theorum/63: all 24 sup entries
    code_to_iast = {"S": "ś", "G": "ṅ", "T": "ṭ", "A": "ā"}
    rows63 = []
    ok63 = True
    for code, aff, feats in SUP:
        iast = "".join(code_to_iast.get(x, x) for x in aff)
        up = iast + ("~" if "su" in feats else "")
        if "sup7" in feats:
            up = "sup"
        c = its(up, "pratyaya", vibhakti=True)
        W = st(("r", "A", "m", "a"), aff if "sup7" not in feats else ("s", "u"), feats)   # theorum/63 declares sup7 as 'su' after its own 1.3.3 step
        out = it_lopa_63(W)
        hand = "".join(out[1])
        comp = "".join(to58(c["remaining_sounds"]))
        eq = hand == comp
        ok63 &= eq
        rows63.append({"code": code, "upadesa": up, "compiled": comp, "hand_coded": hand, "equal": eq})
    checks = {"theorum_58_it_lopa_equals_compiled_1_3_9_on_sap_and_tip": ok58, "theorum_63_it_lopa_equals_compiled_1_3_9_on_all_22_sup_entries": ok63 and len(rows63) == 22}
    return {"checks": checks, "rows_58": rows58, "rows_63": rows63}


# ---------------------------------------------------------------- T3: augment placement (1.1.46 / 1.1.47) and the aṅga (1.4.13)
def placement(agama: str) -> str:
    m = its(agama, "agama")["its"]
    if "k" in m:
        return "after"            # 1.1.46 kit: antaḥ
    if "ṭ" in m:
        return "before"           # 1.1.46 ṭit: ādi
    if "m" in m:
        return "after_last_vowel"  # 1.1.47
    return "undetermined"


def insert_agama(base: tuple[str, ...], agama: str) -> tuple[str, ...]:
    body = its(agama, "agama")["remaining_sounds"]
    where = placement(agama)
    if where == "after":
        return base + body
    if where == "before":
        return body + base
    if where == "after_last_vowel":
        k = max(i for i, s in enumerate(base) if s in VOWELS)
        return base[: k + 1] + body + base[k + 1 :]
    raise ValueError(agama)


def anga_1_4_13(w, j: int) -> tuple[str, ...]:
    """The aṅga of the affix at morpheme index j: everything before it (from the item conditioning the affix)."""
    return tuple(s for m in w[:j] for s in m[0])


def t3_augments_and_anga() -> dict[str, Any]:
    placements = {a: placement(a) for a in ("tu~k", "aṭ", "āṭ", "iṭ", "nu~m", "yāsu~ṭ", "su~ṭ", "mu~k")}
    examples = {
        "a+tuk (before ch, 6.1.73)": "".join(insert_agama(("a",), "tu~k")),
        "aṭ+gam (6.4.71 luṅlaṅlṛṅkṣv aḍ udāttaḥ)": "".join(insert_agama(("g", "a", "m"), "aṭ")),
        "bhavat+num (7.1.70 ugidacāṁ sarvanāmasthāne 'dhātoḥ)": "".join(insert_agama(("bh", "a", "v", "a", "t"), "nu~m")),
        "iṭ+tā (7.2.35 ārdhadhātukasyeḍ valādeḥ)": "".join(insert_agama(("t", "ā"), "iṭ")),
    }
    ik = savarna_expand(p58("i", 1))
    states = set()
    for W0 in (GAM, NI):
        for carry in (True, False):
            states |= set(explore(W0, word_rules(carry))["states"])
    states = sorted(states)
    trigger_equal = True
    paras_ca = True
    n_affix_positions = 0
    for w in states:
        for j, (ph, feats) in enumerate(w):
            if "affix" not in feats:
                continue
            n_affix_positions += 1
            paras_ca &= j > 0 and "affix" not in w[0][1]          # 3.1.1 / 3.1.2: an affix is never first
            anga = anga_1_4_13(w, j)
            cond_anga = bool(anga) and anga[-1] in ik and ("sArvadhAtuka" in feats or "ArdhadhAtuka" in feats)
            prev_ph, prev_f = w[j - 1]
            cond_80 = "root" in prev_f and bool(prev_ph) and prev_ph[-1] in ik and ("sArvadhAtuka" in feats or "ArdhadhAtuka" in feats)
            trigger_equal &= cond_anga == cond_80
    checks = {
        "1_1_46_tuk_after_at_before_from_its_alone": placements["tu~k"] == "after" and placements["aṭ"] == "before" and placements["āṭ"] == "before" and placements["iṭ"] == "before",
        "1_1_47_num_after_last_vowel": placements["nu~m"] == "after_last_vowel" and examples["bhavat+num (7.1.70 ugidacāṁ sarvanāmasthāne 'dhātoḥ)"] == "bhavant",
        "examples_atch_agam_ita": examples["a+tuk (before ch, 6.1.73)"] == "at" and examples["aṭ+gam (6.4.71 luṅlaṅlṛṅkṣv aḍ udāttaḥ)"] == "agam" and examples["iṭ+tā (7.2.35 ārdhadhātukasyeḍ valādeḥ)"] == "itā",
        "7_3_84_trigger_of_theorum_80_equals_anga_1_4_13_ends_in_ik_on_all_reachable_states": trigger_equal and len(states) == 40,
        "3_1_2_paras_ca_holds_on_every_reachable_state": paras_ca and n_affix_positions > 0,
    }
    return {"checks": checks, "placements": placements, "examples": examples, "reachable_states": len(states), "affix_positions": n_affix_positions}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_one_interpreter": t1_one_interpreter(), "t2_hand_coded_are_instances": t2_hand_coded_are_instances(), "t3_augments_and_anga": t3_augments_and_anga()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PANINIAN_IT_SAMJNA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_PANINIAN_IT_SAMJNA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.paninian_it_samjna_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "jnapaka_overrides": JNAPAKA,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "1.3.2–1.3.8 as one interpreter with 1.3.9 reproduce the traditional it-set and remainder of all listed teaching forms; 1.3.4, 'ataddhite', 'pratyayasya' and the three jñāpaka overrides are each load-bearing exactly on the named forms",
                "theorum/58's and theorum/63's hand-coded it_lopa are instances of the compiled 1.3.9 (phones and recorded its)",
                "1.1.46 / 1.1.47 placement read off the its; 1.4.13 aṅga as a prefix; theorum/80's compiled 7.3.84 trigger equals 'aṅga ends in ik' on all 40 reachable states; 3.1.2 holds on every state",
            ],
            "NOT_claimed": [
                "the jñāpaka exceptions are declared from the cited sūtras (7.1.3, 7.3.50, 7.1.2), not derived from them",
                "6.1.64 / 6.1.65 (dhātu-initial ṣ, ṇ) are cited: the certificate shows only that 1.3.6/1.3.7 do not mark them",
                "the 'ir' it (vārttika on 1.3.3), anudātta / svarita its (1.3.12, 1.3.72) and accent are not on the carrier",
                "the list of teaching forms is a finite sample of the Dhātupāṭha and the affix inventory, not the whole",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    payload = build_certificate()
    data = canonical_bytes(payload)
    if args.output is not None:
        args.output.write_bytes(data)
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(f"  {k}: {v}")
    for name in ("t1_one_interpreter", "t2_hand_coded_are_instances", "t3_augments_and_anga"):
        for k, v in payload[name]["checks"].items():
            print(f"    {name}.{k}: {v}")
    print("sha256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
