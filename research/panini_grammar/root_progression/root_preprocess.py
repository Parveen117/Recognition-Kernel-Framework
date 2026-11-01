"""PG3: source-bounded teaching-root preprocessing with retained sound identity.

Consumes the PG2 marker ledger, T81's last-vowel selector and T82's ordinary
num-placement contract. It does not read the expected lexical headword and
does not generate a Sanskrit word or modify the canonical operator engine.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, dataclass
import json
from pathlib import Path

from proof_lab.paninian_samjna_sound_layer import ti_1_1_64, savarna_classes, NASAL
from proof_lab.paninian_it_samjna_compiled import its as t82_its, placement
from proof_lab.shaiva_sources_varga_crystal import VARGAS
from research.panini_grammar.verification.marker_review import designate

HERE = Path(__file__).resolve().parent


def marker_profile() -> dict:
    """New attributed profile; frozen PG2 and T82 files are never rewritten."""
    rules = json.loads((HERE.parent / "verification/MARKER_RULES.json").read_text())
    overlay = json.loads((HERE / "RULES.json").read_text())
    rules["exceptions"].extend(deepcopy(overlay["marker_exceptions"]))
    return rules


@dataclass(frozen=True)
class RootInput:
    lexical_id: str
    teaching: str
    origin: str  # explicitly supplied: listed_dhatu or derived_subdhatu
    nasality_complete: bool


def preprocess(root: RootInput, rules: dict | None = None) -> dict:
    """Apply only the reviewed 6.1.64/65 and 7.1.58/1.1.47 contracts.

    The caller must supply root status and origin. The string alone cannot
    decide whether a term is a listed root or a denominal derivative.
    """
    rules = marker_profile() if rules is None else rules
    if (not all(isinstance(value, str) and value for value in
                (root.lexical_id, root.teaching, root.origin))
            or root.origin not in {"listed_dhatu", "derived_subdhatu"}):
        return {"status": "UNRESOLVED", "reason": "Root origin was not established", "input": asdict(root)}
    marker = designate({"text": root.teaching, "identity": root.lexical_id,
                        "upadesha": root.origin == "listed_dhatu", "category": "root",
                        "vibhakti": False, "taddhita": False,
                        "nasality_complete": root.nasality_complete}, rules)
    if marker["status"] != "LOCAL_DESIGNATION":
        return {"status": "UNRESOLVED", "reason": marker["reason"], "input": asdict(root)}
    original = [{**s, "uid": f"{root.lexical_id}:sound:{s['id']}"} for s in marker["original"]]
    visible = [deepcopy(s) for s in original if s["id"] in marker["visible_ids"]]
    history = [{"rule": "1.3.2–9", "effect": "it_designation_then_lopa",
                "removed_uids": [s["uid"] for s in original if s["id"] not in marker["visible_ids"]],
                "marker_units": deepcopy(marker["marker_units"])}]
    blocked = []
    configuration = json.loads((HERE / "RULES.json").read_text())

    def replace_first(value, sid):
        prior = visible[0]["symbol"]
        visible[0] = {**visible[0], "symbol": value}
        history.append({"rule": sid, "effect": "initial_root_substitution", "target_uid": visible[0]["uid"],
                        "before": prior, "after": value, "source_retained": True})

    if visible and visible[0]["symbol"] == "ṣ":
        if root.origin == "derived_subdhatu":
            blocked.append({"rule": "6.1.64", "reason": "subdhatu exclusion"})
        elif root.lexical_id in configuration["satva_exception_ids"]:
            blocked.append({"rule": "6.1.64", "reason": "Source-identified Kāśikā/Nyāsa exclusion", "lexical_id": root.lexical_id})
        else:
            replace_first("s", "6.1.64")
    if visible and visible[0]["symbol"] == "ṇ":
        if root.origin == "derived_subdhatu":
            blocked.append({"rule": "6.1.65", "reason": "subdhatu exclusion"})
        else:
            replace_first("n", "6.1.65")

    # Unit equality is essential: the i in ñi or ir is not a standalone i-it.
    idit = any(unit["label"] == "i" and unit["rule"] == "1.3.2" for unit in marker["marker_units"])
    if idit:
        symbols = tuple(s["symbol"] for s in visible)
        try:
            suffix = ti_1_1_64(symbols)
        except ValueError:
            return {"status": "UNRESOLVED", "reason": "No vowel remains for ordinary mit placement",
                    "input": asdict(root), "original": original, "marker": marker, "history": history}
        at = len(visible) - len(suffix) + 1
        # Reuse T82 only on its declared ordinary num contract. No complete
        # augment theory or the special masj placement of 7.1.60 is inferred.
        agama = t82_its("nu~m", "agama")
        if placement("nu~m") != "after_last_vowel" or agama["remaining_sounds"] != ("n",):
            raise ValueError("Pinned T82 ordinary num contract changed")
        uid = f"{root.lexical_id}:num:7.1.58"
        inserted = {"uid": uid, "id": None, "symbol": "n", "kind": "consonant",
                    "nasal": False, "accent": "", "offset": None, "introduced_by": "7.1.58"}
        visible = visible[:at] + [inserted] + visible[at:]
        history.append({"rule": "7.1.58", "effect": "num_augment", "placement_rule": "1.1.47",
                        "after_uid": visible[at - 1]["uid"], "inserted_uid": uid,
                        "teaching": "nu~m", "it_evidence": agama["its"]})
    return {"status": "BOUNDED_ROOT_PREPROCESSING", "input": asdict(root),
            "original": original, "marker": marker, "visible": visible,
            "history": history, "blocked": blocked, "idit": idit,
            "projection": "".join(s["symbol"] for s in visible),
            "word_validity": "NOT_EVALUATED", "tripadi_applied": False}


def observed_root(row: dict) -> RootInput | None:
    if row.get("tags") == "ganasutra":
        return None
    # Classification comes from the pinned Dhātupāṭha witness; not the spelling.
    return RootInput(row["i"], row["aupadeshik"], "listed_dhatu", True)


def num_readout(state: dict, *, internal_root: bool) -> dict:
    """Query the inserted num's phonetic realization without feeding it back.

    Only the n introduced by 7.1.58, followed inside the same supplied root
    by jhal, is admitted. This is not a general Tripādī/asiddha resolver.
    """
    if not internal_root or state.get("status") != "BOUNDED_ROOT_PREPROCESSING":
        return {"status": "UNRESOLVED", "reason": "A successful internal-root preprocessing view is required"}
    visible = deepcopy(state["visible"])
    history = []
    stops = tuple(s for group in VARGAS.values() for s in group if s not in NASAL)
    jhal = set(stops) | {"ś", "ṣ", "s", "h"}
    classes = savarna_classes(tuple(s for group in VARGAS.values() for s in group))
    for i, sound in enumerate(visible[:-1]):
        if sound.get("introduced_by") != "7.1.58" or sound["symbol"] != "n":
            continue
        following = visible[i + 1]["symbol"]
        if following not in jhal:
            continue
        visible[i] = {**sound, "symbol": "ṃ", "kind": "ayogavaha"}
        history.append({"rule": "8.3.24", "uid": sound["uid"], "before": "n", "after": "ṃ",
                        "guard": "non-pada-final num followed inside the root by jhal"})
        if following in stops:
            candidates = next(group for group in classes if following in group) & set(NASAL)
            if len(candidates) != 1:
                raise ValueError("T81's admitted stop class no longer has a unique nasal")
            nasal = next(iter(candidates))
            visible[i] = {**visible[i], "symbol": nasal, "kind": "consonant"}
            history.append({"rule": "8.4.58", "uid": sound["uid"], "before": "ṃ", "after": nasal,
                            "guard": "following stop in yay; nasal in its admitted T81 savarṇa class"})
    return {"status": "LOCAL_NUM_PHONETIC_READOUT", "projection": "".join(s["symbol"] for s in visible),
            "visible": visible, "history": history,
            "visibility": "query only; does not replace the pre-Tripādī root state",
            "word_validity": "NOT_EVALUATED"}
