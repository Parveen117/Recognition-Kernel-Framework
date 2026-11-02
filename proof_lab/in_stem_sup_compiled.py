from __future__ import annotations

"""Exact certificate (theorum/123): in-STEMS DECLINED — daṇḍin, yaśasvin (vini),
grāhin (ṇini), uṣṇabhojin (upapada ṇini) in the masculine, daṇḍi in the
neuter: 6.4.13 sau ca (daṇḍī), 6.4.12 inhanpūṣāryamṇāṁ śau (neuter daṇḍīni),
6.1.68 su-lopa, 8.2.7 nalopa on the pada (1.1.62), 8.2.8 na ṅisambuddhyoḥ,
7.1.23 / 7.1.20 for the neuter, 8.3.59 in the locative plural, the an-stem
prathiman (imanic) on theorum/92's carrier as the contrast; each rule shown
load-bearing on exactly its cells.  The engine both theorum/120 and 121
named as their next target.

Quoted sūtras:
 6.4.7    nopadhāyāḥ ; 6.4.8 sarvanāmasthāne cāsambuddhau      the an-stem dīrgha (rājānau) — NOT for in: 6.4.12 restricts
 6.4.12   inhanpūṣāryamṇāṁ śau                                 in / han / pūṣan / aryaman lengthen only before śi
 6.4.13   sau ca                                               … and before su (daṇḍī)
 6.1.68   halṅyābbhyo dīrghāt sutisyapṛktaṁ hal                su dropped after the consonant
 8.2.7    nalopaḥ prātipadikāntasya ; 1.1.62 ; 1.4.14 ; 1.4.17 svādiṣv asarvanāmasthāne (pada before bhyām / bhis / bhyas / su)
 8.2.8    na ṅisambuddhyoḥ                                     the n kept before ṅi and in the sambuddhi (daṇḍini, he daṇḍin)
 7.1.23   svamor napuṁsakāt ; 7.1.20 jaśśasoḥ śiḥ ; 7.1.19 napuṁsakāc ca ; 1.1.42 śi sarvanāmasthānam
 8.3.59   ādeśapratyayayoḥ (daṇḍiṣu) ; 8.2.66 ; 8.3.15
 5.2.115  ata iniṭhanau ; 5.2.121 asmāyāmedhāsrajo viniḥ ; 3.1.134 (ṇini) ; 3.2.78 supy ajātau ṇinis tācchīlye ; 5.1.122 pṛthvādibhya imanij vā

 T1  daṇḍin 22 cells, yaśasvin / grāhin / uṣṇabhojin 1s 1d 3s 3d 7p 8s, neuter daṇḍi 1s 1p 2p ; T2  prathiman on theorum/92.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.hal_stem_sup_compiled import ALL_STAGES as HAL_STAGES, SUP, decline as hal_decline
from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "6.4.7": "nopadhāyāḥ", "6.4.8": "sarvanāmasthāne cāsambuddhau", "6.4.12": "inhanpūṣāryamṇāṁ śau", "6.4.13": "sau ca",
    "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "8.2.7": "nalopaḥ prātipadikāntasya", "1.1.62": "pratyayalope pratyayalakṣaṇam", "1.4.14": "suptiṅantaṁ padam",
    "1.4.17": "svādiṣv asarvanāmasthāne", "8.2.8": "na ṅisambuddhyoḥ", "7.1.23": "svamor napuṁsakāt", "7.1.20": "jaśśasoḥ śiḥ", "7.1.19": "napuṁsakāc ca",
    "1.1.42": "śi sarvanāmasthānam", "8.3.59": "ādeśapratyayayoḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
    "5.2.115": "ata iniṭhanau", "5.2.121": "asmāyāmedhāsrajo viniḥ", "3.1.134": "nandigrahipacādibhyo lyuṇinyacaḥ", "3.2.78": "supy ajātau ṇinis tācchīlye", "5.1.122": "pṛthvādibhya imanij vā",
}
VOWELS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au")
SARVANAMASTHANA = {"1s", "1d", "1p", "2s", "2d", "8s"}
STEMS = {
    "daṇḍin": ("d", "a", "ṇ", "ḍ", "i", "n"), "yaśasvin": ("y", "a", "ś", "a", "s", "v", "i", "n"), "grāhin": ("g", "r", "ā", "h", "i", "n"),
    "uṣṇabhojin": ("u", "ṣ", "ṇ", "a", "bh", "o", "j", "i", "n"),
}
ORACLE_DANDIN = {"1s": "daṇḍī", "1d": "daṇḍinau", "1p": "daṇḍinaḥ", "2s": "daṇḍinam", "2d": "daṇḍinau", "2p": "daṇḍinaḥ", "3s": "daṇḍinā", "3d": "daṇḍibhyām", "3p": "daṇḍibhiḥ",
                 "4s": "daṇḍine", "4d": "daṇḍibhyām", "4p": "daṇḍibhyaḥ", "5s": "daṇḍinaḥ", "5d": "daṇḍibhyām", "5p": "daṇḍibhyaḥ", "6s": "daṇḍinaḥ", "6d": "daṇḍinoḥ", "6p": "daṇḍinām",
                 "7s": "daṇḍini", "7d": "daṇḍinoḥ", "7p": "daṇḍiṣu", "8s": "daṇḍin"}
ORACLE_OTHERS = {"yaśasvin": {"1s": "yaśasvī", "1d": "yaśasvinau", "3s": "yaśasvinā", "3d": "yaśasvibhyām", "7p": "yaśasviṣu", "8s": "yaśasvin"},
                 "grāhin": {"1s": "grāhī", "1d": "grāhiṇau", "3s": "grāhiṇā", "3d": "grāhibhyām", "7p": "grāhiṣu", "8s": "grāhin"},
                 "uṣṇabhojin": {"1s": "uṣṇabhojī", "1d": "uṣṇabhojinau", "3s": "uṣṇabhojinā", "3d": "uṣṇabhojibhyām", "7p": "uṣṇabhojiṣu", "8s": "uṣṇabhojin"}}
ORACLE_NEUTER = {"1s": "daṇḍi", "1p": "daṇḍīni", "2p": "daṇḍīni"}
ALL_STAGES = ("6.4.13", "6.4.12", "6.1.68", "8.2.7", "8.2.8", "7.1.23", "7.1.20", "8.3.59", "8.4.2", "8.2.66", "8.3.15")
AT_KU_PU = {"a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "o", "ai", "au", "h", "y", "v", "r", "k", "kh", "g", "gh", "ṅ", "p", "ph", "b", "bh", "m", "ṁ"}


def _natva(word: list[str], on: set) -> tuple[list[str], list[str]]:
    """8.4.2 across aṭ / ku / pu after r (theorum/91's reading), not on a pada-final n (8.4.37)."""
    path = []
    if "8.4.2" not in on:
        return word, path
    out = list(word)
    for i, s in enumerate(out):
        if s != "n" or i == len(out) - 1:
            continue
        j = i - 1
        while j >= 0 and out[j] in AT_KU_PU and out[j] != "r":
            j -= 1
        if j >= 0 and out[j] in ("r", "ṣ", "ṛ"):
            out[i] = "ṇ"; path.append("n → ṇ after r across aṭ / ku / pu (8.4.2; 8.4.1)")
    return out, path


def decline(name: str, code: str, up: str, neuter: bool = False, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st = list(STEMS[name]); path = [f"{name} (in-stem; {'neuter' if neuter else 'masculine'}) + {up}"]
    r = its(up, "pratyaya", vibhakti=True); aff = list(r["remaining_sounds"])
    sns = code in SARVANAMASTHANA
    if neuter:
        if code in ("1s", "2s") and "7.1.23" in on:
            aff = []; path.append("su / am deleted after the neuter (7.1.23 svamor napuṁsakāt; luk)")
        elif code in ("1p", "2p") and "7.1.20" in on:
            aff = ["i"]; path.append("jas / śas → śi (7.1.20 jaśśasoḥ śiḥ; ś it 1.3.8); śi is sarvanāmasthāna (1.1.42)")
            if "6.4.12" in on:
                st[-2] = "ī"; path.append("upadhā of the in-stem lengthened before śi (6.4.12 inhanpūṣāryamṇāṁ śau)")
    else:
        if code in ("1s",) and "6.4.13" in on:
            st[-2] = "ī"; path.append("upadhā of the in-stem lengthened before su, not in sambuddhi (6.4.13 sau ca)")
        if code in ("1s", "8s") and aff == ["s"] and "6.1.68" in on:
            aff = []; path.append("su dropped after the consonant (6.1.68)")
        if sns and code not in ("1s", "8s"):
            path.append("no upadhā dīrgha before au / jas / am / auṭ: 6.4.12–13 confine it to śi and su (contrast rājānau by 6.4.8)")
    # pada status: before the consonant-initial endings (1.4.17) and when the sup is deleted (1.1.62)
    cons_initial = bool(aff) and aff[0] not in VOWELS
    pada = (not sns and cons_initial) or (not aff)
    if pada and st[-1] == "n":
        if code == "8s" and "8.2.8" in on:
            path.append("n kept in the sambuddhi (8.2.8 na ṅisambuddhyoḥ)")
        elif "8.2.7" in on:
            st = st[:-1]; path.append("pada-final n dropped (8.2.7; pada by 1.4.14 with 1.1.62 / 1.4.17)")
    if code == "7s" and "8.2.8" in on:
        path.append("n kept before ṅi (8.2.8)")
    word = st + aff
    if code == "7p" and "8.3.59" in on and word[-2] == "s" and word[-3] in ("i", "ī", "u", "ū", "e", "o"):
        word[-2] = "ṣ"; path.append("s of sup → ṣ after the iṇ vowel (8.3.59)")
    word, p2 = _natva(word, on); path += p2
    if word[-1] == "s" and "8.2.66" in on:
        word[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            word[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    return "".join(word), path


def paradigm(name: str, neuter: bool = False, stages=ALL_STAGES) -> dict[str, str]:
    return {c: decline(name, c, up, neuter, stages)[0] for c, up in SUP}


def t1_in_stems() -> dict[str, Any]:
    d = paradigm("daṇḍin")
    others = {n: {c: decline(n, c, dict(SUP)[c])[0] for c in ORACLE_OTHERS[n]} for n in ORACLE_OTHERS}
    neut = {c: decline("daṇḍin", c, dict(SUP)[c], neuter=True)[0] for c in ORACLE_NEUTER}
    exp_breaks = {"6.4.13": {"1s"}, "6.1.68": {"1s", "8s"}, "8.2.7": {"1s", "3d", "3p", "4d", "4p", "5d", "5p", "7p"}, "8.2.8": {"8s"},
                  "8.3.59": {"7p"}, "8.2.66": {"1p", "2p", "3p", "4p", "5p", "5s", "6s", "6d", "7d"}, "8.3.15": {"1p", "2p", "3p", "4p", "5p", "5s", "6s", "6d", "7d"}, "8.4.2": set(), "6.4.12": set(), "7.1.23": set(), "7.1.20": set()}
    broken = {s: sorted(c for c, _ in SUP if paradigm("daṇḍin", False, tuple(x for x in ALL_STAGES if x != s))[c] != ORACLE_DANDIN[c]) for s in exp_breaks}
    neut_breaks = {"7.1.23": {"1s"}, "7.1.20": {"1p", "2p"}, "6.4.12": {"1p", "2p"}, "8.2.7": {"1s"}}
    nbroken = {s: sorted(c for c in ORACLE_NEUTER if decline("daṇḍin", c, dict(SUP)[c], True, tuple(x for x in ALL_STAGES if x != s))[0] != ORACLE_NEUTER[c]) for s in neut_breaks}
    gr_broken = sorted(c for c in ORACLE_OTHERS["grāhin"] if decline("grāhin", c, dict(SUP)[c], False, tuple(x for x in ALL_STAGES if x != "8.4.2"))[0] != ORACLE_OTHERS["grāhin"][c])
    checks = {"dandin_22_cells_equal_oracle": all(d[c] == ORACLE_DANDIN[c] for c in ORACLE_DANDIN),
              "yasasvin_grahin_usnabhojin_cells_equal_oracle": all(others[n][c] == ORACLE_OTHERS[n][c] for n in ORACLE_OTHERS for c in ORACLE_OTHERS[n]),
              "neuter_dandi_cells_equal_oracle": all(neut[c] == ORACLE_NEUTER[c] for c in ORACLE_NEUTER),
              "without_8_4_2_exactly_grahinau_grahina_break": gr_broken == ["1d", "3s"]}
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break_masc": set(broken[s]) == v for s, v in exp_breaks.items()})
    checks.update({f"without_{s.replace('.', '_')}_exactly_{len(v)}_break_neuter": set(nbroken[s]) == v for s, v in neut_breaks.items()})
    return {"checks": checks, "dandin": d, "others": others, "neuter": neut, "paths": {"1s": decline("daṇḍin", "1s", "su~")[1], "3d": decline("daṇḍin", "3d", "bhyām")[1], "neuter_1p": decline("daṇḍin", "1p", "jas", True)[1]}, "broken": broken, "neuter_broken": nbroken}


def t2_prathiman() -> dict[str, Any]:
    p = {c: hal_decline(("p", "r", "a", "th", "i", "m", "a", "n"), c, up, HAL_STAGES)[0] for c, up in SUP}
    exp = {"1s": "prathimā", "1d": "prathimānau", "1p": "prathimānaḥ", "3s": "prathimnā", "3d": "prathimabhyām", "6p": "prathimnām", "7s": "prathimni / prathimani", "8s": "prathiman"}
    checks = {"prathiman_on_theorum_92_an_carrier": all(p[c] == exp[c] for c in exp)}
    return {"checks": checks, "prathiman": {c: p[c] for c in exp}}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_in_stems": t1_in_stems(), "t2_prathiman": t2_prathiman()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_IN_STEM_SUP_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_IN_STEM_SUP_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.in_stem_sup_compiled_candidate.v1", "status": status, "sources": SOURCES, "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "daṇḍin declined, 22 cells, with 6.4.13 (daṇḍī), 6.1.68, 8.2.7 on the pada (1.1.62 / 1.4.17), 8.2.8 (daṇḍini, daṇḍin), 8.3.59 (daṇḍiṣu), 8.2.66 / 8.3.15; the neuter daṇḍi with 7.1.23 and 7.1.20 + 6.4.12 (daṇḍīni); yaśasvin (vini), grāhin (ṇini, with 8.4.2 in grāhiṇau / grāhiṇā), uṣṇabhojin on the same engine; each rule breaks exactly the cells stated",
                "prathiman (imanic) declines on theorum/92's an-carrier unchanged (prathimā, prathimānau, prathimnā, prathimnām)",
                "6.4.12 / 6.4.13 confine the upadhā dīrgha of an in-stem to śi and su: the masculine 1d / 1p / 2s / 2d take no dīrgha (contrast 6.4.8 on rājan), recorded as a vacuous-by-design ablation of 6.4.8-type lengthening",
            ],
            "NOT_claimed": ["the feminine (daṇḍinī, 4.1.5 ṛnnebhyo ṅīp), the 7s option of the neuter, han / pūṣan / aryaman (6.4.12's other members), the vin / ṇini / imanic affixation itself (theorum/120 – 121 written derivations; the stems are declared here)", "RH, YM untouched"],
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
