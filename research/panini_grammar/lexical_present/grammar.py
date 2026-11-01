"""PG11: lexical present exceptions with owned augments and substitutions.

This finite linguistic adapter reads no expected forms or conjugator table.
The native operator-family construction remains a separate open obligation.
"""
from copy import deepcopy
import json
from pathlib import Path

from research.panini_grammar.present_expansion.grammar import Grammar as PG10Grammar, Request, VOWELS, sounds, unresolved, root_and_following
from research.panini_grammar.lexical_present.scope import ReviewedScope
from research.panini_grammar.verification.marker_review import designate, tokenize
from research.panini_grammar.snam_lat.grammar import local_nati, collapse_targets

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def ordered(state):
    units = state["morphemes"]
    copied = units[0]["kind"] == "abhyasa"
    root_index = int(copied)
    root, vik, ting = units[root_index], units[root_index + 1], units[-1]
    if root["kind"] != "root" or root["identity"] != state["request"]["lexical_id"] or ting["id"] != "ting":
        raise ValueError("PG11 root and ending ownership changed")
    expected = {"kind": "ślu", "rule": "2.4.75"} if copied else {"kind": "luk", "rule": "2.4.72"}
    if vik["id"] != "vikarana" or vik["visible"] or vik.get("whole_affix_deletion") != expected:
        raise ValueError("The original deleted śap identity must remain")
    if copied:
        if root["identity"] != "1030017" or state.get("abhyasta", {}).get("members") != [units[0]["id"], root["id"]]:
            raise ValueError("The owned ṛ copy must remain distinct from its root")
    if state.get("lexical_abhyasta"):
        designation = state["lexical_abhyasta"]
        if (copied or root["identity"] not in {str(1020000+i) for i in range(66,71)}
                or designation.get("members") != [root["id"]] or designation.get("physical_copy") is not False):
            raise ValueError("Lexical abhyasta is a designation, not a fabricated copy")
    middle = units[root_index+2:-1]
    if len(middle) > 1:
        raise ValueError("Only one reviewed ending augment is admitted")
    if middle:
        augment = middle[0]
        host = "ting:jh-substitute" if augment["id"] == "augment:rut" else "ting"
        if (augment["id"] not in {"augment:it", "augment:iit", "augment:rut"}
                or augment["kind"] != "augment" or augment.get("host") != host
                or not augment["features"].get("tit")
                or state.get("augmented_ending", {}).get("members") != [augment["id"], "ting"]):
            raise ValueError("An augment lost its initial ending membership")
        if host == "ting:jh-substitute":
            component = state.get("jh_substitute", {})
            if (component.get("id") != host or component.get("parent") != "ting"
                    or component.get("uids") != [s["uid"] for s in ting["visible"][:2]]
                    or sounds(ting) != ["a", "t", "e"]):
                raise ValueError("Ruṭ must belong to the actual jh-to-at substitute")
    elif state.get("augmented_ending"):
        raise ValueError("The ending constituent has lost its augment")
    out = [{**deepcopy(s), "owner": unit["id"]} for unit in units for s in unit["visible"]]
    if len({s["uid"] for s in out}) != len(out):
        raise ValueError("Visible sound identities are not unique")
    return out


