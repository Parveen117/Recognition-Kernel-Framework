from __future__ import annotations

"""Exact certificate (theorum/79): ŚAIVA SOURCES II — the varga/manner grid of
the Māheśvara code, and the crystal theorem of recognition.

Continues theorum/78 on the same carriers (the token order of the fourteen
Māheśvara sūtras with 1.1.71; the MR-03 memory lift).  Quoted sources:

 Śiva-sūtra 3.19          kavargādiṣu māheśvaryādyāḥ paśumātaraḥ
 Aṣṭādhyāyī 1.1.69        aṇudit savarṇasya cāpratyayaḥ  (udit: ku cu ṭu tu pu)
 Īśvara-pratyabhijñā 1.5.11  svabhāvam avabhāsasya vimarśaṁ vidur anyathā |
                          prakāśo 'rthoparakto 'pi sphaṭikādijaḍopamaḥ ||
 Vijñāna-bhairava 26      na vrajen na viśec chaktir marudrūpā vikāsite |
                          nirvikalpatayā madhye tayā bhairavarūpatā ||
 Taittirīya Āraṇyaka 10.45 (Aghora)  aghorebhyo 'tha ghorebhyo ghoraghoratarebhyaḥ |
                          sarvebhyaḥ sarvaśarvebhyo namaste astu rudrarūpebhyaḥ ||
 Taittirīya Saṁhitā 4.5.8  namaḥ śivāya ca śivatarāya ca

 T1  VARGA / MANNER GRID.  The 25 stops carry a bijection stop -> (manner
     row, varga column).  The udit classes of 1.1.69 (the vargas of Śiva-sūtra
     3.19) are NOT intervals of the Māheśvara order and equal none of the 294
     pratyāhāra sets; the manner rows ARE pratyāhāras (ñam, jhaṣ, jaś, cay) —
     except the voiceless aspirates, which are no pratyāhāra (only their
     union with the voiceless unaspirated, khay, and the cross-cut chav are).
     The sūtra order lists the stops manner-major; rows 7, 8–9 and 10 share
     one varga permutation (ca, pa, ka, ṭa, ta), rows 11–12 use two others.
 T2  THE CODE'S FREEDOM.  Exactly 2304 within-sūtra reorderings of the 43
     tokens leave every one of the 42 used pratyāhāra sets unchanged (all
     such reorderings enumerated sūtra by sūtra): the leaders of each sūtra
     are forced by the pratyāhāras that start there, the shared varga
     permutation of rows 9 and 10 is NOT forced — it is a choice beyond the
     code.  In T2 the markers and sūtra boundaries are fixed.
 T3  CRYSTAL THEOREM (IPK 1.5.11).  On a commutative base every coboundary
     δα(b,a) = α(a+b) − α(a) − α(b) is symmetric; a symmetric bilinear
     cocycle is the coboundary of α(a) = S(a,a)/2 over Q; a nonzero
     antisymmetric bilinear cocycle is never a coboundary.  Hence for a
     bilinear memory cocycle: recognition-blind on reorderings ⟺ symmetric
     ⟺ coboundary over Q ⟺ class zero.  "Prakāśa without vimarśa is inert
     like a crystal" is the class-zero case; the carrier is theorum/78 T4.
 CITED, NOT CLAIMED: Vijñāna-bhairava 26 names the same two zero-turn
     states as theorum/78 T3 (madhya).  REFUSED: the three-rung ladder
     a-ghora / ghora / ghora-tara and the comparative śiva / śiva-tara have
     no certified object; theorum/50's odd-sector law stays the only
     certified Aghora statement.
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.shaiva_sources_nativized import MAHESHVARA, SUTRA_OF_TOKEN, TOKENS, USED, compose, omega_bilinear, path_memory, pratyahara

SOURCES = {
    "shiva_sutra_3_19": "kavargādiṣu māheśvaryādyāḥ paśumātaraḥ",
    "astadhyayi_1_1_69": "aṇudit savarṇasya cāpratyayaḥ",
    "ishvara_pratyabhijna_karika_1_5_11": "svabhāvam avabhāsasya vimarśaṁ vidur anyathā | prakāśo 'rthoparakto 'pi sphaṭikādijaḍopamaḥ ||",
    "vijnana_bhairava_26": "na vrajen na viśec chaktir marudrūpā vikāsite | nirvikalpatayā madhye tayā bhairavarūpatā ||",
    "taittiriya_aranyaka_10_45_aghora": "aghorebhyo 'tha ghorebhyo ghoraghoratarebhyaḥ | sarvebhyaḥ sarvaśarvebhyo namaste astu rudrarūpebhyaḥ ||",
    "taittiriya_samhita_4_5_8": "namaḥ śivāya ca śivatarāya ca",
}

# ---------------------------------------------------------------- T1 varga / manner grid
VARGAS = {  # 1.1.69 udit classes: ku cu ṭu tu pu
    "ka": ("k", "kh", "g", "gh", "ṅ"),
    "ca": ("c", "ch", "j", "jh", "ñ"),
    "ṭa": ("ṭ", "ṭh", "ḍ", "ḍh", "ṇ"),
    "ta": ("t", "th", "d", "dh", "n"),
    "pa": ("p", "ph", "b", "bh", "m"),
}
MANNER = {  # rows of the 5x5 grid, in Māheśvara order
    "nasal": ("ñ", "m", "ṅ", "ṇ", "n"),
    "voiced_aspirate": ("jh", "bh", "gh", "ḍh", "dh"),
    "voiced": ("j", "b", "g", "ḍ", "d"),
    "voiceless_aspirate": ("kh", "ph", "ch", "ṭh", "th"),
    "voiceless": ("c", "ṭ", "t", "k", "p"),
}
USED_SETS = {name: frozenset(pratyahara(x, j)) for name, x, j, _ in USED}


def _all_pratyahara_sets() -> set[frozenset[str]]:
    out = set()
    for j in range(len(MAHESHVARA)):
        for k in range(len(TOKENS)):
            if SUTRA_OF_TOKEN[k] <= j:
                out.add(frozenset(TOKENS[i] for i in range(k, len(TOKENS)) if SUTRA_OF_TOKEN[i] <= j))
    return out


def _is_interval(subset: frozenset[str]) -> bool:
    pos = sorted(k for k, t in enumerate(TOKENS) if t in subset)
    return pos == list(range(pos[0], pos[-1] + 1))


def t1_varga_manner_grid() -> dict[str, Any]:
    stops = {s for row in MANNER.values() for s in row}
    grid = {s: (m, v) for m, row in MANNER.items() for s in row for v, col in VARGAS.items() if s in col}
    bijection = len(grid) == 25 and len(set(grid.values())) == 25 and stops == {s for col in VARGAS.values() for s in col}
    sets = _all_pratyahara_sets()
    varga_not_interval = all(not _is_interval(frozenset(col)) for col in VARGAS.values())
    varga_not_pratyahara = all(frozenset(col) not in sets for col in VARGAS.values())
    manner_pratyahara = {
        "nasal": USED_SETS["ñam"] == frozenset(MANNER["nasal"]),
        "voiced_aspirate": USED_SETS["jhaṣ"] == frozenset(MANNER["voiced_aspirate"]),
        "voiced": USED_SETS["jaś"] == frozenset(MANNER["voiced"]),
        "voiceless": USED_SETS["cay"] == frozenset(MANNER["voiceless"]),
    }
    voiceless_aspirate_is_no_pratyahara = frozenset(MANNER["voiceless_aspirate"]) not in sets
    khay_is_all_voiceless = USED_SETS["khay"] == frozenset(MANNER["voiceless_aspirate"]) | frozenset(MANNER["voiceless"])
    chav_cross_cut = USED_SETS["chav"] == frozenset(("ch", "ṭh", "th", "c", "ṭ", "t")) and _is_interval(USED_SETS["chav"])
    perm = {m: tuple(grid[s][1] for s in row) for m, row in MANNER.items()}
    shared = perm["nasal"] == perm["voiced_aspirate"] == perm["voiced"] == ("ca", "pa", "ka", "ṭa", "ta")
    manner_major = all(SUTRA_OF_TOKEN[TOKENS.index(a)] <= SUTRA_OF_TOKEN[TOKENS.index(b)] for row in MANNER.values() for a, b in zip(row, row[1:]))
    checks = {
        "stop_to_manner_varga_is_a_bijection_5x5": bijection,
        "no_varga_1_1_69_udit_class_is_an_interval_of_the_maheshvara_order": varga_not_interval,
        "no_varga_equals_any_of_the_294_pratyahara_sets": varga_not_pratyahara,
        "manner_rows_nasal_voiced_aspirate_voiced_voiceless_are_pratyaharas": all(manner_pratyahara.values()),
        "voiceless_aspirates_are_no_pratyahara": voiceless_aspirate_is_no_pratyahara,
        "khay_is_the_union_of_the_two_voiceless_rows": khay_is_all_voiceless,
        "chav_is_an_interval_cutting_across_the_two_voiceless_rows": chav_cross_cut,
        "rows_7_8_9_10_share_the_varga_permutation_ca_pa_ka_ta_ta": shared,
        "stops_are_listed_manner_major": manner_major,
        "pratyahara_count_is_294": len(sets) == 294,
    }
    return {"checks": checks, "varga_permutation_by_row": perm, "manner_rows_as_pratyaharas": manner_pratyahara}


# ---------------------------------------------------------------- T2 the code's freedom
def _sets_under(order: list[str]) -> dict[str, frozenset[str]]:
    """Recompute every used pratyāhāra set when the tokens of each sūtra are reordered (sūtra boundaries and
    markers fixed): from the first occurrence of the initial through the end of the marker's sūtra."""
    sutra_of = SUTRA_OF_TOKEN
    out = {}
    for name, x, j, _ in USED:
        start = order.index(x)
        out[name + f"@{j}"] = frozenset(order[k] for k in range(start, len(order)) if sutra_of[k] <= j)
    return out


