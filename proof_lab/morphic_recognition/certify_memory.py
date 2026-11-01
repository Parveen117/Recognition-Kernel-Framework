"""Source-pinned finite certificates for MR-04 through MR-07.

Ordinary proofs are in the theorem capsules. This executable checks declared
finite contracts; it is not a proof assistant or an external peer review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = Path("theorum/morphic_recognition")
MANIFEST = PACKAGE / "MEMORY_SOURCE_MANIFEST.json"
ARCHIVE = PACKAGE / "MEMORY_CERTIFICATE.json"
THEOREMS = ("MR-04", "MR-05", "MR-06", "MR-07")
PROTOCOL = "rkf-morphic-memory-finite-contract-v1"
REQUIRED_SOURCES = (
    "theorum/morphic_recognition/04_future_complete_linear_recognition.md",
    "theorum/morphic_recognition/05_seam_memory_gluing.md",
    "theorum/morphic_recognition/06_guarded_lopa_future_equivalence.md",
    "theorum/morphic_recognition/07_holonomy_area_scaling.md",
    "theorum/morphic_recognition/02_path_blindness_minimal_memory_repair.md",
    "theorum/61_rewrite_rules_as_cut_module_operators_theorem.md",
    "theorum/morphic_calculus/main.tex",
    "proof_lab/morphic_recognition/memory.py",
    "proof_lab/morphic_recognition/guarded.py",
    "proof_lab/morphic_recognition/holonomy.py",
    "proof_lab/morphic_recognition/certify_memory.py",
    "proof_lab/test_morphic_memory.py",
    "proof_lab/test_guarded_lopa.py",
    "proof_lab/test_holonomy_scaling.py",
    "proof_lab/test_memory_certificate.py",
)


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def check_sources(manifest: dict[str, Any], root: Path = ROOT) -> list[str]:
    """Reject missing, extra, altered, or unpinned required source files."""
    errors = []
    if manifest.get("protocol") != PROTOCOL:
        errors.append("manifest protocol mismatch")
    pins = manifest.get("source_sha256", {})
    if set(pins) != set(REQUIRED_SOURCES):
        errors.append("manifest source set mismatch")
    for relative in REQUIRED_SOURCES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing source: {relative}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != pins.get(relative):
            errors.append(f"stale source: {relative}")
    return errors


def validate_results(results: list[dict[str, Any]],
                     expected: dict[str, list[str]]) -> list[str]:
    """A missing theorem, missing negative control, or vacuous PASS is failure."""
    errors = []
    ids = [r.get("theorem_id") for r in results]
    if sorted(ids) != sorted(THEOREMS) or set(expected) != set(THEOREMS):
        errors.append("theorem coverage mismatch")
    for result in results:
        tid = result.get("theorem_id")
        checks = result.get("checks", [])
        check_ids = [c.get("id") for c in checks]
        required = expected.get(tid, [])
        if (not checks or not required or len(set(check_ids)) != len(check_ids)
                or sorted(check_ids) != sorted(required)):
            errors.append(f"{tid}: obligation coverage mismatch")
        for check in checks:
            if check.get("status") != "pass":
                errors.append(f"{tid}/{check.get('id')}: obligation failed")
    return errors


def check_declared_obligations(manifest: dict[str, Any], root: Path = ROOT) -> list[str]:
    """The manifest must cover the capsule's contract, not just emitted checks."""
    errors = []
    obligations = manifest.get("obligations", {})
    for tid, relative in zip(THEOREMS, REQUIRED_SOURCES[:4]):
        declared = set(re.findall(r"\bMR0[4-7]-[ON]\d+\b",
                                   (root / relative).read_text(encoding="utf-8")))
        expected = obligations.get(tid, [])
        if not declared or declared != set(expected) or len(expected) != len(set(expected)):
            errors.append(f"{tid}: manifest does not match theorem-declared obligations")
    return errors


def collect_results() -> list[dict[str, Any]]:
    from .memory import verify_memory_contract
    from .guarded import verify_guarded_contract
    from .holonomy import verify_holonomy_contract

    memory = verify_memory_contract()
    if isinstance(memory, dict):
        memory = memory["theorems"]
    return [*memory, verify_guarded_contract(), verify_holonomy_contract()]


def build_certificate() -> dict[str, Any]:
    manifest_path = ROOT / MANIFEST
    if not manifest_path.is_file():
        raise ValueError("source manifest missing; verification cannot seal its own inputs")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = check_sources(manifest, ROOT)
    results: list[dict[str, Any]] = []
    if not errors:
        errors += check_declared_obligations(manifest, ROOT)
    if not errors:
        results = collect_results()
        errors += validate_results(results, manifest.get("obligations", {}))
    packet = {
        "protocol": PROTOCOL,
        "status": "PASS" if not errors else ("STALE" if not results else "FAIL"),
        "source_manifest_sha256": digest(manifest),
        "source_sha256": manifest.get("source_sha256", {}),
        "theorem_count": len(results),
        "theorems": results,
        "errors": errors,
        "claim_boundary": {
            "mathematics": "ordinary proofs under the hypotheses in MR-04 through MR-07",
            "computational": "declared finite exact arithmetic obligations only",
            "formal_proof_assistant": False,
            "external_peer_review": False,
            "novelty_priority_established": False,
            "unrestricted_smooth_gluing": False,
            "physical_tvsp_identification": False,
            "full_historical_manuscript_certification": False,
        },
    }
    packet["certificate_sha256"] = digest(packet)
    return packet


def check_record(packet: dict[str, Any]) -> bool:
    content = dict(packet)
    claimed = content.pop("certificate_sha256", None)
    return claimed == digest(content)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-archive", action="store_true")
    args = parser.parse_args()
    packet = build_certificate()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n",
                               encoding="utf-8")
    if args.check_archive:
        archived = json.loads((ROOT / ARCHIVE).read_text(encoding="utf-8"))
        if not check_record(archived) or archived != packet:
            print("FAIL: archived certificate does not reproduce")
            return 1
    print(f"{packet['status']}: {packet['theorem_count']} theorem contracts; "
          f"sha256={packet['certificate_sha256']}")
    for error in packet["errors"]:
        print(error)
    return 0 if packet["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
