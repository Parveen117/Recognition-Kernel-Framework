from __future__ import annotations

"""Write the Stage-1.5 certificate with canonical UTF-8/LF bytes."""

import argparse
import json
from pathlib import Path

from proof_lab.clock_free_cut_memory_stage15_examples import build_certificate


def canonical_bytes() -> bytes:
    return (
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(canonical_bytes())

    result = build_certificate()
    print(result["status"])
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