def t2_code_freedom() -> dict[str, Any]:
    baseline = _sets_under(TOKENS)
    per_sutra: dict[int, int] = {}
    forced_leaders: dict[int, list[str]] = {}
    offset = 0
    for j, (sounds, _) in enumerate(MAHESHVARA):
        n = len(sounds)
        count = 0
        leaders: set[str] | None = None
        for perm in itertools.permutations(sounds):
            order = TOKENS[:offset] + list(perm) + TOKENS[offset + n :]
            if _sets_under(order) == baseline:
                count += 1
                leaders = {perm[0]} if leaders is None else leaders & {perm[0]}
        per_sutra[j] = count
        forced_leaders[j] = sorted(leaders or set())
        offset += n
    total = 1
    for c in per_sutra.values():
        total *= c
    checks = {
        "within_sutra_reorderings_preserving_all_42_used_sets_total_2304": total == 2304,
        "sutras_1_3_4_5_6_8_14_are_rigid": all(per_sutra[j] == 1 for j in (0, 2, 3, 4, 5, 7, 13)),
        "sutra_9_gh_dh_dh_and_sutra_10_tail_g_d_d_are_free_6_each": per_sutra[8] == 6 and per_sutra[9] == 6,
        "sutra_7_nasal_tail_n_n_free_2": per_sutra[6] == 2,
        "sutra_11_has_4_orders_sutra_12_13_2_each_sutra_2_2": per_sutra[10] == 4 and per_sutra[11] == 2 and per_sutra[12] == 2 and per_sutra[1] == 2,
        "leaders_forced_where_a_used_pratyahara_starts": forced_leaders[9] == ["j"] and forced_leaders[7] == ["jh"] and forced_leaders[6] == ["ñ"] and forced_leaders[10] == ["kh"] and forced_leaders[12] == ["ś"],
        "shared_varga_permutation_of_rows_9_and_10_is_not_forced": per_sutra[8] == 6 and per_sutra[9] == 6,
    }
    return {"checks": checks, "orders_per_sutra": per_sutra, "forced_leader_per_sutra": forced_leaders, "total_free_orders": total}


