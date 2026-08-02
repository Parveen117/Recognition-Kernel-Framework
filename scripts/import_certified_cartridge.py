from __future__ import annotations

"""Import the certified mathematical proof-transport cartridge.

The importer reads exact blobs from the pinned source commit using `git show`.
It does not copy the source working tree, so local line endings, notebooks,
uncommitted changes, and generated files cannot silently enter the public repo.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

TARGET_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = TARGET_ROOT / "PUBLIC_EXPORT_MANIFEST.json"
REPORT_PATH = TARGET_ROOT / "PUBLIC_IMPORT_REPORT.json"


def run_git(source: Path, *args: str, input_bytes: bytes | None = None) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(source), *args],
        input=input_bytes,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace")
        raise RuntimeError(f"git {' '.join(args)} failed: {stderr}")
    return completed.stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        required=True,
        help="Local clone of Parveen117/RH-Framework containing the pinned commit.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=TARGET_ROOT,
        help="Local clone of Recognition-Kernel-Framework.",
    )
    parser.add_argument(
        "--run-campaign",
        action="store_true",
        help="Run the certificate campaign after import.",
    )
    args = parser.parse_args()

    source = args.source.resolve()
    target = args.target.resolve()
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    commit = manifest["source_commit"]

    if not (source / ".git").exists():
        raise RuntimeError(f"source is not a Git repository: {source}")
    if not (target / ".git").exists():
        raise RuntimeError(f"target is not a Git repository: {target}")

    # Confirm that the pinned commit object is present locally.
    run_git(source, "cat-file", "-e", f"{commit}^{{commit}}")

    records: list[dict[str, Any]] = []
    for relative in manifest["files"]:
        source_spec = f"{commit}:{relative}"
        expected_blob = run_git(source, "rev-parse", source_spec).decode().strip()
        data = run_git(source, "show", source_spec)
        actual_blob = run_git(source, "hash-object", "--stdin", input_bytes=data).decode().strip()

        if actual_blob != expected_blob:
            raise RuntimeError(
                f"blob mismatch for {relative}: expected {expected_blob}, got {actual_blob}"
            )

        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)

        records.append(
            {
                "path": relative,
                "bytes": len(data),
                "git_blob_sha1": actual_blob,
                "sha256": sha256(data),
            }
        )
        print("IMPORTED", relative, actual_blob)

    report: dict[str, Any] = {
        "schema": "recognition-kernel-public-import-report-v0.1",
        "source_repository": manifest["source_repository"],
        "source_commit": commit,
        "target_repository": "Parveen117/Recognition-Kernel-Framework",
        "file_count": len(records),
        "files": records,
        "archived_campaign_sha256": manifest["archived_campaign_sha256"],
        "scientific_boundary": manifest["scientific_boundary"],
    }
    report["canonical_report_sha256"] = sha256(canonical_json_bytes(report))
    REPORT_PATH.write_text(
        json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print("WROTE", REPORT_PATH.relative_to(target))
    print("IMPORT_REPORT_SHA256", report["canonical_report_sha256"])

    if args.run_campaign:
        completed = subprocess.run(
            [
                sys.executable,
                "certificates/foundation/run_campaign.py",
                "--output",
                "certificates/foundation/campaign_result_reproduced.json",
            ],
            cwd=target,
            text=True,
            capture_output=True,
            check=False,
        )
        print(completed.stdout)
        if completed.stderr:
            print(completed.stderr, file=sys.stderr)
        if completed.returncode != 0:
            return completed.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
