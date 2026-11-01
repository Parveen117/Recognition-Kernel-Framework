"""PG5: reviewed vikaraṇa choices and complete bounded classical laṭ paths.

This is a linguistic adapter over PG3/PG4, not a second operator engine.
The input includes lexical identity, sense and a contextual pada license.
No expected form, headword or external conjugator is consulted here.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, dataclass
import json
from pathlib import Path

from research.panini_grammar.root_progression.root_preprocess import RootInput
from research.panini_grammar.scoped_derivations.derive import Grammar as RootGrammar
from research.panini_grammar.verification.marker_review import designate
from research.panini_grammar.vikarana_lat.scope import ReviewedScope

HERE = Path(__file__).resolve().parent
VOWELS = {"a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "e", "ai", "o", "au"}
GUNA = {"i": ["e"], "ī": ["e"], "u": ["o"], "ū": ["o"], "ṛ": ["a", "r"], "ṝ": ["a", "r"]}
ENDING_NAMES = {"P": ["tip", "tas", "jhi", "sip", "thas", "tha", "mip", "vas", "mas"],
                "A": ["ta", "ātām", "jha", "thās", "āthām", "dhvam", "iṭ", "vahi", "mahiṅ"]}


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


@dataclass(frozen=True)
class Request:
    lexical_id: str
    sense: str
    pada: str
    person: str
    number: str
    pada_licensed: bool | None
    prefixes: tuple[str, ...] | None = ()
    tense: str = "present"
    voice: str = "kartari"
    register: str = "classical"
    samhita: bool | None = True
    at_pause: bool | None = True


def unresolved(reason, **extra):
    return {"status": "UNRESOLVED", "reason": reason, **extra}


def sounds(unit):
    return [s["symbol"] for s in unit["visible"]]


def surface(state):
    return "".join(s["symbol"] for unit in state["morphemes"] for s in unit["visible"])


class Grammar:
    def __init__(self, records, roots, review=None, lexical=None):
        self.review = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.scope = ReviewedScope(records, self.review["scope_policies"])
        if any(r["sanskrit"] != self.scope.frame(r["sid"])["text"] for r in self.review["records"]):
            raise ValueError("Sūtra text differs from the reviewed record")
        self.rules = {r["sid"]: self.scope.compile(r) for r in self.review["records"]}
        if len(self.rules) != len(self.review["records"]) or any(
                r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.rules.values()):
            raise ValueError("PG5 rule records do not bind the reviewed source frames")
        self.root_grammar = RootGrammar(records)
        self.markers = self.root_grammar.markers
        entries = load("LEXICAL_ENTRIES.json")["entries"] if lexical is None else deepcopy(lexical)
        self.entries = {e["id"]: e for e in entries}
        source = {r["i"]: r for r in roots}
        if len(self.entries) != len(entries) or len(source) != len(roots):
            raise ValueError("Duplicate lexical identity")
        for entry in entries:
            row = source[entry["id"]]
            for key in ("baseindex", "aupadeshik", "gana", "pada", "artha"):
                if entry[key] != row[key]:
                    raise ValueError(f"Lexical witness differs: {entry['id']}:{key}")

    def _priority(self, winner, loser):
        matches = [edge for edge in self.review["priority"] if edge["winner"] == winner
                   and loser in edge["loser"].split("/")]
        if len(matches) != 1:
            raise ValueError(f"No unique reviewed exception relation: {winner} over {loser}")
        return deepcopy(matches[0])

    def _guard(self, request):
        if not isinstance(request, Request):
            return unresolved("A typed grammatical Request is required")
        if request.lexical_id not in self.entries:
            return unresolved("Lexical identity has not been reviewed")
        entry = self.entries[request.lexical_id]
        if request.sense != entry["artha"]:
            return unresolved("Sense is not the admitted lexical sense")
        if request.tense != "present" or request.voice != "kartari" or request.register != "classical":
            return unresolved("Only classical present kartari laṭ is admitted")
        if request.pada not in ENDING_NAMES or request.pada_licensed is not True:
            return unresolved("Contextual pada license must be supplied; it is not inferred from spelling")
        if entry["pada"] not in {request.pada, "U"}:
            return unresolved("Chosen pada is outside the admitted lexical witness")
        order = self.review["ending_order"]
        if request.person not in order["persons"] or request.number not in order["numbers"]:
            return unresolved("Person or number is outside the three by three tiṅ inventory")
        if not isinstance(request.prefixes, tuple) or any(p not in {"sam", "pra", "ā"} for p in request.prefixes):
            return unresolved("Prefix identities/status have not been supplied in the reviewed domain")
        if request.samhita is not True or request.at_pause is not True:
            return unresolved("The complete-form profile requires saṃhitā internally and pause after the word")
        return None

    def select(self, request):
        """Resolve reviewed choices; selection alone never certifies a word."""
        error = self._guard(request)
        if error:
            return error
        entry = self.entries[request.lexical_id]
        default = deepcopy(self.review["class_prescriptions"][entry["gana"]])
        choices = [default]
        exception = entry.get("selection_exception")
        if exception == "3.1.70":
            # For divādi members the optional śyan has śap as the other branch.
            fallback = default if entry["gana"] != "4" else {"affix": "śap", "rule": "3.1.68"}
            choices = [{"affix": "śyan", "rule": exception}, fallback]
        elif exception == "3.1.71/72":
            if not request.prefixes or request.prefixes == ("sam",):
                exception = "3.1.71" if not request.prefixes else "3.1.72"
                choices = [{"affix": "śyan", "rule": exception}, {"affix": "śap", "rule": "3.1.68"}]
        elif exception == "3.1.74":
            choices = [{"affix": "śnu", "rule": exception,
                        "coupled_action": {"target": "whole_sru", "substitute": "śṛ"}}]
        elif exception in {"3.1.75", "3.1.76"}:
            choices = [{"affix": "śnu", "rule": exception}, default]
        elif exception == "3.1.80":
            choices = [{"affix": "u", "rule": exception,
                        "coupled_action": {"target": "final_sound", "substitute": "a"}}]
        elif exception == "3.1.82":
            choices = [{"affix": "śnu", "rule": exception}, {"affix": "śnā", "rule": exception}]
        for choice in choices:
            choice["branch_id"] = choice["rule"] + ":" + choice["affix"]
            if choice["rule"] in {"3.1.69", "3.1.73", "3.1.77", "3.1.78", "3.1.79", "3.1.81"}:
                choice["defeats_default_sap"] = self._priority(choice["rule"], "3.1.68")
            if exception and len(choices) > 1:
                choice["option_license"] = exception
        return {"status": "REVIEWED_VIKARANA_CHOICES", "lexical_id": entry["id"],
                "choices": choices, "word_validity": "NOT_EVALUATED",
                "domain": "identified lexical entries; supplied sense and contextual pada license"}

    def _affix(self, name, slot, *, ting=False, lakara=False):
        if ting:
            pada, index = name
            teaching = self.review["endings"][pada][index]
            identity = ENDING_NAMES[pada][index] + ":3.4.78"
        elif lakara:
            teaching, identity = "लँट्", "laṭ:3.2.123"
        else:
            desc = self.review["affixes"][name]
            teaching, identity = desc["teaching"], desc["identity"]
        result = designate({"text": teaching, "identity": identity, "upadesha": True,
                            "category": "lakara" if lakara else "affix", "nasality_complete": True,
                            "vibhakti": ting, "taddhita": False}, self.markers)
        if result["status"] != "LOCAL_DESIGNATION":
            raise ValueError("Affix teaching convention no longer resolves")
        original = [{**s, "uid": f"{slot}:{s['id']}"} for s in result["original"]]
        labels = {m["label"] for m in result["marker_units"]}
        sarva = ting or "ś" in labels
        return {"id": slot, "identity": identity, "kind": "lakara" if lakara else "affix",
                "teaching": teaching, "original": original,
                "visible": [deepcopy(s) for s in original if s["id"] in result["visible_ids"]],
                "marker_evidence": result, "features": {"ting": ting, "sit": "ś" in labels,
                "pit": "p" in labels, "kit": "k" in labels, "ngit": "ṅ" in labels,
                "sarvadhatuka": sarva, "ardhadhatuka": not sarva and not lakara,
                "ngitvat": sarva and "p" not in labels}}

    def _event(self, state, rule, effect, **data):
        event = {"index": len(state["history"]), "rule": rule, "effect": effect, **deepcopy(data)}
        state["history"].append(event)
        return event

    def _replace(self, state, unit, start, count, symbols, rule, effect, **data):
        before = deepcopy(unit["visible"][start:start + count])
        if len(before) != count or not before:
            raise ValueError("Replacement target was not found")
        event = self._event(state, rule, effect, target_morpheme=unit["id"], before=before, **data)
        after = [{"uid": f"{unit['id']}:event:{event['index']}:{i}", "symbol": symbol,
                  "kind": "vowel" if symbol in VOWELS else "ayogavaha" if symbol in {"ṃ", "ḥ"} else "consonant",
                  "replaces": [s["uid"] for s in before], "introduced_by": rule}
                 for i, symbol in enumerate(symbols)]
        unit["visible"][start:start + count] = after
        event["after"] = deepcopy(after)

    def _join(self, state, left, right, symbols, rule):
        before = [deepcopy(left["visible"][-1]), deepcopy(right["visible"][0])]
        event = self._event(state, rule, "two_sound_ekadesha",
                            target_morphemes=[left["id"], right["id"]], before=before,
                            boundary="internal_non_padanta", ownership="posterior_morpheme")
        after = [{"uid": f"seam:event:{event['index']}:{i}", "symbol": symbol,
                  "kind": "vowel" if symbol in VOWELS else "consonant",
                  "replaces": [s["uid"] for s in before], "introduced_by": rule}
                 for i, symbol in enumerate(symbols)]
        left["visible"].pop()
        right["visible"][:1] = after
        event["after"] = deepcopy(after)
        if rule == "6.1.97":
            loser = "6.1.101" if before[1]["symbol"] == "a" else "6.1.88"
            state["blocked"].append({"rule": loser, "by": rule,
                                      "relation": self._priority(rule, loser),
                                      "reason": "source-declared exception at the internal seam"})

    def _append_affix(self, state, unit, rule):
        state["morphemes"].append(unit)
        if rule == "3.4.78":
            self._event(state, rule, "lakara_substitution", sthānin=state["lakara"]["id"],
                        source_visible=state["lakara"]["visible"], substitute=unit["id"],
                        identity=unit["identity"], original=unit["original"])
            state["lakara"]["substituted_by"] = unit["id"]
        else:
            self._event(state, rule, "affix_prescription", morpheme=unit["id"], identity=unit["identity"],
                        original=unit["original"])
        self._event(state, "1.3.2–9", "affix_it_designation_and_lopa", morpheme=unit["id"],
                    markers=unit["marker_evidence"]["marker_units"],
                    remaining_uids=[s["uid"] for s in unit["visible"]])
        if unit["features"]["sarvadhatuka"]:
            self._event(state, "3.4.113", "sarvadhatuka_designation", morpheme=unit["id"],
                        cause="ting" if unit["features"]["ting"] else "retained_s_it")
        elif unit["features"]["ardhadhatuka"]:
            self._event(state, "3.4.114", "ardhadhatuka_designation", morpheme=unit["id"])
        if unit["features"]["ngitvat"]:
            self._event(state, "1.2.4", "ngitvat_designation", morpheme=unit["id"],
                        cause="sarvadhatuka_and_no_p_it", not_a_teaching_ng_marker=True)

    def _guna(self, state, anga, trigger):
        """Only final ik or a short ik immediately before the last consonant.

        The admitted roots require no general syllabifier or puk implementation.
        The triggering affix's markers are never read from a later tiṅ ending.
        """
        if trigger.get("whole_affix_deletion"):
            state["blocked"].append({"rule": "7.3.84/7.3.86", "by": "1.1.63",
                                      "trigger": trigger["id"], "reason": "lu-marked deleted śap cannot license this aṅga effect"})
            return
        if not (trigger["features"]["sarvadhatuka"] or trigger["features"]["ardhadhatuka"]):
            raise ValueError("Guṇa has no admitted triggering affix")
        tail = next(unit for unit in reversed(anga) if unit["visible"])
        seq = sounds(tail)
        if seq[-1] in GUNA:
            index, rule = len(seq) - 1, "7.3.84"
        elif len(seq) >= 2 and seq[-2] in {"i", "u", "ṛ"} and seq[-1] not in VOWELS:
            index, rule = len(seq) - 2, "7.3.86"
        else:
            return
        features = trigger["features"]
        if features["kit"] or features["ngit"] or features["ngitvat"]:
            state["blocked"].append({"rule": rule, "by": "1.1.5", "trigger": trigger["id"],
                                      "relation": self._priority("1.1.5", rule),
                                      "anga": [u["id"] for u in anga],
                                      "reason": "the affix causing guṇa is kit/ngit/ngitvat"})
            return
        self._replace(state, tail, index, 1, GUNA[seq[index]], rule, "guna",
                      trigger=trigger["id"], anga=[u["id"] for u in anga])

    def _ending(self, state, ting, request):
        if request.pada == "A":
            if ting["identity"] == "thās:3.4.78":
                self._replace(state, ting, 0, len(ting["visible"]), ["s", "e"], "3.4.80", "thas_to_se",
                              lakara=state["lakara"]["id"])
                state["blocked"].append({"rule": "3.4.79", "by": "3.4.80",
                                          "relation": self._priority("3.4.80", "3.4.79"),
                                          "reason": "specific thās substitute"})
            else:
                index = max(i for i, s in enumerate(ting["visible"]) if s["symbol"] in VOWELS)
                self._replace(state, ting, index, len(ting["visible"]) - index, ["e"], "3.4.79", "ti_to_e",
                              selector_rule="1.1.64", lakara=state["lakara"]["id"],
                              tit_comes_from_lakara=True)
        # The corrected scope is affix membership, not an initial-only test.
        for index in reversed([i for i, s in enumerate(ting["visible"]) if s["symbol"] == "jh"]):
            self._replace(state, ting, index, 1, ["a", "n", "t"], "7.1.3", "jh_to_ant")

    def plan(self, request):
        selected = self.select(request)
        if selected["status"] != "REVIEWED_VIKARANA_CHOICES":
            return selected
        entry = self.entries[request.lexical_id]
        root_state = self.root_grammar.root(RootInput(entry["id"], entry["aupadeshik"], "listed_dhatu", True))
        if root_state["status"] != "PG4_ROOT_PREPROCESSING":
            return unresolved("The teaching root has unresolved preprocessing", preprocessing=root_state)
        branches = []
        for choice in selected["choices"]:
            root = {"id": "root:" + entry["id"], "identity": entry["id"], "kind": "root",
                    "teaching": entry["aupadeshik"], "original": deepcopy(root_state["original"]),
                    "visible": deepcopy(root_state["visible"]), "features": {"dhatu": True}}
            state = {"status": "MORPHOLOGICAL_PLAN", "request": asdict(request), "choice": deepcopy(choice),
                     "root_preprocessing": deepcopy(root_state), "morphemes": [root], "history": [], "blocked": [],
                     "lakara": self._affix(None, "lakara:lat", lakara=True)}
            self._event(state, "3.2.123", "present_lat", lakara=state["lakara"]["identity"],
                        remaining=sounds(state["lakara"]), markers=state["lakara"]["marker_evidence"]["marker_units"])
            if choice.get("preparation"):
                nic = self._affix("ṇic", "nic")
                self._append_affix(state, nic, "3.1.25")
                self._guna(state, [root], nic)
                self._event(state, "3.1.32", "derived_dhatu_designation", constituents=[root["id"], nic["id"]], sense="svartha")
            vik = self._affix(choice["affix"], "vikarana")
            self._append_affix(state, vik, choice["rule"])
            if choice.get("whole_affix_deletion"):
                deletion = choice["whole_affix_deletion"]
                self._event(state, deletion["rule"], "whole_affix_deletion", kind=deletion["kind"],
                            morpheme=vik["id"], before=vik["visible"], identity_retained=True)
                vik.update(visible=[], whole_affix_deletion=deepcopy(deletion))
                self._guna(state, [root], vik)
            index = 3 * self.review["ending_order"]["persons"].index(request.person) + self.review["ending_order"]["numbers"].index(request.number)
            ting = self._affix((request.pada, index), "ting", ting=True)
            self._append_affix(state, ting, "3.4.78")
            state["open_obligations"] = []
            if choice.get("coupled_action"):
                state["open_obligations"].append({"rule": choice["rule"], "action": choice["coupled_action"], "status": "REQUIRED_NOT_EXECUTED"})
            if entry["derivation"] != "thematic_lat":
                state["open_obligations"].append({"status": "WORD_DERIVATION_NOT_REVIEWED_FOR_THIS_LEXEME"})
            if choice["affix"] == "śnam":
                state["open_obligations"].append({"rule": "1.1.47", "status": "MIT_INFIX_PLACEMENT_NOT_EXECUTED",
                                                  "action": "place śnam after the root's last vowel; the plan's morpheme list is not a spoken ordering"})
            if choice.get("whole_affix_deletion", {}).get("kind") == "ślu":
                state["open_obligations"].append({"rule": "6.1.10", "status": "REDUPLICATION_NOT_EXECUTED"})
            if request.prefixes:
                state["open_obligations"].append({"status": "PREFIX_JOIN_AND_DEPENDENT_RULES_NOT_REVIEWED"})
            branches.append(state)
        return {"status": "REVIEWED_MORPHOLOGICAL_PLANS", "branches": branches}

    def derive(self, request):
        planned = self.plan(request)
        if planned["status"] != "REVIEWED_MORPHOLOGICAL_PLANS":
            return planned
        if any(s["open_obligations"] for s in planned["branches"]):
            return unresolved("Selection is resolved, but a complete word path still has obligations", plans=planned)
        entry = self.entries[request.lexical_id]
        results = []
        for state in planned["branches"]:
            root, vik, ting = state["morphemes"][0], state["morphemes"][-2], state["morphemes"][-1]
            anga = state["morphemes"][:-2]
            self._guna(state, anga, vik)
            if entry.get("syan_lengthening") and state["choice"]["affix"] == "śyan":
                if sounds(root)[-2] != "a":
                    raise ValueError("Reviewed śamādi lengthening target changed")
                self._replace(state, root, len(root["visible"]) - 2, 1, ["ā"], "7.3.74", "identified_samadi_lengthening")
            last = anga[-1]
            if sounds(last)[-1] in {"e", "o", "ai", "au"} and sounds(vik)[0] in VOWELS:
                mapping = {"e": ["a", "y"], "o": ["a", "v"], "ai": ["ā", "y"], "au": ["ā", "v"]}
                self._replace(state, last, len(last["visible"]) - 1, 1, mapping[sounds(last)[-1]], "6.1.78", "ayadi", following_morpheme=vik["id"])
            # All admitted stems now end in the vikaraṇa's a (or ya).
            if sounds(vik)[-1] != "a":
                raise ValueError("A non-thematic branch escaped the admitted domain")
            self._ending(state, ting, request)
            if sounds(ting)[0] == "ā" and ting["features"]["ngitvat"]:
                self._replace(state, ting, 0, 1, ["i", "y"], "7.2.81", "atam_atham_initial_a_to_iy", preceding_anga=vik["id"])
                # This local y is before t/th. No universal val/lopa engine is claimed.
                if sounds(ting)[1:3] in (["y", "t"], ["y", "th"]):
                    self._replace(state, ting, 1, 1, [], "6.1.66", "y_lopa_before_val")
            if sounds(ting)[0] in {"m", "v"}:
                self._replace(state, vik, len(vik["visible"]) - 1, 1, ["ā"], "7.3.101", "a_lengthening_before_yan", trigger=ting["id"])
            elif sounds(ting)[0] in {"a", "e", "o"}:
                self._join(state, vik, ting, [sounds(ting)[0]], "6.1.97")
            elif sounds(ting)[0] == "i":
                self._join(state, vik, ting, ["e"], "6.1.87")
            state["status"] = "PRE_TRIPADI_DERIVATION"
            state["projection"] = surface(state)
            query = self._readout(state, entry)
            results.append({"branch_id": state["choice"]["branch_id"], "pre_tripadi": state,
                            "readout": query, "form": query["projection"]})
        return {"status": "COMPLETE_IN_REVIEWED_LAT_DOMAIN", "request": asdict(request), "branches": results,
                "forms": sorted({r["form"] for r in results}),
                "word_validity": "SOURCE_CHECKED_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}

    def _readout(self, original, entry):
        if original.get("status") != "PRE_TRIPADI_DERIVATION":
            raise ValueError("A pause readout must start from the retained pre-Tripādī derivation")
        state = deepcopy(original)
        state["history"] = []
        root, ting = state["morphemes"][0], state["morphemes"][-1]
        if sounds(ting)[-1] == "s":
            self._replace(state, ting, len(ting["visible"]) - 1, 1, ["r"], "8.2.66", "pada_final_s_to_ru",
                          ru_teaching="रुँ", retained_marker="u", marker_rules=["1.3.2", "1.3.9"])
        if entry.get("rv_lengthening"):
            following = next(u for u in state["morphemes"][1:] if u["visible"])
            seq = sounds(root)
            if seq[-1] in {"r", "v"} and seq[-2] in {"i", "u", "ṛ"} and sounds(following)[0] not in VOWELS:
                self._replace(state, root, len(seq) - 2, 1, [{"i": "ī", "u": "ū", "ṛ": "ṝ"}[seq[-2]]],
                              "8.2.77", "root_upadha_length_before_hal", root_boundary=root["id"], following_morpheme=following["id"])
        if sounds(ting)[-1] == "r":
            self._replace(state, ting, len(ting["visible"]) - 1, 1, ["ḥ"], "8.3.15", "visarga_at_pause")
        visible = [deepcopy(s) for u in state["morphemes"] for s in u["visible"]]
        span = {"status": "SUPPLIED_PHONETIC_SPAN", "original": deepcopy(visible), "visible": visible,
                "history": [], "projection": "".join(s["symbol"] for s in visible)}
        query = self.root_grammar.phonetic(span, samhita=True, pada_final_uids=[visible[-1]["uid"]], following_unit_identities={})
        if query["status"] != "LOCAL_PHONETIC_QUERY":
            raise ValueError("Admitted complete laṭ path produced an unresolved phonetic query")
        return {"status": "LAT_PAUSE_READOUT", "projection": query["projection"], "visible": query["visible"],
                "history": state["history"] + query["history"],
                "source_status": original["status"], "feedback_into_earlier_rules": False}
