from __future__ import annotations

import unittest

from proof_lab.semantic_paninian_normal_form import (
    ClaimRelation,
    NormalizationStatus,
    PaninianSemanticNormalizer,
    TimeAnchor,
    TypedClaim,
    build_certificate,
    build_demo_presentation,
    demo_claims,
)


class SemanticPaninianNormalFormTests(unittest.TestCase):
    def setUp(self) -> None:
        self.presentation = build_demo_presentation()
        self.kernel = PaninianSemanticNormalizer(self.presentation)
        self.claims = demo_claims()

    def test_certificate_passes(self) -> None:
        payload = build_certificate()
        self.assertEqual(
            payload["status"],
            "PASS_TYPED_SEMANTIC_PANINIAN_NORMAL_FORM_STAGE1",
        )
        self.assertTrue(all(payload["checks"].values()))

    def test_alias_paraphrase_is_canonical_identity(self) -> None:
        result = self.kernel.compare(
            self.claims["reference"],
            self.claims["alias"],
        )
        self.assertEqual(result.relation, ClaimRelation.IDENTICAL)
        self.assertFalse(result.surface_equal)

    def test_ontology_entailment_is_not_identity(self) -> None:
        result = self.kernel.compare(
            self.claims["reference"],
            self.claims["broader"],
        )
        self.assertEqual(result.relation, ClaimRelation.LEFT_ENTAILS_RIGHT)
        self.assertFalse(result.canonical_equal)

    def test_time_and_polarity_remain_visible(self) -> None:
        time_result = self.kernel.compare(
            self.claims["reference"],
            self.claims["wrong_year"],
        )
        polarity_result = self.kernel.compare(
            self.claims["reference"],
            self.claims["negated"],
        )
        self.assertEqual(time_result.relation, ClaimRelation.CONTRADICTS_TIME)
        self.assertEqual(
            polarity_result.relation,
            ClaimRelation.CONTRADICTS_POLARITY,
        )

    def test_ambiguous_bindus_fail_closed(self) -> None:
        result = self.kernel.normalize(self.claims["ambiguous"])
        self.assertEqual(result.status, NormalizationStatus.AMBIGUOUS_BINDU)
        self.assertIsNone(result.canonical)
        self.assertTrue(result.unresolved)

    def test_explicit_bindu_hint_resolves_only_named_candidate(self) -> None:
        hinted = TypedClaim(
            text="The Eiffel Tower was built for a fair.",
            subject_key="Eiffel Tower",
            predicate_key="built for",
            object_key="fair",
            bindu_hint="worlds_fair",
        )
        result = self.kernel.normalize(hinted)
        self.assertEqual(result.status, NormalizationStatus.NORMALIZED)
        self.assertIsNotNone(result.canonical)
        assert result.canonical is not None
        self.assertEqual(result.canonical.object_id, "worlds_fair")
        self.assertTrue(any(entry.stage == "bindu_selection" for entry in result.ledger))

    def test_markers_are_ledgered_before_lopa(self) -> None:
        result = self.kernel.normalize(self.claims["reference"])
        self.assertIn("past_tense", result.erased_markers)
        captured = {
            entry.before
            for entry in result.ledger
            if entry.stage == "seam_ledger"
        }
        self.assertIn("past_tense", captured)

    def test_case_only_surface_change_does_not_create_contradiction(self) -> None:
        lower = TypedClaim(
            text="the eiffel tower was built for the 1889 world's fair.",
            subject_key="the eiffel tower",
            predicate_key="built for",
            object_key="1889 world's fair",
            time_anchor=TimeAnchor(1889),
            markers=("past_tense",),
            effect_tags=("historical_event_relation",),
        )
        result = self.kernel.compare(self.claims["reference"], lower)
        self.assertEqual(result.relation, ClaimRelation.IDENTICAL)

    def test_same_core_with_different_effect_tags_is_not_identity(self) -> None:
        altered = TypedClaim(
            text=self.claims["reference"].text,
            subject_key="Eiffel Tower",
            predicate_key="built for",
            object_key="1889 World's Fair",
            time_anchor=TimeAnchor(1889),
            markers=("past_tense",),
            effect_tags=("different_effect_coordinate",),
        )
        result = self.kernel.compare(self.claims["reference"], altered)
        self.assertEqual(
            result.relation,
            ClaimRelation.COMPATIBLE_TYPED_DIFFERENCE,
        )
        self.assertFalse(result.canonical_equal)

    def test_unknown_symbol_does_not_guess(self) -> None:
        unknown = TypedClaim(
            text="The Eiffel Tower was built for some thing.",
            subject_key="Eiffel Tower",
            predicate_key="built for",
            object_key="some thing",
        )
        result = self.kernel.normalize(unknown)
        self.assertEqual(result.status, NormalizationStatus.UNKNOWN_SYMBOL)
        self.assertIsNone(result.canonical)


if __name__ == "__main__":
    unittest.main()
