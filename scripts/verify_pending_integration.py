"""Read-only integrity audit of the 1 November 2026 branch integration.

This checks Git ancestry and source bytes, not mathematical truth. No evidence
file or expected hash is generated or replaced by this command.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "research-history/PENDING_WORK_2026_11_01.json"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def local_bindings(data: dict):
    for group in ("unchanged_local_inputs", "new_stage_arithmetic", "new_stage_theorems"):
        for path, record in data.get(group, {}).items():
            yield path, record["sha256"]
    yield from data.get("sha256", {}).items()
    for group in ("local_files", "inputs"):
        for record in data.get(group, []):
            if record.get("repository", "Parveen117/Recognition-Kernel-Framework") == "Parveen117/Recognition-Kernel-Framework":
                yield record["path"], record["sha256"]


def verify() -> dict:
    record = json.loads(MANIFEST.read_text())
    base = record["base_commit"]
    heads = {b["branch"]: b for b in record["branch_snapshot"]}
    for branch, item in heads.items():
        require(subprocess.run(["git", "merge-base", "--is-ancestor", item["sha"], "HEAD"], cwd=ROOT).returncode == 0,
                f"Unintegrated history: {branch}")

    # The corrected root snapshot was already imported intact by the canonical
    # operator migration; an older active engine must not replace that successor.
    corrected = heads["corrections/native-prerequisites-2026-09-25"]["sha"]
    require(git("rev-parse", corrected + "^{tree}").decode().strip() == record["corrected_reference_tree"], "Correction tree mismatch")
    require(git("rev-parse", "HEAD:operator_foundation/sources/rkf_reference").decode().strip() == record["corrected_reference_tree"], "Canonical corrected reference changed")
    require(git("rev-parse", "HEAD:operator_foundation").decode().strip() == record["canonical_operator_tree"], "Canonical engine tree changed")
    require(git("diff", base, "--", "operator_foundation", "MATHEMATICS_INDEX_2026_09_16.md", "PATENT_NOTICE.md", "GOVERNANCE.md", "RESEARCH_PROVENANCE.md") == b"", "Frozen engine, register, notice or dated provenance changed")

    imported_files = 0
    for branch in (
        "agent/morphic-memory-certification-2026-09-18",
        "agent/rh-source-energy-tail",
        "structure-report-r3",
        "docs/lambda-first-policy-2026-10-10",
    ):
        head = heads[branch]["sha"]
        ancestor = git("merge-base", base, head).decode().strip()
        paths = git("diff", "--name-only", "--diff-filter=AM", ancestor, head).decode().splitlines()
        for path in paths:
            # These navigation surfaces combine multiple lineages. All theorem,
            # implementation, evidence, policy and workflow files remain exact.
            if path in {"MATHEMATICS_INDEX.md", "CERTIFICATE_INDEX.md"}:
                continue
            require((ROOT / path).read_bytes() == git("show", f"{head}:{path}"), f"Imported source changed: {branch}:{path}")
            imported_files += 1

    historical = record["historical_policy"]
    saved_policy = (ROOT / historical["path"]).read_bytes()
    require(sha(saved_policy) == historical["sha256"], "Historical policy snapshot changed")
    require(saved_policy == git("show", historical["source_commit"] + ":AGENTS.md"), "Historical policy provenance changed")
    require((ROOT / ".node-version").read_text().strip() == "22.16.0", "Frozen evidence runtime mismatch")

    manifests = sorted((ROOT / "papers/rkf_completed_weil_endpoint/development").glob("*PINS.json"))
    manifests += sorted((ROOT / "research/lambda_counting").glob("*PINS.json"))
    live = 0
    policy_refs = []
    for manifest in manifests:
        data = json.loads(manifest.read_text())
        for path, expected in local_bindings(data):
            actual = sha((ROOT / path).read_bytes())
            if actual == expected:
                live += 1
            elif (path == "AGENTS.md" and expected == historical["sha256"]
                  and manifest.name in {f"SE{i}_SOURCE_PINS.json" for i in range(9, 18)}):
                # Explicit provenance exception, not a current-file PASS or a
                # replacement pin. The old policy remains independently bound.
                policy_refs.append(manifest.relative_to(ROOT).as_posix())
            else:
                raise ValueError(f"Source mismatch: {manifest.relative_to(ROOT)}: {path}")

    return {
        "status": "PASS_INTEGRATION_INTEGRITY",
        "branch_heads_in_ancestry": len(heads),
        "imported_files_byte_identical": imported_files,
        "source_manifests": len(manifests),
        "current_local_bindings_match": live,
        "historical_policy_bindings": len(policy_refs),
        "historical_policy_manifests": policy_refs,
        "canonical_operator_unchanged": True,
        "universal_theorems_reproved": False,
        "historical_numerical_campaigns_replayed": False,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
