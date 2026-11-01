"""Direct PG6 source, strong/weak, option and visibility checks.

python3.12 research/panini_grammar/non_thematic_lat/verify.py --source-root PATH [--write]
Only PG6's new report is written; no predecessor certificate is replayed.
"""
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
from research.panini_grammar.vikarana_lat.verify import request, iast  # noqa: E402
from research.panini_grammar.non_thematic_lat.grammar import Grammar, Request, sounds, u_context, local_nati  # noqa: E402


def run_cases(grammar, cases):
    result = []
    for case in cases:
        value = grammar.derive(request(case["request"]))
        expected = sorted({iast(w) for w in case["expected_forms"]}) if case["kind"] == "derive" else case["expected_status"]
        actual = value.get("forms") if case["kind"] == "derive" else value["status"]
        completed = case["kind"] != "derive" or value["status"] == "COMPLETE_IN_REVIEWED_NON_THEMATIC_LAT_DOMAIN"
        result.append({"id": case["id"], "kind": case["kind"], "actual": actual,
                       "expected": expected, "agrees": actual == expected and completed})
    return result


def controls(g, records, roots):
    checks = []

    def check(id, condition):
        checks.append({"id": id, "agrees": bool(condition)})

    def req(id, pada="P", person="prathama", number="eka"):
        return Request(id, g.entries[id]["artha"], pada, person, number, True)

    def branch(id, pada="P", person="prathama", number="eka"):
        return g.derive(req(id, pada, person, number))["branches"][0]

    def rules(branch, phase="pre_tripadi"):
        return [e["rule"] for e in branch[phase]["history"]]

    def fails(call):
        try:
            call()
        except (ValueError, KeyError):
            return True
        return False

    f = g.pg6_scope.frame("7.1.5")
    check("7.1.5-retains-member-not-editorial-initial-component", any(t["term"] == "प्रत्ययस्य" for t in f["inherited"]) and any(t["term"] == "आदि" for t in f["excluded"]))
    f = g.pg6_scope.frame("8.4.2")
    check("nati-supplied-terms-preserve-parent-identities", all(any(t["term"] == term and t["source"] == "8.4.1" for t in f["inherited"]) for term in ("नः", "णः", "समानपदे")))
    check("kur-prohibition-has-local-non-padanta-reading", any(t["term"] == "पदस्य" for t in g.pg6_scope.frame("8.2.79")["excluded"]))
    changed = deepcopy(records)
    r = next(r for r in changed if r["i"] == "64087")
    r["an"] = "##".join(t for t in r["an"].split("##") if t != "असंयोगपूर्वस्य$64082")
    check("missing-cluster-inheritance-refuses-record", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "64108")["s"] = "वा करोतेः"
    check("changed-mandatory-wording-refused", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1090014")["gana"] = "1"
    check("pu-gana-cannot-alias-bhvadi-pu", fails(lambda: Grammar(records, changed)))
    changed = deepcopy(g.pg6)
    changed["priority"] = [e for e in changed["priority"] if e["winner"] != "6.4.108"]
    no_relation = Grammar(records, roots, review=changed)
    check("mandatory-kr-lopa-requires-recorded-priority", fails(lambda: no_relation.derive(req("1080010", person="uttama", number="dvi"))))

    su_s, su_w = branch("1050001"), branch("1050001", number="dvi")
    check("strong-status-follows-pit-ending", su_s["pre_tripadi"]["strength"]["pit"] and not su_s["pre_tripadi"]["strength"]["ngitvat"])
    check("weak-status-follows-ngitvat-ending", su_w["pre_tripadi"]["strength"]["ngitvat"] and not su_w["pre_tripadi"]["strength"]["pit"])
    check("root-guna-blocked-before-snu-in-both-strengths", all(any(b["by"] == "1.1.5" and b["trigger"] == "vikarana" for b in x["pre_tripadi"]["blocked"]) for x in (su_s, su_w)))
    check("strong-guna-targets-affix-u-not-root-u", any(e["rule"] == "7.3.84" and e["target_morpheme"] == "vikarana" and e["trigger"] == "ting" for e in su_s["pre_tripadi"]["history"]))
    check("weak-affix-guna-is-separately-blocked", any(b["by"] == "1.1.5" and b["trigger"] == "ting" for b in su_w["pre_tripadi"]["blocked"]))
    su_p, ap_p = branch("1050001", number="bahu"), branch("1050016", number="bahu")
    check("snu-simple-onset-uses-special-yan", "6.4.87" in rules(su_p) and "6.4.77" not in rules(su_p))
    check("snu-cluster-uses-uvang", "6.4.77" in rules(ap_p) and "6.4.87" not in rules(ap_p))
    ap_event = next(e for e in ap_p["pre_tripadi"]["history"] if e["rule"] == "6.4.77")
    check("cluster-is-counted-across-root-affix-seam", ap_event["context"]["cluster_before_u"] and ap_event["context"]["vowel_count"] == 2)
    tan_p = branch("1080001", number="bahu")
    check("tan-u-uses-iko-yan-not-snu-rule", "6.1.77" in rules(tan_p) and "6.4.87" not in rules(tan_p))
    su_v = g.derive(req("1050001", person="uttama", number="dvi"))
    check("u-lopa-retains-both-source-licensed-options", su_v["forms"] == ["sunuvaḥ", "sunvaḥ"] and len(su_v["branches"]) == 2)
    check("optional-branches-have-independent-state", su_v["branches"][0]["pre_tripadi"]["morphemes"] is not su_v["branches"][1]["pre_tripadi"]["morphemes"])
    check("cluster-blocks-u-lopa-before-v", g.derive(req("1050016", person="uttama", number="dvi"))["forms"] == ["āpnuvaḥ"])
    check("pit-mip-is-strong-not-optional-u-loss", g.derive(req("1050001", person="uttama"))["forms"] == ["sunomi"])
    kr_s, kr_w = branch("1080010"), branch("1080010", number="dvi")
    check("kr-retains-kar-before-weak-u-substitution", any(e["rule"] == "6.4.110" and e["before"][0]["symbol"] == "a" and e["after"][0]["symbol"] == "u" for e in kr_w["pre_tripadi"]["history"]))
    check("kr-a-to-u-does-not-apply-in-strong-form", "6.4.110" not in rules(kr_s) and kr_s["form"] == "karoti")
    kr_v = g.derive(req("1080010", person="uttama", number="dvi"))
    check("kr-u-loss-is-mandatory", kr_v["forms"] == ["kurvaḥ"] and len(kr_v["branches"]) == 1)
    ku = kr_v["branches"][0]
    check("part-lopa-preserves-u-affix-identity", ku["pre_tripadi"]["morphemes"][1]["identity"] == "u:3.1.79" and not ku["pre_tripadi"]["morphemes"][1]["visible"] and not ku["pre_tripadi"]["morphemes"][1].get("whole_affix_deletion"))
    check("length-query-does-not-restore-deleted-u", ku["readout"]["visibility_queries"][0]["deleted_u_is_not_restored"] and ku["readout"]["visibility_queries"][0]["license"] == "1.1.58")
    check("kur-length-is-explicitly-prohibited", any(b["by"] == "8.2.79" and b["rule"] == "8.2.77" for b in ku["readout"]["blocked"]) and ku["form"] != "kūrvaḥ")

    kri_d, kri_p = branch("1090001", number="dvi"), branch("1090001", number="bahu")
    check("sna-weak-consonant-and-vowel-paths-differ", "6.4.113" in rules(kri_d) and "6.4.112" in rules(kri_p) and "6.4.113" not in rules(kri_p))
    check("jh-becomes-vowel-initial-before-sna-decision", rules(kri_p).index("7.1.3") < rules(kri_p).index("6.4.112"))
    check("strong-sna-long-a-survives", branch("1090001")["form"] == "krīṇāti" and "6.4.112" not in rules(branch("1090001")))
    su_a = branch("1050001", "A", number="bahu")
    check("non-a-atmanepada-uses-at-not-ant", "7.1.5" in rules(su_a) and "7.1.3" not in rules(su_a) and su_a["form"] == "sunvate")
    kri_a = branch("1090001", "A", number="bahu")
    check("long-a-is-included-in-anatah-domain", "7.1.5" in rules(kri_a) and kri_a["form"] == "krīṇate")
    local = g.plan(req("1050001", "A", number="bahu"))["branches"][0]
    ting = local["morphemes"][-1]
    ting["visible"].insert(0, {"uid": "supplied:at", "symbol": "ā", "kind": "vowel"})
    g._non_a_ending(local, ting, req("1050001", "A", number="bahu"))
    check("7.1.5-does-not-skip-affix-internal-augment", "7.1.5" not in [e["rule"] for e in local["history"]] and sounds(ting) == ["ā", "a", "n", "t", "e"])
    local = g.plan(req("1050001", "A", number="bahu"))["branches"][0]
    local["morphemes"][-2]["visible"][-1]["symbol"] = "a"
    g._non_a_ending(local, local["morphemes"][-1], req("1050001", "A", number="bahu"))
    check("short-a-blocks-7.1.5", sounds(local["morphemes"][-1]) == ["a", "n", "t", "e"])
    for id in ("1090014", "1090016"):
        b = branch(id)
        check("identified-pvadi-shortening:" + id, any(e["rule"] == "7.3.80" and e["before"][0]["symbol"] == "ū" and e["after"][0]["symbol"] == "u" for e in b["pre_tripadi"]["history"]))
    sru = branch("1011092")
    change = next(e for e in sru["pre_tripadi"]["history"] if e["rule"] == "3.1.74" and e["effect"] == "coupled_sru_to_sr")
    check("sru-coupled-substitution-retains-original-root", [s["symbol"] for s in change["before"]] == ["ś", "r", "u"] and [s["symbol"] for s in change["after"]] == ["ś", "ṛ"] and not sru["pre_tripadi"]["open_obligations"])
    check("r-vowel-nati-supplement-is-attributed", any(e["rule"] == "8.4.1" and e["supplemental_reading"] for e in sru["readout"]["history"]))
    check("affix-s-retroflexion-remains-trigger-sensitive", branch("1050001", person="madhyama")["form"] == "sunoṣi" and branch("1090001", person="madhyama")["form"] == "krīṇāsi")
    check("atmanepada-se-s-retroflexion", branch("1090001", "A", "madhyama")["form"] == "krīṇīṣe")
    check("nati-unknown-exception-profile-is-unresolved", local_nati(["r", "a", "n", "a"], 2, same_pada=True, pada_final=False, exceptions_reviewed=False)["status"] == "UNRESOLVED")
    check("nati-needs-same-pada", local_nati(["r", "n", "a"], 1, same_pada=False, pada_final=False, exceptions_reviewed=True)["status"] == "INAPPLICABLE")
    check("pada-final-n-is-protected", local_nati(["r", "a", "n"], 2, same_pada=True, pada_final=True, exceptions_reviewed=True)["rule"] == "8.4.37")
    check("nati-crosses-the-reviewed-at-gap", local_nati(["k", "u", "r", "v", "a", "n", "t", "i"], 5, same_pada=True, pada_final=False, exceptions_reviewed=True)["status"] == "LICENSED")
    kr_p = branch("1080010", number="bahu")
    late = kr_p["readout"]["history"]
    check("kurvanti-n-is-hidden-during-nati", any(e["rule"] == "8.3.24" for e in late) and any(e["rule"] == "8.4.58" for e in late) and not any(e["effect"] == "local_nati" for e in late if "effect" in e) and kr_p["form"] == "kurvanti")
    check("kri-paradigm-retains-retroflex-and-dental-n", kri_p["form"] == "krīṇanti" and rules(kri_p, "readout").index("8.3.24") < rules(kri_p, "readout").index("8.4.2") < rules(kri_p, "readout").index("8.4.58"))
    original = deepcopy(kri_p["pre_tripadi"])
    before = digest(original)
    query = g._readout_non_thematic(original, g.entries["1090001"])
    check("readout-keeps-pre-tripadi-source-unchanged", digest(original) == before)
    check("repeat-readout-reproduces-history", query == kri_p["readout"])
    check("readout-cannot-feed-earlier-rules", fails(lambda: g._readout_non_thematic(query, g.entries["1090001"])))
    query["visible"][0]["symbol"] = "client-edit"
    check("readout-does-not-alias-source", digest(original) == before)
    # Only direct adapter-routing controls for old paths, not predecessor suite replay.
    for id, pada, person, form in [("1010001", "P", "prathama", "bhavati"), ("1010002", "A", "uttama", "edhe"), ("1100001", "P", "prathama", "corayati"), ("1040001", "P", "prathama", "dīvyati")]:
        check("PG5-routing:" + id, g.derive(req(id, pada, person))["forms"] == [form])
    return checks


def comparison(g, table):
    rows, events = [], Counter()
    for id in sorted(g.non_thematic_ids):
        entry = g.entries[id]
        for pada in ("P", "A") if entry["pada"] == "U" else (entry["pada"],):
            cells = table[entry["baseindex"]][pada.lower() + "lat"].split(";")
            if len(cells) != 9:
                raise ValueError("External table does not have nine laṭ cells")
            for i, cell in enumerate(cells):
                req = Request(id, entry["artha"], pada, g.review["ending_order"]["persons"][i // 3], g.review["ending_order"]["numbers"][i % 3], True)
                value = g.derive(req)
                expected = sorted({iast(w) for w in cell.split(",")})
                rows.append({"id": f"{id}:{pada}:{i}", "actual": value["forms"], "expected": expected,
                    "expected_devanagari": cell, "agrees": value["forms"] == expected,
                    "branches": len(value["branches"]), "history_sha256": digest(value["branches"])})
                events.update(e["rule"] for b in value["branches"] for e in b["pre_tripadi"]["history"] + b["readout"]["history"])
    return {"status": "PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE", "lexemes": len(g.non_thematic_ids),
            "paradigms": len(rows) // 9, "cells": len(rows), "branches": sum(r["branches"] for r in rows),
            "agreements": sum(r["agrees"] for r in rows), "differences": [r for r in rows if not r["agrees"]],
            "rule_event_counts": dict(sorted(events.items())), "rows": rows}


def build_report(source_root):
    packets = {n: load(HERE / n) for n in ("RULE_RECORDS.json", "LEXICAL_ENTRIES.json", "REFERENCE_CASES.json")}
    pins = load(HERE / "SOURCE_PINS.json")
    sources = check_sources(packets, pins, source_root)
    records = load(source_root / "sutraani/data.txt")["data"]
    roots = load(source_root / "dhatu/data.txt")["data"]
    before = digest([records, roots])
    g = Grammar(records, roots)
    cases = run_cases(g, packets["REFERENCE_CASES.json"]["cases"])
    checks = controls(g, records, roots)
    checks.append({"id": "source-records-unchanged", "agrees": digest([records, roots]) == before})
    cmp = comparison(g, load(source_root / "dhatu/dhatuforms_vidyut_shuddha_kartari.txt"))
    failures = [c["id"] for c in cases + checks if not c["agrees"]]
    return {"schema": "rkf.panini.pg6.v1", "author": "Monty",
            "status": "FAIL_BOUNDED_PG6_CONTRACTS" if failures else "PASS_BOUNDED_PG6_CONTRACTS",
            "sources": sources, "new_source_bound_records": len(g.pg6_rules),
            "scope_policies": len(g.pg6["scope_policies"]), "case_counts": dict(Counter(c["kind"] for c in cases)),
            "cases": cases, "direct_controls": checks, "failures": failures, "implementation_comparison": cmp,
            "claim_boundary": {"all_gana_members": False, "full_abhiya_or_sthanivad_engine": False,
                "general_nati_satva": False, "soundness_oracle": False, "all_lakaras": False,
                "infix_reduplication_accent_vedic": False, "native_operator_or_calculator_theorem": False}}


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
        raise SystemExit("PG6 report differs; inspect before writing or changing any pin")
    print(json.dumps({"status": report["status"], "sources": report["sources"],
        "cases": report["case_counts"], "controls": len(report["direct_controls"]), "failures": report["failures"],
        "comparison_cells": report["implementation_comparison"]["cells"],
        "comparison_branches": report["implementation_comparison"]["branches"],
        "comparison_differences": len(report["implementation_comparison"]["differences"])}, indent=2))
    return int(bool(report["failures"]))


if __name__ == "__main__":
    raise SystemExit(main())
