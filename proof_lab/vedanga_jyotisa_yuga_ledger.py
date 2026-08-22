from __future__ import annotations

"""Exact certificate (theorum/73): JYOTIṢA — Lagadha's Vedāṅga Jyotiṣa yuga as an
exact cyclic ledger; the owner's note (Vedic repo, "Jyotisha Siddhanta Cyclic
Recognition Engine": Kāla = cycles with Phase and Wind; calendar = phase
ordering + cycle count + intercalation Smṛti; prediction gap K = Res − S = 0)
made executable on the text's own integers.  All rational; no float.

Vedāṅga Jyotiṣa (R̥k-recension) yuga constants:
  5 solar years (of 366 days each) = 1830 sāvana (civil) days
  62 synodic (cāndra) months = 1860 tithis;  67 nakṣatra (sidereal) months
  1835 sidereal days;  124 parvans;  2 adhimāsas (62 − 60)

Facts certified:
 T1  INTERCALATION SMṚTI CLOSES THE YUGA EXACTLY: the solar–lunar residue of
     one year, 12·(1830/62) − 366 = −366/31 day, accumulated over 5 years is
     −1830/31 day = exactly −2 synodic months.  So S_intercalation = 2
     adhimāsa makes K_yuga = 0 with no remainder: 60 solar months + 2 =
     62 cāndra months.  (The owner's K = Res − S = 0, on the text's numbers.)
 T2  Tithi ledger: 1860 tithis − 1830 days = 30 = the omitted (kṣaya) tithis;
     tithi = 61/62 day.  Sidereal − civil days = 1835 − 1830 = 5 = the number
     of years: one extra rotation per solar year, exact.
 T3  Owner's Wind/Phase: for every cycle c with period T_c (day, tithi,
     synodic month, sidereal month, year), Phase_c(1830) = 0 and Wind_c(1830)
     is an integer -- all cycles re-align at the yuga end; at no earlier
     t < 1830 do ALL of them re-align (1830 is the least common closure).
 T4  Daylight zigzag (VJ 1.22, 7/8 with the water clock): day length runs
     from 12 to 18 muhūrtas and back over 183 + 183 days, linearly; the
     solstice ratio is 3:2, the equinox value 15, and the year's total
     daylight = 366 · 15 muhūrtas exactly (the zigzag is symmetric).
 T5  "Calendar cycle ∼ metrical cycle" (owner's Chandas note): the
     intercalation pattern of the yuga is a word in theorum/71's prastāra —
     62 months with 2 adhimāsa positions (VJ places them at the middle and
     the end) — with an uddiṣṭa index and lagakriyā count C(62,2); the
     analogy is a REPRESENTATION (certified), not a deeper claim.
 NOT claimed: any observed position (the Dṛk channel); precession; the
     modern values; that the text's 366-day year is astronomically exact.
"""

import argparse
import hashlib
import json
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

from proof_lab.pingala_chandas_pratyaya import meru, uddishta

YUGA_DAYS = 1830
YEARS = 5
YEAR_DAYS = 366
SYN_MONTHS = 62
TITHIS = 1860
NAK_MONTHS = 67
SIDEREAL_DAYS = 1835
SOLAR_MONTHS = 60


def wind_phase(t: Fr, T: Fr) -> tuple[int, Fr]:
    q = t / T
    w = q.numerator // q.denominator
    return w, q - w


def daylight(d: int) -> Fr:
    """Muhūrtas on day d (0 = winter solstice): 12 + 6·d/183 up to d=183, then back down."""
    d = d % 366
    return Fr(12) + Fr(6 * d, 183) if d <= 183 else Fr(12) + Fr(6 * (366 - d), 183)


