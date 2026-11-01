from __future__ import annotations

"""Exact certificate (theorum/101): LUṄ (THE AORIST) PARASMAIPADA COMPILED — three
aorist shapes on three pinned roots: bhū with the luk of sic (2.4.77) and vuk
(6.4.88), gam with aṅ (3.1.55: the ḷ-it of gamḷ~ read by theorum/82 is
load-bearing), nī with sic, vṛddhi (7.2.1), īṭ (7.3.96), ṣatva / ṣṭutva and
jus (3.4.109).

Quoted sūtras:
 3.2.110  luṅ                                   3.1.43  cli luṅi ; 3.1.44 cleḥ sic
 3.1.55   puṣādidyutādyḷditaḥ parasmaipadeṣu    aṅ (for cli) after puṣādi, dyutādi and ḷdit roots in parasmaipada
 2.4.77   gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu   sic is luk after gā, sthā, ghu, pā, bhū
 6.4.88   bhuvo vug luṅliṭoḥ                     bhū takes vuk before a vowel-initial luṅ / liṭ ending
 7.2.1    sici vṛddhiḥ parasmaipadeṣu            vṛddhi of the ik-final aṅga before sic
 7.3.96   astisico 'pṛkte                        īṭ before a single-sound ending after as / sic
 8.3.59   ādeśapratyayayoḥ ; 8.4.41 ṣṭunā ṣṭuḥ    anaiṣīt, anaiṣṭām
 3.4.109  sijabhyastavidibhyaś ca                jhi → jus after sic
 6.4.71 ; 3.4.100 ; 3.4.101 ; 3.4.99 ; 7.1.3 ; 8.2.23 ; 7.3.101 ; 7.2.10 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9

 T1  abhūt abhūtām abhūvan / abhūḥ abhūtam abhūta / abhūvam abhūva abhūma ;
     agamat agamatām agaman / agamaḥ agamatam agamata / agamam agamāva agamāma ;
     anaiṣīt anaiṣṭām anaiṣuḥ / anaiṣīḥ anaiṣṭam anaiṣṭa / anaiṣam anaiṣva anaiṣma
     — 27 forms; each stage breaks exactly its cells; 3.1.55 breaks all of gam
     and nothing else, 2.4.77 all of bhū, 6.4.88 {3p, 1s} of bhū, 7.2.1 / 7.3.96 /
     3.4.109 their cells of nī.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import BASE, VRDDHI_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its, placement

SOURCES = {
    "3.2.110": "luṅ", "3.1.43": "cli luṅi", "3.1.44": "cleḥ sic", "3.1.55": "puṣādidyutādyḷditaḥ parasmaipadeṣu", "2.4.77": "gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu",
    "6.4.88": "bhuvo vug luṅliṭoḥ", "7.2.1": "sici vṛddhiḥ parasmaipadeṣu", "7.3.96": "astisico 'pṛkte", "8.3.59": "ādeśapratyayayoḥ", "8.4.41": "ṣṭunā ṣṭuḥ",
    "3.4.109": "sijabhyastavidibhyaś ca", "6.4.71": "luṅlaṅlṛṅkṣv aḍ udāttaḥ", "3.4.100": "itaś ca", "3.4.101": "tasthasthamipāṁ tāṁtaṁtāmaḥ", "3.4.99": "nityaṁ ṅitaḥ",
    "7.1.3": "jho 'ntaḥ", "8.2.23": "saṁyogāntasya lopaḥ", "7.3.101": "ato dīrgho yañi", "7.2.10": "ekāca upadeśe 'nudāttāt", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
TING_P = [("3s", "tip"), ("3d", "tas"), ("3p", "jhi"), ("2s", "sip"), ("2d", "thas"), ("2p", "tha"), ("1s", "mip"), ("1d", "vas"), ("1p", "mas")]
ROOTS = {"bhū": "bhū", "gam": "gamḷ~", "nī": "ṇīñ"}
IK = {"i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R"}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "o", "au")
SUBST_101 = {"tas": ("t", "ā", "m"), "thas": ("t", "a", "m"), "tha": ("t", "a"), "mip": ("a", "m")}
ORACLE = {"bhū": {"3s": "abhūt", "3d": "abhūtām", "3p": "abhūvan", "2s": "abhūḥ", "2d": "abhūtam", "2p": "abhūta", "1s": "abhūvam", "1d": "abhūva", "1p": "abhūma"},
          "gam": {"3s": "agamat", "3d": "agamatām", "3p": "agaman", "2s": "agamaḥ", "2d": "agamatam", "2p": "agamata", "1s": "agamam", "1d": "agamāva", "1p": "agamāma"},
          "nī": {"3s": "anaiṣīt", "3d": "anaiṣṭām", "3p": "anaiṣuḥ", "2s": "anaiṣīḥ", "2d": "anaiṣṭam", "2p": "anaiṣṭa", "1s": "anaiṣam", "1d": "anaiṣva", "1p": "anaiṣma"}}
ALL_STAGES = ("3.1.44", "3.1.55", "2.4.77", "6.4.71", "3.4.100", "3.4.101", "3.4.99", "7.1.3", "3.4.109", "8.2.23", "7.2.1", "7.3.96", "8.3.59", "8.4.41", "6.4.88", "7.3.101", "8.2.66", "8.3.15")


def root_sounds(name):
    r = its(ROOTS[name], "dhatu")
    s = list(r["remaining_sounds"])
    if s[0] == "ṇ":
        s[0] = "n"
    return s, r["its"]


def lun(name: str, code: str, up: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st, marks = root_sounds(name)
    aff = list(its(up, "pratyaya", vibhakti=True)["remaining_sounds"])
    path = [f"{ROOTS[name]} → {''.join(st)} (its {marks}); {up} → {''.join(aff)} (luṅ: ṅit)"]
    # the cli: sic (3.1.44), replaced by aṅ for ḷdit roots (3.1.55), luk after bhū (2.4.77)
    vik: list[str] = []
    if "3.1.44" in on:
        vik = ["s"]; path.append("cli → sic (3.1.43, 3.1.44)")
        if "3.1.55" in on and "ḷ" in marks:
            vik = ["a"]; path.append("sic → aṅ: the root is ḷdit (3.1.55; the ḷ-it read by 1.3.2)")
        elif "2.4.77" in on and name == "bhū":
            vik = []; path.append("sic → luk after bhū in parasmaipada (2.4.77)")
    sic = vik == ["s"]
    # endings under the ṅit lakāra
    if "3.4.101" in on and up in SUBST_101:
        aff = list(SUBST_101[up]); path.append(f"{up} → {''.join(aff)} (3.4.101)")
    if up == "jhi":
        if sic and "3.4.109" in on:
            aff = ["u", "s"]; path.append("jhi → jus after sic (3.4.109)")
        elif "7.1.3" in on:
            aff = ["a", "n", "t"] + aff[1:]; path.append("jh → ant (7.1.3)")
    if "3.4.100" in on and up in ("tip", "sip", "jhi") and aff and aff[-1] == "i":
        aff = aff[:-1]; path.append("final i dropped (3.4.100)")
    if "3.4.99" in on and up in ("vas", "mas"):
        aff = aff[:-1]; path.append("s dropped (3.4.99)")
    # sic: vṛddhi, īṭ, ṣatva, ṣṭutva
    if sic:
        if "7.2.1" in on and st[-1] in IK:
            v = rapara_1_1_51(BASE[IK[st[-1]]], antaratama(IK[st[-1]], VRDDHI_SET))
            st = st[:-1] + list(v); path.append(f"vṛddhi before sic in parasmaipada (7.2.1; 1.1.50) → {''.join(st)}")
        if "7.3.96" in on and len(aff) == 1 and aff[0] not in VOWELS:
            aff = ["ī"] + aff; path.append("īṭ before the single-sound ending after sic (7.3.96 astisico 'pṛkte)")
        if "8.3.59" in on and st[-1] in ("i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au"):
            vik = ["ṣ"]; path.append("s → ṣ after iṇ (8.3.59)")
        if "8.4.41" in on and vik == ["ṣ"] and aff and aff[0] == "t":
            aff[0] = "ṭ"; path.append("t → ṭ after ṣ (8.4.41 ṣṭunā ṣṭuḥ)")
    # bhū's vuk before a vowel-initial ending
    if name == "bhū" and not vik and "6.4.88" in on and aff and aff[0] in VOWELS:
        st = st + ["v"]; path.append("vuk before the vowel-initial luṅ ending (6.4.88)")
    # aṅ stem: a + a, 7.3.101
    stem = st + vik
    if "7.3.101" in on and stem[-1] == "a" and aff and aff[0] in ("v", "m") and up in ("vas", "mas"):
        stem[-1] = "ā"; path.append("a → ā before va / ma (7.3.101)")
    if stem[-1] == "a" and aff and aff[0] == "a":
        aff = aff[1:]; path.append("a + a → a (6.1.97)")
    if "6.4.71" in on:
        assert placement("aṭ") == "before"
        stem = ["a"] + stem; path.append("aṭ prefixed (6.4.71; 1.1.46)")
    w = stem + aff
    if "8.2.23" in on and len(w) >= 2 and w[-1] == "t" and w[-2] == "n" and up == "jhi":
        w = w[:-1]; path.append("nt → n at pada end (8.2.23)")
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(w), path


def paradigm(name, stages=ALL_STAGES) -> dict[str, str]:
    return {c: lun(name, c, up, stages)[0] for c, up in TING_P}


def t1_lun() -> dict[str, Any]:
    forms = {r: paradigm(r) for r in ROOTS}
    exp = {"bhū": {"2.4.77": set(ORACLE["bhū"]), "6.4.88": {"3p", "1s"}, "6.4.71": set(ORACLE["bhū"]), "3.1.55": set(), "7.2.1": set(), "7.3.96": set()},
           "gam": {"3.1.55": set(ORACLE["gam"]), "2.4.77": set(), "7.3.101": {"1d", "1p"}, "7.1.3": {"3p"}, "8.2.23": {"3p"}},
           "nī": {"7.2.1": set(ORACLE["nī"]), "7.3.96": {"3s", "2s"}, "8.3.59": set(ORACLE["nī"]), "8.4.41": {"3d", "2d", "2p"}, "3.4.109": {"3p"}, "3.1.44": set(ORACLE["nī"]), "2.4.77": set(), "3.1.55": set()}}
    broken, checks = {}, {}
    for r, table in exp.items():
        for s, v in table.items():
            f = paradigm(r, tuple(x for x in ALL_STAGES if x != s))
            broken[f"{r}:{s}"] = sorted(c for c in ORACLE[r] if f[c] != ORACLE[r][c])
            checks[f"{r}_without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v)) if v else 'nothing'}_break"] = set(broken[f"{r}:{s}"]) == v
    return {"checks": {"lun_27_forms_equal_the_classical_paradigms": forms == ORACLE, **checks}, "forms": forms, "paths": {r: {c: lun(r, c, up)[1] for c, up in TING_P} for r in ROOTS}, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lun": t1_lun()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_LUN_PARASMAIPADA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_LUN_PARASMAIPADA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.lun_parasmaipada_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "luṅ parasmaipada of bhū (sic-luk 2.4.77, vuk 6.4.88), gam (aṅ 3.1.55 by its ḷ-it) and nī (sic with 7.2.1 vṛddhi by theorum/80's antaratama, 7.3.96 īṭ, 8.3.59, 8.4.41, 3.4.109 jus): 27 forms; each stage breaks exactly its cells on exactly the root it governs",
            ],
            "NOT_claimed": ["the other aorist shapes (ksa, cāṅ, ciṇ, the siṣ / sa aorists), ātmanepada luṅ, the puṣādi / dyutādi gaṇas beyond the ḷdit test, 6.4.72, accent, other roots", "stage order a declared pipeline", "RH, YM untouched"],
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
