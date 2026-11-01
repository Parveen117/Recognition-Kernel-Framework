"""PG9: owned ślu reduplication and bounded hu/dā/dhā present paths.

This linguistic adapter preserves copied-from sound identities and separate
abhyāsa/abhyasta designations. It does not read conjugator output. The local
8.2.38 view is not a general reversal of Tripādī visibility.
"""
from copy import deepcopy
import json
from pathlib import Path

from research.panini_grammar.exception_lat.grammar import Grammar as PG8Grammar, Request, VOWELS, sounds, unresolved
from research.panini_grammar.abhyasa_lat.scope import ReviewedScope

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def ordered(state):
    """A separate earlier copy and later root; ślu is retained but unspoken."""
    units = state["morphemes"]
    if len(units) != 4:
        raise ValueError("PG9 requires one abhyāsa, root, deleted śap and tiṅ")
    abhyasa, root, vik, ting = units
    group = state.get("abhyasta", {})
    if (abhyasa["kind"] != "abhyasa" or root["kind"] != "root"
            or abhyasa.get("source_owner") != root["id"]
            or group.get("members") != [abhyasa["id"], root["id"]]
            or not group.get("collective") or vik["id"] != "vikarana"
            or vik.get("whole_affix_deletion") != {"kind": "ślu", "rule": "2.4.75"}
            or vik["visible"] or ting["id"] != "ting"):
        raise ValueError("PG9 ownership, collective designation or ślu identity is missing")
    out = [{**deepcopy(s), "owner": unit["id"]} for unit in units for s in unit["visible"]]
    if len({s["uid"] for s in out}) != len(out):
        raise ValueError("Duplicate visible sound identity")
    return out


