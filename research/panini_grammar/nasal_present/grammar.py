"""PG12: identified śnu/u/śnā present paths with retained root operations.

This bounded linguistic adapter never reads expected words or comparison forms.
The native operator-family construction remains an independent open obligation.
"""
from copy import deepcopy
import json
from pathlib import Path

from research.panini_grammar.lexical_present.grammar import Grammar as PG11Grammar, Request, VOWELS, sounds, unresolved
from research.panini_grammar.nasal_present.scope import ReviewedScope
from research.panini_grammar.non_thematic_lat.grammar import u_context
from research.panini_grammar.verification.marker_review import tokenize

HERE = Path(__file__).resolve().parent
AFFIX_IDENTITIES = {"śnu": "śnu:3.1.73", "u": "u:3.1.79", "śnā": "śnā:3.1.81"}


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def ordered(state):
    units = state["morphemes"]
    if len(units) != 3:
        raise ValueError("PG12 requires one root, one vikaraṇa and one ending")
    root, vik, ting = units
    if (root["kind"] != "root" or root["identity"] != state["request"]["lexical_id"]
            or root["id"] != "root:" + root["identity"] or vik["id"] != "vikarana"
            or vik["identity"] != AFFIX_IDENTITIES.get(state["choice"]["affix"])
            or vik.get("whole_affix_deletion") or ting["id"] != "ting"
            or not ting["features"].get("ting")):
        raise ValueError("The retained root, vikaraṇa or ending identity changed")
    seq = [{**deepcopy(s), "owner": u["id"]} for u in units for s in u["visible"]]
    if len({s["uid"] for s in seq}) != len(seq):
        raise ValueError("Visible sound identities must be unique")
    return seq


def nati_choice(seq, index, *, same_pada, pada_final, exceptions_reviewed, interveners):
    """The reviewed aṭ/ku/pu window; prefix and num extensions are excluded."""
    if not all(isinstance(v, bool) for v in [same_pada, pada_final, exceptions_reviewed]):
        return unresolved("Ṇatva requires explicit boundaries and exception review")
    if not 0 <= index < len(seq) or seq[index] != "n" or not same_pada:
        return {"status": "INAPPLICABLE"}
    if pada_final:
        return {"status": "BLOCKED", "rule": "8.4.37"}
    if not exceptions_reviewed:
        return unresolved("The lexical prohibition context has not been reviewed")
    for j in range(index - 1, -1, -1):
        if seq[j] in {"r", "ṛ", "ṝ", "ṣ"}:
            return {"status": "LICENSED", "rule": "8.4.1" if j == index-1 else "8.4.2",
                    "trigger_index": j, "intervening": seq[j+1:index], "replacement": "ṇ"}
        if seq[j] not in interveners:
            return {"status": "OUTSIDE_REVIEWED_WINDOW"}
    return {"status": "INAPPLICABLE"}


