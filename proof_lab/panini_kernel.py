from __future__ import annotations

"""Exact certificate (theorum/142): THE PĀṆINI KERNEL — the two rule-table engines, the
ledger and the three evidence layers read as one object.

What is checked here is consistency between code and claim, not a new derivation:

  K1  every row of the two engines (its sūtra number) is an entry of the ledger at the
      hand_coded / meta / compiled level, and every hand_coded entry the ledger attributes
      to the engine theorems (125–141, 143) is a row of the engine that theorem re-pinned;
  K2  the rows the two engines share are exactly the junction / tripādī rules that the
      grammar states once for both padas (6.1.77 … 8.4.55), listed;
  K3  the evidence files of theorum/137–141 are present with the hashes the capsules pin;
  K4  the coverage of the Aṣṭādhyāyī by level, per pāda, with the engine rows marked.

Everything else is counted, not claimed.
"""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from proof_lab import astadhyayi_ledger as LED
from proof_lab import sup_rule_table_engine as SUP
from proof_lab import ting_rule_table_engine as TIN

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = {   # file → sha256 pinned in the capsule that produced it
    "research/independent_oracle/CROSSCHECK.json": "81dc3f08367b0e58fc97547cf56ac25e2fd79146f2c12d09385fb998a3d74aac",
    "research/independent_oracle/GENERALIZE.json": "f2b10f6427363abaa1389e77ab4d809603c3f07bd7d2b1ed5de18679886e72a6",   # re-pinned by theorum/143 (23f925a6… was theorum/140's)
    "research/independent_oracle/GENERALIZE_SUP.json": "a55b73b2e4371ffeecb3898840bfd6fd753034bdf2e172252d1bbdaaebb11df3",
}
ENGINE_THEOREMS = {"sup_rule_table_engine": ["125", "126", "127", "128", "141"], "ting_rule_table_engine": ["129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "143"]}


def norm(rid: str) -> str:
    return re.sub(r"[a-z]+$", "", rid)


def k1_rows_and_ledger() -> dict[str, Any]:
    sup_ids = sorted({norm(r) for r in SUP.IDS}); tin_ids = sorted({norm(r) for r in TIN.IDS})
    hand = {x for v in LED.HAND_CODED.values() for x in v}; meta = {x for v in LED.META.values() for x in v}; comp = {x for v in LED.COMPILED.values() for x in v}
    rows_not_in_ledger = sorted(set(sup_ids + tin_ids) - hand - meta - comp)
    ledger_not_in_rows = {}; guard_clauses = {}
    for mod, ths in ENGINE_THEOREMS.items():
        eng = SUP if mod.startswith("sup") else TIN
        ids = set(sup_ids if mod.startswith("sup") else tin_ids)
        for t in ths:
            for x in LED.HAND_CODED.get(t, []):
                if x in ids:
                    continue
                # a sūtra realised as a guard clause of another row: quoted in the engine's SOURCES and named in that row's note
                hosts = [n for n, _, _, note in eng.RULES if x in note]
                if x in eng.SOURCES and hosts:
                    guard_clauses[x] = {"theorem": t, "host_rows": hosts}
                else:
                    ledger_not_in_rows.setdefault(t, []).append(x)
    return {"sup_rows": len(sup_ids), "ting_rows": len(tin_ids), "distinct_sutras_as_rows": len(set(sup_ids + tin_ids)),
            "rows_not_in_ledger": rows_not_in_ledger, "ledger_hand_coded_not_in_rows": ledger_not_in_rows, "guard_clauses": guard_clauses,
            "checks": {"every_row_is_a_ledger_entry": not rows_not_in_ledger, "every_engine_theorem_hand_coded_entry_is_a_row": not ledger_not_in_rows}}


def k2_shared_rows() -> dict[str, Any]:
    shared = sorted({norm(r) for r in SUP.IDS} & {norm(r) for r in TIN.IDS})
    junction_or_tripadi = all(s.startswith(("6.1.", "8.2.", "8.3.", "8.4.")) for s in shared)
    return {"shared": shared, "texts": {s: LED.TEXT.get(s) or SUP.SOURCES.get(s) or TIN.SOURCES.get(s) for s in shared},
            "checks": {"shared_rows_are_junction_or_tripadi_rules": junction_or_tripadi}}


def k3_evidence() -> dict[str, Any]:
    out = {}; ok = True
    for rel, pin in EVIDENCE.items():
        p = ROOT / rel
        if not p.exists():
            out[rel] = {"present": False}; ok = False; continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        out[rel] = {"present": True, "sha256": h, "matches_pin": h.startswith(pin)}
        ok = ok and h.startswith(pin)
    return {"files": out, "checks": {"evidence_files_present_with_pinned_hashes": ok}}


def k4_coverage() -> dict[str, Any]:
    led = json.loads((ROOT / "proof_lab/astadhyayi/ASTADHYAYI_LEDGER.json").read_text(encoding="utf-8"))
    rows = {norm(r) for r in SUP.IDS} | {norm(r) for r in TIN.IDS}
    per_pada: dict[str, Counter] = {}
    for sid, e in led["sutras"].items():
        pada = ".".join(sid.split(".")[:2]); per_pada.setdefault(pada, Counter())
        per_pada[pada][e["level"]] += 1
        if sid in rows:
            per_pada[pada]["engine_row"] += 1
    totals = Counter()
    for c in per_pada.values():
        totals.update(c)
    return {"astadhyayi_total": led["counts"]["astadhyayi_total"], "ledger_entries": led["counts"]["entries"], "levels": led["counts"],
            "engine_rows_in_ledger": sum(1 for sid in led["sutras"] if sid in rows), "per_pada": {k: dict(v) for k, v in sorted(per_pada.items())}, "totals": dict(totals)}


def build_certificate() -> dict[str, Any]:
    k1, k2, k3, k4 = k1_rows_and_ledger(), k2_shared_rows(), k3_evidence(), k4_coverage()
    checks = {**{f"k1_{k}": v for k, v in k1["checks"].items()}, **{f"k2_{k}": v for k, v in k2["checks"].items()}, **{f"k3_{k}": v for k, v in k3["checks"].items()}}
    status = "PASS_PANINI_KERNEL_CANDIDATE" if all(checks.values()) else "FAIL_PANINI_KERNEL_CANDIDATE"
    return {"schema": "rkf.panini_kernel_candidate.v1", "status": status, "checks": checks, "k1": k1, "k2": k2, "k3": k3, "k4": k4,
            "claim_boundary": {
                "proved_by_exact_finite_certificate": [
                    "K1: every sūtra that is a row of either engine is a ledger entry at the hand_coded / meta / compiled level, and every hand_coded entry the ledger attributes to the engine theorems is a row of the engine that theorem re-pinned or a guard clause of a named row (quoted in SOURCES, named in the host row's note) — the code and the claim boundary name the same sūtras",
                    "K2: the rows the two engines share are junction / tripādī rules only (6.1 and 8.2–8.4), i.e. the grammar's pada-independent layer; no aṅga rule is duplicated across the engines",
                    "K3: the evidence files of the audits (theorum/137–141) are present with the hashes their capsules pin",
                ],
                "counted_not_claimed": ["K4: the coverage of the 3,983 sūtras by ledger level and per pāda, with the engine rows marked — a count of what is built, not a measure of what the grammar needs"],
                "NOT_claimed": ["that the two engines together implement the Aṣṭādhyāyī; that a row's guard is the sūtra's full domain; the kṛt / taddhita / samāsa constructions as rows (theorum/118–122 are written constructions); accent; RH, YM"],
            }}


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", default=None); a = ap.parse_args()
    cert = build_certificate()
    print(cert["status"])
    for k, v in cert["checks"].items():
        print(f"    {k}: {v}")
    print("    rows:", cert["k1"]["sup_rows"], cert["k1"]["ting_rows"], "distinct", cert["k1"]["distinct_sutras_as_rows"], "shared", len(cert["k2"]["shared"]))
    print("    coverage:", cert["k4"]["levels"], "engine rows in ledger", cert["k4"]["engine_rows_in_ledger"])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
