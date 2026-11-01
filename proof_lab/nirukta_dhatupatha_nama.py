from __future__ import annotations

"""Exact certificate (theorum/86): NĀMA FROM THE PINNED DHĀTUPĀṬHA — theorum/85's
"nāmāny ākhyātajāni" extended to the lexical entries the PG5 / PG6 stages
pinned from the Dhātupāṭha (research/panini_grammar/*/LEXICAL_ENTRIES.json),
with the ākhyāta side taken from those stages' reference cases.

Sources:
 - the eleven aupadeśika forms below, read from the pinned lexical entries
   (Dhātupāṭha record ids, Devanagari with candrabindu for the anunāsika it)
 - Nirukta 1.12 (theorum/85); Aṣṭādhyāyī 1.3.2–1.3.9 (theorum/82), 1.1.26, 3.2.102,
   1.2.46, 4.1.2, 1.4.14 (theorum/85), and
   6.1.64  dhātvādeḥ ṣaḥ saḥ      the initial ṣ of a dhātu becomes s
   6.4.37  (theorum/85)            nasal lost before a jhal-initial kit affix (tan)
   7.2.10  (theorum/85)            no iṭ for the aniṭ roots
   8.2.44  lvādibhyaḥ              (lū and the lvādi roots: ta of niṣṭhā → na) — cited; lū is refused here

 T1  ELEVEN kta-PRĀTIPADIKAS from the pinned entries: bhū→bhūta, ṣuñ→suta
     (6.1.64), ciñ→cita, āpḷ~→āpta, śakḷ~→śakta, tanu~→tata (6.4.37),
     ḍukṛñ→kṛta, ḍukrīñ→krīta, śru→śruta, pūñ→pūta, hu→huta; theorum/63's
     pinned ladder derives all 22 sup forms of each: 242 nāma forms.
 T2  ĀKHYĀTA FROM PG5 / PG6.  For the same entries, the laṭ 3sg forms the
     PG5 / PG6 reference cases pin (bhavati, sunoti, cinoti, āpnoti, śaknoti,
     tanoti, karoti, krīṇāti, śṛṇoti, punāti) are read from the repository
     and shown disjoint from the nāma forms; hu (juhoti) has no PG case and
     is listed as nāma-only.
 T3  REFUSALS.  lūñ (8.2.44 lūna), adañ (2.4.36 jagdha), pac / labh / tud /
     div (8.2.30, 8.2.40, 8.2.42, 6.1.?) need rules not realized: refused by
     name, not derived.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.astadhyayi_ledger import deva_to_iast
from proof_lab.nirukta_nama_akhyatajani import ANUDATTOPADESA_NASAL, IAST_TO_CODE, JHAL_INITIAL, code
from proof_lab.paninian_it_samjna_compiled import its
from proof_lab.sup_vibhakti_resolver_ladder import ORACLE as ORACLE63, RULES as RULES63, SUP, derive as derive63, paradigm_domains, st as st63, surface as surface63

ROOT = Path(__file__).resolve().parents[1]
PG = ROOT / "research" / "panini_grammar"

SOURCES = {
    "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "6.4.37": "anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti", "7.2.10": "ekāca upadeśe 'nudāttāt",
    "8.2.44": "lvādibhyaḥ", "1.1.26": "ktaktavatū niṣṭhā", "3.2.102": "niṣṭhā", "1.2.46": "kṛttaddhitasamāsāś ca", "1.4.14": "suptiṅantaṁ padam",
    "Nirukta 1.12": "tatra nāmāny ākhyātajānīti śākaṭāyano nairuktasamayaś ca",
    "lexical entries": "research/panini_grammar/{vikarana_lat,non_thematic_lat}/LEXICAL_ENTRIES.json (PG5 / PG6, Dhātupāṭha record ids)",
}

# lexical id → (expected prātipadika, aniṭ declared)
ENTRIES = {"1010001": "bhūta", "1050001": "suta", "1050005": "cita", "1050016": "āpta", "1050017": "śakta", "1080001": "tata",
           "1080010": "kṛta", "1090001": "krīta", "1011092": "śruta", "1090014": "pūta", "1030001": "huta"}
REFUSED = {"1090016": "lūñ: 8.2.44 lvādibhyaḥ (lūna) not realized", "1020001": "adañ: 2.4.36 adaḥ jagdhiḥ (jagdha) not realized",
           "1011151": "ḍupacañṣ: 8.2.30 coḥ kuḥ (pakta) not realized", "1011130": "ḍulabhañṣ: 8.2.40 / 8.4.53 (labdha) not realized",
           "1060001": "tudañ: 8.2.42 radābhyāṁ niṣṭhāto naḥ (tunna) not realized", "1040001": "divu~: samprasāraṇa (dyūta) not realized"}


def load_entries() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for stage in ("vikarana_lat", "non_thematic_lat"):
        d = json.loads((PG / stage / "LEXICAL_ENTRIES.json").read_text(encoding="utf-8"))
        for e in d["entries"]:
            out.setdefault(e["id"], {"aupadeshik": e["aupadeshik"], "gana": e["gana"], "pada": e["pada"], "artha": e["artha"], "stages": []})
            out[e["id"]]["stages"].append(stage)
    return out


def load_lat_3sg() -> dict[str, list[str]]:
    forms: dict[str, set[str]] = {}
    for stage in ("vikarana_lat", "non_thematic_lat"):
        d = json.loads((PG / stage / "REFERENCE_CASES.json").read_text(encoding="utf-8"))
        for c in d["cases"]:
            r = c["request"]
            if c["kind"] == "derive" and r.get("person") == "prathama" and r.get("number") == "eka" and r.get("pada") == "P" and not r.get("prefixes"):
                forms.setdefault(r["lexical_id"], set()).update(c["expected_forms"])
    return {k: sorted(v) for k, v in forms.items()}


def upadesa_iast(deva: str) -> str:
    """Devanagari aupadeśika form → the IAST teaching form theorum/82 reads (ँ → '~' after the vowel)."""
    s = deva_to_iast(deva)
    return s


def kta_from_entry(lex_id: str, entry: dict) -> dict[str, Any]:
    """Admitted entries only: any other lexical id is refused here, not merely listed (guard added after external review)."""
    if lex_id not in ENTRIES:
        raise ValueError(f"{lex_id}: not an admitted kta entry of theorum/86 ({REFUSED.get(lex_id, 'not reviewed')})")
    up = upadesa_iast(entry["aupadeshik"])
    r = its(up, "dhatu")
    dh = list(r["remaining_sounds"])
    steps = [f"{entry['aupadeshik']} → {up} → {''.join(dh)} ({', '.join(sorted(set(r['its'].values())))}; 1.3.9)"]
    if dh and dh[0] == "ṣ":
        dh[0] = "s"
        steps.append("ṣ → s (6.1.64 dhātvādeḥ ṣaḥ saḥ)")
    aff = its("kta", "pratyaya")
    body = list(aff["remaining_sounds"])
    kit = "k" in aff["its"]
    steps.append("kta → ta, kit (1.3.8, 1.3.9); no iṭ (7.2.10, aniṭ declared)")
    root_key = "".join(dh)
    if root_key in ANUDATTOPADESA_NASAL and dh[-1] in ("m", "n") and body[0] in JHAL_INITIAL and kit:
        dh = dh[:-1]
        steps.append(f"nasal lost before jhal-initial kit affix (6.4.37) → {''.join(dh)}")
    prat = tuple(dh) + tuple(body)
    steps.append(f"prātipadika {''.join(prat)} (1.2.46)")
    return {"upadesa": up, "pratipadika": "".join(prat), "sounds": prat, "steps": steps}


def t1_nama_from_dhatupatha() -> dict[str, Any]:
    entries = load_entries()
    dom = paradigm_domains(RULES63)
    out, ok_prat, ok_forms, n = {}, True, True, 0
    for lex, exp in ENTRIES.items():
        e = entries[lex]
        k = kta_from_entry(lex, e)
        ok_prat &= k["pratipadika"] == exp
        stem = code(k["sounds"])
        stem_s = "".join(stem)
        forms = {}
        for c, aff, feats in SUP:
            aff = tuple(aff)
            fe = set(feats) | {"sup"}
            if c == "7p":
                aff = ("s", "u")
            W, _ = derive63(st63(stem, aff, fe), RULES63, dom=dom)
            got = surface63(W)
            expf = (stem_s[:-1] + ORACLE63[c][3:]).replace("N", "n")
            if stem_s[:-1].endswith("r") or "R" in stem_s:       # kṛta, krīta, śruta?: 8.4.2 ṇatva only when nothing but aṭ/ku/pu/āṅ/num intervenes — the t intervenes, so no ṇatva
                pass
            forms[c] = got
            ok_forms &= got == expf
            n += 1
        out[lex] = {"entry": {k2: e[k2] for k2 in ("aupadeshik", "gana", "pada", "artha", "stages")}, "derivation": k["steps"], "pratipadika": k["pratipadika"], "forms": forms}
    checks = {
        "eleven_kta_pratipadikas_equal_the_expected_forms": ok_prat,
        "6_1_64_fires_on_sunj_only": all(("6.1.64" in " ".join(out[l]["derivation"])) == (l == "1050001") for l in ENTRIES),
        "6_4_37_fires_on_tan_only": all(("6.4.37" in " ".join(out[l]["derivation"])) == (l == "1080001") for l in ENTRIES),
        "theorum_63_ladder_derives_all_242_sup_forms": ok_forms and n == 242,
    }
    return {"checks": checks, "entries": out}


def t2_akhyata_from_pg(t1: dict[str, Any]) -> dict[str, Any]:
    lat = load_lat_3sg()
    nama = {f for l in ENTRIES for f in t1["entries"][l]["forms"].values()}
    akhyata_deva = {l: lat.get(l, []) for l in ENTRIES}
    akhyata = {deva_to_iast(f) for fs in akhyata_deva.values() for f in fs}
    akhyata_code = {"".join(IAST_TO_CODE.get(ch, ch) for ch in f) for f in akhyata}
    have = sorted(l for l in ENTRIES if lat.get(l))
    checks = {
        "pg_lat_3sg_forms_present_for_ten_of_the_eleven_entries": len(have) == 10 and "1030001" not in have,
        "nama_and_akhyata_disjoint": not (nama & akhyata_code),
        "every_pg_akhyata_form_ends_in_ti_and_every_nama_form_does_not_end_in_ti": all(f.endswith("ति") for fs in akhyata_deva.values() for f in fs) and not any(f.endswith("ti") for f in nama),
    }
    return {"checks": checks, "akhyata_3sg_from_pg": akhyata_deva, "nama_count": len(nama), "akhyata_count": len(akhyata)}


def t3_refusals() -> dict[str, Any]:
    entries = load_entries()
    checks = {"refused_entries_exist_in_the_pinned_lexicon": all(l in entries for l in REFUSED), "refused_and_derived_are_disjoint": not (set(REFUSED) & set(ENTRIES))}
    return {"checks": checks, "refused": {l: {"aupadeshik": entries[l]["aupadeshik"], "reason": why} for l, why in REFUSED.items()}}


def build_certificate() -> dict[str, Any]:
    t1 = t1_nama_from_dhatupatha()
    t2 = t2_akhyata_from_pg(t1)
    t3 = t3_refusals()
    packets = {"t1_nama_from_dhatupatha": t1, "t2_akhyata_from_pg": t2, "t3_refusals": t3}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_NIRUKTA_DHATUPATHA_NAMA_CANDIDATE" if all(checks.values()) else "FAIL_NIRUKTA_DHATUPATHA_NAMA_CANDIDATE"
    return {
        "schema": "rkf.nirukta_dhatupatha_nama_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "eleven kta-prātipadikas from the pinned Dhātupāṭha entries by theorum/82's its, 6.1.64, 6.4.37, 7.2.10; theorum/63's pinned ladder derives all 242 sup forms",
                "the PG5 / PG6 reference laṭ 3sg forms of the same entries are disjoint from the nāma forms (ākhyāta computed there, nāma here)",
                "six entries refused by the rule they would need (8.2.44, 2.4.36, 8.2.30, 8.2.40 / 8.4.53, 8.2.42, samprasāraṇa)",
            ],
            "NOT_claimed": [
                "aniṭ status is declared (accent is not on the carrier); seṭ roots and the iṭ augment are not derived here",
                "the PG laṭ forms are read as pinned reference data of those stages, not re-derived by this certificate",
                "Gārgya's 'na sarvāṇi' remains undecided; eleven roots and one kṛt affix",
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
