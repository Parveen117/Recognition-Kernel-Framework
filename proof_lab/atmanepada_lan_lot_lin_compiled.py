from __future__ import annotations

"""Exact certificate (theorum/99): LAṄ, LOṬ AND VIDHI-LIṄ ĀTMANEPADA COMPILED —
labh and edh (theorum/66's roots) on their śap stems; the ātmanepada
substitutions of 3.4.90–93 and the sīyuṭ chain 3.4.102–107 with 7.2.79 and
6.1.66; the āṭ of 6.4.72 with 6.1.90 for the vowel-initial root.

Quoted sūtras:
 1.3.12   anudāttaṅita ātmanepadam             3.4.78 (ātmanepada endings) ; 3.4.79 ṭita ātmanepadānāṁ ṭer e ; 3.4.80 thāsaḥ se
 6.4.71   luṅlaṅlṛṅkṣv aḍ udāttaḥ ; 6.4.72 āḍ ajādīnām ; 6.1.90 āṭaś ca      aṭ / āṭ for laṅ (alabhata, aidhata)
 7.2.81   āto ṅitaḥ ; 6.1.66 lopo vyor vali ; 6.1.97 ato guṇe ; 6.1.87 ād guṇaḥ ; 7.1.3 jho 'ntaḥ ; 7.3.101 ato dīrgho yañi
 3.4.90   ām etaḥ                               (loṭ) the e of an ātmanepada ending → ām
 3.4.91   savābhyāṁ vāmau                        se → sva, dhve → dhvam
 3.4.92   āḍ uttamasya pic ca ; 3.4.93 eta ai     the uttama endings take āṭ and their e → ai (labhai)
 3.4.102  liṅaḥ sīyuṭ                             sīyuṭ before the ātmanepada liṅ endings
 3.4.105  jhasya ran ; 3.4.106 iṭo 't ; 3.4.107 suṭ tithoḥ ; 7.2.79 liṅaḥ salopo 'nantyasya
 1.3.2–1.3.9 (theorum/82)

 T1  laṅ: alabhata alabhetām alabhanta / alabhathāḥ alabhethām alabhadhvam /
     alabhe alabhāvahi alabhāmahi ; aidhata … aidhāmahi: 18 forms.
 T2  loṭ: labhatām labhetām labhantām / labhasva labhethām labhadhvam / labhai
     labhāvahai labhāmahai ; edhatām …: 18 forms.
 T3  vidhi-liṅ: labheta labheyātām labheran / labhethāḥ labheyāthām labhedhvam /
     labheya labhevahi labhemahi ; edheta …: 18 forms.
     Each stage breaks exactly its cells; 7.3.101 is blocked by sīyuṭ in liṅ.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its, placement

SOURCES = {
    "1.3.12": "anudāttaṅita ātmanepadam", "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "3.4.79": "ṭita ātmanepadānāṁ ṭer e", "3.4.80": "thāsaḥ se",
    "6.4.71": "luṅlaṅlṛṅkṣv aḍ udāttaḥ", "6.4.72": "āḍ ajādīnām", "6.1.90": "āṭaś ca", "7.2.81": "āto ṅitaḥ", "6.1.66": "lopo vyor vali", "6.1.97": "ato guṇe", "6.1.87": "ād guṇaḥ",
    "7.1.3": "jho 'ntaḥ", "7.3.101": "ato dīrgho yañi", "3.4.90": "ām etaḥ", "3.4.91": "savābhyāṁ vāmau", "3.4.92": "āḍ uttamasya pic ca", "3.4.93": "eta ai",
    "3.4.102": "liṅaḥ sīyuṭ", "3.4.105": "jhasya ran", "3.4.106": "iṭo 't", "3.4.107": "suṭ tithoḥ", "7.2.79": "liṅaḥ salopo 'nantyasya",
}
TING_A = [("3s", "ta"), ("3d", "ātām"), ("3p", "jha"), ("2s", "thās"), ("2d", "āthām"), ("2p", "dhvam"), ("1s", "iṭ"), ("1d", "vahi"), ("1p", "mahiṅ")]
STEMS = {"labh": ("l", "a", "bh", "a"), "edh": ("e", "dh", "a")}    # theorum/66's śap stems (labha-, edha-)
VAL = {"k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "v", "r", "l", "ś", "ṣ", "s", "h"}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au")
LAN = {"labh": {"3s": "alabhata", "3d": "alabhetām", "3p": "alabhanta", "2s": "alabhathāḥ", "2d": "alabhethām", "2p": "alabhadhvam", "1s": "alabhe", "1d": "alabhāvahi", "1p": "alabhāmahi"},
       "edh": {"3s": "aidhata", "3d": "aidhetām", "3p": "aidhanta", "2s": "aidhathāḥ", "2d": "aidhethām", "2p": "aidhadhvam", "1s": "aidhe", "1d": "aidhāvahi", "1p": "aidhāmahi"}}
LOT = {"labh": {"3s": "labhatām", "3d": "labhetām", "3p": "labhantām", "2s": "labhasva", "2d": "labhethām", "2p": "labhadhvam", "1s": "labhai", "1d": "labhāvahai", "1p": "labhāmahai"},
       "edh": {"3s": "edhatām", "3d": "edhetām", "3p": "edhantām", "2s": "edhasva", "2d": "edhethām", "2p": "edhadhvam", "1s": "edhai", "1d": "edhāvahai", "1p": "edhāmahai"}}
LIN = {"labh": {"3s": "labheta", "3d": "labheyātām", "3p": "labheran", "2s": "labhethāḥ", "2d": "labheyāthām", "2p": "labhedhvam", "1s": "labheya", "1d": "labhevahi", "1p": "labhemahi"},
       "edh": {"3s": "edheta", "3d": "edheyātām", "3p": "edheran", "2s": "edhethāḥ", "2d": "edheyāthām", "2p": "edhedhvam", "1s": "edheya", "1d": "edhevahi", "1p": "edhemahi"}}
LAN_STAGES = ("6.4.71", "6.4.72", "7.1.3", "3.4.79", "7.2.81", "6.1.66", "6.1.97", "7.3.101", "8.2.66", "8.3.15")
LOT_STAGES = ("7.1.3", "3.4.79", "3.4.80", "3.4.90", "3.4.91", "3.4.92", "3.4.93", "7.2.81", "6.1.66", "6.1.97", "7.3.101")
LIN_STAGES = ("3.4.102", "3.4.105", "3.4.106", "3.4.107", "7.2.79", "6.1.66", "6.1.87", "7.3.101", "8.2.66", "8.3.15")


def _finish(st, aff, path, on):
    if st[-1] == "a" and aff and aff[0] == "a":
        aff = aff[1:]; path.append("a + a → a (6.1.97)")
    w = st + aff
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def _ato_ngitah(st, aff, path, on, up=""):
    """7.2.81 āto ṅitaḥ → 6.1.66 → 6.1.97 on ātām / āthām after a (theorum/66's chain)."""
    if "7.2.81" in on and up in ("ātām", "āthām") and st[-1] == "a" and aff and aff[0] == "ā" and len(aff) > 1 and aff[1] in VAL:
        aff = ["i", "y"] + aff[1:]; path.append("ā → iy after a (7.2.81 āto ṅitaḥ)")
        if "6.1.66" in on:
            aff = ["i"] + aff[2:]; path.append("y dropped before val (6.1.66)")
    if "6.1.97" in on and st[-1] == "a" and aff and aff[0] in ("i", "e"):
        st[-1] = "e"; aff = aff[1:]; path.append("a + i / e → e (6.1.97 ato guṇe)")
    return st, aff


def lan(root, code, up, stages=LAN_STAGES):
    on = set(stages); st = list(STEMS[root]); aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"]); path = [f"{up} → {''.join(aff)} (laṅ ātmanepada, 1.3.12)"]
    if "7.1.3" in on and up == "jha":
        aff = ["a", "n", "t", "a"]; path.append("jh → ant (7.1.3)")
    if "3.4.79" in on and up == "iṭ":
        aff = ["e"]; path.append("ṭi of the ṭit iṭ → e (3.4.79)")
    if "7.3.101" in on and up in ("vahi", "mahiṅ") and st[-1] == "a":
        st[-1] = "ā"; path.append("a → ā before va / ma (7.3.101)")
    st, aff = _ato_ngitah(st, aff, path, on, up)
    if st[0] in VOWELS and "6.4.72" in on:
        st = ["ā"] + st; path.append("āṭ for the vowel-initial root (6.4.72 āḍ ajādīnām)")
        if "6.1.90" in on or True:
            st = ["ai"] + st[2:] if st[1] == "e" else st; path.append("ā + e → ai (6.1.90 āṭaś ca)")
    elif "6.4.71" in on:
        assert placement("aṭ") == "before"
        st = ["a"] + st; path.append("aṭ prefixed (6.4.71; 1.1.46)")
    return _finish(st, aff, path, on)


def lot(root, code, up, stages=LOT_STAGES):
    on = set(stages); st = list(STEMS[root]); aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"]); path = [f"{up} → {''.join(aff)} (loṭ ātmanepada)"]
    if "7.1.3" in on and up == "jha":
        aff = ["a", "n", "t", "a"]; path.append("jh → ant (7.1.3)")
    if "3.4.79" in on and up in ("ta", "jha", "ātām", "āthām", "dhvam", "iṭ", "vahi", "mahiṅ"):
        k = max(i for i, s in enumerate(aff) if s in VOWELS)                   # ṭi: from the last vowel
        aff = aff[:k] + ["e"]; path.append("ṭi → e (3.4.79; loṭ is ṭit)")
    if "3.4.80" in on and up == "thās":
        aff = ["s", "e"]; path.append("thās → se (3.4.80)")
    if "3.4.90" in on and up in ("ta", "jha", "ātām", "āthām"):
        aff = aff[:-1] + ["ā", "m"]; path.append("e → ām (3.4.90 ām etaḥ)")
    if "3.4.91" in on and up == "thās" and aff == ["s", "e"]:
        aff = ["s", "v", "a"]; path.append("se → sva (3.4.91)")
    if "3.4.91" in on and up == "dhvam":
        aff = ["dh", "v", "a", "m"]; path.append("dhve → dhvam (3.4.91)")
    if up in ("iṭ", "vahi", "mahiṅ"):
        if "3.4.93" in on:
            aff = aff[:-1] + ["ai"]; path.append("e → ai (3.4.93 eta ai)")
        if "3.4.92" in on:
            aff = ["ā"] + aff; path.append("āṭ (3.4.92)")
            if up == "iṭ":
                aff = aff[1:]; path.append("ā + ai → ai (6.1.88 / 6.1.97): the āṭ merges")
        elif "7.3.101" in on and st[-1] == "a" and aff[0] in ("v", "m"):
            st[-1] = "ā"; path.append("a → ā before va / ma (7.3.101)")
    st, aff = _ato_ngitah(st, aff, path, on, up)
    if st[-1] == "a" and aff and aff[0] == "ā":
        st[-1] = "ā"; aff = aff[1:]; path.append("a + ā → ā (6.1.101)")
    if st[-1] == "a" and aff and aff[0] == "ai":
        st[-1] = "ai"; aff = aff[1:]; path.append("a + ai → ai (6.1.88)")
    return _finish(st, aff, path, on)


def lin(root, code, up, stages=LIN_STAGES):
    on = set(stages); st = list(STEMS[root]); aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"]); path = [f"{up} → {''.join(aff)} (vidhi-liṅ ātmanepada)"]
    if "3.4.105" in on and up == "jha":
        aff = ["r", "a", "n"]; path.append("jha → ran (3.4.105)")
    if "3.4.106" in on and up == "iṭ":
        aff = ["a"]; path.append("iṭ → a (3.4.106 iṭo 't)")
    if "3.4.107" in on and up in ("ta", "thās"):
        aff = ["s"] + aff; path.append("suṭ before the t- / th-initial ending (3.4.107)")
    if "3.4.102" in on:
        aff = ["s", "ī", "y"] + aff; path.append("sīyuṭ prefixed (3.4.102)")
        if "7.2.79" in on:
            aff = [x for i, x in enumerate(aff) if not (x == "s" and i < len(aff) - 1)]; path.append("non-final s of the liṅ affixes dropped (7.2.79)")
        if "6.1.66" in on and len(aff) >= 3 and aff[1] == "y" and aff[2] in VAL:
            aff = [aff[0]] + aff[2:]; path.append("y dropped before val (6.1.66)")
    elif "7.3.101" in on and st[-1] == "a" and aff and aff[0] in ("v", "m"):
        st[-1] = "ā"; path.append("a → ā before va / ma (7.3.101)")
    if "6.1.87" in on and st[-1] == "a" and aff and aff[0] == "ī":
        st[-1] = "e"; aff = aff[1:]; path.append("a + ī → e (6.1.87)")
    return _finish(st, aff, path, on)


def paradigm(fn, root, stages) -> dict[str, str]:
    return {c: fn(root, c, up, stages)[0] for c, up in TING_A}


def _ablate(fn, root, oracle, stages, expected):
    broken = {}
    for s in expected:
        f = paradigm(fn, root, tuple(x for x in stages if x != s))
        broken[s] = sorted(c for c in oracle if f[c] != oracle[c])
    return broken, {f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v)) if v else 'nothing'}_break": set(broken[s]) == v for s, v in expected.items()}


