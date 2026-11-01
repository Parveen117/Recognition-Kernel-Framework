"""PG8: sense-selected bhuj, nested im in tṛh, and ad/as present paths.

This extends the linguistic adapter, not the native operator engine. The
source lexicon, deleted units, owned sounds and each visibility exception
remain explicit. No generated form table is read by this module.
"""
from copy import deepcopy
from dataclasses import replace
import json
from pathlib import Path

from research.panini_grammar.snam_lat.grammar import (
    Grammar as PG7Grammar, Request, VOWELS, sounds, unresolved, local_nati,
    collapse_targets,
)
from research.panini_grammar.verification.marker_review import tokenize

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def ordered(state):
    """Order root/śnam/im without splitting the root's morphological identity."""
    units = state["morphemes"]
    if "infix_layout" not in state:
        spans = [(u, u["visible"]) for u in units]
    else:
        root, vik, ting = units[0], units[1], units[-1]
        layout = state["infix_layout"]
        if (layout["root_owner"], layout["infix_owner"]) != (root["id"], vik["id"]):
            raise ValueError("Infix ownership changed")
        anchors = [i for i, s in enumerate(root["visible"]) if s["uid"] == layout["after_uid"]]
        if len(anchors) != 1:
            raise ValueError("The root infix anchor is absent or ambiguous")
        split = anchors[0] + 1
        spans = [(root, root["visible"][:split]), (vik, vik["visible"])]
        if len(units) == 4:
            augment = units[2]
            if augment["id"] != "augment:im" or not state.get("augment_layout"):
                raise ValueError("An unlicensed nested member entered the layout")
            spans.append((augment, augment["visible"]))
        elif len(units) != 3:
            raise ValueError("Only the reviewed single nested augment is admitted")
        spans += [(root, root["visible"][split:]), (ting, ting["visible"])]
    out = [{**deepcopy(s), "owner": unit["id"]} for unit, span in spans for s in span]
    if len({s["uid"] for s in out}) != len(out):
        raise ValueError("Duplicate visible sound identity")
    return out