class Grammar(PG11Grammar):
    def __init__(self, records, roots, review=None):
        super().__init__(records, roots)
        self.pg12 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.pg12_scope = ReviewedScope(records, self.review["scope_policies"], self.pg6["scope_policies"],
            self.pg7["scope_policies"], self.pg9["scope_policies"], self.pg10["scope_policies"],
            self.pg11["scope_policies"], self.pg12["scope_policies"])
        self.pg12_rules = {r["sid"]: self.pg12_scope.compile(r) for r in self.pg12["records"]}
        if (len(self.pg12_rules) != len(self.pg12["records"])
                or any(r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg12_rules.values())
                or any(r["sanskrit"] != self.pg12_scope.frame(r["sid"])["text"] for r in self.pg12["records"])):
            raise ValueError("PG12 wording, occurrences or grammatical cases do not bind")
        additions = load("LEXICAL_ENTRIES.json")["entries"]
        self.pg12_ids = {e["id"] for e in additions}
        if len(self.pg12_ids) != len(additions):
            raise ValueError("Duplicate PG12 lexical identity")
        source = {r["i"]: r for r in roots}
        for entry in additions:
            keys = ["baseindex", "aupadeshik", "gana", "pada", "artha", "tags"]
            if "dhatu_note" in entry:
                keys.append("dhatu_note")
            if any(entry[k] != source[entry["id"]][k] for k in keys):
                raise ValueError("The PG12 source lexical identity or qualification changed")
            self.entries[entry["id"]] = deepcopy(entry)

    def _block12(self, state, winner, loser, **context):
        relations = [e for e in self.pg12["priority"] if (e["winner"], e["loser"]) == (winner, loser)]
        if len(relations) != 1:
            raise ValueError("PG12 local priority is not uniquely reviewed")
        state["blocked"].append({"rule": loser, "by": winner, "relation": deepcopy(relations[0]), **deepcopy(context)})

    @staticmethod
    def _knit(unit):
        return any(unit["features"].get(k) for k in ["kit", "ngit", "ngitvat"])

    def _n_lopa12(self, state):
        root, vik, _ = state["morphemes"]
        if (root["identity"] not in self.pg12_rules["6.4.24"]["parameters"]["lexical_ids"]
                or state["root_preprocessing"]["idit"] or not self._knit(vik)):
            return False
        seq = sounds(root)
        if len(seq) < 2 or seq[-2] != "n" or seq[-1] in VOWELS:
            return False
        self._replace(state, root, len(seq)-2, 1, [], "6.4.24", "non_idit_penultimate_n_lopa",
                      trigger=vik["id"], original_n_not_num=True)
        return True

    def _samprasarana12(self, state):
        root, vik, _ = state["morphemes"]
        p = self.pg12_rules["6.1.16"]["parameters"]
        if root["identity"] not in p["lexical_ids"] or not self._knit(vik):
            return False
        if state.get("samprasarana") or sounds(root) != self.entries[root["identity"]]["root_shape"]:
            raise ValueError("Saṃprasāraṇa requires the retained, unprocessed reviewed root")
        index = 1
        before = deepcopy(root["visible"][index])
        replacement = p["mapping"][before["symbol"]]
        self._replace(state, root, index, 1, [replacement], "6.1.16", "owned_samprasarana", trigger=vik["id"])
        evidence = {"owner": root["id"], "source": before, "result_uid": root["visible"][index]["uid"],
                    "rule": "1.1.45", "trigger": vik["id"]}
        state["samprasarana"] = evidence
        self._event(state, "1.1.45", "result_has_samprasarana_designation", evidence=evidence)
        if sounds(root)[index+1] not in VOWELS:
            raise ValueError("The reviewed following vowel of saṃprasāraṇa is absent")
        self._replace(state, root, index, 2, [replacement], "6.1.108", "root_internal_purvarupa",
                      source_samprasarana_uid=evidence["result_uid"], owner=root["id"])
        if index == len(root["visible"])-1:
            if root["identity"] != "1090034" or sounds(root) != ["j", "i"]:
                raise ValueError("Only the reviewed final jya saṃprasāraṇa can lengthen here")
            self._replace(state, root, index, 1, ["ī"], "6.4.2", "final_samprasarana_lengthening",
                          preceding_anga_consonant_uid=root["visible"][0]["uid"])
        else:
            state["blocked"].append({"rule": "6.4.2", "reason": "the saṃprasāraṇa vowel is not final in this aṅga"})
        return True

    def _ut12(self, state):
        root, vik, _ = state["morphemes"]
        p = self.pg12_rules["6.4.19"]["parameters"]
        if (root["identity"] != p["lexical_id"] or not self._knit(vik)
                or not sounds(vik) or sounds(vik)[0] not in {"n", "m", "ṇ", "ṅ", "ñ"}):
            return False
        if state.get("ut_substitute") or sounds(root) != ["kh", "a", "v"]:
            raise ValueError("The reviewed ūṭh source is the unreplaced final v of khav")
        teaching = [{"uid": f"ut:teaching:{i}", "symbol": x.symbol}
                    for i, x in enumerate(tokenize(p["teaching"]))]
        if [x["symbol"] for x in teaching] != ["ū", "ṭh"]:
            raise ValueError("The ūṭh teaching marker changed")
        source = deepcopy(root["visible"][-1])
        self._replace(state, root, len(root["visible"])-1, 1, ["ū"], "6.4.19", "root_final_v_to_ut",
                      teaching=teaching, trigger=vik["id"], substitute_not_augment=True)
        state["ut_substitute"] = {"identity": "ūṭh:6.4.19", "owner": root["id"], "source": source,
            "visible_uid": root["visible"][-1]["uid"], "teaching": teaching, "marker": deepcopy(teaching[-1]), "is_augment": False}
        self._event(state, "1.3.3", "ut_final_th_marker", marker=teaching[-1])
        self._event(state, "1.3.9", "ut_marker_lopa", marker=teaching[-1], retained_in_memory=True)
        return True

    def _ut_junction12(self, state):
        root = state["morphemes"][0]
        p = self.pg12_rules["6.1.89"]["parameters"]
        evidence = state.get("ut_substitute", {})
        if (root["identity"] != p["lexical_id"] or evidence.get("identity") != p["requires_substitute_identity"]
                or evidence.get("owner") != root["id"] or evidence.get("is_augment") is not False
                or sounds(root)[-2:] != ["a", "ū"] or root["visible"][-1]["uid"] != evidence.get("visible_uid")):
            raise ValueError("Vṛddhi requires the actual owned ūṭh substitute, not any ū")
        self._replace(state, root, len(root["visible"])-2, 2, ["au"], "6.1.89", "a_ut_vrddhi_ekadesha",
                      owned_substitute=deepcopy(evidence), same_root_owner=True)
        self._block12(state, "6.1.89", "6.1.87")

    def _prepare12(self, state):
        ordered(state)
        if state.get("pg12_prepared"):
            raise ValueError("A PG12 root cannot be prepared twice")
        root, vik, _ = state["morphemes"]
        entry = self.entries[root["identity"]]
        if root["identity"] not in self.pg12_ids:
            raise ValueError("This lexical identity is outside PG12 preparation")
        optional = root["identity"] in self.pg12_rules["3.1.82"]["parameters"]["lexical_ids"]
        prescription = self.pg12_rules[{"5": "3.1.73", "8": "3.1.79", "9": "3.1.81"}[entry["gana"]]]
        allowed = self.pg12_rules["3.1.82"]["parameters"]["affixes"] if optional else [prescription["parameters"]["affix"]]
        if (state["choice"]["affix"] not in allowed
                or state["choice"]["rule"] != ("3.1.82" if optional else prescription["sid"])):
            raise ValueError("The selected affix does not belong to this reviewed source class")
        if sounds(root) != entry["root_shape"]:
            raise ValueError("The inherited preprocessing shape has changed")
        if entry.get("classical_license"):
            state["lexical_register_evidence"] = {"source_tags": entry["tags"], "license": entry["classical_license"],
                "requested_register": "classical", "source": "Siddhāntakaumudī/Bālamanoramā 7.4.72"}
            self._event(state, "lexicon:"+root["identity"], "classical_use_with_source_tag_retained", evidence=state["lexical_register_evidence"])
        self._n_lopa12(state)
        self._samprasarana12(state)
        if root["identity"] == "1090043" and vik["features"]["sit"]:
            self._replace(state, root, 0, len(root["visible"]), ["j", "ā"], "7.3.79", "jna_to_long_ja", trigger=vik["id"])
        p = self.pg12_rules["7.3.80"]["parameters"]
        state["pvadi_membership"] = {"reading": p["reading"], "lexical_id": root["identity"],
                                     "member": root["identity"] in p["lexical_ids"]}
        if state["pvadi_membership"]["member"] and vik["features"]["sit"]:
            last = sounds(root)[-1]
            if last not in p["mapping"]:
                raise ValueError("The reviewed pvādi shortening target is not long")
            self._replace(state, root, len(root["visible"])-1, 1, [p["mapping"][last]], "7.3.80", "identified_pvadi_shortening", trigger=vik["id"])
            if last == "ṝ":
                self._block12(state, "7.3.80", "7.1.100", former_vowel=last)
        if root["identity"] == "1090070":
            if sounds(root) != ["s", "v", "ṝ"]:
                raise ValueError("The residual long-ṛ profile is only the identified svṝ root")
            self._r_substitute(state, root, 2, "u", "7.1.102", "labiodental_preceded_long_r_to_ur")
            self._block12(state, "7.1.102", "7.1.100")
        if self._ut12(state):
            self._ut_junction12(state)
        state["pg12_prepared"] = True

    def _root_options12(self, state):
        if not state.get("pg12_prepared") or state.get("pg12_root_strength_resolved"):
            raise ValueError("Root strength requires exactly one prepared PG12 source")
        state["pg12_root_strength_resolved"] = True
        root, vik, _ = state["morphemes"]
        p = self.pg12_rules["7.3.86"]["parameters"]
        if root["identity"] not in p["optional_lexical_ids"]:
            self._guna(state, [root], vik)
            return [state]
        if (state["choice"]["affix"] != p["trigger_affix"] or self._knit(vik)
                or not vik["features"]["ardhadhatuka"] or sounds(root)[-2] not in p["mapping"]):
            raise ValueError("The optional root guṇa needs its actual u affix and short-ik upadhā")
        kept, changed = deepcopy(state), deepcopy(state)
        self._event(kept, "7.3.86", "commentary_guna_not_selected", license=p["option_license"], trigger=vik["id"])
        kept["pg12_options"].append("root-guna-omitted")
        target = changed["morphemes"][0]
        if sounds(target)[-2] == "ṛ":
            self._r_substitute(changed, target, len(target["visible"])-2, "a", "7.3.86", "optional_root_guna")
        else:
            self._replace(changed, target, len(target["visible"])-2, 1, ["e"], "7.3.86", "optional_root_guna", trigger=vik["id"])
        changed["pg12_options"].append("root-guna-selected")
        return [kept, changed]

    def _affix_options12(self, state, request):
        if not state.get("pg12_root_strength_resolved") or state.get("pg12_affix_processed"):
            raise ValueError("Affix strength follows root strength exactly once")
        state["pg12_affix_processed"] = True
        root, vik, ting = state["morphemes"]
        self._non_a_ending(state, ting, request)
        weak = ting["features"]["ngitvat"] or ting["features"]["kit"] or ting["features"]["ngit"]
        state["stem_strength"] = {"weak": weak, "cause": ting["id"], "pit": ting["features"]["pit"],
                                  "ngitvat": ting["features"]["ngitvat"]}
        self._guna(state, [root, vik], ting)
        if weak and state["choice"]["affix"] == "śnā":
            if sounds(vik) != ["n", "ā"]:
                raise ValueError("The original śnā ā must be retained before strength processing")
            if sounds(ting)[0] in VOWELS:
                self._replace(state, vik, 1, 1, [], "6.4.112", "sna_a_lopa_after_ending_substitution", trigger=ting["id"])
            else:
                self._replace(state, vik, 1, 1, ["ī"], "6.4.113", "sna_weak_hal_long_i", trigger=ting["id"])
                self._block6(state, "6.4.113", "6.4.112")
        context = u_context(state)
        variants = [state]
        if context and weak and sounds(ting)[0] in {"m", "v"}:
            if context["cluster_before_u"]:
                state["blocked"].append({"rule": "6.4.107", "reason": "actual consonant cluster before affix u", "context": context})
            else:
                kept, deleted = deepcopy(state), deepcopy(state)
                self._event(kept, "6.4.107", "optional_affix_u_retained", context=context)
                self._replace(deleted, deleted["morphemes"][1], len(vik["visible"])-1, 1, [], "6.4.107", "optional_affix_u_lopa", context=context)
                kept["pg12_options"].append("u-retained"); deleted["pg12_options"].append("u-lopa")
                variants = [kept, deleted]
        for current in variants:
            root, vik, ting = current["morphemes"]
            context = u_context(current)
            if context and sounds(ting)[0] in VOWELS:
                if current["choice"]["affix"] == "śnu":
                    if context["multiple_vowels"] and not context["cluster_before_u"] and ting["features"]["sarvadhatuka"]:
                        rule, symbols = "6.4.87", ["v"]
                        self._block6(current, rule, "6.4.77", context=context)
                    else:
                        rule, symbols = "6.4.77", ["u", "v"]
                        self._block6(current, rule, "6.1.77", context=context)
                else:
                    rule, symbols = "6.1.77", ["v"]
                self._replace(current, vik, len(vik["visible"])-1, 1, symbols, rule, "owned_affix_u_vowel_junction", context=context)
        return variants

    def derive(self, request):
        if not isinstance(request, Request) or request.lexical_id not in self.pg12_ids:
            return super().derive(request)
        if request.prefixes:
            return unresolved("Prefixed PG12 paths require a separate source review")
        plans = self.plan(request)
        if plans["status"] != "REVIEWED_MORPHOLOGICAL_PLANS":
            return plans
        results = []
        for state in plans["branches"]:
            if any(o["status"] != "WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME" for o in state["open_obligations"]):
                return unresolved("An independent morphological obligation remains", plans=plans)
            state["pg12_options"] = []
            self._prepare12(state)
            for root_variant in self._root_options12(state):
                for current in self._affix_options12(root_variant, request):
                    current["fulfilled_obligations"] = [{"prior_obligation": deepcopy(o), "resolution": "reviewed PG12 root and affix path"} for o in current["open_obligations"]]
                    current["open_obligations"] = []
                    current.update(status="PRE_TRIPADI_PG12_DERIVATION", projection="".join(s["symbol"] for s in ordered(current)))
                    view = self._readout12(current)
                    results.append({"branch_id": current["choice"]["branch_id"] + ":" + ":".join(current["pg12_options"] or ["single"]),
                                    "pre_tripadi": current, "readout": view, "form": view["projection"]})
        return {"status": "COMPLETE_IN_REVIEWED_NASAL_PRESENT_DOMAIN", "branches": results,
                "forms": sorted({b["form"] for b in results}), "word_validity": "SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout12(self, original):
        if original.get("status") != "PRE_TRIPADI_PG12_DERIVATION" or original["request"]["lexical_id"] not in self.pg12_ids:
            raise ValueError("Readout requires a retained PG12 morphological source")
        state = {"visible": ordered(original), "history": [], "blocked": [], "visibility_queries": []}
        seq = state["visible"]
        root, vik, ting = original["morphemes"]
        def change(i, symbol, rule, cause=None):
            before = deepcopy(seq[i])
            if before["symbol"] == symbol:
                return
            event = self._event(state, rule, "ordered_phonetic_replacement", before=before, cause_uid=cause)
            seq[i] = {**before, "uid": "pg12:readout:"+str(event["index"]), "symbol": symbol,
                      "kind": "ayogavaha" if symbol in {"ṃ", "ḥ"} else "vowel" if symbol in VOWELS else "consonant",
                      "replaces": [before["uid"]], "introduced_by": rule}
            event["after"] = deepcopy(seq[i])
        if root["identity"] == "1090070":
            positions = [i for i,s in enumerate(seq) if s["owner"] == root["id"]]
            i = positions[-1]
            if [seq[i-1]["symbol"], seq[i]["symbol"]] == ["u", "r"] and seq[i+1]["symbol"] not in VOWELS:
                change(i-1, "ū", "8.2.77", seq[i+1]["uid"])
        if seq[-1]["symbol"] == "s":
            change(len(seq)-1, "r", "8.2.66")
            state["history"][-1].update(ru_teaching="रुँ", retained_marker="u", marker_rules=["1.3.2", "1.3.9"])
            change(len(seq)-1, "ḥ", "8.3.15")
        p = self.root_grammar.rules["8.3.24"]["parameters"]
        for i in range(len(seq)-1):
            if seq[i]["symbol"] in p["targets"] and seq[i+1]["symbol"] in p["following"]:
                change(i, p["replacement"], "8.3.24", seq[i+1]["uid"])
        p = self.pg11_rules["8.3.59"]["parameters"]
        for i in range(1, len(seq)-1):
            if seq[i]["owner"] == "ting" and seq[i]["symbol"] == "s" and seq[i-1]["symbol"] in p["adjacent_triggers"]:
                change(i, "ṣ", "8.3.59", seq[i-1]["uid"])
        pairs = self.pg12_rules["8.4.39"]["parameters"]["lexical_affix_pairs"]
        for i in range(len(seq)):
            choice = nati_choice([s["symbol"] for s in seq], i, same_pada=True, pada_final=i==len(seq)-1,
                exceptions_reviewed=True, interveners=self.pg12_rules["8.4.2"]["parameters"]["interveners"])
            if choice["status"] != "LICENSED":
                continue
            if seq[i]["owner"] == "vikarana" and [root["identity"], original["choice"]["affix"]] in pairs:
                self._block12(state, "8.4.39", choice["rule"], target_uid=seq[i]["uid"], owner="vikarana")
                if root["identity"] == "1090055":
                    license = self.pg12_rules["1.1.56"]["parameters"]
                    if (license.get("lexical_id") != root["identity"] or license.get("query") != "8.4.39"
                            or license.get("retained_identity") != vik["identity"]
                            or license.get("restores_visible_sounds") is not False
                            or self.pg12_rules["8.4.39"]["parameters"].get("retains_sna_identity_after_a_change") is not True):
                        raise ValueError("Kṣubh's retained-śnā query lacks its exact local license")
                    query = {"query": "8.4.39", "retained_identity": vik["identity"], "current_sounds": sounds(vik),
                             "license": "1.1.56", "restores_visible_sounds": False, "owner": "vikarana"}
                    state["visibility_queries"].append(query)
                    self._event(state, "1.1.56", "ksubh_prohibition_retains_sna_identity", query=query)
            else:
                change(i, "ṇ", choice["rule"], seq[choice["trigger_index"]]["uid"])
        span = {"status": "SUPPLIED_PHONETIC_SPAN", "original": deepcopy(seq), "visible": deepcopy(seq), "history": []}
        tail = self.root_grammar.phonetic(span, samhita=True, pada_final_uids=[seq[-1]["uid"]], following_unit_identities={})
        if tail["status"] != "LOCAL_PHONETIC_QUERY" or any(e["rule"] in {"8.2.78", "8.3.24"} for e in tail["history"]):
            raise ValueError("The phonetic tail re-entered an earlier phase or has an unresolved condition")
        return {"status": "PG12_LAT_PAUSE_READOUT", "projection": tail["projection"], "visible": tail["visible"],
                "history": state["history"] + tail["history"], "blocked": state["blocked"] + tail["blocked"],
                "visibility_queries": state["visibility_queries"], "feedback_into_earlier_rules": False,
                "optional_consonant_doubling": "OUTSIDE_PROFILE"}
