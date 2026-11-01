"""Direct PG7 checks; frozen predecessor reports are read, never replayed."""
import argparse
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))

from research.panini_grammar.root_progression.verify import check_sources, digest, load
from research.panini_grammar.vikarana_lat.verify import request, iast
from research.panini_grammar.snam_lat.grammar import Grammar, Request, ordered, sounds, collapse_targets
from research.panini_grammar.snam_lat.coverage import build_coverage


def run_cases(g, cases):
    output = []
    for case in cases:
        value = g.derive(request(case["request"]))
        if case["kind"] == "attested_member":
            expected = sorted({iast(w) for w in case["attested_forms"]})
            actual = value.get("forms", [])
            agrees = value["status"] == "COMPLETE_IN_REVIEWED_SNAM_LAT_DOMAIN" and set(expected) <= set(actual)
        else:
            expected, actual = case["expected_status"], value["status"]
            agrees = expected == actual
        output.append({"id": case["id"], "kind": case["kind"], "actual": actual, "expected": expected, "agrees": agrees})
    return output


def controls(g, records, roots):
    checks = []

    def check(id, value):
        checks.append({"id": id, "agrees": bool(value)})

    def req(id, pada="P", person="prathama", number="eka"):
        return Request(id, g.entries[id]["artha"], pada, person, number, True)

    def derive(id, pada="P", person="prathama", number="eka"):
        return g.derive(req(id, pada, person, number))

    def first(id, pada="P", person="prathama", number="eka"):
        return derive(id, pada, person, number)["branches"][0]

    def fails(call):
        try:
            call()
        except (ValueError, KeyError):
            return True
        return False

    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "64111")["an"] = "सार्वधातुके$64110"
    check("missing-kit-ngit-inheritance-is-rejected", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "11047")["s"] = "परश्च"
    check("changed-mit-wording-is-rejected", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1070007")["gana"] = "4"
    check("same-spelling-yuj-is-not-another-gana", fails(lambda: Grammar(records, changed)))
    changed = deepcopy(g.pg7)
    changed["priority"] = []
    unlicensed = Grammar(records, roots, review=changed)
    check("local-nitya-relation-cannot-be-omitted", fails(lambda: unlicensed.derive(req("1070002"))))
    changed = deepcopy(g.pg7)
    changed["scope_policies"] = []
    check("unadjudicated-parasavarna-term-does-not-compile", fails(lambda: Grammar(records, roots, review=changed)))
    frame = g.pg7_scope.frame("8.4.65")
    check("jhar-rule-excludes-wrong-replacement-not-condition", any(t["term"] == "परसवर्णः" for t in frame["excluded"]) and
          any(t["term"] == "सवर्णे" for t in frame["own"]) and not any(t["term"] == "परसवर्णः" for t in frame["inherited"]))
    check("jhar-option-keeps-hal-and-option-sources", all(any(t["term"] == term and t["source"] == source
          for t in frame["inherited"]) for term, source in [("हलः", "8.4.64"), ("अन्यतरस्याम्", "8.4.62")]))
    plan = g.plan(req("1070001"))["branches"][0]
    check("plan-is-not-mislabelled-as-spoken-order", any(o["status"] == "MIT_INFIX_PLACEMENT_NOT_EXECUTED" for o in plan["open_obligations"]))
    check("plan-retains-m-it-and-s-it", {m["label"] for m in plan["morphemes"][1]["marker_evidence"]["marker_units"]} == {"ś", "m"})
    synthetic = deepcopy(plan)
    synthetic["morphemes"][0]["visible"] = [{"uid": f"synthetic:{i}", "symbol": s,
        "kind": "vowel" if s in {"a", "i"} else "consonant"} for i, s in enumerate(["a", "i", "n", "dh"])]
    g._placement(synthetic)
    check("mit-is-after-last-vowel-not-before-last-consonant", [s["symbol"] for s in ordered(synthetic)][:6] == ["a", "i", "n", "a", "n", "dh"])
    broken = deepcopy(plan)
    broken["morphemes"][1]["marker_evidence"]["marker_units"] = []
    check("no-retained-m-it-means-no-infix-license", fails(lambda: g._placement(broken)))
    strong = first("1070002")
    weak = first("1070002", number="bahu")
    pre = strong["pre_tripadi"]
    check("one-base-root-morpheme-survives", len([m for m in pre["morphemes"] if m["kind"] == "root"]) == 1)
    check("infix-is-a-member-of-the-root-host", pre["host_constituent"]["members"] == ["root:1070002", "vikarana"] and pre["host_constituent"]["infix_is_host_member"])
    check("surface-order-is-distinct-from-constituent-list", pre["projection"] == "bhinadti" and "".join(s["symbol"] for m in pre["morphemes"] for s in m["visible"]) == "bhidnati")
    check("upadha-query-uses-the-root-with-infix", pre["anga_query"]["upadha"] == "a" and weak["pre_tripadi"]["anga_query"]["upadha"] == "n")
    check("nitya-placement-prevents-spurious-bhenatti", any(b.get("by") == "3.1.78" and b["rule"] == "7.3.86" for b in pre["blocked"]) and strong["form"] == "bhinatti")
    check("no-false-root-before-snam-guna-event", not any(e["rule"] in {"7.3.84", "7.3.86"} for e in pre["history"]))
    check("strong-retains-snam-a", sounds(pre["morphemes"][1]) == ["n", "a"] and pre["strength"]["pit"])
    check("weak-loses-only-affix-a", sounds(weak["pre_tripadi"]["morphemes"][1]) == ["n"] and weak["pre_tripadi"]["strength"]["ngitvat"])
    check("snam-identity-survives-partial-lopa", weak["pre_tripadi"]["morphemes"][1]["identity"] == pre["morphemes"][1]["identity"] and not weak["pre_tripadi"]["morphemes"][1].get("whole_affix_deletion"))
    check("word-and-placement-obligations-are-discharged", not pre["open_obligations"] and len(pre["fulfilled_obligations"]) == 2)
    bad = deepcopy(pre)
    bad["infix_layout"]["after_uid"] = "missing"
    check("missing-layout-anchor-is-rejected", fails(lambda: ordered(bad)))
    for id in ("1070011", "1070016", "1070019", "1070020", "1070021", "1070022"):
        b = first(id, "A" if id == "1070011" else "P")["pre_tripadi"]
        event = next(e for e in b["history"] if e["rule"] == "6.4.23")
        check("root-n-is-not-infix-n:" + id, event["target_morpheme"] == "root:" + id and
              event["before"][0]["symbol"] == "n" and b["morphemes"][1]["visible"][0]["symbol"] == "n")
    h = first("1070019")["pre_tripadi"]
    event = next(e for e in h["history"] if e["rule"] == "6.4.23")
    check("hims-num-is-retained-as-the-deleted-source", event["before"][0]["introduced_by"] == "7.1.58" and h["projection"] == "hinasti")
    a = first("1070001", "A", number="bahu")
    event = next(e for e in a["pre_tripadi"]["history"] if e["rule"] == "7.1.5")
    check("jha-sees-root-tail-not-infix-final-a", event["preceding_anga_final"] == "dh" and event["preceding_owner"] == "root:1070001" and a["form"] == "rundhate")
    rudh = first("1070001")
    rules = [e["rule"] for e in rudh["readout"]["history"]]
    check("rudh-t-to-dh-precedes-jastva", rules.index("8.2.40") < rules.index("8.4.53") and rudh["form"] == "ruṇaddhi")
    r = first("1070001", number="dvi")
    rules = [e["rule"] for e in r["readout"]["history"]]
    check("late-dental-n-does-not-feed-nati", rules.index("8.3.24") < rules.index("8.4.58") and
          not any(sid in rules for sid in ("8.4.1", "8.4.2")) and r["form"] == "runddhaḥ")
    check("deleted-a-is-not-restored-for-nasal-readout", r["readout"]["visibility_queries"][0]["license"] == "1.1.58" and r["readout"]["visibility_queries"][0]["deleted_snam_a_is_not_restored"])
    y = first("1070007", "A", "madhyama")
    rules = [e["rule"] for e in y["readout"]["history"]]
    check("velar-trigger-survives-into-satva", rules.index("8.2.30") < rules.index("8.3.59") < rules.index("8.4.55") < rules.index("8.4.58") and y["form"] == "yuṅkṣe")
    y = first("1070007", number="bahu")
    check("palatal-stays-before-vowel", y["form"] == "yuñjanti" and not any(e["rule"] == "8.2.30" for e in y["readout"]["history"]))
    check("sish-has-retroflex-contact-before-ti", first("1070014")["form"] == "śinaṣṭi")
    check("sish-has-k-substitution-only-before-s", first("1070014", person="madhyama")["form"] == "śinakṣi")
    for id, pada, person, number, expected in [
        ("1070001", "P", "prathama", "dvi", {"runddhaḥ", "rundhaḥ"}),
        ("1070002", "P", "madhyama", "dvi", {"bhintthaḥ", "bhinthaḥ"}),
        ("1070002", "A", "madhyama", "bahu", {"bhinddhve", "bhindhve"})]:
        value = derive(id, pada, person, number)
        check("optional-jhar:" + id + ':' + pada + ':' + person, set(value["forms"]) == expected and len(value["branches"]) == 2)
        deleted = next(b for b in value["branches"] if b["readout"]["option"] == "jhar-deleted")
        check("optional-lopa-retains-root-owned-target:" + id + ':' + pada + ':' + person,
              deleted["readout"]["history"][-1]["target"]["owner"] == "root:" + id)
    p = g.pg7_rules["8.4.65"]["parameters"]
    def sites(symbols):
        return collapse_targets([{"symbol": s, "kind": "vowel" if s == "a" else "consonant"} for s in symbols], p)
    for label, symbols, expected in [("needs-prior-hal", ["a", "t", "t"], []),
            ("aspiration-can-differ", ["n", "t", "th"], [1]),
            ("nasal-not-a-jhar-target", ["r", "ṅ", "g"], []),
            ("nasal-not-a-jhar-trigger", ["n", "c", "ñ"], []),
            ("different-varga-refused", ["n", "t", "k"], []),
            ("sibilant-is-not-savarna-to-stop", ["n", "ṣ", "ṭ"], [])]:
        check("collapse-guard:" + label, sites(symbols) == expected)
    check("no-collapse-after-vowel-in-strong-bhinatti", len(derive("1070002")["branches"]) == 1)
    original = deepcopy(r["pre_tripadi"])
    before = digest(original)
    output = g._readout_infix(original)
    check("readout-is-immutable-with-respect-to-source", digest(original) == before)
    check("readout-is-repeatable", output == g._readout_infix(original))
    check("readout-cannot-feed-back", fails(lambda: g._readout_infix(output[0])))
    output[0]["visible"][0]["symbol"] = "client-edit"
    check("readout-does-not-alias-source", digest(original) == before)
    check("readout-branches-do-not-alias", output[1]["visible"][0]["symbol"] != "client-edit")
    check("replacement-has-fresh-identity-and-owner", all(e["before"]["uid"] != e["after"]["uid"] and
          e["before"]["owner"] == e["after"]["owner"] for e in r["readout"]["history"] if e["effect"] == "ordered_phonetic_replacement"))
    # Direct checks of dispatch through the changed adapter, not old-suite replay.
    for id, pada, number, expected in [("1010001", "P", "eka", "bhavati"), ("1080010", "P", "bahu", "kurvanti"),
                                       ("1090001", "A", "bahu", "krīṇate")]:
        check("predecessor-routing:" + id, derive(id, pada, number=number)["forms"] == [expected])
    return checks


def comparison(g, table):
    rows, events = [], Counter()
    for id in sorted(g.snam_ids):
        entry = g.entries[id]
        for pada in ("P", "A") if entry["pada"] == "U" else (entry["pada"],):
            cells = table[entry["baseindex"]][pada.lower() + "lat"].split(";")
            if len(cells) != 9:
                raise ValueError("The pinned laṭ table must have nine cells per pada")
            for i, cell in enumerate(cells):
                req = Request(id, entry["artha"], pada, g.review["ending_order"]["persons"][i // 3],
                              g.review["ending_order"]["numbers"][i % 3], True)
                value = g.derive(req)
                expected = sorted({iast(w) for w in cell.split(",")})
                rows.append({"id": f"{id}:{pada}:{i}", "actual": value.get("forms"), "expected": expected,
                    "expected_devanagari": cell, "agrees": value["status"] == "COMPLETE_IN_REVIEWED_SNAM_LAT_DOMAIN" and value.get("forms") == expected,
                    "branches": len(value.get("branches", [])), "history_sha256": digest(value.get("branches"))})
                events.update(e["rule"] for b in value.get("branches", []) for e in b["pre_tripadi"]["history"] + b["readout"]["history"])
    return {"status": "PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE", "lexemes": len(g.snam_ids),
            "paradigms": len(rows) // 9, "cells": len(rows), "branches": sum(r["branches"] for r in rows),
            "agreements": sum(r["agrees"] for r in rows), "differences": [r for r in rows if not r["agrees"]],
            "rule_event_counts": dict(sorted(events.items())), "rows": rows}


def build_report(source_root):
    packets = {n: load(HERE / n) for n in ("RULE_RECORDS.json", "LEXICAL_ENTRIES.json", "REFERENCE_CASES.json")}
    sources = check_sources(packets, load(HERE / "SOURCE_PINS.json"), source_root)
    records = load(source_root / "sutraani/data.txt")["data"]
    roots = load(source_root / "dhatu/data.txt")["data"]
    before = digest([records, roots])
    g = Grammar(records, roots)
    cases = run_cases(g, packets["REFERENCE_CASES.json"]["cases"])
    checks = controls(g, records, roots)
    checks.append({"id": "source-records-unchanged", "agrees": digest([records, roots]) == before})
    cmp = comparison(g, load(source_root / "dhatu/dhatuforms_vidyut_shuddha_kartari.txt"))
    coverage = build_coverage(records, roots, cmp)
    checks.extend([
        {"id": "coverage-counts-distinct-record-identities", "agrees": coverage["pg4_to_pg7_source_bound_records"]["distinct_sutra_ids"] < coverage["pg4_to_pg7_source_bound_records"]["definitions"]},
        {"id": "coverage-does-not-publish-overall-completion-percent", "agrees": coverage["overall_grammar_completion_percent"] is None},
        {"id": "root-coverage-denominator-excludes-ganasutras", "agrees": coverage["complete_lat_profile"]["root_entry_denominator"] + coverage["lexical_preprocessing"]["ganasutra_directives"] == len(roots)},
    ])
    failures = [c["id"] for c in cases + checks if not c["agrees"]]
    report = {"schema": "rkf.panini.pg7.v1", "author": "Monty",
        "status": "FAIL_BOUNDED_PG7_CONTRACTS" if failures else "PASS_BOUNDED_PG7_CONTRACTS",
        "sources": sources, "new_source_bound_records": len(g.pg7_rules), "scope_policies": len(g.pg7["scope_policies"]),
        "case_counts": dict(Counter(c["kind"] for c in cases)), "cases": cases, "direct_controls": checks,
        "failures": failures, "implementation_comparison": cmp, "coverage_sha256": digest(coverage),
        "claim_boundary": {"all_rudhadi_members": False, "all_lakaras": False, "optional_consonant_doubling": False,
            "full_abhiya_or_sthanivad_engine": False, "raw_sanskrit_interpreter": False, "soundness_oracle": False,
            "native_operator_or_calculator_theorem": False}}
    return report, coverage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report, coverage = build_report(args.source_root)
    for name, value in (("VERIFICATION_RESULT.json", report), ("COVERAGE_STATUS.json", coverage)):
        text = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        target = HERE / name
        if args.write:
            target.write_text(text, encoding="utf-8")
        elif not target.exists() or target.read_text(encoding="utf-8") != text:
            raise SystemExit(f"PG7 {name} differs; inspect before writing")
    print(json.dumps({"status": report["status"], "sources": report["sources"], "cases": report["case_counts"],
        "controls": len(report["direct_controls"]), "failures": report["failures"],
        "comparison_cells": report["implementation_comparison"]["cells"],
        "comparison_branches": report["implementation_comparison"]["branches"],
        "comparison_differences": len(report["implementation_comparison"]["differences"]),
        "combined_lat_roots": coverage["complete_lat_profile"]["root_entries"],
        "combined_lat_cells": coverage["complete_lat_profile"]["cells"]}, indent=2))
    return int(bool(report["failures"]))


if __name__ == "__main__":
    raise SystemExit(main())
