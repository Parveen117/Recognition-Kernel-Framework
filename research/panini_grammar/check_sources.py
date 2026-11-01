"""Read-only PG1 text/provenance checks; no Sanskrit derivation engine."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def check(root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    packet = root / "research/panini_grammar"
    pins = json.loads((packet / "SOURCE_PINS.json").read_text(encoding="utf-8"))
    catalogue = pins["catalogue"]
    path = root / catalogue["path"]
    errors: list[str] = []
    if hashlib.sha256(path.read_bytes()).hexdigest() != catalogue["sha256"]:
        errors.append("SUTRAPATHA.tsv digest differs from the reviewed text")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != catalogue["columns"]:
            return errors + ["Unexpected catalogue columns"], {}
        rows = list(reader)
    ids: set[str] = set()
    keys: set[str] = set()
    counts: Counter[str] = Counter()
    order: list[tuple[int, int, int]] = []
    for row in rows:
        sid, key, sanskrit = (row.get(name) for name in catalogue["columns"])
        if None in row or not sid or not key or not sanskrit:
            errors.append("Malformed or empty catalogue field")
            continue
        try:
            a, p, n = map(int, sid.split("."))
        except ValueError:
            errors.append(f"Invalid sūtra identifier: {sid}")
            continue
        if not (1 <= a <= 8 and 1 <= p <= 4 and n >= 1):
            errors.append(f"Out-of-range identifier: {sid}")
        if key != f"{a}{p}{n:03d}":
            errors.append(f"Source-key mismatch: {sid}")
        if sid in ids or key in keys:
            errors.append(f"Duplicate source identity: {sid}")
        ids.add(sid)
        keys.add(key)
        counts[f"{a}.{p}"] += 1
        order.append((a, p, n))
    if order != sorted(order):
        errors.append("Catalogue is not in sūtra order")
    if dict(counts) != catalogue["pada_record_counts"]:
        errors.append("Pāda counts differ from the pinned edition")
    for ap, count in catalogue["pada_record_counts"].items():
        if not {f"{ap}.{n}" for n in range(1, count + 1)} <= ids:
            errors.append(f"Missing numbered entry in pāda {ap}")
    if len(rows) != pins["external"]["record_counts"]["sutrapatha"]:
        errors.append("Total record count differs from the source inventory")
    foundation = pins["foundation"]
    selected = foundation["ids"]
    if len(set(selected)) != foundation["count"] or len(selected) != foundation["count"]:
        errors.append("Foundation IDs are duplicated or count differs")
    if not set(selected) <= ids:
        errors.append("A foundation sūtra is absent from the catalogue")
    for relative, expected in pins["local_source_sha256"].items():
        source = root / relative
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
            errors.append(f"Historical source changed: {relative}")
    return errors, {"sutras": len(rows), "padas": len(counts), "foundation": len(selected)}


if __name__ == "__main__":
    errors, counts = check()
    if errors:
        for error in errors:
            print("FAIL", error)
        raise SystemExit(1)
    print("PASS_PG1_SOURCE_INTEGRITY", json.dumps(counts, sort_keys=True))
    print("Text/provenance check only; linguistic completeness is not asserted.")
