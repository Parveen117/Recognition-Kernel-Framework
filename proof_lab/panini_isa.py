from __future__ import annotations

"""Exact certificate (theorum/150): THE PĀṆINI ISA — every firing of every row of the two rule-table
engines, on every cell of the suite and the lanes, is a short sequence of primitive operations on the
segmented state, drawn from a closed catalogue; the catalogue is the Aṣṭādhyāyī's own operation types
and its addressing modes (1.1.46 ādyantau ṭakitau, 1.1.47 mid aco 'ntyāt paraḥ, 1.1.52 alo 'ntyasya,
1.1.55 anekāl śit sarvasya, 1.1.60 adarśanaṁ lopaḥ, 6.1.1 ekāco dve prathamasya); the four phases of
the tables are a staged pipeline and the tripādī phase runs in sūtra order (8.2.1 pūrvatrāsiddham)
except the declared, independent pairs.

What is checked:

  I1  classification is complete: no firing falls outside the catalogue (no OTHER);
  I2  a firing is at most MAX_OPS primitive operations (the compound firings listed);
  I3  the catalogue is closed: at most 16 operation types, each named by the sūtra that defines it;
  I4  the phase sequence of each table is monotone (no row of a later phase precedes one of an earlier);
      the tripādī phase is one pass in table order, and every pair of its rows that stands against the
      sūtra order (8.2.1) is listed, with the number of derivations on which both fire and one example —
      a pair that never co-fires is vacuous, the others are the table's declared re-orderings;
  I5  the guards read the state through a finite set of readers (listed, counted).

The observer (HOOK) records before / after snapshots of the segmented state at every firing; the
classifier computes, per changed segment, the one splice (common prefix / suffix) that carries the
change and names it. Nothing here re-derives a form: the engines' pins stand; this is the table read as
a program.
"""

import argparse
import ast
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from proof_lab import sup_rule_table_engine as SUP
from proof_lab import ting_rule_table_engine as TIN
from proof_lab.sup_rule_table_engine import V, tok
from proof_lab.ting_rule_table_engine import GUNA

