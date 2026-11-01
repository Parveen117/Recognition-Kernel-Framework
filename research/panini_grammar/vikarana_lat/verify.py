"""Direct checks for PG5's changed claims; no frozen certificate replay.

python3.12 research/panini_grammar/vikarana_lat/verify.py --source-root PATH [--write]
The optional --write flag writes only this stage's deterministic result.
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

from research.panini_grammar.root_progression.verify import check_sources, digest, load  # noqa: E402
from research.panini_grammar.verification.marker_review import tokenize  # noqa: E402
from research.panini_grammar.vikarana_lat.grammar import Grammar, Request, sounds, surface  # noqa: E402


def request(raw):
    data = deepcopy(raw)
    if isinstance(data.get("prefixes"), list):
        data["prefixes"] = tuple(data["prefixes"])
    return Request(**data)


def iast(text):
    return "".join(s.symbol for s in tokenize(text))


def choice_label(choice):
    if choice.get("whole_affix_deletion"):
        return choice["affix"] + "/" + choice["whole_affix_deletion"]["kind"]
    if choice.get("preparation"):
        return choice["preparation"]["affix"] + "+" + choice["affix"]
    return choice["affix"]


def run_cases(grammar, cases):
    output = []
    for case in cases:
        req = request(case["request"])
        value = grammar.select(req) if case["kind"] == "select" else grammar.derive(req)
        if case["kind"] == "derive":
            expected = sorted({iast(w) for w in case["expected_forms"]})
            actual = value.get("forms")
            agrees = value["status"] == "COMPLETE_IN_REVIEWED_LAT_DOMAIN" and actual == expected
        elif case["kind"] == "select":
            expected = case["expected_choices"]
            actual = sorted(choice_label(c) for c in value.get("choices", []))
            agrees = value["status"] == "REVIEWED_VIKARANA_CHOICES" and actual == expected
        elif case["kind"] == "refuse":
            actual, expected = value["status"], case["expected_status"]
            agrees = actual == expected
        else:
            raise ValueError("Unknown case contract")
        output.append({"id": case["id"], "kind": case["kind"], "actual": actual,
                       "expected": expected, "agrees": agrees})
    return output


def controls(grammar, records, roots):
    output = []

    def check(name, condition):
        output.append({"id": name, "agrees": bool(condition)})

    def req(id, pada="P", person="prathama", number="eka"):
        return Request(id, grammar.entries[id]["artha"], pada, person, number, True)

    def branch(id, pada="P", person="prathama", number="eka", affix=None):
        result = grammar.derive(req(id, pada, person, number))
        return next(b for b in result["branches"] if affix is None or b["pre_tripadi"]["choice"]["affix"] == affix)

    def fails(make):
        try:
            make()
        except (ValueError, KeyError):
            return True
        return False

    frame = grammar.scope.frame("7.1.3")
    check("jho-anta-retains-affix-membership", any(t["term"] == "प्रत्ययस्य" for t in frame["inherited"]))
    check("jho-anta-excludes-initial-component", any(t["term"] == "आदि" for t in frame["excluded"]))
    changed = deepcopy(records)
    row = next(r for r in changed if r["i"] == "31069")
    row["an"] = "##".join(t for t in row["an"].split("##") if t != "कर्तरि$31068")
    check("missing-kartari-scope-refuses-compilation", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(grammar.review)
    next(t for r in changed["records"] if r["sid"] == "3.1.69" for t in r["terms"] if t["kind"] == "own")["case"] = "6"
    check("wrong-case-role-refuses-compilation", fails(lambda: Grammar(records, roots, review=changed)))
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "31068")["s"] = "कर्तरि श"
    check("changed-sutra-text-is-not-accepted-through-old-padaccheda", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(grammar.review)
    changed["priority"] = [e for e in changed["priority"] if (e["winner"], e["loser"]) != ("6.1.97", "6.1.101")]
    missing_relation = Grammar(records, roots, review=changed)
    check("missing-pararupa-exception-is-not-replaced-by-para", fails(lambda: missing_relation.derive(req("1011151", number="bahu"))))
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1040001")["gana"] = "10"
    check("lexical-id-cannot-alias-another-gana", fails(lambda: Grammar(records, changed)))

    sap, sa, syan = [grammar._affix(name, name) for name in ("śap", "śa", "śyan")]
    check("same-visible-a-keeps-distinct-marker-causes", sounds(sap) == sounds(sa) == ["a"] and sap["features"]["pit"] and not sa["features"]["pit"])
    check("ngitvat-comes-from-sarva-and-apit", sa["features"]["ngitvat"] and syan["features"]["ngitvat"] and not sap["features"]["ngitvat"])
    check("ngitvat-is-not-an-invented-ng-teaching-marker", not sa["features"]["ngit"] and "ṅ" not in [m["label"] for m in sa["marker_evidence"]["marker_units"]])
    lat = grammar._affix(None, "lat-control", lakara=True)
    check("lat-retains-l-and-tit-history", sounds(lat) == ["l"] and {m["label"] for m in lat["marker_evidence"]["marker_units"]} == {"a", "ṭ"})
    lat_plan = grammar.plan(req("1010001"))["branches"][0]
    check("ting-substitutes-lakara-rather-than-cooccurring-with-l", lat_plan["lakara"]["substituted_by"] == "ting" and any(e["rule"] == "3.4.78" and e["effect"] == "lakara_substitution" and e["sthānin"] == "lakara:lat" for e in lat_plan["history"]))
    tas, atam, jhi = [grammar._affix((p, i), "ting", ting=True) for p, i in (("P", 1), ("A", 1), ("P", 2))]
    check("vibhakti-final-s-and-m-are-protected", sounds(tas)[-1] == "s" and sounds(atam)[-1] == "m")
    check("atam-has-ngitvat-without-fictional-initial-ng", atam["features"]["ngitvat"] and not atam["marker_evidence"]["marker_units"])
    check("jhi-retains-jh-under-identity-specific-exception", sounds(jhi) == ["jh", "i"])
    # Explicitly supplied local control: jh within, rather than at the start of, an affix.
    jhi["visible"].insert(0, {"uid": "supplied-prefix", "symbol": "ā", "kind": "vowel"})
    local = {"history": [], "blocked": [], "lakara": lat}
    grammar._ending(local, jhi, req("1010001"))
    check("jho-anta-works-on-noninitial-affix-member", sounds(jhi) == ["ā", "a", "n", "t", "i"])

    tud = branch("1060001")["pre_tripadi"]
    check("tud-guna-is-blocked-by-vikarana-not-pit-tip", tud["morphemes"][-1]["features"]["pit"] and any(b["by"] == "1.1.5" and b["trigger"] == "vikarana" for b in tud["blocked"]))
    plan = grammar.plan(req("1060001"))["branches"][0]
    counterfactual = deepcopy(plan)
    counterfactual["morphemes"][-2]["features"]["ngitvat"] = False
    grammar._guna(counterfactual, counterfactual["morphemes"][:-2], counterfactual["morphemes"][-2])
    check("erasing-ngitvat-would-wrongly-give-tod", sounds(counterfactual["morphemes"][0]) == ["t", "o", "d"])
    check("counterfactual-did-not-mutate-real-plan", sounds(plan["morphemes"][0]) == ["t", "u", "d"])
    bhudual = branch("1010001", number="dvi")["pre_tripadi"]
    check("ngitvat-ting-does-not-block-sap-caused-root-guna", bhudual["morphemes"][-1]["features"]["ngitvat"] and any(e["rule"] == "7.3.84" and e["trigger"] == "vikarana" for e in bhudual["history"]))
    hu = grammar.plan(req("1030001"))["branches"][0]
    ad = grammar.plan(req("1020001"))["branches"][0]
    check("luk-and-slu-are-distinct-whole-affix-deletions", ad["morphemes"][-2]["whole_affix_deletion"]["kind"] == "luk" and hu["morphemes"][-2]["whole_affix_deletion"]["kind"] == "ślu")
    check("deleted-sap-retains-identity-and-markers", not hu["morphemes"][-2]["visible"] and hu["morphemes"][-2]["identity"] == "śap:3.1.68" and hu["morphemes"][-2]["features"]["pit"])
    check("lumata-blocks-deleted-sap-guna", sounds(hu["morphemes"][0]) == ["h", "u"] and any(b["by"] == "1.1.63" for b in hu["blocked"]))
    check("slu-retains-unexecuted-reduplication-obligation", any(o.get("rule") == "6.1.10" for o in hu["open_obligations"]))
    rudh = grammar.plan(req("1070001"))["branches"][0]
    check("snam-placement-not-misreported-as-complete", any(o.get("status") == "MIT_INFIX_PLACEMENT_NOT_EXECUTED" for o in rudh["open_obligations"]))
    sru = grammar.plan(req("1011092"))["branches"][0]
    check("sru-sr-substitution-cannot-be-silently-omitted", any(o.get("rule") == "3.1.74" and o["status"] == "REQUIRED_NOT_EXECUTED" for o in sru["open_obligations"]))
    check("same-kr-spelling-does-not-merge-two-lexemes", grammar.select(req("1050007"))["choices"][0]["affix"] == "śnu" and grammar.select(req("1080010"))["choices"][0]["affix"] == "u")
    check("taks-sense-keeps-optional-snu-restricted", len(grammar.select(req("1010743"))["choices"]) == 2 and len(grammar.select(req("1010756"))["choices"]) == 1)

    edh = branch("1010002", "A", "uttama")["pre_tripadi"]
    steps = [e["rule"] for e in edh["history"]]
    check("edhe-uses-ter-e-before-seam-operation", steps.index("3.4.79") < steps.index("6.1.97") and "6.1.87" not in steps)
    check("edhe-records-source-declared-vrddhi-exception", any(b["rule"] == "6.1.88" and b["by"] == "6.1.97" for b in edh["blocked"]))
    edhdual = branch("1010002", "A", number="dvi")["pre_tripadi"]
    steps = [e["rule"] for e in edhdual["history"]]
    check("dual-retains-ordered-ti-iy-y-lopa-guna", [steps.index(s) for s in ("3.4.79", "7.2.81", "6.1.66", "6.1.87")] == sorted(steps.index(s) for s in ("3.4.79", "7.2.81", "6.1.66", "6.1.87")))
    third = branch("1011151", number="bahu")["pre_tripadi"]
    seam = next(e for e in third["history"] if e["rule"] == "6.1.97")
    check("ekadesha-retains-both-morpheme-targets", seam["target_morphemes"] == ["vikarana", "ting"] and len(seam["after"][0]["replaces"]) == 2)
    check("pacanti-exception-does-not-use-finite-containment", any(b["rule"] == "6.1.101" and b["by"] == "6.1.97" for b in third["blocked"]))
    cur = branch("1100001")["pre_tripadi"]
    guna = [e for e in cur["history"] if e["effect"] == "guna"]
    check("cur-has-two-distinct-guna-owners", [(e["rule"], e["target_morpheme"], e["trigger"]) for e in guna] == [("7.3.86", "root:1100001", "nic"), ("7.3.84", "nic", "vikarana")])
    check("nic-dhatu-is-a-community-not-root-renaming", any(e["rule"] == "3.1.32" and e["constituents"] == ["root:1100001", "nic"] for e in cur["history"]))
    div = branch("1040001")
    check("div-tripadi-length-does-not-feed-earlier-guna", div["pre_tripadi"]["projection"] == "divyati" and div["form"] == "dīvyati" and any(e["rule"] == "8.2.77" for e in div["readout"]["history"]))
    before = digest(div["pre_tripadi"])
    query = grammar._readout(div["pre_tripadi"], grammar.entries["1040001"])
    check("readout-does-not-mutate-pre-tripadi-source", digest(div["pre_tripadi"]) == before)
    check("readout-reproduces-from-source", query == div["readout"])
    check("readout-output-cannot-reenter-derivation", fails(lambda: grammar._readout(query, grammar.entries["1040001"])))
    query["visible"][0]["symbol"] = "client-change"
    check("readout-has-no-mutable-alias", digest(div["pre_tripadi"]) == before)
    bhram = grammar.derive(req("1040102"))
    check("optional-bhram-paths-retain-distinct-lengthening", len(bhram["branches"]) == 2 and sorted(any(e["rule"] == "7.3.74" for e in b["pre_tripadi"]["history"]) for b in bhram["branches"]) == [False, True])
    check("unknown-profile-never-becomes-empty-valid-output", grammar.derive(replace(req("1040107"), prefixes=("sam",)))["status"] == "UNRESOLVED")
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1010001")["dhatu"] = "असत्य"
    alternate = Grammar(records, changed)
    check("headword-never-drives-generation", alternate.derive(req("1010001")) == grammar.derive(req("1010001")))
    return output


def comparison(grammar, witness):
    """Compare full result sets against pinned third-party software output."""
    rows, histories = [], []
    for entry in grammar.entries.values():
        if entry["derivation"] != "thematic_lat":
            continue
        for pada in ("P", "A") if entry["pada"] == "U" else (entry["pada"],):
            expected_cells = witness[entry["baseindex"]][pada.lower() + "lat"].split(";")
            if len(expected_cells) != 9:
                raise ValueError("Comparison witness does not have nine laṭ cells")
            for index, cell in enumerate(expected_cells):
                person = grammar.review["ending_order"]["persons"][index // 3]
                number = grammar.review["ending_order"]["numbers"][index % 3]
                value = grammar.derive(Request(entry["id"], entry["artha"], pada, person, number, True))
                actual = value["forms"]
                expected = sorted({iast(word) for word in cell.split(",")})
                rows.append({"id": f"{entry['id']}:{pada}:{index}", "expected_devanagari": cell,
                             "expected": expected, "actual": actual, "agrees": actual == expected,
                             "branches": len(value["branches"]), "history_sha256": digest(value["branches"])})
                histories.extend(e["rule"] for b in value["branches"]
                                 for e in b["pre_tripadi"]["history"] + b["readout"]["history"])
    return {"status": "PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE",
            "lexemes": sum(e["derivation"] == "thematic_lat" for e in grammar.entries.values()),
            "paradigms": len(rows) // 9, "cells": len(rows), "branches": sum(r["branches"] for r in rows),
            "agreements": sum(r["agrees"] for r in rows),
            "differences": [r for r in rows if not r["agrees"]], "rows": rows,
            "rule_event_counts": dict(sorted(Counter(histories).items()))}


def build_report(source_root):
    names = ("RULE_RECORDS.json", "LEXICAL_ENTRIES.json", "REFERENCE_CASES.json")
    packets = {name: load(HERE / name) for name in names}
    pins = load(HERE / "SOURCE_PINS.json")
    sources = check_sources(packets, pins, source_root)
    records = load(source_root / "sutraani/data.txt")["data"]
    roots = load(source_root / "dhatu/data.txt")["data"]
    before = digest([records, roots])
    grammar = Grammar(records, roots)
    cases = run_cases(grammar, packets["REFERENCE_CASES.json"]["cases"])
    checks = controls(grammar, records, roots)
    checks.append({"id": "all-source-records-remain-unchanged", "agrees": digest([records, roots]) == before})
    cmp = comparison(grammar, load(source_root / "dhatu/dhatuforms_vidyut_shuddha_kartari.txt"))
    failures = [r["id"] for r in cases + checks if not r["agrees"]]
    # Disagreements with software are recorded separately; they cannot overrule primary evidence.
    return {"schema": "rkf.panini.pg5.v1", "author": "Monty",
            "status": "PASS_BOUNDED_PG5_CONTRACTS" if not failures else "FAIL_BOUNDED_PG5_CONTRACTS",
            "primary_commit": pins["primary_commit"], "sources": sources,
            "compiled_records": len(grammar.rules), "scope_corrections": len(grammar.review["scope_policies"]),
            "lexical_entries": len(grammar.entries), "gana_classes_with_selection_examples": sorted({int(e["gana"]) for e in grammar.entries.values()}),
            "case_counts": dict(Counter(c["kind"] for c in cases)), "cases": cases,
            "direct_controls": checks, "failures": failures, "implementation_comparison": cmp,
            "claim_boundary": {"all_sutra_compilation": False, "full_gana_conjugation": False,
                "general_priority_or_sthanivad_engine": False, "raw_pada_or_sense_inference": False,
                "independent_valid_sanskrit_oracle": False, "accent_and_vedic": False,
                "new_operator_theorem": False, "calculator_integration": False}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build_report(args.source_root)
    text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    target = HERE / "VERIFICATION_RESULT.json"
    if args.write:
        target.write_text(text, encoding="utf-8")
    elif not target.exists() or target.read_text(encoding="utf-8") != text:
        raise SystemExit("PG5 report differs; inspect the change rather than overwriting a pin")
    print(json.dumps({"status": report["status"], "records": report["compiled_records"],
                      "sources": report["sources"], "cases": report["case_counts"],
                      "controls": len(report["direct_controls"]), "failures": report["failures"],
                      "comparison_cells": report["implementation_comparison"]["cells"],
                      "comparison_differences": len(report["implementation_comparison"]["differences"])}, indent=2))
    return int(bool(report["failures"]))


if __name__ == "__main__":
    raise SystemExit(main())