def build_certificate() -> dict[str, Any]:
    syn = Fr(YUGA_DAYS, SYN_MONTHS)
    yearly_residue = 12 * syn - YEAR_DAYS
    five = YEARS * yearly_residue
    t1 = yearly_residue == Fr(-366, 31) and five == -2 * syn and SOLAR_MONTHS + 2 == SYN_MONTHS and YEARS * YEAR_DAYS == YUGA_DAYS
    tithi = Fr(YUGA_DAYS, TITHIS)
    t2 = TITHIS - YUGA_DAYS == 30 and tithi == Fr(61, 62) and SIDEREAL_DAYS - YUGA_DAYS == YEARS and TITHIS == 30 * SYN_MONTHS
    periods = {"day": Fr(1), "tithi": tithi, "synodic_month": syn, "sidereal_month": Fr(YUGA_DAYS, NAK_MONTHS), "sidereal_day": Fr(YUGA_DAYS, SIDEREAL_DAYS), "year": Fr(YEAR_DAYS)}
    closes = {c: wind_phase(Fr(YUGA_DAYS), T) for c, T in periods.items()}
    t3 = all(ph == 0 for _, ph in closes.values())
    earlier = [t for t in range(1, YUGA_DAYS) if all(wind_phase(Fr(t), T)[1] == 0 for T in periods.values())]
    t3b = earlier == []
    dl = [daylight(d) for d in range(366)]
    t4 = dl[0] == 12 and dl[183] == 18 and Fr(dl[183], dl[0]) == Fr(3, 2) and daylight(91) + daylight(92) == 30 and sum(dl) == 366 * 15 and dl[183 + 91] == dl[183 - 91]
    word = "".join("G" if m in (31, 62) else "L" for m in range(1, 63))  # adhimāsa at mid and end of the yuga (months 31 and 62, 1-indexed)
    idx = uddishta(word)
    M = meru(62)
    t5 = word.count("G") == 2 and M[62][2] == 62 * 61 // 2 and 1 <= idx <= 2**62
    checks = {
        "T1_intercalation_smriti_2_adhimasa_closes_solar_lunar_residue_exactly": t1,
        "T2_tithi_ledger_30_ksaya_and_sidereal_minus_civil_equals_years": t2,
        "T3_all_cycle_phases_zero_at_yuga_end": t3,
        "T3_no_earlier_common_closure_before_1830": t3b,
        "T4_daylight_zigzag_12_to_18_ratio_3_2_total_366x15": t4,
        "T5_intercalation_pattern_is_a_prastara_word_with_uddishta_index": t5,
    }
    status = "PASS_VEDANGA_JYOTISA_YUGA_LEDGER_CANDIDATE" if all(checks.values()) else "FAIL_VEDANGA_JYOTISA_YUGA_LEDGER_CANDIDATE"
    return {
        "schema": "rkf.vedanga_jyotisa_yuga_ledger_candidate.v1",
        "status": status,
        "yearly_solar_lunar_residue_days": str(yearly_residue),
        "five_year_residue_days": str(five),
        "synodic_month_days": str(syn),
        "tithi_days": str(tithi),
        "closures_at_1830": {c: [w, str(ph)] for c, (w, ph) in closes.items()},
        "intercalation_word_uddishta": idx,
        "lagakriya_C_62_2": M[62][2],
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "VJ yuga closes exactly: 5-year solar–lunar residue = −2 synodic months = the intercalation Smṛti (owner's K = Res − S = 0 on the text's integers)",
                "tithi/kṣaya ledger; sidereal − civil days = years; all cycle phases zero at 1830 and at no earlier day",
                "daylight zigzag exact (3:2, equinox 15, symmetric, total 366·15 muhūrtas)",
                "calendar ∼ chandas as a certified representation in theorum/71's prastāra",
            ],
            "NOT_claimed": ["observed positions (Dṛk channel) and the Siddhānta prediction gap — no observation data; precession; modern constants; astronomical accuracy of the 366-day year", "RH, YM untouched"],
        },
        "checks": checks,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k, v)
    print("RESIDUE", payload["yearly_solar_lunar_residue_days"], payload["five_year_residue_days"], "CLOSURES", payload["closures_at_1830"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
