"""PG7: identified class-7 laṭ paths with one root and an owned internal affix.

The morpheme list expresses constituency; the separate layout expresses
pronunciation order. Only this bounded unprefixed, unaccented profile is closed.
Optional consonant doubling (8.4.46–47) is outside this spelling profile.
"""
from copy import deepcopy
import json
from pathlib import Path

from research.panini_grammar.non_thematic_lat.grammar import (
    Grammar as PG6Grammar, Request, VOWELS, sounds, unresolved, local_nati,
)
from research.panini_grammar.snam_lat.scope import ReviewedScope

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def ordered(state):
    """Project an owned infix without turning the root into two morphemes."""
    if "infix_layout" not in state:
        raise ValueError("A reviewed infix layout is required")
    root, vik, ting = state["morphemes"]
    layout = state["infix_layout"]
    if (layout["root_owner"], layout["infix_owner"]) != (root["id"], vik["id"]):
        raise ValueError("Layout names a different root or affix")
    anchors = [i for i, s in enumerate(root["visible"]) if s["uid"] == layout["after_uid"]]
    if len(anchors) != 1:
        raise ValueError("Infix anchor is absent or ambiguous")
    split = anchors[0] + 1
    spans = [(root, root["visible"][:split]), (vik, vik["visible"]),
             (root, root["visible"][split:]), (ting, ting["visible"])]
    result = [{**deepcopy(s), "owner": unit["id"]} for unit, span in spans for s in span]
    if len({s["uid"] for s in result}) != len(result):
        raise ValueError("The surface contains duplicate sound identities")
    return result


def collapse_targets(visible, parameters):
    """8.4.65 within the un-doubled profile: hal + jhar + savarṇa jhar."""
    classes = parameters["savarna_classes"]
    category = {s: i for i, group in enumerate(classes) for s in group}
    return [i for i in range(1, len(visible) - 1)
            if visible[i - 1]["kind"] == "consonant"
            and visible[i]["symbol"] in category
            and visible[i + 1]["symbol"] in category
            and category[visible[i]["symbol"]] == category[visible[i + 1]["symbol"]]]


