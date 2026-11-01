"""Direct PG13 source, causative licensing, constituent and order checks."""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import asdict, replace
import json
from pathlib import Path

from research.panini_grammar.causative_present.grammar import Grammar, CausativeRequest, Request, COMPLETE, sounds, PG5Grammar
from research.panini_grammar.root_progression.verify import check_sources, digest, file_digest, load
from research.panini_grammar.vikarana_lat.verify import iast

HERE = Path(__file__).resolve().parent
PEOPLE = ["prathama", "madhyama", "uttama"]
NUMBERS = ["eka", "dvi", "bahu"]


def request(d):
    d = deepcopy(d)
    if isinstance(d.get("prefixes"), list):
        d["prefixes"] = tuple(d["prefixes"])
    return CausativeRequest(**d)


def controls(g, records, roots):
    rows = []
    def check(n, v): rows.append({"id": n, "agrees": bool(v)})
    def fails(fn):
        try: fn()
        except (ValueError, KeyError): return True
        return False
    def req(i="1010001", **kw):
        return replace(CausativeRequest(i, g.causatives[i]["artha"], "P", "prathama", "eka", True, causative_licensed=True), **kw)
    def raw(i="1010001", **kw):
        r = req(i, **kw)
        return g.plan(r)["branches"][0], r
    def stage(i="1010001", to="DERIVED_DHATU", **kw):
        s, r = raw(i, **kw)
        steps = [(g._root_strength13, (s,)), (g._root_augment13, (s,)), (g._derived13, (s,)),
                 (g._outer13, (s, r)), (g._stem13, (s,)), (g._finish13, (s, r))]
        if s["phase13"] != to:
            for fn, args in steps:
                fn(*args)
                if s["phase13"] == to: break
        return s, r
    def word(i="1010001", **kw): return g.derive(req(i, **kw))["branches"][0]
    def mutate(s, fn, run):
        x = deepcopy(s); fn(x); return fails(lambda: run(x))

    record = deepcopy(next(r for r in g.pg13["records"] if r["sid"] == "3.1.26"))
    record["terms"] = [t for t in record["terms"] if t["term"] != "णिच्"]
    check("nic-inheritance-cannot-disappear", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    record = deepcopy(next(r for r in g.pg13["records"] if r["sid"] == "7.2.115"))
    record["terms"][0]["case"] = "7"
    check("vrddhi-target-case-cannot-be-trigger-case", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    record = deepcopy(next(r for r in g.pg13["records"] if r["sid"] == "6.4.92"))
    record["terms"] = [t for t in record["terms"] if t["term"] != "उपधायाः"]
    check("mit-shortening-requires-upadha-scope", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    record = deepcopy(next(r for r in g.pg13["records"] if r["sid"] == "1.3.86"))
    kartari = [t for t in record["terms"] if t["term"] == "कर्तरि"]
    kartari[1]["occurrence_uid"] = kartari[0]["occurrence_uid"]
    check("repeated-kartari-occurrences-stay-distinct", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    review = deepcopy(g.pg13); review["records"][0]["sanskrit"] += " च"
    check("source-wording-drift-rejected", fails(lambda: Grammar(records, roots, review=review)))
    entries = list(deepcopy(g.causatives).values())
    next(e for e in entries if e["id"] == "1011137")["anubandha_note_मित्"] = "invented"
    check("source-mit-license-cannot-be-rewritten", fails(lambda: Grammar(records, roots, lexical=entries)))
    check("untyped-request-refused", g._guard13({})["status"] == "UNRESOLVED")
    check("lexical-and-causative-licenses-are-independent", g.derive(replace(req(), causative_licensed=False))["status"] == "UNRESOLVED")
    check("causative-and-pada-licenses-are-independent", g.derive(replace(req(), pada_licensed=False))["status"] == "UNRESOLVED")

    s, r = raw()
    check("nit-marker-memory-required", mutate(s, lambda x: x["morphemes"][1]["features"].update(nit=False), g._root_strength13))
    check("a-sit-affix-cannot-stand-in-for-nic", mutate(s, lambda x: x["morphemes"][1]["features"].update(sit=True), g._root_strength13))
    check("root-owner-cannot-change", mutate(s, lambda x: x["morphemes"][0].update(id="root:other"), g.carrier))
    check("duplicate-visible-uids-rejected", mutate(s, lambda x: x["morphemes"][0]["visible"][0].update(uid=x["morphemes"][1]["visible"][0]["uid"]), g.carrier))
    check("missing-nic-rejected", mutate(s, lambda x: x["morphemes"].pop(), g.carrier))
    check("augment-cannot-precede-root-strength", fails(lambda: g._root_augment13(deepcopy(s))))
    check("outer-affixes-need-derived-dhatu", fails(lambda: g._outer13(deepcopy(s), r)))
    g._root_strength13(s)
    check("root-strength-cannot-repeat", fails(lambda: g._root_strength13(deepcopy(s))))
    check("bhu-retains-vrddhi-before-ayadi", [(e["rule"], [v["symbol"] for v in e["after"]]) for e in s["history"] if e["rule"] in {"7.2.115", "6.1.78"}] == [("7.2.115", ["au"]), ("6.1.78", ["ā", "v"])])
    for i in ["1080010", "1011046"]:
        b = word(i); h = b["pre_tripadi"]["history"]
        e = next(e for e in h if e["rule"] == "1.1.51")
        check("r-accompaniment-owned:" + i, [v["symbol"] for v in e["result"]] == ["ā", "r"] and e["source"]["symbol"] == "ṛ")
    b = word("1011049"); units = b["pre_tripadi"]["morphemes"]
    check("two-nayaya-y-sounds-have-distinct-owners", sounds(units[0]) == ["n", "ā", "y"] and sounds(units[1]) == ["a", "y"] and units[0]["visible"][-1]["uid"] != units[1]["visible"][-1]["uid"])
    b = word("1011137"); h = b["pre_tripadi"]["history"]
    long = next(e for e in h if e["rule"] == "7.2.116"); short = next(e for e in h if e["rule"] == "6.4.92")
    check("gam-long-intermediate-survives-shortening", long["index"] < short["index"] and short["before"] == long["after"] and short["after"][0]["symbol"] == "a")
    check("gam-m-is-root-sound-not-mit-marker", sounds(b["pre_tripadi"]["morphemes"][0]) == ["g", "a", "m"])
    check("pac-does-not-borrow-gam-shortening", word("1011151")["form"] == "pācayati" and all(e["rule"] != "6.4.92" for e in word("1011151")["pre_tripadi"]["history"]))
    saved = deepcopy(g.causatives["1011137"])
    g.causatives["1011137"]["tags"] = g.causatives["1011137"]["tags"].replace("मित्", "")
    s, _ = raw("1011137")
    check("gam-shortening-needs-source-mit-tag", fails(lambda: g._root_strength13(s)))
    g.causatives["1011137"] = saved
    b = word("1060006")
    check("krsh-guna-retains-r-history", b["form"] == "karṣayati" and any(e["rule"] == "1.1.51" and e["effect"] == "r_accompanied_guna" for e in b["pre_tripadi"]["history"]))

    for i, name in [("1011077", "puk"), ("1030010", "puk"), ("1011074", "yuk")]:
        s, _ = stage(i, to="ROOT_AUGMENT"); a = s["morphemes"][1]
        check("root-final-augment-ownership:" + i, a["host"] == s["morphemes"][0]["id"] and s["root_constituent"]["members"] == [s["morphemes"][0]["id"], "augment:"+name])
        check("pronunciation-u-is-not-it:" + i, [x["symbol"] for x in a["markers"]] == ["k"] and [x["symbol"] for x in a["pronunciation_only"]] == ["u"] and not any(e["rule"] == "1.3.2" for e in s["history"]))
        check("no-root-augment-alias:" + i, a["visible"][0] is not a["original"][0])
    s, _ = stage("1011074", to="ROOT_AUGMENT")
    check("yuk-blocks-puk-for-drinking-pa", any(e["by"] == "7.3.37" and e["rule"] == "7.3.36" for e in s["blocked"]))
    check("augment-cannot-repeat", fails(lambda: g._root_augment13(deepcopy(s))))
    check("augment-cannot-belong-to-nic", mutate(s, lambda x: x["morphemes"][1].update(host="nic"), g.carrier))
    check("augment-cannot-lose-kit", mutate(s, lambda x: x["morphemes"][1]["features"].update(kit=False), g.carrier))
    check("augment-u-cannot-become-an-it", mutate(s, lambda x: x["morphemes"][1]["markers"].append(x["morphemes"][1]["original"][1]), g.carrier))
    check("augment-visible-sound-must-retain-source-uid", mutate(s, lambda x: x["morphemes"][1]["visible"][0].update(uid="invented"), g.carrier))
    check("kit-augment-cannot-move-after-nic", mutate(s, lambda x: x["morphemes"].__setitem__(slice(1,3), list(reversed(x["morphemes"][1:3]))), g.carrier))
    saved = deepcopy(g.pg13_rules["7.3.37"]["parameters"])
    g.pg13_rules["7.3.37"]["parameters"]["pronunciation_only"] = "k"
    check("augment-role-record-cannot-change", fails(lambda: g._recipe13("1011074")))
    g.pg13_rules["7.3.37"]["parameters"] = saved
    s, r = stage("1030010")
    check("derived-dhatu-contains-root-augment-and-nic", s["derived_dhatu"]["members"] == ["root:1030010", "augment:puk", "nic"])
    check("derived-dhatu-cannot-drop-augment", mutate(s, lambda x: x["derived_dhatu"]["members"].remove("augment:puk"), g.carrier))
    check("derived-dhatu-cannot-drop-nic", mutate(s, lambda x: x["derived_dhatu"]["members"].remove("nic"), g.carrier))
    check("designation-cannot-repeat", fails(lambda: g._derived13(deepcopy(s))))
    check("outer-affixes-cannot-borrow-another-request", fails(lambda: g._outer13(deepcopy(s), replace(r, number="dvi"))))
    check("outer-strength-cannot-precede-outer-affixes", fails(lambda: g._stem13(deepcopy(s))))
    g._outer13(s, r); root_before = deepcopy(s["morphemes"][0]); aug_before = deepcopy(s["morphemes"][1])
    check("outer-affixes-cannot-repeat", fails(lambda: g._outer13(deepcopy(s), r)))
    check("ending-identity-matches-request", mutate(s, lambda x: x["morphemes"][-1].update(identity="mip:3.4.78"), g.carrier))
    g._stem13(s)
    check("outer-guna-target-is-nic-not-root-or-augment", root_before == s["morphemes"][0] and aug_before == s["morphemes"][1] and sounds(s["morphemes"][-3]) == ["a", "y"])
    eh = [e for e in s["history"] if e.get("target_morpheme") == "nic"]
    check("nic-retains-intermediate-e-before-ayadi", [(e["rule"], [x["symbol"] for x in e["after"]]) for e in eh] == [("7.3.84", ["e"]), ("6.1.78", ["a", "y"])])
    check("outer-strength-cannot-repeat", fails(lambda: g._stem13(deepcopy(s))))
    check("phase-cannot-skip-constituent-construction", mutate(s, lambda x: x.update(root_constituent=None), g.carrier))
    g._finish13(s, r)
    check("ending-resolution-cannot-repeat", fails(lambda: g._finish13(deepcopy(s), r)))
    b = word("1040068")
    check("original-A-root-can-have-licensed-causative-P", g.causatives["1040068"]["pada"] == "A" and b["form"] == "bodhayati" and any(e["rule"] == "1.3.86" for e in b["pre_tripadi"]["history"]))
    check("original-class-does-not-select-syan-after-nic", b["pre_tripadi"]["morphemes"][-2]["identity"] == "śap:3.1.68")
    b = word("1010001", person="uttama")
    check("first-person-lengthening-owned-by-sap", any(e["rule"] == "7.3.101" and e["target_morpheme"] == "vikarana" for e in b["pre_tripadi"]["history"]) and b["form"] == "bhāvayāmi")
    b = word("1010001", number="bahu")
    h = b["pre_tripadi"]["history"]
    check("jh-substitution-precedes-sap-ending-merger", next(e["index"] for e in h if e["rule"] == "7.1.3") < next(e["index"] for e in h if e["rule"] == "6.1.97"))
    s = b["pre_tripadi"]; before = digest(s)
    read = PG5Grammar._readout(g, s, g.causatives["1010001"])
    check("readout-repeatable-and-source-immutable", read == b["readout"] and digest(s) == before)
    check("readout-cannot-feed-back", fails(lambda: g._root_strength13(read)))
    read["visible"][0]["symbol"] = "invented"
    check("readout-has-no-source-alias", digest(s) == before)

    for i, form in [("1010001", "bhavati"), ("1030010", "dadāti"), ("1080010", "karoti"), ("1090068", "khaunāti")]:
        r = Request(i, g.entries[i]["artha"], "P", "prathama", "eka", True)
        check("ordinary-request-dispatch-preserved:" + i, form in g.derive(r).get("forms", []))
    return rows


def comparison(g, table):
    rows = []; invariants = {k: True for k in ["distinct_visible_uids", "owned_constituents", "root_teaching_retained", "derived_dhatu_present", "resolved_obligations", "projection_equals_form"]}
    for e in g.causatives.values():
        for i, expected in enumerate(table[e["baseindex"]]["plat"].split(";")):
            r = CausativeRequest(e["id"], e["artha"], "P", PEOPLE[i//3], NUMBERS[i%3], True, causative_licensed=True)
            result = g.derive(r); exp = sorted({iast(w) for w in expected.split(",")})
            b = result["branches"][0]; s = b["pre_tripadi"]; seq = g.carrier(s)
            invariants["distinct_visible_uids"] &= len({x["uid"] for x in seq}) == len(seq)
            invariants["owned_constituents"] &= all(x["owner"] for x in seq)
            invariants["root_teaching_retained"] &= s["morphemes"][0]["teaching"] == e["aupadeshik"]
            invariants["derived_dhatu_present"] &= s["derived_dhatu"]["kind"] == "dhatu"
            invariants["resolved_obligations"] &= not s["open_obligations"]
            invariants["projection_equals_form"] &= b["readout"]["projection"] == b["form"] and result["forms"] == [b["form"]]
            rows.append({"id": e["id"]+":P:"+str(i), "actual": result["forms"], "expected": exp,
                         "agrees": result["status"] == COMPLETE and result["forms"] == exp, "history_sha256": digest(b)})
    return {"roots": len(g.causatives), "paradigms": len(g.causatives), "cells": len(rows), "branches": len(rows),
            "rows": rows, "differences": [r for r in rows if not r["agrees"]], "all_branch_invariants": invariants}


def build(source_root):
    packets = {n: load(HERE/n) for n in ["RULE_RECORDS.json", "LEXICAL_ENTRIES.json", "REFERENCE_CASES.json", "SOURCE_ADJUDICATIONS.json"]}
    sources = check_sources(packets, load(HERE/"SOURCE_PINS.json"), source_root)
    records = load(source_root/"sutraani/data.txt")["data"]; roots = load(source_root/"dhatu/data.txt")["data"]
    before = digest([records, roots]); g = Grammar(records, roots); cases = []
    for c in packets["REFERENCE_CASES.json"]["cases"]:
        v = g.derive(request(c["request"])); expected = sorted({iast(w) for w in c["attested_forms"]}) if c["kind"] == "attested_member" else c["expected_status"]
        actual = v.get("forms", v["status"])
        ok = v["status"] == COMPLETE and set(expected) <= set(actual) if c["kind"] == "attested_member" else v["status"] == expected
        cases.append({"id": c["id"], "kind": c["kind"], "actual": actual, "expected": expected, "agrees": ok})
    checks = controls(g, records, roots)
    checks.append({"id": "source-inputs-unchanged", "agrees": digest([records, roots]) == before})
    cmp = comparison(g, load(source_root/"dhatu/dhatuforms_vidyut_nich_kartari.txt"))
    checks += [{"id": "all-branches:"+k, "agrees": v} for k, v in cmp["all_branch_invariants"].items()]
    lookup = {r["id"]: r for r in cmp["rows"]}
    companion = [{**r, "agrees": lookup[r["pg13_lexical_id"]+":P:"+str(r["slot"])]["actual"] == [r["expected"]]} for r in load(HERE/"COMPANION_EXPECTATIONS.json")["rows"]]
    prior = load(HERE.parent/"nasal_present/COVERAGE_STATUS.json")
    prior_records = prior["source_bound_records_pg4_pg12"]
    distinct_ids = sorted(set(prior_records["distinct_ids"]) | set(g.pg13_rules))
    cov = {"author": "Monty", "frozen_simple_present_report": "../nasal_present/COVERAGE_STATUS.json",
           "simple_present_pg12": deepcopy(prior["complete_lat_profile"]),
           "causative_present_pg13": {"formation": "hetumati_nic", "root_ids": sorted(g.causatives),
                                      **{k: cmp[k] for k in ["roots", "paradigms", "cells", "branches"]},
                                      "pada": "P only, caller supplies a context license independent of the simple-root pada", "causative_license": "required separately", "no_separate_word_witness_ids": ["1060006"]},
           "combined_formation_distinguished_cells": prior["complete_lat_profile"]["cells"] + cmp["cells"],
           "source_bound_records_pg4_pg13": {"definitions": prior_records["definitions"] + len(g.pg13_rules),
                                            "distinct_count": len(distinct_ids), "distinct_ids": distinct_ids},
           "counting_boundary": "Causative profiles are distinct formations; do not add 12 to the 228 simple-present root count. Existing source evidence gaps and predecessor reports remain unchanged.",
           "full_grammar_and_native_operator_lift": "OPEN", "overall_grammar_completion_percent": None}
    failures = [x["id"] for x in cases+checks if not x["agrees"]] + ["comparison:"+x["id"] for x in cmp["differences"]] + ["companion:"+x["root_label"]+":"+str(x["slot"]) for x in companion if not x["agrees"]]
    report = {"author": "Monty", "schema": "rkf.panini.pg13.v1", "status": "FAIL_BOUNDED_PG13_CONTRACTS" if failures else "PASS_BOUNDED_PG13_CONTRACTS",
              "sources": sources, "case_counts": dict(Counter(x["kind"] for x in cases)), "cases": cases, "direct_controls": checks,
              "implementation_comparison": cmp, "companion_expectation_comparison": companion, "failures": failures,
              "coverage_sha256": digest(cov), "implementation_sha256": {n: file_digest(HERE/n) for n in ["grammar.py", "verify.py", "cli.py"]},
              "packet_sha256": {n: file_digest(HERE/n) for n in [*packets, "COMPANION_EXPECTATIONS.json", "CONCURRENT_REVIEW.json", "SOURCE_PINS.json"]},
              "claim_boundary": {"universal_causative": False, "automatic_semantic_or_pada_inference": False, "atmanepada": False, "full_native_operator_lift": False}}
    return report, cov


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("--source-root", type=Path, required=True); p.add_argument("--write", action="store_true")
    a = p.parse_args(); report, cov = build(a.source_root)
    for n, v in [("VERIFICATION_RESULT.json", report), ("COVERAGE_STATUS.json", cov)]:
        text = json.dumps(v, ensure_ascii=False, indent=2, sort_keys=True) + "\n"; target = HERE/n
        if a.write: target.write_text(text, encoding="utf-8")
        elif not target.exists() or target.read_text(encoding="utf-8") != text: raise SystemExit("PG13 report differs: " + n)
    print(json.dumps({"status": report["status"], "sources": report["sources"], "case_counts": report["case_counts"],
        "direct_controls": len(report["direct_controls"]), "comparison_cells": report["implementation_comparison"]["cells"],
        "companion_examples": len(report["companion_expectation_comparison"]), "failures": report["failures"],
        "source_bound_records": {k: v for k, v in cov["source_bound_records_pg4_pg13"].items() if k != "distinct_ids"}}, ensure_ascii=False, indent=2))
    return int(bool(report["failures"]))


if __name__ == "__main__":
    raise SystemExit(main())
