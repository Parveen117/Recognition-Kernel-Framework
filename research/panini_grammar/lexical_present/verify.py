"""Direct PG11 source, occurrence, ownership and lexical-branch checks."""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path

from research.panini_grammar.lexical_present.grammar import Grammar, Request, ordered, sounds, root_and_following
from research.panini_grammar.root_progression.verify import check_sources, digest, file_digest, load
from research.panini_grammar.vikarana_lat.verify import request, iast

HERE=Path(__file__).resolve().parent
COMPLETE="COMPLETE_IN_REVIEWED_LEXICAL_PRESENT_DOMAIN"


def controls(g,records,roots):
    rows=[]
    def check(name,value):rows.append({"id":name,"agrees":bool(value)})
    def req(id="1020039",**kw):
        pf=g.entries[id]["profiles"][0]
        return replace(Request(id,pf["sense"],pf["pada"],"prathama","eka",True),**kw)
    def value(id="1020039",**kw):return g.derive(req(id,**kw))
    def branch(id="1020039",form=None,**kw):
        bs=value(id,**kw)["branches"]
        return bs[0] if form is None else next(b for b in bs if b["form"]==form)
    def raw(id="1020039",**kw):
        r=req(id,**kw);s=g.plan(r)["branches"][0];s["pg11_options"]=[];g._prepare11(s);return s,r
    def ended(id="1020039",**kw):
        s,r=raw(id,**kw);g._ending11(s,r);return s
    def events(b,phase="pre_tripadi"):return b[phase]["history"]
    def fails(call):
        try:call()
        except (ValueError,KeyError):return True
        return False
    r=deepcopy(next(r for r in g.pg11["records"] if r["sid"]=="3.4.84"))
    bru=[t for t in r["terms"] if t["term"]=="ब्रुवः"]
    check("two-bruvah-occurrences-have-distinct-cases",[t["case"] for t in bru]==["5","6"] and bru[0]["occurrence_uid"]!=bru[1]["occurrence_uid"])
    bru[0].pop("occurrence_uid")
    check("homograph-without-occurrence-is-refused",g.pg11_scope.compile(r)["status"]=="UNRESOLVED_RECORD")
    r=deepcopy(next(r for r in g.pg11["records"] if r["sid"]=="3.4.84"));r["terms"][0]["case"]="6"
    check("ablative-cannot-be-rebound-as-genitive",g.pg11_scope.compile(r)["status"]=="UNRESOLVED_RECORD")
    r=deepcopy(next(r for r in g.pg11["records"] if r["sid"]=="3.4.84"));r["terms"]=[t for t in r["terms"] if t["term"]!="वा"]
    check("optional-inheritance-must-be-bound",g.pg11_scope.compile(r)["status"]=="UNRESOLVED_RECORD")
    r=deepcopy(next(r for r in g.pg11["records"] if r["sid"]=="7.2.78"));r["terms"]=[t for t in r["terms"] if t["term"]!="ईशः"]
    check("is-extension-must-be-bound",g.pg11_scope.compile(r)["status"]=="UNRESOLVED_RECORD")
    changed=deepcopy(records);row=next(r for r in changed if r["i"]=="72076");row["an"]=row["an"].replace('##वलादेः$72035','')
    check("source-val-condition-cannot-disappear",fails(lambda:Grammar(changed,roots)))
    changed=deepcopy(records);next(r for r in changed if r["i"]=="82035")["s"]="आहस्धः"
    check("ah-dental-th-wording-is-pinned",fails(lambda:Grammar(changed,roots)))
    changed=deepcopy(roots);next(r for r in changed if r["i"]=="1030017")["tags"]="अनुदात्तोपदेशः"
    check("r-vedic-source-tag-cannot-be-erased",fails(lambda:Grammar(records,changed)))
    changed=deepcopy(roots);next(r for r in changed if r["i"]=="1020007")["dhatu_note"]="corrected silently"
    check("conflicting-caks-note-cannot-be-erased",fails(lambda:Grammar(records,changed)))
    b=branch("1020007");s=b["pre_tripadi"];r=s["morphemes"][0]
    check("caks-raw-preprocessing-remains-visible-in-memory",s["root_preprocessing"]["visible"][-1]["symbol"]=="i" and sounds(r)==["c","a","k","ṣ"])
    marker=r["pg11_marker_evidence"]
    check("caks-nonfinal-marker-keeps-source-uid",any(e["rule"]=="1.3.9" and e["before"][0]["uid"]==marker["source_uid"] for e in events(b)))
    check("caks-nonfinal-i-does-not-license-num",marker["final_idit"] is False and any(e["rule"]=="7.1.58" for e in s["blocked"]))
    check("caks-cluster-lopa-has-root-owner",any(e["rule"]=="8.2.29" and e["target"]["owner"]==r["id"] for e in events(b,"readout")))
    check("caks-vowel-ending-keeps-k",branch("1020007",number="dvi")["form"]=="cakṣāte")
    s,rq=raw("1020039");g._ending_substitution(s,0,"3.4.84")
    check("bru-substitution-is-coupled",sounds(s["morphemes"][0])==["ā","h"] and sounds(s["morphemes"][-1])==["a"] and s["ah_substitution"]["coupled_ending"]==s["morphemes"][-1]["identity"])
    check("substitution-retains-original-root-teaching",s["morphemes"][0]["teaching"]==g.entries["1020039"]["aupadeshik"])
    check("ending-substitution-cannot-repeat",fails(lambda:g._ending_substitution(s,0,"3.4.84")))
    s,_=raw("1020039")
    check("wrong-person-number-slot-is-refused",fails(lambda:g._ending_substitution(s,3,"3.4.84")))
    s,_=raw("1020039",person="madhyama",number="bahu")
    check("bru-sixth-ending-has-no-ah-option",fails(lambda:g._ending_substitution(s,5,"3.4.84")))
    s,_=raw("1020039",pada="A")
    check("bru-A-cannot-borrow-P-substitution",fails(lambda:g._ending_substitution(s,0,"3.4.84")))
    s,_=raw("1020058")
    check("vac-cannot-borrow-vid-ending-option",fails(lambda:g._ending_substitution(s,0,"3.4.83")))
    b=branch("1020059",form="veda");s=b["pre_tripadi"];ting=s["morphemes"][-1]
    check("vid-substitution-does-not-create-perfect",s["request"]["tense"]=="present" and s["lakara"]["identity"]=="laṭ:3.2.123")
    check("nal-markers-retained-separately",set(ting["substitute_marker_labels"])=={"ṇ","l"} and sounds(ting)==["a"])
    check("nal-retains-tip-pit-for-this-lat-domain",ting["features"]["pit"] and ting["features"]==ting["substituted_ending"]["features"] and ting["substituted_ending"]["identity"]=="tip:3.4.78")
    check("vid-weak-substitute-keeps-ngitvat",branch("1020059",form="vidatuḥ",number="dvi")["pre_tripadi"]["morphemes"][-1]["features"]["ngitvat"])
    check("vid-uttama-number-options-retained",value("1020059",person="uttama",number="dvi")["forms"]==["vidva","vidvaḥ"])
    check("bru-fifth-ending-has-two-branches",len(value("1020039",person="madhyama",number="dvi")["branches"])==2)
    check("bru-sixth-and-uttama-have-one-branch",len(value("1020039",person="madhyama",number="bahu")["branches"])==len(value("1020039",person="uttama")["branches"])==1)
    b=branch("1020039",form="āttha",person="madhyama");s=b["pre_tripadi"]
    check("ah-branch-excludes-sthanivad-iit",not s.get("augmented_ending") and any(e["rule"]=="7.3.93" and e["by"]=="8.2.35" for e in s["blocked"]))
    order=[e["rule"] for e in events(b,"readout")]
    check("ah-dental-th-precedes-devoicing",order.index("8.2.35")<order.index("8.4.55") and "8.2.40" not in order)
    s=ended("1020062",number="dvi")
    check("rudadi-it-admits-apit",not s["morphemes"][-1]["features"]["pit"] and g._augment_request(s)==("it","7.2.76"))
    s2=deepcopy(s);s2["morphemes"][-1]["visible"][0]["symbol"]="y"
    check("rudadi-val-excludes-y",g._augment_request(s2) is None)
    for feature in ["ting","sarvadhatuka"]:
        bad=deepcopy(s);bad["morphemes"][-1]["features"][feature]=False
        check("augment-requires-"+feature,g._augment_request(bad) is None)
    check("rudadi-vowel-ending-has-no-it",g._augment_request(ended("1020062",number="bahu")) is None)
    check("sixth-root-jagr-cannot-borrow-rudadi-it",g._augment_request(ended("1020067")) is None)
    check("it-is-inserted",g._augment11(s))
    augment=s["morphemes"][2]
    check("it-belongs-to-ending-not-root",augment["host"]=="ting" and s["augmented_ending"]["members"]==["augment:it","ting"] and root_and_following(s)[1] is augment)
    check("it-marker-memory-survives",[x["symbol"] for x in augment["original"]]==["i","ṭ"] and sounds(augment)==["i"])
    check("it-cannot-repeat",g._augment11(s) is False)
    bad=deepcopy(s);bad["morphemes"][2]["host"]="root:1020062"
    check("wrong-it-host-is-refused",fails(lambda:ordered(bad)))
    bad=deepcopy(s);bad["augmented_ending"]["members"].reverse()
    check("reversed-tit-placement-is-refused",fails(lambda:ordered(bad)))
    s=ended("1020039");check("bru-pit-admits-mandatory-iit",g._augment_request(s)==("iit","7.3.93"))
    s["morphemes"][-1]["features"]["pit"]=False
    check("bru-iit-requires-pit",g._augment_request(s) is None)
    b=branch("1020039",form="bravīti");order=[e["rule"] for e in events(b)]
    check("bru-iit-before-guna-before-ayadi",order.index("7.3.93")<order.index("7.3.84")<order.index("6.1.78"))
    check("bru-A-retains-long-root-u",value("1020039",pada="A")["forms"]==["brūte"])
    for id in ["1020009","1020010"]:
        check("id-is-dhve-it:"+id,g._augment_request(ended(id,person="madhyama",number="bahu"))==("it","7.2.78"))
    check("is-se-has-specific-prescription",g._augment_request(ended("1020010",person="madhyama"))==("it","7.2.77"))
    s,_=raw("1020026",number="bahu")
    check("rut-cannot-precede-jh-substitution",g._augment_request(s) is None)
    s=ended("1020026",number="bahu");g._augment11(s)
    check("rut-host-is-at-component",s["morphemes"][2]["host"]=="ting:jh-substitute" and s["jh_substitute"]["parent"]=="ting")
    check("rut-u-is-pronunciation-memory-not-it",[x["symbol"] for x in s["morphemes"][2]["original"]]==["r","u","ṭ"] and sounds(s["morphemes"][2])==["r"] and [x["label"] for x in s["morphemes"][2]["marker_evidence"]["marker_units"]]==["ṭ"])
    bad=deepcopy(s);bad["morphemes"][2]["host"]="ting"
    check("rut-cannot-lose-component-host",fails(lambda:ordered(bad)))
    bad=deepcopy(s);bad["jh_substitute"]["uids"].reverse()
    check("rut-requires-actual-at-identity",fails(lambda:ordered(bad)))
    b=branch("1020026",number="bahu");order=[e["rule"] for e in events(b)]
    check("si-jh-substitution-before-rut",b["form"]=="śerate" and order.index("7.1.5")<order.index("7.1.6"))
    check("si-guna-does-not-fake-a-strong-ending",b["pre_tripadi"]["morphemes"][-1]["features"]["ngitvat"] and any(e["rule"]=="1.1.5" and e["by"]=="7.4.21" for e in b["pre_tripadi"]["blocked"]))
    check("si-vowel-junction-remains-separate",branch("1020026",number="dvi")["form"]=="śayāte")
    b=branch("1020002",number="dvi")
    check("han-jhal-lopa-targets-n",b["form"]=="hataḥ" and any(e["rule"]=="6.4.37" and e["before"][0]["symbol"]=="n" for e in events(b)))
    b=branch("1020002",number="bahu");order=[e["rule"] for e in events(b)]
    check("han-vowel-lopa-before-h-to-gh",b["form"]=="ghnanti" and order.index("6.4.98")<order.index("7.3.54"))
    check("han-sonorant-ending-keeps-n",branch("1020002",person="uttama",number="dvi")["form"]=="hanvaḥ")
    check("han-strong-s-does-not-borrow-weak-n-lopa",branch("1020002",person="madhyama")["form"]=="haṃsi")
    for id in [str(1020000+i) for i in range(66,71)]:
        b=branch(id,number="bahu");s=b["pre_tripadi"]
        check("lexical-abhyasta-is-not-copy:"+id,s["lexical_abhyasta"]["members"]==[s["morphemes"][0]["id"]] and all(u["kind"]!="abhyasa" for u in s["morphemes"]) and any(e["rule"]=="7.1.4" for e in events(b)))
    check("daridra-weak-hal-i-and-vowel-lopa",value("1020068",number="dvi")["forms"]==["daridritaḥ"] and value("1020068",number="bahu")["forms"]==["daridrati"])
    b=branch("1020070",person="uttama",number="dvi")
    check("sas-root-satva-has-root-owner",b["form"]=="śiṣvaḥ" and any(e["rule"]=="8.3.60" and e["before"]["owner"]=="root:1020070" for e in events(b,"readout")))
    check("sas-vowel-ending-excludes-upadha-i",value("1020070",number="bahu")["forms"]==["śāsati"])
    check("mrj-weak-vowel-keeps-both-options",value("1020061",number="bahu")["forms"]==["mārjanti","mṛjanti"])
    check("mrj-weak-hal-excludes-vrddhi",value("1020061",number="dvi")["forms"]==["mṛṣṭaḥ"])
    b=branch("1020061")
    check("mrj-satva-overrides-generic-j-kutva",any(e["rule"]=="8.2.30" and e["by"]=="8.2.36" for e in b["readout"]["blocked"]))
    b=branch("1020004",person="madhyama");order=[e["rule"] for e in events(b,"readout")]
    check("duh-gh-before-bhas",b["form"]=="dhokṣi" and order.index("8.2.32")<order.index("8.2.37"))
    check("duh-t-ending-excludes-bhas",not any(e["rule"]=="8.2.37" for e in events(branch("1020004"),"readout")))
    check("dih-dhve-admits-bhas",branch("1020005",pada="A",person="madhyama",number="bahu")["form"]=="dhigdhve")
    b=branch("1020006",number="dvi");order=[e["rule"] for e in events(b,"readout")]
    check("lih-local-visibility-and-length-order",b["form"]=="līḍhaḥ" and order.index("8.4.41")<order.index("8.3.13")<order.index("6.3.111"))
    check("lih-lengthening-preserves-root-owner",next(e for e in events(b,"readout") if e["rule"]=="6.3.111")["before"]["owner"]=="root:1020006")
    check("lih-strong-e-is-not-lengthened",not any(e["rule"]=="6.3.111" for e in events(branch("1020006"),"readout")))
    prior=g.pg11;g.pg11=deepcopy(prior)
    next(e for e in g.pg11["visibility_exceptions"] if e.get("query")=="8.3.13")["visible_rule"]="8.4.40"
    try:check("lih-without-local-permission-is-refused",fails(lambda:g._readout11(b["pre_tripadi"])))
    finally:g.pg11=prior
    check("num-and-non-num-vrj-remain-distinct",value("1020022")["forms"]==["vṛkte"] and value("1020023")["forms"]==["vṛṅkte"])
    check("in-yan-differs-from-vi-iyang",value("1020040",number="bahu")["forms"]==["yanti"] and value("1020043",number="bahu")["forms"]==["viyanti"])
    b=branch("1030017",number="bahu");s=b["pre_tripadi"];copy,root,vik,ting=s["morphemes"]
    check("r-keeps-tag-and-classical-license","छान्दसः" in s["lexical_register_evidence"]["source_tags"] and s["lexical_register_evidence"]["requested_register"]=="classical")
    check("r-copy-retains-root-source-identity",copy["original"][0]["copied_from"]==root["original"][0]["uid"] and copy["original"][0]["symbol"]=="ṛ")
    h=events(b);rapara=next(e for e in h if e["rule"]=="1.1.51");lopa=next(e for e in h if e["effect"]=="vowel_initial_copy_consonant_lopa")
    check("r-generated-rapara-survives-in-deletion-history",rapara["result"][-1]["uid"]==lopa["before"][0]["uid"] and lopa["target_morpheme"]==copy["id"])
    order=[e["rule"] for e in h]
    check("copy-iy-precedes-root-yan",b["form"]=="iyrati" and order.index("6.4.78")<order.index("6.1.77"))
    check("r-copy-cannot-repeat",fails(lambda:g._copy_r(s)))
    bad,_=raw("1030017");bad["morphemes"][1]["whole_affix_deletion"]["kind"]="luk"
    check("r-copy-requires-slu",fails(lambda:g._copy_r(bad)))
    bad,_=raw("1030017");bad["morphemes"][0]["visible"].append(deepcopy(bad["morphemes"][0]["visible"][0]))
    check("r-copy-rejects-unreviewed-multiple-vowel-span",fails(lambda:g._copy_r(bad)))
    check("r-strong-and-weak-remain-distinct",value("1030017")["forms"]==["iyarti"] and value("1030017",number="dvi")["forms"]==["iyṛtaḥ"])
    before=digest(s);views=g._readout11(s)
    check("readout-does-not-mutate-source",digest(s)==before)
    check("readout-is-repeatable",views==g._readout11(s))
    check("readout-cannot-feed-back",fails(lambda:g._readout11(views[0])))
    views[0]["visible"][0]["symbol"]="client-change"
    check("readout-has-no-source-alias",digest(s)==before)
    check("untyped-request-is-refused",g.derive({})["status"]=="UNRESOLVED")
    for id,pada,word in [("1020028","P","rauti"),("1030003","P","jihreti"),("1030004","P","piparti"),("1030011","A","dhatte"),("1070001","P","ruṇaddhi"),("1010001","P","bhavati")]:
        r=Request(id,g.entries[id]["artha"],pada,"prathama","eka",True)
        check("unchanged-dispatch:"+id,word in g.derive(r).get("forms",[]))
    return rows


