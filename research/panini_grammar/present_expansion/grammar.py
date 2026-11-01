"""PG10: further juhotyādi and vowel-final adādi present profiles.

Owned copies, grammatical options and ending-initial īṭ remain inspectable.
Expected forms and external conjugator tables are never read by this module.
The native full operator-family lift remains a separate open construction.
"""
from copy import deepcopy
import json
from pathlib import Path

from research.panini_grammar.abhyasa_lat.grammar import Grammar as PG9Grammar, Request, VOWELS, sounds, unresolved, ordered as copy_ordered
from research.panini_grammar.present_expansion.scope import ReviewedScope
from research.panini_grammar.verification.marker_review import tokenize
from research.panini_grammar.snam_lat.grammar import local_nati, collapse_targets

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def ordered(state):
    if state.get("abhyasta"):
        return copy_ordered(state)
    units = state["morphemes"]
    if len(units) not in {3, 4} or units[0]["kind"] != "root" or units[-1]["id"] != "ting":
        raise ValueError("PG10 adādi requires root, deleted śap, optional īṭ and tiṅ")
    vik = units[1]
    if vik["visible"] or vik.get("whole_affix_deletion") != {"kind": "luk", "rule": "2.4.72"}:
        raise ValueError("The identified śap-luk must remain unspoken")
    if len(units) == 4:
        augment = units[2]
        if (augment["id"] != "augment:iit" or augment["kind"] != "augment"
                or augment.get("host") != "ting" or not augment["features"].get("tit")
                or state.get("augmented_ending", {}).get("members") != [augment["id"], "ting"]):
            raise ValueError("īṭ must be an initial member of the following tiṅ")
    elif state.get("augmented_ending"):
        raise ValueError("An augmented ending lost its augment")
    out = [{**deepcopy(s), "owner": u["id"]} for u in units for s in u["visible"]]
    if len({s["uid"] for s in out}) != len(out):
        raise ValueError("Duplicate visible sound identity")
    return out


def root_and_following(state):
    units = state["morphemes"]
    index = next(i for i,u in enumerate(units) if u["kind"] == "root")
    return units[index], next(u for u in units[index+1:] if u["visible"])


