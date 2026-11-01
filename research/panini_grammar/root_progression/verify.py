"""Direct PG3 source, root and retained-history checks; no certificate replay.

python3.12 research/panini_grammar/root_progression/verify.py \
  --source-root /path/to/ashtadhyayi-data [--write]

The corpus comparison is a lexical diagnostic, not a Sanskrit validity oracle.
Without --write, the report must reproduce exactly; only PG3's report is written.
"""

from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import fields, replace
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))

from research.panini_grammar.root_progression.root_preprocess import (  # noqa: E402
    RootInput, marker_profile, num_readout, observed_root, preprocess,
)
from research.panini_grammar.verification.marker_review import designate, tokenize  # noqa: E402
from proof_lab.paninian_it_samjna_compiled import its as t82_its  # noqa: E402
from proof_lab.paninian_samjna_sound_layer import savarna_classes, VOWELS_IAST  # noqa: E402


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def anchors(value):
    if isinstance(value, dict):
        if {"path", "key", "anchor"} <= value.keys():
            yield value
        for child in value.values():
            yield from anchors(child)
    elif isinstance(value, list):
        for child in value:
            yield from anchors(child)


def check_sources(packets, pins, source_root):
    for directory, group in ((source_root, "external_sha256"), (ROOT, "historical_sha256")):
        for path, expected in pins[group].items():
            if file_digest(directory / path) != expected:
                raise ValueError(f"Pinned source changed: {path}; do not repin to pass")
    cache, checked = {}, []
    for packet in packets.values():
        for evidence in anchors(packet):
            path, key = evidence["path"], evidence["key"]
            if path not in pins["external_sha256"]:
                raise ValueError(f"Unpinned citation: {path}")
            if path not in cache:
                source = load(source_root / path)
                if isinstance(source.get("data"), list):
                    rows = source["data"]
                    source = {r["i"]: r for r in rows}
                    if len(source) != len(rows):
                        raise ValueError(f"Duplicate source identities: {path}")
                cache[path] = source
            source = cache[path][key]
            if evidence.get("field"):
                source = source[evidence["field"]]
            if not isinstance(source, str) or not evidence["anchor"] or evidence["anchor"] not in source:
                raise ValueError(f"Citation anchor not found: {evidence}")
            checked.append(evidence)
    return {"literal_anchors": len(checked), "unique_anchors": len({digest(e) for e in checked}),
            "external_files": len(pins["external_sha256"]),
            "historical_files_unchanged": len(pins["historical_sha256"])}


def run_cases(cases, rules):
    results = []
    for case in cases:
        if case["kind"] == "marker":
            value = designate(case["input"], rules)
            actual = {"status": value["status"], "projection": value.get("it_only_projection"),
                      "units": [u["label"] for u in value.get("marker_units", [])]}
        elif case["kind"] == "root":
            value = preprocess(RootInput(**case["input"]), rules)
            actual = {"status": value["status"], "projection": value.get("projection"),
                      "idit": value.get("idit"),
                      "applied": [e["rule"] for e in value.get("history", [])[1:]]}
        elif case["kind"] == "readout":
            value = preprocess(RootInput(**case["input"]), rules)
            query = num_readout(value, internal_root=True)
            actual = {"underlying": value.get("projection"), "readout": query.get("projection"),
                      "applied": [e["rule"] for e in query.get("history", [])]}
        else:
            raise ValueError(f"Unreviewed case kind: {case['kind']}")
        results.append({"id": case["id"], "kind": case["kind"], "actual": actual,
                        "expected": case["expected"], "agrees": actual == case["expected"]})
    return results