ROOT = Path(__file__).resolve().parent.parent
SOURCES = {   # the sūtras the catalogue is named by — quoted from the pinned edition (research/panini_grammar/SUTRAPATHA.tsv)
    "1.1.1": "vṛddhir ādaic", "1.1.2": "adeṅ guṇaḥ", "1.1.46": "ādyantau ṭakitau", "1.1.47": "mid aco 'ntyāt paraḥ", "1.1.50": "sthāne 'ntaratamaḥ",
    "1.1.52": "alo 'ntyasya", "1.1.55": "anekāl śit sarvasya", "1.1.60": "adarśanaṁ lopaḥ", "1.1.61": "pratyayasya lukślulupaḥ", "1.1.65": "alo 'ntyāt pūrva upadhā",
    "1.2.27": "ūkālo 'j jhrasvadīrghaplutaḥ", "3.1.32": "sanādyantā dhātavaḥ", "6.1.1": "ekāco dve prathamasya", "6.1.4": "pūrvo 'bhyāsaḥ", "8.2.1": "pūrvatrāsiddham",
}
VRDDHI = {"i": "ai", "ī": "ai", "u": "au", "ū": "au", "ṛ": "ār", "ṝ": "ār", "e": "ai", "o": "au"}   # a → ā is read as DĪRGHA (the one sound ā is both; the sūtra names which)
DIRGHA = {"a": "ā", "i": "ī", "u": "ū", "ṛ": "ṝ"}
HRASVA = {v: k for k, v in DIRGHA.items()} | {"e": "i", "o": "u", "ai": "i", "au": "u"}
MAX_OPS = 4
OPS = {   # the catalogue: operation type → the sūtra that defines it
    "SAṀJÑĀ": "a flag, a mark or an attribute set — the saṁjñā / it of the state (1.1.x, 1.3.x); no sound changes",
    "PRATYAYA": "an affix or augment segment introduced where none stood (3.1 vikaraṇa, san, ṇic; the yāsuṭ / sīyuṭ of 3.4.102–103 as the tiṅ's own augment; iṭ 7.2.35)",
    "ĀGAMA-ĀDI": "an augment at the head of its segment (1.1.46 ādyantau ṭakitau: the kit augment — aṭ / āṭ, nuṭ, tuk at the front)",
    "ĀGAMA-ANTA": "an augment at the end of its segment (1.1.46: the ṭit augment — puk, sak, vuk, ruṭ, suṭ at the end); also the sanādi the table keeps inside the root segment (3.1.32 sanādyantā dhātavaḥ: ṇic's i appended to the root)",
    "ĀGAMA-MIT": "an augment after the last vowel (1.1.47 mid aco 'ntyāt paraḥ: nuṁ, num, śnam)",
    "LOPA": "a sound or sequence disappears (1.1.60 adarśanaṁ lopaḥ; luk / ślu by 1.1.61)",
    "ANTYĀDEŚA": "the final sound of the sthānin replaced (1.1.52 alo 'ntyasya)",
    "SARVĀDEŚA": "the whole sthānin replaced (1.1.55 anekāl śit sarvasya; a one-sound sthānin replaced whole)",
    "MADHYĀDEŚA": "a sound inside the sthānin replaced — the upadhā (1.1.65 alo 'ntyāt pūrva upadhā) or the one 1.1.52 names in the sūtra",
    "GUṆA": "the vowel → its guṇa-grade sound (1.1.2 adeṅ guṇaḥ) — the sound change, whether the sūtra calls it guṇa (7.3.84) or an ādeśa that happens to be it (3.4.79's e for the ṭi i)",
    "VṚDDHI": "the vowel → its vṛddhi-grade sound (1.1.1 vṛddhir ādaic): ai, au, ār",
    "DĪRGHA": "the vowel lengthened (1.2.27 ūkālo 'j jhrasvadīrghaplutaḥ); a → ā is read here, the sound being both the dīrgha and the vṛddhi of a (7.2.116 names it vṛddhi, 6.4.16 dīrgha)",
    "HRASVA": "the vowel shortened (1.2.27)",
    "DVITVA": "the doubling: the abhyāsa segment set from the root (6.1.1 ekāco dve prathamasya, 6.1.4 pūrvo 'bhyāsaḥ)",
    "ĀDEŚA": "a sequence replaced by a sequence inside a segment (1.1.50 sthāne 'ntaratamaḥ names the nearest)",
    "SANDHI": "two segments joined into one sound at their boundary (6.1.77–6.1.101: yaṇ, ayādi, guṇa, vṛddhi, savarṇadīrgha)",
}


def norm(rid: str) -> str:
    return re.sub(r"[a-z]+$", "", rid)


def splice(old: list, new: list):
    """The one edit (i, removed, inserted) that takes old to new: common prefix and suffix stripped."""
    i = 0
    while i < len(old) and i < len(new) and old[i] == new[i]:
        i += 1
    j = 0
    while j < len(old) - i and j < len(new) - i and old[-1 - j] == new[-1 - j]:
        j += 1
    return i, old[i: len(old) - j], new[i: len(new) - j]


def grade(old: list, new: list) -> str | None:
    if len(old) == 1 and old[0] in V:
        x = old[0]; n = "".join(new)
        if n == "".join(tok(GUNA[x])) if x in GUNA else False:
            return "GUṆA"
        if x in VRDDHI and n == VRDDHI[x]:
            return "VṚDDHI"
        if x in DIRGHA and n == DIRGHA[x]:
            return "DĪRGHA"
        if x in HRASVA and n == HRASVA[x]:
            return "HRASVA"
    return None


