from __future__ import annotations

"""Exact certificate (theorum/88): THE ĀP-STEM SUP PARADIGM COMPILED — ṭāp
feminines of the kta nouns of theorum/86–87 declined through the quoted
sūtras on the theorum/82 it-layer; the nominal grammar opened beyond the
a-stem ladder of theorum/63.

Quoted sūtras:
 4.1.4    ajādyataṣ ṭāp                     ṭāp after the ajādi stems and a-final stems (feminine)
 4.1.2    svaujas … sup                      the sup affixes (theorum/63)
 7.1.18   auṅ āpaḥ                            after āp, au (auṭ) becomes śī
 7.3.116  ṅer ām nadyāmnībhyaḥ                after nadī, āp, nī: ṅi becomes ām
 7.3.113  yāḍ āpaḥ                            a ṅit sup after āp takes the augment yāṭ
 7.1.54   hrasvanadyāpo nuṭ                   after a short vowel, nadī, āp: ām takes nuṭ
 7.3.105  āṅi cāpaḥ                           āp-final → e before ṭā (āṅ) and os
 7.3.106  sambuddhau ca                       and in the sambuddhi
 6.1.68   halṅyābbhyo dīrghāt sutisyapṛktaṁ hal   the single-consonant su (ti, si) drops after a long ṅī / āp
 6.1.69   eṅhrasvāt sambuddheḥ                su of the sambuddhi drops after eṅ / short vowel
 6.1.87   ād guṇaḥ ; 6.1.88 vṛddhir eci ; 6.1.101 akaḥ savarṇe dīrghaḥ ; 6.1.107 ami pūrvaḥ ; 6.1.78 eco 'yavāyāvaḥ  (theorum/58, 80, 63)
 1.1.46   ādyantau ṭakitau (yāṭ, nuṭ prefixed) ; 1.1.56 sthānivad ādeśo 'nalvidhau (ām for ṅi keeps ṅit) ; 1.1.52 alo 'ntyasya ; 1.1.55 anekāl śit sarvasya
 8.2.66   sasajuṣo ruḥ ; 8.3.15 kharavasānayor visarjanīyaḥ   (theorum/63)
 1.3.2–1.3.9 (theorum/82)

 T1  latā: the 22 forms of the classical paradigm (latā late latāḥ … latāyām
     latayoḥ latāsu; he late) are derived from the pinned sup teaching forms.
 T2  Every stage is load-bearing on a named cell: removing 7.1.18 breaks the
     duals, 7.3.113 the ṅit singulars, 7.1.54 the genitive plural, 7.3.105
     latayā / latayoḥ, 7.3.106 the vocative, 6.1.68 the nominative,
     7.3.116 the locative.
 T3  The fifteen kta stems of theorum/86–87 + ṭāp (gatā? no — bhūtā, sutā, citā,
     āptā, śaktā, tatā, kṛtā, krītā, śrutā, pūtā, hutā, paktā, labdhā, tunnā,
     lūnā): 15 × 22 = 330 forms, equal to the latā paradigm with the stem
     exchanged.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.nirukta_dhatupatha_nama import ENTRIES as ENTRIES86, kta_from_entry, load_entries
from proof_lab.paninian_it_samjna_compiled import its
from proof_lab.tripadi_nishtha_compiled import ENTRIES as ENTRIES87, nishtha

SOURCES = {
    "4.1.4": "ajādyataṣ ṭāp", "7.1.18": "auṅ āpaḥ", "7.3.116": "ṅer ām nadyāmnībhyaḥ", "7.3.113": "yāḍ āpaḥ", "7.1.54": "hrasvanadyāpo nuṭ",
    "7.3.105": "āṅi cāpaḥ", "7.3.106": "sambuddhau ca", "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "6.1.69": "eṅhrasvāt sambuddheḥ",
    "6.1.87": "ād guṇaḥ", "6.1.88": "vṛddhir eci", "6.1.101": "akaḥ savarṇe dīrghaḥ", "6.1.107": "ami pūrvaḥ", "6.1.78": "eco 'yavāyāvaḥ",
    "1.1.46": "ādyantau ṭakitau", "1.1.56": "sthānivad ādeśo 'nalvidhau", "1.1.52": "alo 'ntyasya", "1.1.55": "anekāl śit sarvasya",
    "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}

# the 21 sup + sambuddhi, as teaching forms (4.1.2), with the case code
SUP = [("1s", "su~"), ("1d", "auṭ"), ("1p", "jas"), ("2s", "am"), ("2d", "auṭ"), ("2p", "śas"), ("3s", "ṭā"), ("3d", "bhyām"), ("3p", "bhis"),
       ("4s", "ṅe"), ("4d", "bhyām"), ("4p", "bhyas"), ("5s", "ṅasi~"), ("5d", "bhyām"), ("5p", "bhyas"), ("6s", "ṅas"), ("6d", "os"), ("6p", "ām"),
       ("7s", "ṅi"), ("7d", "os"), ("7p", "sup"), ("8s", "su~")]
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")
LATA_ORACLE = {"1s": "latā", "1d": "late", "1p": "latāḥ", "2s": "latām", "2d": "late", "2p": "latāḥ", "3s": "latayā", "3d": "latābhyām", "3p": "latābhiḥ",
               "4s": "latāyai", "4d": "latābhyām", "4p": "latābhyaḥ", "5s": "latāyāḥ", "5d": "latābhyām", "5p": "latābhyaḥ", "6s": "latāyāḥ", "6d": "latayoḥ",
               "6p": "latānām", "7s": "latāyām", "7d": "latayoḥ", "7p": "latāsu", "8s": "late"}
ALL_STAGES = ("7.1.18", "7.3.116", "7.3.113", "7.1.54", "7.3.105", "7.3.106", "6.1.68", "6.1.69", "sandhi", "8.2.66", "8.3.15")


def tap_stem(a_stem: tuple[str, ...]) -> tuple[str, ...]:
    """4.1.4: a-final stem + ṭāp (ā; ṭ, p its) → ā-final by 6.1.101."""
    assert a_stem[-1] == "a"
    ap = its("ṭāp", "pratyaya")["remaining_sounds"]      # ("ā",)
    return a_stem[:-1] + ("ā",)                           # a + ā → ā (6.1.101 akaḥ savarṇe dīrghaḥ)


def decline(stem: tuple[str, ...], code: str, upadesa: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(upadesa, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    marks = set(r["its"])
    ngit = "ṅ" in marks
    st = list(stem)
    path: list[str] = [f"{upadesa} → {''.join(aff)} ({', '.join(sorted(set(r['its'].values())))})"]
    sambuddhi = code == "8s"
    # 7.1.18 auṅ āpaḥ
    if "7.1.18" in on and upadesa == "auṭ":
        aff = list(its("śī", "pratyaya")["remaining_sounds"]); path.append("auṭ → śī (7.1.18; 1.1.55 whole)")
    # 7.3.116 ṅer ām (ām keeps ṅit by 1.1.56)
    if "7.3.116" in on and code == "7s":
        aff = ["ā", "m"]; path.append("ṅi → ām (7.3.116; ṅit retained, 1.1.56)")
    # 7.3.113 yāḍ āpaḥ
    if "7.3.113" in on and ngit:
        yat = list(its("yāṭ", "agama")["remaining_sounds"])
        aff = yat + aff; path.append("yāṭ prefixed (7.3.113; 1.1.46 ṭit → ādi)")
    # 7.1.54 nuṭ
    if "7.1.54" in on and code == "6p":
        nut = list(its("nu~ṭ", "agama")["remaining_sounds"])
        aff = nut + aff; path.append("nuṭ prefixed (7.1.54; 1.1.46)")
    # 7.3.105 āṅi cāpaḥ ; 7.3.106 sambuddhau ca
    if "7.3.105" in on and code in ("3s", "6d", "7d"):
        st[-1] = "e"; path.append("ā → e before ṭā / os (7.3.105; 1.1.52)")
    if "7.3.106" in on and sambuddhi:
        st[-1] = "e"; path.append("ā → e in the sambuddhi (7.3.106)")
    # 6.1.68 / 6.1.69: the single-consonant su drops
    if code == "1s" and "6.1.68" in on and st[-1] == "ā" and aff == ["s"]:
        aff = []; path.append("su dropped after āp (6.1.68)")
    if sambuddhi and "6.1.69" in on and st[-1] == "e" and aff == ["s"]:
        aff = []; path.append("su of the sambuddhi dropped after eṅ (6.1.69)")
    # sandhi at the seam
    if "sandhi" in on and aff and aff[0] in VOWELS:
        a, b = st[-1], aff[0]
        if a == "ā" and b == "ī":
            st[-1] = "e"; aff = aff[1:]; path.append("ā + ī → e (6.1.87)")
        elif a == "e" and b in VOWELS:
            st[-1] = "a"; st.append("y"); path.append("e + vowel → ay (6.1.78; 1.1.55)")
        elif a == "ā" and b in ("a", "ā"):
            if code == "2s":
                aff = aff[1:]; path.append("ā + am → ām (6.1.107 ami pūrvaḥ)")
            else:
                aff = aff[1:]; path.append("ā + a → ā (6.1.101)")
        elif a == "ā" and b == "e":
            st[-1] = "ai"; aff = aff[1:]; path.append("ā + e → ai (6.1.88)")
    # ṅit yā + as / e inside the affix: yā+as → yāḥ, yā+e → yai
    if aff[:2] == ["y", "ā"] and len(aff) > 2:
        if aff[2] in ("a", "ā"):
            aff = aff[:2] + aff[3:]; path.append("yā + a → yā (6.1.101)")
        elif aff[2] == "e":
            aff = ["y", "ai"] + aff[3:]; path.append("yā + e → yai (6.1.88)")
    word = st + aff
    # tripādī: 8.2.66 ruḥ, 8.3.15 visarga
    if word and word[-1] == "s":
        if "8.2.66" in on:
            word[-1] = "r"; path.append("s → ru (8.2.66)")
            if "8.3.15" in on:
                word[-1] = "ḥ"; path.append("r → ḥ at pause (8.3.15)")
    return "".join(word), path


def paradigm(stem: tuple[str, ...], stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(stem, c, up, stages)[0] for c, up in SUP}


def t1_lata() -> dict[str, Any]:
    stem = tap_stem(("l", "a", "t", "a"))                  # latā = lat + a + ṭāp (4.1.4)
    forms = paradigm(stem)
    paths = {c: decline(stem, c, up)[1] for c, up in SUP}
    checks = {"lata_22_forms_equal_the_classical_paradigm": forms == LATA_ORACLE, "tap_stem_is_lata": "".join(stem) == "latā"}
    return {"checks": checks, "forms": forms, "paths": paths}


def t2_stages_load_bearing() -> dict[str, Any]:
    stem = tap_stem(("l", "a", "t", "a"))
    expected_breaks = {"7.1.18": {"1d", "2d"}, "7.3.116": {"7s"}, "7.3.113": {"4s", "5s", "6s", "7s"}, "7.1.54": {"6p"}, "7.3.105": {"3s", "6d", "7d"},
                       "7.3.106": {"8s"}, "6.1.68": {"1s"}, "6.1.69": {"8s"}}
    broken = {}
    for stage in expected_breaks:
        forms = paradigm(stem, tuple(s for s in ALL_STAGES if s != stage))
        broken[stage] = sorted(c for c in LATA_ORACLE if forms[c] != LATA_ORACLE[c])
    checks = {f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected_breaks.items()}
    return {"checks": checks, "broken_cells": broken}


def t3_kta_feminines() -> dict[str, Any]:
    entries = load_entries()
    stems: dict[str, tuple[str, ...]] = {}
    for lex in ENTRIES86:
        stems[kta_from_entry(lex, entries[lex])["pratipadika"]] = tuple(kta_from_entry(lex, entries[lex])["sounds"])
    for lex in ENTRIES87:
        r = nishtha(lex, entries)
        stems[r["output"]] = tuple(r["sounds"])
    out, ok, n = {}, True, 0
    for name, a_stem in stems.items():
        fem = tap_stem(a_stem)
        forms = paradigm(fem)
        pref = "".join(fem[:-1])
        for c, f in forms.items():
            ok &= f == pref + LATA_ORACLE[c][3:]
            n += 1
        out["".join(fem)] = forms
    checks = {"fifteen_tap_feminines_330_forms_equal_the_exchanged_lata_paradigm": ok and n == 330 and len(stems) == 15}
    return {"checks": checks, "stems": sorted(out), "forms": out}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lata": t1_lata(), "t2_stages_load_bearing": t2_stages_load_bearing(), "t3_kta_feminines": t3_kta_feminines()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_AP_STEM_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_AP_STEM_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.ap_stem_sup_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "latā's 22 forms from the pinned sup teaching forms through 4.1.4, 7.1.18, 7.3.116, 7.3.113, 7.1.54, 7.3.105, 7.3.106, 6.1.68, 6.1.69, the sandhi sūtras and 8.2.66 / 8.3.15",
                "each named stage is load-bearing on exactly the cells stated (removal breaks those and only those)",
                "the fifteen ṭāp feminines of the kta nouns of theorum/86–87: 330 forms equal to the exchanged latā paradigm",
            ],
            "NOT_claimed": [
                "the stage order is declared (a pipeline), not derived from 1.4.2 / apavāda relations as theorum/63 does for the a-stem",
                "ṅīp / other feminine stems, nadī, consonant stems, pronouns; ṇatva (8.4.2) is not needed on these stems (no r/ṣ before the n)",
                "4.1.4's ajādi list is cited, not carried; only a-final stems are fed",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


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
    for name, v in payload.items():
        if isinstance(v, dict) and "checks" in v:
            for k, val in v["checks"].items():
                print(f"    {name}.{k}: {val}")
    print("sha256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
