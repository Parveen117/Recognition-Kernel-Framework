"""Direct PG2 source/linguistic controls. No CI, historical replay or certificates.

Usage: python3.12 research/panini_grammar/verification/verify.py \
         --source-root /path/to/ashtadhyayi-data [--write]

Without --write, reproduce and compare the checked-in report. Unknown grammar
is reported as unknown. A successful run is not a Sanskrit soundness proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

from marker_review import designate, root_projection_audit
from source_audit import (SOURCE_COMMIT, SOURCE_FILES, code_census, digest,
                          lexical_report, load, scope_graph, scope_report)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASELINE = "ada439f6ba3109d798b41c216fe7cedc79e60afb"


def evidence_records(value):
    if isinstance(value, dict):
        if {"path", "key", "anchor"} <= value.keys():
            yield value
        for child in value.values():
            yield from evidence_records(child)
    elif isinstance(value, list):
        for child in value:
            yield from evidence_records(child)


def verify_evidence(packet, source_root):
    cache = {}
    count = 0
    for evidence in evidence_records(packet):
        path = evidence["path"]
        if path not in SOURCE_FILES:
            raise ValueError(f"Unpinned source: {path}")
        if path not in cache:
            cache[path] = load(source_root / path)
        source = cache[path]
        key = evidence["key"]
        if "data" in source and isinstance(source["data"], list):
            rows = [r for r in source["data"] if str(r.get("i", r.get("num", r.get("ind")))) == key]
            if len(rows) != 1:
                raise ValueError(f"Nonunique source identity: {path}:{key}")
            source = rows[0]
        else:
            source = source[key]
        if evidence.get("field"):
            source = source[evidence["field"]]
        if not isinstance(source, str) or not evidence["anchor"] or evidence["anchor"] not in source:
            raise ValueError(f"Citation anchor not found: {path}:{key}: {evidence['anchor']}")
        count += 1
    return count


def inheritance_view(facts, contracts):
    """A query-local view only. Actual replacement/history never changes."""
    required = {"is_substitute", "phoneme_dependent", "original_vowel", "following_cause",
                "acts_on_preceding", "replacement", "query", "varac_context",
                "cause_vowel_initial", "cause_is_reduplication_trigger", "reduplication_kind"}
    if not required <= facts.keys():
        return "UNRESOLVED"
    by_id = {r["id"]: r for r in contracts["rules"]}
    admits = lambda r: all(facts.get(k) == v for k, v in r["requires"].items())
    for sid in ("1.1.59", "1.1.56"):
        if admits(by_id[sid]):
            return by_id[sid]["result"]
    if not admits(by_id["1.1.57"]):
        return "NOT_LICENSED_BY_REVIEWED_RULES"
    restriction = by_id["1.1.58"]
    blocked = (facts["query"] in restriction["always_blocked_queries"]
               or (facts["query"] in restriction["deletion_only_queries"] and facts["replacement"] == "deletion")
               or facts[restriction["blocked_replacement_context"]])
    return "SUBSTITUTE_VIEW_1.1.58" if blocked else by_id["1.1.57"]["result"]


def witnessed_priority(case, witnesses):
    """No edge, no winner. Equal-strength or nitya is never assumed by default."""
    candidates, facts = set(case["candidates"]), case["facts"]
    active = {(r["winner"], r["loser"]) for r in witnesses["edges"]
              if all(k in facts and facts[k] == value for k, value in r["requires"].items())}
    winners = [a for a in candidates if all((a, b) in active for b in candidates if b != a)]
    return winners[0] if len(candidates) >= 2 and len(winners) == 1 else "UNRESOLVED"


def run_cases(cases, rules, inheritance, priority):
    results = []
    for case in cases["markers"]:
        actual = designate(case["input"], rules)
        reduced = {"status": actual["status"]}
        if actual["status"] == "LOCAL_DESIGNATION":
            reduced.update(it_only_projection=actual["it_only_projection"],
                           markers=[[entry["symbol"], sid] for entry in actual["it"] for sid in entry["rules"]])
            if "marker_units" in case["expected"]:
                reduced["marker_units"] = [unit["label"] for unit in actual["marker_units"]]
        results.append({"id": case["id"], "kind": "marker", "agrees": reduced == case["expected"],
                        "actual": reduced, "expected": case["expected"]})
    for case in cases["inheritance"]:
        before = digest(case["input"])
        actual = inheritance_view(case["input"], inheritance)
        results.append({"id": case["id"], "kind": "inheritance", "agrees": actual == case["expected"],
                        "actual": actual, "expected": case["expected"],
                        "history_unmodified": before == digest(case["input"])})
    for case in cases["priority"]:
        actual = witnessed_priority(case["input"], priority)
        results.append({"id": case["id"], "kind": "priority", "agrees": actual == case["expected"],
                        "actual": actual, "expected": case["expected"]})
    return results


def scope_controls(graph, adjudications):
    checks = []
    for item in adjudications["positive_context_controls"]:
        present = any(all(edge[k] == v for k, v in item.items()) for edge in graph["contexts"][item["target"]])
        checks.append({"id": f"{item['target']}:{item['source']}:{item['term']}", "agrees": present})
    checks.append({"id": "1.4.13-is-not-a-heading", "agrees": "1.4.13" not in graph["headings"]})
    checks.append({"id": "3.1.68-does-not-import-yang", "agrees": not any("यङ्" in e["term"] for e in graph["contexts"]["3.1.68"])})
    anomalies = {"outside_endpoint": graph["edges_outside_declared_heading_range"],
                 "not_AD": graph["scope_sources_without_AD_tag"]}
    reviewed = set()
    for i, group in enumerate(adjudications["groups"]):
        matching = [e for e in anomalies[group["flag"]] if e["source"] == group["source"]
                    and ("target" not in group or e["target"] == group["target"])]
        checks.append({"id": f"anomaly-group-{i}", "agrees": len(matching) == group["count"]})
        reviewed.update(digest(e) for e in matching)
    checks.append({"id": "all-structural-flags-have-review-records", "agrees": reviewed == {digest(e) for group in anomalies.values() for e in group}})
    return checks


def structural_controls(cases, rules, inheritance, priority):
    """Adverse controls prevent the specific shortcuts identified in the sources."""
    indexed = {c["id"]: c for c in cases["markers"]}
    gam = designate(indexed["gam-original-final"]["input"], rules)
    ordinary = designate(indexed["ordinary-nasal-a"]["input"], rules)
    jhi = designate(indexed["jhi-affix-identity"]["input"], rules)
    missing = {**indexed["jas-final-s-protected"]["input"]}
    del missing["vibhakti"]
    # A name shared by two events does not establish same-word, same-lakṣaṇa
    # nityatva. These are schema rejection controls, not a nitya classifier.
    event_keys = ("operation", "target_identity", "licensing_rule", "accent")
    def same_event(a, b):
        return all(k in a and k in b and a[k] == b[k] for k in event_keys)
    before = {"operation": "aṭ", "target_identity": "dhatu", "licensing_rule": "6.4.71", "accent": "same"}
    after = {**before, "target_identity": "vikarananta"}
    idit = designate(indexed["bhid-simple-idit"]["input"], rules)
    irit = designate(indexed["bhid-compound-irit"]["input"], rules)
    return [
        {"id": "gam-no-rescan", "agrees": gam["it_only_projection"] == "gam" and gam["original"][-2]["id"] in gam["visible_ids"]},
        {"id": "ordinary-nasality-retained", "agrees": ordinary["original"][0]["nasal"] and ordinary["visible_ids"] == [0]},
        {"id": "jhi-origin-survives-it-projection", "agrees": jhi["identity"] == "jhi-affix-identity" and jhi["original"][0]["symbol"] == "jh"},
        {"id": "same-projection-does-not-mean-same-marker", "agrees": idit["it_only_projection"] == irit["it_only_projection"] == "bhid" and [u["label"] for u in idit["marker_units"]] == ["i"] and [u["label"] for u in irit["marker_units"]] == ["ir"]},
        {"id": "unknown-vibhakti-not-false", "agrees": designate(missing, rules)["status"] == "UNRESOLVED"},
        {"id": "missing-inheritance-facts-not-false", "agrees": inheritance_view({}, inheritance) == "UNRESOLVED"},
        {"id": "nitya-target-identity-matters", "agrees": not same_event(before, after), "basis": "Paribhāṣenduśekhara 43; schema control only"},
        {"id": "nitya-laksana-identity-matters", "agrees": not same_event(before, {**before, "licensing_rule": "different"}), "basis": "Paribhāṣenduśekhara 45; schema control only"},
        {"id": "nitya-accent-identity-matters", "agrees": not same_event(before, {**before, "accent": "different"}), "basis": "Paribhāṣenduśekhara 49; schema control only"},
        {"id": "no-evidence-no-priority", "agrees": witnessed_priority({"candidates": ["1.1.1", "8.4.68"], "facts": {}}, priority) == "UNRESOLVED"},
    ]


def legacy_context_probes():
    """Three new counterexample probes, not a replay of any old test campaign."""
    sys.path.insert(0, str(ROOT))
    from proof_lab.paninian_instruction_format import SANDHI_RECORDS, compile_sandhi, _priority_nf
    compiled = [(r["sid"], compile_sandhi(r)) for r in SANDHI_RECORDS]
    return [
        {"junction": list(pair), "bare_T80_result": list(_priority_nf(pair, compiled)),
         "contextual_required_junction": expected, "context": context, "source": source,
         "status": "CONFIRMED_MISSING_CONTEXT_INTERFACE"}
        for pair, expected, context, source in (
            (("a", "a"), ["a"], "pac-a + anti, apadānta thematic a before guṇa", "Kāśikā 6.1.97: pacanti"),
            (("e", "a"), ["e"], "agne + atra, padānta e before short a", "Kāśikā 6.1.109: agne'tra"),
            (("o", "a"), ["o"], "vāyo + atra, padānta o before short a", "Kāśikā 6.1.109: vāyo'tra"),
        )]


def build_report(source_root):
    pins = load(HERE / "SOURCE_PINS.json")
    for path, expected in pins["external_sha256"].items():
        if hashlib.sha256((source_root / path).read_bytes()).hexdigest() != expected:
            raise ValueError(f"Source changed: {path}")
    for path, expected in pins["baseline_code_sha256"].items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            raise ValueError(f"Baseline code changed: {path}; a new review is needed")
    names = ("MARKER_RULES.json", "INHERITANCE_RULES.json", "PRIORITY_WITNESSES.json", "ORACLE_CASES.json", "SCOPE_ADJUDICATIONS.json")
    packets = {name: load(HERE / name) for name in names}
    citation_count = sum(verify_evidence(packet, source_root) for packet in packets.values())
    rules = packets["MARKER_RULES.json"]
    contracts = packets["INHERITANCE_RULES.json"]
    priority = packets["PRIORITY_WITNESSES.json"]
    cases = packets["ORACLE_CASES.json"]
    raw = load(source_root / "sutraani/data.txt")["data"]
    graph = scope_graph(raw)
    case_results = run_cases(cases, rules, contracts, priority)
    controls = scope_controls(graph, packets["SCOPE_ADJUDICATIONS.json"]) + structural_controls(cases, rules, contracts, priority)
    probes = legacy_context_probes()
    if not all(p["bare_T80_result"] != p["contextual_required_junction"] for p in probes):
        raise ValueError("Expected legacy boundary counterexample changed; inspect the changed claim")
    failures = [r["id"] for r in case_results + controls if not r["agrees"]]
    return {
        "stage": "PG2", "author": "Monty", "review_date": "2026-11-01",
        "baseline_commit": BASELINE, "primary_source_commit": SOURCE_COMMIT,
        "verification_status": "LOCAL_REFERENCE_CHECKS_AGREE" if not failures else "REVIEW_FAILURE",
        "grammar_status": "NOT_COMPLETE", "valid_sanskrit_oracle": False,
        "source_anchors_checked": citation_count,
        "input_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                         for name in (*names, "SOURCE_PINS.json", "verify.py", "source_audit.py", "marker_review.py")},
        "scope": scope_report(raw), "legacy_code": code_census(ROOT),
        "lexical": lexical_report(source_root),
        "root_it_only_diagnostic": root_projection_audit(load(source_root / "dhatu/data.txt")["data"], rules),
        "case_counts": dict(Counter(r["kind"] for r in case_results)),
        "case_results": case_results, "structural_controls": controls,
        "legacy_context_probes": probes, "failures": failures,
        "not_claimed": ["Whole-sūtra semantic coverage from source presence or successful fixtures",
                        "Raw Sanskrit scope or instruction compilation", "Universal resolver, soundness or completeness",
                        "Independent philological review or cross-edition agreement", "Quantum-calculator integration"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--write", action="store_true", help="Write this new stage's report; never changes historical evidence")
    args = parser.parse_args()
    report = build_report(args.source_root)
    target = HERE / "VERIFICATION_RESULT.json"
    if args.write:
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    elif not target.is_file() or load(target) != report:
        raise SystemExit("PG2 report differs; inspect before explicitly writing a revised report")
    print(json.dumps({k: report[k] for k in ("verification_status", "grammar_status", "source_anchors_checked", "case_counts", "failures")}, ensure_ascii=False))
    print("Scope flags:", len(report["scope"]["edges_outside_declared_heading_range"]), "+", len(report["scope"]["scope_sources_without_AD_tag"]))
    print("Root marker-only diagnostic:", report["root_it_only_diagnostic"]["counts"])
    raise SystemExit(1 if report["failures"] else 0)
