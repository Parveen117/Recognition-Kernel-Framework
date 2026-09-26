from __future__ import annotations

"""Exact certificate (theorum/70): THE SIX PRAMĀṆAS OF AṄGATVA (Mīmāṃsā-sūtra
3.3.14 śruti-liṅga-vākya-prakaraṇa-sthāna-samākhyānāṃ samavāye pāradaurbalyam
artha-viprakarṣāt) as an executable resolver — and Gāyatrī's aṅgatva DERIVED
from evidence rather than declared (closing theorum/69's declared input).

Carrier: a subsidiary item (mantra / dravya / act) with a set of EVIDENCES,
each (pramāṇa, candidate aṅgin).  The sūtra's own reason for the ranking is
artha-viprakarṣa (remoteness of purport): a weaker pramāṇa establishes
aṅgatva only by INFERRING the stronger ones in turn — liṅga presupposes a
śruti, vākya a liṅga, prakaraṇa a vākya, sthāna a prakaraṇa, samākhyā a
sthāna.  So each pramāṇa has a DELAY depth d = number of inferential steps
to a direct statement:  śruti 0, liṅga 1, vākya 2, prakaraṇa 3, sthāna 4,
samākhyā 5.  Resolution = minimal delay (pūrva-pūrva-balīyastva).  Equal
delay with different candidates -> vikalpa (theorum/69's lawful tie).

Facts certified on the classical instances of the Bhāṣya:
 T1  aindryā gārhapatyam upatiṣṭhate: liṅga (the mantra praises Indra ->
     Indra) vs śruti (the vidhi names gārhapatya) -> śruti, delay 0 < 1.
 T2  syonaṃ te sadanaṃ kṛṇomi: vākya (sentence connects it with the barhis
     act) vs liṅga (content = seat-making for the puroḍāśa) -> liṅga.
 T3  prakaraṇa vs vākya (the prayāja evidence): vākya wins; prakaraṇa alone
     assigns to darśapūrṇamāsa when no vākya is present.
 T4  sthāna vs samākhyā; samākhyā alone ("hautra" -> hotṛ) assigns.
 T5  Monotonicity theorem: removing the strongest evidence can only move the
     assignment to the next delay level -- never to a weaker candidate over
     a stronger one (checked on every subset of every instance).
 T6  GĀYATRĪ: evidences — śruti: the referencing vidhi "gāyatrīṃ japet"
     (sandhyā-japa); liṅga: content "savitur ... dhīmahi" -> Savitṛ-devatā
     rite; samākhyā: the name "sāvitrī" -> Savitṛ.  With the vidhi present,
     aṅgatva = sandhyā-japa by śruti (delay 0); with it removed, liṅga and
     samākhyā AGREE on the Savitṛ rite (delay 1), K = 0 -- no vikalpa needed.
     theorum/69's "referencing vidhi" is thus the śruti evidence of this
     resolver; the assignment is derived, the evidences remain input.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

DELAY = {"śruti": 0, "liṅga": 1, "vākya": 2, "prakaraṇa": 3, "sthāna": 4, "samākhyā": 5}


def resolve(evidences: list[tuple[str, str]]) -> dict[str, Any]:
    if not evidences:
        return {"angin": None, "by": None, "delay": None, "vikalpa": False, "K": 0}
    d = min(DELAY[p] for p, _ in evidences)
    top = sorted({c for p, c in evidences if DELAY[p] == d})
    by = sorted({p for p, _ in evidences if DELAY[p] == d})
    if len(top) == 1:
        return {"angin": top[0], "by": by[0], "delay": d, "vikalpa": False, "K": 0}
    return {"angin": top, "by": by[0], "delay": d, "vikalpa": True, "K": 0}


INSTANCES = {
    "aindrī_mantra": [("liṅga", "Indra"), ("śruti", "gārhapatya")],
    "syonaṃ_te_sadanam": [("vākya", "barhis-act"), ("liṅga", "puroḍāśa-placement")],
    "prayāja": [("prakaraṇa", "darśapūrṇamāsa"), ("vākya", "prayāja-sentence-rite")],
    "hautra": [("sthāna", "position-rite"), ("samākhyā", "hotṛ")],
    "gāyatrī": [("śruti", "sandhyā-japa"), ("liṅga", "Savitṛ-rite"), ("samākhyā", "Savitṛ-rite")],
}
ORACLE = {"aindrī_mantra": ("gārhapatya", "śruti"), "syonaṃ_te_sadanam": ("puroḍāśa-placement", "liṅga"), "prayāja": ("prayāja-sentence-rite", "vākya"), "hautra": ("position-rite", "sthāna"), "gāyatrī": ("sandhyā-japa", "śruti")}


def monotone(evidences) -> bool:
    """Removing evidence never lets a weaker pramāṇa's candidate beat a stronger present one."""
    for k in range(len(evidences)):
        for sub in itertools.combinations(evidences, k + 1):
            r = resolve(list(sub))
            dmin = min(DELAY[p] for p, _ in sub)
            if r["delay"] != dmin:
                return False
            cands = {c for p, c in sub if DELAY[p] == dmin}
            got = set(r["angin"]) if isinstance(r["angin"], list) else {r["angin"]}
            if got != cands:
                return False
    return True


