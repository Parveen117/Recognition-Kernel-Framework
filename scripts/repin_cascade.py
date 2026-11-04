"""Re-pin cascade: after a change to one of the rule tables, every certificate that reads it is re-run, and where its digest
moved the pin is rewritten, the hash in CERTIFICATE_INDEX.md replaced, and the standard note appended to the certificate's
capsule — old pin, commit that holds it, new pin, the headline numbers read from the new certificate. Then the ledger is
rebuilt and the kernel re-pinned the same way. The pinned history is never rewritten: the old pin's line stays in the index
of its own theorem and the note names the commit at which it held.

    python3.12 -B -W ignore scripts/repin_cascade.py --by 163 [--only pg_replay,panini_isa] [--dry]

Prints, per certificate: unchanged / re-pinned old → new, and the numbers. Exit 1 if a certificate fails to build.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent
PY = [sys.executable, "-B", "-W", "ignore"]

# module → (pin file, capsule that carries the re-pin notes, headline extractor)
CASCADE = [
    ("ting_rule_table_engine", "TING_RULE_TABLE_ENGINE_EXPECTED.sha256", "theorum/149_ting_rule_table_engine_san_theorem.md"),
    ("krt_rule_table_engine", "KRT_RULE_TABLE_ENGINE_EXPECTED.sha256", "theorum/151_krt_rule_table_engine_theorem.md"),
    ("krdanta_sup", "KRDANTA_SUP_EXPECTED.sha256", "theorum/153_krdanta_declension_theorem.md"),
    ("panini_isa", "PANINI_ISA_EXPECTED.sha256", "theorum/150_panini_isa_theorem.md"),
    ("pg_replay", "PG_REPLAY_EXPECTED.sha256", "theorum/154_written_construction_replay_theorem.md"),
    ("pg_written_replay", "PG_WRITTEN_REPLAY_EXPECTED.sha256", "theorum/155_written_construction_replay_ii_theorem.md"),
    ("pg_modal_registers", "PG_MODAL_REGISTERS_EXPECTED.sha256", "theorum/156_written_modal_registers_replay_theorem.md"),
    ("pg_modal_registers_ii", "PG_MODAL_REGISTERS_II_EXPECTED.sha256", "theorum/157_written_modal_registers_replay_ii_theorem.md"),
    ("pg_modal_registers_iii", "PG_MODAL_REGISTERS_III_EXPECTED.sha256", "theorum/159_written_modal_registers_replay_iii_theorem.md"),
]
KERNEL = ("panini_kernel", "PANINI_KERNEL_EXPECTED.sha256", "theorum/142_panini_kernel_theorem.md")


def headline(mod: str, c: dict) -> str:
    """The numbers a reader of the capsule wants, read from the certificate itself."""
    try:
        if mod == "ting_rule_table_engine":
            s = c["t1_suite"]; lanes = []
            for k, name in (("open_lane", "open"), ("ardhadhatuka_lane", "ārdhadhātuka"), ("karmani_lane", "karmaṇi"), ("nic_lane", "ṇic"), ("san_lane", "san")):
                lanes.append(f"{name} {s[k]['agree']:,} / {s[k]['cells']:,}")
            return f"{s['cells']:,} suite cells; the lanes " + ", ".join(lanes)
        if mod == "krt_rule_table_engine":
            l = c.get("lane") or c.get("t2_lane") or {}
            return f"the lane {l.get('agree', '?'):,} / {l.get('cells', '?'):,}" if l else ""
        if mod == "krdanta_sup":
            l = c.get("lane") or c.get("t1_lane") or {}
            return f"{l.get('agree', '?'):,} / {l.get('cells', '?'):,} cells" if l else ""
        if mod == "pg_replay":
            r = c["replay"]["totals"]
            return f"{r['replayed']} replayed, {r['agree']} agree, {r['other_branch_of_an_option']} the other branch of an option, {r['to_adjudicate']} to adjudicate, {r['adjudicated']} adjudicated; {len(c['replay']['roots_of_the_written_line_not_declared_by_the_tables'])} roots undeclared"
        if mod == "pg_written_replay":
            r = c["r4_pg19_register"]; pl = c["r6_written_registers"]["placement"]
            return f"R4 {r['replayed']} of {r['positions']} replayed, {r['agree']} agree; R6's placement {pl['row_of_a_table']} rows / {pl['ledger_hand_meta_compiled']} ledger / {pl['neither']} neither"
        if mod.startswith("pg_modal_registers"):
            r = c["totals"]
            return f"{r['replayed']} of {r['positions']} replayed, {r['agree']} agree, {r['other_branch_of_an_option']} the other branch of an option, {r['to_adjudicate']} to adjudicate" + (f", {r['adjudicated']} adjudicated" if r.get("adjudicated") else "") + f"; {r.get('root_not_declared', 0)} positions on undeclared roots"
    except Exception:  # noqa: BLE001
        return ""
    return ""


def run(mod: str) -> tuple[str, dict]:
    out = Path("/tmp") / f"{mod}_cascade.json"
    p = subprocess.run(PY + ["-m", f"proof_lab.{mod}", "--output", str(out)], cwd=R, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout[-2000:], p.stderr[-2000:]); raise SystemExit(f"{mod} failed")
    m = re.search(r"sha256 ([0-9a-f]{64})", p.stdout)
    if not m:
        raise SystemExit(f"{mod}: no digest in output")
    return m.group(1), json.loads(out.read_text(encoding="utf-8"))


def repin(mod: str, pin: str, capsule: str, by: int, dry: bool, extra: str = "") -> bool:
    pinf = R / "proof_lab" / pin
    cur = pinf.read_text(encoding="utf-8").strip()
    head = subprocess.run(["git", "show", f"HEAD:proof_lab/{pin}"], cwd=R, capture_output=True, text=True)
    old = head.stdout.strip() if head.returncode == 0 and head.stdout.strip() else cur   # the committed pin is the one the note names; the file may already hold this session's re-pin
    sha, cert = run(mod)
    if sha == old:
        print(f"{mod:26s} unchanged {old[:8]}…"); return False
    if sha == cur:
        print(f"{mod:26s} already re-pinned this session {old[:8]}… → {sha[:8]}… (pin file written, note present)"); return False
    commit = subprocess.run(["git", "log", "-1", "--format=%h", "--", str(pinf)], cwd=R, capture_output=True, text=True).stdout.strip()
    nums = headline(mod, cert)
    note = f"\n\n*Note (theorum/{by}).* Re-pinned again by theorum/{by} (`{sha[:8]}…`){': ' + nums if nums else ''}{'; ' + extra if extra else ''}. The pin `{old[:8]}…` holds at commit {commit}.\n"
    print(f"{mod:26s} re-pinned {old[:8]}… → {sha[:8]}…  {nums}")
    if dry:
        return True
    pinf.write_text(sha + "\n", encoding="utf-8")
    idx = R / "CERTIFICATE_INDEX.md"; t = idx.read_text(encoding="utf-8")
    prev = cur if (cur != old and cur in t) else old   # a re-run within the session: the index holds the session's earlier re-pin
    if prev not in t:
        print(f"   ! {prev[:8]} not in CERTIFICATE_INDEX.md")
    t = t.replace(prev, sha); idx.write_text(t, encoding="utf-8")
    cap = R / capsule; body = cap.read_text(encoding="utf-8")
    m = re.search(r"\n\n\*Note \(theorum/%d\)\.\*[^\n]*\n?$" % by, body)
    body = body[:m.start()] + "\n" if m else body   # the session's earlier note for the same theorem is replaced, not stacked
    cap.write_text(body.rstrip("\n") + note, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--by", type=int, required=True); ap.add_argument("--only", default=""); ap.add_argument("--dry", action="store_true")
    ap.add_argument("--extra", default="", help="a clause appended to every note (what changed)"); ap.add_argument("--skip-kernel", action="store_true")
    a = ap.parse_args()
    only = set(a.only.split(",")) if a.only else None
    changed = []
    for mod, pin, capsule in CASCADE:
        if only and mod not in only:
            continue
        if repin(mod, pin, capsule, a.by, a.dry, a.extra):
            changed.append(mod)
    if not a.skip_kernel:
        p = subprocess.run(PY + ["-m", "proof_lab.astadhyayi_ledger"], cwd=R, capture_output=True, text=True)
        m = re.search(r'"iast_mismatch_with_pinned_edition": (\d+)', p.stdout); print("ledger", p.stdout.strip().splitlines()[-1][:160] if p.stdout.strip() else p.stderr[-300:])
        if not m or m.group(1) != "0":
            raise SystemExit("ledger: IAST mismatch or failure")
        mod, pin, capsule = KERNEL
        pinf = R / "proof_lab" / pin; cur = pinf.read_text(encoding="utf-8").strip(); sha, cert = run(mod)
        head = subprocess.run(["git", "show", f"HEAD:proof_lab/{pin}"], cwd=R, capture_output=True, text=True); old = head.stdout.strip() or cur
        if sha == old:
            print(f"{mod:26s} unchanged {old[:8]}…")
        elif sha == cur:
            idx_t = (R / "CERTIFICATE_INDEX.md").read_text(encoding="utf-8"); cap_t = (R / capsule).read_text(encoding="utf-8")
            print(f"{mod:26s} already re-pinned this session {old[:8]}… → {sha[:8]}…" + ("" if sha in idx_t and sha[:8] in cap_t else "   ! the index or the capsule does not carry it"))
        else:
            print(f"{mod:26s} re-pinned {old[:8]}… → {sha[:8]}…")
            if not a.dry:
                pinf.write_text(sha + "\n", encoding="utf-8")
                idx = R / "CERTIFICATE_INDEX.md"; t = idx.read_text(encoding="utf-8")
                prev = cur if (cur != old and cur in t) else old
                assert t.count(prev) == 1, "kernel pin in index"; idx.write_text(t.replace(prev, sha), encoding="utf-8")
                cap = R / capsule; t = cap.read_text(encoding="utf-8")
                anchor = "; commit 8824482 holds the first pin."
                assert t.count(anchor) == 1, "kernel capsule anchor"
                t = re.sub(r", theorum/%d \(`[0-9a-f]{8}…`[^)]*\)(?=; commit 8824482)" % a.by, "", t)   # the session's earlier entry for this theorem is replaced
                t = t.replace(anchor, f", theorum/{a.by} (`{sha[:8]}…`{': ' + a.extra if a.extra else ''}){anchor}"); cap.write_text(t, encoding="utf-8")
            changed.append(mod)
    print("changed:", ", ".join(changed) if changed else "nothing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
