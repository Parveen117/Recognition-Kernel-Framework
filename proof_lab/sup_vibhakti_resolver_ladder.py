from __future__ import annotations

"""Exact certificate (theorum/63): SUP-VIBHAKTI CARRIER + RESOLVER LADDER.

Extends theorum/58 with the two pieces a grammar needs before any śloka can
be derived: (a) the nominal sector (4.1.2 sup, 1.4.14 padam) on the a-stem
paradigm of rāma, all 21 forms from canonical sūtras, checked against a
declared SOUNDNESS ORACLE (the standard paradigm); (b) the resolver ladder
of the paribhāṣā  pūrva-para-nitya-antaraṅga-apavādānām uttarottaraṃ balīyaḥ
together with 8.2.1 pūrvatrāsiddham, each resolver made EXECUTABLE on the
carrier:
    apavāda   A is apavāda of B  iff  dom(A) ⊊ dom(B)  (applicability sets
              computed on the reachable carrier -- "specific over general")
    nitya     A is nitya wrt B  iff  A applies both before and after B
              (kṛtākṛtaprasaṅgitva) while B does not survive A
    para      1.4.2, later sūtra wins
    8.2.1     tripādī rules (8.2–8.4) are asiddha to earlier rules: an
              applicable non-tripādī rule acts first
    antaraṅga NOT modelled (declared)
Ladder: 8.2.1 > apavāda > nitya > para.  Which rungs are LOAD-BEARING on
this carrier is computed, not assumed.

Transliteration: A=ā I=ī U=ū R=ṛ S=ś z=ṣ N=ṇ H=visarga; affix given in
upadeśa form with it-markers (1.3.2/1.3.3/1.3.7/1.3.8, 1.3.9 lopa).

Facts certified:
 T1  All 21 forms of rāma derived under the ladder match the oracle
     (soundness on this paradigm); every path passes through 1.3.9.
 T2  Memory channel load-bearing in the nominal sector: erasing it-marker
     memory breaks the ṅit-conditioned forms (7.1.12 / 7.1.13) -- counted.
 T3  Resolver census: for every critical pair on the carrier, which rung
     decides it; apavāda pairs are exhibited as domain-containment facts
     (e.g. 6.1.107 ami pūrvaḥ ⊊ 6.1.101 savarṇadīrgha); whether para alone
     would have sufficed is reported as DATA.  BUILD NOTE: the draft guessed
     "para agrees on this carrier" -- the census refused it: 8.2.1 is
     load-bearing at 8 states (tripādī rules would win by number) and
     apavāda at 7 (7.3.104 osi ca ⊊ 6.1.88, 7.1.12 ⊊ 6.1.101, ...).  The
     nitya rung is never reached on this paradigm.  A PLANTED apavāda placed
     EARLIER than its utsarga additionally shows the rung overriding para.
 T4  8.2.1 certified: 8.2.66 ruḥ / 8.3.15 visarga / 8.4.2 ṇatva never act
     before any sapādasaptādhyāyī rule on any derivation path.
 T5  Confluence verdict (theorum/60 engine) on the nominal carrier under the
     ladder: unique normal form for all 21 inputs.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab.paninian_seam_calculus import sutra_key

VOW = ("a", "A", "i", "I", "u", "U", "R", "e", "o", "ai", "au")
JHAL = set("kgcjtdpbSzsh")  # stops + sibilants (bh, dh represented as 'b','d' + 'h'? we use single tokens below)
YAN = set("yvrl")

# state: (stem tuple, affix tuple, features frozenset, done flag)
State = tuple[tuple[str, ...], tuple[str, ...], frozenset[str]]


def st(stem, affix, feats=()) -> State:
    return (tuple(stem), tuple(affix), frozenset(feats))


def surface(W: State) -> str:
    return "".join(W[0]) + "".join(W[1])


# ---------------------------------------------------------------- it-marker lopa for sup affixes
IT_INITIAL = {"S", "j", "G", "T"}  # 1.3.8 laśakv (ś, j), 1.3.7 cuṭū (ṭ-initial ṭā, ṭakitau) ; G = ṅ (1.3.8 ṅ? ṅe/ṅasi/ṅas: ṅ is it by 1.3.8)
def it_lopa(W: State, carry: bool = True) -> State | None:
    stem, aff, f = W
    if "lopa_done" in f or not aff:
        return None
    feats = set(f)
    a = list(aff)
    # initial it (ṭ of ṭā/auṭ: 1.3.7; ś of śas, j of jas, ṅ of ṅe/ṅasi/ṅas: 1.3.8)
    if a and a[0] in ("T", "S", "j", "G"):
        if carry:
            feats.add({"T": "Tit", "S": "Sit", "j": "jit", "G": "Git"}[a[0]])
        a = a[1:]
    # final it: u of su (1.3.2 anunāsika it), ṭ of auṭ (1.3.3 hal antyam)
    if a and a[-1] == "T":
        if carry:
            feats.add("Tit")
        a = a[:-1]
    if a and a[-1] == "u" and "su" in feats:
        if carry:
            feats.add("uit")
        a = a[:-1]
    feats.add("lopa_done")
    return (stem, tuple(a), frozenset(feats))


# ---------------------------------------------------------------- sūtras (nominal sector)
def r_7_1_9(W):  # ato bhisa ais
    stem, aff, f = W
    if stem and stem[-1] == "a" and aff == ("b", "h", "i", "s") and "ais_done" not in f:
        return (stem, ("ai", "s"), f | {"ais_done"})
    return None


def r_7_1_12(W):  # ṭāṅasiṅasām inātsyāḥ
    stem, aff, f = W
    if stem and stem[-1] == "a" and "lopa_done" in f and "ina_done" not in f:
        if "Tit" in f and aff == ("A",):
            return (stem, ("i", "n", "a"), f | {"ina_done"})
        if "Git" in f and aff == ("a", "s") and "Gasi" in f:
            return (stem, ("A", "t"), f | {"ina_done"})
        if "Git" in f and aff == ("a", "s") and "Gas" in f:
            return (stem, ("s", "y", "a"), f | {"ina_done"})
    return None


def r_7_1_13(W):  # ṅer yaḥ
    stem, aff, f = W
    if stem and stem[-1] == "a" and "Git" in f and aff == ("e",) and "lopa_done" in f and "ya_done" not in f:
        return (stem, ("y", "a"), f | {"ya_done"})
    return None


def r_7_1_54(W):  # hrasvanadyāpo nuṭ
    stem, aff, f = W
    if stem and stem[-1] == "a" and aff == ("A", "m") and "Am" in f and "nuT_done" not in f:
        return (stem, ("n", "A", "m"), f | {"nuT_done"})
    return None


def r_6_4_3(W):  # nāmi : aṅga-final a -> ā before nām
    stem, aff, f = W
    if stem and stem[-1] == "a" and aff[:1] == ("n",) and "nuT_done" in f:
        return (stem[:-1] + ("A",), aff, f)
    return None


def r_7_3_102(W):  # supi ca : a -> ā before yañ-initial sup
    stem, aff, f = W
    if stem and stem[-1] == "a" and aff and aff[0] in ("y", "b") and "sup" in f and "lopa_done" in f:
        return (stem[:-1] + ("A",), aff, f)
    return None


def r_7_3_103(W):  # bahuvacane jhaly et
    stem, aff, f = W
    if stem and stem[-1] == "a" and "bahu" in f and aff and aff[0] in ("b", "s") and "lopa_done" in f:
        return (stem[:-1] + ("e",), aff, f)
    return None


def r_7_3_104(W):  # osi ca
    stem, aff, f = W
    if stem and stem[-1] == "a" and aff == ("o", "s") and "lopa_done" in f:
        return (stem[:-1] + ("e",), aff, f)
    return None


def r_6_1_69(W):  # eṅhrasvāt sambuddheḥ : vocative su elided
    stem, aff, f = W
    if "samb" in f and aff == ("s",) and "lopa_done" in f:
        return (stem, (), f | {"samb_lopa"})
    return None


# sandhi across the stem|affix seam (operate on last stem phone + first affix phone)
def r_6_1_87(W):  # ād guṇaḥ
    stem, aff, f = W
    if stem and stem[-1] in ("a", "A") and aff and aff[0] in ("i", "u", "R") and "lopa_done" in f:
        return (stem[:-1] + ({"i": "e", "u": "o", "R": "ar"}[aff[0]],), aff[1:], f)
    return None


def r_6_1_88(W):  # vṛddhir eci
    stem, aff, f = W
    if stem and stem[-1] in ("a", "A") and aff and aff[0] in ("e", "o", "ai", "au") and "lopa_done" in f:
        return (stem[:-1] + ({"e": "ai", "ai": "ai", "o": "au", "au": "au"}[aff[0]],), aff[1:], f)
    return None


def r_6_1_101(W):  # akaḥ savarṇe dīrghaḥ
    stem, aff, f = W
    if stem and aff and "lopa_done" in f and (stem[-1], aff[0]) in {("a", "a"), ("a", "A"), ("A", "a"), ("A", "A")}:
        return (stem[:-1] + ("A",), aff[1:], f)
    return None


def r_6_1_102(W):  # prathamayoḥ pūrvasavarṇaḥ (a + as of jas/śas -> ās)
    stem, aff, f = W
    if stem and stem[-1] == "a" and aff == ("a", "s") and "lopa_done" in f and ("jit" in f or "Sit" in f):
        return (stem[:-1] + ("A",), ("s",), f | {"pss_done"})
    return None


def r_6_1_103(W):  # tasmāc chaso naḥ puṃsi
    stem, aff, f = W
    if "Sit" in f and "pss_done" in f and aff == ("s",):
        return (stem, ("n",), f)
    return None


def r_6_1_107(W):  # ami pūrvaḥ
    stem, aff, f = W
    if stem and stem[-1] == "a" and aff == ("a", "m") and "am" in f and "lopa_done" in f:
        return (stem, ("m",), f)
    return None


def r_6_1_78(W):  # eco'yavāyāvaḥ at the seam
    stem, aff, f = W
    if stem and stem[-1] in ("e", "o", "ai", "au") and aff and aff[0] in VOW and "lopa_done" in f:
        return (stem[:-1] + ({"e": "ay", "o": "av", "ai": "Ay", "au": "Av"}[stem[-1]],), aff, f)
    return None


# tripādī
def r_8_2_66(W):  # sasajuṣo ruḥ : pada-final s -> r(u)
    stem, aff, f = W
    if aff and aff[-1] == "s" and "lopa_done" in f and "ru_done" not in f and aff not in (("a", "s"), ("b", "h", "i", "s"), ("s", "u")):
        return (stem, aff[:-1] + ("r",), f | {"ru_done"})
    return None


def r_8_3_15(W):  # kharavasānayor visarjanīyaḥ : r -> ḥ at pause
    stem, aff, f = W
    if "ru_done" in f and aff and aff[-1] == "r":
        return (stem, aff[:-1] + ("H",), f)
    return None


def r_8_3_59(W):  # ādeśapratyayayoḥ : s -> ṣ after iṇ (e/i) in sup
    stem, aff, f = W
    if stem and stem[-1] in ("e", "i", "I", "u", "U") and aff[:1] == ("s",) and "sup" in f and "bahu" in f and "lopa_done" in f:
        return (stem, ("z",) + aff[1:], f)
    return None


def r_8_4_2(W):  # aṭkupvāṅnumvyavāye'pi : n -> ṇ after r across aṭ/ku/pu ; 8.4.37 padāntasya blocks pada-final n
    stem, aff, f = W
    full = list(stem + aff)
    if "r" in full:
        ri = full.index("r")
        for k in range(ri + 1, len(full)):
            if full[k] == "n" and k != len(full) - 1 and all(x in VOW or x in ("y", "v", "h", "k", "g", "p", "b", "m", "ay", "Ay", "av", "Av", "ar") for x in full[ri + 1 : k]):
                full[k] = "N"
                ns = len(stem)
                return (tuple(full[:ns]), tuple(full[ns:]), f)
    return None


RULES: list[tuple[str, Callable]] = [
    ("1.3.9", it_lopa),
    ("6.1.69", r_6_1_69),
    ("6.1.78", r_6_1_78),
    ("6.1.87", r_6_1_87),
    ("6.1.88", r_6_1_88),
    ("6.1.101", r_6_1_101),
    ("6.1.102", r_6_1_102),
    ("6.1.103", r_6_1_103),
    ("6.1.107", r_6_1_107),
    ("6.4.3", r_6_4_3),
    ("7.1.9", r_7_1_9),
    ("7.1.12", r_7_1_12),
    ("7.1.13", r_7_1_13),
    ("7.1.54", r_7_1_54),
    ("7.3.102", r_7_3_102),
    ("7.3.103", r_7_3_103),
    ("7.3.104", r_7_3_104),
    ("8.2.66", r_8_2_66),
    ("8.3.15", r_8_3_15),
    ("8.3.59", r_8_3_59),
    ("8.4.2", r_8_4_2),
]

# 4.1.2 svaujasamauṭchaṣṭābhyāmbhisṅebhyāmbhyasṅasibhyāmbhyasṅasosāmṅyossup (upadeśa forms + features)
SUP = [
    ("1s", ("s", "u"), {"su"}), ("1d", ("au", "T"), set()), ("1p", ("j", "a", "s"), {"bahu"}),
    ("2s", ("a", "m"), {"am"}), ("2d", ("au", "T"), set()), ("2p", ("S", "a", "s"), {"bahu"}),
    ("3s", ("T", "A"), set()), ("3d", ("b", "h", "y", "A", "m"), set()), ("3p", ("b", "h", "i", "s"), {"bahu"}),
    ("4s", ("G", "e"), set()), ("4d", ("b", "h", "y", "A", "m"), set()), ("4p", ("b", "h", "y", "a", "s"), {"bahu"}),
    ("5s", ("G", "a", "s"), {"Gasi"}), ("5d", ("b", "h", "y", "A", "m"), set()), ("5p", ("b", "h", "y", "a", "s"), {"bahu"}),
    ("6s", ("G", "a", "s"), {"Gas"}), ("6d", ("o", "s"), set()), ("6p", ("A", "m"), {"Am", "bahu"}),
    ("7s", ("G", "i"), set()), ("7d", ("o", "s"), set()), ("7p", ("s", "u", "p"), {"bahu", "sup7"}),
    ("8s", ("s", "u"), {"su", "samb"}),
]
ORACLE = {
    "1s": "rAmaH", "1d": "rAmau", "1p": "rAmAH", "2s": "rAmam", "2d": "rAmau", "2p": "rAmAn",
    "3s": "rAmeNa", "3d": "rAmAbhyAm", "3p": "rAmaiH", "4s": "rAmAya", "4d": "rAmAbhyAm", "4p": "rAmebhyaH",
    "5s": "rAmAt", "5d": "rAmAbhyAm", "5p": "rAmebhyaH", "6s": "rAmasya", "6d": "rAmayoH", "6p": "rAmANAm",
    "7s": "rAme", "7d": "rAmayoH", "7p": "rAmezu", "8s": "rAma",
}


def inputs():
    out = {}
    for code, aff, feats in SUP:
        aff = tuple(aff)
        fe = set(feats) | {"sup"}
        if code == "7p":
            aff = ("s", "u")  # p of sup is it (1.3.3) -> handled as declared: 'sup7'
        out[code] = st(("r", "A", "m", "a"), aff, fe)
    return out


# ---------------------------------------------------------------- engine
def applicable(W, rules, carry=True):
    out = []
    for sid, fn in rules:
        r = fn(W, carry) if sid == "1.3.9" else fn(W)
        if r is not None and r != W:
            out.append((sid, r))
    return out


def reachable(W0, rules, carry=True):
    seen, frontier = {W0}, [W0]
    while frontier:
        W = frontier.pop()
        for _, W2 in applicable(W, rules, carry):
            if W2 not in seen:
                seen.add(W2)
                frontier.append(W2)
    return seen


def is_tripadi(sid):
    a, p, _ = sutra_key(sid)
    return a == 8 and p >= 2


def resolve(W, app, dom, rules_by_id, carry=True):
    """Ladder: 8.2.1 > apavāda (domain containment) > nitya > para.  Returns (winner, rung)."""
    if len(app) == 1:
        return app[0], "single"
    non_tri = [x for x in app if not is_tripadi(x[0])]
    if non_tri and len(non_tri) < len(app):
        app = non_tri
        if len(app) == 1:
            return app[0], "8.2.1"
    # apavāda: A beats B if dom(A) ⊊ dom(B)
    winners = [x for x in app if all(x is y or dom[x[0]] < dom[y[0]] for y in app)]
    if len(winners) == 1:
        return winners[0], "apavāda"
    # nitya: A applies after B acted, B does not apply after A acted
    def nitya_over(A, B):
        a_after_b = any(s == A[0] for s, _ in applicable(B[1], [(A[0], rules_by_id[A[0]])], carry))
        b_after_a = any(s == B[0] for s, _ in applicable(A[1], [(B[0], rules_by_id[B[0]])], carry))
        return a_after_b and not b_after_a
    winners = [x for x in app if all(x is y or nitya_over(x, y) for y in app)]
    if len(winners) == 1:
        return winners[0], "nitya"
    top = max(sutra_key(x[0]) for x in app)
    winners = [x for x in app if sutra_key(x[0]) == top]
    assert len(winners) == 1, "tie"
    return winners[0], "para"


def paradigm_domains(rules, carry=True, carrier_inputs=None):
    """apavāda needs the PARADIGM carrier: domains over the union of reachable states of all inputs."""
    R = set()
    for W0 in (carrier_inputs or inputs()).values():
        R |= reachable(W0, rules, carry)
    return {sid: frozenset(W for W in R if any(s == sid for s, _ in applicable(W, [(sid, fn)], carry))) for sid, fn in rules}


def derive(W0, rules, carry=True, record=None, dom=None):
    rules_by_id = dict(rules)
    if dom is None:
        dom = paradigm_domains(rules, carry)
    W = W0
    path = []
    for _ in range(30):
        app = applicable(W, rules, carry)
        if not app:
            return W, path
        (sid, W2), rung = resolve(W, app, dom, rules_by_id, carry)
        if record is not None and len(app) > 1:
            record.append({"state": surface(W), "applicable": sorted(s for s, _ in app), "winner": sid, "rung": rung})
        path.append(sid)
        W = W2
    raise AssertionError("no normal form")


def build_certificate() -> dict[str, Any]:
    ins = inputs()
    forms, paths, census = {}, {}, []
    dom_all = paradigm_domains(RULES)
    for code, W0 in ins.items():
        W, p = derive(W0, RULES, record=census, dom=dom_all)
        forms[code] = surface(W)
        paths[code] = p
    sound = {c: forms[c] == ORACLE[c] for c in ORACLE}
    lopa_every = all("1.3.9" in p for p in paths.values())
    # T2 memory control
    forms_nomem = {}
    for code, W0 in ins.items():
        try:
            forms_nomem[code] = surface(derive(W0, RULES, carry=False, dom=paradigm_domains(RULES, carry=False))[0])
        except AssertionError:
            forms_nomem[code] = "NO_NF"
    broken = sorted(c for c in ORACLE if forms_nomem[c] != ORACLE[c])
    # T3 resolver census + para-sufficiency + planted apavāda
    rungs = sorted({c["rung"] for c in census})
    para_would_agree = all(c["winner"] == max(c["applicable"], key=sutra_key) for c in census)
    apavada_pairs = sorted({(c["winner"], o) for c in census if c["rung"] == "apavāda" for o in c["applicable"] if o != c["winner"]})
    # planted: rename 6.1.107 to "5.9.9" (earlier than 6.1.101) -> para would pick 6.1.101 (rāmām), apavāda still picks ami pūrvaḥ (rāmam)
    planted = [("5.9.9" if s == "6.1.107" else s, f) for s, f in RULES]
    W2s, _ = derive(ins["2s"], planted, dom=paradigm_domains(planted))
    W2s_para_only = None
    # para-only derivation of the planted system
    def derive_para(W0, rules):
        W = W0
        for _ in range(30):
            app = applicable(W, rules)
            if not app:
                return W
            non_tri = [x for x in app if not is_tripadi(x[0])] or app
            W = max(non_tri, key=lambda x: sutra_key(x[0]))[1]
        raise AssertionError
    W2s_para_only = surface(derive_para(ins["2s"], planted))
    # T4 8.2.1
    tri_first_ok = all(not (is_tripadi(r) and any(not is_tripadi(q) for q in p[i + 1 :])) for p in paths.values() for i, r in enumerate(p))
    # T5 uniqueness: derive is deterministic; check normal form is a free normal form
    free_nf_ok = True
    for code, W0 in ins.items():
        R = reachable(W0, RULES)
        nfs = {surface(W) for W in R if not applicable(W, RULES)}
        free_nf_ok &= forms[code] in nfs
    checks = {
        "T1_all_21_forms_match_oracle": all(sound.values()),
        "T1_every_path_passes_lopa_1_3_9": lopa_every,
        "T2_memory_erased_breaks_Git_Tit_conditioned_forms": len(broken) > 0 and all(c in broken for c in ("3s", "4s", "5s", "6s")),
        "T3_apavada_rung_exhibits_domain_containment_pairs": len(apavada_pairs) > 0,
        "T3_para_alone_DISAGREES_on_real_data_8_2_1_and_apavada_load_bearing": (not para_would_agree) and "8.2.1" in rungs and "apavāda" in rungs,
        "T3_planted_earlier_apavada_ladder_gives_rAmam_para_alone_gives_other": surface(W2s) == "rAmam" and W2s_para_only != "rAmam",
        "T4_8_2_1_tripadi_never_before_sapadasaptadhyayi_rule": tri_first_ok,
        "T5_ladder_normal_form_is_a_free_normal_form_all_21": free_nf_ok,
    }
    status = "PASS_SUP_VIBHAKTI_RESOLVER_LADDER_CANDIDATE" if all(checks.values()) else "FAIL_SUP_VIBHAKTI_RESOLVER_LADDER_CANDIDATE"
    return {
        "schema": "rkf.sup_vibhakti_resolver_ladder_candidate.v1",
        "status": status,
        "forms": forms,
        "oracle_mismatches": sorted(c for c, ok in sound.items() if not ok),
        "forms_without_memory": forms_nomem,
        "memory_broken_forms": broken,
        "resolver_census": census,
        "rungs_used": rungs,
        "para_alone_would_agree_on_this_carrier": para_would_agree,
        "apavada_pairs_domain_containment": apavada_pairs,
        "planted_apavada": {"ladder": surface(W2s), "para_only": W2s_para_only},
        "sutras_used": [s for s, _ in RULES] + ["4.1.2", "1.4.14", "1.3.2", "1.3.3", "1.3.7", "1.3.8"],
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "all 21 sup forms of rāma derived from canonical sūtras under the resolver ladder match the declared oracle (soundness on this paradigm)",
                "memory channel load-bearing in the nominal sector (ṅit/ṭit-conditioned 7.1.12/7.1.13 forms break without it)",
                "apavāda made executable as domain containment dom(A) ⊊ dom(B) on the carrier; pairs exhibited; planted earlier-apavāda shows the rung overriding para",
                "8.2.1 pūrvatrāsiddham on every derivation path",
                "ladder normal forms are free normal forms (no invented form)",
            ],
            "NOT_claimed": [
                "antaraṅga/bahiraṅga (not modelled); accent; other stem classes (ā-, i-, u-, consonant stems); neuter/feminine; dual/plural beyond this table",
                "completeness of the Aṣṭādhyāyī (21 + 6 sūtras used); soundness beyond the rāma paradigm",
                "antaraṅga rung (never reached here, not modelled); nitya rung never reached on this paradigm (present, untested by data)",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
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
        print(k, v)
    print("FORMS", payload["forms"])
    print("MISMATCH", payload["oracle_mismatches"], "RUNGS", payload["rungs_used"], "PARA_AGREES", payload["para_alone_would_agree_on_this_carrier"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
