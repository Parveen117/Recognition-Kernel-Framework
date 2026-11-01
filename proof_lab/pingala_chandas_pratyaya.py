from __future__ import annotations

"""Exact certificate (theorum/83): PIṄGALA'S SIX PRATYAYAS AS EXACT ALGORITHMS ON
THE LAGHU/GURU CARRIER — the Chandas Vedāṅga, first batch.

Quoted sūtras (Piṅgala, Chandaḥśāstra, adhyāya 8; numbering of the
Kedāranātha / Weber editions as used in the standard algorithmic reading):

 8.20  dvikau glau                      the two: g (guru) and l (laghu)
 8.21  miśrau ca                        and their mixtures
 8.22  pṛthag lā miśrāḥ                 [prastāra] l separately under the mixed ones
 8.23  vasavas trikāḥ                   the three-syllable forms are eight (vasu = 8)
 8.24  l-ardhe                          [naṣṭa] on halving, l
 8.25  saike g                          when one is added (odd), g
 8.26  pratilomagaṇaṁ dvir l-ādyam      [uddiṣṭa] reverse order; double from the first l
 8.27  tato gy ekaṁ jahyāt              then at a g subtract one
 8.28  dvir ardhe                       [saṅkhyā] two at a half
 8.29  rūpe śūnyam                      at a unit, zero
 8.30  dviḥ śūnye                       double at a zero
 8.31  tāvad ardhe tad guṇitam          at a half, multiply by itself
 8.32  dvir dvy ūnaṁ tad antānām        [adhvayoga] twice (the count), less two, for all up to the end
 8.34  pare pūrṇam                      [lagakriyā / meru] in the next, the full
 8.35  pare pūrṇam iti                  in the next, the full, thus

Carrier: words over {l, g} of length n (Piṅgala's syllable pattern of a line of
n syllables), the binary carrier already used by theorum/78's it-marker channel.

 T1  PRASTĀRA (8.20–8.23) enumerates all 2^n patterns without repetition, in
     the order in which the pattern of index k (1-based) reads, laghu = 1 and
     guru = 0, as the little-endian binary digits of k − 1; vasavas trikāḥ: the
     3-syllable prastāra has eight rows.
 T2  NAṢṬA (8.24–8.25) and UDDIṢṬA (8.26–8.27) are mutually inverse bijections
     between {1..2^n} and the prastāra rows, exhaustively for n ≤ 12.
 T3  SAṄKHYĀ (8.28–8.31) — Piṅgala's halving procedure — returns 2^n for every
     n ≤ 64 with ⌈log2 n⌉+popcount−1 multiplications (binary exponentiation);
     ADHVAYOGA (8.32) returns 2^(n+1) − 2 = Σ_{k=1..n} 2^k.
 T4  LAGAKRIYĀ / MERU (8.34–8.35): the meru row n gives the number of patterns
     with r laghus, equal to the exact count in the prastāra and to the
     binomial coefficient; the row sums to the saṅkhyā; the Vedic pādas
     (gāyatrī 24 = 3 × 8, triṣṭubh 44 = 4 × 11, jagatī 48 = 4 × 12) are the
     carriers of 8, 11, 12 syllables, whose prastāras have 256, 2048 and 4096 rows.
"""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SOURCES = {
    "8.20": "dvikau glau", "8.21": "miśrau ca", "8.22": "pṛthag lā miśrāḥ", "8.23": "vasavas trikāḥ",
    "8.24": "l-ardhe", "8.25": "saike g", "8.26": "pratilomagaṇaṁ dvir l-ādyam", "8.27": "tato gy ekaṁ jahyāt",
    "8.28": "dvir ardhe", "8.29": "rūpe śūnyam", "8.30": "dviḥ śūnye", "8.31": "tāvad ardhe tad guṇitam",
    "8.32": "dvir dvy ūnaṁ tad antānām", "8.34": "pare pūrṇam", "8.35": "pare pūrṇam iti",
}


# ---------------------------------------------------------------- prastāra 8.20–8.23
def prastara(n: int) -> list[str]:
    """8.20 the two letters; 8.21 mix them; 8.22 under the mixed rows of length n-1, write g-column then l-column."""
    if n == 0:
        return [""]
    if n == 1:
        return ["g", "l"]                                   # 8.20 dvikau glau
    prev = prastara(n - 1)                                  # 8.21 miśrau ca
    return [p + "g" for p in prev] + [p + "l" for p in prev]   # 8.22 pṛthag lā miśrāḥ: the new (last) column g over the mixed rows, then l separately below


