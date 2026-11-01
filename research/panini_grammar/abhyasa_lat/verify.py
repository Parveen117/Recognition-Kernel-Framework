"""Direct PG9 source, copy ownership, strength and visibility checks."""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path

from research.panini_grammar.abhyasa_lat.grammar import Grammar, Request, ordered, sounds
from research.panini_grammar.root_progression.verify import check_sources, digest, load
from research.panini_grammar.vikarana_lat.verify import request, iast

HERE = Path(__file__).resolve().parent
COMPLETE = "COMPLETE_IN_REVIEWED_ABHYASA_LAT_DOMAIN"


def controls(g, records, roots):
    rows = []
    def check(label, value):
        rows.append({"id": label, "agrees": bool(value)})
    def req(id="1030011", **kw):
        return replace(Request(id, g.entries[id]["artha"], "P", "prathama", "eka", True), **kw)
    def first(id="1030011", **kw):
        return g.derive(req(id, **kw))["branches"][0]
    def fails(call):
        try:
            call()
        except (ValueError, KeyError):
            return True
        return False
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "61010")["s"] = "श्लुः"
    check("slu-wording-cannot-drift", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "71004")["an"] = "झः$71003"
    check("jh-scope-annotation-drift-is-refused", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(g.pg9)
    next(r for r in changed["records"] if r["sid"] == "8.2.38")["terms"].pop()
    check("jhas-final-binding-cannot-disappear", fails(lambda: Grammar(records, roots, changed)))
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1030001")["gana"] = "1"
    check("lexical-class-identity-is-pinned", fails(lambda: Grammar(records, changed)))
    plan = g.plan(req("1030001"))["branches"][0]
    plan["morphemes"][1]["whole_affix_deletion"]["kind"] = "luk"
    check("luk-cannot-trigger-slu-reduplication", fails(lambda: g._reduplicate(plan)))
    plan = g.plan(req("1030001"))["branches"][0]
    plan["morphemes"][0]["visible"].append(deepcopy(plan["morphemes"][0]["visible"][0]))
    check("unreviewed-root-shape-cannot-be-copied", fails(lambda: g._reduplicate(plan)))
    plan = g.plan(req("1030010"))["branches"][0]
    source = deepcopy(plan["morphemes"][0]["visible"])
    g._reduplicate(plan)
    check("existing-abhyasa-is-not-reduplicated", fails(lambda: g._reduplicate(plan)))
    copy, root, vik, ting = plan["morphemes"]
    check("copy-links-every-source-sound", [s["copied_from"] for s in copy["original"]] == [s["uid"] for s in source])
    check("copied-sound-uids-are-new", not ({s["uid"] for s in source} & {s["uid"] for s in copy["original"]}))
    check("teaching-markers-are-not-copied", [s["symbol"] for s in copy["original"]] == ["d", "ā"] and len(root["original"]) > 2)
    check("shortening-keeps-original-long-vowel", sounds(copy) == ["d", "a"] and copy["original"][1]["symbol"] == "ā")
    check("copy-shortening-does-not-mutate-root", root["visible"] == source)
    check("abhyasa-is-not-pratyaya", copy["features"]["pratyaya"] is False)
    check("abhyasta-is-collective", plan["abhyasta"]["members"] == [copy["id"], root["id"]] and plan["abhyasta"]["collective"])
    check("slu-retains-whole-sap-history", not vik["visible"] and bool(vik["original"]) and vik["whole_affix_deletion"] == {"kind":"ślu", "rule":"2.4.75"})
    broken = deepcopy(plan); broken["abhyasta"]["members"].pop()
    check("one-member-cannot-license-abhyasta-ending", fails(lambda: g._ending9(broken, req("1030010"))))
    broken = deepcopy(plan); broken["morphemes"][0]["source_owner"] = "wrong"
    check("wrong-copy-owner-is-refused", fails(lambda: ordered(broken)))
    hu = first("1030001"); state = hu["pre_tripadi"]
    abhyasa,root,vik,ting = state["morphemes"]
    check("hu-strong-guna-only-on-root", sounds(root) == ["h","o"] and sounds(abhyasa) == ["jh","u"])
    history = state["history"]
    check("copy-before-strong-guna", next(e["index"] for e in history if e["rule"] == "6.1.10") < next(e["index"] for e in history if e["effect"] == "guna"))
    check("h-palatalization-precedes-late-jastva", state["projection"] == "jhuhoti" and hu["form"] == "juhoti"
          and any(e["rule"] == "8.4.54" for e in hu["readout"]["history"]))
    weak = first("1030001",number="dvi")
    check("weak-hu-blocks-root-guna", not any(e["effect"] == "guna" for e in weak["pre_tripadi"]["history"])
          and any(e["rule"] == "7.3.84" and e["by"] == "1.1.5" for e in weak["pre_tripadi"]["blocked"]))
    check("hu-no-yan-before-consonant", weak["form"] == "juhutaḥ" and not any(e["rule"] == "6.4.87" for e in weak["pre_tripadi"]["history"]))
    plural = first("1030001",number="bahu")
    event = next(e for e in plural["pre_tripadi"]["history"] if e["rule"] == "6.4.87")
    check("hu-yan-target-is-root-owned", event["target_morpheme"] == "root:1030001" and event["context"]["whole_anga_vowels"] == 2)
    check("abhyasta-jh-excludes-ant", sounds(plural["pre_tripadi"]["morphemes"][-1]) == ["a","t","i"]
          and any(e["rule"] == "7.1.3" and e["by"] == "7.1.4" for e in plural["pre_tripadi"]["blocked"]))
    check("hu-affix-satva-is-separate", first("1030001",person="madhyama")["form"] == "juhoṣi")
    for number,word in [("dvi","juhuvaḥ"),("bahu","juhumaḥ")]:
        b = first("1030001",person="uttama",number=number)
        check("hu-root-u-is-not-optional-affix-u:"+number, b["form"] == word and
              any(e["rule"] == "6.4.107" for e in b["pre_tripadi"]["blocked"]))
    for id in ["1030010","1030011"]:
        strong = first(id)
        check("strong-a-survives:"+id, sounds(strong["pre_tripadi"]["morphemes"][1])[-1] == "ā")
        b = first(id,number="dvi")
        state = b["pre_tripadi"]
        event = next(e for e in state["history"] if e["effect"] == "abhyasta_final_a_lopa")
        check("weak-a-lopa-on-root-not-copy:"+id, event["target_morpheme"] == "root:"+id and
              sounds(state["morphemes"][0])[-1] == "a" and state["morphemes"][1]["original"])
        check("ghu-blocks-i-substitution:"+id, any(e["rule"] == "6.4.113" and e["by"] == "1.1.20" for e in state["blocked"]))
        check("A-dual-keeps-its-ending-long-a:"+id, sounds(first(id,pada="A",number="dvi")["pre_tripadi"]["morphemes"][-1]) == ["ā","t","e"])
    for id,pada,number in [("1030010","P","bahu"),("1030011","A","bahu")]:
        b = first(id,pada=pada,number=number)
        check("collective-at-prescription:"+id+pada, any(e["effect"] == "abhyasta_jh_to_at" for e in b["pre_tripadi"]["history"])
              and not any(e["rule"] in {"7.1.3","7.1.5"} for e in b["pre_tripadi"]["history"]))
    dha = first(number="dvi"); view = dha["readout"]
    check("dha-local-visibility-is-recorded", len(view["visibility_queries"]) == 1 and
          view["visibility_queries"][0]["visible_rule"] == "8.4.54" and view["visibility_queries"][0]["global_tripadi_reversal"] is False)
    order = [e["rule"] for e in view["history"]]
    check("jastva-then-bhas-then-final-devoicing", order.index("8.4.54") < order.index("8.2.38") < order.index("8.4.55"))
    event = next(e for e in view["history"] if e["rule"] == "8.2.38")
    check("bhas-target-is-copy-owned", event["before"]["owner"] == "abhyasa:1030011" and event["before"]["symbol"] == "d" and event["after"]["symbol"] == "dh")
    check("bhas-not-erased-by-reentered-jastva", dha["form"] == "dhattaḥ" and order.count("8.4.54") == 1)
    check("lexical-dha-blocks-t-th-dh", any(e["rule"] == "8.2.40" for e in view["blocked"]) and "8.2.40" not in order)
    for kwargs,word in [({"person":"madhyama","number":"dvi"},"dhatthaḥ"),
                       ({"pada":"A","person":"madhyama"},"dhatse"),
                       ({"pada":"A","person":"madhyama","number":"bahu"},"dhaddhve")]:
        b = first(**kwargs)
        check("dha-bhas-trigger:"+word, b["form"] == word and any(e["rule"] == "8.2.38" for e in b["readout"]["history"]))
    for kwargs,word in [({},"dadhāti"),({"number":"bahu"},"dadhati"),
                       ({"person":"uttama","number":"dvi"},"dadhvaḥ"),
                       ({"person":"uttama","number":"bahu","pada":"A"},"dadhmahe")]:
        b = first(**kwargs)
        check("dha-no-spurious-bhas:"+word, b["form"] == word and not b["readout"]["visibility_queries"])
    check("da-does-not-borrow-dha-bhas", first("1030010",number="dvi")["form"] == "dattaḥ"
          and not first("1030010",number="dvi")["readout"]["visibility_queries"])
    changed = deepcopy(g.pg9); changed["visibility_exceptions"] = []
    bad = Grammar(records,roots,changed)
    check("missing-dha-local-permission-is-refused", fails(lambda: bad.derive(req(number="dvi"))))
    check("unrelated-hu-does-not-use-dha-permission", bad.derive(req("1030001"))["forms"] == ["juhoti"])
    changed = deepcopy(g.pg9); changed["priority"] = [e for e in changed["priority"] if e["winner"] != "7.1.4"]
    bad = Grammar(records,roots,changed)
    check("missing-at-priority-is-refused", fails(lambda: bad.derive(req(number="bahu"))))
    source = dha["pre_tripadi"]; before = digest(source); output = g._readout9(source)
    check("readout-does-not-mutate-source", digest(source) == before)
    check("readout-is-repeatable", output == g._readout9(source))
    check("readout-cannot-feed-back", fails(lambda: g._readout9(output)))
    output["visible"][0]["symbol"] = "client-change"
    check("readout-has-no-source-alias", digest(source) == before)
    # Four dispatch controls only, not a replay of the frozen suites.
    for id,pada,word in [("1010001","P","bhavati"),("1080010","P","karoti"),
                         ("1070001","P","ruṇaddhi"),("1020060","P","asti")]:
        b = g.derive(Request(id,g.entries[id]["artha"],pada,"prathama","eka",True))
        check("unchanged-dispatch:"+id, b.get("forms") == [word])
        if id == "1070001":
            check("other-dh-final-root-keeps-8.2.40", any(e["rule"] == "8.2.40" for e in b["branches"][0]["readout"]["history"]))
    return rows


def comparison(g, table):
    rows = []
    for id in sorted(g.pg9_ids):
        entry = g.entries[id]
        for profile in entry["profiles"]:
            cells = table[entry["baseindex"]][profile["pada"].lower()+"lat"].split(";")
            if len(cells) != 9:
                raise ValueError("Expected nine laṭ cells")
            for i,cell in enumerate(cells):
                req = Request(id,profile["sense"],profile["pada"],g.review["ending_order"]["persons"][i//3],
                              g.review["ending_order"]["numbers"][i%3],True)
                value = g.derive(req); expected = sorted({iast(w) for w in cell.split(",")})
                rows.append({"id":f"{id}:{profile['pada']}:{i}", "actual":value.get("forms"), "expected":expected,
                    "agrees":value["status"] == COMPLETE and value.get("forms") == expected,
                    "branches":len(value.get("branches",[])), "history_sha256":digest(value.get("branches"))})
    return {"status":"PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE", "lexemes":len(g.pg9_ids),
            "paradigms":len(rows)//9, "cells":len(rows), "branches":sum(r["branches"] for r in rows),
            "differences":[r for r in rows if not r["agrees"]], "rows":rows}


def coverage(g, cmp, roots):
    prior = load(HERE.parent/'exception_lat/COVERAGE_STATUS.json')
    pg7 = load(HERE.parent/'snam_lat/COVERAGE_STATUS.json')
    old = prior["complete_lat_profile"]
    old_ids = {id for stage in pg7["complete_lat_profile"]["stages"] for id in stage["root_ids"]} | set(old["new_root_ids"])
    if len(old_ids) != old["root_entries"] or old_ids & g.pg9_ids:
        raise ValueError("Prior/new lexical coverage would be miscounted")
    ids = set(pg7["pg4_to_pg7_source_bound_records"]["distinct_ids"]) | set(g.pg8_rules) | set(g.pg9_rules)
    return {"author":"Monty", "overall_grammar_completion_percent":None, "text_inventory":prior["text_inventory"],
        "source_bound_records_pg4_pg9":{"definitions":prior["bounded_record_definitions_pg4_pg8"]+len(g.pg9_rules),
                                      "distinct_count":len(ids), "distinct_ids":sorted(ids)},
        "complete_lat_profile":{"root_entries":len(old_ids | g.pg9_ids), "root_entry_denominator":old["root_entry_denominator"],
            "root_entries_pending":old["root_entry_denominator"]-len(old_ids | g.pg9_ids),
            "root_ids":sorted(old_ids | g.pg9_ids), "cells":old["cells"]+cmp["cells"],
            "paradigms":old["paradigms"]+cmp["paradigms"], "branches":old["branches"]+cmp["branches"],
            "new_root_ids":sorted(g.pg9_ids), "prior_report":"../exception_lat/COVERAGE_STATUS.json",
            "prior_evidence":"frozen reports read; no predecessor suite or certificate replay"},
        "class3":{"root_entries":len(g.pg9_ids), "source_rows":sum(r["gana"] == "3" for r in roots),
                  "new_cells":cmp["cells"], "new_paradigms":cmp["paradigms"],
                  "scope":"hu P, dā/dhā P and A; unprefixed classical present with supplied semantic/pada license"},
        "class7":prior["class7"], "class2":prior["class2"],
        "companion_nominal_outputs":"Separate T86–T89 domains; not added to present cells; see CONCURRENT_REVIEW.json",
        "full_grammar_and_native_operator_lift":"OPEN"}


def build(source_root):
    packets = {n:load(HERE/n) for n in ["RULE_RECORDS.json","LEXICAL_ENTRIES.json","REFERENCE_CASES.json","CONCURRENT_REVIEW.json"]}
    sources = check_sources(packets,load(HERE/'SOURCE_PINS.json'),source_root)
    records = load(source_root/'sutraani/data.txt')["data"]; roots = load(source_root/'dhatu/data.txt')["data"]
    original = digest([records,roots]); g = Grammar(records,roots); cases = []
    for case in packets["REFERENCE_CASES.json"]["cases"]:
        value = g.derive(request(case["request"]))
        expected = sorted({iast(w) for w in case["attested_forms"]}) if case["kind"] == "attested_member" else case["expected_status"]
        actual = value.get("forms",value["status"])
        ok = value["status"] == COMPLETE and set(expected) <= set(actual) if case["kind"] == "attested_member" else value["status"] == expected
        cases.append({"id":case["id"], "kind":case["kind"], "actual":actual, "expected":expected, "agrees":ok})
    checks = controls(g,records,roots)
    checks.append({"id":"source-inputs-unchanged", "agrees":digest([records,roots]) == original})
    cmp = comparison(g,load(source_root/'dhatu/dhatuforms_vidyut_shuddha_kartari.txt')); cov = coverage(g,cmp,roots)
    failures = [r["id"] for r in cases+checks if not r["agrees"]]+["comparison:"+r["id"] for r in cmp["differences"]]
    report = {"schema":"rkf.panini.pg9.v1", "author":"Monty",
        "status":"FAIL_BOUNDED_PG9_CONTRACTS" if failures else "PASS_BOUNDED_PG9_CONTRACTS",
        "sources":sources, "case_counts":dict(Counter(c["kind"] for c in cases)), "cases":cases,
        "direct_controls":checks, "failures":failures, "implementation_comparison":cmp,
        "coverage_sha256":digest(cov), "source_bound_records":len(g.pg9_rules),
        "claim_boundary":{"general_reduplicator":False, "raw_sanskrit_interpreter":False, "general_asiddha_solver":False,
                          "all_lakaras":False, "soundness_oracle":False, "native_operator_theorem":False}}
    return report,cov


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True); parser.add_argument('--write',action='store_true')
    args = parser.parse_args(); report,cov = build(args.source_root)
    for name,value in [('VERIFICATION_RESULT.json',report),('COVERAGE_STATUS.json',cov)]:
        text = json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True)+'\n'; target = HERE/name
        if args.write:
            target.write_text(text,encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8') != text:
            raise SystemExit('PG9 report differs: '+name)
    print(json.dumps({'status':report['status'], 'sources':report['sources'], 'cases':report['case_counts'],
        'controls':len(report['direct_controls']), 'failures':report['failures'],
        'comparison_cells':report['implementation_comparison']['cells'],
        'comparison_differences':len(report['implementation_comparison']['differences']),
        'coverage':cov['complete_lat_profile']},indent=2))
    return int(bool(report['failures']))


if __name__ == '__main__':
    raise SystemExit(main())
