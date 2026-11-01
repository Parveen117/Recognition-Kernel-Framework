"""Direct PG10 source, morphology, ownership and optional-branch checks."""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path

from research.panini_grammar.present_expansion.grammar import Grammar, Request, ordered, sounds, root_and_following
from research.panini_grammar.root_progression.verify import check_sources, digest, load
from research.panini_grammar.vikarana_lat.verify import request, iast

HERE = Path(__file__).resolve().parent
COMPLETE = "COMPLETE_IN_REVIEWED_PRESENT_EXPANSION_DOMAIN"


def controls(g,records,roots):
    rows = []
    def check(label,value):rows.append({"id":label,"agrees":bool(value)})
    def req(id="1030002",**kw):
        profile = g.entries[id]["profiles"][0]
        return replace(Request(id,profile["sense"],profile["pada"],"prathama","eka",True),**kw)
    def value(id="1030002",**kw):return g.derive(req(id,**kw))
    def first(id="1030002",**kw):return value(id,**kw)["branches"][0]
    def events(branch,phase="pre_tripadi"):return branch[phase]["history"]
    def fails(call):
        try:call()
        except (ValueError,KeyError):return True
        return False
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "73095")["an"] = "सार्वधातुके$73087##ईट्$73093##वा$73094"
    check("iit-hal-inheritance-cannot-disappear",fails(lambda:Grammar(changed,roots)))
    changed = deepcopy(records)
    next(r for r in changed if r["i"] == "64115")["s"] = "भियः"
    check("bhi-option-wording-is-pinned",fails(lambda:Grammar(changed,roots)))
    changed = deepcopy(g.pg10)
    next(r for r in changed["records"] if r["sid"] == "7.3.89")["terms"].pop()
    check("non-abhyasta-condition-must-be-bound",fails(lambda:Grammar(records,roots,changed)))
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1030004")["aupadeshik"] = "पृ"
    check("long-pr-cannot-be-replaced-by-short-pr",fails(lambda:Grammar(records,changed)))
    changed = deepcopy(roots)
    next(r for r in changed if r["i"] == "1020029")["tags"] = "छान्दसः"
    check("register-annotation-drift-is-refused",fails(lambda:Grammar(records,changed)))
    plan = g.plan(req("1030003"))["branches"][0]
    source = deepcopy(plan["morphemes"][0]["visible"])
    g._copy10(plan)
    copy,root,vik,ting = plan["morphemes"]
    check("cluster-copy-links-all-three-source-sounds",[s["copied_from"] for s in copy["original"]] == [s["uid"] for s in source])
    check("copy-removes-only-its-internal-r",sounds(copy) == ["jh","i"] and root["visible"] == source)
    deleted = next(e for e in plan["history"] if e["effect"] == "noninitial_copy_consonant_lopa")
    check("deleted-cluster-r-keeps-copy-owner",deleted["target_morpheme"] == copy["id"] and deleted["before"][0]["symbol"] == "r")
    check("copy-original-keeps-long-vowel",[s["symbol"] for s in copy["original"]] == ["h","r","ī"])
    check("copy-cannot-repeat",fails(lambda:g._copy10(plan)))
    bad = g.plan(req("1030003"))["branches"][0]; bad["morphemes"][1]["whole_affix_deletion"]["kind"] = "luk"
    check("luk-cannot-trigger-copying",fails(lambda:g._copy10(bad)))
    for id in ["1030004","1030005","1030006"]:
        b = first(id); history = events(b)
        rapara = next(e for e in history if e["rule"] == "1.1.51")
        removed = next(e for e in history if e["effect"] == "noninitial_copy_consonant_lopa")
        check("rapara-r-is-later-deleted-from-copy:"+id,
              rapara["result"][-1]["uid"] == removed["before"][0]["uid"] and rapara["index"] < removed["index"])
        check("copy-i-is-distinct-from-root-strength:"+id,sounds(b["pre_tripadi"]["morphemes"][0])[-1] == "i")
    bhi = value(number="dvi")
    check("bhi-both-weak-hal-options",bhi["forms"] == ["bibhitaḥ","bibhītaḥ"] and len(bhi["branches"]) == 2)
    check("bhi-strong-has-no-shortening-option",value()["forms"] == ["bibheti"] and len(value()["branches"]) == 1)
    b = first(number="bahu")
    check("bhi-vowel-initial-uses-yan-not-shortening",b["form"] == "bibhyati" and
          any(e["rule"] == "6.4.82" for e in events(b)) and not any(e["rule"] == "6.4.115" for e in events(b)))
    b = first("1030003",number="bahu")
    check("hri-cluster-forces-iyang",b["form"] == "jihriyati" and any(e["rule"] == "6.4.77" for e in events(b)) and
          any(e["rule"] == "6.4.82" for e in b["pre_tripadi"]["blocked"]))
    check("long-pr-weak-consonant",value("1030004",number="dvi")["forms"] == ["pipūrtaḥ"])
    b = first("1030004",number="bahu")
    check("long-pr-no-lengthening-before-vowel",b["form"] == "pipurati" and not any(e["rule"] == "8.2.77" for e in events(b,"readout")))
    check("short-pr-remains-a-distinct-paradigm",value("1030005",number="dvi")["forms"] == ["pipṛtaḥ"] and value("1030005",number="bahu")["forms"] == ["piprati"])
    b = first("1030004")
    check("strong-pr-guna-defeats-utva",b["form"] == "piparti" and any(e["rule"] == "7.1.102" and e["by"] == "7.3.84" for e in b["pre_tripadi"]["blocked"]))
    b = first("1030004",number="dvi")
    event = next(e for e in events(b,"readout") if e["rule"] == "8.2.77")
    check("long-pr-lengthening-is-root-owned",event["before"]["owner"] == "root:1030004" and event["before"]["symbol"] == "u")
    check("bhr-atmanepada-yan",value("1030006",pada="A")["forms"] == ["bibhṛte"] and value("1030006",pada="A",number="dvi")["forms"] == ["bibhrāte"])
    check("class2-ma-and-class3-ma-are-distinct",value("1020057")["forms"] == ["māti"] and value("1030007")["forms"] == ["mimīte"])
    check("motion-ha-and-abandoning-ha-are-distinct",value("1030008")["forms"] == ["jihīte"] and value("1030009")["forms"] == ["jahāti"])
    check("ha-tyaga-keeps-both-weak-options",value("1030009",number="dvi")["forms"] == ["jahitaḥ","jahītaḥ"])
    for id,word in [("1030007","mimate"),("1030008","jihate"),("1030009","jahati")]:
        b = first(id,number="bahu")
        check("non-ghu-a-lopa-before-vowel:"+id,b["form"] == word and any(e["rule"] == "6.4.112" for e in events(b)))
    for id,copyword,strong,weak in [("1030012","ne","nenekti","nenijati"),("1030013","ve","vevekti","vevijati"),("1030014","ve","veveṣṭi","veviṣati")]:
        a,b = first(id),first(id,number="bahu")
        check("copy-guna-in-both-strengths:"+id,"".join(sounds(a["pre_tripadi"]["morphemes"][0])) == copyword == "".join(sounds(b["pre_tripadi"]["morphemes"][0])))
        check("root-guna-separate-from-copy-guna:"+id,a["form"] == strong and b["form"] == weak and
              any(e["rule"] == "7.3.86" for e in events(a)) and not any(e["rule"] == "7.3.86" for e in events(b)))
    b = first("1030012",pada="A",person="madhyama",number="bahu")
    check("nij-j-kutva-before-dhv",b["form"] == "nenigdhve" and any(e["rule"] == "8.2.30" for e in events(b,"readout")))
    b = first("1030014",pada="A",person="madhyama",number="bahu")
    order = [e["rule"] for e in events(b,"readout")]
    check("vis-retroflex-contact-before-voicing",b["form"] == "veviḍḍhve" and order.index("8.4.41") < order.index("8.4.53"))
    for id,word in [("1020027","yauti"),("1020030","nauti"),("1020031","kṣauti"),("1020032","kṣṇauti"),("1020033","snauti")]:
        b = first(id)
        check("adadi-u-vrddhi-with-root-preprocessing:"+id,b["form"] == word and any(e["rule"] == "7.3.89" for e in events(b)))
    check("weak-u-no-vrddhi",value("1020027",number="dvi")["forms"] == ["yutaḥ"])
    check("vowel-initial-u-uses-uvang",value("1020027",number="bahu")["forms"] == ["yuvanti"])
    check("u-root-before-v-keeps-vowel",value("1020027",person="uttama",number="dvi")["forms"] == ["yuvaḥ"])
    plan = g.plan(req("1020028"))["branches"][0]
    g._non_a_ending(plan,plan["morphemes"][-1],req("1020028"))
    check("ru-iit-is-eligible",g._iit_eligible(plan))
    no_pit = deepcopy(plan);no_pit["morphemes"][-1]["features"]["pit"] = False
    check("iit-does-not-require-pit",g._iit_eligible(no_pit))
    for feature in ["ting","sarvadhatuka"]:
        altered = deepcopy(plan);altered["morphemes"][-1]["features"][feature] = False
        check("iit-requires-"+feature,g._iit(altered) is False and len(altered["morphemes"]) == 3)
    altered = deepcopy(plan);altered["morphemes"][-1]["visible"][0]["symbol"] = "a"
    check("iit-requires-hal-initial-ending",g._iit(altered) is False)
    altered = g.plan(req("1020027"))["branches"][0]
    check("yu-cannot-borrow-ru-iit",g._iit(altered) is False)
    check("iit-is-prescribed",g._iit(plan) is True)
    root,following = root_and_following(plan); augment = plan["morphemes"][2]
    check("iit-belongs-to-ting-not-anga",following is augment and augment["host"] == "ting" and plan["augmented_ending"]["members"] == [augment["id"],"ting"])
    check("iit-marker-memory-is-separate",[s["symbol"] for s in augment["original"]] == ["ī","ṭ"] and sounds(augment) == ["ī"] and augment["features"]["pratyaya"] is False)
    check("iit-cannot-be-inserted-twice",g._iit(plan) is False)
    broken = deepcopy(plan);broken["morphemes"][2]["host"] = "root"
    check("wrong-augment-host-is-refused",fails(lambda:ordered(broken)))
    broken = deepcopy(plan);broken["augmented_ending"]["members"].reverse()
    check("reversed-tit-placement-is-refused",fails(lambda:ordered(broken)))
    changed = deepcopy(g.pg10)
    next(r for r in changed["records"] if r["sid"] == "7.3.95")["parameters"]["teaching"] = "ईड्"
    bad = Grammar(records,roots,changed)
    check("iit-teaching-marker-cannot-drift",fails(lambda:bad.derive(req("1020028"))))
    ru = value("1020028")
    check("ru-both-strong-options",ru["forms"] == ["rauti","ravīti"])
    b = next(b for b in ru["branches"] if b["form"] == "ravīti")
    order = [e["rule"] for e in events(b)]
    check("iit-before-guna-before-ayadi",order.index("7.3.95") < order.index("7.3.84") < order.index("6.1.78"))
    check("iit-blocks-hal-vrddhi",any(e["rule"] == "7.3.89" and e.get("first_owner") == "augment:iit" for e in b["pre_tripadi"]["blocked"]))
    b = next(b for b in value("1020028",number="dvi")["branches"] if b["form"] == "ruvītaḥ")
    check("weak-iit-uses-uvang-not-guna",any(e["rule"] == "6.4.77" for e in events(b)) and not any(e["rule"] == "7.3.84" for e in events(b)))
    check("plural-ending-resolved-before-iit",value("1020028",number="bahu")["forms"] == ["ruvanti"] and len(value("1020028",number="bahu")["branches"]) == 1)
    check("stu-A-apit-option",value("1020038",pada="A")["forms"] == ["stute","stuvīte"])
    check("stu-A-vowel-ending-no-iit",value("1020038",pada="A",number="dvi")["forms"] == ["stuvāte"])
    check("urnu-both-strong-options",value("1020034")["forms"] == ["ūrṇauti","ūrṇoti"])
    check("urnu-weak-no-strong-options",value("1020034",number="dvi")["forms"] == ["ūrṇutaḥ"])
    check("urnu-U-pada-is-explicit",value("1020034",pada="A")["forms"] == ["ūrṇute"])
    check("hnu-cluster-u-uses-uvang",value("1020077",number="dvi")["forms"] == ["hnuvāte"])
    b = first("1020044",number="bahu")
    seam = next(e for e in events(b) if e["rule"] == "6.1.101")
    check("ya-joint-substitution-keeps-both-uids",b["form"] == "yānti" and [s["symbol"] for s in seam["before"]] == ["ā","a"] and len(seam["after"][0]["replaces"]) == 2)
    check("joint-long-a-has-ending-owner",any(s["symbol"] == "ā" and s["owner"] == "ting" for s in ordered(b["pre_tripadi"])))
    check("class2-a-does-not-borrow-abhyasta-lopa",value("1020044",number="dvi")["forms"] == ["yātaḥ"] and not any(e["rule"] == "6.4.112" for e in events(first("1020044",number="dvi"))))
    check("dap-and-daa-have-distinct-paths",value("1020054")["forms"] == ["dāti"] and value("1030010")["forms"] == ["dadāti"])
    b = first("1020056",number="bahu"); order = [e["rule"] for e in events(b,"readout")]
    check("late-nasal-does-not-feed-back-to-nati",b["form"] == "prānti" and order.index("8.3.24") < order.index("8.4.58") and "8.4.2" not in order)
    source = b["pre_tripadi"]; before = digest(source); output = g._readout10(source)
    check("readout-does-not-mutate-source",digest(source) == before)
    check("readout-is-repeatable",output == g._readout10(source))
    check("readout-cannot-feed-back",fails(lambda:g._readout10(output[0])))
    output[0]["visible"][0]["symbol"] = "client-change"
    check("readout-has-no-source-alias",digest(source) == before)
    # Minimal old dispatch coverage; frozen predecessor suites are not run.
    for id,pada,word in [("1010001","P","bhavati"),("1080010","P","karoti"),("1070001","P","ruṇaddhi"),("1020060","P","asti"),("1030001","P","juhoti"),("1030011","A","dhatte")]:
        r = Request(id,g.entries[id]["artha"],pada,"prathama","eka",True)
        check("unchanged-dispatch:"+id,g.derive(r).get("forms") == [word])
    return rows


