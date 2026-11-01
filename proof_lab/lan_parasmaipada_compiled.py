from __future__ import annotations

"""Exact certificate (theorum/95): LAṄ (THE IMPERFECT) PARASMAIPADA COMPILED ON
theorum/58's STEMS — bhū, gam, nī; the aṭ augment placed by theorum/82's
marker reading; the ṅit ending substitutions 3.4.99–101 and 7.1.3 / 8.2.23.

Quoted sūtras:
 3.2.111  anadyatane laṅ                         laṅ for the past not of today
 3.4.78   tiptasjhi sipthastha mibvasmas …        the tiṅ endings
 1.3.78   śeṣāt kartari parasmaipadam             parasmaipada in the agent voice (the rest)
 3.4.113  tiṅśit sārvadhātukam (theorum/58)       3.1.68 kartari śap (theorum/58)
 6.4.71   luṅlaṅlṛṅkṣv aḍ udāttaḥ                  the augment aṭ before luṅ, laṅ, lṛṅ (1.1.46: ṭit → prefixed; theorum/82)
 3.4.100  itaś ca                                 the i of a ṅit (lakāra) ending drops
 3.4.101  tasthasthamipāṁ tāṁtaṁtāmaḥ             tas, thas, tha, mip → tām, tam, ta, am
 3.4.99   nityaṁ ṅitaḥ                            the s of vas / mas drops always after a ṅit lakāra
 7.1.3    jho 'ntaḥ                               jh of an ending → ant
 8.2.23   saṁyogāntasya lopaḥ                     a pada-final cluster loses its last sound (ant → an)
 7.3.101  ato dīrgho yañi                          a → ā before a yañ-initial sārvadhātuka (va, ma)
 8.2.66   sasajuṣo ruḥ ; 8.3.15                    abhavaḥ
 1.3.2–1.3.9 (theorum/82)

 T1  bhū, gam, nī: 27 forms (abhavat … abhavāma; agacchat … agacchāma; anayat
     … anayāma) from theorum/58's derived present stems (śap, guṇa, ayādi,
     7.3.77 / 6.1.73 / 8.4.40) with the laṅ endings; each stage breaks exactly
     its cells: 6.4.71 all nine, 3.4.100 {3s, 2s, 3p}, 3.4.101 {3d, 2d, 2p,
     1s}, 3.4.99 {1d, 1p}, 7.1.3 and 8.2.23 {3p}, 7.3.101 {1d, 1p}, 8.2.66 {2s}.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its, placement
from proof_lab.paninian_seam_calculus import GAM, NI, derive, word

SOURCES = {
    "3.2.111": "anadyatane laṅ", "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "1.3.78": "śeṣāt kartari parasmaipadam",
    "3.4.113": "tiṅśit sārvadhātukam", "3.1.68": "kartari śap", "6.4.71": "luṅlaṅlṛṅkṣv aḍ udāttaḥ", "1.1.46": "ādyantau ṭakitau", "3.4.100": "itaś ca",
    "3.4.101": "tasthasthamipāṁ tāṁtaṁtāmaḥ", "3.4.99": "nityaṁ ṅitaḥ", "7.1.3": "jho 'ntaḥ", "8.2.23": "saṁyogāntasya lopaḥ", "7.3.101": "ato dīrgho yañi",
    "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
TING_P = [("3s", "tip"), ("3d", "tas"), ("3p", "jhi"), ("2s", "sip"), ("2d", "thas"), ("2p", "tha"), ("1s", "mip"), ("1d", "vas"), ("1p", "mas")]
CODE58 = {"S": "ś", "A": "ā", "I": "ī", "U": "ū", "R": "ṛ", "N": "ṅ", "J": "ñ", "F": "ṇ", "T": "ṭ", "z": "ṣ"}
BHU = word((("b", "h", "U"), {"root"}), (("S", "a", "p"), {"affix"}), (("t", "i", "p"), {"affix", "tiN"}))
ORACLE = {
    "bhū": {"3s": "abhavat", "3d": "abhavatām", "3p": "abhavan", "2s": "abhavaḥ", "2d": "abhavatam", "2p": "abhavata", "1s": "abhavam", "1d": "abhavāva", "1p": "abhavāma"},
    "gam": {"3s": "agacchat", "3d": "agacchatām", "3p": "agacchan", "2s": "agacchaḥ", "2d": "agacchatam", "2p": "agacchata", "1s": "agaccham", "1d": "agacchāva", "1p": "agacchāma"},
    "nī": {"3s": "anayat", "3d": "anayatām", "3p": "anayan", "2s": "anayaḥ", "2d": "anayatam", "2p": "anayata", "1s": "anayam", "1d": "anayāva", "1p": "anayāma"},
}
ALL_STAGES = ("6.4.71", "3.4.100", "3.4.101", "3.4.99", "7.1.3", "8.2.23", "7.3.101", "8.2.66", "8.3.15")
SUBST_101 = {"tas": ("t", "ā", "m"), "thas": ("t", "a", "m"), "tha": ("t", "a"), "mip": ("a", "m")}


def present_stem(w) -> tuple[str, ...]:
    """theorum/58's derived present stem (root + śap after 1.3.9, 3.4.113, 7.3.77, 6.1.73, 8.4.40, 7.3.84, 6.1.78): the first two morphemes."""
    d = derive(w)
    return tuple(CODE58.get(s, s) for m in d[:2] for s in m[0])