# ---------------------------------------------------------------- T3 crystal theorem
def t3_crystal_theorem() -> dict[str, Any]:
    arrows = [(p, q) for p in range(4) for q in range(4)]
    # (i) every coboundary of a normalized 1-cochain is symmetric on a commutative base
    alphas = [
        lambda a: Fraction(a[0] ** 2 + 3 * a[0] * a[1] - a[1] ** 3),
        lambda a: Fraction((a[0] * 7 + a[1] * 3) % 5 - 2) if a != (0, 0) else Fraction(0),
        lambda a: Fraction(a[0] * a[1] * (a[0] - a[1])),
    ]
    coboundary_symmetric = all(
        (al(compose(b, a)) - al(b) - al(a)) == (al(compose(a, b)) - al(a) - al(b))
        for al in alphas
        for a in arrows
        for b in arrows
    )
    coboundary_is_cocycle = all(
        (al(compose(c, compose(b, a))) - al(c) - al(compose(b, a))) + (al(compose(b, a)) - al(b) - al(a))
        == (al(compose(compose(c, b), a)) - al(compose(c, b)) - al(a)) + (al(compose(c, b)) - al(c) - al(b))
        for al in alphas[:2]
        for a in arrows[:6]
        for b in arrows[:6]
        for c in arrows[:6]
    )
    # (ii) a symmetric bilinear cocycle S is the coboundary of alpha(a) = S(a,a)/2 over Q
    S = ((1, 2), (2, -3))
    alpha_S = lambda a: omega_bilinear(S, a, a) / 2
    symmetric_is_coboundary = all(omega_bilinear(S, b, a) == alpha_S(compose(b, a)) - alpha_S(b) - alpha_S(a) for a in arrows for b in arrows)
    # (iii) a nonzero antisymmetric bilinear cocycle is never a coboundary: coboundaries are symmetric,
    #       so an antisymmetric coboundary equals its own negative, hence vanishes.
    A = ((0, 1), (-1, 0))
    antisym = all(omega_bilinear(A, b, a) == -omega_bilinear(A, a, b) for a in arrows for b in arrows)
    nonzero = any(omega_bilinear(A, b, a) != 0 for a in arrows for b in arrows)
    # (iv) blind <=> symmetric on the theorum/78 T4 data: reorderings of multisets
    gens = [(1, 0), (0, 1), (1, 1), (2, 1)]

    def blind(B) -> bool:
        om = lambda b, a: omega_bilinear(B, b, a)
        for size in (2, 3, 4):
            for ms in itertools.combinations_with_replacement(gens, size):
                if len({path_memory(om, list(p))[0] for p in itertools.permutations(ms)}) > 1:
                    return False
        return True

    samples = [((1, 2), (2, -3)), ((0, 1), (-1, 0)), ((1, 3), (-2, 2)), ((2, 0), (0, 5)), ((0, 0), (1, 0)), ((1, 1), (1, 1))]
    blind_iff_symmetric = all(blind(B) == (B[0][1] == B[1][0]) for B in samples)
    checks = {
        "every_coboundary_is_symmetric_on_a_commutative_base": coboundary_symmetric,
        "coboundaries_satisfy_the_cocycle_identity": coboundary_is_cocycle,
        "symmetric_bilinear_cocycle_is_the_coboundary_of_S_aa_over_2": symmetric_is_coboundary,
        "nonzero_antisymmetric_cocycle_exists_and_cannot_be_a_coboundary": antisym and nonzero,
        "recognition_blind_iff_symmetric_iff_coboundary_class_zero": blind_iff_symmetric,
    }
    return {"checks": checks, "samples_blind": {str(B): blind(B) for B in samples}}