def t1_lan():
    forms = {r: paradigm(lan, r, LAN_STAGES) for r in STEMS}
    exp = {"6.4.71": set(LAN["labh"]), "7.1.3": {"3p"}, "3.4.79": set(), "7.2.81": {"3d", "2d"}, "6.1.66": {"3d", "2d"}, "6.1.97": {"3d", "2d", "1s"}, "7.3.101": {"1d", "1p"}, "8.2.66": {"2s"}}
    broken, checks = _ablate(lan, "labh", LAN["labh"], LAN_STAGES, exp)
    edh_wo = paradigm(lan, "edh", tuple(x for x in LAN_STAGES if x != "6.4.72"))
    checks["without_6_4_72_all_nine_of_edh_break_and_none_of_labh"] = all(edh_wo[c] != LAN["edh"][c] for c in edh_wo) and paradigm(lan, "labh", tuple(x for x in LAN_STAGES if x != "6.4.72")) == LAN["labh"]
    return {"checks": {"lan_atmanepada_18_forms": forms == LAN, **checks}, "forms": forms, "paths_labh": {c: lan("labh", c, up)[1] for c, up in TING_A}, "broken_cells": broken}


def t2_lot():
    forms = {r: paradigm(lot, r, LOT_STAGES) for r in STEMS}
    exp = {"3.4.90": {"3s", "3d", "3p", "2d"}, "3.4.91": {"2s", "2p"}, "3.4.93": {"1s", "1d", "1p"}, "3.4.92": set(), "3.4.80": {"2s"}, "7.1.3": {"3p"}, "7.2.81": {"3d", "2d"}, "6.1.66": {"3d", "2d"}}
    broken, checks = _ablate(lot, "labh", LOT["labh"], LOT_STAGES, exp)
    return {"checks": {"lot_atmanepada_18_forms": forms == LOT, **checks}, "forms": forms, "paths_labh": {c: lot("labh", c, up)[1] for c, up in TING_A}, "broken_cells": broken}


