"""Adversarial source and obligation integrity for the MR-04--07 packet."""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from proof_lab.morphic_recognition.certify_memory import (
    ARCHIVE, MANIFEST, PROTOCOL, REQUIRED_SOURCES, ROOT, THEOREMS,
    build_certificate, check_declared_obligations, check_record, check_sources,
    digest, validate_results,
)


class MemoryCertificateTests(unittest.TestCase):
    def test_archive_reproduces_from_current_sources(self):
        packet = build_certificate()
        self.assertEqual(packet["status"], "PASS", packet["errors"])
        archived = json.loads((ROOT / ARCHIVE).read_text(encoding="utf-8"))
        self.assertTrue(check_record(archived))
        self.assertEqual(packet, archived)
        self.assertFalse(packet["claim_boundary"]["formal_proof_assistant"])
        self.assertFalse(packet["claim_boundary"]["external_peer_review"])

    def test_missing_and_modified_sources_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pins = {}
            for relative in REQUIRED_SOURCES:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(relative, encoding="utf-8")
                pins[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
            manifest = {"protocol": PROTOCOL, "source_sha256": pins}
            self.assertEqual(check_sources(manifest, root), [])
            victim = root / REQUIRED_SOURCES[0]
            victim.write_text("changed theorem", encoding="utf-8")
            self.assertTrue(any("stale source" in e for e in check_sources(manifest, root)))
            victim.unlink()
            self.assertTrue(any("missing source" in e for e in check_sources(manifest, root)))
            del pins[REQUIRED_SOURCES[1]]
            self.assertIn("manifest source set mismatch", check_sources(manifest, root))

    def test_failed_missing_duplicate_and_empty_obligations_are_rejected(self):
        expected = {tid: [f"{tid}-example"] for tid in THEOREMS}
        results = [{"theorem_id": tid, "checks": [
            {"id": expected[tid][0], "status": "pass"}]} for tid in THEOREMS]
        self.assertEqual(validate_results(results, expected), [])
        failed = copy.deepcopy(results)
        failed[0]["checks"][0]["status"] = "fail"
        self.assertTrue(validate_results(failed, expected))
        self.assertTrue(validate_results(results[:-1], expected))
        duplicated = copy.deepcopy(results)
        duplicated[0]["checks"] *= 2
        self.assertTrue(validate_results(duplicated, expected))
        empty = copy.deepcopy(results)
        empty[0]["checks"] = []
        self.assertTrue(validate_results(empty, expected))
        self.assertTrue(validate_results(results, {}))

    def test_certificate_tampering_is_detected(self):
        packet = {"status": "FAIL", "theorems": []}
        packet["certificate_sha256"] = digest(packet)
        self.assertTrue(check_record(packet))
        packet["status"] = "PASS"
        self.assertFalse(check_record(packet))

    def test_manifest_cannot_silently_drop_a_declared_negative_control(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            obligations = {}
            for tid, relative in zip(THEOREMS, REQUIRED_SOURCES[:4]):
                prefix = tid.replace("-", "")
                ids = [f"{prefix}-O1", f"{prefix}-N1"]
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("\n".join(ids), encoding="utf-8")
                obligations[tid] = ids
            manifest = {"obligations": obligations}
            self.assertEqual(check_declared_obligations(manifest, root), [])
            obligations["MR-04"].pop()
            self.assertTrue(check_declared_obligations(manifest, root))


if __name__ == "__main__":
    unittest.main()
