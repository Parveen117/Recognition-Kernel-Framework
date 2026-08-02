from __future__ import annotations

"""Fail-closed public-release text and privacy audit.

This script is intentionally conservative. It scans tracked text files for
private paths, credential-like strings, loaded language that is disallowed in
the public reviewer repository, and explicit RH overclaims.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".tex",
    ".txt",
    ".rst",
    ".json",
    ".yml",
    ".yaml",
    ".toml",
    ".cff",
}

PATTERNS: dict[str, re.Pattern[str]] = {
    "loaded_language": re.compile(
        r"\b(?:contaminat\w*|pollut\w*|violent\s+proof|enemy\s+theorem|truth\s+machine)\b",
        re.IGNORECASE,
    ),
    "rh_overclaim": re.compile(
        r"\b(?:RH\s+is\s+proved|RH\s+is\s+solved|we\s+prove\s+RH|"
        r"complete\s+proof\s+of\s+the\s+Riemann\s+Hypothesis|"
        r"Riemann\s+Hypothesis\s+follows\s+unconditionally)\b",
        re.IGNORECASE,
    ),
    "windows_user_path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+"),
    "github_token": re.compile(r"(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    "openai_like_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "aws_access_key": re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
    "private_address_marker": re.compile(
        r"\b(?:Correspondence\s+Address|House\s+No\.?[- ]?\d+|Pocket[- ]?\d+|"
        r"Sector[- ]?\d+.*Rohini)\b",
        re.IGNORECASE,
    ),
}


def tracked_files() -> list[Path]:
    completed = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return [ROOT / item for item in completed.stdout.splitlines() if item]


def main() -> int:
    findings: list[tuple[str, str, int, str]] = []

    for path in tracked_files():
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        relative = path.relative_to(ROOT).as_posix()
        for line_number, line in enumerate(text.splitlines(), start=1):
            for category, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(
                        (category, relative, line_number, line.strip()[:300])
                    )

    if findings:
        print("FAIL_PUBLIC_RELEASE_AUDIT")
        for category, path, line_number, text in findings:
            print(f"{category}: {path}:{line_number}: {text}")
        return 1

    print("PASS_PUBLIC_RELEASE_AUDIT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
