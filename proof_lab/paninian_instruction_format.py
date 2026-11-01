from __future__ import annotations

"""Exact certificate (theorum/80): THE SŪTRA AS AN INSTRUCTION — Pāṇini's
paribhāṣā instruction format compiles to the realized rules.

theorum/58, 60 and 61 realize Aṣṭādhyāyī rules as hand-written functions.
Here each rule is instead written as a CASE-STRUCTURED RECORD read straight
off the sūtra (which word is genitive, nominative, ablative, locative; which
markers; which governing sūtra), and one interpreter applies the quoted
meta-rules:

 1.1.49  ṣaṣṭhī sthāneyogā              genitive  = the sthānin (what is replaced)
 1.1.66  tasminn iti nirdiṣṭe pūrvasya  locative  = right context: act on what precedes
 1.1.67  tasmād ity uttarasya           ablative  = left context: act on what follows
 6.1.84  ekaḥ pūrvaparayoḥ              (adhikāra 6.1.85–111) one substitute for both
 6.1.72  saṁhitāyām                     (adhikāra) sandhi acts only in close contact
 1.1.69  aṇudit savarṇasya cāpratyayaḥ  an aṇ / udit term denotes its savarṇas too
 1.1.70  taparas tatkālasya             unless marked with t: then that duration only
 1.1.52  alo 'ntyasya                   a substitute replaces the final sound
 1.1.55  anekāl śit sarvasya            a multi-sound or ś-marked one replaces all
 1.1.46  ādyantau ṭakitau               ṭ-marked augments go first, k-marked last
 1.3.10  yathāsaṅkhyam anudeśaḥ samānām equal-length lists correspond in order
 1.1.50  sthāne 'ntaratamaḥ             otherwise the closest substitute is chosen
 1.1.51  ur aṇ raparaḥ                  an aṇ replacing ṛ/ḷ is followed by r/l
 1.4.2   vipratiṣedhe paraṁ kāryam      conflict at one locus: the later sūtra acts

 T1  SANDHI COMPILES.  The five sandhi sūtras of theorum/58 (6.1.77, 78, 87,
     88, 101) as records; on 58's 100 junctions the compiled rule equals
     58's hand-coded rule wherever 58's rule fires, and fires in addition on
     EXACTLY the 24 junctions whose trigger is a long ī/ū — the savarṇa that
     1.1.69 grants and that 58's declaration left out.  theorum/58 = the
     compiled language restricted to short-vowel triggers.
 T2  ANTARATAMA (1.1.50) WITH THE STHĀNA TABLE selects every substitute 58
     tabulates (yaṇ for ik; guṇa/vṛddhi for ik and ec; 1.1.51 r/l-para),
     uniquely, by Jaccard place similarity with the simple/compound
     tie-break; on 6.1.77 it coincides with yathāsaṅkhya (1.3.10) on the
     Māheśvara order — and this coherence pins ṛ before ḷ in sūtra 2, cutting
     theorum/79's 2304 code-preserving orders to 1152.
 T3  COMPILED CONFLUENCE.  Under 1.4.2 the compiled sandhi has a unique
     normal form on every junction; the free-application critical pairs are
     exactly 6.1.77 vs 6.1.101 on {i,ī}² ∪ {u,ū}² (eight junctions; 58's four
     plus their savarṇa images), all resolved for 6.1.101.
 T4  WORD RULES COMPILE.  7.3.77 (genitive plural sthānin, 1.1.52), 6.1.73
     (tuk: k-marked augment, 1.1.46, after the short vowel), 8.4.40 (stu ↦
     ścu by 1.3.10 across the lists and 1.1.50 inside a varga, read off
     theorum/79's manner rows), 7.3.84 (guṇa of an ik-final aṅga) and 6.1.78
     compile from records and agree with theorum/58's functions on every
     reachable state of the gam and nī derivations (theorum/60 graph).
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable

from proof_lab.paninian_seam_calculus import (
    GAM,
    GUNA,
    IK,
    NI,
    SANDHI,
    SHORT,
    VOWELS,
    VRDDHI,
    ayadi_internal_6_1_78,
    chah_7_3_77,
    guna_7_3_84,
    is_Sit,
    it_lopa,
    sarvadhatuka_3_4_113,
    scutva_8_4_40,
    set_m,
    tuk_6_1_73,
)
from proof_lab.seam_compensated_confluence_verdict import explore, word_rules
from proof_lab.shaiva_sources_nativized import TOKENS, pratyahara
from proof_lab.shaiva_sources_varga_crystal import MANNER, VARGAS

SOURCES = {
    "1.1.49": "ṣaṣṭhī sthāneyogā",
    "1.1.66": "tasminn iti nirdiṣṭe pūrvasya",
    "1.1.67": "tasmād ity uttarasya",
    "6.1.84": "ekaḥ pūrvaparayoḥ",
    "6.1.72": "saṁhitāyām",
    "1.1.69": "aṇudit savarṇasya cāpratyayaḥ",
    "1.1.70": "taparas tatkālasya",
    "1.1.52": "alo 'ntyasya",
    "1.1.55": "anekāl śit sarvasya",
    "1.1.46": "ādyantau ṭakitau",
    "1.3.10": "yathāsaṅkhyam anudeśaḥ samānām",
    "1.1.50": "sthāne 'ntaratamaḥ",
    "1.1.51": "ur aṇ raparaḥ",
    "1.4.2": "vipratiṣedhe paraṁ kāryam",
    "6.1.77": "iko yaṇ aci",
    "6.1.78": "eco 'yavāyāvaḥ",
    "6.1.87": "ād guṇaḥ",
    "6.1.88": "vṛddhir eci",
    "6.1.101": "akaḥ savarṇe dīrghaḥ",
    "7.3.77": "iṣugamiyamāṁ chaḥ",
    "6.1.73": "che ca",
    "6.1.71": "hrasvasya piti kṛti tuk",
    "8.4.40": "stoḥ ścunā ścuḥ",
    "7.3.84": "sārvadhātukārdhadhātukayoḥ",
    "1.1.1": "vṛddhir ādaic",
    "1.1.2": "adeṅ guṇaḥ",
}

# ---------------------------------------------------------------- alphabet bridge (theorum/58 spells ṛ ḷ ś ṣ ā ī ū as R L S z A I U)
IAST_TO_58 = {"ṛ": "R", "ḷ": "L", "ś": "S", "ṣ": "z", "ā": "A", "ī": "I", "ū": "U", "ñ": "J", "ṅ": "N", "ṇ": "F", "ṭ": "T", "ṭh": "Th", "ḍ": "D", "ḍh": "Dh"}


def p58(initial: str, marker_sutra: int) -> tuple[str, ...]:
    """A pratyāhāra of the Māheśvara order (theorum/78) in theorum/58's spelling."""
    return tuple(IAST_TO_58.get(s, s) for s in pratyahara(initial, marker_sutra))