def lan(stem: tuple[str, ...], code: str, up: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = its(up, "pratyaya", vibhakti=True)
    aff = list(r["remaining_sounds"])
    st = list(stem)
    path = [f"{up} → {''.join(aff)} (laṅ: ṅit, 3.2.111; parasmaipada 1.3.78)"]
    # ending substitutions under the ṅit lakāra
    if "3.4.101" in on and up in SUBST_101:
        aff = list(SUBST_101[up]); path.append(f"{up} → {''.join(aff)} (3.4.101)")
    if "7.1.3" in on and up == "jhi":
        aff = ["a", "n", "t"] + aff[1:]; path.append("jh → ant (7.1.3)")
    if "3.4.100" in on and up in ("tip", "sip", "jhi") and aff[-1] == "i":
        aff = aff[:-1]; path.append("final i dropped (3.4.100 itaś ca)")
    if "3.4.99" in on and up in ("vas", "mas"):
        aff = aff[:-1]; path.append("s dropped (3.4.99 nityaṁ ṅitaḥ)")
    # 7.3.101: a → ā before yañ-initial sārvadhātuka (va, ma)
    if "7.3.101" in on and st[-1] == "a" and aff and aff[0] in ("v", "m") and up in ("vas", "mas"):
        st[-1] = "ā"; path.append("a → ā before va / ma (7.3.101)")
    # seam: a + a → a (6.1.97 ato guṇe) for am / ant
    if st[-1] == "a" and aff and aff[0] == "a":
        aff = aff[1:]; path.append("a + a → a (6.1.97 ato guṇe)")
    # aṭ augment
    if "6.4.71" in on:
        at = its("aṭ", "agama")
        assert placement("aṭ") == "before"
        st = list(at["remaining_sounds"]) + st; path.append("aṭ prefixed (6.4.71; 1.1.46 ṭit → ādi)")
    word_ = st + aff
    if "8.2.23" in on and len(word_) >= 2 and word_[-1] == "t" and word_[-2] == "n" and up == "jhi":
        word_ = word_[:-1]; path.append("pada-final cluster nt → n (8.2.23)")
    if word_[-1] == "s" and "8.2.66" in on:
        word_[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            word_[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(word_), path


def paradigm(stem, stages=ALL_STAGES) -> dict[str, str]:
    return {c: lan(stem, c, up, stages)[0] for c, up in TING_P}


def t1_lan() -> dict[str, Any]:
    stems = {"bhū": present_stem(BHU), "gam": present_stem(GAM), "nī": present_stem(NI)}
    forms = {r: paradigm(s) for r, s in stems.items()}
    expected = {"6.4.71": set(ORACLE["bhū"]), "3.4.100": {"3s", "2s", "3p"}, "3.4.101": {"3d", "2d", "2p", "1s"}, "3.4.99": {"1d", "1p"}, "7.1.3": {"3p"}, "8.2.23": {"3p"},
                "7.3.101": {"1d", "1p"}, "8.2.66": {"2s"}}
    broken = {}
    for s in expected:
        f = paradigm(stems["bhū"], tuple(x for x in ALL_STAGES if x != s))
        broken[s] = sorted(c for c in ORACLE["bhū"] if f[c] != ORACLE["bhū"][c])
    checks = {"present_stems_from_theorum_58_are_bhava_gaccha_naya": ["".join(stems[r]) for r in ("bhū", "gam", "nī")] == ["bhava", "gaccha", "naya"],
              "twenty_seven_lan_forms_equal_the_classical_paradigms": forms == ORACLE}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{'_'.join(sorted(v))}_break": set(broken[s]) == v for s, v in expected.items()})
    return {"checks": checks, "stems": {r: "".join(s) for r, s in stems.items()}, "forms": forms, "paths_bhu": {c: lan(stems["bhū"], c, up)[1] for c, up in TING_P}, "broken_cells": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_lan": t1_lan()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_LAN_PARASMAIPADA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_LAN_PARASMAIPADA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.lan_parasmaipada_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "bhū, gam, nī: 27 laṅ parasmaipada forms from theorum/58's derived present stems with 6.4.71 (aṭ placed by theorum/82's marker reading), 3.4.100, 3.4.101, 3.4.99, 7.1.3, 8.2.23, 7.3.101, 8.2.66 / 8.3.15; each stage breaks exactly its cells",
            ],
            "NOT_claimed": [
                "ātmanepada laṅ, the aṭ / āṭ choice for vowel-initial roots (6.4.72), accent (udātta of 6.4.71), roots outside theorum/58's three, other lakāras (loṭ, liṅ, luṅ)",
                "the stage order is a declared pipeline",
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