class Grammar(PG9Grammar):
    def __init__(self, records, roots, review=None):
        super().__init__(records, roots)
        self.pg10 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.pg10_scope = ReviewedScope(records, self.review["scope_policies"], self.pg6["scope_policies"],
            self.pg7["scope_policies"], self.pg9["scope_policies"], self.pg10["scope_policies"])
        self.pg10_rules = {r["sid"]: self.pg10_scope.compile(r) for r in self.pg10["records"]}
        if len(self.pg10_rules) != len(self.pg10["records"]) or any(
                r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg10_rules.values()):
            raise ValueError("PG10 record lost a source-bound term")
        if any(r["sanskrit"] != self.pg10_scope.frame(r["sid"])["text"] for r in self.pg10["records"]):
            raise ValueError("PG10 Sanskrit wording differs from its source")
        additions = load("LEXICAL_ENTRIES.json")["entries"]
        self.pg10_ids = {e["id"] for e in additions}
        if len(self.pg10_ids) != len(additions):
            raise ValueError("Duplicate PG10 lexical identity")
        source = {r["i"]: r for r in roots}
        for entry in additions:
            if any(entry[k] != source[entry["id"]][k] for k in ("baseindex", "aupadeshik", "gana", "pada", "artha", "tags")):
                raise ValueError("PG10 lexical identity or register differs from the pinned source")
            self.entries[entry["id"]] = deepcopy(entry)

    def _block10(self, state, winner, loser, **data):
        edges = [e for e in self.pg10["priority"] if (e["winner"],e["loser"]) == (winner,loser)]
        if len(edges) != 1:
            raise ValueError("Missing or ambiguous PG10 local priority")
        state["blocked"].append({"rule":loser,"by":winner,"relation":deepcopy(edges[0]),**deepcopy(data)})

    def _r_substitute(self, state, unit, index, vowel, rule, effect):
        if sounds(unit)[index] not in {"ṛ","ṝ"}:
            raise ValueError("r-accompanied substitution requires an ṛ-vowel source")
        before = deepcopy(unit["visible"][index])
        self._replace(state, unit, index, 1, [vowel,"r"], rule, effect, rapara_rule="1.1.51")
        self._event(state, "1.1.51", "an_substitute_is_r_accompanied", source=before,
                    result=unit["visible"][index:index+2], owner=unit["id"], licensed_with=rule)

    def _copy10(self, state):
        if state.get("abhyasta") or len(state["morphemes"]) != 3:
            raise ValueError("Only an unreduplicated plan can enter PG10 copying")
        root,vik,ting = state["morphemes"]
        shapes = self.pg10_rules["6.1.10"]["parameters"]["root_shapes"]
        if root["identity"] not in shapes or sounds(root) != shapes[root["identity"]]:
            raise ValueError("The exact reviewed one-vowel root shape is required")
        if (vik.get("whole_affix_deletion") != {"kind":"ślu","rule":"2.4.75"}
                or vik["visible"] or not vik["identity"].startswith("śap:")):
            raise ValueError("Copying needs the retained śap-ślu identity")
        if sum(s in VOWELS for s in sounds(root)) != 1 or sounds(root)[0] in VOWELS:
            raise ValueError("Vowel-initial and multiple-vowel copying are outside PG10")
        copied = [{"uid":f"abhyasa:{root['identity']}:copy:{i}","symbol":s["symbol"],"kind":s["kind"],
                   "copied_from":s["uid"],"introduced_by":"6.1.10"} for i,s in enumerate(root["visible"])]
        unit = {"id":"abhyasa:"+root["identity"],"identity":"copy-of:"+root["id"],"kind":"abhyasa",
                "source_owner":root["id"],"original":copied,"visible":deepcopy(copied),
                "features":{"abhyasa":True,"pratyaya":False}}
        self._event(state,"6.1.10","copy_first_one_vowel_root",source_owner=root["id"],
                    source_span=root["visible"],copies=copied,selector_rule="6.1.1",trigger=vik["whole_affix_deletion"])
        state["morphemes"].insert(0,unit)
        self._event(state,"6.1.4","earlier_copy_is_abhyasa",owner=unit["id"])
        state["abhyasta"] = {"id":"abhyasta:"+root["identity"],"members":[unit["id"],root["id"]],"collective":True,"rule":"6.1.5"}
        self._event(state,"6.1.5","both_occurrences_collectively_abhyasta",constituent=state["abhyasta"])
        index = next(i for i,s in enumerate(sounds(unit)) if s in VOWELS)
        short = self.pg10_rules["7.4.59"]["parameters"]["mapping"]
        if sounds(unit)[index] in short:
            self._replace(state,unit,index,1,[short[sounds(unit)[index]]],"7.4.59","copy_vowel_shortening")
        for sid in ("7.4.75","7.4.76","7.4.77"):
            p = self.pg10_rules[sid]["parameters"]
            if root["identity"] not in p["lexical_ids"]:
                continue
            if sid == "7.4.75":
                self._replace(state,unit,index,1,p["mapping"][sounds(unit)[index]],sid,"nij_group_copy_guna")
            elif sounds(unit)[index] in {"ṛ","ṝ"}:
                self._r_substitute(state,unit,index,p["substitute"],sid,"lexical_copy_i")
                self._block10(state,sid,"7.4.66")
            else:
                self._replace(state,unit,index,1,[p["substitute"]],sid,"lexical_copy_i")
        # Remove later consonants, including a newly introduced rapara r.
        # Original copied sounds and their root links survive in memory.
        for i in range(len(unit["visible"])-1,0,-1):
            if sounds(unit)[i] not in VOWELS:
                self._replace(state,unit,i,1,[],"7.4.60","noninitial_copy_consonant_lopa")
        self._event(state,"7.4.60","first_copy_consonant_retained",owner=unit["id"],uid=unit["visible"][0]["uid"])
        if sounds(unit)[0] == "h":
            self._replace(state,unit,0,1,["jh"],"7.4.62","copy_h_to_palatal_aspirate")
        ordered(state)

    def _strength(self, state):
        ting = state["morphemes"][-1]; f = ting["features"]
        weak = f["kit"] or f["ngit"] or f["ngitvat"]
        state["strength"] = {"reading":"weak" if weak else "strong","cause":ting["id"],"pit":f["pit"],"ngitvat":f["ngitvat"]}
        return weak

    def _juhotyadi_states(self, state, request):
        self._copy10(state)
        self._ending9(state,request)
        abhyasa,root,vik,ting = state["morphemes"]
        weak = self._strength(state)
        self._guna(state,[abhyasa,root,vik],ting)
        if root["identity"] == self.pg10_rules["7.1.102"]["parameters"]["lexical_id"]:
            if weak:
                if sounds(root) != ["p","ṝ"]:
                    raise ValueError("The pṝ substitution requires the original long root vowel")
                self._r_substitute(state,root,1,"u","7.1.102","labial_preceded_long_r_to_u")
                self._block10(state,"7.1.102","7.1.100")
            else:
                self._block10(state,"7.3.84","7.1.102")
        hal = sounds(ting)[0] not in VOWELS
        if weak and ting["features"]["sarvadhatuka"] and hal and root["identity"] == "1030002":
            variants = [deepcopy(state),deepcopy(state)]
            self._event(variants[0],"6.4.115","optional_bhi_long_i_retained")
            self._replace(variants[1],variants[1]["morphemes"][1],1,1,["i"],"6.4.115","optional_bhi_short_i")
            for current,option in zip(variants,["bhi-long","bhi-short"]):
                current["pg10_options"].append(option)
            return variants
        if weak and ting["features"]["sarvadhatuka"] and sounds(root)[-1] == "ā":
            if not hal:
                self._replace(state,root,len(root["visible"])-1,1,[],"6.4.112","abhyasta_a_lopa_before_vowel",trigger=ting["id"])
            elif root["identity"] == "1030009":
                long,short = deepcopy(state),deepcopy(state)
                self._replace(long,long["morphemes"][1],1,1,["ī"],"6.4.113","non_ghu_a_to_long_i")
                self._block10(long,"6.4.113","6.4.112")
                self._event(long,"6.4.116","optional_short_i_not_selected")
                self._replace(short,short["morphemes"][1],1,1,["i"],"6.4.116","ha_tyaga_optional_short_i")
                self._block10(short,"6.4.116","6.4.113")
                for current,option in [(long,"ha-long"),(short,"ha-short")]:
                    current["pg10_options"].append(option)
                return [long,short]
            else:
                self._replace(state,root,len(root["visible"])-1,1,["ī"],"6.4.113","non_ghu_a_to_long_i",trigger=ting["id"])
                self._block10(state,"6.4.113","6.4.112")
        return [state]

    def _iit_eligible(self, state):
        root,following = root_and_following(state); ting = state["morphemes"][-1]
        return (not state.get("abhyasta") and root["identity"] in self.pg10_rules["7.3.95"]["parameters"]["lexical_ids"]
                and following is ting and ting["features"]["ting"] and ting["features"]["sarvadhatuka"]
                and sounds(ting)[0] not in VOWELS)

    def _iit(self, state):
        if not self._iit_eligible(state):
            return False
        teaching = self.pg10_rules["7.3.95"]["parameters"]["teaching"]
        original = [{"uid":f"augment:iit:source:{i}","symbol":s.symbol,
                     "kind":"vowel" if s.symbol in VOWELS else "consonant"} for i,s in enumerate(tokenize(teaching))]
        if [s["symbol"] for s in original] != ["ī","ṭ"]:
            raise ValueError("Only the source-reviewed īṭ teaching unit is admitted")
        augment = {"id":"augment:iit","identity":"īṭ:7.3.95","kind":"augment","host":"ting",
                   "teaching":teaching,"original":original,"visible":deepcopy(original[:1]),
                   "features":{"tit":True,"pratyaya":False},
                   "marker_evidence":{"marker_units":[{"label":"ṭ","uid":original[1]["uid"],"rule":"1.3.3"}]}}
        self._event(state,"7.3.95","optional_iit_prescribed",host="ting",original=original)
        self._event(state,"1.3.3","augment_final_t_it",target=original[1])
        self._event(state,"1.3.9","augment_marker_lopa",removed=original[1],identity_retained=True)
        state["morphemes"].insert(-1,augment)
        state["augmented_ending"] = {"id":"ending-with-iit","members":[augment["id"],"ting"],"host":"ting","rule":"1.1.46"}
        self._event(state,"1.1.46","tit_augment_initial_member_of_ending",constituent=state["augmented_ending"],anga_member=False)
        ordered(state)
        return True

    def _vrddhi_eligible(self, state):
        root,following = root_and_following(state); ting = state["morphemes"][-1]
        return (not state.get("abhyasta") and state["morphemes"][1].get("whole_affix_deletion") == {"kind":"luk","rule":"2.4.72"}
                and sounds(root)[-1] == "u" and ting["features"]["pit"] and ting["features"]["sarvadhatuka"]
                and not self._strength(state) and sounds(following)[0] not in VOWELS)

    def _adadi_states(self, state, request):
        root,vik,ting = state["morphemes"]
        if vik.get("whole_affix_deletion") != {"kind":"luk","rule":"2.4.72"}:
            raise ValueError("Adādi paths require the retained śap-luk")
        self._non_a_ending(state,ting,request)
        candidates = [state]
        if self._iit_eligible(state):
            absent,present = deepcopy(state),deepcopy(state)
            self._event(absent,"7.3.95","optional_iit_not_selected")
            if not self._iit(present):
                raise ValueError("An eligible īṭ branch failed its prescription")
            absent["pg10_options"].append("no-iit");present["pg10_options"].append("iit")
            candidates = [absent,present]
        outputs = []
        for current in candidates:
            root,following = root_and_following(current); ting = current["morphemes"][-1]
            self._strength(current)
            if self._vrddhi_eligible(current):
                if root["identity"] == self.pg10_rules["7.3.90"]["parameters"]["lexical_id"]:
                    guna,vrddhi = deepcopy(current),deepcopy(current)
                    self._block10(guna,"7.3.90","7.3.89")
                    self._guna(guna,[guna["morphemes"][0]],guna["morphemes"][-1])
                    self._event(guna,"7.3.90","optional_vrddhi_not_selected")
                    self._replace(vrddhi,vrddhi["morphemes"][0],len(root["visible"])-1,1,["au"],"7.3.90","optional_urnu_vrddhi")
                    self._block10(vrddhi,"7.3.90","7.3.89")
                    guna["pg10_options"].append("urnu-guna");vrddhi["pg10_options"].append("urnu-vrddhi")
                    outputs += [guna,vrddhi]
                    continue
                self._replace(current,root,len(root["visible"])-1,1,["au"],"7.3.89","luk_pit_hal_u_vrddhi",trigger=ting["id"])
                self._block10(current,"7.3.89","7.3.84")
            else:
                if current.get("augmented_ending") and ting["features"]["pit"]:
                    current["blocked"].append({"rule":"7.3.89","reason":"īṭ makes the following ending vowel-initial",
                                               "first_owner":following["id"],"first_sound":sounds(following)[0]})
                self._guna(current,[root],ting)
            outputs.append(current)
        return outputs

    def _junction10(self, state):
        root,following = root_and_following(state)
        if sounds(following)[0] not in VOWELS:
            return
        last = sounds(root)[-1]
        if last == "ā" and sounds(following)[0] == "a":
            self._join(state,root,following,["ā"],"6.1.101")
        elif last == "o":
            self._replace(state,root,len(root["visible"])-1,1,["a","v"],"6.1.78","o_before_iit_to_av",following_owner=following["id"])
        elif last in {"i","ī","u","ū"}:
            count = sum(s["symbol"] in VOWELS for u in state["morphemes"] if u["id"] not in {"ting","augment:iit"} for s in u["visible"])
            cluster = 0
            for s in reversed(sounds(root)[:-1]):
                if s in VOWELS:break
                cluster += 1
            context = {"whole_anga_vowels":count,"root_internal_preceding_consonants":cluster,"root_owner":root["id"],"following_owner":following["id"]}
            if last in {"i","ī"} and count > 1 and cluster < 2:
                self._replace(state,root,len(root["visible"])-1,1,["y"],"6.4.82","unclustered_i_yan",context=context)
                self._block10(state,"6.4.82","6.4.77",context=context)
            else:
                if last in {"i","ī"}:
                    state["blocked"].append({"rule":"6.4.82","reason":"root-internal cluster or single-vowel anga", "context":context})
                self._replace(state,root,len(root["visible"])-1,1,self.pg10_rules["6.4.77"]["parameters"]["mapping"][last],
                              "6.4.77","root_iy_uv_before_vowel",context=context)
                self._block10(state,"6.4.77","6.1.77",context=context)
        elif last == "ṛ":
            self._replace(state,root,len(root["visible"])-1,1,["r"],"6.1.77","root_r_yan_before_vowel",following_owner=following["id"])

    def derive(self, request):
        if not isinstance(request,Request) or request.lexical_id not in self.pg10_ids:
            return super().derive(request)
        plans = self.plan(request)
        if plans["status"] != "REVIEWED_MORPHOLOGICAL_PLANS":return plans
        if request.prefixes:return unresolved("Prefixed PG10 paths are outside the reviewed profile")
        results = []
        for state in plans["branches"]:
            entry = self.entries[request.lexical_id]
            if sounds(state["morphemes"][0]) != entry["root_shape"]:
                raise ValueError("Root preprocessing no longer matches the reviewed lexical shape")
            if any(o["status"] not in {"WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME","REDUPLICATION_NOT_EXECUTED"} for o in state["open_obligations"]):
                return unresolved("An independent plan obligation remains",plans=plans)
            state["pg10_options"] = []
            variants = self._juhotyadi_states(state,request) if entry["group"] == "juhotyadi" else self._adadi_states(state,request)
            for current in variants:
                self._junction10(current)
                current["fulfilled_obligations"] = [{"prior_obligation":deepcopy(o),"resolution":"PG10 bounded word path"} for o in current["open_obligations"]]
                current["open_obligations"] = []
                current.update(status="PRE_TRIPADI_PG10_DERIVATION",projection="".join(s["symbol"] for s in ordered(current)))
                for view in self._readout10(current):
                    results.append({"branch_id":current["choice"]["branch_id"]+":"+":".join(current["pg10_options"]+[view["option"]]),
                                    "pre_tripadi":deepcopy(current),"readout":view,"form":view["projection"]})
        return {"status":"COMPLETE_IN_REVIEWED_PRESENT_EXPANSION_DOMAIN","branches":results,
                "forms":sorted({b["form"] for b in results}),"word_validity":"SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout10(self, original):
        if original.get("status") != "PRE_TRIPADI_PG10_DERIVATION" or original["request"]["lexical_id"] not in self.pg10_ids:
            raise ValueError("A retained PG10 source is required; a readout cannot feed back")
        state = {"visible": ordered(original), "history": [], "blocked": [], "visibility_queries": []}
        seq = state["visible"]

        def change(i, substitute, rule, cause=None):
            before = deepcopy(seq[i])
            if before["symbol"] == substitute:
                return
            event = self._event(state, rule, "ordered_phonetic_replacement", before=before, cause_uid=cause)
            seq[i] = {**before, "uid": f"pg10:readout:{event['index']}", "symbol": substitute,
                      "kind": "ayogavaha" if substitute in {"ṃ", "ḥ"} else "vowel" if substitute in VOWELS else "consonant",
                      "replaces": [before["uid"]], "introduced_by": rule}
            event["after"] = deepcopy(seq[i])

        for sid in ("8.2.30", "8.2.40", "8.2.41"):
            p = (self.pg10_rules if sid == "8.2.30" else self.pg7_rules)[sid]["parameters"]
            for i in range(len(seq) - 1):
                a, b = seq[i]["symbol"], seq[i + 1]["symbol"]
                if sid == "8.2.40":
                    if a in p["preceding"] and b in p["targets"]:
                        change(i + 1, p["replacement"], sid, seq[i]["uid"])
                elif a in p["mapping"] and b in p["following"]:
                    change(i, p["mapping"][a], sid, seq[i + 1]["uid"])
        root,following = root_and_following(original)
        if (root["identity"] == self.pg10_rules["8.2.77"]["parameters"]["lexical_id"]
                and sounds(root) == ["p","u","r"] and sounds(following)[0] not in VOWELS):
            target = root["visible"][-2]["uid"]
            index = next(i for i,s in enumerate(seq) if s["uid"] == target)
            change(index,"ū","8.2.77",following["visible"][0]["uid"])
        if seq[-1]["symbol"] == "s":
            change(len(seq) - 1, "r", "8.2.66")
            state["history"][-1].update(ru_teaching="रुँ", retained_marker="u", marker_rules=["1.3.2", "1.3.9"])
            change(len(seq) - 1, "ḥ", "8.3.15")
        p = self.root_grammar.rules["8.3.24"]["parameters"]
        for i in range(len(seq) - 1):
            if seq[i]["symbol"] in p["targets"] and seq[i + 1]["symbol"] in p["following"]:
                change(i, p["replacement"], "8.3.24", seq[i + 1]["uid"])
        p = self.pg10_rules["8.3.59"]["parameters"]
        for i in range(1, len(seq) - 1):
            if seq[i]["owner"] == "ting" and seq[i]["symbol"] == "s" and seq[i - 1]["symbol"] in p["adjacent_triggers"]:
                change(i, "ṣ", "8.3.59", seq[i - 1]["uid"])
        for i in range(len(seq)):
            choice = local_nati([s["symbol"] for s in seq], i, same_pada=True,
                                pada_final=i == len(seq) - 1, exceptions_reviewed=True)
            if choice["status"] == "LICENSED":
                change(i, "ṇ", choice["rule"], seq[choice["trigger_index"]]["uid"])
        # Reuse the reviewed PG4 contact parameters and their specific
        # prohibitions, but schedule every phase explicitly in this new view.
        for sid, inhibition in (("8.4.40", "8.4.44"), ("8.4.41", "8.4.43")):
            p = self.root_grammar.rules[sid]["parameters"]
            while True:
                updates = []
                for i, sound in enumerate(seq):
                    if sound["symbol"] not in p["mapping"]:
                        continue
                    for j in (i - 1, i + 1):
                        if not 0 <= j < len(seq) or seq[j]["symbol"] not in p["triggers"]:
                            continue
                        q = self.root_grammar.rules[inhibition]["parameters"]
                        blocked = (sid == "8.4.40" and j < i and seq[j]["symbol"] == q["preceding"] and sound["symbol"] in q["target"] or
                                   sid == "8.4.41" and j > i and seq[j]["symbol"] == q["following"] and sound["symbol"] in q["target"])
                        if blocked:
                            state["blocked"].append({"rule": sid, "by": inhibition, "target_uid": sound["uid"]})
                        else:
                            updates.append((i, p["mapping"][sound["symbol"]], seq[j]["uid"]))
                if not updates:
                    break
                for i, symbol, cause in updates:
                    change(i, symbol, sid, cause)
        for sid in ("8.4.53", "8.4.54", "8.4.55", "8.4.58"):
            if sid == "8.4.54":
                mapping = self.pg10_rules[sid]["parameters"]["mapping"]
                owners = {u["id"] for u in original["morphemes"] if u["kind"] == "abhyasa"}
                for i,sound in enumerate(seq):
                    if sound["owner"] in owners and sound["symbol"] in mapping:
                        change(i,mapping[sound["symbol"]],sid)
                continue
            p = (self.pg7_rules if sid == "8.4.55" else self.root_grammar.rules)[sid]["parameters"]
            for i in range(len(seq) - 2, -1, -1):
                a, b = seq[i]["symbol"], seq[i + 1]["symbol"]
                if sid == "8.4.58":
                    if a == p["target"] and b in p["mapping"]:
                        change(i, p["mapping"][b], sid, seq[i + 1]["uid"])
                elif a in p["mapping"] and b in p["following"]:
                    change(i, p["mapping"][a], sid, seq[i + 1]["uid"])
        targets = collapse_targets(seq, self.pg7_rules["8.4.65"]["parameters"])
        if len(targets) > 1:
            raise ValueError("Multiple interacting collapse sites are outside PG10")
        outputs = []
        for delete in ([False, True] if targets else [False]):
            variant = deepcopy(state)
            variant["option"] = "jhar-deleted" if delete else "jhar-retained" if targets else "no-jhar-option"
            if targets:
                i = targets[0]
                self._event(variant, "8.4.65", "optional_jhar_lopa" if delete else "optional_jhar_retained",
                            target=deepcopy(variant["visible"][i]),
                            preceding_uid=variant["visible"][i - 1]["uid"],
                            following_uid=variant["visible"][i + 1]["uid"])
                if delete:
                    del variant["visible"][i]
            variant.update(status="PG10_LAT_PAUSE_READOUT", projection="".join(s["symbol"] for s in variant["visible"]),
                           feedback_into_earlier_rules=False, optional_consonant_doubling="OUTSIDE_PROFILE")
            outputs.append(variant)
        return outputs