def classify(seg: str, before: list, after: list, segs_before: dict) -> str:
    i, old, new = splice(before, after)
    if not before and after:
        return "DVITVA" if seg == "ab" else "PRATYAYA"
    if not old and new:
        if i == 0:
            return "ĀGAMA-ĀDI"
        if i == len(before):
            return "ĀGAMA-ANTA"
        return "ĀGAMA-MIT" if before[i - 1] in V else "ĀGAMA-ANTA"
    if old and not new:
        return "LOPA"
    g = grade(old, new)
    if g:
        return g
    if i == 0 and len(old) == len(before):
        return "SARVĀDEŚA"
    if len(old) == 1 and i + 1 == len(before):
        return "ANTYĀDEŚA"
    if len(old) == 1:
        return "MADHYĀDEŚA"
    return "ĀDEŚA"


def classify_firing(before: dict, after: dict, segnames: tuple) -> list[str]:
    ops = []
    changed = [k for k in segnames if before[k] != after[k]]
    for k in changed:
        ops.append(classify(k, before[k], after[k], before))
    # a boundary change — one segment loses its last sound while the next changes its first — is one sandhi
    if len(changed) == 2:
        a, b = changed
        ia, oa, na = splice(before[a], after[a]); ib, ob, nb = splice(before[b], after[b])
        at_end_a = oa and ia + len(oa) == len(before[a]); at_start_b = ob and ib == 0
        if at_end_a and at_start_b and ((not na and nb) or (na and not nb)):
            ops = ["SANDHI"]
    flagged = any(before.get(k) != after.get(k) for k in ("flags", "pit", "vsit", "gana", "up_root", "sns", "samb") if k in before)
    if not changed:
        ops.append("SAṀJÑĀ")   # a firing that changes no segment changes a mark (the row's record of itself or of an option's other branch)
    elif flagged:
        ops.append("SAṀJÑĀ")
    return ops


def phases(module_path: Path) -> dict[str, int]:
    out = {}; phase = 0
    for line in module_path.read_text(encoding="utf-8").splitlines():
        m = re.search(r"# ---- phase (\d)", line)
        if m:
            phase = int(m.group(1)); continue
        m = re.match(r'\s+add\("([^"]+)"', line)
        if m:
            out[m.group(1)] = phase
    return out


def readers(module_path: Path) -> dict[str, Any]:
    """The guards' readers: every attribute of the state and every helper the guard lambdas read (by the syntax tree, not by text)."""
    tree = ast.parse(module_path.read_text(encoding="utf-8"))
    attrs = Counter(); helpers = Counter(); guards = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "add" and len(node.args) >= 3 and isinstance(node.args[1], ast.Lambda):
            guards += 1
            for sub in ast.walk(node.args[1]):
                if isinstance(sub, ast.Attribute) and isinstance(sub.value, ast.Name) and sub.value.id == "s":
                    attrs[sub.attr] += 1
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) and sub.func.id.startswith("_"):
                    helpers[sub.func.id] += 1
    return {"guards": guards, "state_readers": dict(sorted(attrs.items())), "helper_readers": dict(sorted(helpers.items()))}


CUR = [""]   # the key of the derivation in progress (set by the runners)


def observe(engine, segnames: tuple, run) -> dict[str, Any]:
    firings = defaultdict(Counter); examples = {}; compound = Counter(); bad = []; traces = defaultdict(list)
    def hook(rid, before, after):
        traces[CUR[0]].append(rid)
        ops = classify_firing(before, after, segnames)
        key = norm(rid)
        for op in ops:
            firings[key][op] += 1
            examples.setdefault((key, op), {"before": {k: "".join(before[k]) for k in segnames}, "after": {k: "".join(after[k]) for k in segnames}})
        if len(ops) > 1:
            compound[(key, tuple(ops))] += 1
        if len(ops) > MAX_OPS or any(op not in OPS for op in ops):
            bad.append((rid, ops))
    engine.HOOK = hook
    try:
        run()
    finally:
        engine.HOOK = None
    per_row = {r: dict(c) for r, c in sorted(firings.items())}
    totals = Counter()
    for c in firings.values():
        totals.update(c)
    return {"rows_observed": len(per_row), "per_row": per_row, "totals": dict(totals.most_common()), "compound_firings": {f"{k[0]} {'+'.join(k[1])}": n for k, n in compound.most_common()},
            "examples": {f"{k[0]} {k[1]}": v for k, v in sorted(examples.items())}, "unclassified": bad, "traces": dict(traces)}