def comparison(g,table):
    rows=[];invariants={k:True for k in ["resolved_obligations","unique_visible_uids","owned_ending_augments",
        "retained_ending_sources","lexical_abhyasta_without_fake_copy","branch_forms_equal_reported_forms"]}
    for id in sorted(g.pg11_ids):
        e=g.entries[id]
        for pf in e["profiles"]:
            cells=table[e["baseindex"]][pf["pada"].lower()+"lat"].split(";")
            if len(cells)!=9:raise ValueError("Nine comparison cells are required")
            for i,cell in enumerate(cells):
                r=Request(id,pf["sense"],pf["pada"],g.review["ending_order"]["persons"][i//3],g.review["ending_order"]["numbers"][i%3],True)
                v=g.derive(r);expected=sorted({iast(w) for w in cell.split(",")})
                invariants["branch_forms_equal_reported_forms"] &= sorted({b["form"] for b in v["branches"]})==v["forms"]
                for b in v["branches"]:
                    s=b["pre_tripadi"];seq=ordered(s)
                    invariants["resolved_obligations"] &= not s["open_obligations"]
                    invariants["unique_visible_uids"] &= len({x["uid"] for x in seq})==len(seq)
                    for u in s["morphemes"]:
                        if u["kind"]=="augment":invariants["owned_ending_augments"] &= u["host"] in {"ting","ting:jh-substitute"} and s["augmented_ending"]["members"]==[u["id"],"ting"]
                    if s.get("ending_substitution"):
                        t=s["morphemes"][-1]
                        invariants["retained_ending_sources"] &= t["features"]==t["substituted_ending"]["features"] and s["request"]["tense"]=="present"
                    if s.get("lexical_abhyasta"):
                        invariants["lexical_abhyasta_without_fake_copy"] &= all(u["kind"]!="abhyasa" for u in s["morphemes"])
                rows.append({"id":f"{id}:{pf['pada']}:{i}","group":e["group"],"actual":v["forms"],"expected":expected,
                    "agrees":v["status"]==COMPLETE and v["forms"]==expected,"branches":len(v["branches"]),"history_sha256":digest(v["branches"])})
    return {"status":"PINNED_IMPLEMENTATION_COMPARISON_NOT_SOUNDNESS_ORACLE","lexemes":len(g.pg11_ids),"paradigms":len(rows)//9,
        "cells":len(rows),"branches":sum(r["branches"] for r in rows),"differences":[r for r in rows if not r["agrees"]],"rows":rows,"all_branch_invariants":invariants}


def coverage(g,cmp,roots,witnesses):
    prior=load(HERE.parent/'present_expansion/COVERAGE_STATUS.json');old=prior["complete_lat_profile"]
    old_ids=set(old["root_ids"])
    if old_ids & g.pg11_ids:raise ValueError("PG11 overlaps already counted roots")
    ids=set(prior["source_bound_records_pg4_pg10"]["distinct_ids"])|set(g.pg11_rules);all_ids=old_ids|g.pg11_ids
    source={r["i"]:r for r in roots};groups={}
    for group in ["extended_adadi","vowel_initial_juhotyadi"]:
        members={id for id in g.pg11_ids if g.entries[id]["group"]==group};rows=[r for r in cmp["rows"] if r["group"]==group]
        groups[group]={"root_ids":sorted(members),"root_entries":len(members),"cells":len(rows),"paradigms":len(rows)//9,"branches":sum(r["branches"] for r in rows)}
    return {"author":"Monty","overall_grammar_completion_percent":None,"text_inventory":prior["text_inventory"],
        "source_bound_records_pg4_pg11":{"definitions":prior["source_bound_records_pg4_pg10"]["definitions"]+len(g.pg11_rules),"distinct_count":len(ids),"distinct_ids":sorted(ids)},
        "complete_lat_profile":{"root_entries":len(all_ids),"root_entry_denominator":old["root_entry_denominator"],"root_entries_pending":old["root_entry_denominator"]-len(all_ids),
            "root_ids":sorted(all_ids),"new_root_ids":sorted(g.pg11_ids),"cells":old["cells"]+cmp["cells"],"paradigms":old["paradigms"]+cmp["paradigms"],"branches":old["branches"]+cmp["branches"],
            "prior_report":"../present_expansion/COVERAGE_STATUS.json","prior_evidence":"frozen PG10 report read; no predecessor suite or certificate replay"},
        "new_groups":groups,"class2":{"complete_root_entries":sum(source[id]["gana"]=="2" for id in all_ids),"source_lexical_rows":76,"source_rows":77,
            "remaining_prefix_context_ids":["1020012","1020041","1020042"],"remaining_vedic_ids":[str(1020000+i) for i in range(71,76)]},
        "class3":{"complete_root_entries":sum(source[id]["gana"]=="3" for id in all_ids),"source_rows":26,"unmarked_entries_covered":14,"tagged_rows_unadmitted":11,
            "classical_use_exception":"1030017 ṛ: source tag retained; explicit Siddhāntakaumudī classical-use license; only the sole-vowel copying profile is admitted"},
        "class7":prior["class7"],"literal_commentary_word_evidence":{"witnesses":sum(witnesses["literal_word_witnesses_by_root"].values()),"roots_with_literal_words":len(witnesses["literal_word_witnesses_by_root"]),
            "no_separate_word_witness_ids":witnesses["no_separate_word_witness_ids"],"inherited_pg10_witness_gaps":prior["literal_commentary_word_evidence"]["no_separate_word_witness_ids"],
            "boundary":"New pṛj has lexical/rule evidence and nine comparison cells, but no separate exact full-word witness in the selected passages. The six PG10 word-evidence gaps remain open."},
        "source_adjudications":len(load(HERE/'SOURCE_ADJUDICATIONS.json')["decisions"]),"companion_nominal_outputs":"Separate domains; not counted as present verb cells.","full_grammar_and_native_operator_lift":"OPEN"}


def build(source_root):
    packets={n:load(HERE/n) for n in ["RULE_RECORDS.json","LEXICAL_ENTRIES.json","REFERENCE_CASES.json","SOURCE_ADJUDICATIONS.json"]}
    sources=check_sources(packets,load(HERE/'SOURCE_PINS.json'),source_root)
    records=load(source_root/'sutraani/data.txt')["data"];roots=load(source_root/'dhatu/data.txt')["data"]
    original=digest([records,roots]);g=Grammar(records,roots);cases=[]
    for c in packets["REFERENCE_CASES.json"]["cases"]:
        v=g.derive(request(c["request"]))
        expected=sorted({iast(w) for w in c["attested_forms"]}) if c["kind"]=="attested_member" else c["expected_status"]
        actual=v.get("forms",v["status"])
        ok=v["status"]==COMPLETE and set(expected)<=set(actual) if c["kind"]=="attested_member" else v["status"]==expected
        cases.append({"id":c["id"],"kind":c["kind"],"actual":actual,"expected":expected,"agrees":ok})
    checks=controls(g,records,roots)
    checks.append({"id":"source-inputs-unchanged","agrees":digest([records,roots])==original})
    cmp=comparison(g,load(source_root/'dhatu/dhatuforms_vidyut_shuddha_kartari.txt'))
    checks += [{"id":"all-branches:"+k,"agrees":v} for k,v in cmp["all_branch_invariants"].items()]
    cov=coverage(g,cmp,roots,packets["REFERENCE_CASES.json"])
    failures=[r["id"] for r in cases+checks if not r["agrees"]]+["comparison:"+r["id"] for r in cmp["differences"]]
    report={"schema":"rkf.panini.pg11.v1","author":"Monty","status":"FAIL_BOUNDED_PG11_CONTRACTS" if failures else "PASS_BOUNDED_PG11_CONTRACTS",
        "sources":sources,"case_counts":dict(Counter(c["kind"] for c in cases)),"cases":cases,"direct_controls":checks,"failures":failures,
        "implementation_comparison":cmp,"coverage_sha256":digest(cov),"source_bound_records":len(g.pg11_rules),
        "implementation_sha256":{name:file_digest(HERE/name) for name in ["grammar.py","scope.py","verify.py","cli.py"]},
        "claim_boundary":{"raw_sanskrit_interpreter":False,"general_reduplicator":False,"general_asiddha_solver":False,"all_lakaras":False,"soundness_oracle":False,"native_operator_theorem":False}}
    return report,cov


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--source-root',type=Path,required=True);parser.add_argument('--write',action='store_true');args=parser.parse_args()
    report,cov=build(args.source_root)
    for name,value in [('VERIFICATION_RESULT.json',report),('COVERAGE_STATUS.json',cov)]:
        text=json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True)+'\n';target=HERE/name
        if args.write:target.write_text(text,encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8')!=text:raise SystemExit('PG11 report differs: '+name)
    print(json.dumps({'status':report['status'],'sources':report['sources'],'cases':report['case_counts'],'controls':len(report['direct_controls']),
        'failures':report['failures'],'comparison_cells':report['implementation_comparison']['cells'],'comparison_branches':report['implementation_comparison']['branches'],
        'comparison_differences':len(report['implementation_comparison']['differences']),
        'combined_coverage':{k:v for k,v in cov['complete_lat_profile'].items() if k not in ['root_ids','new_root_ids']}},indent=2))
    return int(bool(report['failures']))


if __name__=='__main__':raise SystemExit(main())
