from __future__ import annotations

"""Exact certificate (theorum/84): THE VEDĀṄGA PACKETS 71–73 BOUND TO THEIR
QUOTED SOURCES — Piṅgala, Baudhāyana, Lagadha quoted; every number those
pinned certificates use is shown to be the text's number.  The pins of
theorum/71, 72, 73 are not touched: this packet imports their functions and
compares.

Quoted sources:

 Piṅgala, Chandaḥśāstra 8 (standard printed numbering)
   8.20 dvikau glau   8.21 miśrau ca   8.22 pṛthag lā miśrāḥ   8.23 vasavas trikāḥ
   8.24 l-ardhe   8.25 saike g   8.26 pratilomagaṇaṁ dvir l-ādyam   8.27 tato gy ekaṁ jahyāt
   8.28 dvir ardhe   8.29 rūpe śūnyam   8.30 dviḥ śūnye   8.31 tāvad ardhe tad guṇitam
   8.32 dvir dvy ūnaṁ tad antānām   8.34 pare pūrṇam   8.35 pare pūrṇam iti

 Baudhāyana Śulbasūtra (Thibaut numbering / Sen–Bag numbering)
   i.48 / 1.12  dīrghacaturasrasyākṣṇayā rajjuḥ pārśvamānī tiryaṅmānī ca yat pṛthagbhūte
                kurutas tad ubhayaṁ karoti
   i.61–62 / 2.12  samasya dvikaraṇī / pramāṇaṁ tṛtīyena vardhayet tac caturthenātma-
                catustriṁśonena saviśeṣaḥ

 Ṛgveda Vedāṅga Jyotiṣa (Lagadha; GRETIL text)
   1   pañcasaṁvatsaramayaṁ yugādhyakṣaṁ prajāpatim
   4   nirekaṁ dvādaśārdhābdaṁ dviguṇaṁ gatasaṁjñikam /
       ṣaṣṭyā ṣaṣṭyā yutaṁ dvābhyāṁ parvaṇāṁ rāśir ucyate
   22  yad uttarasyāyanato gataṁ syāc cheṣaṁ tu yad dakṣiṇato 'yanasya /
       tad ekaṣaṣṭyā dviguṇaṁ vibhaktaṁ sadvādaśaṁ syād divasapramāṇam
   32  yugasya pañcavarṣasya kālajñānaṁ pracakṣate

 T1  CHANDAS.  The four pratyaya procedures written from the quoted sūtras
     (prastāra by 8.20–8.23, naṣṭa by 8.24–8.25, uddiṣṭa by 8.26–8.27,
     saṅkhyā by 8.28–8.31, meru by 8.34–8.35) equal theorum/71's pinned
     functions on every input n ≤ 10 (meru n ≤ 12); the literal adhvayoga
     8.32 (2·2^n − 2) is theorum/71's value minus one for every n — a
     discrepancy recorded against the pinned packet, not silently fixed.
 T2  ŚULBA.  The √2 cord read from i.61–62 — the measure increased by its
     third, that by its fourth, less the thirty-fourth part of that — is
     1 + 1/3 + 1/12 − 1/408 = 577/408 = theorum/72's sqrt2_cord(); the
     diagonal rule i.48 is theorum/72's diagonal_bindu = 0 on its triples.
 T3  JYOTIṢA.  RVJ 1 / 32: five years; RVJ 4's "sixty and sixty, with two
     and two" = 124 parvans = 2 × 62 synodic months = theorum/73's
     SYN_MONTHS, with 62 − 60 = 2 adhimāsas; RVJ 22's day-length rule —
     days elapsed from the northern solstice, doubled, divided by sixty-one,
     plus twelve — equals theorum/73's daylight(d) in muhūrtas for every day
     of the half-year and gives 18 at d = 183 and 12 at d = 0.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab import pingala_chandas_pratyaya as T71
from proof_lab import sulba_measure_residue as T72
from proof_lab import vedanga_jyotisa_yuga_ledger as T73

SOURCES = {
    "Chandaḥśāstra 8.20": "dvikau glau", "8.21": "miśrau ca", "8.22": "pṛthag lā miśrāḥ", "8.23": "vasavas trikāḥ",
    "8.24": "l-ardhe", "8.25": "saike g", "8.26": "pratilomagaṇaṁ dvir l-ādyam", "8.27": "tato gy ekaṁ jahyāt",
    "8.28": "dvir ardhe", "8.29": "rūpe śūnyam", "8.30": "dviḥ śūnye", "8.31": "tāvad ardhe tad guṇitam",
    "8.32": "dvir dvy ūnaṁ tad antānām", "8.34": "pare pūrṇam", "8.35": "pare pūrṇam iti",
    "BŚS i.48 / 1.12": "dīrghacaturasrasyākṣṇayā rajjuḥ pārśvamānī tiryaṅmānī ca yat pṛthagbhūte kurutas tad ubhayaṁ karoti",
    "BŚS i.61–62 / 2.12": "samasya dvikaraṇī / pramāṇaṁ tṛtīyena vardhayet tac caturthenātmacatustriṁśonena saviśeṣaḥ",
    "RVJ 1": "pañcasaṁvatsaramayaṁ yugādhyakṣaṁ prajāpatim",
    "RVJ 4": "nirekaṁ dvādaśārdhābdaṁ dviguṇaṁ gatasaṁjñikam / ṣaṣṭyā ṣaṣṭyā yutaṁ dvābhyāṁ parvaṇāṁ rāśir ucyate",
    "RVJ 22": "yad uttarasyāyanato gataṁ syāc cheṣaṁ tu yad dakṣiṇato 'yanasya / tad ekaṣaṣṭyā dviguṇaṁ vibhaktaṁ sadvādaśaṁ syād divasapramāṇam",
    "RVJ 32": "yugasya pañcavarṣasya kālajñānaṁ pracakṣate",
}


# ---------------------------------------------------------------- T1 chandas: the procedures written from the sūtras
def prastara_q(n: int) -> list[str]:
    if n == 0:
        return [""]
    if n == 1:
        return ["g", "l"]                                              # 8.20
    prev = prastara_q(n - 1)                                           # 8.21
    return [p + "g" for p in prev] + [p + "l" for p in prev]           # 8.22: the g column over the mixed rows, l separately below


def nashta_q(n: int, k: int) -> str:
    out, x = [], k
    for _ in range(n):
        if x % 2 == 0:
            out.append("l"); x //= 2                                   # 8.24 l-ardhe
        else:
            out.append("g"); x = (x + 1) // 2                          # 8.25 saike g
    return "".join(out)


def uddishta_q(p: str) -> int:
    x = 1
    for s in reversed(p):                                              # 8.26 pratilomagaṇam
        x *= 2                                                         # dviḥ
        if s == "g":
            x -= 1                                                     # 8.27 tato gy ekaṁ jahyāt
    return x


def sankhya_q(n: int) -> int:
    marks, x = [], n
    while x > 0:
        if x % 2 == 0:
            marks.append(2); x //= 2                                   # 8.28 dvir ardhe
        else:
            marks.append(0); x -= 1                                    # 8.29 rūpe śūnyam
    v = 1
    for m in reversed(marks):
        v = v * 2 if m == 0 else v * v                                 # 8.30 dviḥ śūnye ; 8.31 tāvad ardhe tad guṇitam
    return v


def adhvayoga_q(n: int) -> int:
    return 2 * sankhya_q(n) - 2                                        # 8.32 dvir dvy ūnam


def meru_q(n: int) -> list[int]:
    row = [1]
    for _ in range(n):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]   # 8.34–8.35 pare pūrṇam
    return row


def _t71_meru_row(n: int) -> list[int]:
    M = T71.meru(n)
    row = M[n] if isinstance(M[0], list) else M
    return [int(x) for x in row if x]


def t1_chandas() -> dict[str, Any]:
    up = str.maketrans({"g": "G", "l": "L"})                       # theorum/71 writes G / L
    ok_pr = all([p.translate(up) for p in prastara_q(n)] == T71.prastara(n) for n in range(1, 11))
    ok_na = all(nashta_q(n, k).translate(up) == T71.nashta(n, k) for n in range(1, 11) for k in range(1, 2 ** n + 1))
    ok_ud = all(uddishta_q(p) == T71.uddishta(p.translate(up)) for n in range(1, 11) for p in prastara_q(n))
    ok_sa = all(sankhya_q(n) == T71.sankhya(n) for n in range(0, 11))
    ok_ad = all(adhvayoga_q(n) == T71.adhvayoga(n) - 1 for n in range(1, 11))   # theorum/71 pinned 2·S − 1; the sūtra says "dvy ūnam", less two
    meru_rows = {}
    ok_me = True
    for n in range(0, 13):
        r71 = _t71_meru_row(n)
        meru_rows[n] = r71
        ok_me &= meru_q(n) == r71
    checks = {
        "prastara_8_20_23_equals_theorum_71_n_le_10": ok_pr,
        "nashta_8_24_25_equals_theorum_71_every_row_n_le_10": ok_na,
        "uddishta_8_26_27_equals_theorum_71_every_row_n_le_10": ok_ud,
        "sankhya_8_28_31_equals_theorum_71_n_le_10": ok_sa,
        "adhvayoga_8_32_literal_2S_minus_2_equals_theorum_71_value_minus_one_for_every_n_le_10_DISCREPANCY_RECORDED": ok_ad,
        "meru_8_34_35_equals_theorum_71_rows_n_le_12": ok_me,
        "vasavas_trikah_8_23": len(prastara_q(3)) == 8,
    }
    return {"checks": checks, "prastara_3": prastara_q(3), "meru_row_6": meru_rows[6]}


# ---------------------------------------------------------------- T2 śulba: the cord read from the sūtra
def sqrt2_cord_q() -> Fraction:
    pramana = Fraction(1)
    v = pramana + pramana / 3                        # pramāṇaṁ tṛtīyena vardhayet: increase the measure by its third
    fourth = (pramana / 3) / 4                       # tac caturthena: that (the third) by its fourth
    v += fourth
    v -= fourth / 34                                 # ātmacatustriṁśonena: less the thirty-fourth part of that
    return v


def t2_sulba() -> dict[str, Any]:
    q = sqrt2_cord_q()
    ok_triples = all(T72.diagonal_bindu(a, b, d) == 0 for a, b, d in T72.TRIPLES)
    checks = {
        "sqrt2_cord_read_from_i_61_62_equals_theorum_72_sqrt2_cord": q == T72.sqrt2_cord() == Fraction(577, 408),
        "diagonal_rule_i_48_bindu_zero_on_theorum_72_triples": ok_triples,
        "cord_is_1_plus_1_3_plus_1_12_minus_1_408": q == 1 + Fraction(1, 3) + Fraction(1, 12) - Fraction(1, 408),
    }
    return {"checks": checks, "cord": str(q), "triples": T72.TRIPLES}


# ---------------------------------------------------------------- T3 jyotiṣa: the numbers read from the verses
def daylength_rvj22(d: int) -> Fraction:
    """days elapsed from the northern solstice (or remaining to the southern), doubled, divided by sixty-one, plus twelve."""
    return Fraction(2 * d, 61) + 12


def t3_jyotisa() -> dict[str, Any]:
    parvans = 60 + 60 + 2 + 2                                          # RVJ 4: ṣaṣṭyā ṣaṣṭyā yutaṁ dvābhyām
    half_year = T73.YUGA_DAYS // T73.YEARS // 2                        # 183
    ok_day = all(daylength_rvj22(d) == T73.daylight(d) for d in range(0, half_year + 1))
    checks = {
        "rvj_1_32_five_years_equals_theorum_73_YEARS": T73.YEARS == 5,
        "rvj_4_parvans_124_equals_2_times_theorum_73_SYN_MONTHS": parvans == 124 == 2 * T73.SYN_MONTHS,
        "two_adhimasas_are_62_minus_60": T73.SYN_MONTHS - T73.SOLAR_MONTHS == 2,
        "rvj_22_daylength_equals_theorum_73_daylight_on_every_day_of_the_half_year": ok_day,
        "rvj_22_gives_12_at_solstice_start_and_18_at_183_days": daylength_rvj22(0) == 12 and daylength_rvj22(183) == 18,
    }
    return {"checks": checks, "parvans": parvans, "half_year_days": half_year, "sample": {d: str(daylength_rvj22(d)) for d in (0, 61, 122, 183)}}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_chandas": t1_chandas(), "t2_sulba": t2_sulba(), "t3_jyotisa": t3_jyotisa()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_VEDANGA_SOURCES_QUOTED_CANDIDATE" if all(checks.values()) else "FAIL_VEDANGA_SOURCES_QUOTED_CANDIDATE"
    return {
        "schema": "rkf.vedanga_sources_quoted_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "pins_untouched": {"theorum/71": "PINGALA_CHANDAS_PRATYAYA_EXPECTED.sha256", "theorum/72": "SULBA_MEASURE_RESIDUE_EXPECTED.sha256", "theorum/73": "VEDANGA_JYOTISA_YUGA_LEDGER_EXPECTED.sha256"},
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "theorum/71's prastāra, naṣṭa, uddiṣṭa, saṅkhyā and meru equal the procedures written from the quoted Chandaḥśāstra 8.20–8.35 (n ≤ 10; meru n ≤ 12)",
                "theorum/71's pinned adhvayoga is 2·2^n − 1; the literal 8.32 'dvir dvy ūnam' gives 2·2^n − 2 (the sum over lengths 1..n); the two differ by exactly 1 for every n — recorded, theorum/71's pin left as is",
                "theorum/72's √2 cord is the number read from BŚS i.61–62 (577/408); its diagonal rule is i.48 on the text's triples",
                "theorum/73's 5 years, 62 synodic months (124 parvans, RVJ 4) and daylight rule (RVJ 22, 2d/61 + 12) are the verses' numbers",
            ],
            "NOT_claimed": [
                "1830 days, 67 nakṣatra months, 1835 sidereal days and 1860 tithis are the Yajus recension's integers; their verses are not quoted here (text not verified in this session) — theorum/73 keeps them as declared inputs",
                "the reading of RVJ 4 as the parvan total of the yuga follows Kuppanna Sastry; the verse's role as an elapsed-parvan formula is not modelled",
                "Śulba numbering is given in both Thibaut and Sen–Bag systems; theorum/72's citations mix them (1.48 Thibaut, 2.12 Sen–Bag) and are left as pinned",
                "RH, YM untouched",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n").encode("utf-8")


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