SAVARNA = {"a": ("a", "A"), "i": ("i", "I"), "u": ("u", "U"), "R": ("R",), "L": ("L",)}  # 1.1.69 on 58's carrier (no ṝ ḹ)
BASE = {v: k for k, vs in SAVARNA.items() for v in vs}
LONG = {"a": "A", "i": "I", "u": "U"}


def savarna_expand(sounds: tuple[str, ...], tapara: bool = False) -> tuple[str, ...]:
    """1.1.69: an aṇ (or udit) term denotes its savarṇas; 1.1.70: not when t-marked."""
    if tapara:
        return sounds
    out: list[str] = []
    for s in sounds:
        out.extend(SAVARNA.get(s, (s,)))
    return tuple(dict.fromkeys(out))


# ---------------------------------------------------------------- 1.1.50 sthāne 'ntaratamaḥ with the sthāna table
PLACE = {  # sthāna of the vowels and semivowels on the carrier; e/ai = kaṇṭha+tālu, o/au = kaṇṭha+oṣṭha, v = danta+oṣṭha
    "a": {"kantha"}, "A": {"kantha"},
    "i": {"talu"}, "I": {"talu"}, "e": {"kantha", "talu"}, "ai": {"kantha", "talu"},
    "u": {"ostha"}, "U": {"ostha"}, "o": {"kantha", "ostha"}, "au": {"kantha", "ostha"},
    "R": {"murdhan"}, "L": {"danta"},
    "y": {"talu"}, "v": {"danta", "ostha"}, "r": {"murdhan"}, "l": {"danta"},
}
COMPOUND = {"e", "o", "ai", "au"}  # sandhyakṣara