class Grammar(PG6Grammar):
    def __init__(self, records, roots, review=None):
        super().__init__(records, roots)
        self.pg7 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.pg7_scope = ReviewedScope(records, self.review["scope_policies"],
                                      self.pg6["scope_policies"], self.pg7["scope_policies"])
        self.pg7_rules = {r["sid"]: self.pg7_scope.compile(r) for r in self.pg7["records"]}
        if len(self.pg7_rules) != len(self.pg7["records"]) or any(
                r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg7_rules.values()):
            raise ValueError("PG7 record has unresolved source terms")
        if any(r["sanskrit"] != self.pg7_scope.frame(r["sid"])["text"] for r in self.pg7["records"]):
            raise ValueError("PG7 sūtra wording differs from its source")
        additions = load("LEXICAL_ENTRIES.json")["entries"]
        source = {r["i"]: r for r in roots}
        self.snam_ids = {e["id"] for e in additions}
        if len(self.snam_ids) != len(additions):
            raise ValueError("Duplicate PG7 lexical identity")
        for entry in additions:
            if any(entry[k] != source[entry["id"]][k]
                   for k in ("baseindex", "aupadeshik", "gana", "pada", "artha")):
                raise ValueError("PG7 lexical identity differs from the pinned root")
            self.entries[entry["id"]] = deepcopy(entry)

    def _placement(self, state):
        root, vik, _ = state["morphemes"]
        if vik["identity"] != self.review["affixes"]["śnam"]["identity"] or not any(
                m["label"] == "m" for m in vik["marker_evidence"]["marker_units"]):
            raise ValueError("Internal placement requires the retained śnam m-it")
        vowels = [s for s in root["visible"] if s["symbol"] in VOWELS]
        if not vowels:
            raise ValueError("No root vowel licenses mit placement")
        state["infix_layout"] = {"root_owner": root["id"], "infix_owner": vik["id"],
            "after_uid": vowels[-1]["uid"], "rule": "1.1.47", "root_remains_one_constituent": True}
        state["host_constituent"] = {"id": "root-with-snam", "kind": "root_with_mit_member",
            "base_root": root["id"], "members": [root["id"], vik["id"]],
            "infix_is_host_member": True, "license": "1.1.47"}
        self._event(state, "1.1.47", "place_owned_mit_infix",
                    layout=state["infix_layout"])

    def _infix_ending(self, state, request):
        ting = state["morphemes"][-1]
        if request.pada != "A" or "jh" not in sounds(ting):
            self._ending(state, ting, request)
            return
        stem = [s for s in ordered(state) if s["owner"] != ting["id"]]
        index = max(i for i, s in enumerate(sounds(ting)) if s in VOWELS)
        self._replace(state, ting, index, len(ting["visible"]) - index, ["e"], "3.4.79", "ti_to_e",
                      selector_rule="1.1.64", lakara=state["lakara"]["id"])
        if sounds(ting)[0] != "jh" or stem[-1]["symbol"] == "a":
            raise ValueError("The PG7 jha contract requires immediate non-a aṅga adjacency")
        self._replace(state, ting, 0, 1, ["a", "t"], "7.1.5", "jh_to_at",
                      preceding_anga_final=stem[-1]["symbol"], preceding_owner=stem[-1]["owner"])
        self._block6(state, "7.1.5", "7.1.3")

    def derive(self, request):
        if not isinstance(request, Request) or request.lexical_id not in self.snam_ids:
            return super().derive(request)
        plans = self.plan(request)
        if plans["status"] != "REVIEWED_MORPHOLOGICAL_PLANS":
            return plans
        if request.prefixes:
            return unresolved("Prefixed śnam paths have not been reviewed", plans=plans)
        results = []
        for state in plans["branches"]:
            if state["choice"]["affix"] != "śnam":
                return unresolved("This PG7 lexical path requires śnam")
            if any(o["status"] not in {"WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME",
                                       "MIT_INFIX_PLACEMENT_NOT_EXECUTED"} for o in state["open_obligations"]):
                return unresolved("An independent plan obligation remains", plans=plans)
            root, vik, ting = state["morphemes"]
            self._placement(state)
            edges = [e for e in self.pg7["priority"] if e["winner"] == "3.1.78" and e["loser"] == "7.3.86"]
            if len(edges) != 1:
                raise ValueError("The local śnam-before-guṇa priority needs its reviewed evidence")
            if len(sounds(root)) >= 2 and sounds(root)[-2] in {"i", "u", "ṛ"} and ting["features"]["pit"]:
                state["blocked"].append({"rule": "7.3.86", "by": "3.1.78", "relation": deepcopy(edges[0]),
                    "reason": "śnam applies with or without guṇa; after insertion the old root vowel is not the aṅga upadhā"})
            # Delete only the root-owned n immediately following śnam. The
            # affix's own n and its retained identity are different objects.
            anchor = state["infix_layout"]["after_uid"]
            split = next(i for i, s in enumerate(root["visible"]) if s["uid"] == anchor) + 1
            if split < len(root["visible"]) and root["visible"][split]["symbol"] == "n":
                self._replace(state, root, split, 1, [], "6.4.23", "root_n_lopa_after_snam",
                              preceding_affix=vik["id"], infix_n_is_not_target=True)
            self._infix_ending(state, request)
            weak = ting["features"]["kit"] or ting["features"]["ngit"] or ting["features"]["ngitvat"]
            state["strength"] = {"reading": "weak" if weak else "strong", "cause": ting["id"],
                                 "pit": ting["features"]["pit"], "ngitvat": ting["features"]["ngitvat"]}
            if weak and ting["features"]["sarvadhatuka"]:
                if sounds(vik) != ["n", "a"]:
                    raise ValueError("6.4.111 requires the reviewed śnam a")
                self._replace(state, vik, 1, 1, [], "6.4.111", "snam_a_lopa", trigger=ting["id"])
            seq = [s["symbol"] for s in ordered(state) if s["owner"] != ting["id"]]
            state["anga_query"] = {"relative_to": ting["id"], "constituent": state["host_constituent"]["id"], "ordered_symbols": seq,
                                   "upadha": seq[-2], "root_is_not_the_whole_anga": True}
            if seq[-2] not in {"a", "n"}:
                raise ValueError("An unreviewed guṇa/strong-weak aṅga escaped the PG7 domain")
            state["fulfilled_obligations"] = [{"prior_obligation": deepcopy(o),
                "resolution": "executed by PG7 owned-infix derivation"} for o in state["open_obligations"]]
            state["open_obligations"] = []
            state.update(status="PRE_TRIPADI_INFIX_DERIVATION", projection="".join(s["symbol"] for s in ordered(state)))
            for query in self._readout_infix(state):
                results.append({"branch_id": state["choice"]["branch_id"] + ":" + query["option"],
                                "pre_tripadi": deepcopy(state), "readout": query, "form": query["projection"]})
        return {"status": "COMPLETE_IN_REVIEWED_SNAM_LAT_DOMAIN", "branches": results,
                "forms": sorted({b["form"] for b in results}),
                "word_validity": "SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout_infix(self, original):
        if original.get("status") != "PRE_TRIPADI_INFIX_DERIVATION":
            raise ValueError("An owned-infix source is required; a readout cannot feed back")
        state = {"visible": ordered(original), "history": [], "blocked": [], "visibility_queries": []}
        seq = state["visible"]

        def change(i, substitute, rule, cause=None):
            before = deepcopy(seq[i])
            if before["symbol"] == substitute:
                return
            event = self._event(state, rule, "ordered_phonetic_replacement", before=before, cause_uid=cause)
            seq[i] = {**before, "uid": f"pg7:readout:{event['index']}", "symbol": substitute,
                      "kind": "ayogavaha" if substitute in {"ṃ", "ḥ"} else "vowel" if substitute in VOWELS else "consonant",
                      "replaces": [before["uid"]], "introduced_by": rule}
            event["after"] = deepcopy(seq[i])

        for sid in ("8.2.30", "8.2.40", "8.2.41"):
            p = self.pg7_rules[sid]["parameters"]
            for i in range(len(seq) - 1):
                a, b = seq[i]["symbol"], seq[i + 1]["symbol"]
                if sid == "8.2.40":
                    if a in p["preceding"] and b in p["targets"]:
                        change(i + 1, p["replacement"], sid, seq[i]["uid"])
                elif a in p["mapping"] and b in p["following"]:
                    change(i, p["mapping"][a], sid, seq[i + 1]["uid"])
        if seq[-1]["symbol"] == "s":
            change(len(seq) - 1, "r", "8.2.66")
            state["history"][-1].update(ru_teaching="रुँ", retained_marker="u", marker_rules=["1.3.2", "1.3.9"])
            change(len(seq) - 1, "ḥ", "8.3.15")
        if any(e["rule"] == "6.4.111" for e in original["history"]):
            state["visibility_queries"].append({"query": "8.3.24/8.4.58", "license": "1.1.58",
                "deleted_snam_a_is_not_restored": True, "evidence": "Siddhāntakaumudī/Bālamanoramā 3.1.78"})
        p = self.root_grammar.rules["8.3.24"]["parameters"]
        for i in range(len(seq) - 1):
            if seq[i]["symbol"] in p["targets"] and seq[i + 1]["symbol"] in p["following"]:
                change(i, p["replacement"], "8.3.24", seq[i + 1]["uid"])
        p = self.pg7_rules["8.3.59"]["parameters"]
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
        for sid in ("8.4.53", "8.4.55", "8.4.58"):
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
            raise ValueError("Multiple interacting collapse sites are outside PG7")
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
            variant.update(status="SNAM_LAT_PAUSE_READOUT", projection="".join(s["symbol"] for s in variant["visible"]),
                           feedback_into_earlier_rules=False, optional_consonant_doubling="OUTSIDE_PROFILE")
            outputs.append(variant)
        return outputs
