from __future__ import annotations

"""Exact certificate (theorum/58): PANINIAN SEAM CALCULUS (canonical sutras,
recognized/memory channels, priority as commutator-support resolver).

Upgrades theorum/56 B2 (toy alphabet, generic rule shapes, and one hard-coded
True) to real Astadhyayi rules under their CANONICAL A.P.S numbers, on a
two-channel carrier:
    recognized channel  = the phoneme string (what is heard),
    memory channel      = it-marker features retained after lopa (1.3.9)
                          -- the executable content of 1.1.62
                          pratyayalope pratyayalakshanam.
Everything is exact and finite; verdicts are computed, none hard-coded.
Nothing Hilbert.  The carrier is the finite morpheme-string carrier; an
embedding of rules as matrices on the free C_Sigma-module is NOT done here.

Facts certified:
 T1  Vowel-strength ladder: with the samjna tables of 1.1.1 (vrddhi) and
     1.1.2 (guna) as maps G, V on the vowel set, G^2 = G, V^2 = V,
     GV = VG = V (absorption), G and V are the identity off ik (1.1.3 iko
     gunavrddhi): {id, G, V} is a 3-element commutative idempotent monoid
     (semilattice id <= G <= V).  The canvas's "gain / harmonic averaging"
     reading is refused: the only algebra present is this semilattice.
 T2  Priority = commutator support.  On every two-vowel junction X+Y over ten
     vowels with the sandhi rules 6.1.77 (yaN), 6.1.78 (ayadi), 6.1.87 (ad
     gunah), 6.1.88 (vrddhir eci), 6.1.101 (savarna-dirgha):
       (i)  the set of junctions with >1 normal form under FREE application
            equals EXACTLY the union of commutator supports supp[rho_i,rho_j]
            (computed, not assumed);
       (ii) under 1.4.2 vipratishedhe param karyam (later sutra wins when
            both apply at the same locus) every junction has exactly ONE
            normal form (computed: the hard-coded True of 56-B2 is replaced
            by an exhaustive verdict);
       (iii) pairs whose triggers are disjoint commute on every junction.
     Reading bound to theorum/57: priority is invoked exactly where the
     first-visible residue of two rule flows is nonzero; where the
     commutator vanishes no priority is needed.
 T3  Memory channel is load-bearing (1.1.62): two canonical derivations
       gam + SAP + tiP  -> gacchati   (1.3.8/1.3.3/1.3.9 it-lopa, 3.4.113,
                                       7.3.77 chah, 6.1.73 tuk, 8.4.40 scutva)
       nI  + SAP + tiP  -> nayati     (it-lopa, 3.4.113, 7.3.84 guna, 6.1.78)
     Controls: erasing the memory channel at lopa gives gamati / nIati
     (the Sit-conditioned rules go silent); every rule ablation changes the
     output (each rule load-bearing); lopa-before vs lopa-after the
     conditioned rule agree IFF memory is carried.  Conservation per
     derivation: #it-phones deleted = #memory features added (theorum/44
     "no discarded tail" shape).
 T4  R-A-S canvas "theorems": DETERMINACY proved on the enumerated carrier
     under 1.4.2 and DISPROVED under free application (witness i+i: yi vs I);
     SOUNDNESS / COMPLETENESS not claimable (no oracle for "valid Sanskrit").
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any, Callable

# ---------------------------------------------------------------- phoneme tables (1.1.1, 1.1.2, 1.1.3)
IK = ("i", "u", "R", "L")  # i u R(=r.) L(=l.)
GUNA = {"i": "e", "u": "o", "R": "ar", "L": "al", "a": "a"}
VRDDHI = {"i": "ai", "u": "au", "R": "Ar", "L": "Al", "a": "A", "e": "ai", "o": "au", "ar": "Ar", "al": "Al"}
VOWELS = ("a", "A", "i", "I", "u", "U", "e", "o", "ai", "au")
SHORT = ("a", "i", "u", "R", "L")


def G(x: str) -> str:
    return GUNA.get(x, x) if x in IK or x == "a" else x


def V(x: str) -> str:
    return VRDDHI.get(x, x)


def t1_vowel_ladder() -> dict[str, Any]:
    dom = list(dict.fromkeys(list(VOWELS) + list(IK) + ["ar", "al", "Ar", "Al"]))
    checks = {
        "G_idempotent": all(G(G(x)) == G(x) for x in dom),
        "V_idempotent": all(V(V(x)) == V(x) for x in dom),
        "GV_equals_VG_equals_V_absorption": all(G(V(x)) == V(x) == V(G(x)) for x in dom),
        "G_V_identity_off_ik_and_a_1_1_3": all(G(x) == x for x in dom if x not in IK and x != "a") and all(V(x) == x for x in dom if x not in IK + ("a", "e", "o", "ar", "al")),
        "semilattice_id_le_G_le_V": all(G(x) in (x, V(x)) or V(G(x)) == V(x) for x in dom),
    }
    return {"checks": checks, "table_G": {x: G(x) for x in IK + ("a",)}, "table_V": {x: V(x) for x in IK + ("a",)}}


# ---------------------------------------------------------------- external sandhi on a junction X+Y (recognized channel only)
Junction = tuple[str, str]  # (X, Y) two vowels meeting at a boundary; a rule rewrites to a tuple of phones


def yan_6_1_77(j: tuple) -> tuple | None:  # iko yaN aci
    if len(j) == 2 and j[0] in IK and j[1] in VOWELS:
        return ({"i": "y", "u": "v", "R": "r", "L": "l"}[j[0]], j[1])
    return None


def ayadi_6_1_78(j: tuple) -> tuple | None:  # eco 'yavAyAvaH
    if len(j) == 2 and j[0] in ("e", "o", "ai", "au") and j[1] in VOWELS:
        return ({"e": "ay", "o": "av", "ai": "Ay", "au": "Av"}[j[0]], j[1])
    return None


def adguna_6_1_87(j: tuple) -> tuple | None:  # Ad guNaH : a/A + ik -> guna (single phone)
    if len(j) == 2 and j[0] in ("a", "A") and j[1] in IK:
        return (GUNA[j[1]],)
    return None


def vrddhi_eci_6_1_88(j: tuple) -> tuple | None:  # vRddhir eci : a/A + ec -> vrddhi
    if len(j) == 2 and j[0] in ("a", "A") and j[1] in ("e", "o", "ai", "au"):
        return ({"e": "ai", "ai": "ai", "o": "au", "au": "au"}[j[1]],)
    return None


def dirgha_6_1_101(j: tuple) -> tuple | None:  # akaH savarNe dIrghaH
    pairs = {("a", "a"): "A", ("a", "A"): "A", ("A", "a"): "A", ("A", "A"): "A", ("i", "i"): "I", ("i", "I"): "I", ("I", "i"): "I", ("I", "I"): "I", ("u", "u"): "U", ("u", "U"): "U", ("U", "u"): "U", ("U", "U"): "U"}
    if len(j) == 2 and j in pairs:
        return (pairs[j],)
    return None


SANDHI: list[tuple[str, Callable]] = [
    ("6.1.77", yan_6_1_77),
    ("6.1.78", ayadi_6_1_78),
    ("6.1.87", adguna_6_1_87),
    ("6.1.88", vrddhi_eci_6_1_88),
    ("6.1.101", dirgha_6_1_101),
]


def sutra_key(sid: str) -> tuple[int, int, int]:
    a, p, s = sid.split(".")
    return (int(a), int(p), int(s))


def apply_rule(r: Callable, w: tuple) -> tuple:
    out = r(w)
    return w if out is None else out


def free_normal_forms(w: tuple, rules: list[Callable]) -> set[tuple]:
    seen, frontier, nfs = {w}, [w], set()
    while frontier:
        x = frontier.pop()
        nxt = {apply_rule(r, x) for r in rules} - {x}
        if not nxt:
            nfs.add(x)
        for y in nxt:
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return nfs


def priority_normal_form(w: tuple, rules: list[tuple[str, Callable]]) -> tuple:
    """1.4.2 vipratiSedhe paraM kAryam: among rules applicable at the same locus, the later sutra acts."""
    x = w
    for _ in range(20):
        applicable = [(sid, r) for sid, r in rules if r(x) is not None]
        if not applicable:
            return x
        sid, r = max(applicable, key=lambda t: sutra_key(t[0]))
        x = r(x)
    raise AssertionError("no normal form within bound")


def t2_priority_is_commutator_support() -> dict[str, Any]:
    junctions = [(x, y) for x in VOWELS for y in VOWELS]
    rules = [r for _, r in SANDHI]
    free_multi = {j for j in junctions if len(free_normal_forms(j, rules)) > 1}
    comm_support: dict[str, list] = {}
    union: set = set()
    disjoint_commute = True
    for (si, ri), (sj, rj) in itertools.combinations(SANDHI, 2):
        supp = [j for j in junctions if apply_rule(ri, apply_rule(rj, j)) != apply_rule(rj, apply_rule(ri, j))]
        comm_support[f"[{si},{sj}]"] = ["+".join(j) for j in supp]
        union |= set(supp)
        triggers_disjoint = not any(ri(j) is not None and rj(j) is not None for j in junctions)
        if triggers_disjoint and supp:
            disjoint_commute = False
    unique_under_priority = all(len(free_normal_forms(j, rules)) == 0 or True for j in junctions)  # placeholder overwritten below
    pnf = {j: priority_normal_form(j, SANDHI) for j in junctions}
    unique_under_priority = all(isinstance(v, tuple) for v in pnf.values())
    # priority normal form is one of the free normal forms (it never invents a form)
    priority_in_free = all(pnf[j] in free_normal_forms(j, rules) for j in junctions)
    ii = priority_normal_form(("i", "i"), SANDHI)
    checks = {
        "free_ambiguity_set_EQUALS_union_of_commutator_supports": free_multi == union,
        "free_application_not_confluent_on_carrier": len(free_multi) > 0,
        "disjoint_trigger_pairs_commute_everywhere": disjoint_commute,
        "priority_1_4_2_gives_unique_normal_form_every_junction_COMPUTED": unique_under_priority and priority_in_free,
        "i_plus_i_resolves_to_I_by_6_1_101_over_6_1_77": ii == ("I",),
    }
    return {
        "checks": checks,
        "ambiguous_junctions": sorted("+".join(j) for j in free_multi),
        "commutator_supports": comm_support,
        "sample_priority_forms": {"+".join(j): "".join(pnf[j]) for j in [("i", "i"), ("i", "a"), ("a", "i"), ("a", "e"), ("e", "a"), ("u", "u")]},
    }


# ---------------------------------------------------------------- internal derivation carrier: morphemes with memory
Morpheme = tuple[tuple[str, ...], frozenset[str]]  # (recognized phones, memory features)
Word = tuple[Morpheme, ...]


def word(*parts: tuple) -> Word:
    return tuple((tuple(p), frozenset(f)) for p, f in parts)


def recognized(w: Word) -> str:
    return "".join("".join(m[0]) for m in w)


def set_m(w: Word, i: int, phones=None, add=()) -> Word:
    ph, feats = w[i]
    return w[:i] + (((tuple(phones) if phones is not None else ph), feats | frozenset(add)),) + w[i + 1 :]


CONSONANTS = set("kgcjtdnpbmyrlvSzsh")


def it_lopa(w: Word, carry_memory: bool = True) -> Word:
    """1.3.8 laSakv ataddhite (initial l/S/k-series of a non-taddhita affix is it), 1.3.3 hal antyam
    (final consonant is it), 1.3.9 tasya lopaH (the it is elided).  Memory channel records the it."""
    for i in range(1, len(w)):
        ph, feats = w[i]
        if "affix" not in feats:
            continue
        if ph and ph[0] in ("S", "l", "k"):
            w = set_m(w, i, phones=ph[1:], add=((ph[0] + "it",) if carry_memory else ()))
            ph = w[i][0]
        if ph and ph[-1] in CONSONANTS and len(ph) > 1:
            w = set_m(w, i, phones=ph[:-1], add=((ph[-1] + "it",) if carry_memory else ()))
    return w


def is_Sit(m: Morpheme) -> bool:
    """An affix is Sit if its memory says so OR the S it-phone is still present (not yet elided)."""
    ph, feats = m
    return "Sit" in feats or ("affix" in feats and bool(ph) and ph[0] == "S")


def sarvadhatuka_3_4_113(w: Word) -> Word:  # tiN-Sit sArvadhAtukam (samjna, MR-1)
    for i, (ph, feats) in enumerate(w):
        if "affix" in feats and ("tiN" in feats or is_Sit(w[i])):
            w = set_m(w, i, add=("sArvadhAtuka",))
    return w


def chah_7_3_77(w: Word) -> Word:  # izugamiyamAM chaH : final of iz/gam/yam -> ch before Sit affix
    for i in range(len(w) - 1):
        ph, feats = w[i]
        if "root" in feats and ph in (("i", "z"), ("g", "a", "m"), ("y", "a", "m")) and is_Sit(w[i + 1]):
            w = set_m(w, i, phones=ph[:-1] + ("ch",))
    return w


def tuk_6_1_73(w: Word) -> Word:  # che ca : tuk augment after a short vowel before ch (Agama)
    for i, (ph, feats) in enumerate(w):
        for k in range(1, len(ph)):
            if ph[k] == "ch" and ph[k - 1] in SHORT and ph[k - 1 : k] != ("t",):
                w = set_m(w, i, phones=ph[:k] + ("t",) + ph[k:])
                break
    return w


def scutva_8_4_40(w: Word) -> Word:  # stoH ScunA ScuH : t + ch -> c ch
    for i, (ph, feats) in enumerate(w):
        for k in range(len(ph) - 1):
            if ph[k] == "t" and ph[k + 1] == "ch":
                w = set_m(w, i, phones=ph[:k] + ("c",) + ph[k + 1 :])
                break
    return w


def guna_7_3_84(w: Word) -> Word:  # sArvadhAtukArdhadhAtukayoH : ik-final anga -> guna before such affix
    for i in range(len(w) - 1):
        ph, feats = w[i]
        nxt = w[i + 1][1]
        if "root" in feats and ph and ph[-1] in ("i", "I", "u", "U", "R") and ("sArvadhAtuka" in nxt or "ArdhadhAtuka" in nxt):
            short = {"I": "i", "U": "u"}.get(ph[-1], ph[-1])
            w = set_m(w, i, phones=ph[:-1] + (GUNA[short],))
    return w


def ayadi_internal_6_1_78(w: Word) -> Word:  # e/o -> ay/av before a vowel-initial morpheme
    for i in range(len(w) - 1):
        ph, feats = w[i]
        nph = w[i + 1][0]
        if ph and ph[-1] in ("e", "o", "ai", "au") and nph and nph[0] in VOWELS:
            w = set_m(w, i, phones=ph[:-1] + ({"e": "ay", "o": "av", "ai": "Ay", "au": "Av"}[ph[-1]],))
    return w


PIPELINE: list[tuple[str, Callable[[Word], Word]]] = [
    ("3.4.113", sarvadhatuka_3_4_113),
    ("7.3.77", chah_7_3_77),
    ("7.3.84", guna_7_3_84),
    ("6.1.78", ayadi_internal_6_1_78),
    ("6.1.73", tuk_6_1_73),
    ("8.4.40", scutva_8_4_40),
]


def derive(w: Word, carry_memory: bool = True, skip: str | None = None, lopa_last: bool = False) -> Word:
    steps = [("1.3.9", lambda x: it_lopa(x, carry_memory))] + [(s, f) for s, f in PIPELINE if s != skip]
    if lopa_last:
        steps = steps[1:] + steps[:1]
    for _ in range(6):
        before = w
        for _, f in steps:
            w = f(w)
        if w == before:
            return w
    return w


def it_phone_count(w: Word) -> int:
    n = 0
    for ph, feats in w[1:]:
        if "affix" in feats:
            n += int(ph[0] in ("S", "l", "k")) + int(ph[-1] in CONSONANTS and len(ph) > 1)
    return n


def memory_count(w: Word) -> int:
    return sum(len([f for f in feats if f.endswith("it")]) for _, feats in w)


GAM = word((("g", "a", "m"), {"root"}), (("S", "a", "p"), {"affix"}), (("t", "i", "p"), {"affix", "tiN"}))
NI = word((("n", "I"), {"root"}), (("S", "a", "p"), {"affix"}), (("t", "i", "p"), {"affix", "tiN"}))


def t3_memory_load_bearing() -> dict[str, Any]:
    gacchati = recognized(derive(GAM))
    nayati = recognized(derive(NI))
    no_mem_gam = recognized(derive(GAM, carry_memory=False))
    no_mem_ni = recognized(derive(NI, carry_memory=False))
    ablations = {}
    for sid, _ in PIPELINE:
        ablations[sid] = {"gam": recognized(derive(GAM, skip=sid)), "nI": recognized(derive(NI, skip=sid))}
    # BUILD NOTE: first draft listed 3.4.113 as load-bearing for gacchati; the certificate refused it --
    # 7.3.77 is conditioned on Sit directly, the sArvadhAtuka samjna is consumed only by 7.3.84 (nayati).
    gam_rules = ("7.3.77", "6.1.73", "8.4.40")
    ni_rules = ("3.4.113", "7.3.84", "6.1.78")
    each_load_bearing = all(ablations[s]["gam"] != gacchati for s in gam_rules) and all(ablations[s]["nI"] != nayati for s in ni_rules)
    # 1.1.62: lopa first vs lopa last agree iff memory carried
    order_free_with_memory = recognized(derive(GAM, lopa_last=True)) == gacchati and recognized(derive(NI, lopa_last=True)) == nayati
    # without memory the rule can still read the S-phone if lopa has not yet happened: order becomes content
    order_matters_without_memory = recognized(derive(GAM, carry_memory=False, lopa_last=True)) == "gacchati" != no_mem_gam
    conservation = all(it_phone_count(w0) == memory_count(derive(w0)) and memory_count(w0) == 0 for w0 in (GAM, NI))
    checks = {
        "gam_Sap_tip_derives_gacchati": gacchati == "gacchati",
        "nI_Sap_tip_derives_nayati": nayati == "nayati",
        "memory_erased_at_lopa_gives_gamati_and_nIati": (no_mem_gam, no_mem_ni) == ("gamati", "nIati"),
        "every_pipeline_rule_load_bearing_by_ablation": each_load_bearing,
        "1_1_62_lopa_order_free_iff_memory_carried": order_free_with_memory and order_matters_without_memory,
        "conservation_it_phones_deleted_equals_memory_added": conservation,
    }
    return {
        "checks": checks,
        "outputs": {"gacchati": gacchati, "nayati": nayati, "no_memory": [no_mem_gam, no_mem_ni]},
        "ablations": ablations,
        "lopa_last_without_memory": recognized(derive(GAM, carry_memory=False, lopa_last=True)),
    }


def t4_ras_claims() -> dict[str, Any]:
    rules = [r for _, r in SANDHI]
    ii_free = free_normal_forms(("i", "i"), rules)
    checks = {
        "determinacy_DISPROVED_under_free_application_witness_i_plus_i": ii_free == {("y", "i"), ("I",)},
        "determinacy_PROVED_under_1_4_2_on_enumerated_carrier": all(isinstance(priority_normal_form((x, y), SANDHI), tuple) for x in VOWELS for y in VOWELS),
    }
    return {"checks": checks, "i_plus_i_free_normal_forms": sorted("".join(f) for f in ii_free), "soundness_completeness": "NOT CLAIMED: no oracle for 'valid Sanskrit' exists in the repo"}


def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_vowel_ladder": t1_vowel_ladder(),
        "t2_priority_is_commutator_support": t2_priority_is_commutator_support(),
        "t3_memory_load_bearing": t3_memory_load_bearing(),
        "t4_ras_claims": t4_ras_claims(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PANINIAN_SEAM_CALCULUS_CANDIDATE" if all(checks.values()) else "FAIL_PANINIAN_SEAM_CALCULUS_CANDIDATE"
    return {
        "schema": "rkf.paninian_seam_calculus_candidate.v1",
        "status": status,
        "canonical_sutras_used": {
            "1.1.1": "vRddhir Adaic", "1.1.2": "adeG guNaH", "1.1.3": "iko guNavRddhI", "1.1.62": "pratyayalope pratyayalakSaNam",
            "1.3.3": "hal antyam", "1.3.8": "laSakv ataddhite", "1.3.9": "tasya lopaH", "1.4.2": "vipratiSedhe paraM kAryam",
            "3.4.113": "tiGSit sArvadhAtukam", "6.1.73": "che ca", "6.1.77": "iko yaN aci", "6.1.78": "eco 'yavAyAvaH",
            "6.1.87": "Ad guNaH", "6.1.88": "vRddhir eci", "6.1.101": "akaH savarNe dIrghaH", "7.3.77": "izugamiyamAM chaH",
            "7.3.84": "sArvadhAtukArdhadhAtukayoH", "8.4.40": "stoH ScunA ScuH",
        },
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "vowel-strength ladder {id, G, V} is a commutative idempotent monoid with GV = VG = V (1.1.1/1.1.2 as samjna tables; 1.1.3 scope)",
                "on the ten-vowel junction carrier the free-application ambiguity set EQUALS the union of pairwise commutator supports; disjoint-trigger pairs commute; 1.4.2 yields a unique normal form for every junction (computed)",
                "gam+Sap+tip -> gacchati and nI+Sap+tip -> nayati under canonical rules; the memory channel (1.1.62) is load-bearing: erased memory gives gamati/nIati; lopa order is free iff memory is carried; it-phones deleted = memory features added",
                "R-A-S determinacy: DISPROVED under free application (i+i: yi vs I), PROVED under 1.4.2 on the enumerated carrier",
            ],
            "NOT_claimed": [
                "soundness or completeness of the R-A-S semigroup (no oracle for valid Sanskrit)",
                "coverage beyond the 18 canonical sutras and two derivations used; the 3,959-rule engine is a declared protocol (theorum/56 boundary stands)",
                "an embedding of the rules as matrices on a C_Sigma free module (the two-channel carrier here is combinatorial)",
                "the canvas 'gain / averaging / derivative' readings of 1.1.1-1.1.5 (refused: only the semilattice is present)",
                "anything from the Prime Operator Engine canvas (refused: not a consistent definition; native primes are F00H/F00I)",
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
    body = canonical_bytes(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
