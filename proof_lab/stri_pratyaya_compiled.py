from __future__ import annotations

"""Exact certificate (theorum/111): THE FEMININE AFFIXES COMPILED — ṭāp (4.1.4)
with 7.3.44 (kārikā), ṅīp after ugit (4.1.6; 7.1.81 for the śatṛ after śap:
bhavantī), ṅīp after ṇit / ñit taddhitas (4.1.15) and yañ (4.1.16, with
6.4.150), ṅīṣ after the gaurādi (4.1.41), the bha operations 6.4.148; the
feminine stems then declined on theorum/88 (ā) and theorum/89 (ī); each rule
shown load-bearing on exactly the stems it governs.

Quoted sūtras:
 4.1.3    striyām ; 4.1.1 ṅyāp-prātipadikāt                  the feminine adhikāra
 4.1.4    ajādyataṣ ṭāp                                     ṭāp after an a-final stem: bālā, devā, ajā
 7.3.44   pratyayasthāt kāt pūrvasyāta id āpy asupaḥ       a before an affixal k → i before āp: kārikā, pācikā, nāyikā
 4.1.6    ugitaś ca                                         ṅīp after an ugit: bhavantī, dhīmatī, bhagavatī
 7.1.81   śapśyanor nityam                                  the śatṛ after śap always takes num before ṅī: bhavantī (not *bhavatī)
 4.1.15   ṭiḍḍhāṇañdvayasajdaghnañmātractayapṭhakṭhañkañkvarapaḥ     ṅīp after ṇit / ñit / ṭhak taddhitas: aupagavī, śaivī, dākṣī, paurāṇikī
 4.1.16   yañaś ca ; 6.4.150 halas taddhitasya             gārgī (the y of yañ dropped after a consonant before ī)
 4.1.41   ṣidgaurādibhyaś ca                                ṅīṣ: gaurī
 6.4.148  yasyeti ca ; 1.4.18 yaci bham                     the a / i of the bha dropped before ī
 1.3.3    halantyam (p of ṭāp, ṅīp, ṣ of ṅīṣ) ; 1.3.7 cuṭū (ṭ of ṭāp, ṅ of ṅīp) ; 1.3.6 ṣaḥ pratyayasya ; 1.3.9

 T1  13 feminine stems ; T2  bālā, kārikā on theorum/88 and bhavantī, gārgī on theorum/89 (1s, 3s, 6p).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.ap_stem_sup_compiled import paradigm as ap_paradigm
from proof_lab.ghi_stem_sup_compiled import natva_8_4_2
from proof_lab.ngi_stem_sup_compiled import paradigm as ngi_paradigm
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "4.1.3": "striyām", "4.1.1": "ṅyāpprātipadikāt", "4.1.4": "ajādyataṣ ṭāp", "7.3.44": "pratyayasthāt kāt pūrvasyāta id āpy asupaḥ",
    "4.1.6": "ugitaś ca", "7.1.81": "śapśyanor nityam", "4.1.15": "ṭiḍḍhāṇañdvayasajdaghnañmātractayapṭhakṭhañkañkvarapaḥ", "4.1.16": "yañaś ca",
    "6.4.150": "halas taddhitasya", "4.1.41": "ṣidgaurādibhyaś ca", "6.4.148": "yasyeti ca", "1.4.18": "yaci bham",
    "8.4.2": "aṭkupvāṅnumvyavāye 'pi", "1.3.3": "halantyam", "1.3.7": "cuṭū", "1.3.6": "ṣaḥ pratyayasya", "1.3.9": "tasya lopaḥ",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "au", "o")
UK = {"u", "ṛ", "ḷ"}
# (masculine / base stem, the affix that formed it (its read by theorum/82) or None, feminine affix, expected)
CASES = [
    (("b", "ā", "l", "a"), None, "ṭāp", "bālā"), (("d", "e", "v", "a"), None, "ṭāp", "devā"), (("a", "j", "a"), None, "ṭāp", "ajā"),
    (("k", "ā", "r", "a", "k", "a"), "ṇvul", "ṭāp", "kārikā"), (("p", "ā", "c", "a", "k", "a"), "ṇvul", "ṭāp", "pācikā"), (("n", "ā", "y", "a", "k", "a"), "ṇvul", "ṭāp", "nāyikā"),
    (("bh", "a", "v", "a", "t"), "śatṛ~", "ṅīp", "bhavantī"), (("dh", "ī", "m", "a", "t"), "matu~p", "ṅīp", "dhīmatī"), (("bh", "a", "g", "a", "v", "a", "t"), "matu~p", "ṅīp", "bhagavatī"),
    (("au", "p", "a", "g", "a", "v", "a"), "aṇ", "ṅīp", "aupagavī"), (("d", "ā", "kṣ", "i"), "iñ", "ṅīp", "dākṣī"), (("g", "ā", "r", "g", "y", "a"), "yañ", "ṅīp", "gārgī"),
    (("g", "au", "r", "a"), None, "ṅīṣ", "gaurī"),
]
ALL_STAGES = ("7.3.44", "7.1.81", "6.4.150", "6.4.148")
SAP_SATR = {"śatṛ~"}   # 7.1.81: śatṛ after śap (the present stem of theorum/58 carries śap)


def feminine(stem, formed_by, aff, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st = list(stem)
    a = its(aff, "pratyaya", taddhita=False)
    fem = list(a["remaining_sounds"])
    path = [f"{''.join(st)} + {aff} → {''.join(fem)} (its {a['its']}; striyām 4.1.3)"]
    if aff == "ṭāp":
        path.append("ṭāp after the a-final stem (4.1.4 ajādyataṣ ṭāp)")
        if formed_by == "ṇvul" and st[-2] == "k" and st[-3] == "a" and "7.3.44" in on:
            st[-3] = "i"; path.append("a before the affixal k → i before āp (7.3.44 pratyayasthāt kāt pūrvasyāta id āpy asupaḥ)")
        st = st[:-1]; path.append("a + ā → ā (6.1.101 akaḥ savarṇe dīrghaḥ)")
        return "".join(st + fem), path
    # ṅīp / ṅīṣ
    if formed_by is not None:
        f = its(formed_by, "pratyaya", taddhita=formed_by in ("aṇ", "iñ", "yañ"))
        marks = f["its"]
        if any(k in UK for k in marks):
            path.append(f"ṅīp after the ugit {formed_by} (4.1.6 ugitaś ca)")
            if formed_by in SAP_SATR and "7.1.81" in on:
                k = max(i for i, s in enumerate(st) if s in VOWELS)
                st = st[: k + 1] + ["n"] + st[k + 1 :]; path.append("num always, for the śatṛ after śap, before ṅī (7.1.81 śapśyanor nityam)")
        elif formed_by == "yañ":
            path.append("ṅīp after yañ (4.1.16 yañaś ca)")
        else:
            path.append(f"ṅīp after the ṇit / ñit taddhita {formed_by} (4.1.15)")
    else:
        path.append("ṅīṣ after the gaurādi (4.1.41 ṣidgaurādibhyaś ca)")
    if formed_by == "yañ" and st[-2:] == ["y", "a"] and st[-3] not in VOWELS and "6.4.150" in on:
        st = st[:-2]; path.append("the y of the taddhita yañ dropped after the consonant before ī (6.4.150 halas taddhitasya; 6.4.148)")
    elif st[-1] in ("a", "i") and "6.4.148" in on:
        st = st[:-1]; path.append("final a / i of the bha dropped before ī (6.4.148 yasyeti ca; bha 1.4.18)")
    return "".join(st + fem), path


def t1_feminines() -> dict[str, Any]:
    forms = {e: feminine(s, f, a)[0] for s, f, a, e in CASES}
    exp_breaks = {"7.3.44": {"kārikā", "pācikā", "nāyikā"}, "7.1.81": {"bhavantī"}, "6.4.150": {"gārgī"}, "6.4.148": {"aupagavī", "dākṣī", "gaurī"}}
    broken = {x: sorted(e for s, f, a, e in CASES if feminine(s, f, a, tuple(y for y in ALL_STAGES if y != x))[0] != e) for x in exp_breaks}
    checks = {"thirteen_feminine_stems_equal_the_classical_forms": all(forms[e] == e for e in forms)}
    checks.update({f"without_{x.replace('.', '_')}_exactly_{len(v)}_break": set(broken[x]) == v for x, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {e: feminine(s, f, a)[1] for s, f, a, e in CASES}, "broken": broken}


def t2_declined() -> dict[str, Any]:
    tok = lambda w: tuple(w)
    natva = lambda par: {c: "".join(natva_8_4_2(list(w))[0]) for c, w in par.items()}   # 8.4.2 across ku (theorum/91's ṇatva; the ā / ī carriers of 88 / 89 carried no r / ṣ trigger)
    bala, karika = natva(ap_paradigm(tok("bālā"))), natva(ap_paradigm(tok("kārikā")))
    bhav, garg = natva(ngi_paradigm(tok("bhavantī"))), natva(ngi_paradigm(tok("gārgī")))
    checks = {
        "bala_on_theorum_88": (bala["1s"], bala["3s"], bala["6p"]) == ("bālā", "bālayā", "bālānām"),
        "karika_on_theorum_88": (karika["1s"], karika["3s"], karika["6p"]) == ("kārikā", "kārikayā", "kārikāṇām"),
        "bhavanti_on_theorum_89": (bhav["1s"], bhav["3s"], bhav["6p"]) == ("bhavantī", "bhavantyā", "bhavantīnām"),
        "gargi_on_theorum_89": (garg["1s"], garg["3s"], garg["6p"]) == ("gārgī", "gārgyā", "gārgīṇām"),
    }
    return {"checks": checks, "bala": bala, "karika": karika, "bhavanti": bhav, "gargi": garg}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_feminines": t1_feminines(), "t2_declined": t2_declined()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_STRI_PRATYAYA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_STRI_PRATYAYA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.stri_pratyaya_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "thirteen feminine stems by 4.1.4 (with 7.3.44), 4.1.6 (with 7.1.81), 4.1.15, 4.1.16 (with 6.4.150), 4.1.41, and 6.4.148; each rule breaks exactly the stems stated; the ugit / ṇit / ñit status of the forming affix read by theorum/82",
                "bālā, kārikā declined on theorum/88 and bhavantī, gārgī on theorum/89 (1s, 3s, 6p), with 8.4.2 across the ku applied after the carrier by theorum/91's ṇatva (kārikāṇām, gārgīṇām) — recorded, since the ā / ī carriers were certified on stems without an r / ṣ trigger",
            ],
            "NOT_claimed": [
                "the choice between ṭāp, ṅīp and ṅīṣ for a stem the sūtras do not decide here (gaurādi membership of gaura declared); 4.1.5 ṛnnebhyo ṅīp, 4.1.20–4.1.75, the ṅīn, the ūṅ, the feminine of nouns in -ṛ (mātṛ), the accent",
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