# ---------------------------------------------------------------- naṣṭa 8.24–8.25: from the row number to the pattern
def nashta(n: int, k: int) -> str:
    out = []
    x = k
    for _ in range(n):
        if x % 2 == 0:
            out.append("l")                                 # 8.24 l-ardhe: even — halve, write l
            x //= 2
        else:
            out.append("g")                                 # 8.25 saike g: odd — add one and halve, write g
            x = (x + 1) // 2
    return "".join(out)


# ---------------------------------------------------------------- uddiṣṭa 8.26–8.27: from the pattern to the row number
def uddishta(pattern: str) -> int:
    x = 1
    for s in reversed(pattern):                             # 8.26 pratilomagaṇam: go in reverse order
        x *= 2                                              # dviḥ: double (from the first l on; before it the value is 1)
        if s == "g":
            x -= 1                                          # 8.27 tato gy ekaṁ jahyāt: at a g, subtract one
    return x


# ---------------------------------------------------------------- saṅkhyā 8.28–8.31: Piṅgala's halving procedure
def sankhya(n: int) -> tuple[int, int]:
    """Returns (2^n, number of multiplications).  8.28 write 2 when n is halved (even), 8.29 write 0 when 1 is
    subtracted (odd); then from the end: 8.30 at a 0 double, 8.31 at a 2 square."""
    marks = []
    x = n
    while x > 0:
        if x % 2 == 0:
            marks.append("2")                               # 8.28 dvir ardhe
            x //= 2
        else:
            marks.append("0")                               # 8.29 rūpe śūnyam
            x -= 1
    value, mults = 1, 0
    for m in reversed(marks):
        if m == "0":
            value *= 2                                      # 8.30 dviḥ śūnye
            mults += 1
        else:
            value *= value                                  # 8.31 tāvad ardhe tad guṇitam
            mults += 1
    return value, mults


def adhvayoga(n: int) -> int:
    """8.32 dvir dvy ūnaṁ tad antānām: twice the count, less two — the total of all metres of length 1..n."""
    return 2 * sankhya(n)[0] - 2


# ---------------------------------------------------------------- lagakriyā / meru 8.34–8.35
def meru(n: int) -> list[int]:
    """8.34–8.35 pare pūrṇam: each cell of the next row is the full sum of the two above it (first row 1)."""
    row = [1]
    for _ in range(n):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row


def binom(n: int, r: int) -> int:
    v = Fraction(1)
    for i in range(r):
        v *= Fraction(n - i, i + 1)
    assert v.denominator == 1
    return int(v)


def bits_little_endian(k: int, n: int) -> str:
    return "".join("l" if (k >> i) & 1 else "g" for i in range(n))


def t1_prastara() -> dict[str, Any]:
    rows = {n: prastara(n) for n in range(0, 13)}
    checks = {
        "prastara_has_2_pow_n_distinct_rows_n_le_12": all(len(rows[n]) == 2 ** n and len(set(rows[n])) == 2 ** n for n in rows),
        "vasavas_trikah_8_23_three_syllable_prastara_has_eight_rows": len(rows[3]) == 8,
        "row_k_reads_as_little_endian_binary_of_k_minus_1_laghu_is_1": all(rows[n][k - 1] == bits_little_endian(k - 1, n) for n in rows for k in range(1, 2 ** n + 1)),
        "first_row_all_guru_last_row_all_laghu": all(rows[n][0] == "g" * n and rows[n][-1] == "l" * n for n in rows if n > 0),
    }
    return {"checks": checks, "prastara_3": rows[3], "prastara_4": rows[4]}


def t2_nashta_uddishta() -> dict[str, Any]:
    ok_nashta = ok_uddishta = ok_inverse = True
    for n in range(0, 13):
        rows = prastara(n)
        for k, p in enumerate(rows, start=1):
            ok_nashta &= nashta(n, k) == p
            ok_uddishta &= uddishta(p) == k
            ok_inverse &= uddishta(nashta(n, k)) == k and nashta(n, uddishta(p)) == p
    checks = {
        "nashta_8_24_25_returns_row_k_of_the_prastara_n_le_12": ok_nashta,
        "uddishta_8_26_27_returns_the_row_number_n_le_12": ok_uddishta,
        "nashta_and_uddishta_mutually_inverse_n_le_12": ok_inverse,
    }
    return {"checks": checks, "examples": {"nashta(4, 11)": nashta(4, 11), "uddishta('glgl')": uddishta("glgl"), "uddishta('gggg')": uddishta("gggg"), "uddishta('llll')": uddishta("llll")}}