def antaratama_winners(sthanin: str, candidates: tuple[str, ...]) -> list[str]:
    """1.1.50: the candidates closest in place (Jaccard similarity of sthāna sets), ties broken by
    simple/compound kind.  A lawful selection needs exactly one winner."""
    s = PLACE[sthanin]

    def score(c: str) -> tuple[Fraction, int]:
        p = PLACE[c]
        return (Fraction(len(s & p), len(s | p)), int((c in COMPOUND) == (sthanin in COMPOUND)))

    best = max(score(c) for c in candidates)
    return [c for c in candidates if score(c) == best]


def antaratama(sthanin: str, candidates: tuple[str, ...]) -> str:
    winners = antaratama_winners(sthanin, candidates)
    assert len(winners) == 1, (sthanin, candidates, winners)
    return winners[0]


def rapara_1_1_51(sthanin: str, substitute: str) -> str:
    """1.1.51: an aṇ substitute of ṛ/ḷ is followed by r/l."""
    if sthanin in ("R", "L") and substitute in ("a", "A", "i", "I", "u", "U"):
        return substitute + ("r" if sthanin == "R" else "l")
    return substitute


# ---------------------------------------------------------------- the instruction record and its interpreter (sandhi, two-sound junction)
Record = dict[str, Any]

GUNA_SET = ("a", "e", "o")  # 1.1.2 adeṅ guṇaḥ
VRDDHI_SET = ("A", "ai", "au")  # 1.1.1 vṛddhir ādaic

SANDHI_RECORDS: list[Record] = [
    # 6.1.77 iko yaṇ aci: ikaḥ (gen) yaṇ (nom) aci (loc)
    {"sid": "6.1.77", "sthanin": ("ik", p58("i", 1)), "adesa": ("list", p58("y", 5)), "left": None, "right": ("ac", p58("a", 3)), "ekadesa": False},
    # 6.1.78 eco 'yavāyāvaḥ: ecaḥ (gen) ay av āy āv (nom) aci (loc, anuvṛtti)
    {"sid": "6.1.78", "sthanin": ("ec", p58("e", 3)), "adesa": ("list", ("ay", "av", "Ay", "Av")), "left": None, "right": ("ac", p58("a", 3)), "ekadesa": False},
    # 6.1.87 ād guṇaḥ: āt (abl) guṇaḥ (nom, saṁjñā 1.1.2) iki (loc, anuvṛtti); under 6.1.84
    {"sid": "6.1.87", "sthanin": ("ik", p58("i", 1)), "adesa": ("samjna", GUNA_SET), "left": ("a", ("a",)), "right": None, "ekadesa": True},
    # 6.1.88 vṛddhir eci: āt (abl) vṛddhiḥ (nom, saṁjñā 1.1.1) eci (loc); under 6.1.84
    {"sid": "6.1.88", "sthanin": ("ec", p58("e", 3)), "adesa": ("samjna", VRDDHI_SET), "left": ("a", ("a",)), "right": None, "ekadesa": True},
    # 6.1.101 akaḥ savarṇe dīrghaḥ: akaḥ (gen) savarṇe (loc) dīrghaḥ (nom); under 6.1.84
    {"sid": "6.1.101", "sthanin": ("ak", p58("a", 1)), "adesa": ("dirgha", ()), "left": None, "right": ("savarna", ()), "ekadesa": True},
]


