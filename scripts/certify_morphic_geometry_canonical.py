#!/usr/bin/env python3
"""Run the Morphic Geometry certifier from its canonical provenance snapshot.

The first import was manually staged under morphic_calculus. After successful
byte-for-byte materialization, source_original.tex in morphic_geometry becomes
the canonical immutable input for all subsequent certification runs.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPL = ROOT / "scripts" / "certify_morphic_geometry.py"

spec = importlib.util.spec_from_file_location("morphic_geometry_cert_impl", IMPL)
if spec is None or spec.loader is None:
    raise SystemExit("Could not load Morphic Geometry certifier")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# The canonical input is now the exact hash-pinned snapshot in its own folder.
mod.SOURCE = mod.ORIGINAL

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"prepare", "finalize", "verify"}:
        print("usage: certify_morphic_geometry_canonical.py {prepare|finalize|verify}", file=sys.stderr)
        raise SystemExit(2)
    {"prepare": mod.prepare, "finalize": mod.finalize, "verify": mod.verify}[sys.argv[1]]()
