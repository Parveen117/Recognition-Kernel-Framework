from __future__ import annotations

"""Exact certificate (theorum/71): CHANDAS — Piṅgala's six pratyayas as exact
algorithms, the meru closure law of the owner's note, the mātrā-meru, and
the Gāyatrī's own metre read off theorum/67's line.

Owner's note (Vedic repo, "Pingala Meru Prastara Binary Chandas"):
  alphabet {L, G}, weights w(L)=1, w(G)=2; Prastāra(n) = {L,G}^n;
  meru closure  M(n,r) - M(n-1,r-1) - M(n-1,r) - S_M(n,r) = 0;
  meter closure K_C(u) = Rec(NF(Prastāra(u))) - Rec(u) - S_C(u) = 0.

Piṅgala's pratyayas (Chandaḥ-sūtra 8.20–8.35), each exact here:
  prastāra   the ordered table of all 2^n patterns (8.20–8.23: first G,
             then the L-row rule; we certify Piṅgala's order)
  naṣṭa      row index -> pattern (8.24–8.25: halve; even -> L, odd -> G ... )
  uddiṣṭa    pattern -> row index (8.26–8.27)
  lagakriyā  number of patterns with r gurus = meru = C(n, r) (8.28–8.31 meru)
  saṅkhyā    2^n by the doubling/squaring rule (8.28–8.31)
  adhvayoga  2·saṅkhyā − 1 (8.32–8.35)

Facts certified:
 T1  uddiṣṭa ∘ naṣṭa = id and naṣṭa ∘ uddiṣṭa = id on every row, n ≤ 10;
     naṣṭa(n, 1) = G^n (first row), naṣṭa(n, 2^n) = L^n (last row) -- the
     prastāra order is Piṅgala's.
 T2  meru closure with S_M = 0 for all n ≤ 12 with the correct boundary
     (M(n,0)=M(n,n)=1); control: a planted boundary M(n,0)=0 is still
     self-consistent under the recursion (residue 0 against itself!) but
     disagrees with the prastāra counts -- so S_M must be measured against
     the recognized object (Rec), as the owner's note writes it, not against
     the recursion alone.
     Row sums = saṅkhyā = 2^n; lagakriyā counts match the prastāra itself.
 T3  mātrā-meru: the number of patterns of total weight m (w(L)=1, w(G)=2)
     satisfies F(m) = F(m-1) + F(m-2), F(1)=1, F(2)=2 (Virahāṅka recursion),
     verified by enumeration for m ≤ 16.
 T4  GĀYATRĪ from theorum/67's text: syllabified, laghu/guru assigned by
     1.4.10–12 (hrasvaṃ laghu; saṃyoge guru; dīrghaṃ ca) with anusvāra /
     visarga as guru.  Result: pāda 1 has SEVEN syllables as written
     (ta-tsa-vi-tu-rva-re-ṇyaṃ), pādas 2 and 3 have eight.  The gāyatrī
     metre (3 x 8 = 24) is reached only with the traditional metrical
     restoration vareṇyam -> vareṇiyam (svarabhakti, a DECLARED Vedic
     reading, not a sūtra of the engine).  Both counts are certified; the
     uddiṣṭa index of each pāda's L/G pattern in the 8-syllable prastāra
     is computed.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.pada_to_line_external_sandhi import tok

# ---------------------------------------------------------------- pratyayas
def prastara(n: int) -> list[str]:
    """Piṅgala's order: row 1 = all G; each next row: find first G from the left, make it L,
    everything before it G, rest unchanged (8.23)."""
    rows = ["G" * n]
    while True:
        cur = rows[-1]
        i = cur.find("G")
        if i < 0:
            return rows
        rows.append("G" * i + "L" + cur[i + 1 :])


def nashta(n: int, row: int) -> str:
    """8.24–8.25: from row r, for each syllable: if r even -> L and halve; if odd -> G and (r+1)/2."""
    out = []
    for _ in range(n):
        if row % 2 == 0:
            out.append("L"); row //= 2
        else:
            out.append("G"); row = (row + 1) // 2
    return "".join(out)


def uddishta(pattern: str) -> int:
    """8.26–8.27: 1 + sum over L positions of 2^(i)."""
    return 1 + sum(2**i for i, ch in enumerate(pattern) if ch == "L")


def meru(n: int, broken_boundary: bool = False) -> list[list[int]]:
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][0] = 0 if broken_boundary else 1
        M[i][i] = 1 if i or not broken_boundary else M[i][i]
        for r in range(1, i):
            M[i][r] = M[i - 1][r - 1] + M[i - 1][r]
    return M


def meru_residue(M, n) -> int:
    return sum(abs(M[i][r] - M[i - 1][r - 1] - M[i - 1][r]) for i in range(2, n + 1) for r in range(1, i))


def sankhya(n: int) -> int:  # 8.28–8.31 doubling/squaring
    if n == 0:
        return 1
    return sankhya(n // 2) ** 2 if n % 2 == 0 else 2 * sankhya(n - 1)


def adhvayoga(n: int) -> int:
    return 2 * sankhya(n) - 1


# ---------------------------------------------------------------- mātrā-meru
def matra_count(m: int) -> int:
    """Number of L/G words of total weight m, by enumeration."""
    return sum(1 for n in range(m + 1) for p in prastara(n) if p.count("L") + 2 * p.count("G") == m) if m <= 16 else -1


# ---------------------------------------------------------------- Gāyatrī metre
VOW = {"a", "i", "u", "R", "A", "I", "U", "e", "o", "ai", "au"}
LONG = {"A", "I", "U", "e", "o", "ai", "au"}


def syllabify(phones: list[str]) -> list[tuple[str, str]]:
    """Split at vowels; a syllable is guru if its vowel is long / followed by anusvāra-visarga /
    followed by a consonant cluster (saṃyoga) before the next vowel."""
    idx = [i for i, p in enumerate(phones) if p in VOW]
    out = []
    for k, i in enumerate(idx):
        nxt = idx[k + 1] if k + 1 < len(idx) else len(phones)
        coda = phones[i + 1 : nxt]
        v = phones[i]
        guru = v in LONG or any(c in ("M", "H") for c in coda) or len([c for c in coda if c not in ("M", "H")]) >= 2
        start = idx[k - 1] + 1 if k else 0
        out.append(("".join(phones[start : i + 1]), "G" if guru else "L"))
    return out


def pada_meter(text: str):
    phones = list(tok(text.replace(" ", "")))
    syl = syllabify(phones)
    pattern = "".join(g for _, g in syl)
    return {"syllables": [s for s, _ in syl], "count": len(syl), "pattern": pattern, "uddishta_in_8": uddishta(pattern) if len(pattern) == 8 else None}


GAYATRI_PADAS = ["tat savitur vareNyaM", "bhargo devasya dhImahi", "dhiyo yo naH pracodayAt"]
RESTORED_PADA1 = "tat savitur vareNiyaM"  # declared Vedic metrical reading (svarabhakti)


def build_certificate() -> dict[str, Any]:
    t1 = all(nashta(n, r) == p and uddishta(p) == r for n in range(1, 11) for r, p in enumerate(prastara(n), start=1))
    order = all(prastara(n)[0] == "G" * n and prastara(n)[-1] == "L" * n and len(prastara(n)) == 2**n for n in range(1, 11))
    M = meru(12)
    t2 = meru_residue(M, 12) == 0 and all(sum(M[n][: n + 1]) == sankhya(n) == 2**n for n in range(13))
    lag = all(M[n][r] == sum(1 for p in prastara(n) if p.count("G") == r) for n in range(1, 11) for r in range(n + 1))
    # BUILD NOTE: the first control measured the broken meru against ITSELF (recursion residue) and found 0 --
    # a wrong boundary propagates consistently.  The owner's S_M must be measured against the recognized object
    # (lagakriyā counts from the prastāra itself): there the planted boundary shows a nonzero residue.
    Mb = meru(10, broken_boundary=True)
    broken = sum(abs(Mb[n][r] - sum(1 for p in prastara(n) if p.count("G") == r)) for n in range(1, 11) for r in range(n + 1)) > 0 and meru_residue(Mb, 10) == 0
    adh = all(adhvayoga(n) == 2 ** (n + 1) - 1 for n in range(11))
    F = [matra_count(m) for m in range(1, 17)]
    t3 = F[0] == 1 and F[1] == 2 and all(F[m] == F[m - 1] + F[m - 2] for m in range(2, 16))
    padas = [pada_meter(p) for p in GAYATRI_PADAS]
    restored = pada_meter(RESTORED_PADA1)
    counts = [p["count"] for p in padas]
    t4_written = counts == [7, 8, 8]
    t4_restored = restored["count"] == 8 and [restored["count"]] + counts[1:] == [8, 8, 8]
    checks = {
        "T1_uddishta_nashta_inverse_n_le_10_and_pingala_order": t1 and order,
        "T2_meru_closure_S_M_zero_rowsums_sankhya_lagakriya_matches_prastara": t2 and lag,
        "T2_planted_boundary_self_consistent_but_nonzero_against_prastara": broken,
        "T2_adhvayoga_2_sankhya_minus_1": adh,
        "T3_matra_meru_virahanka_recursion_m_le_16": t3,
        "T4_gayatri_as_written_7_8_8": t4_written,
        "T4_gayatri_with_declared_restoration_8_8_8_24": t4_restored,
    }
    status = "PASS_PINGALA_CHANDAS_PRATYAYA_CANDIDATE" if all(checks.values()) else "FAIL_PINGALA_CHANDAS_PRATYAYA_CANDIDATE"
    return {
        "schema": "rkf.pingala_chandas_pratyaya_candidate.v1",
        "status": status,
        "prastara_4": prastara(4),
        "meru_8": M[8][:9],
        "matra_counts_1_16": F,
        "gayatri_padas_as_written": padas,
        "gayatri_pada1_restored": restored,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Piṅgala's prastāra order; naṣṭa/uddiṣṭa mutually inverse (n ≤ 10); lagakriyā = meru = prastāra counts; saṅkhyā by doubling/squaring = 2^n; adhvayoga = 2·2^n − 1",
                "owner's meru closure law holds with S_M = 0 under the correct boundary; S_M is exactly the boundary defect (planted control)",
                "mātrā-meru (w(L)=1, w(G)=2) obeys the Virahāṅka/Fibonacci recursion by enumeration, m ≤ 16",
                "Gāyatrī from the theorum/67 text: 7-8-8 syllables as written; 8-8-8 = 24 only with the declared metrical restoration vareṇiyam; laghu/guru by 1.4.10–12",
            ],
            "NOT_claimed": ["the restoration vareṇiyam is DECLARED (Vedic recitation), not derived by a sūtra", "accent; caesura; the other vṛttas", "RH, YM untouched"],
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
    print("GAYATRI", [(p["count"], p["pattern"]) for p in payload["gayatri_padas_as_written"]], "RESTORED", payload["gayatri_pada1_restored"]["pattern"])
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