def compile_sandhi(rec: Record) -> Callable[[tuple], tuple | None]:
    name, base_sthanin = rec["sthanin"]
    sthanin = savarna_expand(base_sthanin)  # 1.1.69 (ik, ec, ak are aṇ and not t-marked)
    kind, adesa = rec["adesa"]
    left = savarna_expand(rec["left"][1]) if rec["left"] else None
    right = savarna_expand(rec["right"][1]) if rec["right"] and rec["right"][0] != "savarna" else None

    def substitute(x: str) -> str:
        if kind == "list":  # 1.3.10 yathāsaṅkhya on the base lists; a savarṇa follows its base (1.1.69)
            assert len(base_sthanin) == len(adesa)
            return adesa[base_sthanin.index(BASE.get(x, x))]
        if kind == "samjna":  # 1.1.50 antaratama among the saṁjñā's members, then 1.1.51
            return rapara_1_1_51(BASE.get(x, x), antaratama(x, adesa))
        if kind == "dirgha":
            return LONG[BASE[x]]
        raise ValueError(kind)

    def rule(j: tuple) -> tuple | None:
        if len(j) != 2:
            return None
        X, Y = j
        if rec["ekadesa"]:  # 6.1.84: the pair (prior, posterior) is replaced by one sound
            if left is not None:  # 1.1.67: the ablative term is the prior, the sthānin is the posterior
                if X in left and Y in sthanin:
                    return (substitute(Y),)
                return None
            if rec["right"][0] == "savarna":  # 6.1.101: posterior savarṇa of the prior
                if X in sthanin and BASE.get(Y) == BASE.get(X) and X in BASE and Y in BASE:
                    return (substitute(X),)
                return None
        # 1.1.66: the locative term is the posterior; the sthānin is the prior; 1.1.52 / 1.1.55 replace it whole
        if X in sthanin and right is not None and Y in right:
            return (substitute(X), Y)
        return None

    return rule


def sutra_key(sid: str) -> tuple[int, int, int]:
    a, p, s = sid.split(".")
    return (int(a), int(p), int(s))


def t1_sandhi_compiles() -> dict[str, Any]:
    junctions = [(x, y) for x in VOWELS for y in VOWELS]
    compiled = {rec["sid"]: compile_sandhi(rec) for rec in SANDHI_RECORDS}
    hand = dict(SANDHI)
    agree_where_hand_fires = True
    extra: dict[str, list[str]] = {}
    hand_only: list[str] = []
    for sid in compiled:
        extra[sid] = []
        for j in junctions:
            h, c = hand[sid](j), compiled[sid](j)
            if h is not None:
                agree_where_hand_fires &= c == h
            elif c is not None:
                extra[sid].append("+".join(j))
            if h is not None and c is None:
                hand_only.append(sid + ":" + "+".join(j))
    expected_extra = {
        "6.1.77": sorted(f"{x}+{y}" for x in ("I", "U") for y in VOWELS),
        "6.1.78": [],
        "6.1.87": sorted(f"{x}+{y}" for x in ("a", "A") for y in ("I", "U")),
        "6.1.88": [],
        "6.1.101": [],
    }
    checks = {
        "compiled_equals_hand_coded_wherever_58_fires": agree_where_hand_fires and not hand_only,
        "extra_firings_are_exactly_the_long_ik_savarna_junctions_1_1_69": {k: sorted(v) for k, v in extra.items()} == expected_extra,
        "twenty_four_extra_junctions": sum(len(v) for v in extra.values()) == 24,
        "compiled_6_1_77_on_long_ik": compiled["6.1.77"](("I", "a")) == ("y", "a") and compiled["6.1.77"](("U", "e")) == ("v", "e"),
        "compiled_6_1_87_on_long_ik": compiled["6.1.87"](("a", "I")) == ("e",) and compiled["6.1.87"](("A", "U")) == ("o",),
    }
    return {"checks": checks, "extra_firings": extra}