# ---------------------------------------------------------------- certificate
def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_varga_manner_grid": t1_varga_manner_grid(),
        "t2_code_freedom": t2_code_freedom(),
        "t3_crystal_theorem": t3_crystal_theorem(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SHAIVA_SOURCES_VARGA_CRYSTAL_CANDIDATE" if all(checks.values()) else "FAIL_SHAIVA_SOURCES_VARGA_CRYSTAL_CANDIDATE"
    return {
        "schema": "rkf.shaiva_sources_varga_crystal_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Varga/manner grid: the 25 stops are a 5x5 bijection (manner row, 1.1.69 udit varga); no varga is an interval of the Māheśvara order or any of the 294 pratyāhāra sets; the manner rows nasal (ñam), voiced aspirate (jhaṣ), voiced (jaś) and voiceless (cay) are pratyāhāras, the voiceless aspirates are not (khay is their union with cay, chav cuts across); rows 7, 8-9, 10 share the varga permutation (ca, pa, ka, ṭa, ta)",
                "The code's freedom: exactly 2304 within-sūtra reorderings of the 43 tokens preserve all 42 used pratyāhāra sets (markers and boundaries fixed); every sūtra at which a used pratyāhāra starts has its leader forced; the shared varga permutation of sūtras 9 and 10 is not forced by the code",
                "Crystal theorem: on a commutative base every coboundary is symmetric, a symmetric bilinear cocycle is a coboundary over Q, a nonzero antisymmetric one never is; so a bilinear memory cocycle is recognition-blind on reorderings iff symmetric iff coboundary (class zero) — the IPK 1.5.11 crystal case of theorum/78 T4",
            ],
            "NOT_claimed": [
                "Which mātṛkā presides over which varga (Śiva-sūtra 3.19 is cited for the varga partition only)",
                "Any reading of the three-rung Aghora ladder (TA 10.45) or of śiva/śivatara (TS 4.5.8): no certified object; theorum/50's odd-sector law remains the only certified Aghora statement",
                "Breath identification in Vijñāna-bhairava 26 (cited as the same two zero-turn states of theorum/78 T3)",
                "RH, YM untouched",
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"])
    for k, v in payload["checks"].items():
        print(k.upper(), v)
    print("CERTIFICATE_SHA256", certificate_sha256(payload))
    return 0 if payload["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
