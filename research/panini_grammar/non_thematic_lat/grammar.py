"""PG6: strong/weak śnu, u and śnā laṭ paths on ten reviewed lexemes.

Extends the frozen PG5 linguistic adapter. It is not an unrestricted
ābhīya, sthānivad, ṇatva or Sanskrit-validity engine.
"""
from copy import deepcopy
import json
from pathlib import Path

from research.panini_grammar.vikarana_lat.grammar import (
    Grammar as PG5Grammar, Request, VOWELS, load as load_pg5, sounds, surface, unresolved,
)
from research.panini_grammar.non_thematic_lat.scope import ReviewedScope

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def u_context(state):
    """Read the entire aṅga before tiṅ, retaining the vikaraṇa's ownership."""
    units = state["morphemes"][:-1]
    seq = [s["symbol"] for u in units for s in u["visible"]]
    if not units[-1]["visible"] or sounds(units[-1])[-1] != "u":
        return None
    cluster = 0
    for symbol in reversed(seq[:-1]):
        if symbol in VOWELS:
            break
        cluster += 1
    return {"multiple_vowels": sum(s in VOWELS for s in seq) > 1,
            "cluster_before_u": cluster >= 2, "vowel_count": sum(s in VOWELS for s in seq),
            "affix_owner": units[-1]["id"], "target_uid": units[-1]["visible"][-1]["uid"]}


def local_nati(seq, index, *, same_pada, pada_final, exceptions_reviewed):
    """Adjacent r/ṛ/ṣ or an aṭ-only gap, in a reviewed non-exception context."""
    if not all(isinstance(x, bool) for x in (same_pada, pada_final, exceptions_reviewed)):
        return unresolved("Ṇatva needs explicit boundaries and exception review")
    if not 0 <= index < len(seq) or seq[index] != "n":
        return {"status": "INAPPLICABLE"}
    if not same_pada:
        return {"status": "INAPPLICABLE", "reason": "different padas"}
    if pada_final:
        return {"status": "BLOCKED", "rule": "8.4.37"}
    if not exceptions_reviewed:
        return unresolved("Full ṇatva prohibitions and lexical exceptions are not implemented")
    for j in range(index - 1, -1, -1):
        if seq[j] in {"r", "ṛ", "ṝ", "ṣ"}:
            return {"status": "LICENSED", "rule": "8.4.1" if j == index - 1 else "8.4.2",
                    "trigger_index": j, "replacement": "ṇ",
                    "supplement": "Kāśikā 8.4.1 ṛvarṇa reading" if seq[j] in {"ṛ", "ṝ"} else None}
        if seq[j] not in VOWELS | {"h", "y", "v"}:
            return {"status": "OUTSIDE_LOCAL_TRIGGER_WINDOW"}
    return {"status": "INAPPLICABLE"}


