from __future__ import annotations

"""Exact certificate (theorum/105): ṇIC CAUSATIVES COMPILED — twelve roots with
ṇic (3.1.26 hetumati ca) in laṭ parasmaipada (3s, 3p, 1s): the ṇit vṛddhi
7.2.115 / 7.2.116, the mit shortening 6.4.92, the augments puk (7.3.36) and yuk
(7.3.37), the laghūpadha guṇa 7.3.86 (with 1.1.51), then ṇi + śap by 7.3.84 and
6.1.78 and the tiṅ with 7.1.3, 6.1.97, 7.3.101; each rule shown load-bearing on
exactly the forms it governs.

Quoted sūtras:
 3.1.26   hetumati ca                              ṇic after a root in the causative sense (3.1.25 satyāpa… ṇic)
 3.1.32   sanādyantā dhātavaḥ                      the ṇijanta is a dhātu (so śap and the tiṅ follow)
 1.3.3    halantyam ; 1.3.7 cuṭū ; 1.3.9 tasya lopaḥ      ṇic → i
 7.2.115  aco ñṇiti                                vṛddhi of a final vowel before ṇic: bhau, kār, nai, hār
 7.2.116  ata upadhāyāḥ                            vṛddhi of a penultimate a: pāc, gām
 6.4.92   mitāṁ hrasvaḥ                            the mit root's penultimate stays short: gam (Dhātupāṭha gaṇasūtra: janī-jṝṣ-knasu-rañjo 'mantāś ca)
 7.3.36   artihrīvlīrīknūyīkṣmāyyātāṁ puṅ ṇau       puk after an ā-final root: sthāp, dāp
 7.3.37   śācchāsāhvāvyāvepāṁ yuk                  yuk after pā: pāy
 7.3.86   pugantalaghūpadhasya ca                  guṇa of a light penultimate ik: ved, bodh, karṣ (1.1.51)
 1.1.51   ur aṇ raparaḥ
 3.1.68   kartari śap ; 3.4.113 tiṅśit sārvadhātukam ; 1.3.78 śeṣāt kartari parasmaipadam
 7.3.84   sārvadhātukārdhadhātukayoḥ               ṇi → ṇe before śap ; 6.1.78 eco 'yavāyāvaḥ → ay
 3.4.78   tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ
 7.1.3    jho 'ntaḥ ; 6.1.97 ato guṇe ; 7.3.101 ato dīrgho yañi
 1.4.13   yasmāt pratyayavidhis tadādi pratyaye 'ṅgam

 T1  bhāvayati, kārayati, nāyayati, hārayati, pācayati, gamayati, sthāpayati,
     dāpayati, pāyayati, vedayati, bodhayati, karṣayati — each in 3s / 3p / 1s,
     36 forms.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_instruction_format import GUNA_SET, VRDDHI_SET, antaratama, rapara_1_1_51
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "3.1.26": "hetumati ca", "3.1.32": "sanādyantā dhātavaḥ", "1.3.3": "halantyam", "1.3.7": "cuṭū", "1.3.9": "tasya lopaḥ",
    "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "6.4.92": "mitāṁ hrasvaḥ",
    "7.3.36": "artihrīvlīrīknūyīkṣmāyyātāṁ puṅ ṇau", "7.3.37": "śācchāsāhvāvyāvepāṁ yuk", "7.3.86": "pugantalaghūpadhasya ca", "1.1.51": "ur aṇ raparaḥ",
    "3.1.68": "kartari śap", "3.4.113": "tiṅśit sārvadhātukam", "1.3.78": "śeṣāt kartari parasmaipadam",
    "7.3.84": "sārvadhātukārdhadhātukayoḥ", "6.1.78": "eco 'yavāyāvaḥ",
    "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "7.1.3": "jho 'ntaḥ", "6.1.97": "ato guṇe", "7.3.101": "ato dīrgho yañi",
    "1.4.13": "yasmāt pratyayavidhis tadādi pratyaye 'ṅgam",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "e", "ai", "au", "o")
TO58 = {"a": "a", "ā": "A", "i": "i", "ī": "I", "u": "u", "ū": "U", "ṛ": "R", "ṝ": "RR"}
FROM58 = {"A": "ā", "ai": "ai", "au": "au", "e": "e", "o": "o", "a": "a"}
AYADI = {"e": ("a", "y"), "o": ("a", "v"), "ai": ("ā", "y"), "au": ("ā", "v")}
MIT = {"gam"}  # Dhātupāṭha gaṇasūtra under ghaṭādi: janī-jṝṣ-knasu-rañjo 'mantāś ca — the am-final roots are mit
PUK_ROOTS = {"sthā", "dā"}  # 7.3.36 ātām: the ā-final roots (pā is taken by 7.3.37)
YUK_ROOTS = {"pā"}
ROOTS = {
    "bhū": ("bh", "ū"), "kṛ": ("k", "ṛ"), "nī": ("n", "ī"), "hṛ": ("h", "ṛ"), "pac": ("p", "a", "c"), "gam": ("g", "a", "m"),
    "sthā": ("s", "th", "ā"), "dā": ("d", "ā"), "pā": ("p", "ā"), "vid": ("v", "i", "d"), "budh": ("b", "u", "dh"), "kṛṣ": ("k", "ṛ", "ṣ"),
}
STEM_ORACLE = {"bhū": "bhāvaya", "kṛ": "kāraya", "nī": "nāyaya", "hṛ": "hāraya", "pac": "pācaya", "gam": "gamaya", "sthā": "sthāpaya",
               "dā": "dāpaya", "pā": "pāyaya", "vid": "vedaya", "budh": "bodhaya", "kṛṣ": "karṣaya"}
CELLS = [("3s", "tip"), ("3p", "jhi"), ("1s", "mip")]
ALL_STAGES = ("7.2.115", "7.2.116", "6.4.92", "7.3.36", "7.3.37", "7.3.86", "1.1.51", "7.3.84", "6.1.78", "7.1.3", "6.1.97", "7.3.101")


def _vr(v: str, cands) -> str:
    return FROM58[antaratama(TO58[v], cands)]


def causative(root: str, code: str, up: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    r = list(ROOTS[root])
    n = its("ṇic", "pratyaya")
    assert n["remaining_sounds"] == ("i",) and set(n["its"]) == {"ṇ", "c"}
    path = [f"{root} + ṇic (3.1.26; ṇ 1.3.7, c 1.3.3 → i); the ṇijanta is a dhātu (3.1.32)"]
    # 7.2.115 / 7.2.116: ṇit vṛddhi (ṇic is ṇit)
    if r[-1] in VOWELS and "7.2.115" in on:
        v = antaratama(TO58[r[-1]], VRDDHI_SET)
        sub = rapara_1_1_51(TO58[r[-1]], v) if "1.1.51" in on else v
        r = r[:-1] + ([FROM58[sub]] if sub in FROM58 else [FROM58[sub[0]], sub[1]])
        path.append(f"final vowel → vṛddhi before ṇit (7.2.115 aco ñṇiti; 1.1.50" + ("; 1.1.51)" if root in ("kṛ", "hṛ") and "1.1.51" in on else ")") + f" → {''.join(r)}")
        if r[-1] in AYADI and "6.1.78" in on:
            r = r[:-1] + list(AYADI[r[-1]]); path.append(f"{''.join(r)}: ec → āy / āv before the vowel of ṇic (6.1.78 eco 'yavāyāvaḥ)")
    elif len(r) >= 2 and r[-2] == "a" and "7.2.116" in on:
        r[-2] = "ā"; path.append(f"penultimate a → ā before ṇit (7.2.116 ata upadhāyāḥ) → {''.join(r)}")
        if root in MIT and "6.4.92" in on:
            r[-2] = "a"; path.append("the mit root's penultimate stays short (6.4.92 mitāṁ hrasvaḥ; gaṇasūtra amantāś ca)")
    elif len(r) >= 2 and r[-2] in ("i", "u", "ṛ") and "7.3.86" in on:
        g = antaratama(TO58[r[-2]], GUNA_SET)
        sub = rapara_1_1_51(TO58[r[-2]], g) if "1.1.51" in on else g
        r = r[:-2] + list(sub if sub != "A" else "ā") + r[-1:]
        path.append(f"light penultimate ik → guṇa before ṇic (7.3.86 pugantalaghūpadhasya ca" + ("; 1.1.51)" if root == "kṛṣ" else ")") + f" → {''.join(r)}")
    # augments after an ā-final root
    if root in PUK_ROOTS and "7.3.36" in on:
        r = r + ["p"]; path.append("puk after the ā-final root (7.3.36 …ātāṁ puṅ ṇau; k it 1.3.3, u 1.3.2)")
    if root in YUK_ROOTS and "7.3.37" in on:
        r = r + ["y"]; path.append("yuk after pā (7.3.37 śācchāsāhvāvyāvepāṁ yuk)")
    stem = r + ["i"]
    # śap (3.1.68) after the ṇijanta dhātu; ṇi → guṇa (7.3.84) → ay (6.1.78)
    sap = list(its("śap", "pratyaya")["remaining_sounds"])
    assert sap == ["a"]
    if "7.3.84" in on:
        stem[-1] = FROM58[antaratama("i", GUNA_SET)]; path.append("ṇi → ṇe before the sārvadhātuka śap (7.3.84; 3.1.68, 3.4.113)")
        if "6.1.78" in on:
            stem = stem[:-1] + ["a", "y"]; path.append("e → ay before the vowel (6.1.78)")
    stem = stem + sap
    # tiṅ
    t = its(up, "pratyaya", vibhakti=True)
    aff = list(t["remaining_sounds"])
    if up == "jhi" and "7.1.3" in on:
        aff = ["a", "n", "t"] + aff[1:]; path.append("jh → ant (7.1.3 jho 'ntaḥ)")
    if up == "mip" and "7.3.101" in on and stem[-1] == "a":
        stem[-1] = "ā"; path.append("a → ā before the yañ-initial sārvadhātuka mi (7.3.101)")
    if stem[-1] == "a" and aff and aff[0] == "a" and "6.1.97" in on:
        aff = aff[1:]; path.append("a + a → a (6.1.97 ato guṇe)")
    path.append(f"{up} → {''.join(aff)} (3.4.78; parasmaipada 1.3.78)")
    return "".join(stem + aff), path


def forms_for(root: str, stages=ALL_STAGES) -> dict[str, str]:
    return {c: causative(root, c, up, stages)[0] for c, up in CELLS}


def oracle(root: str) -> dict[str, str]:
    s = STEM_ORACLE[root]
    return {"3s": s + "ti", "3p": s + "nti", "1s": s[:-1] + "āmi"}


def t1_causatives() -> dict[str, Any]:
    forms = {r: forms_for(r) for r in ROOTS}
    exp = {r: oracle(r) for r in ROOTS}
    all_cells = {f"{r}.{c}" for r in ROOTS for c, _ in CELLS}
    exp_breaks = {
        "7.2.115": {f"{r}.{c}" for r in ("bhū", "kṛ", "nī", "hṛ") for c, _ in CELLS},
        "7.2.116": {f"pac.{c}" for c, _ in CELLS}, "6.4.92": {f"gam.{c}" for c, _ in CELLS},
        "7.3.36": {f"{r}.{c}" for r in ("sthā", "dā") for c, _ in CELLS}, "7.3.37": {f"pā.{c}" for c, _ in CELLS},
        "7.3.86": {f"{r}.{c}" for r in ("vid", "budh", "kṛṣ") for c, _ in CELLS}, "1.1.51": {f"{r}.{c}" for r in ("kṛ", "hṛ", "kṛṣ") for c, _ in CELLS},
        "7.3.84": all_cells, "6.1.78": all_cells, "7.1.3": {f"{r}.3p" for r in ROOTS}, "6.1.97": {f"{r}.3p" for r in ROOTS}, "7.3.101": {f"{r}.1s" for r in ROOTS},
    }
    broken = {}
    for s in exp_breaks:
        st = tuple(x for x in ALL_STAGES if x != s)
        broken[s] = sorted(f"{r}.{c}" for r in ROOTS for c, _ in CELLS if forms_for(r, st)[c] != exp[r][c])
    checks = {"thirty_six_causative_forms_equal_the_classical_forms": all(forms[r][c] == exp[r][c] for r in ROOTS for c, _ in CELLS)}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break": set(broken[s]) == v for s, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {r: causative(r, "3s", "tip")[1] for r in ROOTS}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_causatives": t1_causatives()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_NIC_CAUSATIVE_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_NIC_CAUSATIVE_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.nic_causative_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "twelve ṇijanta roots in laṭ parasmaipada 3s / 3p / 1s (36 forms) by 3.1.26 with 7.2.115, 7.2.116, 6.4.92, 7.3.36, 7.3.37, 7.3.86, 1.1.51, then 3.1.68 with 7.3.84, 6.1.78, and 3.4.78 with 7.1.3, 6.1.97, 7.3.101; each rule breaks exactly the forms stated",
            ],
            "NOT_claimed": [
                "the mit status of gam is declared from the Dhātupāṭha gaṇasūtra (amantāś ca), not derived; the puk / yuk root lists of 7.3.36 / 7.3.37 are read as the sūtra names them",
                "the vṛddhi of ā (7.2.115 on sthā, dā, pā) is vacuous on the surface and so not an ablation target; ātmanepada, other lakāras, 6.4.51 ṇer aniṭi (which deletes ṇi before iṭ-less ārdhadhātukas), the ṇijanta's kṛt forms",
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
