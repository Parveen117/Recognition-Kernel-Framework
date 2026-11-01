"""Direct PG8 source, ownership, ordering and scope checks. No prior replay."""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path

from research.panini_grammar.exception_lat.grammar import Grammar, Request, ordered, sounds
from research.panini_grammar.root_progression.verify import check_sources, digest, load
from research.panini_grammar.vikarana_lat.verify import request, iast

HERE = Path(__file__).resolve().parent
COMPLETE = {"COMPLETE_IN_REVIEWED_EXCEPTION_LAT_DOMAIN", "COMPLETE_IN_REVIEWED_SNAM_LAT_DOMAIN"}


def controls(g, records, roots):
    rows = []
    def check(label, value):
        rows.append({"id": label, "agrees": bool(value)})
    def req(id="1070018", **kw):
        p = g.entries[id]["profiles"][0]
        return replace(Request(id, p["sense"], p["pada"], "prathama", "eka", True), **kw)
    def first(id="1070018", **kw):
        return g.derive(req(id, **kw))["branches"][0]
    def fails(call):
        try:
            call()
        except (ValueError, KeyError):
            return True
        return False
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "73092")["an"] = "सार्वधातुके$73087##हलि$73089"
    check("im-pit-inheritance-cannot-disappear", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "13066")["s"] = "भुजः"
    check("bhuj-semantic-restriction-cannot-disappear", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1070017")["gana"] = "6"
    check("same-spelling-bhuj-cannot-change-gana", fails(lambda: Grammar(records, changed)))
    check("source-pada-P-not-overwritten-to-U", g.entries["1070017"]["pada"] == "P")
    for sense,pada,effect in [("पालने","P","anavana_condition_false"),("अभ्यवहारे","A","atmanepada_prescribed")]:
        b = first("1070017", sense=sense, pada=pada)
        event = next(e for e in b["pre_tripadi"]["history"] if e["rule"] == "1.3.66")
        check("bhuj-sense-history:"+pada, event["sense"] == sense and event["outcome"] == effect and event["source_pada"] == "P")
        check("bhuj-request-keeps-real-pada:"+pada, b["pre_tripadi"]["request"]["pada"] == pada)
    trh = first(); state = trh["pre_tripadi"]; units = state["morphemes"]
    check("nested-layout-retains-one-root", len([u for u in units if u["kind"] == "root"]) == 1)
    check("im-is-augment-not-pratyaya", units[2]["kind"] == "augment" and units[2]["features"]["pratyaya"] is False)
    check("two-distinct-m-it-owners", units[1]["marker_evidence"]["marker_units"][-1]["label"] == "m" and units[2]["marker_evidence"]["marker_units"][0]["label"] == "m")
    check("original-im-preserved", sounds({"visible": units[2]["original"]}) == ["i","m"])
    check("im-m-is-absent-from-speech", all(s["uid"] != units[2]["original"][1]["uid"] for s in ordered(state)))
    check("im-host-has-three-members", len(state["host_constituent"]["members"]) == 3)
    check("im-placed-after-snam-a-not-root-vowel", state["augment_layout"]["after_source_uid"].startswith("vikarana:"))
    seam = next(e for e in state["history"] if e["rule"] == "6.1.87")
    check("ekadesha-keeps-both-source-uids", [s["symbol"] for s in seam["before"]] == ["a","i"] and len(seam["after"][0]["replaces"]) == 2)
    check("ekadesha-has-augment-surface-owner", any(s["symbol"] == "e" and s["owner"] == "augment:im" for s in ordered(state)))
    history = state["history"]
    place = next(e["index"] for e in history if e["effect"] == "place_owned_mit_infix")
    prescribe = next(e["index"] for e in history if e["rule"] == "7.3.92")
    check("snam-before-im-before-guna", place < prescribe < seam["index"])
    check("old-root-guna-is-blocked-by-snam", any(e["rule"] == "7.3.86" and e["by"] == "3.1.78" for e in state["blocked"]))
    check("pre-tripadi-is-not-final-word", state["projection"] == "tṛnehti" and trh["form"] == "tṛṇeḍhi")
    weak = first(number="dvi")
    check("weak-trh-has-no-im", len(weak["pre_tripadi"]["morphemes"]) == 3 and not any(e["rule"] == "7.3.92" for e in weak["pre_tripadi"]["history"]))
    check("weak-snam-lopa-keeps-original-a", any(e["effect"] == "snam_a_lopa" and e["before"][0]["symbol"] == "a" for e in weak["pre_tripadi"]["history"]))
    query = trh["readout"]["visibility_queries"]
    check("stutva-read-permission-is-explicit", any(q.get("query") == "8.3.13" and q["visible_rule"] == "8.4.41" and q["global_tripadi_reversal"] is False for q in query))
    order = [e["rule"] for e in trh["readout"]["history"]]
    check("h-dh-stutva-lopa-order", order.index("8.2.31") < order.index("8.2.40") < order.index("8.4.41") < order.index("8.3.13"))
    deleted = next(e for e in trh["readout"]["history"] if e["rule"] == "8.3.13")
    check("lopa-target-is-root-owned", deleted["target"]["owner"] == "root:1070018")
    changed = deepcopy(g.pg8); changed["visibility_exceptions"] = []
    bad = Grammar(records, roots, review=changed)
    check("missing-special-visibility-is-refused", fails(lambda: bad.derive(req())))
    second = first(person="madhyama")
    order = [e["rule"] for e in second["readout"]["history"]]
    check("trh-si-uses-k-path-not-ddh-lopa", "8.2.41" in order and "8.3.13" not in order and second["form"] == "tṛṇekṣi")
    for person,number in [("prathama","bahu"),("uttama","dvi"),("uttama","bahu")]:
        b = first(person=person,number=number)
        check("h-survives-before-non-jhal:"+person+number, "h" in [s["symbol"] for s in b["readout"]["visible"]] and not any(e["rule"] == "8.2.31" for e in b["readout"]["history"]))
    # Negative augment guards on a fresh pre-strength plan: the requirement
    # is actual tiṅ features and initial sound, not the person/number label.
    for feature in ["pit", "sarvadhatuka"]:
        plan = g.plan(req())["branches"][0]; g._placement(plan)
        plan["morphemes"][-1]["features"][feature] = False
        check("im-needs-"+feature, g._im(plan) is False and len(plan["morphemes"]) == 3)
    plan = g.plan(req())["branches"][0]; g._placement(plan)
    plan["morphemes"][-1]["visible"][0]["symbol"] = "a"
    check("im-needs-hal-initial-trigger", g._im(plan) is False)
    for id in ["1020001","1020060"]:
        b = first(id); root,vik,ting = b["pre_tripadi"]["morphemes"]
        check("retained-sap-luk:"+id, not vik["visible"] and vik["identity"].startswith("śap") and bool(vik["original"]))
        check("luk-identity-not-marker-deletion:"+id, vik["whole_affix_deletion"] == {"kind":"luk","rule":"2.4.72"})
    check("as-strong-a-retained", first("1020060")["pre_tripadi"]["projection"] == "asti")
    b = first("1020060",number="dvi")
    check("as-weak-deletes-only-root-a", any(e["effect"] == "as_a_lopa" and e["target_morpheme"] == "root:1020060" for e in b["pre_tripadi"]["history"]))
    check("as-does-not-borrow-snam-visibility", not any(q.get("query") == "8.3.24/8.4.58" for q in b["readout"]["visibility_queries"]))
    b = first("1020060",person="madhyama")
    check("asi-deletes-root-s-not-ending-s", any(e["effect"] == "as_s_lopa_before_s" and e["target_morpheme"] == "root:1020060" for e in b["pre_tripadi"]["history"]) and sounds(b["pre_tripadi"]["morphemes"][-1]) == ["s","i"])
    check("ad-does-not-receive-as-s-deletion", not any(e["rule"] == "7.4.50" for e in first("1020001",person="madhyama")["pre_tripadi"]["history"]))
    before = digest(state); result = g._readout8(state)
    check("readout-does-not-mutate-source", digest(state) == before)
    check("readout-is-repeatable", result == g._readout8(state))
    check("readout-cannot-feed-back", fails(lambda: g._readout8(result[0])))
    result[0]["visible"][0]["symbol"] = "client-change"
    check("readout-has-no-source-alias", digest(state) == before)
    broken = deepcopy(state);broken["augment_layout"] = None
    check("nested-member-needs-layout", fails(lambda: ordered(broken)))
    broken = deepcopy(state);broken["infix_layout"]["after_uid"] = "absent"
    check("lost-root-anchor-is-refused", fails(lambda: ordered(broken)))
    for id,pada,word in [("1010001","P","bhavati"),("1080010","P","karoti"),("1070002","P","bhinatti")]:
        r = Request(id,g.entries[id]["artha"],pada,"prathama","eka",True)
        check("unchanged-dispatch:"+id, g.derive(r).get("forms") == [word])
    r = Request("1070001",g.entries["1070001"]["artha"],"P","prathama","eka",True)
    b = g.derive(r)["branches"][0]
    check("dh-final-is-not-the-lexical-dha-exception", b["form"] == "ruṇaddhi" and
          any(e["rule"] == "8.2.40" for e in b["readout"]["history"]))
    return rows


def comparison(g, table):
    rows=[]
    for id in sorted(g.pg8_ids):
        entry=g.entries[id]
        for profile in entry["profiles"]:
            cells=table[entry["baseindex"]][profile["pada"].lower()+"lat"].split(";")
            if len(cells) != 9: raise ValueError("Expected nine laṭ cells")
            for i,cell in enumerate(cells):
                req=Request(id,profile["sense"],profile["pada"],g.review["ending_order"]["persons"][i//3],g.review["ending_order"]["numbers"][i%3],True)
                value=g.derive(req);expected=sorted({iast(w) for w in cell.split(",")})
                rows.append({"id":f"{id}:{profile['pada']}:{i}","sense":profile["sense"],"actual":value.get("forms"),"expected":expected,
                    "agrees":value["status"] in COMPLETE and value.get("forms")==expected,"branches":len(value.get("branches",[])),"history_sha256":digest(value.get("branches"))})
    return {"status":"PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE","lexemes":len(g.pg8_ids),"paradigms":len(rows)//9,
        "cells":len(rows),"branches":sum(r["branches"] for r in rows),"differences":[r for r in rows if not r["agrees"]],"rows":rows}


def coverage(g, cmp):
    prior=load(HERE.parent/'snam_lat/COVERAGE_STATUS.json')
    old=prior["complete_lat_profile"];old_ids={id for stage in old["stages"] for id in stage["root_ids"]}
    if old_ids & g.pg8_ids: raise ValueError("New root entries would be double-counted")
    ids=set(prior["pg4_to_pg7_source_bound_records"]["distinct_ids"]) | set(g.pg8_rules)
    return {"author":"Monty","overall_grammar_completion_percent":None,
        "text_inventory":prior["text_inventory"],"source_bound_sutra_ids_pg4_pg8":len(ids),
        "bounded_record_definitions_pg4_pg8":prior["pg4_to_pg7_source_bound_records"]["definitions"]+len(g.pg8_rules),
        "complete_lat_profile":{"root_entries":len(old_ids | g.pg8_ids),"root_entry_denominator":old["root_entry_denominator"],
            "root_entries_pending":old["root_entry_denominator"]-len(old_ids | g.pg8_ids),
            "cells":old["cells"]+cmp["cells"],"paradigms":old["paradigms"]+cmp["paradigms"],"branches":old["branches"]+cmp["branches"],
            "new_root_ids":sorted(g.pg8_ids),"prior_report":"../snam_lat/COVERAGE_STATUS.json","prior_evidence":"frozen report read, not replayed"},
        "class7":{"root_entries":25,"source_rows":25,"scope":"identified unprefixed classical kartari present profiles; bhuj meanings explicitly selected; not all contexts of class 7"},
        "class2":{"complete_root_entries":2,"root_ids":["1020001","1020060"],"other_members":"OPEN"},
        "class3":"OPEN: reduplication and full paths pending",
        "companion_kta_outputs":"Separate reported domain; not added to verb cells; see CONCURRENT_REVIEW.json",
        "full_grammar_and_native_operator_lift":"OPEN"}


def build(source_root):
    packets={n:load(HERE/n) for n in ["RULE_RECORDS.json","LEXICAL_ENTRIES.json","REFERENCE_CASES.json","CONCURRENT_REVIEW.json"]}
    sources=check_sources(packets,load(HERE/'SOURCE_PINS.json'),source_root)
    records=load(source_root/'sutraani/data.txt')["data"];roots=load(source_root/'dhatu/data.txt')["data"]
    original=digest([records,roots]);g=Grammar(records,roots);cases=[]
    for c in packets["REFERENCE_CASES.json"]["cases"]:
        value=g.derive(request(c["request"]))
        expected=sorted({iast(w) for w in c["attested_forms"]}) if c["kind"]=="attested_member" else c["expected_status"]
        actual=value.get("forms",value["status"])
        ok=value["status"] in COMPLETE and set(expected)<=set(actual) if c["kind"]=="attested_member" else value["status"]==expected
        cases.append({"id":c["id"],"kind":c["kind"],"actual":actual,"expected":expected,"agrees":ok})
    checks=controls(g,records,roots)
    checks.append({"id":"source-inputs-unchanged","agrees":digest([records,roots])==original})
    cmp=comparison(g,load(source_root/'dhatu/dhatuforms_vidyut_shuddha_kartari.txt'));cov=coverage(g,cmp)
    failures=[r["id"] for r in cases+checks if not r["agrees"]]+["comparison:"+r["id"] for r in cmp["differences"]]
    report={"schema":"rkf.panini.pg8.v1","author":"Monty","status":"FAIL_BOUNDED_PG8_CONTRACTS" if failures else "PASS_BOUNDED_PG8_CONTRACTS",
        "sources":sources,"case_counts":dict(Counter(c["kind"] for c in cases)),"cases":cases,"direct_controls":checks,"failures":failures,
        "implementation_comparison":cmp,"coverage_sha256":digest(cov),"source_bound_records":len(g.pg8_rules),
        "claim_boundary":{"raw_sanskrit_interpreter":False,"general_asiddha_solver":False,"all_lakaras":False,"soundness_oracle":False,"native_operator_theorem":False}}
    return report,cov


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--source-root',type=Path,required=True);parser.add_argument('--write',action='store_true');args=parser.parse_args()
    report,cov=build(args.source_root)
    for name,value in [('VERIFICATION_RESULT.json',report),('COVERAGE_STATUS.json',cov)]:
        text=json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True)+'\n';target=HERE/name
        if args.write: target.write_text(text,encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8')!=text: raise SystemExit('PG8 report differs: '+name)
    print(json.dumps({'status':report['status'],'sources':report['sources'],'cases':report['case_counts'],'controls':len(report['direct_controls']),
        'failures':report['failures'],'comparison_cells':report['implementation_comparison']['cells'],'comparison_differences':len(report['implementation_comparison']['differences']),
        'coverage':cov['complete_lat_profile']},indent=2))
    return int(bool(report['failures']))


if __name__=='__main__':
    raise SystemExit(main())
