from __future__ import annotations

"""Fail-closed public-release text and privacy audit.

The audit scans tracked and untracked non-ignored text files for private paths,
credential-like strings, disallowed loaded rhetoric, and explicit RH
overclaims. Pattern fragments are assembled at runtime so the audit does not
flag its own rule definitions.
"""

import re
import subprocess
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

# Keep the public repository free of loaded or promotional phrasing while
# avoiding literal self-matches inside this audit source.
_LOADED_TERMS = (
    "contam" + r"inat\w*",
    "poll" + r"ut\w*",
    "viol" + r"ent\s+proof",
    "ene" + r"my\s+theorem",
    "tru" + r"th\s+machine",
)

PATTERNS: dict[str, re.Pattern[str]] = {
    "loaded_language": re.compile(
        r"\b(?:" + "|".join(_LOADED_TERMS) + r")\b",
        re.IGNORECASE,
    ),
    "rh_overclaim": re.compile(
        r"\b(?:RH\s+is\s+proved|RH\s+is\s+solved|we\s+prove\s+RH|"
        r"complete\s+proof\s+of\s+the\s+Riemann\s+Hypothesis|"
        r"Riemann\s+Hypothesis\s+follows\s+unconditionally)\b",
        re.IGNORECASE,
    ),
    "windows_user_path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+"),
    "github_token": re.compile(
        r"(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"
    ),
    "openai_like_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "aws_access_key": re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
    "private_address_marker": re.compile(
        r"\b(?:Correspondence\s+Address|House\s+No\.?[- ]?\d+|"
        r"Pocket[- ]?\d+|Sector[- ]?\d+.*Rohini)\b",
        re.IGNORECASE,
    ),
}

# A reviewed, explicitly negative statement in an immutable source packet.
# Match the complete wording and path, not a generic "No" or a whole file:
# different wording and any additional positive claim still fail closed.
REVIEWED_RH_DENIALS = {
    "papers/rkf_completed_weil_endpoint/development/SE19_RETAINED_RESIDUAL_POLE_RECOVERY.md": (
        "No smaller numerical anchor,\n"
        "eta-zero sign, historical five-label identification, K0 or RH is "
        "proved.",
    ),
}


def audit_text(relative: str, text: str) -> list[tuple[str, str, int, str]]:
    reviewed_spans = [
        (match.start(), match.end())
        for statement in REVIEWED_RH_DENIALS.get(relative, ())
        for match in re.finditer(re.escape(statement), text)
    ]
    findings: list[tuple[str, str, int, str]] = []
    offset = 0
    for line_number, line in enumerate(text.splitlines(keepends=True), start=1):
        for category, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                if category == "rh_overclaim" and any(
                    start <= offset + match.start()
                    and offset + match.end() <= end
                    for start, end in reviewed_spans
                ):
                    continue
                findings.append(
                    (category, relative, line_number, line.strip()[:300])
                )
        offset += len(line)
    return findings


def candidate_files() -> list[Path]:
    completed = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return sorted(
        {ROOT / item for item in completed.stdout.splitlines() if item}
    )


def main() -> int:
    findings: list[tuple[str, str, int, str]] = []

    for path in candidate_files():
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        relative = path.relative_to(ROOT).as_posix()
        findings.extend(audit_text(relative, text))

    if findings:
        print("FAIL_PUBLIC_RELEASE_AUDIT")
        for category, path, line_number, text in findings:
            print(f"{category}: {path}:{line_number}: {text}")
        return 1

    print("PASS_PUBLIC_RELEASE_AUDIT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
