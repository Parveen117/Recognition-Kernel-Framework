from __future__ import annotations

"""Run implemented RH-Framework foundation certificate packages.

This orchestrator does not turn missing packages into passes. It discovers only
packages that contain a verify.py, executes each verifier in a subprocess, and
writes a machine-readable campaign summary. A package is PASS only when its own
process exits zero and its result JSON reports a PASS status.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
FOUNDATION = ROOT / "certificates" / "foundation"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def discover_packages() -> list[Path]:
    packages: list[Path] = []
    for verifier in FOUNDATION.glob("*/verify.py"):
        if verifier.parent.name.startswith("_"):
            continue
        packages.append(verifier.parent)
    return sorted(packages, key=lambda path: path.name)


def run_package(package: Path) -> dict[str, Any]:
    verifier = package / "verify.py"
    result_path = package / "result.json"
    if result_path.exists():
        result_path.unlink()

    completed = subprocess.run(
        [sys.executable, str(verifier), "--output", str(result_path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    result: dict[str, Any] | None = None
    parse_error: str | None = None
    if result_path.exists():
        try:
            result = json.loads(result_path.read_text(encoding="utf-8"))
        except Exception as exc:  # fail closed
            parse_error = f"{type(exc).__name__}: {exc}"

    reported_status = result.get("status") if isinstance(result, dict) else None
    passed = completed.returncode == 0 and isinstance(reported_status, str) and reported_status.startswith("PASS")

    return {
        "package": package.name,
        "verifier": verifier.relative_to(ROOT).as_posix(),
        "result": result_path.relative_to(ROOT).as_posix(),
        "returncode": completed.returncode,
        "reported_status": reported_status,
        "passed": passed,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "parse_error": parse_error,
        "result_sha256": (
            sha256_bytes(result_path.read_bytes()) if result_path.exists() else None
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=FOUNDATION / "campaign_result.json",
    )
    args = parser.parse_args()

    packages = discover_packages()
    records = [run_package(package) for package in packages]
    all_passed = bool(records) and all(record["passed"] for record in records)

    summary: dict[str, Any] = {
        "schema": "rh-framework-foundation-campaign-v0.1",
        "status": (
            "PASS_IMPLEMENTED_FOUNDATION_CERTIFICATE_CAMPAIGN"
            if all_passed
            else "INCONCLUSIVE_IMPLEMENTED_FOUNDATION_CERTIFICATE_CAMPAIGN"
        ),
        "implemented_package_count": len(records),
        "packages": records,
        "missing_planned_packages_are_not_passes": True,
        "scientific_boundary": {
            "implemented_packages_only": True,
            "active_band_source_positivity": "OPEN",
            "eta_zero_endpoint": "OPEN",
            "riemann_hypothesis": "OPEN",
        },
    }
    summary["canonical_summary_sha256"] = sha256_bytes(canonical_bytes(summary))

    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(summary["status"])
    print(summary["canonical_summary_sha256"])
    for record in records:
        print(record["package"], record["reported_status"], record["returncode"])

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