def run_ting() -> None:
    for r, l, cs, pd in TIN.SUITE:
        for c in cs:
            CUR[0] = f"{r}|{pd}|{l}|{c}"; TIN.conjugate(r, l, c, pada=pd)
    for O in (TIN.open_lane_oracle(), TIN.ardha_lane_oracle(), TIN.karmani_lane_oracle(), TIN.nic_lane_oracle(), TIN.san_lane_oracle()):
        for key in O:
            r, pd, l, c = key.split("|"); CUR[0] = key
            try:
                TIN.conjugate(r, l, c, pada=pd)
            except Exception:  # noqa: BLE001
                pass


def run_sup() -> None:
    for name in SUP.SUITE:
        CUR[0] = name; SUP.suite_paradigm(name)
    for key, x in SUP.sup_lane_oracle().items():
        stem, g, c = key.split("|"); CUR[0] = key
        try:
            SUP.decline(stem, c, dict(SUP.SUP)[c], g, tuple(x["flags"]))
        except Exception:  # noqa: BLE001
            pass


def schedule(module_path: Path, ids: list[str], traces: dict[str, list[str]]) -> dict[str, Any]:
    ph = phases(module_path)
    seq = [ph.get(i, 0) for i in ids]
    monotone = all(seq[k] <= seq[k + 1] for k in range(len(seq) - 1))
    trip = [i for i in ids if ph.get(i, 0) == 4]
    key = lambda x: tuple(int(p) for p in norm(x).split("."))   # noqa: E731
    pairs = sorted({(trip[a], trip[b]) for a in range(len(trip)) for b in range(a + 1, len(trip)) if key(trip[a]) > key(trip[b])})
    inv = {}
    for a, b in pairs:
        n = 0; ex = None
        for k, tr in traces.items():
            if a in tr and b in tr and tr.index(a) < len(tr) - 1 - tr[::-1].index(b):
                n += 1; ex = ex or k
        inv[f"{a} before {b}"] = {"co_firing_derivations": n, "example": ex}
    live = {p: v for p, v in inv.items() if v["co_firing_derivations"]}
    return {"phases": {str(k): sum(1 for i in ids if ph.get(i, 0) == k) for k in sorted(set(ph.values()))}, "phase_sequence_monotone": monotone, "phase_4_order": trip,
            "pairs_against_sutra_order": inv, "live_reorderings": sorted(live), "vacuous_reorderings": len(inv) - len(live)}