def t3_sankhya_adhvayoga() -> dict[str, Any]:
    vals = {n: sankhya(n) for n in range(0, 65)}
    naive_bound = all(vals[n][1] <= n for n in vals)
    log_bound = all(vals[n][1] == (n.bit_length() - 1) + bin(n).count("1") for n in vals if n > 0)
    checks = {
        "sankhya_8_28_31_equals_2_pow_n_for_n_le_64": all(vals[n][0] == 2 ** n for n in vals),
        "multiplications_equal_floor_log2_plus_popcount_binary_exponentiation": log_bound and naive_bound,
        "adhvayoga_8_32_equals_sum_of_sankhya_1_to_n_for_n_le_64": all(adhvayoga(n) == sum(2 ** k for k in range(1, n + 1)) for n in range(0, 65)),
    }
    return {"checks": checks, "sankhya_table": {n: vals[n][0] for n in range(0, 13)}, "multiplications": {n: vals[n][1] for n in range(1, 17)}, "adhvayoga_table": {n: adhvayoga(n) for n in range(1, 9)}}


VEDIC_METRES = {"gāyatrī": 24, "uṣṇik": 28, "anuṣṭubh": 32, "bṛhatī": 36, "paṅkti": 40, "triṣṭubh": 44, "jagatī": 48}   # traditional syllable counts of the seven Vedic metres (declared, not quoted here)
PADA_SYLLABLES = {"gāyatrī": 8, "anuṣṭubh": 8, "triṣṭubh": 11, "jagatī": 12}


def t4_meru_and_vedic_metres() -> dict[str, Any]:
    ok_meru = ok_sum = ok_count = True
    for n in range(0, 13):
        row = meru(n)
        rows = prastara(n)
        ok_meru &= row == [binom(n, r) for r in range(n + 1)]
        ok_sum &= sum(row) == sankhya(n)[0]
        ok_count &= all(sum(1 for p in rows if p.count("l") == r) == row[r] for r in range(n + 1))
    pada = {m: {"syllables_per_pada": s, "prastara_rows": sankhya(s)[0], "meru_row": meru(s)} for m, s in PADA_SYLLABLES.items()}
    checks = {
        "meru_8_34_35_row_n_equals_binomial_coefficients_n_le_12": ok_meru,
        "meru_row_sums_to_sankhya": ok_sum,
        "meru_cell_r_equals_number_of_prastara_rows_with_r_laghus": ok_count,
        "vedic_pada_carriers_8_11_12_have_256_2048_4096_rows": pada["gāyatrī"]["prastara_rows"] == 256 and pada["triṣṭubh"]["prastara_rows"] == 2048 and pada["jagatī"]["prastara_rows"] == 4096,
        "vedic_metre_lengths_are_pada_multiples": VEDIC_METRES["gāyatrī"] == 3 * 8 and VEDIC_METRES["anuṣṭubh"] == 4 * 8 and VEDIC_METRES["triṣṭubh"] == 4 * 11 and VEDIC_METRES["jagatī"] == 4 * 12,
    }
    return {"checks": checks, "meru_rows_0_to_6": {n: meru(n) for n in range(7)}, "vedic_padas": pada}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_prastara": t1_prastara(), "t2_nashta_uddishta": t2_nashta_uddishta(), "t3_sankhya_adhvayoga": t3_sankhya_adhvayoga(), "t4_meru_and_vedic_metres": t4_meru_and_vedic_metres()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PINGALA_CHANDAS_PRATYAYA_CANDIDATE" if all(checks.values()) else "FAIL_PINGALA_CHANDAS_PRATYAYA_CANDIDATE"
    return {
        "schema": "rkf.pingala_chandas_pratyaya_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "prastāra 8.20–8.23 enumerates the 2^n patterns, row k = little-endian binary of k−1 with laghu = 1 (n ≤ 12)",
                "naṣṭa 8.24–8.25 and uddiṣṭa 8.26–8.27 are mutually inverse bijections (n ≤ 12)",
                "saṅkhyā 8.28–8.31 = 2^n with ⌊log2 n⌋ + popcount multiplications (n ≤ 64); adhvayoga 8.32 = 2^(n+1) − 2",
                "meru 8.34–8.35 = binomial coefficients = counts of r-laghu rows, summing to the saṅkhyā (n ≤ 12); Vedic pāda carriers of 8, 11, 12 syllables",
            ],
            "NOT_claimed": [
                "the sūtra numbering follows the standard printed editions (Kedāranātha / Weber); other editions number differently",
                "the reading of 8.34–8.35 as the meru is Halāyudha's commentary, cited",
                "metre identification of actual Vedic lines, gaṇa system, mātrā metres (chapters 1–7), pātākā-prastāra (later commentators); the seven metre lengths are the traditional table, declared not quoted; theorum/65's Gāyatrī (the mantra) is not touched",
                "no link to RH or YM is claimed",
            ],
        },
        "checks": checks,
        **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


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
