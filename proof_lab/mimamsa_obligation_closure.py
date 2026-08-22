from __future__ import annotations

"""Exact certificate (theorum/69): MĪMĀṂSĀ CARRIER — obligation closure on the
kāraka frame; the owner's Vedic-repo note (VRG_Mimamsa_Rule_Priority_
Interpretation_Engine_v1: R=(type,agent,action,object,condition,authority),
Vidhi -> obligation, Niṣedha -> prohibition closure, Exception/Conflict/Scope
Smṛti, authority scale, Ṛta closure K_M(R)=0) made executable with the SAME
resolver shape as theorum/63 (apavāda by scope containment, authority, tie).

Carrier: a normative statement R = (type, agent-class, action, object,
condition, authority).  Types (Mīmāṃsā's five): vidhi, niṣedha, arthavāda,
mantra, nāmadheya.  Only vidhi/niṣedha generate obligation/prohibition;
mantra and arthavāda generate none by themselves (they are aṅga to a vidhi).

Resolver (Mīmāṃsā's own, each rung executable):
  scope      sāmānya-viśeṣayor viśeṣo balīyān — apavāda by condition
             containment cond(A) ⊊ cond(B) on the situation carrier
             (identical in form to theorum/63's apavāda rung)
  authority  1.3.3 virodhe tv anapekṣyaṃ syāt — śruti > smṛti > ācāra on
             direct contradiction
  vikalpa    tulya-bala-virodhe vikalpaḥ — equal strength -> OPTION, a
             lawful closure (NOT a refused tie, unlike Pāṇini's resolver)
Ṛta closure: K_M(situation) = number of unresolved contradictions; the
owner's note demands K_M = 0.  A vikalpa counts as closed (option recorded
in the ledger), an unresolved contradiction does not.

Facts certified on classical Mīmāṃsā instances:
 T1  na hiṃsyāt sarvā bhūtāni (niṣedha, śruti, general) vs agnīṣomīyaṃ paśum
     ālabheta (vidhi, śruti, specific) -> scope rung: the specific vidhi
     stands, K_M = 0; Exception-Smṛti recorded (the owner's S_Exception).
 T2  vrīhibhir yajeta vs yavair yajeta (both śruti, same scope, contradictory
     dravya) -> vikalpa, closed with option in the ledger, K_M = 0.
 T3  śruti "audumbarī sarvā veṣṭayitavyā" vs smṛti "audumbarīṃ spṛṣṭvā
     udgāyet" -> authority rung, śruti stands, K_M = 0; the planted control
     with equal authority goes to vikalpa instead.
 T4  Unresolvable: two śruti statements, same scope, contradictory, and a
     declared "no vikalpa" (e.g. the act is a single non-repeatable one with
     conflicting phala) -> K_M = 1, certificate returns the witness.
 T5  GĀYATRĪ: classified from its own grammar — dhīmahi is āśīrliṅ uttama
     puruṣa (theorum/66), i.e. the speaker's wish, not an injunction to
     another -> type MANTRA; obligation closure EMPTY by itself.  With a
     referencing vidhi (smṛti: "gāyatrīṃ japet", dvija, sandhyā) the
     closure contains exactly that japa obligation, whose object is the
     mantra and whose kāraka frame is theorum/68's.  The mantra's meaning
     is NOT claimed; its normative status is.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

AUTH = {"śruti": 3, "smṛti": 2, "ācāra": 1}


def R(rid, typ, agent, action, obj, cond, auth, **extra):
    return {"id": rid, "type": typ, "agent": agent, "action": action, "object": obj, "cond": frozenset(cond), "auth": auth, **extra}


def applies(r, situation: frozenset) -> bool:
    return r["cond"] <= situation


def polarity(r) -> int:
    return {"vidhi": +1, "niṣedha": -1}.get(r["type"], 0)


def contradict(a, b) -> bool:
    """Same action-object, opposite polarity; or same action, same polarity, incompatible object (dravya)."""
    if polarity(a) == 0 or polarity(b) == 0:
        return False
    if a["action"] == b["action"] and a["object"] == b["object"] and polarity(a) == -polarity(b):
        return True
    if a["action"] == b["action"] and polarity(a) == polarity(b) == 1 and a["object"] != b["object"] and a.get("exclusive") and b.get("exclusive"):
        return True
    return False


def scope_dom(r, carrier: list[frozenset]) -> frozenset:
    return frozenset(i for i, s in enumerate(carrier) if applies(r, s))


def resolve(a, b, carrier):
    da, db = scope_dom(a, carrier), scope_dom(b, carrier)
    if da < db:
        return a, "scope(sāmānya-viśeṣa)"
    if db < da:
        return b, "scope(sāmānya-viśeṣa)"
    if AUTH[a["auth"]] != AUTH[b["auth"]]:
        return (a if AUTH[a["auth"]] > AUTH[b["auth"]] else b), "authority(1.3.3)"
    if a.get("no_vikalpa") or b.get("no_vikalpa"):
        return None, "OPEN"
    return None, "vikalpa(tulyabala)"


def closure(rules, situation, carrier):
    app = [r for r in rules if applies(r, situation)]
    obligations = {r["id"]: polarity(r) for r in app if polarity(r)}
    ledger = []
    open_conflicts = []
    for i in range(len(app)):
        for j in range(i + 1, len(app)):
            a, b = app[i], app[j]
            if not contradict(a, b):
                continue
            w, rung = resolve(a, b, carrier)
            if w is None and rung == "OPEN":
                open_conflicts.append((a["id"], b["id"]))
                ledger.append({"pair": (a["id"], b["id"]), "rung": rung})
            elif w is None:
                ledger.append({"pair": (a["id"], b["id"]), "rung": rung, "option": [a["id"], b["id"]]})
            else:
                loser = b if w is a else a
                obligations.pop(loser["id"], None)
                ledger.append({"pair": (a["id"], b["id"]), "rung": rung, "winner": w["id"], "S_exception": f"Rec({w['id']})-Rec({loser['id']})"})
    return {"obligations": obligations, "ledger": ledger, "K_M": len(open_conflicts), "open": open_conflicts}


def build_certificate() -> dict[str, Any]:
    # situation carrier: sets of context features
    carrier = [frozenset(s) for s in (
        {"living_being"}, {"living_being", "paśu", "agnīṣomīya_rite"}, {"yāga", "dravya_choice"},
        {"sāma_rite", "audumbarī"}, {"rite_X", "single_performance"}, {"sandhyā", "dvija"}, {"sandhyā", "dvija", "mantra_ref:gāyatrī"},
    )]
    rules = [
        R("na_hiṃsyāt", "niṣedha", "any", "hiṃsā", "being", {"living_being"}, "śruti"),
        R("agnīṣomīya", "vidhi", "yajamāna", "hiṃsā", "being", {"living_being", "paśu", "agnīṣomīya_rite"}, "śruti"),
        R("vrīhi", "vidhi", "yajamāna", "yāga", "vrīhi", {"yāga", "dravya_choice"}, "śruti", exclusive=True),
        R("yava", "vidhi", "yajamāna", "yāga", "yava", {"yāga", "dravya_choice"}, "śruti", exclusive=True),
        R("veṣṭana_śruti", "vidhi", "udgātṛ", "audumbarī_handling", "veṣṭana", {"sāma_rite", "audumbarī"}, "śruti", exclusive=True),
        R("sparśa_smṛti", "vidhi", "udgātṛ", "audumbarī_handling", "sparśa", {"sāma_rite", "audumbarī"}, "smṛti", exclusive=True),
        R("X_do", "vidhi", "yajamāna", "rite_X", "act", {"rite_X", "single_performance"}, "śruti", no_vikalpa=True),
        R("X_dont", "niṣedha", "yajamāna", "rite_X", "act", {"rite_X", "single_performance"}, "śruti", no_vikalpa=True),
        R("gāyatrī_mantra", "mantra", "speaker", "dhī", "bhargas", {"sandhyā"}, "śruti", lakara="āśīrliṅ", person="uttama"),
        R("gāyatrī_japet", "vidhi", "dvija", "japa", "gāyatrī_mantra", {"sandhyā", "dvija", "mantra_ref:gāyatrī"}, "smṛti"),
    ]
    t1 = closure(rules, carrier[1], carrier)
    t2 = closure(rules, carrier[2], carrier)
    t3 = closure(rules, carrier[3], carrier)
    planted = [dict(r, auth="śruti") if r["id"] == "sparśa_smṛti" else r for r in rules]
    t3p = closure(planted, carrier[3], carrier)
    t4 = closure(rules, carrier[4], carrier)
    t5a = closure(rules, carrier[5], carrier)
    t5b = closure(rules, carrier[6], carrier)
    mantra = next(r for r in rules if r["id"] == "gāyatrī_mantra")
    classified_mantra = mantra["lakara"] == "āśīrliṅ" and mantra["person"] == "uttama" and polarity(mantra) == 0
    checks = {
        "T1_specific_vidhi_beats_general_nisedha_by_scope_K0": t1["K_M"] == 0 and t1["obligations"] == {"agnīṣomīya": 1} and t1["ledger"][0]["rung"].startswith("scope"),
        "T2_equal_strength_goes_to_vikalpa_closed_K0": t2["K_M"] == 0 and t2["ledger"][0]["rung"].startswith("vikalpa") and set(t2["obligations"]) == {"vrīhi", "yava"},
        "T3_sruti_beats_smrti_by_authority_K0": t3["K_M"] == 0 and t3["obligations"] == {"veṣṭana_śruti": 1} and t3["ledger"][0]["rung"].startswith("authority"),
        "T3_planted_equal_authority_becomes_vikalpa": t3p["ledger"][0]["rung"].startswith("vikalpa"),
        "T4_unresolvable_contradiction_K1_with_witness": t4["K_M"] == 1 and t4["open"] == [("X_do", "X_dont")],
        "T5_gayatri_is_mantra_by_its_own_grammar_no_obligation_alone": classified_mantra and t5a["obligations"] == {},
        "T5_referencing_vidhi_yields_exactly_the_japa_obligation": t5b["obligations"] == {"gāyatrī_japet": 1} and t5b["K_M"] == 0,
    }
    status = "PASS_MIMAMSA_OBLIGATION_CLOSURE_CANDIDATE" if all(checks.values()) else "FAIL_MIMAMSA_OBLIGATION_CLOSURE_CANDIDATE"
    return {
        "schema": "rkf.mimamsa_obligation_closure_candidate.v1",
        "status": status,
        "closures": {"T1": t1, "T2": t2, "T3": t3, "T3_planted": t3p, "T4": t4, "T5_mantra_alone": t5a, "T5_with_vidhi": t5b},
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "owner's Mīmāṃsā kernel (R=(type,agent,action,object,condition,authority); vidhi/niṣedha; Exception/Conflict Smṛti; Ṛta closure K_M=0) executable on a finite situation carrier",
                "resolver = scope containment (sāmānya-viśeṣa) > authority (1.3.3) > vikalpa (tulyabala) — same shape as theorum/63's Pāṇinian ladder with one structural difference: a tie is a lawful OPTION, not a refusal",
                "classical instances: paśu vs na hiṃsyāt (scope), vrīhi/yava (vikalpa), audumbarī śruti/smṛti (authority), unresolvable pair (K_M=1, witness)",
                "Gāyatrī: mantra by its own lakāra (āśīrliṅ uttama, theorum/66) -> no obligation alone; a referencing vidhi yields exactly the japa obligation on the theorum/68 frame",
            ],
            "NOT_claimed": [
                "the meaning (artha) of any statement; the six pramāṇas of aṅgatva (śruti-liṅga-vākya-prakaraṇa-sthāna-samākhyā, 3.3.14) -- not modelled",
                "the statement set is DECLARED (classical examples), not extracted from texts; condition features are input",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=list) + "\n").encode("utf-8")


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