def retained_history_controls(cases, rules, rows):
    by_id = {c["id"]: c for c in cases}
    controls = []

    def check(name, condition):
        controls.append({"id": name, "agrees": bool(condition)})

    def root(name):
        return RootInput(**by_id[name]["input"])

    def state(name):
        return preprocess(root(name), rules)

    n = state("ni-initial-n")
    check("replacement-keeps-original-uid-and-sound",
          n["original"][0]["symbol"] == "ṇ" and n["visible"][0]["symbol"] == "n"
          and n["original"][0]["uid"] == n["visible"][0]["uid"])
    check("removed-marker-remains-in-source-history",
          n["original"][-1]["symbol"] == "ñ"
          and n["original"][-1]["uid"] in n["history"][0]["removed_uids"]
          and n["marker"]["marker_units"][-1]["label"] == "ñ")
    i, ir = state("bhid-idit-num"), state("bhid-irit-no-num")
    check("same-it-projection-does-not-collapse-i-and-ir",
          i["marker"]["it_only_projection"] == ir["marker"]["it_only_projection"] == "bhid"
          and i["idit"] and not ir["idit"]
          and i["projection"] == "bhind" and ir["projection"] == "bhid")
    ni = state("mid-compound-ni")
    check("compound-ni-is-not-standalone-idit",
          any(u["label"] == "ñi" for u in ni["marker"]["marker_units"]) and not ni["idit"])
    inserted = next(s for s in i["visible"] if s.get("introduced_by") == "7.1.58")
    check("num-has-fresh-identity-and-placement-history",
          inserted["uid"] not in {s["uid"] for s in i["original"]}
          and i["history"][-1]["placement_rule"] == "1.1.47"
          and i["history"][-1]["inserted_uid"] == inserted["uid"])
    query_input = preprocess(root("gad-retroflex-nasal"), rules)
    before = digest(query_input)
    first = num_readout(query_input, internal_root=True)
    check("tripadi-query-preserves-earlier-state",
          digest(query_input) == before and query_input["projection"] == "ganḍ"
          and first["projection"] == "gaṇḍ" and not query_input["tripadi_applied"])
    check("readout-repeated-query-is-stable", first == num_readout(query_input, internal_root=True))
    check("readout-cannot-be-fed-back-as-preprocessing-state",
          num_readout(first, internal_root=True)["status"] == "UNRESOLVED")
    first["visible"][0]["symbol"] = "changed-in-client"
    check("readout-has-no-mutable-alias-to-root", digest(query_input) == before)
    check("pada-boundary-not-assumed", num_readout(query_input, internal_root=False)["status"] == "UNRESOLVED")
    check("missing-nasality-refused", preprocess(replace(root("bhid-idit-num"), nasality_complete=False), rules)["status"] == "UNRESOLVED")
    check("unknown-root-origin-refused", preprocess(replace(root("ni-initial-n"), origin="unknown"), rules)["status"] == "UNRESOLVED")
    check("missing-lexical-identity-refused", preprocess(replace(root("ni-initial-n"), lexical_id=""), rules)["status"] == "UNRESOLVED")
    check("expected-headword-is-not-an-input-field", "headword" not in {f.name for f in fields(RootInput)})
    row = next(r for r in rows if r["i"] == "1010067")
    check("headword-mutation-does-not-affect-preprocessing",
          preprocess(observed_root(row), rules) == preprocess(observed_root({**row, "dhatu": "changed"}), rules))
    check("ganasutra-is-not-a-root", observed_root(next(r for r in rows if r.get("tags") == "ganasutra")) is None)
    jhi = by_id["jhi-retain-jh"]["input"]
    unknown = designate({**jhi, "identity": "unreviewed-affix"}, rules)
    check("jnapaka-exception-is-identity-scoped", unknown["it_only_projection"] == "i")
    check("exception-preserves-affix-identity", designate(jhi, rules)["identity"] == jhi["identity"])
    no_vowel = RootInput("synthetic-idit-no-vowel", "किँ", "listed_dhatu", True)
    check("num-without-placement-vowel-refused", preprocess(no_vowel, rules)["status"] == "UNRESOLVED")
    for name, teaching, expected in (("nasal", "कमिँ", "kanm"), ("semivowel", "कयिँ", "kany"),
                                     ("no-vowel", "किँइँ", "k")):
        # Explicitly synthetic domain controls: m and y are not jhal. The last
        # cannot license ordinary mit placement after both vowels elide.
        probe = preprocess(RootInput("synthetic-" + name, teaching, "listed_dhatu", True), rules)
        if name != "no-vowel":
            result = num_readout(probe, internal_root=True)
            check(name + "-following-num-is-outside-jhal", probe["projection"] == expected and not result["history"])
        else:
            check("elided-vowels-cannot-license-placement", probe["status"] == "UNRESOLVED")
    return controls