def comparison(g,table):
    rows = []; invariants = {"all_plans_have_resolved_obligations":True,"all_visible_uids_are_unique":True,
        "all_copies_keep_root_source_links":True,"all_iit_units_belong_to_endings":True,"branch_forms_equal_reported_forms":True}
    for id in sorted(g.pg10_ids):
        e = g.entries[id]
        for pf in e["profiles"]:
            cells = table[e["baseindex"]][pf["pada"].lower()+"lat"].split(";")
            if len(cells) != 9:raise ValueError("Expected nine present cells")
            for i,cell in enumerate(cells):
                r = Request(id,pf["sense"],pf["pada"],g.review["ending_order"]["persons"][i//3],g.review["ending_order"]["numbers"][i%3],True)
                v = g.derive(r); expected = sorted({iast(w) for w in cell.split(",")})
                invariants["branch_forms_equal_reported_forms"] &= sorted({b["form"] for b in v["branches"]}) == v["forms"]
                for b in v["branches"]:
                    state = b["pre_tripadi"]; seq = ordered(state)
                    invariants["all_plans_have_resolved_obligations"] &= not state["open_obligations"]
                    invariants["all_visible_uids_are_unique"] &= len({s["uid"] for s in seq}) == len(seq)
                    for u in state["morphemes"]:
                        if u["kind"] == "abhyasa":
                            copy = next(e for e in state["history"] if e["rule"] == "6.1.10")
                            invariants["all_copies_keep_root_source_links"] &= [s["copied_from"] for s in u["original"]] == [s["uid"] for s in copy["source_span"]]
                        if u["kind"] == "augment":
                            invariants["all_iit_units_belong_to_endings"] &= u["host"] == "ting" and state["augmented_ending"]["members"] == [u["id"],"ting"]
                rows.append({"id":f"{id}:{pf['pada']}:{i}","group":e["group"],"actual":v.get("forms"),"expected":expected,
                    "agrees":v["status"] == COMPLETE and v.get("forms") == expected,"branches":len(v.get("branches",[])),"history_sha256":digest(v.get("branches"))})
    return {"status":"PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE","lexemes":len(g.pg10_ids),
        "paradigms":len(rows)//9,"cells":len(rows),"branches":sum(r["branches"] for r in rows),
        "differences":[r for r in rows if not r["agrees"]],"rows":rows,"all_branch_invariants":invariants}


def coverage(g,cmp,roots,witnesses):
    prior = load(HERE.parent/'abhyasa_lat/COVERAGE_STATUS.json');old = prior["complete_lat_profile"]
    old_ids = set(old["root_ids"])
    if old_ids & g.pg10_ids:raise ValueError("New lexical coverage overlaps frozen coverage")
    ids = set(prior["source_bound_records_pg4_pg9"]["distinct_ids"]) | set(g.pg10_rules)
    groups = {}
    for group in ["juhotyadi","adadi_u","adadi_a"]:
        members = {id for id in g.pg10_ids if g.entries[id]["group"] == group};rows = [r for r in cmp["rows"] if r["group"] == group]
        groups[group] = {"root_ids":sorted(members),"root_entries":len(members),"cells":len(rows),"paradigms":len(rows)//9,"branches":sum(r["branches"] for r in rows)}
    source = {r["i"]:r for r in roots}; all_ids = old_ids | g.pg10_ids
    return {"author":"Monty","overall_grammar_completion_percent":None,"text_inventory":prior["text_inventory"],
        "source_bound_records_pg4_pg10":{"definitions":prior["source_bound_records_pg4_pg9"]["definitions"]+len(g.pg10_rules),"distinct_count":len(ids),"distinct_ids":sorted(ids)},
        "complete_lat_profile":{"root_entries":len(all_ids),"root_entry_denominator":old["root_entry_denominator"],
            "root_entries_pending":old["root_entry_denominator"]-len(all_ids),"root_ids":sorted(all_ids),
            "cells":old["cells"]+cmp["cells"],"paradigms":old["paradigms"]+cmp["paradigms"],"branches":old["branches"]+cmp["branches"],
            "new_root_ids":sorted(g.pg10_ids),"prior_report":"../abhyasa_lat/COVERAGE_STATUS.json","prior_evidence":"frozen report read; no predecessor suite or certificate replay"},
        "new_groups":groups,
        "class3":{"complete_root_entries":sum(source[id]["gana"] == "3" for id in all_ids),"source_rows":sum(r["gana"] == "3" for r in roots),
                  "unmarked_entries_covered":14,"unmarked_entries_in_source":14,"tagged_rows_unadmitted":12,
                  "boundary":"First fourteen unmarked entries in the pinned gaṇa have the stated present profiles. The tagged ṛ entry also has a traditional classical-use discussion; it still requires its own vowel-initial review."},
        "class2":{"complete_root_entries":sum(source[id]["gana"] == "2" for id in all_ids),"source_rows":sum(r["gana"] == "2" for r in roots),"source_lexical_rows":sum(r["gana"] == "2" and r["aupadeshik"] != "-" for r in roots)},
        "class7":prior["class7"],
        "literal_commentary_word_evidence":{"witnesses":sum(witnesses["literal_word_witnesses_by_root"].values()),"roots_with_literal_words":len(witnesses["literal_word_witnesses_by_root"]),"no_separate_word_witness_ids":witnesses["no_separate_word_witness_ids"],"boundary":"These six entries have pinned lexical/rule contracts and implementation comparisons, but no separate full-word witness in the selected commentary passages."},
        "companion_nominal_outputs":"Separate domains; not counted as verb cells.","full_grammar_and_native_operator_lift":"OPEN"}


def build(source_root):
    packets = {n:load(HERE/n) for n in ["RULE_RECORDS.json","LEXICAL_ENTRIES.json","REFERENCE_CASES.json"]}
    sources = check_sources(packets,load(HERE/'SOURCE_PINS.json'),source_root)
    records = load(source_root/'sutraani/data.txt')["data"]; roots = load(source_root/'dhatu/data.txt')["data"]
    original = digest([records,roots]);g = Grammar(records,roots);cases = []
    for c in packets["REFERENCE_CASES.json"]["cases"]:
        v = g.derive(request(c["request"]))
        expected = sorted({iast(w) for w in c["attested_forms"]}) if c["kind"] == "attested_member" else c["expected_status"]
        actual = v.get("forms",v["status"])
        ok = v["status"] == COMPLETE and set(expected) <= set(actual) if c["kind"] == "attested_member" else v["status"] == expected
        cases.append({"id":c["id"],"kind":c["kind"],"actual":actual,"expected":expected,"agrees":ok})
    checks = controls(g,records,roots)
    checks.append({"id":"source-inputs-unchanged","agrees":digest([records,roots]) == original})
    cmp = comparison(g,load(source_root/'dhatu/dhatuforms_vidyut_shuddha_kartari.txt'))
    checks += [{"id":"all-branches:"+k,"agrees":v} for k,v in cmp["all_branch_invariants"].items()]
    cov = coverage(g,cmp,roots,packets["REFERENCE_CASES.json"])
    failures = [r["id"] for r in cases+checks if not r["agrees"]]+["comparison:"+r["id"] for r in cmp["differences"]]
    report = {"schema":"rkf.panini.pg10.v1","author":"Monty","status":"FAIL_BOUNDED_PG10_CONTRACTS" if failures else "PASS_BOUNDED_PG10_CONTRACTS",
        "sources":sources,"case_counts":dict(Counter(c["kind"] for c in cases)),"cases":cases,"direct_controls":checks,
        "failures":failures,"implementation_comparison":cmp,"coverage_sha256":digest(cov),"source_bound_records":len(g.pg10_rules),
        "claim_boundary":{"raw_sanskrit_interpreter":False,"general_reduplicator":False,"general_asiddha_solver":False,"all_lakaras":False,"soundness_oracle":False,"native_operator_theorem":False}}
    return report,cov


def main():
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument('--source-root',type=Path,required=True);parser.add_argument('--write',action='store_true');args = parser.parse_args()
    report,cov = build(args.source_root)
    for name,value in [('VERIFICATION_RESULT.json',report),('COVERAGE_STATUS.json',cov)]:
        text = json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True)+'\n';target = HERE/name
        if args.write:target.write_text(text,encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8') != text:raise SystemExit('PG10 report differs: '+name)
    print(json.dumps({'status':report['status'],'sources':report['sources'],'cases':report['case_counts'],'controls':len(report['direct_controls']),
        'failures':report['failures'],'comparison_cells':report['implementation_comparison']['cells'],'comparison_branches':report['implementation_comparison']['branches'],
        'comparison_differences':len(report['implementation_comparison']['differences']),
        'combined_coverage':{k:v for k,v in cov['complete_lat_profile'].items() if k not in ['root_ids','new_root_ids']}},indent=2))
    return int(bool(report['failures']))


if __name__ == '__main__':raise SystemExit(main())
