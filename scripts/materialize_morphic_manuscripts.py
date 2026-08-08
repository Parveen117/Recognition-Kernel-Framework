#!/usr/bin/env python3
"""Hash-pinned bootstrap for Morphic Algebra / Morphic Calculus certification.

The substantive builder is stored as gzip+base64 chunks so the repository can
reconstruct it deterministically without depending on this chat session.
"""
from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path
import subprocess
import sys

EXPECTED_BUILDER_SHA256 = "410e65071876c212f371188545cb9dca930fd8bebef07eff6869eec7ef7673de"


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    chunk_dir = repo / "scripts" / "morphic_cert_builder_chunks"
    parts = sorted(chunk_dir.glob("builder.py.gz.b64.part*"))
    if not parts:
        raise SystemExit("No Morphic certification builder chunks found")

    encoded = "".join(part.read_text(encoding="ascii").strip() for part in parts)
    builder = gzip.decompress(base64.b64decode(encoded))
    digest = hashlib.sha256(builder).hexdigest()
    if digest != EXPECTED_BUILDER_SHA256:
        raise SystemExit(
            f"Morphic certification builder SHA mismatch: {digest} != {EXPECTED_BUILDER_SHA256}"
        )

    generated = repo / "scripts" / "_generated_morphic_builder.py"
    try:
        generated.write_bytes(builder)
        completed = subprocess.run(
            [sys.executable, str(generated), *sys.argv[1:]],
            cwd=repo,
            check=False,
        )
        return completed.returncode
    finally:
        generated.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
