from __future__ import annotations

"""Exact certificate (theorum/87): THE TRIPĀDĪ NIṢṬHĀ RULES COMPILED IN ASIDDHA
ORDER — the four refusals of theorum/86 (pakta, labdha, tunna, lūna) realized,
with 8.2.1 shown load-bearing on labdha.

Quoted sūtras:
 8.2.1   pūrvatrāsiddham                    (adhikāra) what follows is as if not done with respect to what precedes
 8.2.30  coḥ kuḥ                            a ca-varga sound becomes the ka-varga sound (at pada end / before jhal)
 8.2.40  jhaṣas tathor dho 'dhaḥ            after a jhaṣ (gh jh ḍh dh bh), t / th of an affix become dh (not after dh-)
 8.2.42  radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ   after r / d the t of niṣṭhā becomes n, and a preceding d too
 8.2.44  lvādibhyaḥ                         after lū and the lvādi roots (the niṣṭhā t becomes n)
 8.4.53  jhalāṁ jaś jhaśi                   a jhal becomes jaś before a jhaś
 1.1.26  ktaktavatū niṣṭhā                  kta and ktavatu are niṣṭhā
 (theorum/82: 1.3.2–1.3.9; theorum/85: 1.2.46, 3.2.102, 7.2.10)

Pinned Dhātupāṭha entries (PG5): 1011151 डुपचँष्, 1011130 डुलभँष्, 1060001 तुदँ, 1090016 लूञ्

 T1  THE FOUR NOUNS.  pac + ta → pakta (8.2.30); labh + ta → labdha (8.2.40
     then 8.4.53); tud + ta → tunna (8.2.42, both parts); lū + ta → lūna
     (8.2.44).  The rules are applied as 8.2.1 says: in sūtra order, each
     seeing only the output of the earlier ones.
 T2  8.2.1 IS LOAD-BEARING.  Applying 8.4.53 before 8.2.40 on labh + ta
     leaves *labhdha* (8.4.53 finds no jhaś to act before, and is then asiddha
     for the dh that 8.2.40 creates only in the lawful order).  The other three
     derivations are order-independent on their inputs.
 T3  88 SUP FORMS.  theorum/63's pinned ladder derives all 22 forms of each.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.nirukta_dhatupatha_nama import load_entries, upadesa_iast
from proof_lab.nirukta_nama_akhyatajani import code
from proof_lab.paninian_it_samjna_compiled import its
from proof_lab.shaiva_sources_varga_crystal import VARGAS
from proof_lab.sup_vibhakti_resolver_ladder import ORACLE as ORACLE63, RULES as RULES63, SUP, derive as derive63, paradigm_domains, st as st63, surface as surface63

SOURCES = {
    "8.2.1": "pūrvatrāsiddham", "8.2.30": "coḥ kuḥ", "8.2.40": "jhaṣas tathor dho 'dhaḥ", "8.2.42": "radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ",
    "8.2.44": "lvādibhyaḥ", "8.4.53": "jhalāṁ jaś jhaśi", "1.1.26": "ktaktavatū niṣṭhā",
}

CU, KU = VARGAS["ca"], VARGAS["ka"]
JHAS = tuple(v[3] for v in VARGAS.values())            # gh jh ḍh dh bh
JAS = tuple(v[2] for v in VARGAS.values())             # g j ḍ d b
JHAS_SET = set(JHAS) | set(JAS)                        # jhaś = jaś + jhaṣ (voiced stops)
JHAL = {s for v in VARGAS.values() for s in v if s not in (v[4],)} | {"ś", "ṣ", "s", "h"}   # all non-nasal stops + sibilants + h
JAS_OF = {v[0]: v[2] for v in VARGAS.values()} | {v[1]: v[2] for v in VARGAS.values()} | {v[3]: v[2] for v in VARGAS.values()} | {v[2]: v[2] for v in VARGAS.values()}
JAS_OF.update({"ś": "j", "ṣ": "ḍ", "s": "d", "h": "g"})
LVADI = ("lū",)                                        # 8.2.44's gaṇa: lū and the lvādi roots (only lū admitted here)

Form = tuple[str, ...]   # sounds; the niṣṭhā boundary is the index where the affix starts


def r_8_2_30(x: Form, b: int) -> Form:   # coḥ kuḥ: root-final ca-varga before the jhal-initial affix
    if x[b - 1] in CU and x[b] in JHAL:
        return x[: b - 1] + (KU[CU.index(x[b - 1])],) + x[b:]
    return x


def r_8_2_40(x: Form, b: int) -> Form:   # jhaṣas tathor dho 'dhaḥ
    if x[b - 1] in JHAS and x[b - 1] != "dh" and x[b] in ("t", "th"):
        return x[:b] + ("dh",) + x[b + 1 :]
    return x


def r_8_2_42(x: Form, b: int) -> Form:   # radābhyāṁ niṣṭhāto naḥ pūrvasya ca daḥ
    if x[b - 1] in ("r", "d") and x[b] == "t":
        pre = x[: b - 1] + (("n",) if x[b - 1] == "d" else ("r",))
        return pre + ("n",) + x[b + 1 :]
    return x


def r_8_2_44(x: Form, b: int, root: str) -> Form:   # lvādibhyaḥ
    if root in LVADI and x[b] == "t":
        return x[:b] + ("n",) + x[b + 1 :]
    return x


def r_8_4_53(x: Form, b: int) -> Form:   # jhalāṁ jaś jhaśi: a jhal before a jhaś becomes jaś
    out = list(x)
    for i in range(len(out) - 1):
        if out[i] in JHAL and out[i + 1] in JHAS_SET:
            out[i] = JAS_OF[out[i]]
    return tuple(out)


TRIPADI = [("8.2.30", r_8_2_30), ("8.2.40", r_8_2_40), ("8.2.42", r_8_2_42), ("8.2.44", r_8_2_44), ("8.4.53", r_8_4_53)]


def apply_tripadi(x: Form, b: int, root: str, order: list) -> tuple[Form, list[str]]:
    """8.2.1: apply in the given order, each rule seeing only the output of the earlier ones (one pass)."""
    fired = []
    for sid, fn in order:
        y = fn(x, b, root) if sid == "8.2.44" else fn(x, b)
        if y != x:
            fired.append(sid)
            x = y
    return x, fired


ENTRIES = {"1011151": ("pac", "pakta"), "1011130": ("labh", "labdha"), "1060001": ("tud", "tunna"), "1090016": ("lū", "lūna")}


def nishtha(lex: str, entries: dict, order=TRIPADI) -> dict[str, Any]:
    up = upadesa_iast(entries[lex]["aupadeshik"])
    dh = tuple(its(up, "dhatu")["remaining_sounds"])
    aff = tuple(its("kta", "pratyaya")["remaining_sounds"])      # ta, kit
    x0 = dh + aff
    b = len(dh)
    x, fired = apply_tripadi(x0, b, "".join(dh), order)
    return {"upadesa": up, "dhatu": "".join(dh), "input": "".join(x0), "output": "".join(x), "sounds": x, "fired": fired}


def t1_four_nouns() -> dict[str, Any]:
    entries = load_entries()
    out = {lex: nishtha(lex, entries) for lex in ENTRIES}
    checks = {
        "pakta_labdha_tunna_luna": all(out[l]["output"] == exp for l, (_, exp) in ENTRIES.items()),
        "dhatus_from_the_pinned_teaching_forms": all(out[l]["dhatu"] == r for l, (r, _) in ENTRIES.items()),
        "rules_fired_as_expected": out["1011151"]["fired"] == ["8.2.30"] and out["1011130"]["fired"] == ["8.2.40", "8.4.53"] and out["1060001"]["fired"] == ["8.2.42"] and out["1090016"]["fired"] == ["8.2.44"],
    }
    return {"checks": checks, **out}


def t2_asiddha_order_load_bearing() -> dict[str, Any]:
    entries = load_entries()
    reversed_order = list(reversed(TRIPADI))
    lawful = {l: nishtha(l, entries)["output"] for l in ENTRIES}
    reverse = {l: nishtha(l, entries, reversed_order)["output"] for l in ENTRIES}
    checks = {
        "reverse_order_breaks_labdha_only": reverse["1011130"] == "labhdha" and all(reverse[l] == lawful[l] for l in ENTRIES if l != "1011130"),
        "lawful_order_is_the_sutra_order_8_2_1": [s for s, _ in TRIPADI] == sorted((s for s, _ in TRIPADI), key=lambda s: tuple(int(p) for p in s.split("."))),
    }
    return {"checks": checks, "lawful": lawful, "reverse_order": reverse}


def t3_sup_forms() -> dict[str, Any]:
    entries = load_entries()
    dom = paradigm_domains(RULES63)
    out, ok, n = {}, True, 0
    for lex in ENTRIES:
        stem = code(nishtha(lex, entries)["sounds"])
        stem_s = "".join(stem)
        forms = {}
        for c, aff, feats in SUP:
            aff = tuple(aff)
            fe = set(feats) | {"sup"}
            if c == "7p":
                aff = ("s", "u")
            W, _ = derive63(st63(stem, aff, fe), RULES63, dom=dom)
            got = surface63(W)
            exp = (stem_s[:-1] + ORACLE63[c][3:]).replace("N", "n")
            forms[c] = got
            ok &= got == exp
            n += 1
        out[lex] = forms
    checks = {"theorum_63_ladder_derives_all_88_sup_forms": ok and n == 88}
    return {"checks": checks, "forms": out}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_four_nouns": t1_four_nouns(), "t2_asiddha_order_load_bearing": t2_asiddha_order_load_bearing(), "t3_sup_forms": t3_sup_forms()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_TRIPADI_NISHTHA_COMPILED_CANDIDATE" if all(checks.values()) else "FAIL_TRIPADI_NISHTHA_COMPILED_CANDIDATE"
    return {
        "schema": "rkf.tripadi_nishtha_compiled_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "pac/labh/tud/lū + kta → pakta, labdha, tunna, lūna by 8.2.30, 8.2.40 + 8.4.53, 8.2.42, 8.2.44 applied in sūtra order (8.2.1), from the pinned teaching forms",
                "8.2.1 is load-bearing: the reverse order leaves labhdha and changes nothing else on these inputs",
                "theorum/63's pinned ladder derives all 88 sup forms of the four nouns",
            ],
            "NOT_claimed": [
                "8.2.1 in general (only this five-rule, four-input instance); 6.4.22 and the rest of the Tripādī",
                "the lvādi gaṇa beyond lū; 8.2.30's pada-end condition (only the pre-affix case is used)",
                "aniṭ status declared (7.2.10); the padas' ṇatva/ṣatva beyond theorum/63's ladder",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    payload = build_certificate()
    data = canonical_bytes(payload)
    if args.output is not None:
        args.output.write_bytes(data)
    print(payload["status"])
    for name, v in payload.items():
        if isinstance(v, dict) and "checks" in v:
            for k, val in v["checks"].items():
                print(f"    {name}.{k}: {val}")
    print("sha256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
