from __future__ import annotations

"""Exact certificate (theorum/113): THE PRONOMINAL ADVERBS COMPILED — tasil (5.3.7),
tral (5.3.10), dā (5.3.15) and haḥ for idam (5.3.11) on tad, yad, kim, idam,
etad, sarva: the sarvanāma stem changes 7.2.102 tyadādīnām aḥ (with 6.1.97),
7.2.103 kimaḥ kaḥ, 7.2.104 ku tihoḥ, 5.3.3 idama iś, 5.3.5 etadaḥ an (atra,
ataḥ); the sup inside deleted by 2.4.71 (as in theorum/104); each rule shown
load-bearing on exactly the words it governs.

Quoted sūtras:
 5.3.1    prāg diśo vibhaktiḥ                           the affixes up to 5.3.27 are vibhakti (so 7.2.102 ff. apply)
 5.3.2    kiṁsarvanāmabahubhyo 'dvyādibhyaḥ             after kim, the sarvanāmas (not dvi etc.)
 5.3.7    pañcamyās tasil ; 5.3.10 saptamyās tral ; 5.3.15 sarvaikānyakiṁyattadaḥ kāle dā
 5.3.11   idamo haḥ (iha) ; 5.3.3 idama iś ; 5.3.5 etado 'n (etad → a: atra, ataḥ)
 7.2.102  tyadādīnām aḥ (tad → ta, yad → ya ; 6.1.97 ato guṇe)
 7.2.103  kimaḥ kaḥ (kadā) ; 7.2.104 ku tihoḥ (kutra, kutaḥ)
 2.4.71   supo dhātuprātipadikayoḥ ; 1.1.38 taddhitaś cāsarvavibhaktiḥ (the adverbs are avyaya) ; 1.3.3 ; 1.3.8 (l of tasil, tral)
 8.2.66   sasajuṣo ruḥ ; 8.3.15 kharavasānayor visarjanīyaḥ (tataḥ)

 T1  tataḥ, tatra, tadā ; yataḥ, yatra, yadā ; kutaḥ, kutra, kadā ; iha ; ataḥ, atra ; sarvataḥ, sarvatra, sarvadā — 15 words.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its

SOURCES = {
    "5.3.1": "prāg diśo vibhaktiḥ", "5.3.2": "kiṁsarvanāmabahubhyo 'dvyādibhyaḥ", "5.3.7": "pañcamyās tasil", "5.3.10": "saptamyās tral",
    "5.3.15": "sarvaikānyakiṁyattadaḥ kāle dā", "5.3.11": "idamo haḥ", "5.3.3": "idama iś", "5.3.5": "etado 'n",
    "7.2.102": "tyadādīnām aḥ", "7.2.103": "kimaḥ kaḥ", "7.2.104": "ku tihoḥ", "2.4.71": "supo dhātuprātipadikayoḥ", "1.1.38": "taddhitaś cāsarvavibhaktiḥ",
    "1.3.3": "halantyam", "1.3.8": "laśakv ataddhite", "6.1.97": "ato guṇe", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayor visarjanīyaḥ",
}
STEMS = {"tad": ("t", "a", "d"), "yad": ("y", "a", "d"), "kim": ("k", "i", "m"), "idam": ("i", "d", "a", "m"), "etad": ("e", "t", "a", "d"), "sarva": ("s", "a", "r", "v", "a")}
AFFIXES = {"tasil": "5.3.7", "tral": "5.3.10", "dā": "5.3.15"}
CASES = [("tad", "tasil", "tataḥ"), ("tad", "tral", "tatra"), ("tad", "dā", "tadā"), ("yad", "tasil", "yataḥ"), ("yad", "tral", "yatra"), ("yad", "dā", "yadā"),
         ("kim", "tasil", "kutaḥ"), ("kim", "tral", "kutra"), ("kim", "dā", "kadā"), ("idam", "tral", "iha"), ("etad", "tasil", "ataḥ"), ("etad", "tral", "atra"),
         ("sarva", "tasil", "sarvataḥ"), ("sarva", "tral", "sarvatra"), ("sarva", "dā", "sarvadā")]
TYADADI = {"tad", "yad", "etad", "idam"}
ALL_STAGES = ("2.4.71", "7.2.102", "6.1.97", "7.2.103", "7.2.104", "5.3.3", "5.3.5", "5.3.11", "8.2.66", "8.3.15")


def adverb(stem: str, aff: str, stages=ALL_STAGES) -> tuple[str, list[str]]:
    on = set(stages)
    st = list(STEMS[stem])
    a = its(aff, "pratyaya", taddhita=True)
    rem = list(a["remaining_sounds"])
    if aff == "tasil" and rem == ["t", "a", "s", "i"]:
        rem = ["t", "a", "s"]   # the i of tasil is uccāraṇārtha (declared: it only carries the it l, as the tradition reads tasil / tral)
    sup = {"tasil": "ṅasi", "tral": "ṅi", "dā": "ṅi"}[aff]
    path = [f"{stem} + {sup} + {aff} → {''.join(rem)} ({AFFIXES[aff]}; its {a['its']}; vibhakti 5.3.1; after a sarvanāma 5.3.2)"]
    if "2.4.71" in on:
        path.append("the inner sup deleted (2.4.71)")
    else:
        st = st + list(sup)
    if stem == "idam" and aff == "tral" and "5.3.11" in on:
        rem = ["h", "a"]; path.append("tral → ha after idam (5.3.11 idamo haḥ)")
    if stem == "idam" and "5.3.3" in on:
        st = ["i"]; path.append("idam → i before the vibhakti taddhita (5.3.3 idama iś)")
    elif stem == "etad" and "5.3.5" in on:
        st = ["a"]; path.append("etad → a (5.3.5 etado 'n; 1.1.55 anekāl śit sarvasya)")
    elif stem in TYADADI and "7.2.102" in on:
        st = st[:-1] + ["a"]; path.append(f"final sound of the tyadādi → a before the vibhakti (7.2.102 tyadādīnām aḥ): {''.join(st)}")
        if st[-2] == "a" and "6.1.97" in on:
            st = st[:-1]; path.append("a + a → a (6.1.97 ato guṇe)")
    elif stem == "kim":
        if aff in ("tasil", "tral") and "7.2.104" in on:
            st = ["k", "u"]; path.append("kim → ku before tasil / tral (7.2.104 ku tihoḥ)")
        elif aff == "dā" and "7.2.103" in on:
            st = ["k", "a"]; path.append("kim → ka before the vibhakti (7.2.103 kimaḥ kaḥ)")
    w = st + rem
    if w[-1] == "s" and "8.2.66" in on:
        w[-1] = "r"; path.append("s → ru (8.2.66)")
        if "8.3.15" in on:
            w[-1] = "ḥ"; path.append("r → ḥ (8.3.15)")
    path.append(f"avyaya (1.1.38 taddhitaś cāsarvavibhaktiḥ): {''.join(w)}")
    return "".join(w), path


def t1_adverbs() -> dict[str, Any]:
    forms = {e: adverb(s, a)[0] for s, a, e in CASES}
    exp_breaks = {"2.4.71": {e for s_, _, e in CASES if s_ in ("tad", "yad", "sarva")}, "7.2.102": {"tataḥ", "tatra", "tadā", "yataḥ", "yatra", "yadā"}, "6.1.97": {"tataḥ", "tatra", "tadā", "yataḥ", "yatra", "yadā"},
                  "7.2.103": {"kadā"}, "7.2.104": {"kutaḥ", "kutra"}, "5.3.3": {"iha"}, "5.3.5": {"ataḥ", "atra"}, "5.3.11": {"iha"},
                  "8.2.66": {"tataḥ", "yataḥ", "kutaḥ", "ataḥ", "sarvataḥ"}, "8.3.15": {"tataḥ", "yataḥ", "kutaḥ", "ataḥ", "sarvataḥ"}}
    broken = {x: sorted(e for s, a, e in CASES if adverb(s, a, tuple(y for y in ALL_STAGES if y != x))[0] != e) for x in exp_breaks}
    checks = {"fifteen_adverbs_equal_the_classical_forms": all(forms[e] == e for e in forms)}
    checks.update({f"without_{x.replace('.', '_')}_exactly_{len(v)}_break": set(broken[x]) == v for x, v in exp_breaks.items()})
    return {"checks": checks, "forms": forms, "paths": {e: adverb(s, a)[1] for s, a, e in CASES}, "broken": broken}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_adverbs": t1_adverbs()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PRONOMINAL_TADDHITA_ADVERBS_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_PRONOMINAL_TADDHITA_ADVERBS_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.pronominal_taddhita_adverbs_compiled_candidate.v1", "status": status, "sources": SOURCES, "stage_order": list(ALL_STAGES),
        "claim_boundary": {
            "proved_by_exact_finite_certificate": ["fifteen adverbs from six sarvanāma stems with tasil, tral, dā (and haḥ for idam) by 5.3.7 / 5.3.10 / 5.3.15 / 5.3.11 with 2.4.71, 7.2.102 + 6.1.97, 7.2.103, 7.2.104, 5.3.3, 5.3.5, 8.2.66, 8.3.15; each rule breaks exactly the words stated"],
            "NOT_claimed": ["the i of tasil is read as uccāraṇārtha (declared); in kim / idam / etad the sarvādeśa (1.1.55) replaces stem and sup together, so 2.4.71 is masked there (its ablation set is the eleven tad / yad / sarva words)", "the sense (pañcamī / saptamī / kāla) is declared from the vidhi sūtra; thāl (tathā, 5.3.24), the diś affixes 5.3.27 ff., the optional forms of 5.3.4 (idam → eta), the accent", "RH, YM untouched"],
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
