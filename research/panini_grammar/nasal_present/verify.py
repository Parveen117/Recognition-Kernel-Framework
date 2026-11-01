"""Direct PG12 source, ownership, branching and ordering checks."""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path

from research.panini_grammar.nasal_present.grammar import Grammar, Request, ordered, sounds, nati_choice
from research.panini_grammar.non_thematic_lat.grammar import u_context
from research.panini_grammar.root_progression.verify import check_sources, digest, file_digest, load
from research.panini_grammar.vikarana_lat.verify import request, iast

HERE = Path(__file__).resolve().parent
COMPLETE = "COMPLETE_IN_REVIEWED_NASAL_PRESENT_DOMAIN"


def controls(g, records, roots):
    rows = []
    def check(name, value): rows.append({"id": name, "agrees": bool(value)})
    def fails(call):
        try: call()
        except (ValueError, KeyError): return True
        return False
    def req(id="1090071", **kw):
        p = g.entries[id]["profiles"][0]
        return replace(Request(id, p["sense"], p["pada"], "prathama", "eka", True), **kw)
    def value(id="1090071", **kw): return g.derive(req(id, **kw))
    def branch(id="1090071", form=None, **kw):
        bs = value(id, **kw)["branches"]
        return bs[0] if form is None else next(b for b in bs if b["form"] == form)
    def raw(id="1090071", affix=None, **kw):
        r = req(id, **kw); plans = g.plan(r)["branches"]
        s = plans[0] if affix is None else next(s for s in plans if s["choice"]["affix"] == affix)
        s["pg12_options"] = []
        return s, r
    def prepared(id="1090071", **kw):
        s,r = raw(id, **kw); g._prepare12(s); return s,r
    def history(b, phase="pre_tripadi"): return b[phase]["history"]
    def rules(b, phase="pre_tripadi"): return [e["rule"] for e in history(b, phase)]
    record = deepcopy(next(r for r in g.pg12["records"] if r["sid"] == "3.1.82"))
    record["terms"] = [t for t in record["terms"] if t["term"] != "श्ना"]
    check("optional-sna-inheritance-cannot-disappear", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    record = deepcopy(next(r for r in g.pg12["records"] if r["sid"] == "3.1.81")); record["terms"][0]["case"] = "6"
    check("source-ablative-is-not-genitive", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    record = deepcopy(next(r for r in g.pg12["records"] if r["sid"] == "6.4.2")); record["terms"] = [t for t in record["terms"] if t["term"] != "अणः"]
    check("lengthening-an-domain-must-bind", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    record = deepcopy(g.pg12["records"][0]); record["terms"].append(deepcopy(record["terms"][0]))
    check("same-occurrence-cannot-be-bound-twice", g.pg12_scope.compile(record)["status"] == "UNRESOLVED_RECORD")
    changed = deepcopy(records); next(r for r in changed if r["i"] == "73080")["an"] = ""
    check("source-sit-inheritance-cannot-be-erased", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(records); next(r for r in changed if r["i"] == "61016")["s"] = "changed"
    check("samprasarana-wording-is-pinned", fails(lambda: Grammar(changed, roots)))
    changed = deepcopy(roots); next(r for r in changed if r["i"] == "1050033")["tags"] = "अनुदात्तोपदेशः"
    check("classical-exception-retains-vedic-tag", fails(lambda: Grammar(records, changed)))
    changed = deepcopy(roots); next(r for r in changed if r["i"] == "1090060")["dhatu_note"] = "silently resolved"
    check("initial-u-source-disagreement-cannot-be-erased", fails(lambda: Grammar(records, changed)))

    for id, affixes in [("1050002", {"śnu"}), ("1080004", {"u"}), ("1090034", {"śnā"}), ("1090007", {"śnu", "śnā"})]:
        check("exact-affix-selection:"+id, {x["affix"] for x in g.select(req(id))["choices"]} == affixes)
    s,_ = raw("1090034"); s["choice"].update(affix="śnu", rule="3.1.73"); s["morphemes"][1] = g._affix("śnu", "vikarana")
    check("wrong-source-class-affix-is-refused", fails(lambda: g._prepare12(s)))
    s,_ = prepared(); check("preparation-cannot-repeat", fails(lambda: g._prepare12(s)))
    bad = deepcopy(s); bad["morphemes"][0]["identity"] = "1090034"
    check("root-owner-cannot-change", fails(lambda: ordered(bad)))
    bad = deepcopy(s); bad["morphemes"].insert(1, deepcopy(bad["morphemes"][0]))
    check("no-fabricated-extra-root-or-augment", fails(lambda: ordered(bad)))
    bad = deepcopy(s); bad["morphemes"][-1]["visible"][0]["uid"] = bad["morphemes"][0]["visible"][0]["uid"]
    check("visible-uids-cannot-be-duplicated", fails(lambda: ordered(bad)))
    b = branch("1050033")
    check("kshi-classical-license-remains-inspectable", "छान्दसः" in b["pre_tripadi"]["lexical_register_evidence"]["source_tags"] and b["form"] == "kṣiṇoti")
    b = branch("1090060")
    check("udhras-marker-reading-preserves-teaching", b["form"] == "dhrasnāti" and b["pre_tripadi"]["morphemes"][0]["teaching"].startswith("उँ"))

    s,_ = raw("1090007"); before = deepcopy(s["morphemes"][0]["visible"][-2]); check("n-lopa-applies", g._n_lopa12(s))
    event = s["history"][-1]
    check("n-lopa-retains-owned-deleted-source", event["before"] == [before] and event["target_morpheme"] == "root:1090007" and sounds(s["morphemes"][0]) == ["s", "t", "a", "bh"])
    check("n-lopa-cannot-repeat", not g._n_lopa12(s))
    s,_ = raw("1090007"); s["root_preprocessing"]["idit"] = True
    check("idit-blocks-root-n-lopa", not g._n_lopa12(s) and sounds(s["morphemes"][0])[-2] == "n")
    s,_ = raw("1090007")
    for f in ["kit", "ngit", "ngitvat"]: s["morphemes"][1]["features"][f] = False
    check("non-knit-affix-blocks-n-lopa", not g._n_lopa12(s))
    s,_ = raw("1090007"); s["morphemes"][0]["visible"][-2]["symbol"] = "m"
    check("n-lopa-does-not-delete-other-nasals", not g._n_lopa12(s))
    s,_ = raw("1080002")
    check("final-n-is-not-penultimate-n", not g._n_lopa12(s))
    for id, form in [("1050026", "dabhnoti"), ("1090044", "badhnāti"), ("1090050", "kuthnāti")]:
        b = branch(id); check("distinct-root-n-lopa:"+id, b["form"] == form and "6.4.24" in rules(b))
    for id in [str(1090000+i) for i in range(6,11)]:
        v = value(id)
        check("optional-snu-sna-preserved:"+id, len(v["branches"]) == 2 and {b["pre_tripadi"]["choice"]["affix"] for b in v["branches"]} == {"śnu", "śnā"})
    check("sku-affix-choice-composes-with-u-loss", len(value("1090006", person="uttama", number="dvi")["branches"]) == 3)
    check("stambh-cluster-blocks-u-loss", len(value("1090007", person="uttama", number="dvi")["branches"]) == 2)
    check("stambh-snu-vowel-junction-is-uv", "stabhnuvanti" in value("1090007", number="bahu")["forms"])

    b = branch("1090071"); s = b["pre_tripadi"]; h = history(b); e = next(e for e in h if e["rule"] == "6.1.108")
    check("grah-samprasarana-owner-retained", s["samprasarana"]["owner"] == "root:1090071" and s["samprasarana"]["source"]["symbol"] == "r")
    check("samprasarana-precedes-purvarupa", rules(b).index("6.1.16") < rules(b).index("1.1.45") < rules(b).index("6.1.108"))
    check("purvarupa-remembers-both-root-sounds", [x["symbol"] for x in e["before"]] == ["ṛ", "a"] and e["source_samprasarana_uid"] == e["before"][0]["uid"] and len(e["after"][0]["replaces"]) == 2)
    check("grah-nonfinal-vowel-is-not-lengthened", "6.4.2" not in rules(b) and any(x["rule"] == "6.4.2" for x in s["blocked"]) and b["form"] == "gṛhṇāti")
    s,_ = raw(); g._samprasarana12(s)
    check("samprasarana-cannot-repeat", fails(lambda: g._samprasarana12(s)))
    s,_ = raw()
    for f in ["kit", "ngit", "ngitvat"]: s["morphemes"][1]["features"][f] = False
    check("samprasarana-requires-knit", not g._samprasarana12(s))
    s,_ = raw("1090043")
    check("jna-cannot-borrow-jya-samprasarana", not g._samprasarana12(s))
    b = branch("1090034"); h = history(b); order = rules(b)
    check("jya-purvarupa-lengthening-shortening-order", b["form"] == "jināti" and order.index("6.1.108") < order.index("6.4.2") < order.index("7.3.80"))
    long = next(e for e in h if e["rule"] == "6.4.2"); short = next(e for e in h if e["rule"] == "7.3.80")
    check("jya-shortening-keeps-intermediate-long-vowel", short["before"] == long["after"] and short["target_morpheme"] == "root:1090034")
    b = branch("1090043")
    check("jna-long-ja-remains-distinct", b["form"] == "jānāti" and "7.3.79" in rules(b) and "7.3.80" not in rules(b))
    for id, form in [("1090040", "vrīṇāti"), ("1090041", "bhrīṇāti"), ("1090042", "kṣīṇāti"), ("1090069", "heṭhṇāti")]:
        b = branch(id)
        check("explicit-pvadi-endpoint:"+id, b["form"] == form and not b["pre_tripadi"]["pvadi_membership"]["member"] and "7.3.80" not in rules(b))
    check("same-dhu-headword-different-gana-shortening", value("1050010")["forms"] == ["dhūnoti"] and value("1090020")["forms"] == ["dhunāti"])
    s,_ = raw("1090020"); s["morphemes"][1]["features"]["sit"] = False; g._prepare12(s)
    check("pvadi-shortening-requires-sit", sounds(s["morphemes"][0]) == ["dh", "ū"])
    b = branch("1090017")
    check("pvadi-short-r-blocks-long-r-replacement", sounds(b["pre_tripadi"]["morphemes"][0]) == ["s", "t", "ṛ"] and any(x["rule"] == "7.1.100" and x["by"] == "7.3.80" for x in b["pre_tripadi"]["blocked"]))
    b = branch("1090070")
    check("sva-r-substitute-has-labiodental-license", "7.1.102" in rules(b) and any(x["rule"] == "7.1.100" and x["by"] == "7.1.102" for x in b["pre_tripadi"]["blocked"]))
    rapara = next(e for e in history(b) if e["rule"] == "1.1.51")
    check("sva-rapara-r-retains-source-vowel", rapara["source"]["symbol"] == "ṝ" and [x["symbol"] for x in rapara["result"]] == ["u", "r"])
    check("sva-lengthening-is-readout-only", sounds(b["pre_tripadi"]["morphemes"][0]) == ["s", "v", "u", "r"] and b["form"] == "svūrṇāti" and "8.2.77" in rules(b, "readout"))

    s,_ = raw("1090068"); check("ut-substitution-applies", g._ut12(s))
    ut = s["ut_substitute"]
    check("ut-is-owned-substitute-not-augment", ut["owner"] == "root:1090068" and ut["is_augment"] is False and len(s["morphemes"]) == 3 and ut["source"]["symbol"] == "v")
    check("ut-marker-retained-separately", [x["symbol"] for x in ut["teaching"]] == ["ū", "ṭh"] and ut["marker"]["symbol"] == "ṭh")
    check("ut-substitution-cannot-repeat", fails(lambda: g._ut12(s)))
    bad = deepcopy(s); bad["ut_substitute"]["owner"] = "vikarana"
    check("ut-junction-rejects-wrong-owner", fails(lambda: g._ut_junction12(bad)))
    bad = deepcopy(s); bad["ut_substitute"]["visible_uid"] = "invented"
    check("ut-junction-requires-actual-substitute-uid", fails(lambda: g._ut_junction12(bad)))
    bad = deepcopy(s); bad.pop("ut_substitute")
    check("ordinary-long-u-cannot-license-ut-vrddhi", fails(lambda: g._ut_junction12(bad)))
    g._ut_junction12(s)
    check("ut-junction-cannot-repeat", fails(lambda: g._ut_junction12(s)))
    check("ut-vrddhi-preserves-two-sound-source", sounds(s["morphemes"][0]) == ["kh", "au"] and next(e for e in s["history"] if e["rule"] == "6.1.89")["before"][1]["uid"] == ut["visible_uid"])
    s,_ = raw("1090068"); s["morphemes"][1]["visible"][0]["symbol"] = "y"
    check("ut-requires-nasal-initial-affix", not g._ut12(s))
    s,_ = raw("1090068")
    for f in ["kit", "ngit", "ngitvat"]: s["morphemes"][1]["features"][f] = False
    check("ut-requires-knit", not g._ut12(s))
    check("khac-and-khav-do-not-collapse", value("1090067")["forms"] == ["khacñāti"] and value("1090068")["forms"] == ["khaunāti"])

    s,_ = raw("1080005")
    check("root-strength-cannot-precede-preparation", fails(lambda: g._root_options12(s)))
    s,r = prepared("1080005"); options = g._root_options12(s)
    check("root-strength-cannot-repeat", fails(lambda: g._root_options12(options[0])))
    check("guna-created-cluster-changes-u-eligibility", not u_context(options[0])["cluster_before_u"] and u_context(options[1])["cluster_before_u"])
    check("root-guna-has-owned-r-accompaniment", any(e["rule"] == "1.1.51" and e["owner"] == "root:1080005" for e in options[1]["history"]))
    s,r = prepared("1080004")
    check("affix-strength-cannot-precede-root-strength", fails(lambda: g._affix_options12(s, r)))
    s = g._root_options12(s)[0]; out = g._affix_options12(s, r)
    check("affix-strength-cannot-repeat", fails(lambda: g._affix_options12(out[0], r)))
    for id in [str(1080000+i) for i in range(4,8)]:
        v = value(id, pada="A")
        check("weak-ending-still-allows-both-root-guna-readings:"+id, len(v["branches"]) == 2 and all(b["pre_tripadi"]["stem_strength"]["weak"] for b in v["branches"]))
    v = value("1080005", person="uttama", number="dvi")
    check("rn-cluster-denies-only-guna-u-loss-branch", v["forms"] == ["arṇuvaḥ", "ṛṇuvaḥ", "ṛṇvaḥ"] and len(v["branches"]) == 3)
    v = value("1080004", person="uttama", number="dvi")
    check("e-guna-keeps-u-loss-cross-product", len(v["branches"]) == 4)
    check("strong-ending-never-borrows-weak-u-loss", len(value("1080005", person="uttama")["branches"]) == 2)
    check("ordinary-tanadi-nasal-root-u-loss-retained", value("1080002", person="uttama", number="dvi")["forms"] == ["sanuvaḥ", "sanvaḥ"])
    b = branch("1090017", number="bahu"); order = rules(b)
    check("jh-substitution-precedes-sna-a-lopa", order.index("7.1.3") < order.index("6.4.112"))
    b = branch("1090017", pada="A", number="bahu"); order = rules(b)
    check("middle-jh-at-precedes-sna-a-lopa", order.index("7.1.5") < order.index("6.4.112"))
    check("sna-weak-hal-and-vowel-targets-differ", value("1090017", number="dvi")["forms"] == ["stṛṇītaḥ"] and value("1090017", number="bahu")["forms"] == ["stṛṇanti"])

    def nati(seq, **kw):
        args = dict(same_pada=True, pada_final=False, exceptions_reviewed=True, interveners=g.pg12_rules["8.4.2"]["parameters"]["interveners"]); args.update(kw)
        return nati_choice(seq, len(seq)-1, **args)
    check("nati-admits-labial-intervention", nati(["ṛ", "p", "n"])["status"] == "LICENSED")
    check("nati-admits-guttural-intervention", nati(["r", "g", "n"])["status"] == "LICENSED")
    check("nati-admits-mixed-reviewed-interveners", nati(["r", "a", "gh", "bh", "n"])["status"] == "LICENSED")
    check("nati-stops-at-dental", nati(["ṛ", "d", "n"])["status"] == "OUTSIDE_REVIEWED_WINDOW")
    check("nati-stops-at-l", nati(["r", "l", "n"])["status"] == "OUTSIDE_REVIEWED_WINDOW")
    check("nati-does-not-invent-num-extension", nati(["r", "ṃ", "n"])["status"] == "OUTSIDE_REVIEWED_WINDOW")
    check("nati-requires-same-word", nati(["r", "n"], same_pada=False)["status"] == "INAPPLICABLE")
    check("nati-excludes-word-final-n", nati(["r", "n"], pada_final=True)["rule"] == "8.4.37")
    check("nati-requires-exception-review", nati(["r", "n"], exceptions_reviewed=False)["status"] == "UNRESOLVED")
    check("nati-requires-known-boundaries", nati(["r", "n"], same_pada=None)["status"] == "UNRESOLVED")
    for id, form in [("1050028", "tṛpnoti"), ("1090055", "kṣubhnāti")]:
        b = branch(id)
        check("lexical-nati-prohibition:"+id, b["form"] == form and any(x["by"] == "8.4.39" and x["owner"] == "vikarana" for x in b["readout"]["blocked"]))
    for number, form in [("dvi", "kṣubhnītaḥ"), ("bahu", "kṣubhnanti")]:
        b = branch("1090055", number=number); q = b["readout"]["visibility_queries"][0]
        check("ksubh-prohibition-survives-a-change:"+number, b["form"] == form and q["retained_identity"] == "śnā:3.1.81" and q["restores_visible_sounds"] is False)
    original_rules = g.pg12_rules
    for field, changed, name in [("retained_identity", "śnu:3.1.73", "wrong-affix"),
                                 ("restores_visible_sounds", True, "invented-sound-restoration")]:
        g.pg12_rules = deepcopy(original_rules); g.pg12_rules["1.1.56"]["parameters"][field] = changed
        try: check("ksubh-query-refuses-"+name, fails(lambda: g._readout12(b["pre_tripadi"])))
        finally: g.pg12_rules = original_rules
    b = branch("1090017", number="bahu")
    check("late-ending-n-does-not-feed-back-to-nati", b["form"] == "stṛṇanti" and any(s["symbol"] == "n" and s["owner"] == "ting" for s in b["readout"]["visible"]))
    check("same-phonetic-n-not-all-retroflex", value("1090051")["forms"] == ["mṛdnāti"] and value("1090052")["forms"] == ["mṛḍṇāti"])
    check("s-contact-prohibition-remains-active", value("1090058")["forms"] == ["kliśnāti"])
    s = b["pre_tripadi"]; before = digest(s); v = g._readout12(s)
    check("readout-preserves-source", digest(s) == before)
    check("readout-is-repeatable", v == g._readout12(s))
    check("readout-cannot-feed-back", fails(lambda: g._readout12(v)))
    v["visible"][0]["symbol"] = "client-change"
    check("readout-has-no-source-alias", digest(s) == before)
    check("untyped-request-is-refused", g.derive({})["status"] == "UNRESOLVED")
    for id,pada,word in [("1050001","P","sunoti"),("1080010","P","karoti"),("1090001","P","krīṇāti"),
                         ("1020039","P","bravīti"),("1030017","P","iyarti"),("1070001","P","ruṇaddhi")]:
        r = Request(id, g.entries[id]["artha"], pada, "prathama", "eka", True)
        check("unchanged-dispatch:"+id, word in g.derive(r).get("forms", []))
    return rows


def comparison(g, table):
    rows = []
    invariants = {k: True for k in ["resolved_obligations", "unique_visible_uids", "one_root_one_affix_one_ending",
        "root_teaching_retained", "distinct_branch_ids", "branch_forms_equal_reported_forms", "ut_substitute_owned_by_root"]}
    for id in sorted(g.pg12_ids):
        e = g.entries[id]
        for pf in e["profiles"]:
            cells = table[e["baseindex"]][pf["pada"].lower()+"lat"].split(";")
            if len(cells) != 9: raise ValueError("Nine comparison cells are required")
            for i, cell in enumerate(cells):
                r = Request(id, pf["sense"], pf["pada"], g.review["ending_order"]["persons"][i//3], g.review["ending_order"]["numbers"][i%3], True)
                v = g.derive(r); expected = sorted({iast(w) for w in cell.split(",")})
                invariants["branch_forms_equal_reported_forms"] &= sorted({b["form"] for b in v["branches"]}) == v["forms"]
                invariants["distinct_branch_ids"] &= len({b["branch_id"] for b in v["branches"]}) == len(v["branches"])
                for b in v["branches"]:
                    s = b["pre_tripadi"]; seq = ordered(s)
                    invariants["resolved_obligations"] &= not s["open_obligations"]
                    invariants["unique_visible_uids"] &= len({x["uid"] for x in seq}) == len(seq)
                    invariants["one_root_one_affix_one_ending"] &= len(s["morphemes"]) == 3 and sum(u["kind"] == "root" for u in s["morphemes"]) == 1
                    invariants["root_teaching_retained"] &= s["morphemes"][0]["teaching"] == e["aupadeshik"]
                    if s.get("ut_substitute"):
                        invariants["ut_substitute_owned_by_root"] &= s["ut_substitute"]["owner"] == s["morphemes"][0]["id"] and s["ut_substitute"]["is_augment"] is False
                rows.append({"id": f"{id}:{pf['pada']}:{i}", "group": e["group"], "actual": v["forms"], "expected": expected,
                             "agrees": v["status"] == COMPLETE and v["forms"] == expected, "branches": len(v["branches"]), "history_sha256": digest(v["branches"])})
    return {"status": "PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE", "lexemes": len(g.pg12_ids), "paradigms": len(rows)//9,
            "cells": len(rows), "branches": sum(r["branches"] for r in rows), "differences": [r for r in rows if not r["agrees"]],
            "all_branch_invariants": invariants, "rows": rows}


def coverage(g, cmp, roots, witnesses):
    prior = load(HERE.parent/'lexical_present/COVERAGE_STATUS.json'); old = prior["complete_lat_profile"]
    old_ids = set(old["root_ids"])
    if old_ids & g.pg12_ids: raise ValueError("PG12 double-counts a prior completed root")
    all_ids = old_ids | g.pg12_ids
    sutras = set(prior["source_bound_records_pg4_pg11"]["distinct_ids"]) | set(g.pg12_rules)
    groups = {}
    for name in ["further_svadi", "further_tanadi", "further_kryadi"]:
        members = {id for id in g.pg12_ids if g.entries[id]["group"] == name}; rows = [r for r in cmp["rows"] if r["group"] == name]
        groups[name] = {"root_ids": sorted(members), "root_entries": len(members), "paradigms": len(rows)//9,
                        "cells": len(rows), "branches": sum(r["branches"] for r in rows)}
    classes = {}
    for gana in ["5", "8", "9"]:
        source_ids = {r["i"] for r in roots if r["gana"] == gana}
        classes["class"+gana] = {"source_rows": len(source_ids), "complete_root_entries": len(all_ids & source_ids),
            "remaining_ids": sorted(source_ids-all_ids), "scope": "identified unprefixed classical present profiles; not every context or textual interpretation"}
    old_gaps = sorted(set(prior["literal_commentary_word_evidence"]["no_separate_word_witness_ids"] + prior["literal_commentary_word_evidence"]["inherited_pg10_witness_gaps"]))
    return {"author": "Monty", "overall_grammar_completion_percent": None, "text_inventory": prior["text_inventory"],
        "source_bound_records_pg4_pg12": {"definitions": prior["source_bound_records_pg4_pg11"]["definitions"]+len(g.pg12_rules),
            "distinct_count": len(sutras), "distinct_ids": sorted(sutras)},
        "complete_lat_profile": {"root_entries": len(all_ids), "root_entry_denominator": old["root_entry_denominator"],
            "root_entries_pending": old["root_entry_denominator"]-len(all_ids), "root_ids": sorted(all_ids), "new_root_ids": sorted(g.pg12_ids),
            "cells": old["cells"]+cmp["cells"], "paradigms": old["paradigms"]+cmp["paradigms"], "branches": old["branches"]+cmp["branches"],
            "prior_report": "../lexical_present/COVERAGE_STATUS.json", "prior_evidence": "frozen PG11 coverage read; no predecessor suite or certificate replay"},
        "new_groups": groups, **classes, "class2": prior["class2"], "class3": prior["class3"], "class7": prior["class7"],
        "literal_commentary_word_evidence": {"witnesses": sum(witnesses["literal_word_witnesses_by_root"].values()),
            "roots_with_literal_words": len(witnesses["literal_word_witnesses_by_root"]), "no_separate_word_witness_ids": witnesses["no_separate_word_witness_ids"],
            "inherited_pg10_pg11_witness_gaps": old_gaps,
            "boundary": "New entries without exact full-word witnesses have lexical/rule evidence and comparison cells; these are not relabeled as literal word evidence. Earlier seven gaps stay open."},
        "source_adjudications": len(load(HERE/'SOURCE_ADJUDICATIONS.json')["decisions"]),
        "selected_pvadi_reading": "explicit named subdivision ending at plī; later members of the broad reading are not silently included",
        "companion_nominal_outputs": prior["companion_nominal_outputs"], "full_grammar_and_native_operator_lift": "OPEN"}


def build(source_root):
    packets = {n: load(HERE/n) for n in ["RULE_RECORDS.json", "LEXICAL_ENTRIES.json", "REFERENCE_CASES.json", "SOURCE_ADJUDICATIONS.json"]}
    sources = check_sources(packets, load(HERE/'SOURCE_PINS.json'), source_root)
    records = load(source_root/'sutraani/data.txt')["data"]; roots = load(source_root/'dhatu/data.txt')["data"]
    original = digest([records, roots]); g = Grammar(records, roots); cases = []
    for c in packets["REFERENCE_CASES.json"]["cases"]:
        v = g.derive(request(c["request"]))
        expected = sorted({iast(w) for w in c["attested_forms"]}) if c["kind"] == "attested_member" else c["expected_status"]
        actual = v.get("forms", v["status"])
        ok = v["status"] == COMPLETE and set(expected) <= set(actual) if c["kind"] == "attested_member" else v["status"] == expected
        cases.append({"id": c["id"], "kind": c["kind"], "actual": actual, "expected": expected, "agrees": ok})
    checks = controls(g, records, roots)
    checks.append({"id": "source-inputs-unchanged", "agrees": digest([records, roots]) == original})
    cmp = comparison(g, load(source_root/'dhatu/dhatuforms_vidyut_shuddha_kartari.txt'))
    checks += [{"id": "all-branches:"+k, "agrees": v} for k,v in cmp["all_branch_invariants"].items()]
    cov = coverage(g, cmp, roots, packets["REFERENCE_CASES.json"])
    failures = [r["id"] for r in cases+checks if not r["agrees"]] + ["comparison:"+r["id"] for r in cmp["differences"]]
    report = {"schema": "rkf.panini.pg12.v1", "author": "Monty", "status": "FAIL_BOUNDED_PG12_CONTRACTS" if failures else "PASS_BOUNDED_PG12_CONTRACTS",
        "sources": sources, "case_counts": dict(Counter(c["kind"] for c in cases)), "cases": cases, "direct_controls": checks, "failures": failures,
        "implementation_comparison": cmp, "coverage_sha256": digest(cov), "source_bound_records": len(g.pg12_rules),
        "implementation_sha256": {n: file_digest(HERE/n) for n in ["grammar.py", "scope.py", "verify.py", "cli.py"]},
        "claim_boundary": {"raw_sanskrit_interpreter": False, "all_lakaras": False, "all_textual_readings": False,
                           "general_nati_or_visibility_solver": False, "soundness_oracle": False, "native_operator_theorem": False}}
    return report, cov


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True); parser.add_argument('--write', action='store_true')
    args = parser.parse_args(); report,cov = build(args.source_root)
    for name,value in [('VERIFICATION_RESULT.json', report), ('COVERAGE_STATUS.json', cov)]:
        text = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True)+'\n'; target = HERE/name
        if args.write: target.write_text(text, encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8') != text: raise SystemExit('PG12 report differs: '+name)
    print(json.dumps({'status': report['status'], 'sources': report['sources'], 'cases': report['case_counts'],
        'controls': len(report['direct_controls']), 'failures': report['failures'], 'comparison_cells': report['implementation_comparison']['cells'],
        'comparison_branches': report['implementation_comparison']['branches'], 'comparison_differences': len(report['implementation_comparison']['differences']),
        'combined_coverage': {k:v for k,v in cov['complete_lat_profile'].items() if k not in ['root_ids', 'new_root_ids']}}, indent=2))
    return int(bool(report['failures']))


if __name__ == '__main__':
    raise SystemExit(main())
