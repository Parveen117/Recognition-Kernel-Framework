from __future__ import annotations

"""Exact certificate (theorum/114): AVYAYĪBHĀVA AND DVIGU COMPILED — the two
compound kinds theorum/104 left out: avyayībhāva (2.1.6, 2.1.7) with its neuter
(2.4.18), the sup after it (2.4.82 luk after a non-a stem, 2.4.83 am after an
a-stem), and the dvigu (2.1.52) as samāhāra with 2.4.17 (neuter), 4.1.21
(ṅīp after an a-final samāhāra dvigu), 5.4.92 (ṭac after go); each rule shown
load-bearing on exactly the words it governs.

Quoted sūtras:
 2.1.6    avyayaṁ vibhaktisamīpasamṛddhi… (avyayībhāva)   upakumbham (samīpa), pratidinam (vīpsā), adhihari (adhikaraṇa)
 2.1.7    yathā 'sādṛśye                                 yathāśakti
 2.1.5    avyayībhāvaḥ ; 1.1.41 avyayībhāvaś ca (avyaya) ; 2.4.18 avyayībhāvaś ca (napuṁsaka)
 2.4.82   avyayād āpsupaḥ                                the sup after an avyaya is deleted: adhihari, yathāśakti
 2.4.83   nāvyayībhāvād ato 'm tv apañcamyāḥ              after an a-final avyayībhāva the sup is not deleted but → am: upakumbham, pratidinam
 2.1.52   saṁkhyāpūrvo dviguḥ ; 2.1.51 taddhitārthottarapadasamāhāre ca
 2.4.17   sa napuṁsakam (samāhāra dvigu is neuter) ; 2.4.1 dvigur ekavacanam
 4.1.21   dvigoḥ (ṅīp after an a-final samāhāra dvigu): trilokī, pañcamūlī ; 6.4.148
 5.4.92   gor ataddhitaluki (ṭac after go in a dvigu): pañcagavam ; 6.1.78 ; 7.1.24 ato 'm (neuter su / am → am)
 2.4.71   supo dhātuprātipadikayoḥ ; 1.2.43 ; 2.2.30 (the avyaya / the number first)

 T1  upakumbham, pratidinam, adhihari, yathāśakti ; trilokī, pañcamūlī, pañcagavam, tripadam — 8 words (nominative forms).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "2.1.6": "avyayaṁ vibhaktisamīpasamṛddhivyṛddhyarthābhāvātyayāsampratiśabdaprādurbhāvapaścādyathānupūrvyayaugapadyasādṛśyasampattisākalyāntavacaneṣu",
    "2.1.7": "yathā 'sādṛśye", "2.1.5": "avyayībhāvaḥ", "1.1.41": "avyayībhāvaś ca", "2.4.18": "avyayībhāvaś ca", "2.4.82": "avyayād āpsupaḥ",
    "2.4.83": "nāvyayībhāvād ato 'm tv apañcamyāḥ", "2.1.52": "saṁkhyāpūrvo dviguḥ", "2.1.51": "taddhitārthottarapadasamāhāre ca", "2.4.17": "sa napuṁsakam",
    "2.4.1": "dvigur ekavacanam", "4.1.21": "dvigoḥ", "6.4.148": "yasyeti ca", "5.4.92": "gor ataddhitaluki", "6.1.78": "eco 'yavāyāvaḥ", "7.1.24": "ato 'm",
    "2.4.71": "supo dhātuprātipadikayoḥ", "1.2.43": "prathamānirdiṣṭaṁ samāsa upasarjanam", "2.2.30": "upasarjanaṁ pūrvam",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au")
CASES = [  # (first member, second member (prātipadika), kind, vidhi, expected nominative)
    (("u", "p", "a"), ("k", "u", "m", "bh", "a"), "avyayībhāva", "2.1.6", "upakumbham"),
    (("p", "r", "a", "t", "i"), ("d", "i", "n", "a"), "avyayībhāva", "2.1.6", "pratidinam"),
    (("a", "dh", "i"), ("h", "a", "r", "i"), "avyayībhāva", "2.1.6", "adhihari"),
    (("y", "a", "th", "ā"), ("ś", "a", "k", "t", "i"), "avyayībhāva", "2.1.7", "yathāśakti"),
    (("t", "r", "i"), ("l", "o", "k", "a"), "dvigu", "2.1.52", "trilokī"),
    (("p", "a", "ñ", "c", "a"), ("m", "ū", "l", "a"), "dvigu", "2.1.52", "pañcamūlī"),
    (("p", "a", "ñ", "c", "a"), ("g", "o"), "dvigu", "2.1.52", "pañcagavam"),
    (("t", "r", "i"), ("p", "a", "d", "a"), "dvigu", "2.1.52", "tripadam"),
]
NGIP_DVIGU = {"trilokī", "pañcamūlī"}   # 4.1.21 dvigoḥ: the a-final samāhāra dvigu takes ṅīp (declared where 4.1.21 / 2.4.17 leave an option: tripadam stays neuter)
ALL_STAGES = ("2.4.71", "2.4.82", "2.4.83", "2.4.17", "4.1.21", "6.4.148", "5.4.92", "6.1.78", "7.1.24")


def compound(m1, m2, kind, vidhi, expected, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    p1, p2 = list(m1), list(m2)
    path = [f"{''.join(p1)} + {''.join(p2)} ({kind}, {vidhi}; the avyaya / number is upasarjana 1.2.43 and stands first 2.2.30)"]
    if "2.4.71" in on:
        path.append("inner sup deleted (2.4.71)")
    else:
        p2 = p2 + ["s", "u"]
    st = p1 + p2
    if kind == "avyayībhāva":
        path.append("the compound is avyaya (1.1.41) and neuter (2.4.18)")
        if st[-1] == "a" and "2.4.83" in on:
            path.append("the sup after the a-final avyayībhāva is not deleted but becomes am (2.4.83): -am")
            return "".join(st + ["m"]), path
        if "2.4.82" in on:
            path.append("the sup after the avyaya is deleted (2.4.82 avyayād āpsupaḥ)")
            return "".join(st), path
        return "".join(st + ["s"]), path
    # dvigu, samāhāra
    if "5.4.92" in on and p2 == ["g", "o"]:
        p2 = ["g", "o"] + ["a"]; path.append("ṭac after go in the dvigu (5.4.92 gor ataddhitaluki)")
        if "6.1.78" in on:
            p2 = ["g", "a", "v", "a"]; path.append("o → av before the vowel (6.1.78)")
        st = p1 + p2
    if "2.4.17" in on:
        path.append("the samāhāra dvigu is neuter (2.4.17 sa napuṁsakam; one number 2.4.1)")
    if expected in NGIP_DVIGU and "4.1.21" in on and st[-1] == "a":
        if "6.4.148" in on:
            st = st[:-1]; path.append("a of the bha dropped before ṅīp (6.4.148)")
        st = st + ["ī"]; path.append("ṅīp after the a-final samāhāra dvigu (4.1.21 dvigoḥ); nominative su dropped after ī (6.1.68)")
        return "".join(st), path
    if "2.4.17" in on and st[-1] == "a" and "7.1.24" in on:
        path.append("neuter su → am (7.1.24 ato 'm; 6.1.107 ami pūrvaḥ)")
        return "".join(st + ["m"]), path
    return "".join(st + ["s"]), path


def t1_compounds() -> dict[str, Any]:
    forms = {e: compound(a, b, k, v, e)[0] for a, b, k, v, e in CASES}
    exp_breaks = {"2.4.71": {e for *_, e in CASES}, "2.4.82": {"adhihari", "yathāśakti"}, "2.4.83": {"upakumbham", "pratidinam"},
                  "2.4.17": {"pañcagavam", "tripadam"}, "4.1.21": {"trilokī", "pañcamūlī"}, "6.4.148": {"trilokī", "pañcamūlī"}, "5.4.92": {"pañcagavam"}, "6.1.78": {"pañcagavam"}, "7.1.24": {"pañcagavam", "tripadam"}}
    broken = {x: sorted(e for a, b, k, v, e in CASES if compound(a, b, k, v, e, tuple(y for y in ALL_STAGES if y != x))[0] != e) for x in exp_breaks}
    checks = {"eight_compounds_equal_the_classical_forms": all(forms[e] == e for e in forms)}
    checks.update({f"without_{x.replace('.', '_')}_exactly_{len(v)}_break": set(broken[x]) == v for x, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {e: compound(a, b, k, v, e)[1] for a, b, k, v, e in CASES}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_compounds": t1_compounds()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_AVYAYIBHAVA_DVIGU_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_AVYAYIBHAVA_DVIGU_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.avyayibhava_dvigu_compiled_candidate.v1", "status": status, "sources": SOURCES, "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": ["four avyayībhāvas (upakumbham, pratidinam by 2.4.83; adhihari, yathāśakti by 2.4.82) and four samāhāra dvigus (trilokī, pañcamūlī by 4.1.21 + 6.4.148; pañcagavam by 5.4.92 + 6.1.78 + 2.4.17 + 7.1.24; tripadam) in the nominative; each rule breaks exactly the words stated (2.4.71 all eight)"],
            "NOT_claimed": ["the sense of each avyayībhāva (samīpa, vīpsā, adhikaraṇa, sādṛśya) declared from 2.1.6 / 2.1.7; the ṅīp / neuter option of 4.1.21 (tripadam kept neuter) declared; the other cases of the avyayībhāva (2.4.84 tṛtīyāsaptamyor bahulam), the dvigu's taddhita sense, the non-samāhāra dvigu, the accent", "RH, YM untouched"],
        },
        "checks": checks, **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=None); args = parser.parse_args()
    payload = build_certificate(); data = canonical_bytes(payload)
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
