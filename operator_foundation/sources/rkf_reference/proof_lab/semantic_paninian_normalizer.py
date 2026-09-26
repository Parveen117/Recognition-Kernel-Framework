from __future__ import annotations

"""Deterministic normalizer for explicitly typed semantic claims."""

from typing import Mapping

from proof_lab.semantic_paninian_types import (
    CanonicalClaim,
    ClaimRelation,
    ComparisonResult,
    LedgerEntry,
    NormalizationResult,
    NormalizationStatus,
    SemanticPresentation,
    TypedClaim,
)


class PaninianSemanticNormalizer:
    def __init__(self, presentation: SemanticPresentation):
        self.presentation = presentation

    @staticmethod
    def _key(value: str) -> str:
        return " ".join(value.casefold().strip().split())

    def _resolve(
        self,
        raw: str,
        aliases: Mapping[str, tuple[str, ...]],
        kind: str,
        bindu_hint: str | None,
        ledger: list[LedgerEntry],
        trace: list[str],
    ) -> tuple[str | None, NormalizationStatus, tuple[str, ...]]:
        normalized_key = self._key(raw)
        candidates = aliases.get(normalized_key)
        if candidates is None:
            return None, NormalizationStatus.UNKNOWN_SYMBOL, (
                f"unknown {kind}: {raw}",
            )

        trace.append(f"alias:{kind}:{normalized_key}")
        if len(candidates) == 1:
            chosen = candidates[0]
            ledger.append(
                LedgerEntry(
                    stage="ordered_rewrite",
                    rule=f"{kind}_alias",
                    before=raw,
                    after=chosen,
                )
            )
            return chosen, NormalizationStatus.NORMALIZED, tuple()

        if bindu_hint is not None and bindu_hint in candidates:
            ledger.append(
                LedgerEntry(
                    stage="bindu_selection",
                    rule=f"{kind}_bindu_hint",
                    before="|".join(candidates),
                    after=bindu_hint,
                    note="residual ambiguity resolved by explicit typed hint",
                )
            )
            trace.append(f"bindu:{kind}:{bindu_hint}")
            return bindu_hint, NormalizationStatus.NORMALIZED, tuple()

        ledger.append(
            LedgerEntry(
                stage="bindu_selection",
                rule=f"{kind}_ambiguity_open",
                before=raw,
                after="|".join(candidates),
                note="no silent selector is permitted",
            )
        )
        return None, NormalizationStatus.AMBIGUOUS_BINDU, (
            f"ambiguous {kind}: {raw} -> {','.join(candidates)}",
        )

    def normalize(self, claim: TypedClaim) -> NormalizationResult:
        ledger: list[LedgerEntry] = []
        trace: list[str] = []
        unresolved: list[str] = []

        subject_id, subject_status, subject_unresolved = self._resolve(
            claim.subject_key,
            self.presentation.entity_aliases,
            "subject",
            claim.bindu_hint,
            ledger,
            trace,
        )
        unresolved.extend(subject_unresolved)

        predicate_id, predicate_status, predicate_unresolved = self._resolve(
            claim.predicate_key,
            self.presentation.predicate_aliases,
            "predicate",
            claim.bindu_hint,
            ledger,
            trace,
        )
        unresolved.extend(predicate_unresolved)

        object_id, object_status, object_unresolved = self._resolve(
            claim.object_key,
            self.presentation.entity_aliases,
            "object",
            claim.bindu_hint,
            ledger,
            trace,
        )
        unresolved.extend(object_unresolved)

        statuses = (subject_status, predicate_status, object_status)
        if NormalizationStatus.AMBIGUOUS_BINDU in statuses:
            status = NormalizationStatus.AMBIGUOUS_BINDU
        elif NormalizationStatus.UNKNOWN_SYMBOL in statuses:
            status = NormalizationStatus.UNKNOWN_SYMBOL
        else:
            status = NormalizationStatus.NORMALIZED

        canonical: CanonicalClaim | None = None
        if status == NormalizationStatus.NORMALIZED:
            assert subject_id is not None
            assert predicate_id is not None
            assert object_id is not None
            subject_type = self.presentation.entity_types.get(subject_id)
            object_type = self.presentation.entity_types.get(object_id)
            spec = self.presentation.relation_specs.get(predicate_id)
            if subject_type is None or object_type is None or spec is None:
                status = NormalizationStatus.TYPE_GUARD_FAILURE
                unresolved.append("missing entity type or relation specification")
            elif subject_type not in spec.subject_types or object_type not in spec.object_types:
                status = NormalizationStatus.TYPE_GUARD_FAILURE
                unresolved.append(
                    f"type guard failed: {subject_type} -{predicate_id}-> {object_type}"
                )
                ledger.append(
                    LedgerEntry(
                        stage="precedence_resolution",
                        rule="relation_type_guard",
                        before=f"{subject_type}|{predicate_id}|{object_type}",
                        after="OPEN",
                    )
                )
            else:
                ledger.append(
                    LedgerEntry(
                        stage="precedence_resolution",
                        rule="relation_type_guard",
                        before=f"{subject_type}|{predicate_id}|{object_type}",
                        after="CLOSED",
                    )
                )
                trace.append("precedence:relation_type_guard")
                canonical = CanonicalClaim(
                    subject_id=subject_id,
                    predicate_id=predicate_id,
                    object_id=object_id,
                    polarity=claim.polarity,
                    time_anchor=claim.time_anchor,
                    modality=claim.modality,
                    subject_type=subject_type,
                    object_type=object_type,
                    effect_tags=tuple(sorted(set(claim.effect_tags))),
                )

        erased_markers = tuple(sorted(set(claim.markers)))
        for marker in erased_markers:
            ledger.append(
                LedgerEntry(
                    stage="seam_ledger",
                    rule="marker_capture_before_lopa",
                    before=marker,
                    after="LEDGERED",
                )
            )
        if erased_markers:
            trace.append("lopa:grammatical_markers_erased")

        return NormalizationResult(
            status=status,
            surface_text=claim.text,
            canonical=canonical,
            rewrite_trace=tuple(trace),
            ledger=tuple(ledger),
            erased_markers=erased_markers,
            unresolved=tuple(unresolved),
            presentation_hash=self.presentation.presentation_hash,
        )

    def compare(self, left: TypedClaim, right: TypedClaim) -> ComparisonResult:
        left_nf = self.normalize(left)
        right_nf = self.normalize(right)
        surface_equal = self._key(left.text) == self._key(right.text)

        if left_nf.canonical is None or right_nf.canonical is None:
            return ComparisonResult(
                relation=ClaimRelation.UNRESOLVED,
                reasons=tuple(left_nf.unresolved + right_nf.unresolved),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        a = left_nf.canonical
        b = right_nf.canonical
        canonical_equal = a == b
        if canonical_equal:
            return ComparisonResult(
                relation=ClaimRelation.IDENTICAL,
                reasons=("all typed canonical coordinates agree",),
                surface_equal=surface_equal,
                canonical_equal=True,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        if (
            a.subject_id != b.subject_id
            or a.predicate_id != b.predicate_id
            or a.modality != b.modality
        ):
            return ComparisonResult(
                relation=ClaimRelation.INCOMPARABLE,
                reasons=("subject, predicate, or modality differs",),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        if a.polarity != b.polarity:
            return ComparisonResult(
                relation=ClaimRelation.CONTRADICTS_POLARITY,
                reasons=("same typed relation has opposite polarity",),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        if (
            a.time_anchor is not None
            and b.time_anchor is not None
            and not a.time_anchor.overlaps(b.time_anchor)
        ):
            return ComparisonResult(
                relation=ClaimRelation.CONTRADICTS_TIME,
                reasons=("non-overlapping typed time anchors",),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        if a.object_id == b.object_id:
            return ComparisonResult(
                relation=ClaimRelation.COMPATIBLE_TYPED_DIFFERENCE,
                reasons=(
                    "core subject-predicate-object coordinates agree but at least one retained typed coordinate differs",
                ),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        left_ancestors = self.presentation.ancestors(a.object_id)
        right_ancestors = self.presentation.ancestors(b.object_id)
        if b.object_id in left_ancestors:
            return ComparisonResult(
                relation=ClaimRelation.LEFT_ENTAILS_RIGHT,
                reasons=("left object is a typed specialization of right object",),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )
        if a.object_id in right_ancestors:
            return ComparisonResult(
                relation=ClaimRelation.RIGHT_ENTAILS_LEFT,
                reasons=("right object is a typed specialization of left object",),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        spec = self.presentation.relation_specs[a.predicate_id]
        if spec.functional_target:
            return ComparisonResult(
                relation=ClaimRelation.CONTRADICTS_FUNCTIONAL_TARGET,
                reasons=("functional relation has distinct canonical targets",),
                surface_equal=surface_equal,
                canonical_equal=False,
                left_status=left_nf.status,
                right_status=right_nf.status,
            )

        return ComparisonResult(
            relation=ClaimRelation.INCOMPARABLE,
            reasons=("no ontology order or contradiction rule connects the targets",),
            surface_equal=surface_equal,
            canonical_equal=False,
            left_status=left_nf.status,
            right_status=right_nf.status,
        )
