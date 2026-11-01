"""Regressions for the reviewed SE19 denial, without exempting its whole file."""

import unittest

from scripts.public_release_audit import REVIEWED_RH_DENIALS, ROOT, audit_text


class PublicReleaseAuditTests(unittest.TestCase):
    path = "papers/rkf_completed_weil_endpoint/development/SE19_RETAINED_RESIDUAL_POLE_RECOVERY.md"
    positive = "RH is " + "proved."

    def setUp(self):
        self.denial = REVIEWED_RH_DENIALS[self.path][0]

    def test_actual_immutable_packet_is_not_an_overclaim(self):
        source = (ROOT / self.path).read_text(encoding="utf-8")
        self.assertIn(self.denial, source)
        self.assertEqual(audit_text(self.path, source), [])

    def test_missing_negation_is_rejected(self):
        findings = audit_text(self.path, self.denial.replace("No smaller", "A smaller"))
        self.assertEqual([f[0] for f in findings], ["rh_overclaim"])
        self.assertEqual(findings[0][2], 2)

    def test_changed_wording_requires_review(self):
        findings = audit_text(self.path, self.denial.replace("anchor", "bound"))
        self.assertEqual([f[0] for f in findings], ["rh_overclaim"])

    def test_exception_is_limited_to_its_reviewed_path(self):
        findings = audit_text("README.md", self.denial)
        self.assertEqual([f[0] for f in findings], ["rh_overclaim"])

    def test_additional_claim_on_same_line_is_rejected(self):
        findings = audit_text(self.path, self.denial + " " + self.positive)
        self.assertEqual([f[0] for f in findings], ["rh_overclaim"])
        self.assertEqual(findings[0][2], 2)

    def test_additional_claim_on_next_line_is_rejected(self):
        findings = audit_text(self.path, self.denial + "\n" + self.positive)
        self.assertEqual([f[0] for f in findings], ["rh_overclaim"])
        self.assertEqual(findings[0][2], 3)

    def test_other_audit_categories_still_apply(self):
        token = "ghp_" + "a" * 24
        findings = audit_text(self.path, self.denial + "\n" + token)
        self.assertEqual([f[0] for f in findings], ["github_token"])


if __name__ == "__main__":
    unittest.main()
