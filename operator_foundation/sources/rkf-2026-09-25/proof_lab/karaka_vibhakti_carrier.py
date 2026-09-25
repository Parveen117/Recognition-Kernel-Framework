from __future__ import annotations

"""Exact certificate (theorum/68): KĀRAKA → VIBHAKTI CARRIER (Aṣṭādhyāyī 1.4 + 2.3)
— the bridge from form to meaning, applied to the Gāyatrī.

Carrier: a sentence frame = verb (voice, person) + a set of nominals each with
a semantic relation to the action.  Two layers of Pāṇini's rules:
  (1) kāraka saṃjñā (1.4.23–55): semantic relation -> saṃjñā
        1.4.24 dhruvam apāye'pādānam      source   -> apādāna
        1.4.32 karmaṇā yam abhipraiti sa sampradānam  recipient -> sampradāna
        1.4.42 sādhakatamaṃ karaṇam        instrument -> karaṇa
        1.4.45 ādhāro'dhikaraṇam           locus    -> adhikaraṇa
        1.4.49 kartur īpsitatamaṃ karma    patient  -> karma
        1.4.54 svatantraḥ kartā            agent    -> kartā
  (2) vibhakti-artha (2.3) under the ABHIHITA LEDGER:
        3.4.69 laḥ karmaṇi ca bhāve cākarmakebhyaḥ: the la (tiṅ) EXPRESSES
              the kartā in kartari prayoga, the karma in karmaṇi prayoga
        2.3.1 anabhihite  -- every 2.3 kāraka-vibhakti applies ONLY to a
              kāraka not already expressed (the ledger guard)
        2.3.2 karmaṇi dvitīyā · 2.3.18 kartṛkaraṇayos tṛtīyā · 2.3.13 caturthī
        sampradāne · 2.3.28 apādāne pañcamī · 2.3.36 saptamy adhikaraṇe ·
        2.3.46 prātipadikārtha-… prathamā (abhihita kāraka / bare stem) ·
        2.3.50 ṣaṣṭhī śeṣe (non-kāraka relation)
        viśeṣaṇa-samānādhikaraṇya: an attribute takes its head's vibhakti
        (declared convention, not a 2.3 sūtra)

The abhihita ledger is the same two-channel structure as 1.1.62's memory:
what the tiṅ has already expressed is invisible to the 2.3 rules.

Facts certified:
 T1  Gāyatrī frame -> vibhaktis equal the vibhaktis the padas actually carry
     (theorum/63/65 codes): tat 2 (attr of bhargas), savitṛ 6, vareṇya 2,
     bhargas 2, deva 6 | yad 1, dhī 2, asmad 6.  The implicit kartā (vayam,
     uttama puruṣa) is abhihita by dhīmahi and gets NO separate pada —
     exactly what the text shows.
 T2  Voice switch (kartari <-> karmaṇi) flips the ledger: "bhargaḥ … dhīyate
     asmābhiḥ" -> bhargas 1, asmad 3 (2.3.18).  Certified both ways.
 T3  2.3.1 is load-bearing: without the anabhihite guard the passive gives
     karma dvitīyā (*bhargaḥ→bhargam) — refused.
 T4  Determinism: each nominal receives exactly one vibhakti; no two 2.3
     rules fire on the same nominal (conflict-freeness computed).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SANJNA = {"agent": ("kartā", "1.4.54"), "patient": ("karma", "1.4.49"), "instrument": ("karaṇa", "1.4.42"), "recipient": ("sampradāna", "1.4.32"), "source": ("apādāna", "1.4.24"), "locus": ("adhikaraṇa", "1.4.45")}
VIBHAKTI = {"kartā": (3, "2.3.18"), "karma": (2, "2.3.2"), "karaṇa": (3, "2.3.18"), "sampradāna": (4, "2.3.13"), "apādāna": (5, "2.3.28"), "adhikaraṇa": (7, "2.3.36")}


def abhihita(verb: dict[str, Any]) -> set[str]:
    """3.4.69: la expresses kartā (kartari) or karma (karmaṇi)."""
    return {"kartā"} if verb["voice"] == "kartari" else {"karma"}


def assign(frame: dict[str, Any], guard_2_3_1: bool = True) -> dict[str, dict[str, Any]]:
    expressed = abhihita(frame["verb"])
    out: dict[str, dict[str, Any]] = {}
    fired: dict[str, list[str]] = {}
    # pass 1: kāraka nominals and śeṣa
    for nom in frame["nominals"]:
        stem, rel = nom["stem"], nom["rel"]
        if rel in SANJNA:
            sanjna, s_sutra = SANJNA[rel]
            rules = []
            vib, v_sutra = VIBHAKTI[sanjna]
            if (sanjna not in expressed) or not guard_2_3_1:
                rules.append((vib, v_sutra))
            if sanjna in expressed:
                rules.append((1, "2.3.46"))
            fired[stem] = [r[1] for r in rules]
            if guard_2_3_1:
                assert len(rules) == 1, f"conflict on {stem}: {rules}"
            vib, v_sutra = rules[0]
            out[stem] = {"saṃjñā": sanjna, "saṃjñā_sūtra": s_sutra, "vibhakti": vib, "vibhakti_sūtra": v_sutra, "abhihita": sanjna in expressed}
        elif rel == "śeṣa":
            out[stem] = {"saṃjñā": None, "vibhakti": 6, "vibhakti_sūtra": "2.3.50", "abhihita": False}
            fired[stem] = ["2.3.50"]
    # pass 2: attributes agree with their head
    for nom in frame["nominals"]:
        if nom["rel"] == "attr":
            head = out[nom["head"]]
            out[nom["stem"]] = {"saṃjñā": None, "vibhakti": head["vibhakti"], "vibhakti_sūtra": "samānādhikaraṇa(decl)", "head": nom["head"], "abhihita": False}
            fired[nom["stem"]] = ["samānādhikaraṇa(decl)"]
    # implicit kartā expressed by tiṅ: no pada
    if frame["verb"].get("implicit_agent") and frame["verb"]["voice"] == "kartari":
        out["(" + frame["verb"]["implicit_agent"] + ")"] = {"saṃjñā": "kartā", "vibhakti": None, "vibhakti_sūtra": "abhihita by tiṅ (3.4.69); no pada", "abhihita": True}
    return out


GAYATRI_L1 = {
    "verb": {"form": "dhImahi", "voice": "kartari", "person": "uttama", "implicit_agent": "vayam"},
    "nominals": [
        {"stem": "bhargas", "rel": "patient"},
        {"stem": "tad", "rel": "attr", "head": "bhargas"},
        {"stem": "vareNya", "rel": "attr", "head": "bhargas"},
        {"stem": "savitR", "rel": "śeṣa"},
        {"stem": "deva", "rel": "śeṣa"},
    ],
}
GAYATRI_L2 = {
    "verb": {"form": "pracodayAt", "voice": "kartari", "person": "prathama"},
    "nominals": [{"stem": "yad", "rel": "agent"}, {"stem": "dhI", "rel": "patient"}, {"stem": "asmad", "rel": "śeṣa"}],
}
# vibhakti codes the padas carry in theorum/63/65/67 (oracle)
PADA_VIBHAKTI = {"tad": 2, "savitR": 6, "vareNya": 2, "bhargas": 2, "deva": 6, "yad": 1, "dhI": 2, "asmad": 6}
PASSIVE_L1 = {"verb": {"form": "dhIyate", "voice": "karmaṇi", "person": "prathama"}, "nominals": [{"stem": "bhargas", "rel": "patient"}, {"stem": "asmad", "rel": "agent"}, {"stem": "deva", "rel": "śeṣa"}]}


def build_certificate() -> dict[str, Any]:
    a1, a2 = assign(GAYATRI_L1), assign(GAYATRI_L2)
    got = {k: v["vibhakti"] for k, v in {**a1, **a2}.items() if v["vibhakti"] is not None}
    t1 = got == PADA_VIBHAKTI
    implicit_ok = a1["(vayam)"]["abhihita"] and a1["(vayam)"]["vibhakti"] is None
    p = assign(PASSIVE_L1)
    t2 = p["bhargas"]["vibhakti"] == 1 and p["bhargas"]["vibhakti_sūtra"] == "2.3.46" and p["asmad"]["vibhakti"] == 3 and p["asmad"]["vibhakti_sūtra"] == "2.3.18"
    # active again: kartā expressed, karma dvitīyā
    t2b = a1["bhargas"]["vibhakti_sūtra"] == "2.3.2" and a2["yad"]["vibhakti_sūtra"] == "2.3.46"
    # T3 planted: drop 2.3.1 guard in passive -> karma gets dvitīyā
    p_noguard = assign(PASSIVE_L1, guard_2_3_1=False)
    t3 = p_noguard["bhargas"]["vibhakti"] == 2
    # T4 determinism: with guard, exactly one rule per nominal (assert inside assign) -> re-run all frames
    t4 = True
    for fr in (GAYATRI_L1, GAYATRI_L2, PASSIVE_L1):
        try:
            assign(fr)
        except AssertionError:
            t4 = False
    checks = {
        "T1_gayatri_karaka_vibhaktis_equal_pada_vibhaktis": t1,
        "T1_implicit_karta_abhihita_by_ting_no_pada": implicit_ok,
        "T2_voice_switch_flips_ledger_passive_bhargas_1_asmad_3": t2,
        "T2_active_karma_2_3_2_and_expressed_karta_2_3_46": t2b,
        "T3_without_2_3_1_passive_karma_wrongly_dvitiya": t3,
        "T4_exactly_one_vibhakti_rule_per_nominal": t4,
    }
    status = "PASS_KARAKA_VIBHAKTI_CARRIER_CANDIDATE" if all(checks.values()) else "FAIL_KARAKA_VIBHAKTI_CARRIER_CANDIDATE"
    return {
        "schema": "rkf.karaka_vibhakti_carrier_candidate.v1",
        "status": status,
        "gayatri_line1": a1,
        "gayatri_line2": a2,
        "passive_control": p,
        "planted_no_2_3_1": {k: v["vibhakti"] for k, v in p_noguard.items()},
        "sutras_used": ["1.4.24", "1.4.32", "1.4.42", "1.4.45", "1.4.49", "1.4.54", "2.3.1", "2.3.2", "2.3.13", "2.3.18", "2.3.28", "2.3.36", "2.3.46", "2.3.50", "3.4.69"],
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "kāraka saṃjñā + 2.3 vibhakti rules under the abhihita ledger (3.4.69 / 2.3.1) assign to every Gāyatrī nominal exactly the vibhakti its pada carries; the implicit kartā is expressed by the tiṅ and has no pada",
                "voice switch flips the ledger (passive: karma prathamā, kartā tṛtīyā); 2.3.1 load-bearing (planted control)",
                "one vibhakti rule per nominal: the 2.3 sector is conflict-free on these frames",
            ],
            "NOT_claimed": [
                "the semantic relations (agent/patient/śeṣa) are INPUT — declared from the traditional anvaya, not derived from the text",
                "the meaning of the padas, the verb's sense, or any Mīmāṃsā-level obligation (that is the next carrier)",
                "karmapravacanīya, upapada-vibhakti, dvikarmaka verbs, samāsa-internal kāraka",
                "RH, YM untouched",
            ],
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
    print("L1", {k: v["vibhakti"] for k, v in payload["gayatri_line1"].items()}, "L2", {k: v["vibhakti"] for k, v in payload["gayatri_line2"].items()}, "PASSIVE", {k: v["vibhakti"] for k, v in payload["passive_control"].items()})
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
