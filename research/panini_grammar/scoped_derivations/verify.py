"""Direct PG4 source, scope, grammar and retained-history checks.

python3.12 research/panini_grammar/scoped_derivations/verify.py \
  --source-root /path/to/ashtadhyayi-data [--write]

No CI, old certificate campaigns or operator-engine suites are invoked.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))

from research.panini_grammar.scoped_derivations.derive import Grammar, RootInput, supplied_span  # noqa: E402
from research.panini_grammar.scoped_derivations.scope import ScopeIndex, parse_padaccheda  # noqa: E402
from research.panini_grammar.root_progression.root_preprocess import observed_root  # noqa: E402
from research.panini_grammar.root_progression.verify import check_sources, digest, file_digest, load  # noqa: E402
from research.panini_grammar.verification.marker_review import tokenize  # noqa: E402


def run_cases(grammar, cases):
    output = []
    for case in cases:
        kind, inp, expected = case["kind"], case["input"], case["expected"]
        if kind == "root":
            state, query = grammar.root_readout(RootInput(**inp))
            actual = {"status": query["status"], "projection": query.get("projection"), "pg4_rules":
                      [e["rule"] for e in state.get("history", []) + query.get("history", [])
                       if e["rule"] not in {"1.3.2–9", "6.1.64", "6.1.65", "7.1.58"}]}
        elif kind == "tuk":
            actual = grammar.tuk_choices(**inp)
        elif kind == "length":
            actual = grammar.root_length_choice(**inp)
        elif kind == "sap":
            actual = grammar.prescribe_sap(inp)
        elif kind == "phonetic":
            state = supplied_span(inp["text"], case["id"])
            final = [state["visible"][i]["uid"] for i in inp["boundary_after"]]
            units = {state["visible"][int(i)]["uid"]: value for i, value in inp["following_units"].items()}
            actual = grammar.phonetic(state, samhita=inp["samhita"], pada_final_uids=final, following_unit_identities=units)
            actual["blocked_rules"] = sorted({e["rule"] for e in actual.get("blocked", [])})
        else:
            raise ValueError(f"Unreviewed case kind: {kind}")
        reduced = {key: actual.get(key) for key in expected}
        output.append({"id": case["id"], "kind": kind, "actual": reduced, "expected": expected,
                       "agrees": reduced == expected})
    return output


def scope_controls(grammar, records):
    scope = grammar.scope
    controls = []

    def check(name, condition):
        controls.append({"id": name, "agrees": bool(condition)})

    def inherits(target, source, term=None):
        return any(e["source"] == source and (term is None or e["term"] == term) for e in scope.frame(target)["inherited"])

    observed = scope.summary()["scope_policy_counts"]
    for policy in scope.policies:
        check("policy:" + policy["id"], observed.get(policy["id"], 0) == policy["expected_edges"])
    check("va-not-imported-at-5.3.1", not inherits("5.3.1", "4.1.82"))
    check("va-still-in-scope-at-5.2.140", inherits("5.2.140", "4.1.82"))
    check("uttarapadadi-at-old-endpoint", inherits("6.2.137", "6.2.111", "उत्तरपदादिः"))
    check("uttarapadasya-after-split", inherits("6.2.138", "6.2.111", "उत्तरपदस्य"))
    check("adi-does-not-leak-after-split", not inherits("6.2.138", "6.2.111", "उत्तरपदादिः"))
    check("antah-reference-corrected", inherits("6.2.144", "6.2.143", "अन्तः") and not inherits("6.2.144", "6.2.14"))
    antah = next(e for e in scope.frame("6.2.144")["inherited"] if e["term"] == "अन्तः")
    check("wrong-reference-retained-as-provenance", antah["raw_source"] == "6.2.14" and "6$2$14" in antah["raw"])
    check("ekadesa-through-6.1.111", inherits("6.1.111", "6.1.84"))
    check("sut-kat-through-6.1.157", inherits("6.1.157", "6.1.135"))
    check("sese-heading-accepted", inherits("4.3.23", "4.2.92"))
    check("padasya-excluded-at-8.2.78", not inherits("8.2.78", "8.1.16"))
    check("padasya-preserved-at-8.2.76", inherits("8.2.76", "8.1.16"))
    check("anga-samjna-is-not-an-adhikara", "1.4.13" not in scope.graph["headings"])
    check("pratyaya-heading-at-last-rule", inherits("5.4.160", "3.1.1"))
    check("pratyaya-heading-ends-before-6.1.1", not inherits("6.1.1", "3.1.1"))
    check("anga-heading-at-last-rule", inherits("7.4.97", "6.4.1"))
    check("anga-heading-ends-before-8.1.1", not inherits("8.1.1", "6.4.1"))
    check("dhato-heading-3.1.91-at-3.4.117", inherits("3.4.117", "3.1.91"))
    check("earlier-dhato-source-in-sap", inherits("3.1.68", "3.1.22", "धातोः") and not inherits("3.1.68", "3.1.91"))
    check("sap-does-not-import-yang-action", not any("यङ्" in e["term"] for e in scope.frame("3.1.68")["inherited"]))
    check("guna-inherited-aci-not-iki", inherits("6.1.87", "6.1.77", "अचि") and not inherits("6.1.87", "6.1.77", "इकि"))
    check("kartari-is-a-semantic-role", next(t["role"] for t in grammar.rules["3.1.68"]["terms"] if t["term"] == "कर्तरि") == "semantic_agent")
    check("acah-genitive-is-partitive", next(t["role"] for t in grammar.rules["1.1.47"]["terms"] if t["term"] == "अचः") == "partitive_vowel_domain")
    # Counterfactual removal of inherited conditions must stop compilation.
    for sid, key, field, removed in (("6.1.65", "61065", "an", "धात्वादेः$61064"),
                                     ("8.4.43", "84043", "an", "न$84042")):
        changed = deepcopy(records)
        row = next(r for r in changed if r["i"] == key)
        row[field] = "##".join(x for x in row[field].split("##") if x != removed)
        contract = next(r for r in grammar.review["records"] if r["sid"] == sid)
        check("missing-inheritance-refused:" + sid, ScopeIndex(changed).compile(contract)["status"] == "UNRESOLVED_RECORD")
    changed = deepcopy(next(r for r in grammar.review["records"] if r["sid"] == "3.1.68"))
    next(t for t in changed["terms"] if t["term"] == "कर्तरि")["case"] = "6"
    check("wrong-case-role-binding-refused", scope.compile(changed)["status"] == "UNRESOLVED_RECORD")
    raw = next(r for r in records if r["i"] == "72034")
    check("noncanonical-padaccheda-not-silently-fixed", parse_padaccheda(raw)[0]["status"] == "UNRESOLVED_ANNOTATION_SHAPE")
    return controls


def history_controls(grammar, rows):
    checks = []

    def check(name, condition):
        checks.append({"id": name, "agrees": bool(condition)})

    def inp(key):
        return observed_root(next(r for r in rows if r["i"] == key))

    root = grammar.root(inp("1011077"))
    check("conditioned-restoration-preserves-original", root["original"][1]["symbol"] == "ṭh" and root["visible"][1]["symbol"] == "th" and root["original"][1]["uid"] == root["visible"][1]["uid"])
    check("restoration-needs-lexical-witness", grammar.root(replace(inp("1011077"), lexical_id="unreviewed"))["status"] == "UNRESOLVED")
    check("lexical-id-cannot-alias-different-teaching", grammar.root(replace(inp("1011077"), teaching="ष्टु"))["status"] == "UNRESOLVED")
    root = grammar.root(inp("1060016"))
    augment = next(s for s in root["visible"] if s.get("introduced_by") == "6.1.73")
    event = next(e for e in root["history"] if e["rule"] == "6.1.73")
    check("tuk-recipient-is-the-vowel", next(s for s in root["visible"] if s["uid"] == event["recipient_uid"])["symbol"] == "ṛ")
    check("tuk-has-fresh-uid", augment["uid"] not in {s["uid"] for s in root["original"]})
    before = digest(root)
    query = grammar.phonetic(root, samhita=True, pada_final_uids=[], following_unit_identities={})
    check("query-retains-pre-tripadi-root", digest(root) == before and root["projection"] == "ṛtch" and query["projection"] == "ṛcch")
    check("query-repeated-from-source-is-stable", query == grammar.phonetic(root, samhita=True, pada_final_uids=[], following_unit_identities={}))
    check("query-output-cannot-feed-earlier-stage", grammar.phonetic(query, samhita=True, pada_final_uids=[], following_unit_identities={})["status"] == "UNRESOLVED")
    query["visible"][0]["symbol"] = "client-change"
    check("query-has-no-mutable-source-alias", digest(root) == before)
    state, query = grammar.root_readout(inp("1010243"))
    check("early-num-blocks-later-tuk-contact", state["projection"] == "unch" and query["projection"] == "uñch" and not any(e["rule"] in {"6.1.73", "6.1.75"} for e in state["history"]))
    state, query = grammar.root_readout(inp("1010239"))
    check("tripadi-length-does-not-overwrite-root", state["projection"] == "hurch" and query["projection"] == "hūrch" and state["visible"][1]["symbol"] == "u" and query["visible"][1]["kind"] == "vowel")
    state = supplied_span("कुर्वन्ति")
    query = grammar.phonetic(state, samhita=True, pada_final_uids=[], following_unit_identities={})
    check("same-visible-n-retains-two-events", [e["rule"] for e in query["history"]] == ["8.3.24", "8.4.58"] and [e["after"] for e in query["history"]] == ["ṃ", "n"])
    check("unknown-boundary-refused", grammar.phonetic(state, samhita=True, pada_final_uids=None, following_unit_identities={})["status"] == "UNRESOLVED")
    check("missing-boundary-uid-refused", grammar.phonetic(state, samhita=True, pada_final_uids=["absent"], following_unit_identities={})["status"] == "UNRESOLVED")
    row = next(r for r in rows if r["i"] == "1010021")
    check("headword-never-drives-derivation", grammar.root_readout(observed_root(row)) == grammar.root_readout(observed_root({**row, "dhatu": "changed"})))
    candidate = grammar.prescribe_sap({"base_is_dhatu": True, "following_is_sarvadhatuka": True, "agent_is_expressed": True})
    check("sap-is-a-candidate-not-final-vikarana-selection", candidate["selection_status"] == "VIKARANA_COMPETITION_NOT_RESOLVED" and candidate["affix"]["it_only_projection"] == "a")
    return checks


def root_diagnostic(grammar, rows):
    previous = load(ROOT / "research/panini_grammar/root_progression/VERIFICATION_RESULT.json")["root_diagnostic"]
    previous_differences = {r["id"] for r in previous["remaining_differences"]}
    previous_unknown = {r["id"] for r in previous["unresolved"]}
    counts, applied = Counter(), Counter()
    trace, remaining, unresolved, directives, added, regressions = [], [], [], [], [], []
    for row in rows:
        root = observed_root(row)
        if root is None:
            directives.append({"id": row["i"], "text": row["dhatu"], "tag": row["tags"]})
            continue
        state, query = grammar.root_readout(root)
        if state["status"] == "UNRESOLVED":
            unresolved.append({"id": row["i"], "teaching": row["aupadeshik"], "headword": row["dhatu"], "reason": state["reason"]})
            continue
        expected = "".join(s.symbol for s in tokenize(row["dhatu"]))
        agrees = query.get("projection") == expected and query["status"] == "LOCAL_PHONETIC_QUERY"
        counts["exact_headword_agreement" if agrees else "different_projection"] += 1
        events = [e["rule"] for e in state["history"] + query.get("history", [])]
        applied.update(events)
        item = {"id": row["i"], "teaching": row["aupadeshik"], "headword": row["dhatu"], "headword_tokens": expected,
                "preprocessed": state["projection"], "phonetic_query": query.get("projection"),
                "query_status": query["status"], "rules": events, "open_obligations": query.get("open_obligations", [])}
        trace.append(item)
        if agrees and row["i"] in previous_differences:
            added.append(row["i"])
        if not agrees:
            remaining.append(item)
            if row["i"] not in previous_differences | previous_unknown:
                regressions.append(row["i"])
    return {"status": "PINNED_HEADWORD_DIAGNOSTIC_NOT_GRAMMAR_ACCURACY",
            "source_records": len(rows), "root_records": len(rows) - len(directives),
            "counts": {**dict(counts), "unresolved": len(unresolved), "non_root_directives": len(directives)},
            "previous_PG3_counts": previous["stage_counts"]["num_phonetic_readout"],
            "new_agreements": len(added), "new_agreement_ids": added, "regression_ids": regressions,
            "all_resolved_records_sha256": digest(trace), "rule_application_counts": dict(sorted(applied.items())),
            "remaining_differences": remaining, "unresolved": unresolved, "directives": directives,
            "assumptions": ["Lexical identities and nasal teaching flags supplied by the pinned source",
                            "Internal classical-root profile; no prior ekādeśa or unknown constituent boundaries",
                            "The separate readout includes only the documented rule profile",
                            "Headwords are comparison data; no source spelling is silently corrected"]}


def build_report(source_root):
    names = ("SCOPE_POLICIES.json", "RULE_RECORDS.json", "LEXICAL_WITNESSES.json", "REFERENCE_CASES.json")
    packets = {name: load(HERE / name) for name in names}
    pins = load(HERE / "SOURCE_PINS.json")
    source_checks = check_sources(packets, pins, source_root)
    records = load(source_root / "sutraani/data.txt")["data"]
    rows = load(source_root / "dhatu/data.txt")["data"]
    source_before = digest(records)
    grammar = Grammar(records)
    for witness in packets["LEXICAL_WITNESSES.json"]["withdraw_conditioned_retroflexion"]:
        row = next(r for r in rows if r["i"] == witness["id"])
        if row["aupadeshik"] != witness["teaching"] or tokenize(witness["teaching"])[witness["position"]].symbol != witness["from"]:
            raise ValueError(f"Lexical witness mismatch: {witness['id']}")
    cases = run_cases(grammar, packets["REFERENCE_CASES.json"]["cases"])
    controls = scope_controls(grammar, records) + history_controls(grammar, rows)
    diagnostic = root_diagnostic(grammar, rows)
    controls += [{"id": "source-annotations-unmodified", "agrees": digest(records) == source_before},
                 {"id": "no-lost-headword-agreements-on-this-witness", "agrees": not diagnostic["regression_ids"]}]
    failures = [r["id"] for r in cases + controls if not r["agrees"]]
    return {"stage": "PG4", "author": "Monty", "review_date": "2026-11-01", "baseline_commit": pins["baseline_commit"],
            "primary_source_commit": pins["primary_commit"],
            "verification_status": "LOCAL_REFERENCE_CHECKS_AGREE" if not failures else "REVIEW_FAILURE",
            "grammar_status": "NOT_COMPLETE", "valid_sanskrit_oracle": False,
            "source_checks": source_checks, "lexical_witnesses_checked": len(grammar.lexical),
            "input_sha256": {name: file_digest(HERE / name) for name in (*names, "SOURCE_PINS.json", "scope.py", "derive.py", "verify.py")},
            "scope": grammar.scope.summary(), "bound_record_count": len(grammar.rules),
            "bound_records": grammar.rules, "case_counts": dict(Counter(c["kind"] for c in cases)),
            "intentional_unresolved_cases": [c["id"] for c in cases if c["expected"].get("status") in {"UNRESOLVED", "PARTIAL_PHONETIC_QUERY"}],
            "case_results": cases, "structural_controls": controls,
            "root_diagnostic": diagnostic, "failures": failures,
            "not_claimed": ["Raw Sanskrit scope or semantic parsing for all 3,983 sūtras",
                            "All case fields or all commentary scope choices verified",
                            "Universal nitya/antaraṅga/bahiraṅga or sthānivad resolution",
                            "A complete phonetic normal form or full verbal/nominal derivation",
                            "Independent Sanskrit soundness, completeness or calculator integration",
                            "CI success or main-branch merge"]}


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
        raise SystemExit("PG4 report differs; review the changed evidence before writing")
    print(json.dumps({k: report[k] for k in ("verification_status", "grammar_status", "source_checks", "bound_record_count", "case_counts", "failures")}, ensure_ascii=False))
    print("Root diagnostic:", report["root_diagnostic"]["counts"], "Additional agreements:", report["root_diagnostic"]["new_agreements"])
    print("Structural controls:", len(report["structural_controls"]), "Intentional unresolved cases:", len(report["intentional_unresolved_cases"]))
    raise SystemExit(1 if report["failures"] else 0)
