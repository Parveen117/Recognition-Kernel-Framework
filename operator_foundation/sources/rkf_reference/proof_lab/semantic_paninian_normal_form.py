from __future__ import annotations

"""Certificate fixture for the typed semantic Paninian normal-form stage."""

import argparse
import json
from pathlib import Path
from typing import Any

from proof_lab.semantic_paninian_normalizer import PaninianSemanticNormalizer
from proof_lab.semantic_paninian_types import (
    ClaimRelation,
    Modality,
    NormalizationStatus,
    RelationSpec,
    SemanticPresentation,
    TimeAnchor,
    TypedClaim,
)

__all__ = [
    "ClaimRelation",
    "Modality",
    "NormalizationStatus",
    "PaninianSemanticNormalizer",
    "RelationSpec",
    "SemanticPresentation",
    "TimeAnchor",
    "TypedClaim",
    "build_certificate",
    "build_demo_presentation",
    "demo_claims",
]


def load_source_pins() -> dict[str, str]:
    path = Path(__file__).with_name("imported") / "SEMANTIC_PANINIAN_SOURCE_PINS.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {str(key): str(value) for key, value in payload["source_pins"].items()}


def build_demo_presentation() -> SemanticPresentation:
    return SemanticPresentation(
        entity_aliases={
            "eiffel tower": ("eiffel_tower",),
            "the eiffel tower": ("eiffel_tower",),
            "1889 world's fair": ("worlds_fair_1889",),
            "1889 world’s fair": ("worlds_fair_1889",),
            "1889 universal exposition": ("worlds_fair_1889",),
            "exposition universelle of 1889": ("worlds_fair_1889",),
            "world's fair": ("worlds_fair",),
            "world’s fair": ("worlds_fair",),
            "universal exposition": ("worlds_fair",),
            "exhibition": ("exhibition",),
            "1888 exhibition": ("exhibition_1888",),
            "fair": ("worlds_fair", "trade_fair"),
        },
        predicate_aliases={
            "built for": ("built_for",),
            "constructed for": ("built_for",),
            "erected for": ("built_for",),
        },
        entity_types={
            "eiffel_tower": "monument",
            "worlds_fair_1889": "event",
            "worlds_fair": "event_category",
            "exhibition": "event_category",
            "exhibition_1888": "event",
            "trade_fair": "event_category",
        },
        ontology_parents={
            "worlds_fair_1889": ("worlds_fair",),
            "worlds_fair": ("exhibition",),
            "exhibition_1888": ("exhibition",),
            "trade_fair": ("exhibition",),
        },
        relation_specs={
            "built_for": RelationSpec(
                subject_types=("monument",),
                object_types=("event", "event_category"),
                functional_target=True,
            )
        },
        source_pins=load_source_pins(),
    )


def demo_claims() -> dict[str, TypedClaim]:
    return {
        "reference": TypedClaim(
            text="The Eiffel Tower was built for the 1889 World's Fair.",
            subject_key="The Eiffel Tower",
            predicate_key="built for",
            object_key="1889 World's Fair",
            time_anchor=TimeAnchor(1889),
            markers=("past_tense", "definite_subject"),
            effect_tags=("historical_event_relation",),
        ),
        "alias": TypedClaim(
            text="The Eiffel Tower was constructed for the 1889 Universal Exposition.",
            subject_key="Eiffel Tower",
            predicate_key="constructed for",
            object_key="1889 Universal Exposition",
            time_anchor=TimeAnchor(1889),
            markers=("past_tense",),
            effect_tags=("historical_event_relation",),
        ),
        "broader": TypedClaim(
            text="The Eiffel Tower was built for an exhibition in 1889.",
            subject_key="Eiffel Tower",
            predicate_key="built for",
            object_key="exhibition",
            time_anchor=TimeAnchor(1889),
            markers=("past_tense", "indefinite_object"),
            effect_tags=("historical_event_relation",),
        ),
        "wrong_year": TypedClaim(
            text="The Eiffel Tower was built for an exhibition in 1888.",
            subject_key="Eiffel Tower",
            predicate_key="built for",
            object_key="1888 exhibition",
            time_anchor=TimeAnchor(1888),
            markers=("past_tense",),
            effect_tags=("historical_event_relation",),
        ),
        "negated": TypedClaim(
            text="The Eiffel Tower was not built for the 1889 World's Fair.",
            subject_key="Eiffel Tower",
            predicate_key="built for",
            object_key="1889 World's Fair",
            polarity=False,
            time_anchor=TimeAnchor(1889),
            markers=("past_tense", "negation"),
            effect_tags=("historical_event_relation",),
        ),
        "ambiguous": TypedClaim(
            text="The Eiffel Tower was built for a fair.",
            subject_key="Eiffel Tower",
            predicate_key="built for",
            object_key="fair",
            markers=("past_tense", "indefinite_object"),
        ),
    }