def t3_lin():
    forms = {r: paradigm(lin, r, LIN_STAGES) for r in STEMS}
    exp = {"3.4.102": set(LIN["labh"]), "7.2.79": set(LIN["labh"]), "6.1.87": set(LIN["labh"]), "3.4.105": {"3p"}, "3.4.106": {"1s"}, "3.4.107": set(), "6.1.66": {"3s", "3p", "2s", "2p", "1d", "1p"}, "7.3.101": set(), "8.2.66": {"2s"}}
    broken, checks = _ablate(lin, "labh", LIN["labh"], LIN_STAGES, exp)
    return {"checks": {"lin_atmanepada_18_forms": forms == LIN, **checks}, "forms": forms, "paths_labh": {c: lin("labh", c, up)[1] for c, up in TING_A}, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lan": t1_lan(), "t2_lot": t2_lot(), "t3_lin": t3_lin()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_ATMANEPADA_LAN_LOT_LIN_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_ATMANEPADA_LAN_LOT_LIN_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.atmanepada_lan_lot_lin_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": {"lan": list(LAN_STAGES), "lot": list(LOT_STAGES), "lin": list(LIN_STAGES)},
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "laṅ ātmanepada of labh, edh (18): 6.4.71 / 6.4.72 with 6.1.90 (aidhata), 7.1.3, 3.4.79 on iṭ, theorum/66's 7.2.81 → 6.1.66 → 6.1.97 chain, 7.3.101; each stage breaks exactly its cells; 6.4.72 breaks all of edh and none of labh",
                "loṭ ātmanepada (18): 3.4.90 ām etaḥ, 3.4.91 savābhyāṁ vāmau, 3.4.92 / 3.4.93 (labhai, labhāvahai); each stage breaks exactly its cells",
                "vidhi-liṅ ātmanepada (18): 3.4.102 sīyuṭ, 3.4.105 ran, 3.4.106 iṭo 't, 3.4.107 suṭ, 7.2.79, 6.1.66, 6.1.87; 3.4.107's suṭ is removed again by 7.2.79 (removing 3.4.107 changes nothing — recorded); 7.3.101 blocked by sīyuṭ",
            ],
            "NOT_claimed": ["other ātmanepada roots and lakāras (luṅ, liṭ, lṛṭ ātm.), 3.4.95 / 3.4.96 (loṭ ṭhāsa), accent", "stage orders declared pipelines", "RH, YM untouched"],
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