class Grammar(PG5Grammar):
    def __init__(self, records, roots, review=None):
        self.pg6 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        additions = load("LEXICAL_ENTRIES.json")["entries"]
        merged = {e["id"]: e for e in load_pg5("LEXICAL_ENTRIES.json")["entries"]}
        merged.update({e["id"]: e for e in additions})
        super().__init__(records, roots, lexical=list(merged.values()))
        self.non_thematic_ids = {e["id"] for e in additions}
        self.pg6_scope = ReviewedScope(records, self.review["scope_policies"], self.pg6["scope_policies"])
        self.pg6_rules = {r["sid"]: self.pg6_scope.compile(r) for r in self.pg6["records"]}
        if len(self.pg6_rules) != len(self.pg6["records"]) or any(
                r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg6_rules.values()):
            raise ValueError("PG6 records do not bind the reviewed source scopes")
        if any(r["sanskrit"] != self.pg6_scope.frame(r["sid"])["text"] for r in self.pg6["records"]):
            raise ValueError("PG6 Sanskrit text differs from the reviewed reading")

    def _relation6(self, winner, loser):
        edges = [e for e in self.pg6["priority"] if (e["winner"], e["loser"]) == (winner, loser)]
        if len(edges) != 1:
            raise ValueError("Missing or ambiguous PG6 local priority relation")
        return deepcopy(edges[0])

    def _block6(self, state, winner, loser, **data):
        state["blocked"].append({"rule": loser, "by": winner,
                                 "relation": self._relation6(winner, loser), **deepcopy(data)})

    def _non_a_ending(self, state, ting, request):
        if request.pada != "A" or not any(s == "jh" for s in sounds(ting)):
            self._ending(state, ting, request)  # reuse PG5 for every unaffected ending
            return
        # 3.4.79 depends on the ṭit lakāra, before testing the stem junction.
        index = max(i for i, s in enumerate(sounds(ting)) if s in VOWELS)
        self._replace(state, ting, index, len(ting["visible"]) - index, ["e"], "3.4.79", "ti_to_e",
                      selector_rule="1.1.64", lakara=state["lakara"]["id"], tit_comes_from_lakara=True)
        anga_final = next(u for u in reversed(state["morphemes"][:-1]) if u["visible"])["visible"][-1]["symbol"]
        for index in reversed([i for i, s in enumerate(sounds(ting)) if s == "jh"]):
            # The jh itself must adjoin the non-short-a aṅga. A preceding
            # augment within the affix cannot be silently skipped.
            if index == 0 and anga_final != "a":
                self._replace(state, ting, index, 1, ["a", "t"], "7.1.5", "jh_to_at",
                              preceding_anga_final=anga_final)
                self._block6(state, "7.1.5", "7.1.3")
            else:
                self._replace(state, ting, index, 1, ["a", "n", "t"], "7.1.3", "jh_to_ant")

    def derive(self, request):
        if not isinstance(request, Request) or request.lexical_id not in self.non_thematic_ids:
            return super().derive(request)
        plans = self.plan(request)
        if plans["status"] != "REVIEWED_MORPHOLOGICAL_PLANS":
            return plans
        if request.prefixes:
            return unresolved("Complete prefixed non-thematic paths have not been reviewed", plans=plans)
        entry = self.entries[request.lexical_id]
        results = []
        for state in plans["branches"]:
            root, vik, ting = state["morphemes"]
            if state["choice"]["affix"] not in {"śnu", "u", "śnā"}:
                return unresolved("This selected vikaraṇa is outside PG6")
            remaining = [o for o in state["open_obligations"]
                         if o.get("status") != "WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME"
                         and not (entry.get("coupled_root_replacement") and o.get("rule") == "3.1.74")]
            if remaining:
                return unresolved("An independent plan obligation remains", obligations=remaining)
            state["fulfilled_obligations"] = [{"prior_obligation": deepcopy(o),
                "resolution": "executed by this reviewed PG6 derivation"} for o in state["open_obligations"]]
            state["open_obligations"] = []
            if entry.get("coupled_root_replacement"):
                if sounds(root) != ["ś", "r", "u"]:
                    raise ValueError("Śru witness no longer matches the coupled substitution")
                self._replace(state, root, 0, 3, ["ś", "ṛ"], "3.1.74", "coupled_sru_to_sr",
                              licensed_with=vik["id"], original_lexical_identity=entry["id"])
            self._guna(state, [root], vik)
            if entry.get("pvadi_shortening"):
                if sounds(root)[-1] != "ū" or not vik["features"]["sit"]:
                    raise ValueError("Reviewed pū/lū śit shortening guard changed")
                self._replace(state, root, len(root["visible"]) - 1, 1, ["u"], "7.3.80", "identified_pvadi_shortening", trigger=vik["id"])
            self._non_a_ending(state, ting, request)
            weak = ting["features"]["kit"] or ting["features"]["ngit"] or ting["features"]["ngitvat"]
            state["strength"] = {"reading": "weak" if weak else "strong", "cause": ting["id"],
                                 "pit": ting["features"]["pit"], "ngitvat": ting["features"]["ngitvat"]}
            self._guna(state, [root, vik], ting)
            if weak and entry.get("weak_kr"):
                if sounds(root) != ["k", "a", "r"]:
                    raise ValueError("The reviewed kṛ weak path requires the retained kar stage")
                self._replace(state, root, 1, 1, ["u"], "6.4.110", "weak_kr_a_to_u", trigger=ting["id"], u_affix=vik["id"])
                state["blocked"].append({"rule": "7.3.86", "by": "6.4.110-tpara-reading",
                    "reason": "Kāśikā's short-u prescription explicitly prevents renewed laghūpadha guṇa here"})
            if weak and state["choice"]["affix"] == "śnā":
                if sounds(vik) != ["n", "ā"]:
                    raise ValueError("The śnā target must be the original long ā")
                if sounds(ting)[0] in VOWELS:
                    self._replace(state, vik, 1, 1, [], "6.4.112", "sna_a_lopa_before_vowel", trigger=ting["id"])
                else:
                    self._replace(state, vik, 1, 1, ["ī"], "6.4.113", "sna_a_to_long_i_before_hal", trigger=ting["id"], ghu=False)
                    self._block6(state, "6.4.113", "6.4.112")
            alternatives = [(state, "unchanged")]
            context = u_context(state)
            if context and sounds(ting)[0] in {"m", "v"} and weak:
                if entry.get("weak_kr"):
                    self._block6(state, "6.4.108", "6.4.107")
                    self._replace(state, vik, len(vik["visible"]) - 1, 1, [], "6.4.108", "mandatory_final_affix_u_lopa", context=context)
                    alternatives = [(state, "u-lopa-mandatory")]
                elif not context["cluster_before_u"]:
                    kept, deleted = deepcopy(state), deepcopy(state)
                    self._event(kept, "6.4.107", "optional_u_retained", context=context)
                    target = deleted["morphemes"][-2]
                    self._replace(deleted, target, len(target["visible"]) - 1, 1, [], "6.4.107", "optional_final_affix_u_lopa", context=context)
                    alternatives = [(kept, "u-retained"), (deleted, "u-lopa-optional")]
                else:
                    state["blocked"].append({"rule": "6.4.107", "reason": "u is preceded by a consonant cluster", "context": context})
            for current, option in alternatives:
                root, vik, ting = current["morphemes"]
                context = u_context(current)
                if context and sounds(ting)[0] in VOWELS:
                    if current["choice"]["affix"] == "śnu":
                        if context["multiple_vowels"] and not context["cluster_before_u"] and ting["features"]["sarvadhatuka"]:
                            rule, substitute = "6.4.87", ["v"]
                            self._block6(current, rule, "6.4.77", context=context)
                        else:
                            rule, substitute = "6.4.77", ["u", "v"]
                            self._block6(current, rule, "6.1.77", context=context)
                    else:
                        rule, substitute = "6.1.77", ["v"]
                    self._replace(current, vik, len(vik["visible"]) - 1, 1, substitute, rule, "u_vowel_junction", context=context)
                current.update(status="PRE_TRIPADI_DERIVATION", projection=surface(current), pg6_option=option)
                query = self._readout_non_thematic(current, entry)
                results.append({"branch_id": current["choice"]["branch_id"] + ":" + option,
                                "pre_tripadi": current, "readout": query, "form": query["projection"]})
        return {"status": "COMPLETE_IN_REVIEWED_NON_THEMATIC_LAT_DOMAIN", "branches": results,
                "forms": sorted({b["form"] for b in results}),
                "word_validity": "SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout_non_thematic(self, original, entry):
        if original.get("status") != "PRE_TRIPADI_DERIVATION":
            raise ValueError("A retained pre-Tripādī derivation is required")
        state = deepcopy(original)
        state["history"], state["blocked"] = [], []
        root, vik, ting = state["morphemes"]
        queries = []
        if sounds(ting)[-1] == "s":
            self._replace(state, ting, len(ting["visible"]) - 1, 1, ["r"], "8.2.66", "pada_final_s_to_ru",
                          ru_teaching="रुँ", retained_marker="u", marker_rules=["1.3.2", "1.3.9"])
        following = next(u for u in state["morphemes"][1:] if u["visible"])
        if entry.get("weak_kr") and sounds(root) == ["k", "u", "r"] and sounds(following)[0] not in VOWELS:
            deleted = any(e["rule"] == "6.4.108" for e in original["history"])
            queries.append({"query": "8.2.77", "visible_root": "kur", "current_following": sounds(following)[0],
                            "deleted_u_is_not_restored": deleted, "license": "1.1.58" if deleted else "current local view",
                            "evidence": "Kāśikā 6.4.108", "outcome": "BLOCKED_BY_8.2.79"})
            self._block6(state, "8.2.79", "8.2.77")
        if sounds(ting)[-1] == "r":
            self._replace(state, ting, len(ting["visible"]) - 1, 1, ["ḥ"], "8.3.15", "visarga_at_pause")

        def refs():
            return [(unit, i) for unit in state["morphemes"] for i in range(len(unit["visible"]))]

        # Run the early nasal operation with PG4's already reviewed parameters.
        # A later 8.4.58 n must not be visible to the intervening ṇatva operation.
        places = refs()
        params = self.root_grammar.rules["8.3.24"]["parameters"]
        for (unit, i), (next_unit, j) in zip(places, places[1:]):
            if unit["visible"][i]["symbol"] in params["targets"] and next_unit["visible"][j]["symbol"] in params["following"]:
                self._replace(state, unit, i, 1, [params["replacement"]], "8.3.24", "pre_nati_anusvara",
                              cause_uid=next_unit["visible"][j]["uid"])
        # Bounded adjacent-affix ṣatva. No general intervening-num/visarga/śar domain.
        places = refs()
        for index, (unit, i) in enumerate(places):
            if index and unit is ting and unit["visible"][i]["symbol"] == "s":
                previous, j = places[index - 1]
                if previous["visible"][j]["symbol"] in {"i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "e", "o", "ai", "au"}:
                    self._replace(state, unit, i, 1, ["ṣ"], "8.3.59", "adjacent_ting_s_retroflexion", cause_uid=previous["visible"][j]["uid"])
        places = refs()
        for index, (unit, i) in enumerate(places):
            seq = [u["visible"][j]["symbol"] for u, j in places]
            choice = local_nati(seq, index, same_pada=True, pada_final=index == len(places) - 1, exceptions_reviewed=True)
            if choice["status"] == "LICENSED":
                cause, j = places[choice["trigger_index"]]
                self._replace(state, unit, i, 1, [choice["replacement"]], choice["rule"], "local_nati",
                              cause_uid=cause["visible"][j]["uid"], supplemental_reading=choice["supplement"])
        visible = [deepcopy(u["visible"][i]) for u, i in refs()]
        span = {"status": "SUPPLIED_PHONETIC_SPAN", "visible": visible, "original": deepcopy(visible), "history": []}
        tail = self.root_grammar.phonetic(span, samhita=True, pada_final_uids=[visible[-1]["uid"]], following_unit_identities={})
        if tail["status"] != "LOCAL_PHONETIC_QUERY" or any(e["rule"] in {"8.2.78", "8.3.24"} for e in tail["history"]):
            raise ValueError("PG4 tail would re-enter an earlier phase or leave an unresolved query")
        return {"status": "NON_THEMATIC_LAT_PAUSE_READOUT", "projection": tail["projection"], "visible": tail["visible"],
                "history": state["history"] + tail["history"], "blocked": state["blocked"] + tail["blocked"],
                "visibility_queries": queries, "feedback_into_earlier_rules": False}