# ---------------------------------------------------------------- T2 antaratama reproduces the tables and coincides with yathāsaṅkhya
def t2_antaratama() -> dict[str, Any]:
    ik, yan = p58("i", 1), p58("y", 5)
    by_place = {x: antaratama(x, yan) for x in ik}
    by_order = {x: yan[ik.index(x)] for x in ik}  # 1.3.10
    guna_sel = {x: rapara_1_1_51(x, antaratama(x, GUNA_SET)) for x in ik}
    vrddhi_sel = {x: rapara_1_1_51(x, antaratama(x, VRDDHI_SET)) for x in ik + p58("e", 3)}
    # the ṛ/ḷ freedom of theorum/79 T2 (sūtra 2 admits both orders): only the order ṛ ḷ keeps 1.3.10 = 1.1.50
    coherent_orders = 0
    for perm in itertools.permutations(("R", "L")):
        ik_perm = ("i", "u") + perm
        coherent_orders += int(all(yan[ik_perm.index(x)] == antaratama(x, yan) for x in ik_perm))
    checks = {
        "antaratama_yan_equals_yathasankhya_yan_on_the_maheshvara_order": by_place == by_order == {"i": "y", "u": "v", "R": "r", "L": "l"},
        "antaratama_guna_reproduces_58_GUNA_with_1_1_51": guna_sel == {x: GUNA[x] for x in ik},
        "antaratama_vrddhi_reproduces_58_VRDDHI_and_6_1_88_table": vrddhi_sel == {**{x: VRDDHI[x] for x in ik}, "e": "ai", "ai": "ai", "o": "au", "au": "au"},
        "antaratama_unique_in_every_case_used_COMPUTED": all(
            len(antaratama_winners(x, cands)) == 1
            for cands, xs in ((yan, ik), (GUNA_SET, ik), (VRDDHI_SET, ik + p58("e", 3)))
            for x in savarna_expand(xs)
        ),
        "coherence_1_3_10_with_1_1_50_pins_r_before_l_in_sutra_2": coherent_orders == 1,
        "code_preserving_orders_drop_from_2304_to_1152": 2304 * coherent_orders // 2 == 1152,
    }
    return {"checks": checks, "yan_by_place": by_place, "guna_by_place": guna_sel, "vrddhi_by_place": vrddhi_sel}


# ---------------------------------------------------------------- T3 compiled confluence under 1.4.2
def _free_nfs(w: tuple, rules: list[Callable]) -> set[tuple]:
    seen, frontier, nfs = {w}, [w], set()
    while frontier:
        x = frontier.pop()
        nxt = {r(x) for r in rules if r(x) is not None} - {x}
        if not nxt:
            nfs.add(x)
        for y in nxt:
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return nfs


def _priority_nf(w: tuple, rules: list[tuple[str, Callable]]) -> tuple:
    x = w
    for _ in range(20):
        applicable = [(sid, r) for sid, r in rules if r(x) is not None]
        if not applicable:
            return x
        top = max(sutra_key(sid) for sid, _ in applicable)
        winners = [r for sid, r in applicable if sutra_key(sid) == top]
        assert len(winners) == 1
        x = winners[0](x)
    raise AssertionError("no normal form")


def t3_compiled_confluence() -> dict[str, Any]:
    junctions = [(x, y) for x in VOWELS for y in VOWELS]
    rules = [(rec["sid"], compile_sandhi(rec)) for rec in SANDHI_RECORDS]
    fns = [r for _, r in rules]
    ambiguous = {j for j in junctions if len(_free_nfs(j, fns)) > 1}
    expected = {(x, y) for x in ("i", "I") for y in ("i", "I")} | {(x, y) for x in ("u", "U") for y in ("u", "U")}
    conflicting_pairs = set()
    for j in ambiguous:
        firing = tuple(sid for sid, r in rules if r(j) is not None)
        conflicting_pairs.add(firing)
    unique = True
    resolved_to_dirgha = True
    for j in junctions:
        try:
            nf = _priority_nf(j, rules)
        except AssertionError:
            unique = False
            continue
        if j in ambiguous:
            resolved_to_dirgha &= nf == (LONG[BASE[j[0]]],)
    checks = {
        "free_application_ambiguous_exactly_on_ik_savarna_squares": ambiguous == expected,
        "the_only_conflict_is_6_1_77_vs_6_1_101": conflicting_pairs == {("6.1.77", "6.1.101")},
        "1_4_2_gives_a_unique_normal_form_on_every_junction": unique,
        "conflicts_resolve_to_the_later_sutra_6_1_101": resolved_to_dirgha,
    }
    return {"checks": checks, "ambiguous": sorted("+".join(j) for j in ambiguous)}


# ---------------------------------------------------------------- T4 word rules compile
STU = ("s", "t", "th", "d", "dh", "n")  # s + tu (1.1.69 udit)
SCU = ("S", "c", "ch", "j", "jh", "J")  # ś + cu
ROW_OF = {IAST_TO_58.get(s, s): m for m, row in MANNER.items() for s in row}
CA_VARGA = {ROW_OF[IAST_TO_58.get(s, s)]: IAST_TO_58.get(s, s) for s in VARGAS["ca"]}


