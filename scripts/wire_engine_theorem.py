"""Wire a new theorem packet into the ledger, CERTIFICATE_INDEX, both indices, README, the index test range and CI.

    python scripts/wire_engine_theorem.py <spec.json>

The spec: N (int), theorem_file, module, sha, old_sha ("" for a new module), status, title, boundary, family, family_desc,
hand (sūtra ids hand-coded by the packet), meta (saṁjñā / paribhāṣā sūtras it reads), texts (id → IAST as the pinned edition writes it),
index_para, readme (a bold **N — title.** item). After it: python -m proof_lab.astadhyayi_ledger (IAST mismatch must be 0), the kernel re-pin,
and for a NEW module the CI scope / unittest list / --output line / pin tuple are added by hand."""
import re, sys, json
from pathlib import Path
R = Path(__file__).resolve().parent.parent   # the repository root
a = json.loads(Path(sys.argv[1]).read_text())
N = a["N"]; P = N - 1; th = a["theorem_file"]; mod = a["module"]; sha = a["sha"]; old = a["old_sha"]
p = R / "proof_lab/astadhyayi_ledger.py"; t = p.read_text()
if a.get("hand"):
    t = t.replace("HAND_CODED = {  # exact finite functions in certified packets: the numbers each packet's source actually carries\n",
                  "HAND_CODED = {  # exact finite functions in certified packets: the numbers each packet's source actually carries\n    \"%d\": %s,\n" % (N, json.dumps(a["hand"], ensure_ascii=False)), 1)
blk = t[t.index("HAND_CODED = {"): t.index("\n}\n", t.index("HAND_CODED = {"))]
allhand = set(re.findall(r'"(\d+\.\d+\.\d+)"', blk))
meta = [m for m in a.get("meta", []) if m not in allhand]
if meta:
    t = t.replace("META = {  # interpreter / saṁjñā / paribhāṣā sūtras implemented by a certificate\n",
                  "META = {  # interpreter / saṁjñā / paribhāṣā sūtras implemented by a certificate\n    \"%d\": %s,\n" % (N, json.dumps(meta, ensure_ascii=False)), 1)
t2, n = re.subn(r'(    "%d": "theorum/%d_[^"]+",\n)\}' % (P, P), r'\1' + '    "%d": "%s",\n}' % (N, th), t, count=1); assert n == 1; t = t2
old_pk = '"%d": "%s"}' % (P, mod)
if t.count(old_pk) == 1:
    t = t.replace(old_pk, '"%d": "%s", "%d": "%s"}' % (P, mod, N, mod))
else:
    i = t.index("PACKET_OF = {"); j = t.index("}", i); t = t[:j] + ', "%d": "%s"' % (N, mod) + t[j:]
if a.get("texts"):
    t = t.replace("TEXT = {\n", "TEXT = {\n    " + ", ".join('"%s": "%s"' % (k, v) for k, v in a["texts"].items()) + ",\n", 1)
p.write_text(t)
p = R / "CERTIFICATE_INDEX.md"; t = p.read_text()
if old:
    assert t.count("`%s`" % old) >= 1; t = t.replace("`%s`" % old, "`%s`" % sha)
sec = "## Theorem %d %s packet\n\n| Field | Value |\n|---|---|\n| Certificate class | %s |\n| Status | `%s` |\n| Canonical result SHA-256 | `%s` |\n| Boundary | %s |\n\n```text\n%s\nproof_lab/%s.py\nproof_lab/test_%s.py\nproof_lab/%s_EXPECTED.sha256\n```\n\n## Consolidated parallel-lineage index" % (N, a["title"], a["title"], a["status"], sha, a["boundary"], th, mod, mod, mod.upper())
assert t.count("## Consolidated parallel-lineage index") == 1; t = t.replace("## Consolidated parallel-lineage index", sec); p.write_text(t)
p = R / "MATHEMATICS_INDEX_2026_09_16.md"; t = p.read_text()
fam_prev = [l for l in t.split("\n") if ("[T%d](" % P) in l and l.startswith("| ")][0]
t = t.replace(fam_prev, fam_prev + "\n| %s | [T%d](%s) | %s |" % (a["family"], N, th, a["family_desc"]), 1)
reg_prev = [l for l in t.split("\n") if l.startswith("| %d | [" % P)][0]
t = t.replace(reg_prev, reg_prev + "\n| %d | [%s](%s) | %s |" % (N, a["title"], th, a["boundary"]), 1); p.write_text(t)
p = R / "MATHEMATICS_INDEX.md"; t = p.read_text()
t = t.replace("SP1 and Theorems 78–%d (" % P, "SP1 and Theorems 78–%d (" % N).replace("the Vedāṅgas: Theorems 78–%d" % P, "the Vedāṅgas: Theorems 78–%d" % N)
k = "\n## Observer innovations SE49"; assert t.count(k) == 1; t = t.replace(k, "\n" + a["index_para"] + "\n" + k, 1); p.write_text(t)
p = R / "theorum/README.md"; t = p.read_text()
old_item = [l for l in t.split("\n") if re.match(r"\d+\. \*\*%d " % P, l)][0]
num = int(old_item.split(".")[0]) + 1
t = t.replace(old_item, old_item + "\n%d. %s" % (num, a["readme"]), 1).replace("NUMBERED THEOREM FILES 01-%d" % P, "NUMBERED THEOREM FILES 01-%d" % N); p.write_text(t)
p = R / "proof_lab/test_mathematics_index.py"; t = p.read_text()
t = t.replace("test_numbered_capsules_01_through_%d_are" % P, "test_numbered_capsules_01_through_%d_are" % N).replace("list(range(1, %d))" % (P + 1), "list(range(1, %d))" % (N + 1)); p.write_text(t)
p = R / ".github/workflows/repository-checks.yml"; t = p.read_text()
prev_line = [l for l in t.split("\n") if ("'theorum/%d_" % P) in l][0]
t = t.replace(prev_line + "\n", prev_line + "\n" + prev_line.replace(prev_line.strip(), "'%s'," % th) + "\n", 1).replace("Check Theorem 78-%d quoted" % P, "Check Theorem 78-%d quoted" % N); p.write_text(t)
print("wired", N)