def historical_probes(cases, rules):
    """New counterexamples only; no predecessor certificate or suite is called."""
    probes = []
    for case in cases:
        if "legacy_T82" not in case:
            continue
        annotated = "".join(s.symbol + ("~" if s.nasal else "") for s in tokenize(case["input"]["text"]))
        old = t82_its(**case["legacy_T82"])
        corrected_input = t82_its(annotated, "pratyaya")
        current = designate(case["input"], rules)
        probes.append({"id": case["id"], "legacy_unmarked_input": case["legacy_T82"]["upadesa"],
                       "legacy_unmarked_result": "".join(old["remaining_sounds"]),
                       "explicit_nasal_input": annotated,
                       "legacy_same_annotated_result": "".join(corrected_input["remaining_sounds"]),
                       "reviewed_result": current["it_only_projection"],
                       "scope": "Same annotated input shows the missing l exception; raw-input nasality is also missing.",
                       "agrees": current["it_only_projection"] == "l" and corrected_input["remaining_sounds"] == ()})
    old_rules = load(HERE.parent / "verification/MARKER_RULES.json")
    jhi = next(c for c in cases if c["id"] == "jhi-retain-jh")["input"]
    old_input = {**jhi, "identity": "jhi-affix-identity"}
    before, after = designate(old_input, old_rules), designate(old_input, rules)
    probes.append({"id": "PG2-jhi-reading-superseded", "historical_projection": before["it_only_projection"],
                   "reviewed_projection": after["it_only_projection"],
                   "agrees": before["it_only_projection"] == "i" and after["it_only_projection"] == "jhi"})
    vowel_classes = [sorted(group) for group in savarna_classes(("ṛ", "ṝ", "ḷ", "ḹ"))]
    probes.append({"id": "T81-vowel-table-is-not-exhaustive-traditional-savarna",
                   "classes": vowel_classes, "long_l_in_inventory": "ḹ" in VOWELS_IAST,
                   "agrees": not any("ṛ" in c and "ḷ" in c for c in vowel_classes) and "ḹ" in VOWELS_IAST,
                   "scope": "Confirms the source-review limitation; does not repair or certify the entire sound table."})
    return probes


def root_diagnostic(rows, rules):
    stages = ("marker_only", "root_preprocessing", "num_phonetic_readout")
    counts = {stage: {"exact_headword_agreement": 0, "different_projection": 0} for stage in stages}
    unresolved, directives, differences, trace = [], [], [], []
    new_matches = {"preprocessing_over_markers": [], "readout_over_preprocessing": [], "readout_over_markers": []}
    regressions = {"preprocessing_from_markers": [], "readout_from_preprocessing": [], "readout_from_markers": []}
    events, ir_count = Counter(), 0
    for row in rows:
        root = observed_root(row)
        if root is None:
            directives.append({"id": row["i"], "text": row["dhatu"], "source_tag": row["tags"]})
            continue
        state = preprocess(root, rules)
        try:
            expected = "".join(s.symbol for s in tokenize(row["dhatu"]))
        except ValueError:
            expected = None
        if state["status"] == "UNRESOLVED" or expected is None:
            unresolved.append({"id": row["i"], "teaching": row["aupadeshik"], "headword": row["dhatu"],
                               "reason": state.get("reason", "Headword notation needs review")})
            continue
        query = num_readout(state, internal_root=True)
        values = (state["marker"]["it_only_projection"], state["projection"], query["projection"])
        matches = tuple(v == expected for v in values)
        ir_count += any(u["label"] == "ir" for u in state["marker"]["marker_units"])
        for stage, match in zip(stages, matches):
            counts[stage]["exact_headword_agreement" if match else "different_projection"] += 1
        for a, b, new_key, regression_key in (
            (0, 1, "preprocessing_over_markers", "preprocessing_from_markers"),
            (1, 2, "readout_over_preprocessing", "readout_from_preprocessing"),
            (0, 2, "readout_over_markers", "readout_from_markers"),
        ):
            if not matches[a] and matches[b]:
                new_matches[new_key].append(row["i"])
            if matches[a] and not matches[b]:
                regressions[regression_key].append(row["i"])
        applied = [e["rule"] for e in state["history"][1:] + query["history"]]
        events.update(applied)
        record = {"id": row["i"], "teaching": row["aupadeshik"], "headword": row["dhatu"],
                  "expected_tokens": expected, **dict(zip(stages, values)), "applied": applied}
        trace.append(record)
        if not matches[-1]:
            differences.append(record)
    return {"status": "HEADWORD_DIAGNOSTIC_NOT_GRAMMAR_ACCURACY", "records": len(rows),
            "root_entries": len(rows) - len(directives), "stage_counts": counts,
            "unresolved_count": len(unresolved), "non_root_directive_count": len(directives),
            "assumptions": ["Pinned lexical classification and nasal teaching marks are supplied inputs.",
                            "Headwords are comparison data only; matching is not an independent soundness oracle.",
                            "Tripādī readout is a local query, not the input to later pre-Tripādī derivation."],
            "compound_ir_records": ir_count, "rule_application_counts": dict(sorted(events.items())),
            "new_match_counts": {k: len(v) for k, v in new_matches.items()}, "new_match_ids": new_matches,
            "regression_ids": regressions, "all_resolved_projection_records_sha256": digest(trace),
            "remaining_differences": differences, "unresolved": unresolved, "non_root_directives": directives}