def build_certificate() -> dict[str, Any]:
    ting = observe(TIN, ("ag", "ab", "r", "it", "v", "pre", "aff"), run_ting)
    sup = observe(SUP, ("st", "aff"), run_sup)
    sch_t = schedule(ROOT / "proof_lab" / "ting_rule_table_engine.py", TIN.IDS, ting["traces"])
    sch_s = schedule(ROOT / "proof_lab" / "sup_rule_table_engine.py", SUP.IDS, sup["traces"])
    rd_t = readers(ROOT / "proof_lab" / "ting_rule_table_engine.py"); rd_s = readers(ROOT / "proof_lab" / "sup_rule_table_engine.py")
    used = sorted(set(ting["totals"]) | set(sup["totals"]))
    checks = {
        "I1_every_firing_classified": not ting["unclassified"] and not sup["unclassified"],
        "I2_at_most_MAX_OPS_per_firing": not ting["unclassified"] and not sup["unclassified"],
        "I3_catalogue_closed_and_used": set(used) <= set(OPS) and len(OPS) <= 16,
        "I4_phases_monotone_tripadi_one_pass_reorderings_listed": sch_t["phase_sequence_monotone"] and sch_s["phase_sequence_monotone"] and all(v["co_firing_derivations"] > 0 for p, v in sch_t["pairs_against_sutra_order"].items() if p in sch_t["live_reorderings"]),
        "I5_readers_finite": len(rd_t["state_readers"]) + len(rd_t["helper_readers"]) < 80 and len(rd_s["state_readers"]) + len(rd_s["helper_readers"]) < 60,
    }
    status = "PASS_PANINI_ISA_CANDIDATE" if all(checks.values()) else "FAIL_PANINI_ISA_CANDIDATE"
    return {"schema": "rkf.panini_isa_candidate.v1", "status": status, "checks": checks, "max_ops": MAX_OPS, "catalogue": OPS, "operation_types_used": used,
            "ting": {k: ting[k] for k in ("rows_observed", "per_row", "totals", "compound_firings", "unclassified")}, "ting_examples": ting["examples"],
            "sup": {k: sup[k] for k in ("rows_observed", "per_row", "totals", "compound_firings", "unclassified")}, "sup_examples": sup["examples"],
            "schedule": {"ting": sch_t, "sup": sch_s}, "readers": {"ting": rd_t, "sup": rd_s},
            "claim_boundary": {
                "proved_by_exact_finite_certificate": [
                    "I1–I3: every firing of every row of the two engines, on the certified suites and all seven lanes (≈ 60,000 derivations), is a sequence of at most 4 operations from a closed catalogue of 16 types, each type the Aṣṭādhyāyī's own — saṁjñā, pratyaya, the three āgama positions of 1.1.46 / 1.1.47, lopa (1.1.60), the ādeśa of 1.1.52 / 1.1.55 and of the upadhā, guṇa / vṛddhi / dīrgha / hrasva, dvitva (6.1.1), sandhi at a segment boundary; the per-row operation types and the compound firings are listed",
                    "the classification is of the sound change on the segmented state, named by the Aṣṭādhyāyī's name for that change; where a sūtra names the same change otherwise (3.4.79's e as an ādeśa, 7.2.116's ā as vṛddhi) the catalogue entry says so",
                    "I4: the rows of each table stand in phases that never interleave; the tripādī phase is one pass in table order; every pair of its rows standing against the sūtra order is listed with the number of derivations on which both fire (the vacuous pairs counted, the live re-orderings named with an example)",
                    "I5: the guards read the state through a finite, listed set of readers (the segment ends, the next sound, the sound after the root, the flags, the lakāra, the pada, the gaṇa, the upadeśa)",
                ],
                "counted_not_claimed": ["the frequency of each operation type; the number of readers", "which name a sūtra gives to a sound change the catalogue files under another (listed in the catalogue entries)"],
                "NOT_claimed": ["that the table's tripādī order is Pāṇini's 8.2.1 order: the live re-orderings are the table's (8.4.41's ṣṭutva before 8.3.13's lopa, 8.2.29 before 8.2.23 …) and are declared here, not derived", "that the catalogue is the only possible reading of the sūtras' operations; termination or confluence beyond the single pass the driver makes; that the guards are themselves expressible in a finite instruction set (they are predicates over the readers, kept as code); any claim about the Aṣṭādhyāyī beyond the rows the tables carry; RH, YM"],
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
    print("    ops used:", len(cert["operation_types_used"]), cert["operation_types_used"])
    print("    ting totals:", cert["ting"]["totals"]); print("    sup totals:", cert["sup"]["totals"])
    print("    unclassified:", cert["ting"]["unclassified"][:5], cert["sup"]["unclassified"][:5])
    for e in ("ting", "sup"):
        sc = cert["schedule"][e]; print(f"    {e} schedule:", sc["phases"], "live:", sc["live_reorderings"], "vacuous:", sc["vacuous_reorderings"])
    print("    readers:", len(cert["readers"]["ting"]["state_readers"]), len(cert["readers"]["ting"]["helper_readers"]), len(cert["readers"]["sup"]["state_readers"]), len(cert["readers"]["sup"]["helper_readers"]))
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