def build_certificate() -> dict[str, Any]:
    res = {k: resolve(v) for k, v in INSTANCES.items()}
    ok = {k: (res[k]["angin"], res[k]["by"]) == ORACLE[k] for k in ORACLE}
    pr_alone = resolve([("prakaraṇa", "darśapūrṇamāsa")])
    sam_alone = resolve([("samākhyā", "hotṛ")])
    g_no_vidhi = resolve([e for e in INSTANCES["gāyatrī"] if e[0] != "śruti"])
    tie = resolve([("liṅga", "A"), ("liṅga", "B")])
    checks = {
        "T1_T4_classical_instances_match_bhasya": all(ok.values()),
        "T3_T4_weaker_pramana_assigns_when_alone": pr_alone["angin"] == "darśapūrṇamāsa" and sam_alone["angin"] == "hotṛ",
        "T5_monotone_under_evidence_removal_all_instances": all(monotone(v) for v in INSTANCES.values()),
        "T6_gayatri_sruti_vidhi_gives_sandhya_japa": res["gāyatrī"]["angin"] == "sandhyā-japa" and res["gāyatrī"]["delay"] == 0,
        "T6_gayatri_without_vidhi_linga_and_samakhya_agree_savitr_K0": g_no_vidhi["angin"] == "Savitṛ-rite" and g_no_vidhi["delay"] == 1 and not g_no_vidhi["vikalpa"],
        "equal_delay_different_candidates_is_vikalpa": tie["vikalpa"] and tie["angin"] == ["A", "B"],
    }
    status = "PASS_ANGATVA_PRAMANA_LADDER_CANDIDATE" if all(checks.values()) else "FAIL_ANGATVA_PRAMANA_LADDER_CANDIDATE"
    return {
        "schema": "rkf.angatva_pramana_ladder_candidate.v1",
        "status": status,
        "delay": DELAY,
        "results": res,
        "gayatri_without_vidhi": g_no_vidhi,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "MS 3.3.14 as a delay-ordered resolver (artha-viprakarṣa = inferential delay); classical Bhāṣya instances reproduced; monotone under evidence removal",
                "Gāyatrī's aṅgatva derived: sandhyā-japa by śruti when the vidhi is present; Savitṛ-rite by liṅga+samākhyā (agreeing) when it is absent -- theorum/69's declared 'referencing vidhi' is now the śruti evidence of this resolver",
                "equal-delay disagreement is vikalpa (theorum/69 tie semantics), not refusal",
            ],
            "NOT_claimed": ["the evidences themselves are INPUT (read off the texts by the tradition); the sub-rules of each pramāṇa (e.g. what counts as liṅga) are not modelled", "artha of any mantra", "RH, YM untouched"],
        },
        "checks": checks,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k, v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
