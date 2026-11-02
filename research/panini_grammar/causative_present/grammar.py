"""PG13: licensed ṇic presents with separate root, augment and affix owners.

The finite causative adapter does not read expected words or conjugation tables.
Ordinary Request objects still dispatch to the unchanged PG12 implementation.
"""
from copy import deepcopy
from dataclasses import asdict, dataclass
import json
from pathlib import Path

from research.panini_grammar.nasal_present.grammar import Grammar as PG12Grammar
from research.panini_grammar.root_progression.root_preprocess import RootInput
from research.panini_grammar.verification.marker_review import tokenize
from research.panini_grammar.vikarana_lat.grammar import (
    Grammar as PG5Grammar, Request, VOWELS, sounds, surface, unresolved, ENDING_NAMES,
)

HERE = Path(__file__).resolve().parent
COMPLETE = "COMPLETE_IN_REVIEWED_CAUSATIVE_PRESENT_DOMAIN"


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


@dataclass(frozen=True)
class CausativeRequest(Request):
    formation: str = "nic"
    causative_licensed: bool | None = None


class Grammar(PG12Grammar):
    def __init__(self, records, roots, review=None, lexical=None):
        super().__init__(records, roots)
        self.pg13 = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.pg13_rules = {r["sid"]: self.pg12_scope.compile(r) for r in self.pg13["records"]}
        if (len(self.pg13_rules) != len(self.pg13["records"])
                or any(r["status"] != "COMPILED_REVIEWED_RECORD" for r in self.pg13_rules.values())
                or any(r["sanskrit"] != self.pg12_scope.frame(r["sid"])["text"] for r in self.pg13["records"])):
            raise ValueError("PG13 wording, occurrence or case does not bind")
        additions = load("LEXICAL_ENTRIES.json")["entries"] if lexical is None else deepcopy(lexical)
        self.causatives = {e["id"]: deepcopy(e) for e in additions}
        if len(self.causatives) != len(additions):
            raise ValueError("Duplicate causative lexical identity")
        source = {r["i"]: r for r in roots}
        for entry in additions:
            keys = ["baseindex", "aupadeshik", "gana", "pada", "artha", "tags"]
            if "anubandha_note_मित्" in entry:
                keys.append("anubandha_note_मित्")
            if any(entry[k] != source[entry["id"]][k] for k in keys):
                raise ValueError("Causative root identity, meaning or source qualification changed")

    def _guard13(self, request):
        if not isinstance(request, CausativeRequest):
            return unresolved("A typed CausativeRequest is required")
        if request.lexical_id not in self.causatives:
            return unresolved("The causative lexical identity has not been reviewed")
        if request.sense != self.causatives[request.lexical_id]["artha"]:
            return unresolved("The original root sense is not the selected lexical sense")
        if request.formation != "nic" or request.causative_licensed is not True:
            return unresolved("The prayojaka causative meaning must be independently licensed")
        if request.pada != "P" or request.pada_licensed is not True:
            return unresolved("This profile requires a supplied parasmaipada context license")
        if (request.tense, request.voice, request.register) != ("present", "kartari", "classical"):
            return unresolved("Only classical kartari causative present is admitted")
        if request.prefixes != () or not isinstance(request.prefixes, tuple):
            return unresolved("Only an explicitly unprefixed context is reviewed")
        if request.person not in self.review["ending_order"]["persons"] or request.number not in self.review["ending_order"]["numbers"]:
            return unresolved("Person or number is outside the three by three domain")
        if request.samhita is not True or request.at_pause is not True:
            return unresolved("Internal saṃhitā and pause readout must be specified")
        return None

    def _recipe13(self, lexical_id):
        for rule, name in [("7.3.37", "yuk"), ("7.3.36", "puk")]:
            p = self.pg13_rules[rule]["parameters"]
            if lexical_id in p["lexical_ids"]:
                if (p["marker"] != "k" or p["pronunciation_only"] != "u"
                        or p["placement"] != "kit_final_member_of_root" or len(p["visible"]) != 1):
                    raise ValueError("The source-reviewed augment roles cannot change")
                return name, p["teaching"], p["visible"][0], rule
        return None

    def carrier(self, state):
        """Check constituent identity and kit placement without flattening owners."""
        units = state["morphemes"]
        nics = [u for u in units if u["id"] == "nic"]
        if not units or len(nics) != 1:
            raise ValueError("Exactly one root and one causative affix are required")
        root, nic = units[0], nics[0]
        phases = {"ROOT_AND_NIC": (False, False, False), "ROOT_STRENGTH": (False, False, False),
                  "ROOT_AUGMENT": (True, False, False), "DERIVED_DHATU": (True, True, False),
                  "OUTER_AFFIXES": (True, True, True), "STEM_READY": (True, True, True), "COMPLETE": (True, True, True)}
        if phases.get(state.get("phase13")) != tuple(bool(state.get(k)) for k in ["root_constituent", "derived_dhatu", "outer_affixes"]):
            raise ValueError("The phase and constituent boundaries disagree")
        lex = state["request"]["lexical_id"]
        if (root["kind"] != "root" or root["identity"] != lex or root["id"] != "root:" + lex
                or root["teaching"] != self.causatives[lex]["aupadeshik"]
                or nic["kind"] != "affix" or nic["identity"] != "ṇic:3.1.25"
                or nic["teaching"] != "णिच्"
                or {m["label"] for m in nic["marker_evidence"]["marker_units"]} != {"ṇ", "c"}
                or not nic["features"].get("nit") or not nic["features"].get("ardhadhatuka")
                or any(nic["features"].get(k) for k in ["sit", "kit", "ngit", "ngitvat"])):
            raise ValueError("The retained root or causative trigger changed")
        expected = [root["id"]]
        augmented = state.get("root_constituent")
        if augmented:
            recipe = self._recipe13(lex)
            if recipe:
                name, teaching, sound, rule = recipe
                aug = units[1]
                if (aug["id"] != "augment:" + name or aug["identity"] != name + ":" + rule
                        or aug["kind"] != "augment" or aug["host"] != root["id"]
                        or aug["teaching"] != teaching or not aug["features"].get("kit")
                        or [s["symbol"] for s in aug["original"]] != [sound, "u", "k"]
                        or sounds(aug) != [sound]
                        or aug["visible"] != [aug["original"][0]]
                        or aug["markers"] != [aug["original"][2]]
                        or aug["pronunciation_only"] != [aug["original"][1]]):
                    raise ValueError("The kit augment lost its source, owner or pronunciation distinction")
                expected.append(aug["id"])
            if augmented != {"id": "root-constituent:" + lex, "members": expected.copy(), "head": root["id"]}:
                raise ValueError("The root constituent has lost a member or changed its host")
        expected.append("nic")
        derived = state.get("derived_dhatu")
        if derived and (not augmented or derived != {"id": "causative-dhatu:" + lex,
                "members": expected.copy(), "kind": "dhatu", "head": augmented["id"], "rule": "3.1.32"}):
            raise ValueError("The derived dhātu must include its full root constituent and ṇic")
        if state.get("outer_affixes"):
            vik, ting = units[-2:]
            req = state["request"]
            index = 3 * self.review["ending_order"]["persons"].index(req["person"]) + self.review["ending_order"]["numbers"].index(req["number"])
            if (not derived or vik["id"] != "vikarana" or vik["identity"] != "śap:3.1.68"
                    or vik.get("whole_affix_deletion") or ting["id"] != "ting" or not ting["features"].get("ting")
                    or ting["identity"] != ENDING_NAMES[req["pada"]][index] + ":3.4.78"):
                raise ValueError("The causative's outer affixes changed")
            expected += ["vikarana", "ting"]
        if [u["id"] for u in units] != expected:
            raise ValueError("Unexpected, missing or reordered constituent")
        seq = [{**deepcopy(s), "owner": u["id"]} for u in units for s in u["visible"]]
        if len({s["uid"] for s in seq}) != len(seq):
            raise ValueError("Visible sound identities must be unique")
        return seq

    def _require13(self, state, phase):
        if state.get("phase13") != phase:
            raise ValueError("Causative stages cannot repeat, run out of order or read back a projection")
        self.carrier(state)

    def plan(self, request):
        if not isinstance(request, CausativeRequest):
            return super().plan(request)
        error = self._guard13(request)
        if error:
            return error
        e = self.causatives[request.lexical_id]
        rs = self.root_grammar.root(RootInput(e["id"], e["aupadeshik"], "listed_dhatu", True))
        if rs["status"] != "PG4_ROOT_PREPROCESSING" or [s["symbol"] for s in rs["visible"]] != e["root_shape"]:
            return unresolved("The reviewed root preprocessing no longer resolves")
        root = {"id": "root:" + e["id"], "identity": e["id"], "kind": "root", "teaching": e["aupadeshik"],
                "original": deepcopy(rs["original"]), "visible": deepcopy(rs["visible"]), "features": {"dhatu": True}}
        state = {"status": "CAUSATIVE_MORPHOLOGICAL_PLAN", "request": asdict(request), "morphemes": [root],
                 "root_preprocessing": rs, "history": [], "blocked": [], "open_obligations": [],
                 "choice": {"affix": "śap", "rule": "3.1.68", "branch_id": "nic:3.1.26:śap"},
                 "lakara": self._affix(None, "lakara:lat", lakara=True), "phase13": "ROOT_AND_NIC"}
        nic = self._affix("ṇic", "nic")
        nic["features"]["nit"] = "ṇ" in {m["label"] for m in nic["marker_evidence"]["marker_units"]}
        self._append_affix(state, nic, "3.1.26")
        self._event(state, "3.1.26", "supplied_prayojaka_license", supplied=request.causative_licensed, base_sense=request.sense)
        self.carrier(state)
        return {"status": "REVIEWED_CAUSATIVE_PLAN", "branches": [state]}

    def _ayadi13(self, state, unit, following):
        mapping = self.pg13_rules["6.1.78"]["parameters"]["mapping"]
        seq = sounds(unit)
        if seq[-1] in mapping and sounds(following)[0] in VOWELS:
            self._replace(state, unit, len(seq)-1, 1, mapping[seq[-1]], "6.1.78", "owned_ayadi",
                          following_morpheme=following["id"])

    def _root_strength13(self, state):
        self._require13(state, "ROOT_AND_NIC")
        root, nic = state["morphemes"]
        if sounds(root) != self.causatives[root["identity"]]["root_shape"] or sounds(nic) != ["i"]:
            raise ValueError("Root strength needs the original reviewed root and actual ṇic")
        seq = sounds(root)
        mapping = self.pg13_rules["7.2.115"]["parameters"]["mapping"]
        if seq[-1] in mapping:
            before = deepcopy(root["visible"][-1])
            self._replace(state, root, len(seq)-1, 1, mapping[seq[-1]], "7.2.115", "nit_final_vrddhi",
                          trigger=nic["id"], retained_nit=True, surface_identity=seq[-1] == "ā")
            if before["symbol"] == "ṛ":
                self._event(state, "1.1.51", "r_accompanied_vrddhi", source=before, result=deepcopy(root["visible"][-2:]))
        elif len(seq) >= 2 and seq[-2] == "a":
            self._replace(state, root, len(seq)-2, 1, ["ā"], "7.2.116", "nit_penultimate_a_vrddhi", trigger=nic["id"])
        else:
            before = deepcopy(root["visible"])
            self._guna(state, [root], nic)
            if "ṛ" in seq and sounds(root) != seq:
                self._event(state, "1.1.51", "r_accompanied_guna", source=before, result=deepcopy(root["visible"]))
        mit = self.pg13_rules["6.4.92"]["parameters"]["lexical_ids"]
        if root["identity"] in mit:
            e = self.causatives[root["identity"]]
            if "मित्" not in e["tags"] or not e.get("anubandha_note_मित्") or sounds(root)[-2] != "ā":
                raise ValueError("Mit shortening needs the retained source license and actual long upadhā")
            self._replace(state, root, len(root["visible"])-2, 1, ["a"], "6.4.92", "licensed_mit_shortening",
                          trigger=nic["id"], lexical_id=root["identity"], retained_source_note=e["anubandha_note_मित्"])
        self._ayadi13(state, root, nic)
        state["phase13"] = "ROOT_STRENGTH"

    def _root_augment13(self, state):
        self._require13(state, "ROOT_STRENGTH")
        root, nic = state["morphemes"]
        recipe = self._recipe13(root["identity"])
        members = [root["id"]]
        if recipe:
            name, teaching, symbol, rule = recipe
            if sounds(root)[-1] != "ā" or sounds(nic) != ["i"]:
                raise ValueError("This augment profile requires final ā before actual ṇic")
            original = [{"uid": f"augment:{name}:source:{i}", "symbol": s.symbol, "kind": s.kind}
                        for i, s in enumerate(tokenize(teaching))]
            if [s["symbol"] for s in original] != [symbol, "u", "k"]:
                raise ValueError("The augment teaching form changed")
            aug = {"id": "augment:" + name, "identity": name + ":" + rule, "kind": "augment", "host": root["id"],
                   "teaching": teaching, "original": original, "visible": deepcopy(original[:1]),
                   "markers": deepcopy(original[2:]), "pronunciation_only": deepcopy(original[1:2]), "features": {"kit": True}}
            state["morphemes"].insert(1, aug)
            members.append(aug["id"])
            self._event(state, rule, "root_final_augment", host=root["id"], owner=aug["id"], original=original, trigger=nic["id"])
            self._event(state, "1.3.3", "augment_final_k_it", target=original[-1])
            self._event(state, "1.3.9", "augment_marker_lopa", removed=original[-1])
            self._event(state, rule, "pronunciation_only_u_not_an_it", sound=original[1],
                        evidence="Bālamanoramā: उकार उच्चारणार्थः", marker_nasality_invented=False)
            self._event(state, "1.1.46", "kit_augment_final_root_member", host=root["id"], member=aug["id"])
            if name == "yuk":
                state["blocked"].append({"rule": "7.3.36", "by": "7.3.37", "reason": "pā in the drinking sense; explicit yuk exception to puk"})
        state["root_constituent"] = {"id": "root-constituent:" + root["identity"], "members": members, "head": root["id"]}
        state["phase13"] = "ROOT_AUGMENT"
        self.carrier(state)

    def _derived13(self, state):
        self._require13(state, "ROOT_AUGMENT")
        lex = state["request"]["lexical_id"]
        state["derived_dhatu"] = {"id": "causative-dhatu:" + lex, "members": state["root_constituent"]["members"] + ["nic"],
                                  "kind": "dhatu", "head": state["root_constituent"]["id"], "rule": "3.1.32"}
        self._event(state, "3.1.32", "derived_dhatu_designation", constituent=state["derived_dhatu"], sense="hetumati")
        state["phase13"] = "DERIVED_DHATU"

    def _outer13(self, state, request):
        self._require13(state, "DERIVED_DHATU")
        if state["request"] != asdict(request):
            raise ValueError("Outer affixes cannot borrow another request")
        self._event(state, "3.2.123", "present_lat", lakara=state["lakara"]["identity"])
        rule = "1.3.86" if request.lexical_id in self.pg13_rules["1.3.86"]["parameters"]["lexical_ids"] else "1.3.78"
        self._event(state, rule, "supplied_causative_parasmaipada_context", license=request.pada_licensed,
                    simple_root_pada_not_transferred=True)
        self._append_affix(state, self._affix("śap", "vikarana"), "3.1.68")
        self._event(state, "1.4.13", "causative_anga_for_sap", anga=state["derived_dhatu"], following="vikarana")
        index = 3 * self.review["ending_order"]["persons"].index(request.person) + self.review["ending_order"]["numbers"].index(request.number)
        self._append_affix(state, self._affix((request.pada, index), "ting", ting=True), "3.4.78")
        state["outer_affixes"] = True
        state["phase13"] = "OUTER_AFFIXES"
        self.carrier(state)

    def _stem13(self, state):
        self._require13(state, "OUTER_AFFIXES")
        nic, vik = state["morphemes"][-3:-1]
        if sounds(nic) != ["i"] or sounds(vik) != ["a"]:
            raise ValueError("The outer śap must act on the actual unstrengthened ṇic vowel")
        self._guna(state, state["morphemes"][:-2], vik)
        self._ayadi13(state, nic, vik)
        state["phase13"] = "STEM_READY"

    def _finish13(self, state, request):
        self._require13(state, "STEM_READY")
        if state["request"] != asdict(request):
            raise ValueError("Ending rules cannot borrow another request")
        vik, ting = state["morphemes"][-2:]
        self._ending(state, ting, request)
        if sounds(ting)[0] in {"m", "v"}:
            self._replace(state, vik, len(vik["visible"])-1, 1, ["ā"], "7.3.101", "outer_a_lengthening", trigger=ting["id"])
        elif sounds(ting)[0] == "a":
            self._join(state, vik, ting, ["a"], "6.1.97")
        state["phase13"] = "COMPLETE"
        state["status"] = "PRE_TRIPADI_DERIVATION"
        state["projection"] = surface(state)
        self.carrier(state)

    def derive(self, request):
        if not isinstance(request, CausativeRequest):
            return super().derive(request)
        planned = self.plan(request)
        if planned["status"] != "REVIEWED_CAUSATIVE_PLAN":
            return planned
        state = planned["branches"][0]
        self._root_strength13(state)
        self._root_augment13(state)
        self._derived13(state)
        self._outer13(state, request)
        self._stem13(state)
        self._finish13(state, request)
        readout = PG5Grammar._readout(self, state, self.causatives[request.lexical_id])
        return {"status": COMPLETE, "request": asdict(request), "forms": [readout["projection"]],
                "branches": [{"branch_id": state["choice"]["branch_id"], "pre_tripadi": state,
                              "readout": readout, "form": readout["projection"]}],
                "word_validity": "SOURCE_CHECKED_CAUSATIVE_PROFILE_NOT_UNRESTRICTED_SANSKRIT_ORACLE"}