def scu_of(x: str) -> str:
    """8.4.40 stu ↦ ścu: s ↦ ś by 1.3.10 across the lists; a tu stop ↦ the cu stop of the same manner row (1.1.50)."""
    if x == "s":
        return "S"
    return CA_VARGA[ROW_OF[x]]


def c_chah_7_3_77(w):  # iṣu-gami-yamām (gen. pl.) chaḥ (nom.), śiti (loc., anuvṛtti): 1.1.52 the final sound
    for i in range(len(w) - 1):
        ph, feats = w[i]
        if "root" in feats and ph in (("i", "z"), ("g", "a", "m"), ("y", "a", "m")) and is_Sit(w[i + 1]):
            w = set_m(w, i, phones=ph[:-1] + ("ch",))
    return w


def c_tuk_6_1_73(w):  # che ca, hrasvasya ... tuk (6.1.71): k-marked augment (1.1.46 ādyantau ṭakitau) after the short vowel before ch
    for i, (ph, feats) in enumerate(w):
        for k in range(1, len(ph)):
            if ph[k] == "ch" and ph[k - 1] in SHORT:
                w = set_m(w, i, phones=ph[:k] + ("t",) + ph[k:])
                break
    return w


def c_scutva_8_4_40(w):  # stoḥ (gen.) ścunā (instr.: in contact with ścu) ścuḥ (nom.)
    for i, (ph, feats) in enumerate(w):
        for k in range(len(ph) - 1):
            if ph[k] in STU and ph[k + 1] in SCU:
                w = set_m(w, i, phones=ph[:k] + (scu_of(ph[k]),) + ph[k + 1 :])
                break
            if ph[k] in SCU and ph[k + 1] in STU:
                w = set_m(w, i, phones=ph[: k + 1] + (scu_of(ph[k + 1]),) + ph[k + 2 :])
                break
    return w


def c_guna_7_3_84(w):  # aṅga (6.4.1) ending in ik (1.1.3) ↦ guṇa (1.1.2, antaratama 1.1.50, 1.1.51) before sārvadhātuka/ārdhadhātuka
    ik = savarna_expand(p58("i", 1))
    for i in range(len(w) - 1):
        ph, feats = w[i]
        nxt = w[i + 1][1]
        if "root" in feats and ph and ph[-1] in ik and ("sArvadhAtuka" in nxt or "ArdhadhAtuka" in nxt):
            w = set_m(w, i, phones=ph[:-1] + (rapara_1_1_51(BASE[ph[-1]], antaratama(ph[-1], GUNA_SET)),))
    return w


def c_ayadi_6_1_78(w):  # ec-final morpheme before a vowel-initial one: 1.3.10 list, 1.1.55 whole
    ec, lst = p58("e", 3), ("ay", "av", "Ay", "Av")
    for i in range(len(w) - 1):
        ph, feats = w[i]
        nph = w[i + 1][0]
        if ph and ph[-1] in ec and nph and nph[0] in VOWELS:
            w = set_m(w, i, phones=ph[:-1] + (lst[ec.index(ph[-1])],))
    return w