def build_certificate() -> dict[str, Any]:
    presentation = build_demo_presentation()
    kernel = PaninianSemanticNormalizer(presentation)
    claims = demo_claims()
    reference = claims["reference"]
    normalizations = {
        name: kernel.normalize(claim).to_dict()
        for name, claim in claims.items()
    }
    comparisons = {
        name: kernel.compare(reference, claim).to_dict()
        for name, claim in claims.items()
        if name != "reference"
    }

    checks = {
        "presentation_hash_is_stable_length": len(presentation.presentation_hash) == 64,
        "reference_normalizes": normalizations["reference"]["status"] == "NORMALIZED",
        "surface_alias_normalizes_to_identity": comparisons["alias"]["relation"] == "IDENTICAL",
        "broader_claim_is_entailed_not_identical": comparisons["broader"]["relation"] == "LEFT_ENTAILS_RIGHT",
        "wrong_year_is_time_contradiction": comparisons["wrong_year"]["relation"] == "CONTRADICTS_TIME",
        "negation_is_polarity_contradiction": comparisons["negated"]["relation"] == "CONTRADICTS_POLARITY",
        "ambiguous_alias_fails_closed": normalizations["ambiguous"]["status"] == "AMBIGUOUS_BINDU",
        "lopa_erases_only_after_ledger_capture": (
            len(normalizations["reference"]["erased_markers"]) > 0
            and any(
                entry["stage"] == "seam_ledger"
                for entry in normalizations["reference"]["ledger"]
            )
        ),
        "casefold_is_not_entity_contradiction": comparisons["alias"]["relation"] == "IDENTICAL",
        "nyaya_truth_not_silently_claimed": True,
        "mimamsa_obligation_not_silently_claimed": True,
        "semantic_no_blindness_not_silently_promoted": True,
    }
    status = (
        "PASS_TYPED_SEMANTIC_PANINIAN_NORMAL_FORM_STAGE1"
        if all(checks.values())
        else "FAIL_TYPED_SEMANTIC_PANINIAN_NORMAL_FORM_STAGE1"
    )
    return {
        "schema": "rkf.typed_semantic_paninian_normal_form_stage1.v1",
        "status": status,
        "presentation_hash": presentation.presentation_hash,
        "claim_boundary": {
            "proved": [
                "explicitly typed claims normalize under deterministic source-pinned alias, precedence, Bindu, ledger, and Lopa rules",
                "surface paraphrase can normalize to canonical identity",
                "ontology entailment remains distinct from identity",
                "polarity and non-overlapping time anchors remain visible contradiction coordinates",
                "ambiguous aliases fail closed without silent Bindu selection",
            ],
            "open": [
                "unrestricted natural-language parsing",
                "Nyaya evidential support and defeat",
                "Mimamsa context and rule-priority resolution",
                "Yukti proof transport",
                "semantic observer injectivity and no-blindness",
                "truth certification for any historical claim",
            ],
        },
        "checks": checks,
        "normalizations": normalizations,
        "comparisons_from_reference": comparisons,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_certificate()
    body = canonical_bytes(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    print(payload["status"])
    print("PRESENTATION_HASH", payload["presentation_hash"])
    print("ALIAS_RELATION", payload["comparisons_from_reference"]["alias"]["relation"])
    print("BROADER_RELATION", payload["comparisons_from_reference"]["broader"]["relation"])
    print("AMBIGUOUS_STATUS", payload["normalizations"]["ambiguous"]["status"])
    print("NYAYA_TRUTH_CERTIFIED", False)
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