def build_report(source_root):
    pins = load(HERE / "SOURCE_PINS.json")
    names = ("RULES.json", "REFERENCE_CASES.json", "CLAIM_REVIEW.json")
    packets = {name: load(HERE / name) for name in names}
    source_checks = check_sources(packets, pins, source_root)
    rows = load(source_root / "dhatu/data.txt")["data"]
    rules = marker_profile()
    cases = packets["REFERENCE_CASES.json"]["cases"]
    case_results = run_cases(cases, rules)
    controls = retained_history_controls(cases, rules, rows)
    probes = historical_probes(cases, rules)
    diagnostic = root_diagnostic(rows, rules)
    # Compare to the frozen PG2 root-only diagnostic without rerunning PG2.
    prior = load(HERE.parent / "verification/VERIFICATION_RESULT.json")
    prior_counts = prior["root_it_only_diagnostic"]["counts"]
    controls.append({"id": "marker-baseline-reproduces-frozen-PG2-root-counts", "agrees":
                     diagnostic["stage_counts"]["marker_only"] == {k: prior_counts[k] for k in
                         ("exact_headword_agreement", "different_projection")}
                     and diagnostic["unresolved_count"] == prior_counts["unresolved_notation"]
                     and diagnostic["non_root_directive_count"] == prior_counts["non_root_ganasutra"]})
    controls.append({"id": "no-lost-matches-on-this-pinned-witness",
                     "agrees": not any(diagnostic["regression_ids"].values())})
    failures = [r["id"] for r in case_results + controls + probes if not r["agrees"]]
    ledger = load(ROOT / "proof_lab/astadhyayi/ASTADHYAYI_LEDGER.json")
    return {"stage": "PG3", "author": "Monty", "review_date": "2026-11-01",
            "reviewed_commits": pins["reviewed_commits"], "primary_source_commit": pins["primary_commit"],
            "verification_status": "LOCAL_REFERENCE_CHECKS_AGREE" if not failures else "REVIEW_FAILURE",
            "grammar_status": "NOT_COMPLETE", "valid_sanskrit_oracle": False,
            "source_checks": source_checks,
            "input_sha256": {name: file_digest(HERE / name) for name in
                             (*names, "SOURCE_PINS.json", "root_preprocess.py", "verify.py")},
            "case_counts": dict(Counter(r["kind"] for r in case_results)), "case_results": case_results,
            "structural_controls": controls, "historical_counterexample_probes": probes,
            "root_diagnostic": diagnostic,
            "coverage_caveat": {"pinned_sutra_records": len(load(source_root / "sutraani/data.txt")["data"]),
                                "historical_ledger_counts": ledger["counts"],
                                "PG2_static_T80_operation_ids": prior["legacy_code"]["T80_distinct_operation_ids"],
                                "status": "DECLARATION_COUNTS_NOT_RULE_COMPLETENESS"},
            "failures": failures,
            "not_claimed": ["A complete Dhātupāṭha derivation or all-sūtra compilation",
                            "Automatic scope, class, sense, pada, seṭ or nasality inference",
                            "Universal priority, sthānivad or Tripādī visibility resolution",
                            "Independent Sanskrit soundness or completeness",
                            "Calculator integration, CI success or main-branch merge"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build_report(args.source_root)
    target = HERE / "VERIFICATION_RESULT.json"
    if args.write:
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    elif not target.is_file() or load(target) != report:
        raise SystemExit("PG3 report differs; inspect the changed evidence before writing")
    print(json.dumps({k: report[k] for k in ("verification_status", "grammar_status", "source_checks", "case_counts", "failures")}, ensure_ascii=False))
    print("Root diagnostic:", report["root_diagnostic"]["stage_counts"])
    print("Structural controls:", len(report["structural_controls"]), "Historical probes:", len(report["historical_counterexample_probes"]))
    raise SystemExit(1 if report["failures"] else 0)
