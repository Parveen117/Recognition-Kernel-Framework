"""PG4's source-bound grammar adapter; no full word generator or validity oracle.

Rule records bind inherited terms before they can be used. The phonetic view
is separate from root preprocessing, and later stages never feed earlier ones.
"""
from __future__ import annotations

from copy import deepcopy

from research.panini_grammar.root_progression.root_preprocess import RootInput, marker_profile, preprocess
from research.panini_grammar.verification.marker_review import designate, tokenize
from proof_lab.paninian_it_samjna_compiled import its, placement
from research.panini_grammar.scoped_derivations.scope import ScopeIndex, applicability, load


class Grammar:
    def __init__(self, records, review=None):
        self.scope = ScopeIndex(records)
        self.review = load("RULE_RECORDS.json") if review is None else deepcopy(review)
        self.rules = {r["sid"]: self.scope.compile(r) for r in self.review["records"]}
        bad = {sid: r["errors"] for sid, r in self.rules.items() if r["status"] != "COMPILED_REVIEWED_RECORD"}
        if bad:
            raise ValueError(f"Unresolved source-bound records: {bad}")
        self.markers = marker_profile()
        self.lexical = {r["id"]: r for r in load("LEXICAL_WITNESSES.json")["withdraw_conditioned_retroflexion"]}

    def prescribe_sap(self, facts):
        rule = self.rules["3.1.68"]
        status = applicability(rule, facts)
        if status != "APPLICABLE":
            return {"status": status, "rule": "3.1.68"}
        p = rule["parameters"]
        affix = designate({"text": p["teaching"], "identity": p["identity"], "upadesha": True,
                           "category": "affix", "nasality_complete": True,
                           "vibhakti": False, "taddhita": False}, self.markers)
        return {"status": "CANDIDATE_AFFIX", "rule": "3.1.68", "affix": affix,
                "selection_status": "VIKARANA_COMPETITION_NOT_RESOLVED",
                "placement": "after the supplied root, before the supplied sārvadhātuka affix",
                "accent": "inherited initial-udātta prescription recorded; phonetic realization not supplied",
                "word_validity": "NOT_EVALUATED"}

    def tuk_choices(self, *, vowel, following, samhita, pada_final, left_identity,
                    particle_sense_licensed, prior_ekadesha, chandas):
        """One local junction; unknown visibility and Vedic scope remain unknown."""
        if not isinstance(samhita, bool):
            return {"status": "UNRESOLVED", "reason": "saṃhitā status missing"}
        empty = {"status": "LOCAL_TUK_CHOICES", "choices": [{"insert": False, "rule": None}], "blocked": []}
        if not samhita or following != "ch":
            return empty
        length = next((k for k, values in self.review["vowel_length"].items() if vowel in values), None)
        if vowel == "ḹ":
            return {"status": "UNRESOLVED", "reason": "Long ḹ is outside the reviewed vowel profile"}
        if length is None:
            return empty
        if not isinstance(pada_final, bool) or prior_ekadesha is not False or chandas is not False:
            return {"status": "UNRESOLVED", "reason": "boundary, 6.1.86 visibility or chandas reading not supplied in the admitted profile"}
        special = left_identity in self.rules["6.1.74"]["parameters"]["identities"]
        if left_identity is None or special and (particle_sense_licensed is not True or vowel != "ā"):
            return {"status": "UNRESOLVED", "reason": "particle identity/sense not established"}
        candidates = []
        for sid in ("6.1.73", "6.1.74", "6.1.75", "6.1.76"):
            rule = self.rules[sid]
            if applicability(rule, {"samhita": samhita}) != "APPLICABLE":
                continue
            p = rule["parameters"]
            if p.get("length", length) != length or p.get("pada_final", pada_final) != pada_final:
                continue
            if p.get("identities") and left_identity not in p["identities"]:
                continue
            candidates.append(sid)
        blocked = [deepcopy(edge) for edge in self.review["priority"]
                   if edge["winner"] in candidates and edge["loser"] in candidates]
        losers = {edge["loser"] for edge in blocked}
        winners = [sid for sid in candidates if sid not in losers]
        if len(winners) != 1:
            return {"status": "UNRESOLVED", "reason": "No unique source-supported prescription", "candidates": candidates}
        winner = winners[0]
        choices = [{"insert": True, "rule": winner}]
        if self.rules[winner]["parameters"]["optional"]:
            choices.insert(0, {"insert": False, "rule": winner})
        return {"status": "LOCAL_TUK_CHOICES", "choices": choices, "blocked": blocked}

    def root(self, root: RootInput):
        state = preprocess(root, self.markers)
        if state["status"] != "BOUNDED_ROOT_PREPROCESSING":
            return state
        out = deepcopy(state)
        witness = self.lexical.get(root.lexical_id)
        if (witness is None and any(e["rule"] == "6.1.64" for e in out["history"])
                and len(out["original"]) > 1 and out["original"][1]["symbol"] in {"ṭ", "ṭh", "ḍ", "ḍh", "ṇ"}):
            return {"status": "UNRESOLVED", "reason": "Conditioned retroflexion needs an identified lexical witness"}
        if witness and root.teaching != witness["teaching"]:
            return {"status": "UNRESOLVED", "reason": "Lexical witness and supplied teaching form disagree"}
        if witness and any(e["rule"] == "6.1.64" for e in out["history"]):
            original = out["original"][witness["position"]]
            target = next(s for s in out["visible"] if s["uid"] == original["uid"])
            if target["symbol"] != witness["from"]:
                raise ValueError("Conditioned teaching-sound witness no longer matches")
            target["symbol"] = witness["to"]
            out["history"].append({"rule": "PG4-conditioned-dental-restoration", "target_uid": target["uid"],
                                   "before": witness["from"], "after": witness["to"],
                                   "cause_rule": "6.1.64", "cause_uid": out["original"][0]["uid"],
                                   "witness_id": root.lexical_id,
                                   "scope": "identified teaching convention, not general rule rollback"})
        # PG3's upadeśa-stage num has already been licensed. It can interrupt
        # vowel–ch contact (e.g. uchi -> unch); never erase it to make tuk fire.
        source = out["visible"]
        visible = []
        for i, sound in enumerate(source):
            visible.append(sound)
            if i + 1 == len(source):
                continue
            choices = self.tuk_choices(vowel=sound["symbol"], following=source[i + 1]["symbol"],
                samhita=True, pada_final=False, left_identity="ordinary_root",
                particle_sense_licensed=False, prior_ekadesha=False, chandas=False)
            if choices["status"] != "LOCAL_TUK_CHOICES" or len(choices["choices"]) != 1:
                return {"status": "UNRESOLVED", "reason": "Internal root tuk needs a distinct grammatical branch"}
            choice = choices["choices"][0]
            if choice["insert"]:
                augment = its("tu~k", "agama")
                if augment["remaining_sounds"] != ("t",) or placement("tu~k") != "after":
                    raise ValueError("Pinned ordinary T82 tuk contract changed")
                uid = f"{sound['uid']}:tuk:{choice['rule']}"
                visible.append({"uid": uid, "id": None, "symbol": "t", "kind": "consonant",
                                "nasal": False, "accent": "", "offset": None, "introduced_by": choice["rule"]})
                out["history"].append({"rule": choice["rule"], "effect": "tuk_augment", "inserted_uid": uid,
                    "recipient_uid": sound["uid"], "placement_rule": "1.1.46", "it_evidence": augment["its"]})
        out.update(status="PG4_ROOT_PREPROCESSING", visible=visible,
                   projection="".join(s["symbol"] for s in visible),
                   profile="internal root, non-Vedic, no prior ekādeśa; source lexical identity and nasality supplied")
        return out

    def root_length_choice(self, *, vowel, rv, following_is_consonant,
                           is_dhatu, rv_is_root_upadha, rv_origin):
        """8.2.78 on its reviewed original-root domain; no guessed sthānivad view."""
        p = self.rules["8.2.78"]["parameters"]
        if not all(isinstance(v, bool) for v in (following_is_consonant, is_dhatu, rv_is_root_upadha)):
            return {"status": "UNRESOLVED", "reason": "Root, position or consonant fact is missing"}
        if not all((is_dhatu, rv_is_root_upadha, following_is_consonant)) or rv not in p["rv"]:
            return {"status": "INAPPLICABLE"}
        if rv_origin == "yan_hidden_by_reviewed_view":
            return {"status": "INAPPLICABLE", "reason": "The supplied reviewed query sees the original vowel, not r/v"}
        if rv_origin != "original":
            return {"status": "UNRESOLVED", "reason": "Yaṇ/bahiraṅga visibility requires a source-supported query view"}
        if vowel == p["unhandled_target"]:
            return {"status": "UNRESOLVED", "reason": "Lengthening ḷ is outside the reviewed vowel profile"}
        if vowel not in p["mapping"]:
            return {"status": "INAPPLICABLE"}
        return {"status": "LICENSED_REPLACEMENT", "rule": "8.2.78", "replacement": p["mapping"][vowel]}

    def phonetic(self, state, *, samhita, pada_final_uids, following_unit_identities):
        """Ordered rule-local readout. No global normal-form or derivation claim."""
        if state.get("status") not in {"PG4_ROOT_PREPROCESSING", "BOUNDED_ROOT_PREPROCESSING", "SUPPLIED_PHONETIC_SPAN"}:
            return {"status": "UNRESOLVED", "reason": "A source state is required; a query result cannot be fed back"}
        if not isinstance(samhita, bool) or pada_final_uids is None or following_unit_identities is None:
            return {"status": "UNRESOLVED", "reason": "Missing contact, boundary or unit information"}
        visible = deepcopy(state["visible"])
        if not set(pada_final_uids) <= {s["uid"] for s in visible}:
            return {"status": "UNRESOLVED", "reason": "Boundary names a missing sound identity"}
        final = set(pada_final_uids)
        history, blocked, obligations = [], [], []

        def change(i, symbol, sid, cause_uid):
            prior = visible[i]["symbol"]
            if prior == symbol:
                return False
            kind = "vowel" if any(symbol in group for group in self.review["vowel_length"].values()) else "consonant"
            visible[i] = {**visible[i], "symbol": symbol, "kind": "ayogavaha" if symbol == "ṃ" else kind}
            history.append({"rule": sid, "target_uid": visible[i]["uid"], "cause_uid": cause_uid,
                            "before": prior, "after": symbol})
            return True

        for sid in ("8.2.78", "8.3.24", "8.4.40", "8.4.41", "8.4.53", "8.4.58"):
            rule = self.rules[sid]
            if applicability(rule, {"samhita": samhita}) != "APPLICABLE":
                continue
            p = rule["parameters"]
            if rule["opcode"] == "root_upadha_length":
                if state.get("status") == "SUPPLIED_PHONETIC_SPAN":
                    continue  # supplied spans assert no root constituency
                if len(visible) < 3:
                    continue
                original = {s["uid"]: s["symbol"] for s in state["original"]}
                rv = visible[-2]
                result = self.root_length_choice(vowel=visible[-3]["symbol"], rv=rv["symbol"],
                    following_is_consonant=visible[-1]["kind"] == "consonant",
                    is_dhatu=True, rv_is_root_upadha=True,
                    rv_origin="original" if state["input"]["origin"] == "listed_dhatu" and original.get(rv["uid"]) == rv["symbol"] else "unreviewed")
                if result["status"] == "LICENSED_REPLACEMENT":
                    change(len(visible) - 3, result["replacement"], sid, rv["uid"])
                elif result["status"] == "UNRESOLVED":
                    obligations.append({"rule": sid, "target_uid": visible[-3]["uid"], "reason": result["reason"]})
            elif rule["opcode"] == "nasalize":
                for i, sound in enumerate(visible[:-1]):
                    if sound["symbol"] in p["targets"] and visible[i + 1]["symbol"] in p["following"] and sound["uid"] not in final:
                        change(i, p["replacement"], sid, visible[i + 1]["uid"])
            elif rule["opcode"] == "contact":
                # Each change exits this record's target class, so the local
                # iteration terminates. No later sūtra is revisited here.
                while True:
                    updates = []
                    for i, sound in enumerate(visible):
                        if sound["symbol"] not in p["mapping"]:
                            continue
                        causes, refusals = [], []
                        for j in (i - 1, i + 1):
                            if not 0 <= j < len(visible) or visible[j]["symbol"] not in p["triggers"]:
                                continue
                            inhibition = None
                            if sid == "8.4.40" and j < i:
                                q = self.rules["8.4.44"]["parameters"]
                                if visible[j]["symbol"] == q["preceding"] and sound["symbol"] in q["target"]:
                                    inhibition = "8.4.44"
                            if sid == "8.4.41" and j > i:
                                q = self.rules["8.4.43"]["parameters"]
                                if visible[j]["symbol"] == q["following"] and sound["symbol"] in q["target"]:
                                    inhibition = "8.4.43"
                            if sid == "8.4.41" and j < i and visible[j]["symbol"] != "ṣ" and visible[j]["uid"] in final:
                                unit = following_unit_identities.get(sound["uid"])
                                if unit is None:
                                    inhibition = "UNRESOLVED_8.4.42_UNIT"
                                    obligations.append({"rule": "8.4.42", "target_uid": sound["uid"], "reason": "following unit identity missing"})
                                elif unit not in self.rules["8.4.42"]["parameters"]["named_exceptions"]:
                                    inhibition = "8.4.42"
                            if inhibition:
                                refusal = {"rule": inhibition, "blocked_rule": sid, "target_uid": sound["uid"], "cause_uid": visible[j]["uid"]}
                                refusals.append(refusal)
                                if refusal not in blocked:
                                    blocked.append(refusal)
                            else:
                                causes.append(visible[j]["uid"])
                        if causes and refusals:
                            obligations.append({"rule": sid, "target_uid": sound["uid"], "reason": "mixed licensed and inhibited contact causes need review"})
                        elif causes:
                            updates.append((i, p["mapping"][sound["symbol"]], causes))
                    if not updates:
                        break
                    for i, replacement, causes in updates:
                        change(i, replacement, sid, causes)
            elif rule["opcode"] == "voice_before_jhas":
                for i in range(len(visible) - 2, -1, -1):
                    if visible[i]["symbol"] in p["mapping"] and visible[i + 1]["symbol"] in p["following"]:
                        change(i, p["mapping"][visible[i]["symbol"]], sid, visible[i + 1]["uid"])
            elif rule["opcode"] == "parasavarna":
                for i, sound in enumerate(visible[:-1]):
                    if sound["symbol"] != p["target"]:
                        continue
                    following = visible[i + 1]["symbol"]
                    if following in p["mapping"] and sound["uid"] not in final:
                        change(i, p["mapping"][following], sid, visible[i + 1]["uid"])
                    elif following in {"y", "r", "l", "v"} or following in p["mapping"] and sound["uid"] in final:
                        obligations.append({"rule": sid, "target_uid": sound["uid"], "reason": "semivowel realization or 8.4.59 pada-final option outside this profile"})
        return {"status": "PARTIAL_PHONETIC_QUERY" if obligations else "LOCAL_PHONETIC_QUERY",
                "projection": "".join(s["symbol"] for s in visible), "visible": visible,
                "history": history, "blocked": blocked, "open_obligations": obligations,
                "visibility": "separate ordered query; no feedback to preceding sūtras or root state",
                "word_validity": "NOT_EVALUATED"}

    def root_readout(self, root):
        state = self.root(root)
        return state, self.phonetic(state, samhita=True, pada_final_uids=[], following_unit_identities={})


def supplied_span(text, identity="control"):
    return {"status": "SUPPLIED_PHONETIC_SPAN", "visible":
            [{**s.__dict__, "uid": f"{identity}:sound:{s.id}"} for s in tokenize(text)],
            "note": "Supplied local phonetic context; not a derived Sanskrit word"}
