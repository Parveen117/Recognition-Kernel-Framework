"""A bounded it-designation review, not a word generator or Sanskrit parser.

All selectors read the original upadeśa.  1.3.9 projects the result only once.
Affix identity, grammatical class, and conventional nasality are input evidence;
they are not inferred from the visible string. Rule records are hand reviewed.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from pathlib import Path
import json


INDEPENDENT = dict(zip("अआइईउऊऋॠऌॡएऐओऔ", ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")))
MATRA = dict(zip("ािीुूृॄॢॣेैोौ", ("ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au")))
CONSONANT = dict(zip("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह", (
    "k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ",
    "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "ś", "ṣ", "s", "h")))


@dataclass(frozen=True)
class Sound:
    id: int
    symbol: str
    kind: str
    offset: int
    nasal: bool = False
    accent: str = ""


def tokenize(text: str) -> tuple[Sound, ...]:
    """Explicit Devanāgarī teaching forms only; uncertain notation is rejected."""
    result = []

    def add(symbol, kind, offset):
        result.append(Sound(len(result), symbol, kind, offset))

    i = 0
    while i < len(text):
        c = text[i]
        if c in INDEPENDENT:
            add(INDEPENDENT[c], "vowel", i)
        elif c in "ंः":
            # Preserve ayogavāhas in ordinary text and lexical headwords. Their
            # status in a teaching unit is deliberately left outside this audit.
            add({"ं": "ṃ", "ः": "ḥ"}[c], "ayogavaha", i)
        elif c in CONSONANT:
            add(CONSONANT[c], "consonant", i)
            if i + 1 < len(text) and text[i + 1] == "्":
                i += 1
            elif i + 1 < len(text) and text[i + 1] in MATRA:
                i += 1
                add(MATRA[text[i]], "vowel", i)
            else:
                add("a", "vowel", i)
        elif c == "ँ":
            if not result or result[-1].kind != "vowel" or result[-1].nasal:
                raise ValueError("Ambiguous nasalization attachment")
            result[-1] = replace(result[-1], nasal=True)
        elif c in "॒॑":
            if not result or result[-1].kind != "vowel":
                raise ValueError("Accent attachment needs review")
            result[-1] = replace(result[-1], accent=result[-1].accent + c)
        else:
            raise ValueError(f"Unsupported teaching-form notation {c!r} at {i}")
        i += 1
    if not result:
        raise ValueError("Empty teaching form")
    return tuple(result)


def select(rule: dict, sounds: tuple[Sound, ...]) -> set[int]:
    selector = rule["selector"]
    if selector == "nasal_vowels":
        return {s.id for s in sounds if s.kind == "vowel" and s.nasal}
    if selector == "final_consonant":
        return {sounds[-1].id} if sounds[-1].kind == "consonant" else set()
    if selector == "initial_symbols":
        return {0} if sounds[0].symbol in rule["symbols"] else set()
    if selector in {"initial_sequences", "final_sequences"}:
        selected = set()
        symbols = [s.symbol for s in sounds]
        for sequence in rule["sequences"]:
            start = 0 if selector == "initial_sequences" else len(symbols) - len(sequence)
            if start >= 0 and symbols[start:start + len(sequence)] == sequence:
                if rule.get("first_must_be_nasal") and not sounds[start].nasal:
                    continue
                selected.update(range(start, start + len(sequence)))
        return selected
    raise ValueError(f"Unknown selector: {selector}")


def designate(case: dict, rules: dict) -> dict:
    """Return designation evidence, never a validity judgment on a Sanskrit word."""
    required = {"upadesha", "category", "identity", "nasality_complete", "vibhakti", "taddhita"}
    if not required <= case.keys() or not all(isinstance(case[k], bool) for k in ("upadesha", "nasality_complete", "vibhakti", "taddhita")):
        return {"status": "UNRESOLVED", "reason": "Missing or untyped grammatical input"}
    if case["category"] not in {"root", "affix", "lakara", "phoneme_inventory", "ordinary"}:
        return {"status": "UNRESOLVED", "reason": "Unreviewed teaching-unit category"}
    if (case["category"] in {"root", "phoneme_inventory"} and (case["vibhakti"] or case["taddhita"])) or (case["category"] == "ordinary" and case["upadesha"]):
        return {"status": "UNRESOLVED", "reason": "Inconsistent grammatical input"}
    if case["upadesha"] and not case["nasality_complete"]:
        return {"status": "UNRESOLVED", "reason": "Conventional nasality has not been supplied"}
    try:
        sounds = tokenize(case["text"])
    except ValueError as error:
        return {"status": "UNRESOLVED", "reason": str(error)}
    if case["upadesha"] and any(s.kind == "ayogavaha" for s in sounds):
        return {"status": "UNRESOLVED", "reason": "Teaching-unit ayogavāha convention needs review"}
    facts = {**case, "affix": case["category"] in {"affix", "lakara"}}
    proposals = {}
    all_rules = rules["rules"] + rules.get("supplements", [])
    for rule in all_rules:
        if all(facts.get(k) == value for k, value in rule["requires"].items()):
            proposals[rule["id"]] = select(rule, sounds)
        else:
            proposals[rule["id"]] = set()
    inhibited = []
    for rule in rules["rules"]:
        if rule["effect"] != "inhibit":
            continue
        if case["identity"] in rule.get("except_identities", []):
            continue
        protected = proposals[rule["id"]]
        for index in protected & proposals[rule["blocks"]]:
            if sounds[index].symbol in rule["symbols"]:
                proposals[rule["blocks"]].remove(index)
                inhibited.append({"index": index, "rule": rule["id"], "blocked": rule["blocks"]})
    for exception in rules["exceptions"]:
        if not all(facts.get(k) == value for k, value in exception["requires"].items()):
            continue
        if exception.get("identities") and case["identity"] not in exception["identities"]:
            continue
        for index in sorted(proposals[exception["blocks"]].copy()):
            if sounds[index].symbol in exception["symbols"]:
                proposals[exception["blocks"]].remove(index)
                inhibited.append({"index": index, "rule": exception["id"], "blocked": exception["blocks"]})
    for supplement in rules.get("supplements", []):
        for blocked in supplement.get("supersedes_component_designations", []):
            proposals[blocked].difference_update(proposals[supplement["id"]])
    ledger = []
    designation_rules = {r["id"] for r in all_rules if r["effect"] == "designate"}
    for sound in sounds:
        reasons = sorted(sid for sid, indices in proposals.items() if sid in designation_rules and sound.id in indices)
        if reasons:
            ledger.append({"index": sound.id, "symbol": sound.symbol, "rules": reasons})
    marked = {entry["index"] for entry in ledger}
    visible = tuple(sound for sound in sounds if sound.id not in marked)
    units = []
    for rule in all_rules:
        indices = sorted(proposals[rule["id"]])
        if rule["effect"] != "designate" or not indices:
            continue
        groups = [indices] if rule.get("compound_marker") else [[i] for i in indices]
        for group in groups:
            units.append({"indices": group, "label": "".join(sounds[i].symbol for i in group), "rule": rule["id"]})
    units.sort(key=lambda unit: unit["indices"])
    return {"status": "LOCAL_DESIGNATION", "identity": case["identity"],
            "original": [asdict(s) for s in sounds], "it": ledger,
            "marker_units": units,
            "inhibited": inhibited, "visible_ids": [s.id for s in visible],
            "it_only_projection": "".join(s.symbol for s in visible),
            "projection_rule": "1.3.9", "word_validity": "NOT_EVALUATED"}


def root_projection_audit(rows: list[dict], rules: dict) -> dict:
    """Compare marker-only projections to publisher headwords; retain differences."""
    counts = {"exact_headword_agreement": 0, "different_projection": 0, "unresolved_notation": 0, "non_root_ganasutra": 0}
    differences, unresolved, directives = [], [], []
    signatures = {"initial_n_only": 0, "initial_s_only": 0, "other_difference": 0}
    compound_ir_count = 0
    for row in rows:
        if row.get("tags") == "ganasutra":
            counts["non_root_ganasutra"] += 1
            directives.append({"id": row["i"], "text": row["dhatu"], "source_tag": row["tags"]})
            continue
        case = {"text": row["aupadeshik"], "identity": "dhatu:" + row["i"],
                "category": "root", "upadesha": True, "nasality_complete": True,
                "vibhakti": False, "taddhita": False}
        result = designate(case, rules)
        compound_ir_count += any(unit["label"] == "ir" for unit in result.get("marker_units", []))
        try:
            headword = "".join(s.symbol for s in tokenize(row["dhatu"]))
        except ValueError:
            headword = None
        if result["status"] == "UNRESOLVED" or headword is None:
            counts["unresolved_notation"] += 1
            unresolved.append({"id": row["i"], "upadesha": row["aupadeshik"],
                               "headword": row["dhatu"], "reason": result.get("reason", "Headword notation")})
        elif result["it_only_projection"] == headword:
            counts["exact_headword_agreement"] += 1
        else:
            counts["different_projection"] += 1
            projection = result["it_only_projection"]
            if projection.startswith("ṇ") and "n" + projection[1:] == headword:
                signatures["initial_n_only"] += 1
            elif projection.startswith("ṣ") and "s" + projection[1:] == headword:
                signatures["initial_s_only"] += 1
            else:
                signatures["other_difference"] += 1
            differences.append({"id": row["i"], "upadesha": row["aupadeshik"],
                                "headword": row["dhatu"], "it_only": result["it_only_projection"],
                                "headword_tokens": headword})
    return {"status": "DIAGNOSTIC_NOT_ROOT_DERIVATION_VALIDATION", "counts": counts,
            "assumption": "Treat published aupadeshik nasal flags as supplied; no independent completeness claim.",
            "compound_ir_records": compound_ir_count,
            "difference_signatures_not_rule_validations": signatures,
            "differences": differences, "unresolved": unresolved, "non_root_directives": directives}


def read_rules() -> dict:
    return json.loads(Path(__file__).with_name("MARKER_RULES.json").read_text(encoding="utf-8"))