class Grammar(PG7Grammar):
    def __init__(self, records, roots, review=None):
        super().__init__(records, roots)
        self.pg8 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.pg8_rules = {r["sid"]: self.pg7_scope.compile(r) for r in self.pg8["records"]}
        if len(self.pg8_rules) != len(self.pg8["records"]) or any(
                r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg8_rules.values()):
            raise ValueError("PG8 record lost a source-bound term")
        if any(r["sanskrit"] != self.pg7_scope.frame(r["sid"])["text"] for r in self.pg8["records"]):
            raise ValueError("PG8 Sanskrit wording differs from the source")
        source = {r["i"]: r for r in roots}
        additions = load("LEXICAL_ENTRIES.json")["entries"]
        self.pg8_ids = {e["id"] for e in additions}
        if len(self.pg8_ids) != len(additions):
            raise ValueError("Duplicate PG8 identity")
        for e in additions:
            if any(e[k] != source[e["id"]][k] for k in ("baseindex", "aupadeshik", "gana", "pada", "artha")):
                raise ValueError("PG8 lexical identity differs from its pinned source")
            self.entries[e["id"]] = deepcopy(e)
        self.snam_ids.add("1070017")  # bhuj reuses the reviewed PG7 operations.

    def _guard(self, request):
        if isinstance(request, Request) and request.lexical_id == "1070017":
            selected = self.pg8_rules["1.3.66"]["parameters"]["sense_pada"]
            if request.sense not in selected or request.pada != selected[request.sense]:
                return unresolved("Bhuj needs a reviewed disambiguated sense and its licensed pada")
            # Validate the common profile without changing the source row or
            # the actual semantic request used in the derivation.
            return super()._guard(replace(request, sense=self.entries[request.lexical_id]["artha"], pada="P"))
        return super()._guard(request)

    def plan(self, request):
        result = super().plan(request)
        if result["status"] == "REVIEWED_MORPHOLOGICAL_PLANS" and request.lexical_id == "1070017":
            for state in result["branches"]:
                self._event(state, "1.3.66", "sense_conditioned_pada",
                            sense=request.sense, pada=request.pada,
                            outcome="atmanepada_prescribed" if request.pada == "A" else "anavana_condition_false",
                            source_pada=self.entries[request.lexical_id]["pada"],
                            contextual_license_remains_supplied=True)
        return result

    def _im(self, state):
        root, vik, ting = state["morphemes"]
        p = self.pg8_rules["7.3.92"]["parameters"]
        if root["identity"] != p["lexical_id"] or sounds(vik) != ["n", "a"]:
            raise ValueError("im requires tṛh with śnam already present")
        if not (ting["features"]["sarvadhatuka"] and ting["features"]["pit"]
                and sounds(ting)[0] not in VOWELS):
            return False
        original = [{"uid": f"augment:im:source:{i}", "symbol": s.symbol,
                     "kind": "vowel" if s.symbol in VOWELS else "consonant"}
                    for i, s in enumerate(tokenize(p["teaching"]))]
        if [s["symbol"] for s in original] != ["i", "m"]:
            raise ValueError("Only the reviewed im teaching unit is parsed here")
        unit = {"id": "augment:im", "identity": "im:7.3.92", "kind": "augment",
                "teaching": p["teaching"], "original": original,
                "visible": deepcopy(original[:1]),
                "marker_evidence": {"marker_units": [{"label": "m", "uid": original[1]["uid"], "rule": "1.3.3"}]},
                "features": {"mit": True, "pratyaya": False}}
        self._event(state, "7.3.92", "im_prescription_after_snam", trigger=ting["id"],
                    host=state["host_constituent"]["id"], original=original)
        self._event(state, "1.3.3", "augment_final_m_it", target=original[1])
        self._event(state, "1.3.9", "augment_marker_lopa", removed=original[1], identity_retained=True)
        vowels = [s for s in ordered(state) if s["owner"] != ting["id"] and s["symbol"] in VOWELS]
        if vowels[-1]["uid"] != vik["visible"][-1]["uid"]:
            raise ValueError("The last vowel of the assembled aṅga must be śnam's a")
        state["augment_layout"] = {"owner": unit["id"], "after_source_uid": vowels[-1]["uid"],
                                   "host": state["host_constituent"]["id"], "rule": "1.1.47"}
        state["morphemes"].insert(2, unit)
        state["host_constituent"]["members"].append(unit["id"])
        self._event(state, "1.1.47", "nested_mit_after_host_last_vowel", layout=state["augment_layout"])
        # a + i gives e at an internal seam. Both source UIDs survive in the
        # ekādeśa event; its new surface sound is owned by the augment.
        self._join(state, vik, unit, self.pg8_rules["6.1.87"]["parameters"]["a_i_replacement"], "6.1.87")
        return True

    def derive(self, request):
        if not isinstance(request, Request) or request.lexical_id not in {"1070018", "1020001", "1020060"}:
            return super().derive(request)
        plans = self.plan(request)
        if plans["status"] != "REVIEWED_MORPHOLOGICAL_PLANS":
            return plans
        if request.prefixes:
            return unresolved("Prefixed PG8 paths have not been reviewed")
        results = []
        for state in plans["branches"]:
            if any(o["status"] not in {"WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME",
                                      "MIT_INFIX_PLACEMENT_NOT_EXECUTED"} for o in state["open_obligations"]):
                return unresolved("An independent plan obligation remains", plans=plans)
            root, vik, ting = state["morphemes"]
            weak = ting["features"]["kit"] or ting["features"]["ngit"] or ting["features"]["ngitvat"]
            state["strength"] = {"reading": "weak" if weak else "strong", "cause": ting["id"],
                                 "pit": ting["features"]["pit"], "ngitvat": ting["features"]["ngitvat"]}
            self._ending(state, ting, request)
            if request.lexical_id == "1070018":
                if state["choice"]["affix"] != "śnam":
                    raise ValueError("tṛh requires the retained śnam choice")
                self._placement(state)
                edges = [e for e in self.pg7["priority"] if e["winner"] == "3.1.78" and e["loser"] == "7.3.86"]
                if len(edges) != 1:
                    raise ValueError("The śnam-before-guṇa relation is absent")
                state["blocked"].append({"rule": "7.3.86", "by": "3.1.78", "relation": deepcopy(edges[0])})
                if weak:
                    self._replace(state, vik, 1, 1, [], "6.4.111", "snam_a_lopa", trigger=ting["id"])
                else:
                    self._im(state)
            else:
                if vik.get("whole_affix_deletion") != {"kind": "luk", "rule": "2.4.72"}:
                    raise ValueError("adādi requires retained śap-luk")
                self._guna(state, [root, vik], ting)
                if request.lexical_id == "1020060":
                    if weak:
                        self._replace(state, root, 0, 1, [], "6.4.111", "as_a_lopa", trigger=ting["id"])
                    if sounds(ting)[0] == "s":
                        self._replace(state, root, len(root["visible"])-1, 1, [], "7.4.50", "as_s_lopa_before_s", trigger=ting["id"])
            state["fulfilled_obligations"] = [{"prior_obligation": deepcopy(o), "resolution": "PG8 bounded word path"}
                                               for o in state["open_obligations"]]
            state["open_obligations"] = []
            state.update(status="PRE_TRIPADI_PG8_DERIVATION", projection="".join(s["symbol"] for s in ordered(state)))
            for query in self._readout8(state):
                results.append({"branch_id": state["choice"]["branch_id"]+":"+query["option"],
                                "pre_tripadi": deepcopy(state), "readout": query, "form": query["projection"]})
        return {"status": "COMPLETE_IN_REVIEWED_EXCEPTION_LAT_DOMAIN", "branches": results,
                "forms": sorted({b["form"] for b in results}),
                "word_validity": "SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout_infix(self, original):
        # Older class-7 requests keep the frozen PG7 path. Only the newly
        # admitted bhuj routes through this stage's late view.
        if original["request"]["lexical_id"] == "1070017":
            return self._readout8(original)
        return super()._readout_infix(original)

    def _readout8(self, original):
        if original.get("status") not in {"PRE_TRIPADI_INFIX_DERIVATION", "PRE_TRIPADI_PG8_DERIVATION"}:
            raise ValueError("A retained morphological source is required; a readout cannot feed back")
        if original["request"]["lexical_id"] not in self.pg8_ids:
            raise ValueError("The PG8 phonetic profile requires an admitted lexical identity")
        state = {"visible": ordered(original), "history": [], "blocked": [], "visibility_queries": []}
        seq = state["visible"]

        def change(i, substitute, rule, cause=None):
            before = deepcopy(seq[i])
            if before["symbol"] == substitute:
                return
            event = self._event(state, rule, "ordered_phonetic_replacement", before=before, cause_uid=cause)
            seq[i] = {**before, "uid": f"pg8:readout:{event['index']}", "symbol": substitute,
                      "kind": "ayogavaha" if substitute in {"ṃ", "ḥ"} else "vowel" if substitute in VOWELS else "consonant",
                      "replaces": [before["uid"]], "introduced_by": rule}
            event["after"] = deepcopy(seq[i])

        for sid in ("8.2.30", "8.2.31", "8.2.40", "8.2.41"):
            p = (self.pg8_rules if sid == "8.2.31" else self.pg7_rules)[sid]["parameters"]
            for i in range(len(seq) - 1):
                a, b = seq[i]["symbol"], seq[i + 1]["symbol"]
                if sid == "8.2.40":
                    if a in p["preceding"] and b in p["targets"]:
                        change(i + 1, p["replacement"], sid, seq[i]["uid"])
                elif a in p["mapping"] and b in p["following"]:
                    change(i, p["mapping"][a], sid, seq[i + 1]["uid"])
        if original["request"]["lexical_id"] == "1070018":
            edges = self.pg8["visibility_exceptions"]
            expected = {"query": "8.3.13", "visible_rule": "8.4.41", "target_pair": ["ḍh", "dh"]}
            if len(edges) != 1 or any(edges[0].get(k) != v for k, v in expected.items()):
                raise ValueError("The reviewed ḍh-lopa visibility exception is absent")
            # Kāśikā 8.3.13 explicitly admits ṣṭutva here despite 8.2.1.
            for i in range(len(seq)-2, -1, -1):
                if [seq[i]["symbol"], seq[i+1]["symbol"]] == edges[0]["target_pair"]:
                    state["visibility_queries"].append({**deepcopy(expected),
                        "target_uid": seq[i]["uid"], "cause_uid": seq[i+1]["uid"],
                        "license": deepcopy(edges[0]["evidence"]), "global_tripadi_reversal": False})
                    change(i+1, "ḍh", "8.4.41", seq[i]["uid"])
                    self._event(state, "8.3.13", "dh_lopa_with_local_stutva_visibility",
                                target=deepcopy(seq[i]), cause_uid=seq[i+1]["uid"])
                    del seq[i]
        if seq[-1]["symbol"] == "s":
            change(len(seq) - 1, "r", "8.2.66")
            state["history"][-1].update(ru_teaching="रुँ", retained_marker="u", marker_rules=["1.3.2", "1.3.9"])
            change(len(seq) - 1, "ḥ", "8.3.15")
        if any(e["effect"] == "snam_a_lopa" for e in original["history"]):
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
            variant.update(status="PG8_LAT_PAUSE_READOUT", projection="".join(s["symbol"] for s in variant["visible"]),
                           feedback_into_earlier_rules=False, optional_consonant_doubling="OUTSIDE_PROFILE")
            outputs.append(variant)
        return outputs