class Grammar(PG8Grammar):
    def __init__(self, records, roots, review=None):
        super().__init__(records, roots)
        self.pg9 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.pg9_scope = ReviewedScope(records, self.review["scope_policies"],
            self.pg6["scope_policies"], self.pg7["scope_policies"], self.pg9["scope_policies"])
        self.pg9_rules = {r["sid"]: self.pg9_scope.compile(r) for r in self.pg9["records"]}
        if len(self.pg9_rules) != len(self.pg9["records"]) or any(
                r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg9_rules.values()):
            raise ValueError("PG9 record lost a source-bound term")
        if any(r["sanskrit"] != self.pg9_scope.frame(r["sid"])["text"] for r in self.pg9["records"]):
            raise ValueError("PG9 Sanskrit wording differs from its source")
        source = {r["i"]: r for r in roots}
        additions = load("LEXICAL_ENTRIES.json")["entries"]
        self.pg9_ids = {e["id"] for e in additions}
        if len(self.pg9_ids) != len(additions):
            raise ValueError("Duplicate PG9 lexical identity")
        for entry in additions:
            if any(entry[k] != source[entry["id"]][k] for k in ("baseindex", "aupadeshik", "gana", "pada", "artha")):
                raise ValueError("PG9 lexical identity differs from the pinned source")
            self.entries[entry["id"]] = deepcopy(entry)

    def _block9(self, state, winner, loser, **data):
        edges = [e for e in self.pg9["priority"] if (e["winner"], e["loser"]) == (winner, loser)]
        if len(edges) != 1:
            raise ValueError("Missing or ambiguous PG9 local priority")
        state["blocked"].append({"rule": loser, "by": winner, "relation": deepcopy(edges[0]), **deepcopy(data)})

    def _reduplicate(self, state):
        if state.get("abhyasta") or len(state["morphemes"]) != 3:
            raise ValueError("An already reduplicated state cannot be copied again")
        root, vik, ting = state["morphemes"]
        shapes = self.pg9_rules["6.1.10"]["parameters"]["root_shapes"]
        if root["identity"] not in shapes or sounds(root) != shapes[root["identity"]]:
            raise ValueError("Only the three reviewed one-consonant/one-vowel roots may be copied")
        if (vik.get("whole_affix_deletion") != {"kind": "ślu", "rule": "2.4.75"}
                or vik["visible"] or not vik["identity"].startswith("śap:")):
            raise ValueError("Reduplication requires the retained śap-ślu identity")
        original = [{"uid": f"abhyasa:{root['identity']}:copy:{i}", "symbol": s["symbol"],
                     "kind": s["kind"], "copied_from": s["uid"], "introduced_by": "6.1.10"}
                    for i, s in enumerate(root["visible"])]
        unit = {"id": "abhyasa:" + root["identity"], "identity": "copy-of:" + root["id"],
                "kind": "abhyasa", "source_owner": root["id"], "original": original,
                "visible": deepcopy(original), "features": {"abhyasa": True, "pratyaya": False}}
        self._event(state, "6.1.10", "copy_first_one_vowel_root", source_owner=root["id"],
                    source_span=deepcopy(root["visible"]), copies=original,
                    selector_rule="6.1.1", trigger=deepcopy(vik["whole_affix_deletion"]))
        state["morphemes"].insert(0, unit)
        self._event(state, "6.1.4", "earlier_copy_is_abhyasa", owner=unit["id"])
        state["abhyasta"] = {"id": "abhyasta:" + root["identity"],
                             "members": [unit["id"], root["id"]], "collective": True, "rule": "6.1.5"}
        self._event(state, "6.1.5", "both_occurrences_collectively_abhyasta", constituent=state["abhyasta"])
        # All admitted copies are CV. The general cluster and coda machinery
        # of 7.4.60 is not inferred from these no-deletion cases.
        self._event(state, "7.4.60", "first_consonant_retained_no_other_consonant", owner=unit["id"],
                    retained_uid=unit["visible"][0]["uid"], deleted=[])
        short = self.pg9_rules["7.4.59"]["parameters"]["mapping"]
        if sounds(unit)[1] in short:
            self._replace(state, unit, 1, 1, [short[sounds(unit)[1]]], "7.4.59", "abhyasa_vowel_shortening")
        palatal = self.pg9_rules["7.4.62"]["parameters"]["mapping"]
        if sounds(unit)[0] in palatal:
            self._replace(state, unit, 0, 1, [palatal[sounds(unit)[0]]], "7.4.62", "abhyasa_h_to_jh")
        if root["identity"] in self.pg9_rules["1.1.20"]["parameters"]["ghu_ids"]:
            root["features"]["ghu"] = True
            self._event(state, "1.1.20", "identified_ghu_root", owner=root["id"], lexical_id=root["identity"])
        ordered(state)

    def _ending9(self, state, request):
        ordered(state)  # The abhyasta designation must name both occurrences.
        ting = state["morphemes"][-1]
        for index in reversed([i for i, s in enumerate(sounds(ting)) if s == "jh"]):
            self._replace(state, ting, index, 1, self.pg9_rules["7.1.4"]["parameters"]["replacement"],
                          "7.1.4", "abhyasta_jh_to_at", preceding_constituent=state["abhyasta"]["id"])
            self._block9(state, "7.1.4", "7.1.3")
        # The already resolved jh cannot enter PG5's generic ant replacement.
        self._ending(state, ting, request)

    def _strength9(self, state):
        abhyasa, root, vik, ting = state["morphemes"]
        features = ting["features"]
        weak = features["kit"] or features["ngit"] or features["ngitvat"]
        state["strength"] = {"reading": "weak" if weak else "strong", "cause": ting["id"],
                             "pit": features["pit"], "ngitvat": features["ngitvat"]}
        self._guna(state, [abhyasa, root, vik], ting)
        if weak and features["sarvadhatuka"] and sounds(root)[-1] == "ā":
            if not root["features"].get("ghu"):
                raise ValueError("PG9 ā-lopa needs its identified ghu designation")
            if sounds(ting)[0] not in VOWELS:
                state["blocked"].append({"rule": "6.4.113", "by": "1.1.20",
                    "reason": "aghoḥ condition false for identified ghu root", "target": root["id"]})
            self._replace(state, root, len(root["visible"])-1, 1, [], "6.4.112", "abhyasta_final_a_lopa",
                          trigger=ting["id"], constituent=state["abhyasta"]["id"])
        if root["identity"] == "1030001" and sounds(root)[-1] == "u":
            if sounds(ting)[0] in VOWELS:
                seq = sounds(abhyasa) + sounds(root)
                # This admitted shape has exactly one consonant before u.
                if (sum(s in VOWELS for s in seq) < 2 or seq[-3] not in VOWELS
                        or seq[-2] in VOWELS or not features["sarvadhatuka"]):
                    raise ValueError("hu-yaṇ requires a multiple-vowel aṅga and unclustered u")
                context = {"constituent": state["abhyasta"]["id"], "whole_anga_vowels": 2,
                           "cluster_before_u": False, "target_owner": root["id"]}
                self._replace(state, root, 1, 1, [self.pg9_rules["6.4.87"]["parameters"]["mapping"]["u"]],
                              "6.4.87", "hu_u_to_yan_before_vowel", context=context, trigger=ting["id"])
                self._block9(state, "6.4.87", "6.4.77", context=context)
            elif weak and sounds(ting)[0] in {"m", "v"}:
                state["blocked"].append({"rule": "6.4.107", "reason": "hu u belongs to the root, not a pratyaya",
                                        "target_owner": root["id"], "evidence": deepcopy(self.pg9["non_application_evidence"])})

    def derive(self, request):
        if not isinstance(request, Request) or request.lexical_id not in self.pg9_ids:
            return super().derive(request)
        plans = self.plan(request)
        if plans["status"] != "REVIEWED_MORPHOLOGICAL_PLANS":
            return plans
        if request.prefixes:
            return unresolved("Prefixed reduplicated paths have not been reviewed")
        results = []
        for state in plans["branches"]:
            if any(o["status"] not in {"WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME", "REDUPLICATION_NOT_EXECUTED"}
                   for o in state["open_obligations"]):
                return unresolved("An independent plan obligation remains", plans=plans)
            self._reduplicate(state)
            self._ending9(state, request)
            self._strength9(state)
            state["fulfilled_obligations"] = [{"prior_obligation": deepcopy(o), "resolution": "PG9 bounded word path"}
                                               for o in state["open_obligations"]]
            state["open_obligations"] = []
            state.update(status="PRE_TRIPADI_PG9_DERIVATION", projection="".join(s["symbol"] for s in ordered(state)))
            query = self._readout9(state)
            results.append({"branch_id": state["choice"]["branch_id"]+":pg9", "pre_tripadi": state,
                            "readout": query, "form": query["projection"]})
        return {"status": "COMPLETE_IN_REVIEWED_ABHYASA_LAT_DOMAIN", "branches": results,
                "forms": sorted({b["form"] for b in results}),
                "word_validity": "SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout9(self, original):
        if original.get("status") != "PRE_TRIPADI_PG9_DERIVATION" or original["request"]["lexical_id"] not in self.pg9_ids:
            raise ValueError("PG9 readout needs a retained admitted morphological derivation")
        state = {"visible": ordered(original), "history": [], "blocked": [], "visibility_queries": []}
        seq = state["visible"]
        abhyasa, root, vik, ting = original["morphemes"]

        def change(i, substitute, rule, effect, cause=None):
            before = deepcopy(seq[i])
            if before["symbol"] == substitute:
                return
            event = self._event(state, rule, effect, before=before, cause_uid=cause)
            seq[i] = {**before, "uid": f"pg9:readout:{event['index']}", "symbol": substitute,
                      "kind": "ayogavaha" if substitute in {"ḥ", "ṃ"} else "vowel" if substitute in VOWELS else "consonant",
                      "replaces": [before["uid"]], "introduced_by": rule}
            event["after"] = deepcopy(seq[i])

        # Kāśikā 8.2.38 expressly suspends both ā-lopa sthānivad restoration
        # and the invisibility of abhyāsa-jaśtva in this particular query.
        # Evaluate that jaśtva once on the retained copy, then bhaṣ. The later
        # ordinary 8.4.54 pass cannot re-enter the consumed original target.
        p = self.pg9_rules["8.2.38"]["parameters"]
        consumed = set()
        suffix = sounds(ting)
        trigger = suffix[0] in p["initial_triggers"] or suffix[:2] == p["sequence_trigger"]
        if root["identity"] == p["lexical_id"] and sounds(root)[-1] == p["root_final"] and trigger:
            edges = self.pg9["visibility_exceptions"]
            expected = {"query": "8.2.38", "visible_rule": "8.4.54", "lexical_id": root["identity"],
                        "deleted_a_is_not_restored": True, "query_consumes_abhyasa_jastva_once": True}
            if len(edges) != 1 or any(edges[0].get(k) != v for k, v in expected.items()):
                raise ValueError("The dhā-specific visibility permission is missing")
            index = next(i for i, s in enumerate(seq) if s["owner"] == abhyasa["id"])
            original_target = seq[index]["uid"]
            if seq[index]["symbol"] != "dh" or not any(e["effect"] == "abhyasta_final_a_lopa" for e in original["history"]):
                raise ValueError("The local dhā view lacks original abhyāsa or ā-lopa history")
            query = {**deepcopy(expected), "source_target_uid": original_target,
                     "license": deepcopy(edges[0]["evidence"]), "global_tripadi_reversal": False}
            state["visibility_queries"].append(query)
            change(index, self.pg9_rules["8.4.54"]["parameters"]["mapping"]["dh"],
                   "8.4.54", "jastva_visible_to_dha_query")
            if seq[index]["symbol"] != p["target"]:
                raise ValueError("bhaṣ needs the locally visible abhyāsa d")
            change(index, p["replacement"], "8.2.38", "dha_abhyasa_bhas", ting["visible"][0]["uid"])
            consumed.add(original_target)
            query["consumed_original_targets"] = sorted(consumed)
        # 8.2.40 excludes dadhāti lexically, not every dh-final root.
        p = self.pg7_rules["8.2.40"]["parameters"]
        for i in range(len(seq)-1):
            if seq[i]["symbol"] in p["preceding"] and seq[i+1]["symbol"] in p["targets"]:
                if root["identity"] == self.pg9_rules["8.2.40"]["parameters"]["excluded_lexical_id"]:
                    state["blocked"].append({"rule": "8.2.40", "reason": "adhaḥ excludes the identified dadhāti root",
                                            "lexical_id": root["identity"], "target_uid": seq[i+1]["uid"]})
                else:
                    change(i+1, p["replacement"], "8.2.40", "jhas_t_th_to_dh", seq[i]["uid"])
        if seq[-1]["symbol"] == "s":
            change(len(seq)-1, "r", "8.2.66", "pada_final_s_to_ru")
            state["history"][-1].update(ru_teaching="रुँ", retained_marker="u", marker_rules=["1.3.2", "1.3.9"])
            change(len(seq)-1, "ḥ", "8.3.15", "visarga_at_pause")
        p = self.pg7_rules["8.3.59"]["parameters"]
        for i in range(1, len(seq)):
            if seq[i]["owner"] == "ting" and seq[i]["symbol"] == "s" and seq[i-1]["symbol"] in p["adjacent_triggers"]:
                change(i, "ṣ", "8.3.59", "adjacent_ting_s_retroflexion", seq[i-1]["uid"])
        p = self.root_grammar.rules["8.4.53"]["parameters"]
        for i in range(len(seq)-2, -1, -1):
            if seq[i]["symbol"] in p["mapping"] and seq[i+1]["symbol"] in p["following"]:
                change(i, p["mapping"][seq[i]["symbol"]], "8.4.53", "jhal_jash_before_jhash", seq[i+1]["uid"])
        mapping = self.pg9_rules["8.4.54"]["parameters"]["mapping"]
        for i, sound in enumerate(seq):
            if sound["owner"] == abhyasa["id"] and sound["symbol"] in mapping:
                if consumed:
                    state["blocked"].append({"rule": "8.4.54", "reason": "original abhyāsa target already consumed in licensed 8.2.38 query",
                                            "original_targets": sorted(consumed), "target_uid": sound["uid"]})
                else:
                    change(i, mapping[sound["symbol"]], "8.4.54", "ordinary_abhyasa_jastva")
        p = self.pg7_rules["8.4.55"]["parameters"]
        for i in range(len(seq)-2, -1, -1):
            if seq[i]["symbol"] in p["mapping"] and seq[i+1]["symbol"] in p["following"]:
                change(i, p["mapping"][seq[i]["symbol"]], "8.4.55", "jhal_car_before_khar", seq[i+1]["uid"])
        state.update(status="PG9_LAT_PAUSE_READOUT", projection="".join(s["symbol"] for s in seq),
                     feedback_into_earlier_rules=False, optional_consonant_doubling="OUTSIDE_PROFILE")
        return state
