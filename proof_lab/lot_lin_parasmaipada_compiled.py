from __future__ import annotations

"""Exact certificate (theorum/96): LOṬ AND VIDHI-LIṄ PARASMAIPADA COMPILED ON
theorum/58's STEMS — bhū, gam, nī; the imperative on 3.4.85–92 and 6.4.105,
the optative on yāsuṭ (3.4.103) with 7.2.79 / 7.2.80 / 6.1.66 / 6.1.97 and jus
(3.4.108); 7.3.101 shown blocked by the intervening yāsuṭ (bhaveva).

Quoted sūtras:
 3.3.162  loṭ ca                               3.3.161  vidhinimantraṇāmantraṇādhīṣṭasampraśnaprārthaneṣu liṅ
 3.4.85   loṭo laṅvat                          loṭ behaves like laṅ (3.4.100, 3.4.101, 3.4.99 apply)
 3.4.86   er uḥ                                the i of a loṭ ending becomes u (tu, antu)
 3.4.87   ser hy apic ca                       sip becomes hi, and is apit
 3.4.89   mer niḥ                               mip becomes ni
 3.4.92   āḍ uttamasya pic ca                   the uttama endings take āṭ and are pit (bhavāni, bhavāva, bhavāma)
 6.4.105  ato heḥ                               hi is luk after a (bhava)
 3.4.103  yāsuṭ parasmaipadeṣūdātto ṅic ca      liṅ parasmaipada endings take yāsuṭ and are ṅit
 3.4.108  jher jus                              jhi becomes jus
 7.2.79   liṅaḥ salopo 'nantyasya               the non-final s of the liṅ augment drops (sārvadhātuka)
 7.2.80   ato yeyaḥ                             after a, yā becomes iy
 6.1.66   lopo vyor vali                        v / y drop before a val consonant
 6.1.97   ato guṇe                              a + guṇa vowel → the latter (pararūpa)
 3.4.100 ; 3.4.101 ; 3.4.99 ; 7.1.3 ; 8.2.23 ; 7.3.101 ; 8.2.66 ; 8.3.15 ; 1.1.46 ; 1.3.2–1.3.9

 T1  loṭ: bhavatu bhavatām bhavantu / bhava bhavatam bhavata / bhavāni
     bhavāva bhavāma (and gaccha-, naya-): 27 forms; each stage breaks
     exactly its cells (3.4.86 {3s, 3p}, 3.4.87 + 6.4.105 {2s}, 3.4.89 {1s},
     3.4.92 {1s} — on 1d / 1p the surface coincides with 7.3.101's bhavāva, recorded —, 3.4.85-inherited 3.4.101 {3d, 2d, 2p}, 3.4.99 {1d, 1p}).
 T2  vidhi-liṅ: bhavet bhavetām bhaveyuḥ / bhaveḥ bhavetam bhaveta / bhaveyam
     bhaveva bhavema (and gacche-, naye-): 27 forms; 3.4.103 all nine,
     7.2.79 and 7.2.80 all nine, 6.1.66 {3s, 3d, 2s, 2d, 2p, 1d, 1p}, 3.4.108
     {3p}; 7.3.101 does not fire (yāsuṭ intervenes): removing it changes nothing.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.lan_parasmaipada_compiled import BHU, CODE58, ORACLE as LAN_ORACLE, TING_P, present_stem
from proof_lab.paninian_it_samjna_compiled import its, placement
from proof_lab.paninian_seam_calculus import GAM, NI

SOURCES = {
    "3.3.162": "loṭ ca", "3.3.161": "vidhinimantraṇāmantraṇādhīṣṭasampraśnaprārthaneṣu liṅ", "3.4.85": "loṭo laṅvat", "3.4.86": "er uḥ", "3.4.87": "ser hy apic ca",
    "3.4.89": "mer niḥ", "3.4.92": "āḍ uttamasya pic ca", "6.4.105": "ato heḥ", "3.4.103": "yāsuṭ parasmaipadeṣūdātto ṅic ca", "3.4.108": "jher jus",
    "7.2.79": "liṅaḥ salopo 'nantyasya", "7.2.80": "ato yeyaḥ", "6.1.66": "lopo vyor vali", "6.1.97": "ato guṇe", "3.4.100": "itaś ca",
    "3.4.101": "tasthasthamipāṁ tāṁtaṁtāmaḥ", "3.4.99": "nityaṁ ṅitaḥ", "7.1.3": "jho 'ntaḥ", "8.2.23": "saṁyogāntasya lopaḥ", "7.3.101": "ato dīrgho yañi",
    "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
VAL = {"k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "v", "r", "l", "ś", "ṣ", "s", "h"}  # val = all consonants but y
LOT = {"bhū": {"3s": "bhavatu", "3d": "bhavatām", "3p": "bhavantu", "2s": "bhava", "2d": "bhavatam", "2p": "bhavata", "1s": "bhavāni", "1d": "bhavāva", "1p": "bhavāma"},
       "gam": {"3s": "gacchatu", "3d": "gacchatām", "3p": "gacchantu", "2s": "gaccha", "2d": "gacchatam", "2p": "gacchata", "1s": "gacchāni", "1d": "gacchāva", "1p": "gacchāma"},
       "nī": {"3s": "nayatu", "3d": "nayatām", "3p": "nayantu", "2s": "naya", "2d": "nayatam", "2p": "nayata", "1s": "nayāni", "1d": "nayāva", "1p": "nayāma"}}
LIN = {"bhū": {"3s": "bhavet", "3d": "bhavetām", "3p": "bhaveyuḥ", "2s": "bhaveḥ", "2d": "bhavetam", "2p": "bhaveta", "1s": "bhaveyam", "1d": "bhaveva", "1p": "bhavema"},
       "gam": {"3s": "gacchet", "3d": "gacchetām", "3p": "gaccheyuḥ", "2s": "gaccheḥ", "2d": "gacchetam", "2p": "gaccheta", "1s": "gaccheyam", "1d": "gaccheva", "1p": "gacchema"},
       "nī": {"3s": "nayet", "3d": "nayetām", "3p": "nayeyuḥ", "2s": "nayeḥ", "2d": "nayetam", "2p": "nayeta", "1s": "nayeyam", "1d": "nayeva", "1p": "nayema"}}
LOT_STAGES = ("3.4.85", "3.4.86", "3.4.87", "3.4.89", "3.4.92", "6.4.105", "3.4.100", "3.4.101", "3.4.99", "7.1.3", "8.2.23", "7.3.101")
LIN_STAGES = ("3.4.103", "3.4.108", "3.4.100", "3.4.101", "3.4.99", "7.2.79", "7.2.80", "6.1.66", "6.1.97", "7.3.101", "8.2.66", "8.3.15")
SUBST_101 = {"tas": ("t", "ā", "m"), "thas": ("t", "a", "m"), "tha": ("t", "a"), "mip": ("a", "m")}


def lot(stem, code, up, stages=LOT_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    st = list(stem)
    path = [f"{up} → {''.join(aff)} (loṭ, 3.3.162)"]
    laṅvat = "3.4.85" in on
    if laṅvat and "3.4.101" in on and up in SUBST_101:
        aff = list(SUBST_101[up]); path.append(f"{up} → {''.join(aff)} (3.4.101 via 3.4.85 loṭo laṅvat)")
    if "7.1.3" in on and up == "jhi":
        aff = ["a", "n", "t"] + aff[1:]; path.append("jh → ant (7.1.3)")
    if "3.4.86" in on and up in ("tip", "jhi") and aff[-1] == "i":
        aff[-1] = "u"; path.append("i → u (3.4.86 er uḥ)")
    if "3.4.87" in on and up == "sip":
        aff = ["h", "i"]; path.append("sip → hi, apit (3.4.87)")
        if "6.4.105" in on and st[-1] == "a":
            aff = []; path.append("hi → luk after a (6.4.105 ato heḥ)")
    if "3.4.89" in on and up == "mip":
        aff = ["n", "i"]; path.append("mip → ni (3.4.89)")
    if laṅvat and "3.4.99" in on and up in ("vas", "mas"):
        aff = aff[:-1]; path.append("s dropped (3.4.99 via 3.4.85)")
    if "3.4.92" in on and up in ("mip", "vas", "mas"):
        at = its("āṭ", "agama")
        assert placement("āṭ") == "before"
        aff = list(at["remaining_sounds"]) + aff; path.append("āṭ prefixed to the uttama ending, pit (3.4.92; 1.1.46)")
    elif "7.3.101" in on and st[-1] == "a" and aff and aff[0] in ("v", "m"):
        st[-1] = "ā"; path.append("a → ā before va / ma (7.3.101)")
    if st[-1] == "a" and aff and aff[0] == "a":
        aff = aff[1:]; path.append("a + a → a (6.1.97)")
    if st[-1] == "a" and aff and aff[0] == "ā":
        st[-1] = "ā"; aff = aff[1:]; path.append("a + ā → ā (6.1.101)")
    return "".join(st + aff), path


def lin(stem, code, up, stages=LIN_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    st = list(stem)
    path = [f"{up} → {''.join(aff)} (vidhi-liṅ, 3.3.161)"]
    if "3.4.108" in on and up == "jhi":
        aff = ["u", "s"]; path.append("jhi → jus (3.4.108)")
    if "3.4.101" in on and up in SUBST_101:
        aff = list(SUBST_101[up]); path.append(f"{up} → {''.join(aff)} (3.4.101)")
    if "3.4.100" in on and up in ("tip", "sip") and aff[-1] == "i":
        aff = aff[:-1]; path.append("final i dropped (3.4.100; ṅit by 3.4.103)")
    if "3.4.99" in on and up in ("vas", "mas"):
        aff = aff[:-1]; path.append("s dropped (3.4.99)")
    if "3.4.103" in on:
        ys = list(its("yāsu~ṭ", "agama")["remaining_sounds"])          # yās
        assert placement("yāsu~ṭ") == "before"
        aff = ys + aff; path.append("yāsuṭ prefixed, ṅit (3.4.103; 1.1.46)")
        if "7.2.79" in on:
            aff = [x for i, x in enumerate(aff) if not (x == "s" and i == 2)]; path.append("non-final s of yās dropped (7.2.79)")
        if "7.2.80" in on and st[-1] == "a" and aff[:2] == ["y", "ā"]:
            aff = ["i", "y"] + aff[2:]; path.append("yā → iy after a (7.2.80 ato yeyaḥ)")
            if "6.1.66" in on and len(aff) > 2 and aff[2] in VAL:
                aff = ["i"] + aff[2:]; path.append("y dropped before val (6.1.66)")
    elif "7.3.101" in on and st[-1] == "a" and aff and aff[0] in ("v", "m"):
        st[-1] = "ā"; path.append("a → ā before va / ma (7.3.101)")
    if "6.1.97" in on and st[-1] == "a" and aff and aff[0] in ("i", "e", "o"):
        st[-1] = {"i": "e", "e": "e", "o": "o"}[aff[0]]; aff = aff[1:]; path.append("a + i → e (6.1.97 ato guṇe)")
    word_ = st + aff
    if word_[-1] == "s" and "8.2.66" in on:
        word_[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            word_[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(word_), path


def paradigm(fn, stem, stages) -> dict[str, str]:
    return {c: fn(stem, c, up, stages)[0] for c, up in TING_P}


def _ablate(fn, stem, oracle, stages, expected):
    broken = {}
    for s in expected:
        f = paradigm(fn, stem, tuple(x for x in stages if x != s))
        broken[s] = sorted(c for c in oracle if f[c] != oracle[c])
    return broken, {f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v)) if v else 'nothing'}_break": set(broken[s]) == v for s, v in expected.items()}


def t1_lot() -> dict[str, Any]:
    stems = {"bhū": present_stem(BHU), "gam": present_stem(GAM), "nī": present_stem(NI)}
    forms = {r: paradigm(lot, s, LOT_STAGES) for r, s in stems.items()}
    exp = {"3.4.85": {"3d", "2d", "2p", "1d", "1p"}, "3.4.86": {"3s", "3p"}, "3.4.87": {"2s"}, "6.4.105": {"2s"}, "3.4.89": {"1s"}, "3.4.92": {"1s"},   # without āṭ, 7.3.101 gives the same surface bhavāva / bhavāma: 3.4.92 is surface-load-bearing on 1s only (recorded)
           "3.4.101": {"3d", "2d", "2p"}, "3.4.99": {"1d", "1p"}, "7.1.3": {"3p"}, "7.3.101": set()}
    broken, checks = _ablate(lot, stems["bhū"], LOT["bhū"], LOT_STAGES, exp)
    return {"checks": {"lot_27_forms_equal_the_classical_paradigms": forms == LOT, **checks}, "forms": forms, "paths_bhu": {c: lot(stems["bhū"], c, up)[1] for c, up in TING_P}, "broken_cells": broken}


def t2_lin() -> dict[str, Any]:
    stems = {"bhū": present_stem(BHU), "gam": present_stem(GAM), "nī": present_stem(NI)}
    forms = {r: paradigm(lin, s, LIN_STAGES) for r, s in stems.items()}
    exp = {"3.4.103": set(LIN["bhū"]), "7.2.79": set(LIN["bhū"]), "7.2.80": set(LIN["bhū"]), "6.1.66": {"3s", "3d", "2s", "2d", "2p", "1d", "1p"}, "3.4.108": {"3p"},
           "6.1.97": set(LIN["bhū"]), "7.3.101": set(), "3.4.100": {"3s", "2s"}, "3.4.101": {"3d", "2d", "2p", "1s"}, "3.4.99": {"1d", "1p"}, "8.2.66": {"3p", "2s"}}
    broken, checks = _ablate(lin, stems["bhū"], LIN["bhū"], LIN_STAGES, exp)
    return {"checks": {"lin_27_forms_equal_the_classical_paradigms": forms == LIN, **checks}, "forms": forms, "paths_bhu": {c: lin(stems["bhū"], c, up)[1] for c, up in TING_P}, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lot": t1_lot(), "t2_lin": t2_lin()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_LOT_LIN_PARASMAIPADA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_LOT_LIN_PARASMAIPADA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.lot_lin_parasmaipada_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": {"lot": list(LOT_STAGES), "lin": list(LIN_STAGES)},
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "loṭ parasmaipada of bhū, gam, nī (27 forms) on theorum/58's stems by 3.4.85 (inheriting 3.4.100 / 101 / 99), 3.4.86, 3.4.87 with 6.4.105, 3.4.89, 3.4.92 (āṭ by theorum/82's placement), 7.1.3; each stage breaks exactly its cells",
                "vidhi-liṅ parasmaipada (27 forms) by 3.4.103 yāsuṭ (ṅit), 3.4.108 jus, 7.2.79, 7.2.80, 6.1.66, 6.1.97; each stage breaks exactly its cells; 7.3.101 is blocked by the intervening yāsuṭ (bhaveva): removing it changes nothing",
            ],
            "NOT_claimed": ["ātmanepada loṭ / liṅ (3.4.90, 3.4.93, sīyuṭ 3.4.102), āśīr-liṅ (3.4.104, 3.4.116), 3.4.88 vā chandasi, roots outside theorum/58's three", "stage orders are declared pipelines", "RH, YM untouched"],
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