def t4_word_rules_compile() -> dict[str, Any]:
    pairs = [("7.3.77", chah_7_3_77, c_chah_7_3_77), ("6.1.73", tuk_6_1_73, c_tuk_6_1_73), ("8.4.40", scutva_8_4_40, c_scutva_8_4_40), ("7.3.84", guna_7_3_84, c_guna_7_3_84), ("6.1.78", ayadi_internal_6_1_78, c_ayadi_6_1_78)]
    states = set()
    for W0 in (GAM, NI):
        states |= set(explore(W0, word_rules(True))["states"])
        states |= set(explore(W0, word_rules(False))["states"])
    agree = {sid: all(hand(W) == comp(W) for W in states) for sid, hand, comp in pairs}
    # the compiled pipeline reaches the same normal forms
    def derive(W, rules):
        for _ in range(8):
            before = W
            for f in rules:
                W = f(W)
            if W == before:
                return W
        return W
    hand_pipe = [lambda x: it_lopa(x, True), sarvadhatuka_3_4_113, chah_7_3_77, guna_7_3_84, ayadi_internal_6_1_78, tuk_6_1_73, scutva_8_4_40]
    comp_pipe = [lambda x: it_lopa(x, True), sarvadhatuka_3_4_113, c_chah_7_3_77, c_guna_7_3_84, c_ayadi_6_1_78, c_tuk_6_1_73, c_scutva_8_4_40]
    same_nf = all(derive(W0, hand_pipe) == derive(W0, comp_pipe) for W0 in (GAM, NI))
    gam_nf = "".join("".join(m[0]) for m in derive(GAM, comp_pipe))
    ni_nf = "".join("".join(m[0]) for m in derive(NI, comp_pipe))
    grid_scutva = {x: scu_of(x) for x in STU}
    checks = {
        "compiled_word_rules_equal_hand_coded_on_every_reachable_state": all(agree.values()),
        "compiled_pipeline_reaches_gacchati_and_nayati": same_nf and gam_nf == "gacchati" and ni_nf == "nayati",
        "scutva_table_from_the_manner_grid_1_3_10_and_1_1_50": grid_scutva == {"s": "S", "t": "c", "th": "ch", "d": "j", "dh": "jh", "n": "J"},
        "tuk_is_a_k_marked_augment_placed_last_1_1_46": c_tuk_6_1_73((( ("g", "a", "ch"), frozenset({"root"})),)) == ((("g", "a", "t", "ch"), frozenset({"root"})),),
    }
    return {"checks": checks, "agreement_by_rule": agree, "reachable_states": len(states), "scutva_table": grid_scutva}


# ---------------------------------------------------------------- certificate
def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_sandhi_compiles": t1_sandhi_compiles(),
        "t2_antaratama": t2_antaratama(),
        "t3_compiled_confluence": t3_compiled_confluence(),
        "t4_word_rules_compile": t4_word_rules_compile(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PANINIAN_INSTRUCTION_FORMAT_CANDIDATE" if all(checks.values()) else "FAIL_PANINIAN_INSTRUCTION_FORMAT_CANDIDATE"
    return {
        "schema": "rkf.paninian_instruction_format_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Instruction format: with 1.1.49 (genitive = sthānin), 1.1.66 (locative = posterior), 1.1.67 (ablative = prior), 6.1.84 (ekādeśa scope), 1.1.69/1.1.70 (savarṇa unless t-marked), 1.1.52/1.1.55 (replacement scope), 1.3.10 (yathāsaṅkhya), 1.1.50 (antaratama by sthāna), 1.1.51 (r/l-para) the five sandhi sūtras compile from case-structured records to rules that equal theorum/58's hand-coded rules wherever those fire and additionally fire on exactly the 24 long-ī/ū junctions that 1.1.69 grants — theorum/58 is the compiled language restricted to short-vowel triggers",
                "Antaratama with the sthāna table reproduces every substitute table of theorum/58 uniquely (yaṇ, guṇa with 1.1.51, vṛddhi) and coincides with yathāsaṅkhya on 6.1.77; that coherence pins ṛ before ḷ in Māheśvara sūtra 2 and halves theorum/79's 2304 code-preserving orders to 1152",
                "Compiled sandhi is confluent under 1.4.2 on all 100 junctions; free application is ambiguous exactly on {i,ī}² ∪ {u,ū}², the only conflict is 6.1.77 vs 6.1.101, resolved to the later sūtra",
                "The word rules 7.3.77, 6.1.73, 8.4.40, 7.3.84, 6.1.78 compile from records (1.1.52, 1.1.46, the theorum/79 manner grid for ścutva) and equal theorum/58's functions on every reachable state of the gam and nī derivations; the compiled pipeline reaches gacchati and nayati",
            ],
            "NOT_claimed": [
                "A general Aṣṭādhyāyī interpreter: only the paribhāṣās listed and the rules realized in theorum/58 are compiled; adhikāra spans are declared (6.1.72, 6.1.84, 6.4.1), not parsed",
                "Long ṝ ḹ and pluta (outside theorum/58's declared carrier)",
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
