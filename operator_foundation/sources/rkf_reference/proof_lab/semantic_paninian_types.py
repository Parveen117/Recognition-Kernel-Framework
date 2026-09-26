from __future__ import annotations

"""Typed carriers for the semantic Paninian normal-form stage."""

import json
from dataclasses import asdict, dataclass
from enum import Enum
from hashlib import sha256
from typing import Any, Mapping


class Modality(str, Enum):
    ASSERTED = "ASSERTED"
    POSSIBLE = "POSSIBLE"
    REPORTED = "REPORTED"


class NormalizationStatus(str, Enum):
    NORMALIZED = "NORMALIZED"
    AMBIGUOUS_BINDU = "AMBIGUOUS_BINDU"
    UNKNOWN_SYMBOL = "UNKNOWN_SYMBOL"
    TYPE_GUARD_FAILURE = "TYPE_GUARD_FAILURE"


class ClaimRelation(str, Enum):
    IDENTICAL = "IDENTICAL"
    LEFT_ENTAILS_RIGHT = "LEFT_ENTAILS_RIGHT"
    RIGHT_ENTAILS_LEFT = "RIGHT_ENTAILS_LEFT"
    CONTRADICTS_POLARITY = "CONTRADICTS_POLARITY"
    CONTRADICTS_TIME = "CONTRADICTS_TIME"
    CONTRADICTS_FUNCTIONAL_TARGET = "CONTRADICTS_FUNCTIONAL_TARGET"
    COMPATIBLE_TYPED_DIFFERENCE = "COMPATIBLE_TYPED_DIFFERENCE"
    INCOMPARABLE = "INCOMPARABLE"
    UNRESOLVED = "UNRESOLVED"


@dataclass(frozen=True)
class TimeAnchor:
    start_year: int
    end_year: int | None = None

    def __post_init__(self) -> None:
        if self.end_year is not None and self.end_year < self.start_year:
            raise ValueError("end_year must not precede start_year")

    @property
    def final_year(self) -> int:
        return self.start_year if self.end_year is None else self.end_year

    def overlaps(self, other: "TimeAnchor") -> bool:
        return not (
            self.final_year < other.start_year
            or other.final_year < self.start_year
        )

    def to_dict(self) -> dict[str, int | None]:
        return asdict(self)


@dataclass(frozen=True)
class TypedClaim:
    text: str
    subject_key: str
    predicate_key: str
    object_key: str
    polarity: bool = True
    time_anchor: TimeAnchor | None = None
    modality: Modality = Modality.ASSERTED
    markers: tuple[str, ...] = tuple()
    effect_tags: tuple[str, ...] = tuple()
    precedence_context: tuple[str, ...] = tuple()
    bindu_hint: str | None = None


@dataclass(frozen=True)
class RelationSpec:
    subject_types: tuple[str, ...]
    object_types: tuple[str, ...]
    functional_target: bool = False


@dataclass(frozen=True)
class LedgerEntry:
    stage: str
    rule: str
    before: str
    after: str
    note: str = ""

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class CanonicalClaim:
    subject_id: str
    predicate_id: str
    object_id: str
    polarity: bool
    time_anchor: TimeAnchor | None
    modality: Modality
    subject_type: str
    object_type: str
    effect_tags: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "subject_id": self.subject_id,
            "predicate_id": self.predicate_id,
            "object_id": self.object_id,
            "polarity": self.polarity,
            "time_anchor": None if self.time_anchor is None else self.time_anchor.to_dict(),
            "modality": self.modality.value,
            "subject_type": self.subject_type,
            "object_type": self.object_type,
            "effect_tags": list(self.effect_tags),
        }


@dataclass(frozen=True)
class NormalizationResult:
    status: NormalizationStatus
    surface_text: str
    canonical: CanonicalClaim | None
    rewrite_trace: tuple[str, ...]
    ledger: tuple[LedgerEntry, ...]
    erased_markers: tuple[str, ...]
    unresolved: tuple[str, ...]
    presentation_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.value,
            "surface_text": self.surface_text,
            "canonical": None if self.canonical is None else self.canonical.to_dict(),
            "rewrite_trace": list(self.rewrite_trace),
            "ledger": [entry.to_dict() for entry in self.ledger],
            "erased_markers": list(self.erased_markers),
            "unresolved": list(self.unresolved),
            "presentation_hash": self.presentation_hash,
        }


@dataclass(frozen=True)
class ComparisonResult:
    relation: ClaimRelation
    reasons: tuple[str, ...]
    surface_equal: bool
    canonical_equal: bool
    left_status: NormalizationStatus
    right_status: NormalizationStatus

    def to_dict(self) -> dict[str, Any]:
        return {
            "relation": self.relation.value,
            "reasons": list(self.reasons),
            "surface_equal": self.surface_equal,
            "canonical_equal": self.canonical_equal,
            "left_status": self.left_status.value,
            "right_status": self.right_status.value,
        }


@dataclass(frozen=True)
class SemanticPresentation:
    entity_aliases: Mapping[str, tuple[str, ...]]
    predicate_aliases: Mapping[str, tuple[str, ...]]
    entity_types: Mapping[str, str]
    ontology_parents: Mapping[str, tuple[str, ...]]
    relation_specs: Mapping[str, RelationSpec]
    source_pins: Mapping[str, str]

    def canonical_payload(self) -> dict[str, Any]:
        return {
            "entity_aliases": {key: list(self.entity_aliases[key]) for key in sorted(self.entity_aliases)},
            "predicate_aliases": {key: list(self.predicate_aliases[key]) for key in sorted(self.predicate_aliases)},
            "entity_types": {key: self.entity_types[key] for key in sorted(self.entity_types)},
            "ontology_parents": {key: list(self.ontology_parents[key]) for key in sorted(self.ontology_parents)},
            "relation_specs": {
                key: {
                    "subject_types": list(self.relation_specs[key].subject_types),
                    "object_types": list(self.relation_specs[key].object_types),
                    "functional_target": self.relation_specs[key].functional_target,
                }
                for key in sorted(self.relation_specs)
            },
            "source_pins": {key: self.source_pins[key] for key in sorted(self.source_pins)},
        }

    @property
    def presentation_hash(self) -> str:
        body = json.dumps(self.canonical_payload(), sort_keys=True, separators=(",", ":")).encode("utf-8")
        return sha256(body).hexdigest()

    def ancestors(self, entity_id: str) -> frozenset[str]:
        seen: set[str] = set()
        stack = list(self.ontology_parents.get(entity_id, tuple()))
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            stack.extend(self.ontology_parents.get(current, tuple()))
        return frozenset(seen)