class Grammar(PG10Grammar):
    def __init__(self, records, roots, review=None):
        super().__init__(records, roots)
        self.pg11 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.pg11_scope = ReviewedScope(records, self.review["scope_policies"], self.pg6["scope_policies"],
            self.pg7["scope_policies"], self.pg9["scope_policies"], self.pg10["scope_policies"], self.pg11["scope_policies"])
        self.pg11_rules = {r["sid"]: self.pg11_scope.compile(r) for r in self.pg11["records"]}
        if len(self.pg11_rules) != len(self.pg11["records"]) or any(r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg11_rules.values()):
            raise ValueError("PG11 source occurrence or grammatical case is unbound")
        if any(r["sanskrit"] != self.pg11_scope.frame(r["sid"])["text"] for r in self.pg11["records"]):
            raise ValueError("PG11 Sanskrit wording changed")
        additions = load("LEXICAL_ENTRIES.json")["entries"]
        self.pg11_ids = {e["id"] for e in additions}
        if len(self.pg11_ids) != len(additions):
            raise ValueError("Duplicate PG11 lexical identity")
        source = {r["i"]: r for r in roots}
        for entry in additions:
            keys = ["baseindex", "aupadeshik", "gana", "pada", "artha", "tags"]
            if "dhatu_note" in entry:
                keys.append("dhatu_note")
            if any(entry[k] != source[entry["id"]][k] for k in keys):
                raise ValueError("PG11 source identity, register or conflicting note changed")
            self.entries[entry["id"]] = deepcopy(entry)

    def _block11(self, state, winner, loser, **context):
        edges = [e for e in self.pg11["priority"] if (e["winner"],e["loser"]) == (winner,loser)]
        if len(edges) != 1:
            raise ValueError("PG11 local priority was not reviewed")
        state["blocked"].append({"rule": loser, "by": winner, "relation": deepcopy(edges[0]), **deepcopy(context)})

    def _prepare11(self, state):
        root = state["morphemes"][0]
        entry = self.entries[root["identity"]]
        if sounds(root) != entry.get("preprocessed_shape",entry["root_shape"]):
            raise ValueError("The inherited root no longer has its reviewed shape")
        if root["identity"] == "1020007":
            unit = deepcopy(root["visible"][-1])
            self._event(state,"1.3.2","commentary_supplied_nonfinal_i_marker",target=unit,
                lexical_id=root["identity"],source="Bālamanoramā/Tattvabodhinī 3.4.112",
                modern_pronunciation_only_note_retained=True,raw_nasality_inferred=False)
            root["pg11_marker_evidence"] = {"label":"i","source_uid":unit["uid"],"final_idit":False,
                                           "interpretation":"explicit traditional commentary"}
            self._replace(state,root,len(root["visible"])-1,1,[],"1.3.9","nonfinal_i_marker_lopa")
            state["blocked"].append({"rule":"7.1.58","reason":"the reviewed i marker is not final idit",
                                      "evidence":"अन्ते इदितः, Bālamanoramā/Tattvabodhinī 3.4.112"})
        if sounds(root) != entry["root_shape"]:
            raise ValueError("Reviewed root preparation failed")
        if root["identity"] == "1030017":
            state["lexical_register_evidence"] = {"source_tags":entry["tags"],"requested_register":"classical",
                "license":entry["classical_license"],"source":"Siddhāntakaumudī 7.3.87"}
            self._event(state,"lexicon:1030017","explicit_classical_use_despite_retained_tag",evidence=state["lexical_register_evidence"])
        if root["identity"] in self.pg11_rules["6.1.6"]["parameters"]["lexical_ids"]:
            state["lexical_abhyasta"] = {"id":"lexical-abhyasta:"+root["identity"],"members":[root["id"]],
                                         "physical_copy":False,"rule":"6.1.6"}
            self._event(state,"6.1.6","lexical_abhyasta_without_copy",designation=state["lexical_abhyasta"])

    def _copy_r(self, state):
        if state.get("abhyasta") or len(state["morphemes"]) != 3:
            raise ValueError("Ṛ copying requires an unprocessed ślu plan")
        root,vik,ting = state["morphemes"]
        if (root["identity"] != "1030017" or sounds(root) != ["ṛ"] or vik["visible"]
                or vik.get("whole_affix_deletion") != {"kind":"ślu","rule":"2.4.75"}):
            raise ValueError("Only the reviewed sole-vowel ṛ span can enter PG11 copying")
        copied = [{"uid":"abhyasa:1030017:copy:0","symbol":"ṛ","kind":"vowel",
                   "copied_from":root["visible"][0]["uid"],"introduced_by":"6.1.10"}]
        unit = {"id":"abhyasa:1030017","identity":"copy-of:"+root["id"],"kind":"abhyasa", "source_owner":root["id"],
                "original":deepcopy(copied),"visible":deepcopy(copied),"features":{"abhyasa":True,"pratyaya":False}}
        self._event(state,"6.1.10","copy_sole_vowel_root_span",source_span=root["visible"],copies=copied,
                    selector_rule="6.1.1",no_second_vowel_span_exists=True)
        state["morphemes"].insert(0,unit)
        self._event(state,"6.1.4","earlier_copy_is_abhyasa",owner=unit["id"])
        state["abhyasta"] = {"id":"abhyasta:1030017","members":[unit["id"],root["id"]],"collective":True,"rule":"6.1.5"}
        self._event(state,"6.1.5","both_occurrences_collectively_abhyasta",constituent=state["abhyasta"])
        self._r_substitute(state,unit,0,"i","7.4.77","arti_copy_i")
        self._block11(state,"7.4.77","7.4.66")
        self._replace(state,unit,1,1,[],"7.4.60","vowel_initial_copy_consonant_lopa")
        ordered(state)

    def _ending11(self, state, request):
        ting = state["morphemes"][-1]
        if state.get("lexical_abhyasta") or state.get("abhyasta"):
            for i in reversed([i for i,s in enumerate(sounds(ting)) if s == "jh"]):
                self._replace(state,ting,i,1,["a","t"],"7.1.4","abhyasta_jh_to_at",
                    preceding_constituent=state.get("lexical_abhyasta",state.get("abhyasta"))["id"])
                self._block11(state,"7.1.4","7.1.3")
            self._ending(state,ting,request)
        else:
            self._non_a_ending(state,ting,request)
        if request.lexical_id == "1020026" and request.person == "prathama" and request.number == "bahu":
            event = next(e for e in state["history"] if e["effect"] == "jh_to_at")
            state["jh_substitute"] = {"id":"ting:jh-substitute","parent":"ting","source":deepcopy(event["before"]),
                                      "uids":[s["uid"] for s in event["after"]],"rule":"7.1.5"}

    def _ending_substitution(self, state, index, rule):
        ting = state["morphemes"][-1]
        if state.get("ending_substitution"):
            raise ValueError("An ending cannot receive the terminal substitution twice")
        p = self.pg11_rules[rule]["parameters"]
        request_slot = (3*self.review["ending_order"]["persons"].index(state["request"]["person"])
                        +self.review["ending_order"]["numbers"].index(state["request"]["number"]))
        if (state["request"]["lexical_id"] != p["lexical_id"] or index not in p["slots"]
                or index != request_slot
                or state["request"]["pada"] != "P" or state["request"]["tense"] != "present"):
            raise ValueError("This lexical present ending substitution is not licensed")
        teaching = self.pg11_rules["3.4.82"]["parameters"]["teaching"][index]
        parsed = designate({"text":teaching,"identity":teaching+":"+rule,"upadesha":True,
            "category":"affix","nasality_complete":True,"vibhakti":True,"taddhita":False},self.markers)
        if parsed["status"] != "LOCAL_DESIGNATION":
            raise ValueError("The terminal ending teaching form did not parse")
        before = deepcopy(ting)
        original = [{**s,"uid":f"ting:substitute:{s['id']}"} for s in parsed["original"]]
        visible = [deepcopy(s) for s in original if s["id"] in parsed["visible_ids"]]
        if [s["symbol"] for s in visible] != self.pg11_rules["3.4.82"]["parameters"]["visible"][index]:
            raise ValueError("The reviewed ending marker convention changed")
        ting.update(identity=teaching+":"+rule,teaching=teaching,original=original,visible=visible,
                    marker_evidence=deepcopy(parsed),substituted_ending=before,
                    substitute_marker_labels=[m["label"] for m in parsed["marker_units"]])
        state["ending_substitution"] = {"rule":rule,"slot":index,"source_identity":before["identity"],"substitute_identity":ting["identity"]}
        self._event(state,rule,"optional_present_ending_substitution",source=before,substitute=deepcopy(ting),slot=index)
        self._event(state,"1.3.3/1.3.7/1.3.9","substitute_marker_designation_and_lopa",owner="ting",
                    markers=parsed["marker_units"],visible_uids=[s["uid"] for s in visible])
        self._event(state,"1.1.56","ending_substitute_retains_lat_features",source_features=before["features"],
                    retained_features=ting["features"],source_sounds_restored=False,does_not_create_lit=True)
        if rule == "3.4.84":
            root = state["morphemes"][0]
            self._replace(state,root,0,len(root["visible"]),["ā","h"],rule,"coupled_bru_to_ah",
                          paired_ending=ting["identity"],teaching_final_a_is_pronunciation_only=True)
            state["ah_substitution"] = {"rule":rule,"root_owner":root["id"],"coupled_ending":ting["identity"]}
            state["blocked"].append({"rule":"7.3.93","by":"8.2.35","reason":"source-reviewed jhal wording excludes inherited īṭ in āh",
                                      "source":"Siddhāntakaumudī 7.3.93"})

    def _ending_variants(self, state, request):
        slot = 3*self.review["ending_order"]["persons"].index(request.person)+self.review["ending_order"]["numbers"].index(request.number)
        rule = "3.4.83" if request.lexical_id == "1020059" else "3.4.84" if request.lexical_id == "1020039" and slot < 5 else None
        if rule and request.pada == "P":
            normal,alternate = deepcopy(state),deepcopy(state)
            self._event(normal,rule,"optional_ending_substitution_not_selected")
            self._ending11(normal,request)
            self._ending_substitution(alternate,slot,rule)
            normal["pg11_options"].append("regular-ending");alternate["pg11_options"].append("terminal-ending")
            return [normal,alternate]
        self._ending11(state,request)
        return [state]

    def _augment_request(self, state):
        root,following = root_and_following(state);ting=state["morphemes"][-1]
        if following is not ting or not ting["features"]["sarvadhatuka"] or not ting["features"]["ting"]:
            return None
        seq=sounds(ting);id=root["identity"]
        if id == "1020026" and state.get("jh_substitute"):
            return ("rut","7.1.6")
        if id in self.pg11_rules["7.2.76"]["parameters"]["lexical_ids"] and seq[0] not in VOWELS|{"y"}:
            return ("it","7.2.76")
        if id == "1020010" and seq == ["s","e"]:
            return ("it","7.2.77")
        if id in self.pg11_rules["7.2.78"]["parameters"]["lexical_ids"] and seq in [["s","e"],["dh","v","e"]]:
            return ("it","7.2.78")
        if id == "1020039" and not state.get("ah_substitution") and ting["features"]["pit"] and seq[0] not in VOWELS:
            return ("iit","7.3.93")
        return None

    def _augment11(self, state):
        choice = self._augment_request(state)
        if not choice:
            return False
        name,rule=choice
        teaching=self.pg11_rules[rule]["parameters"]["teaching"]
        original=[{"uid":f"augment:{name}:source:{i}","symbol":s.symbol,"kind":"vowel" if s.symbol in VOWELS else "consonant"}
                  for i,s in enumerate(tokenize(teaching))]
        expected={"it":["i","ṭ"],"iit":["ī","ṭ"],"rut":["r","u","ṭ"]}[name]
        if [s["symbol"] for s in original] != expected:
            raise ValueError("The ending augment's source teaching form changed")
        host="ting:jh-substitute" if name=="rut" else "ting"
        unit={"id":"augment:"+name,"identity":name+":"+rule,"kind":"augment","host":host,
              "teaching":teaching,"original":original,"visible":deepcopy(original[:1]),
              "features":{"tit":True,"pratyaya":False},
              "marker_evidence":{"marker_units":[{"label":"ṭ","uid":original[-1]["uid"],"rule":"1.3.3"}]}}
        self._event(state,rule,"mandatory_ending_augment",host=host,owner=unit["id"],original=original)
        self._event(state,"1.3.3","augment_final_t_it",target=original[-1])
        self._event(state,"1.3.9","augment_marker_lopa",removed=original[-1])
        if name=="rut":
            unit["pronunciation_only"]=[deepcopy(original[1])]
            self._event(state,rule,"rut_notation_vowel_not_spoken",unit=original[1],not_an_it_lopa_claim=True,
                        evidence="Bālamanoramā 7.1.6: रुटि उकार उच्चारणार्थः")
        state["morphemes"].insert(-1,unit)
        state["augmented_ending"]={"id":"ending-with-"+name,"members":[unit["id"],"ting"],"host":host,"rule":"1.1.46"}
        self._event(state,"1.1.46","tit_augment_initial_member",host=host,parent="ting",anga_member=False)
        ordered(state)
        return True

    def _strength11(self, state):
        root,following=root_and_following(state);ting=state["morphemes"][-1]
        weak=self._strength(state);id=root["identity"];first=sounds(following)[0]
        if id=="1020002" and weak:
            if first in self.pg7_rules["8.2.30"]["parameters"]["following"]:
                self._replace(state,root,len(root["visible"])-1,1,[],"6.4.37","han_final_n_lopa",trigger=ting["id"])
            elif first in VOWELS:
                self._replace(state,root,1,1,[],"6.4.98","han_upadha_a_lopa",trigger=ting["id"])
                self._replace(state,root,0,1,["gh"],"7.3.54","han_h_before_actual_n",deleted_a_not_restored=True,
                              local_license="Kāśikā 7.3.54 excludes sthānivad interruption here")
        if id=="1020070" and weak and first not in VOWELS:
            self._replace(state,root,1,1,["i"],"6.4.34","sas_weak_hal_upadha_i")
        if id=="1020068" and weak:
            if first in VOWELS:
                self._replace(state,root,len(root["visible"])-1,1,[],"6.4.112","lexical_abhyasta_a_lopa")
            else:
                self._replace(state,root,len(root["visible"])-1,1,["i"],"6.4.114","daridra_weak_hal_i")
                self._block11(state,"6.4.114","6.4.113")
        if id=="1020026":
            self._replace(state,root,1,1,["e"],"7.4.21","si_guna_despite_ngit",trigger=ting["id"])
            self._block11(state,"7.4.21","1.1.5")
            return [state]
        if id=="1020061":
            if not weak or first in VOWELS:
                variants=[deepcopy(state)] if not weak else [deepcopy(state),deepcopy(state)]
                target=variants[-1];r=target["morphemes"][0]
                self._r_substitute(target,r,1,"ā","7.2.114","mrj_vrddhi")
                self._block11(target,"7.2.114","7.3.86")
                target["pg11_options"].append("mrj-vrddhi")
                if weak:
                    self._event(variants[0],"7.2.114","weak_vowel_vrddhi_not_selected",license="क्ङित्यजादौ वेष्यते")
                    variants[0]["pg11_options"].append("mrj-weak")
                return variants
        if id=="1020067":
            if weak:
                state["blocked"].append({"rule":"7.3.85","reason":"the actual ending is ngitvat"})
            else:
                self._r_substitute(state,root,len(root["visible"])-1,"a","7.3.85","jagr_guna")
                return [state]
        self._guna(state,[root],ting)
        return [state]

    def _junction11(self, state):
        root,following=root_and_following(state)
        if state.get("abhyasta"):
            copy=state["morphemes"][0]
            if sounds(copy)!=["i"] or sounds(root)[0] not in self.pg11_rules["6.4.78"]["parameters"]["before"]:
                raise ValueError("Ṛ copy junction no longer has the reviewed dissimilar vowel")
            self._replace(state,copy,0,1,["i","y"],"6.4.78","copy_iy_before_root_vowel",following_owner=root["id"])
        if sounds(following)[0] not in VOWELS:
            return
        if root["identity"]=="1020040" and sounds(root)==["i"]:
            self._replace(state,root,0,1,["y"],"6.4.81","in_weak_vowel_yan")
            self._block11(state,"6.4.81","6.4.77")
        elif sounds(root)[-1]=="e":
            self._replace(state,root,len(root["visible"])-1,1,["a","y"],"6.1.78","e_before_vowel_to_ay")
        else:
            self._junction10(state)

    def derive(self, request):
        if not isinstance(request,Request) or request.lexical_id not in self.pg11_ids:
            return super().derive(request)
        if request.prefixes:
            return unresolved("Prefixed PG11 paths are outside the reviewed domain")
        plans=self.plan(request)
        if plans["status"]!="REVIEWED_MORPHOLOGICAL_PLANS":return plans
        results=[]
        for state in plans["branches"]:
            if any(o["status"] not in {"WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME","REDUPLICATION_NOT_EXECUTED"} for o in state["open_obligations"]):
                return unresolved("An independent morphological obligation remains",plans=plans)
            state["pg11_options"]=[]
            self._prepare11(state)
            if request.lexical_id=="1030017":self._copy_r(state)
            for current in self._ending_variants(state,request):
                self._augment11(current)
                for variant in self._strength11(current):
                    self._junction11(variant)
                    variant["fulfilled_obligations"]=[{"prior_obligation":deepcopy(o),"resolution":"PG11 reviewed lexical path"} for o in variant["open_obligations"]]
                    variant["open_obligations"]=[]
                    variant.update(status="PRE_TRIPADI_PG11_DERIVATION",projection="".join(s["symbol"] for s in ordered(variant)))
                    for view in self._readout11(variant):
                        results.append({"branch_id":variant["choice"]["branch_id"]+":"+":".join(variant["pg11_options"]+[view["option"]]),
                            "pre_tripadi":deepcopy(variant),"readout":view,"form":view["projection"]})
        return {"status":"COMPLETE_IN_REVIEWED_LEXICAL_PRESENT_DOMAIN","branches":results,"forms":sorted({b["form"] for b in results}),
                "word_validity":"SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout11(self, original):
        if original.get("status") != "PRE_TRIPADI_PG11_DERIVATION" or original["request"]["lexical_id"] not in self.pg11_ids:
            raise ValueError("Only a retained PG11 morphological source can enter readout")
        state={"visible":ordered(original),"history":[],"blocked":[],"visibility_queries":[]}
        seq=state["visible"]
        root,following=root_and_following(original);id=root["identity"];owner=root["id"]
        jhal=self.pg11_rules["8.2.30"]["parameters"]["following"]

        def change(i,symbol,rule,cause=None):
            before=deepcopy(seq[i])
            if before["symbol"]==symbol:return
            event=self._event(state,rule,"ordered_phonetic_replacement",before=before,cause_uid=cause)
            seq[i]={**before,"uid":f"pg11:readout:{event['index']}","symbol":symbol,
                "kind":"ayogavaha" if symbol in {"ṃ","ḥ"} else "vowel" if symbol in VOWELS else "consonant",
                "replaces":[before["uid"]],"introduced_by":rule}
            event["after"]=deepcopy(seq[i])

        def remove(i,rule,effect):
            self._event(state,rule,effect,target=deepcopy(seq[i]),following_uid=seq[i+1]["uid"] if i+1<len(seq) else None)
            del seq[i]

        def root_positions():return [i for i,s in enumerate(seq) if s["owner"]==owner]

        last=root_positions()[-1]
        if id in self.pg11_rules["8.2.25"]["parameters"]["lexical_ids"] and seq[last]["symbol"]=="s" and seq[last+1]["symbol"]=="dh":
            remove(last,"8.2.25","root_s_lopa_before_dh_affix")
        positions=root_positions();last=positions[-1]
        if (id=="1020007" and [seq[i]["symbol"] for i in positions[-2:]]==["k","ṣ"]
                and seq[last+1]["symbol"] in jhal):
            remove(positions[-2],"8.2.29","caks_cluster_initial_k_lopa")
        last=root_positions()[-1];a=seq[last]["symbol"];b=seq[last+1]["symbol"]
        if b in jhal:
            if id in self.pg11_rules["8.2.36"]["parameters"]["lexical_ids"] and a in {"j","ś"}:
                if a=="j":self._block11(state,"8.2.36","8.2.30")
                change(last,"ṣ","8.2.36",seq[last+1]["uid"])
            elif a in self.pg11_rules["8.2.30"]["parameters"]["mapping"]:
                change(last,self.pg11_rules["8.2.30"]["parameters"]["mapping"][a],"8.2.30",seq[last+1]["uid"])
            elif a=="h":
                if original.get("ah_substitution"):
                    self._block11(state,"8.2.35","8.2.31")
                    change(last,"th","8.2.35",seq[last+1]["uid"])
                elif id in self.pg11_rules["8.2.32"]["parameters"]["lexical_ids"] and root["original"][0]["symbol"]=="d":
                    self._block11(state,"8.2.32","8.2.31")
                    change(last,"gh","8.2.32",seq[last+1]["uid"])
                elif id=="1020006":
                    change(last,"ḍh","8.2.31",seq[last+1]["uid"])
                else:raise ValueError("An unreviewed h-final exception reached PG11 readout")
        positions=root_positions();last=positions[-1]
        if (id in self.pg11_rules["8.2.37"]["parameters"]["lexical_ids"]
                and sum(seq[i]["symbol"] in VOWELS for i in positions)==1
                and seq[last]["symbol"] in {"jh","bh","gh","ḍh","dh"}
                and (seq[last+1]["symbol"]=="s" or [s["symbol"] for s in seq[last+1:last+3]]==["dh","v"])):
            if seq[positions[0]]["symbol"]!="d":raise ValueError("The admitted bhaṣ target is original root d")
            change(positions[0],"dh","8.2.37",seq[last+1]["uid"])
        for sid in ("8.2.40","8.2.41"):
            p=self.pg7_rules[sid]["parameters"]
            for i in range(len(seq)-1):
                a,b=seq[i]["symbol"],seq[i+1]["symbol"]
                if sid=="8.2.40" and a in p["preceding"] and b in p["targets"]:
                    change(i+1,p["replacement"],sid,seq[i]["uid"])
                elif sid=="8.2.41" and a in p["mapping"] and b in p["following"]:
                    change(i,p["mapping"][a],sid,seq[i+1]["uid"])
        if id=="1020006":
            dh_edge=[e for e in self.pg11["visibility_exceptions"] if e.get("query")=="8.3.13"]
            length_edge=[e for e in self.pg11["visibility_exceptions"] if e.get("query")=="6.3.111"]
            if (len(dh_edge)!=1 or dh_edge[0].get("visible_rule")!="8.4.41" or dh_edge[0].get("lexical_id")!=id
                    or dh_edge[0].get("target_pair")!=["ḍh","dh"] or len(length_edge)!=1
                    or length_edge[0].get("visible_rule")!="8.3.13" or length_edge[0].get("lexical_id")!=id
                    or length_edge[0].get("requires_actual_deletion") is not True):
                raise ValueError("Lih's local visibility permissions are absent")
            for i in range(len(seq)-2,-1,-1):
                if seq[i]["owner"]==owner and [seq[i]["symbol"],seq[i+1]["symbol"]]==["ḍh","dh"]:
                    state["visibility_queries"].append({**deepcopy(dh_edge[0]),"target_uid":seq[i]["uid"],"global_tripadi_reversal":False})
                    change(i+1,"ḍh","8.4.41",seq[i]["uid"])
                    removed=deepcopy(seq[i]);remove(i,"8.3.13","dh_lopa_with_local_stutva_visibility")
                    state["visibility_queries"].append({**deepcopy(length_edge[0]),"deletion_uid":removed["uid"],"global_tripadi_reversal":False})
                    if i>0 and seq[i-1]["owner"]==owner and seq[i-1]["symbol"]=="i":
                        change(i-1,"ī","6.3.111",removed["uid"])
                    else:
                        state["blocked"].append({"rule":"6.3.111","reason":"the preceding vowel is outside the admitted short-i lengthening"})
        if seq[-1]["symbol"]=="s":
            change(len(seq)-1,"r","8.2.66")
            state["history"][-1].update(ru_teaching="रुँ",retained_marker="u",marker_rules=["1.3.2","1.3.9"])
            change(len(seq)-1,"ḥ","8.3.15")
        p=self.root_grammar.rules["8.3.24"]["parameters"]
        for i in range(len(seq)-1):
            if seq[i]["symbol"] in p["targets"] and seq[i+1]["symbol"] in p["following"]:
                change(i,p["replacement"],"8.3.24",seq[i+1]["uid"])
        p=self.pg11_rules["8.3.59"]["parameters"]
        for i in range(1,len(seq)-1):
            if seq[i]["owner"]=="ting" and seq[i]["symbol"]=="s" and seq[i-1]["symbol"] in p["adjacent_triggers"]:
                change(i,"ṣ","8.3.59",seq[i-1]["uid"])
        if id=="1020070":
            for i in range(1,len(seq)):
                if seq[i]["owner"]==owner and seq[i]["symbol"]=="s" and seq[i-1]["symbol"]=="i":
                    change(i,"ṣ","8.3.60",seq[i-1]["uid"])
        for i in range(len(seq)):
            choice=local_nati([s["symbol"] for s in seq],i,same_pada=True,pada_final=i==len(seq)-1,exceptions_reviewed=True)
            if choice["status"]=="LICENSED":change(i,"ṇ",choice["rule"],seq[choice["trigger_index"]]["uid"])
        for sid,inhibition in (("8.4.40","8.4.44"),("8.4.41","8.4.43")):
            p=self.root_grammar.rules[sid]["parameters"]
            while True:
                updates=[]
                for i,sound in enumerate(seq):
                    if sound["symbol"] not in p["mapping"]:continue
                    for j in (i-1,i+1):
                        if not 0<=j<len(seq) or seq[j]["symbol"] not in p["triggers"]:continue
                        q=self.root_grammar.rules[inhibition]["parameters"]
                        blocked=(sid=="8.4.40" and j<i and seq[j]["symbol"]==q["preceding"] and sound["symbol"] in q["target"] or
                                 sid=="8.4.41" and j>i and seq[j]["symbol"]==q["following"] and sound["symbol"] in q["target"])
                        if blocked:state["blocked"].append({"rule":sid,"by":inhibition,"target_uid":sound["uid"]})
                        else:updates.append((i,p["mapping"][sound["symbol"]],seq[j]["uid"]))
                if not updates:break
                for i,symbol,cause in updates:change(i,symbol,sid,cause)
        for sid in ("8.4.53","8.4.55","8.4.58"):
            p=(self.pg7_rules if sid=="8.4.55" else self.root_grammar.rules)[sid]["parameters"]
            for i in range(len(seq)-2,-1,-1):
                a,b=seq[i]["symbol"],seq[i+1]["symbol"]
                if sid=="8.4.58":
                    if a==p["target"] and b in p["mapping"]:change(i,p["mapping"][b],sid,seq[i+1]["uid"])
                elif a in p["mapping"] and b in p["following"]:change(i,p["mapping"][a],sid,seq[i+1]["uid"])
        targets=collapse_targets(seq,self.pg7_rules["8.4.65"]["parameters"])
        if len(targets)>1:raise ValueError("Multiple interacting collapse sites are not admitted")
        outputs=[]
        for delete in ([False,True] if targets else [False]):
            variant=deepcopy(state)
            variant["option"]="jhar-deleted" if delete else "jhar-retained" if targets else "no-jhar-option"
            if targets:
                i=targets[0]
                self._event(variant,"8.4.65","optional_jhar_lopa" if delete else "optional_jhar_retained",
                            target=variant["visible"][i],preceding_uid=variant["visible"][i-1]["uid"],following_uid=variant["visible"][i+1]["uid"])
                if delete:del variant["visible"][i]
            variant.update(status="PG11_LAT_PAUSE_READOUT",projection="".join(s["symbol"] for s in variant["visible"]),
                           feedback_into_earlier_rules=False,optional_consonant_doubling="OUTSIDE_PROFILE")
            outputs.append(variant)
        return outputs
