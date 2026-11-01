from __future__ import annotations

"""Exact certificate (theorum/78): ŚAIVA SOURCES CITED AND NATIVIZED — the
Māheśvara-sūtra interval code, the Spanda turn group, the Pratyabhijñā
recognition defect.

Every statement below starts from a quoted primary text (the fourteen
Māheśvara sūtras with the Nandikeśvara-kāśikā verse, Aṣṭādhyāyī 1.1.71 /
1.3.3 / 1.3.9 / 1.1.69, Spanda-kārikā 1.1–1.2, Vijñāna-bhairava 24, Śiva-sūtra
1.4 / 2.7, Īśvara-pratyabhijñā-kārikā 1.1.1 with the Vimarśinī gloss,
Pratyabhijñā-hṛdaya 11) and is either an exact finite theorem on an object the
framework already owns — the recognized/memory two-channel carrier of
theorum/58, the EMK turn R of theorum/55 and its native dagger (theorum/50),
the cocycle memory lift of MR-03 — or an explicit refusal.  Nothing
interpretive is claimed; the Sanskrit is the source of the DEFINITIONS, the
certificate is the source of the VERDICTS.

 T1  MĀHEŚVARA INTERVAL CODE.  The fourteen sūtras (43 sound tokens, 42
     sounds — h twice — 14 it-markers, 1.3.3 hal antyam, deleted by 1.3.9)
     generate pratyāhāras by 1.1.71 ādir antyena sahetā as INTERVALS of the
     token order: recognized initial + memory marker.  Certified: ik equals
     theorum/58's IK; 58's ten-vowel carrier is the 1.1.69 savarṇa closure of
     ac restricted by 58's own declaration (ṛ ḷ omitted by 58, not by the
     sūtras); 305 (initial, later marker) pairs; all 42 pratyāhāras of the
     traditional list are intervals of the order with two h positions; the
     ONLY name with two sets is aṇ; no marker is ever a member of its set.
 T2  THE REPEATED h IS NECESSARY (the fourteenth beat).  With one h there is
     NO linear order of the 42 sounds in which ac, aṭ, yaṇ, yar, val and hal
     are all intervals: exhaustive over the membership atoms (contraction
     lemma in the note), 720 orders, none works; with h split in two, the
     Māheśvara order itself works.  So any interval code of these six
     Aṣṭādhyāyī classes repeats a sound, and the sūtras repeat exactly h.
 T3  SPANDA TURN GROUP.  Spanda 1.1 unmeṣa/nimeṣa, śakti-cakra; 1.2 "no
     obstruction anywhere".  On the EMK carrier the odd generator R (R² = −I,
     theorum/55 T1) generates the cyclic group {I, R, −I, −R} of order
     exactly four; nimeṣa = R³ = R† (native dagger); R R† = I; the orbit of a
     seed has four states of which exactly two have zero turn channel
     (Vijñāna-bhairava 24 "utpatti-dvitaya-sthāna", cited, not claimed);
     Exp(tD) Exp(−tD) = I exactly in jets for D = ωR AND for the nilpotent
     control — unobstructedness is a property of every odd-generator flow —
     while lopa (1.3.9, the zero map of theorum/56 B2) has no right inverse.
 T4  PRATYABHIJÑĀ RECOGNITION DEFECT (MR-03 extension).  For two histories
     with the same composite, δ(γ,η) = Ω(γ) − Ω(η).  On a commutative base
     with a bilinear cocycle ω_B: δ between reorderings of the same arrows
     depends only on the antisymmetric (turn) part of B — the symmetric part
     is recognition-blind — and δ is invariant under every coboundary gauge
     change when the two histories use the same arrow multiset; across
     different decompositions of one composite it shifts by the gauge sums
     (recorded obligation).  MR-03 §9's ω(b,a) = ba is symmetric, hence
     blind; the turn cocycle q'p distinguishes xy from yx (δ = 1).
 REFUSED / NOT CLAIMED: marker-count minimality of the fourteen sūtras (a
     published classical theorem, not re-derived here); breath, deity,
     ontology, or any identification of Ω, π, δ with the five acts beyond
     vocabulary; RH, YM untouched.
"""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab.generalized_euler_emk_dock import I2, R, is_anti_self_dagger
from proof_lab.loop_residue_first_visible_jet_binding import DEPTH, j_add, j_const, j_mul, j_scale
from proof_lab.native_seam_gap_odd_covariance import dagger, eye, is_zero, m_scale, m_sub, mat, sc, star, zeros
from proof_lab.paninian_seam_calculus import IK, VOWELS

# ---------------------------------------------------------------- sources (quoted)
SOURCES = {
    "nandikesvara_kasika_1": "nṛttāvasāne naṭarājarājo nanāda ḍhakkāṁ navapañcavāram | uddhartukāmaḥ sanakādisiddhān etad vimarśe śivasūtrajālam ||",
    "maheshvara_sutras": "a i u ṇ | ṛ ḷ k | e o ṅ | ai au c | ha ya va ra ṭ | la ṇ | ña ma ṅa ṇa na m | jha bha ñ | gha ḍha dha ṣ | ja ba ga ḍa da ś | kha pha cha ṭha tha ca ṭa ta v | ka pa y | śa ṣa sa r | ha l ||",
    "astadhyayi_1_1_71": "ādir antyena sahetā",
    "astadhyayi_1_3_3": "halantyam",
    "astadhyayi_1_3_9": "tasya lopaḥ",
    "astadhyayi_1_1_69": "aṇudit savarṇasya cāpratyayaḥ",
    "spanda_karika_1_1": "yasyonmeṣanimeṣābhyāṁ jagataḥ pralayodayau | taṁ śakticakravibhavaprabhavaṁ śaṅkaraṁ stumaḥ ||",
    "spanda_karika_1_2": "yatra sthitam idaṁ sarvaṁ kāryaṁ yasmāc ca nirgatam | tasyānāvṛtarūpatvān na nirodho 'sti kutracit ||",
    "vijnana_bhairava_24": "ūrdhve prāṇo hy adho jīvo visargātmā paroccaret | utpattidvitayasthāne bharaṇād bharitā sthitiḥ ||",
    "shiva_sutra_1_4": "jñānādhiṣṭhānaṁ mātṛkā",
    "shiva_sutra_2_7": "mātṛkācakrasambodhaḥ",
    "ishvara_pratyabhijna_karika_1_1_1": "kathañcid āsādya maheśvarasya dāsyaṁ janasyāpy upakāram icchan | samastasampatsamavāptihetuṁ tatpratyabhijñām upapādayāmi ||",
    "vimarsini_gloss_on_1_1_1": "pratīpam ātmābhimukhyena jñānaṁ prakāśaḥ pratyabhijñā — the recognition 'sa evāyam' (this is that same one)",
    "pratyabhijna_hrdaya_11": "ābhāsanaraktivimarśanabījāvasthāpanavilāpanatas tāni",
}

# ---------------------------------------------------------------- T1 the fourteen sūtras as a token order
MAHESHVARA: list[tuple[tuple[str, ...], str]] = [
    (("a", "i", "u"), "ṇ"),
    (("ṛ", "ḷ"), "k"),
    (("e", "o"), "ṅ"),
    (("ai", "au"), "c"),
    (("h", "y", "v", "r"), "ṭ"),
    (("l",), "ṇ"),
    (("ñ", "m", "ṅ", "ṇ", "n"), "m"),
    (("jh", "bh"), "ñ"),
    (("gh", "ḍh", "dh"), "ṣ"),
    (("j", "b", "g", "ḍ", "d"), "ś"),
    (("kh", "ph", "ch", "ṭh", "th", "c", "ṭ", "t"), "v"),
    (("k", "p"), "y"),
    (("ś", "ṣ", "s"), "r"),
    (("h",), "l"),
]
TOKENS: list[str] = [s for sounds, _ in MAHESHVARA for s in sounds]  # 43 sound tokens in order
SUTRA_OF_TOKEN: list[int] = [i for i, (sounds, _) in enumerate(MAHESHVARA) for _ in sounds]


def pratyahara(initial: str, marker_sutra: int) -> tuple[str, ...]:
    """1.1.71 ādir antyena sahetā: the initial sound (recognized channel) together with the
    it-marker closing sūtra `marker_sutra` (memory channel, 1.3.3 / 1.3.9) denotes the sound
    tokens from the FIRST occurrence of the initial through the end of that sūtra."""
    start = TOKENS.index(initial)
    assert SUTRA_OF_TOKEN[start] <= marker_sutra, (initial, marker_sutra)
    out = [t for k, t in enumerate(TOKENS) if k >= start and SUTRA_OF_TOKEN[k] <= marker_sutra]
    return tuple(out)


# the traditional list of pratyāhāras used in the Aṣṭādhyāyī: (name, initial, marker sūtra index, where used)
# Sūtra numbers are given where the use is certain; "traditional list" otherwise.
USED: list[tuple[str, str, int, str]] = [
    ("aṇ", "a", 0, "1.1.51 ur aṇ raparaḥ (short aṇ)"),
    ("aṇ", "a", 5, "1.1.69 aṇudit savarṇasya cāpratyayaḥ (long aṇ)"),
    ("ak", "a", 1, "6.1.101 akaḥ savarṇe dīrghaḥ"),
    ("ik", "i", 1, "1.1.3 iko guṇavṛddhī; 6.1.77 iko yaṇ aci"),
    ("uk", "u", 1, "traditional list"),
    ("eṅ", "e", 2, "6.1.94 eṅi pararūpam"),
    ("ac", "a", 3, "6.1.77 iko yaṇ aci"),
    ("ic", "i", 3, "traditional list"),
    ("ec", "e", 3, "6.1.78 eco 'yavāyāvaḥ"),
    ("aic", "ai", 3, "traditional list"),
    ("aṭ", "a", 4, "8.4.2 aṭkupvāṅnumvyavāye 'pi"),
    ("iṇ", "i", 5, "8.3.57 iṇkoḥ"),
    ("yaṇ", "y", 5, "6.1.77 iko yaṇ aci"),
    ("am", "a", 6, "traditional list"),
    ("yam", "y", 6, "8.4.64 halo yamāṁ yami lopaḥ"),
    ("ñam", "ñ", 6, "traditional list"),
    ("ṅam", "ṅ", 6, "8.3.32 ṅamo hrasvād aci ṅamuṇ nityam"),
    ("yañ", "y", 7, "traditional list"),
    ("jhaṣ", "jh", 8, "8.2.37 ekāco baśo bhaṣ jhaṣantasya sdhvoḥ"),
    ("bhaṣ", "bh", 8, "8.2.37"),
    ("aś", "a", 9, "traditional list"),
    ("haś", "h", 9, "6.1.114 haśi ca"),
    ("vaś", "v", 9, "traditional list"),
    ("jhaś", "jh", 9, "8.4.53 jhalāṁ jaś jhaśi"),
    ("jaś", "j", 9, "8.2.39 jhalāṁ jaśo 'nte; 8.4.53"),
    ("baś", "b", 9, "8.2.37"),
    ("chav", "ch", 10, "8.3.7 naś chavy apraśān"),
    ("yay", "y", 11, "8.4.58 anusvārasya yayi parasavarṇaḥ"),
    ("may", "m", 11, "8.3.33 mayo uño vo vā"),
    ("jhay", "jh", 11, "8.4.62 jhayo ho 'nyatarasyām"),
    ("khay", "kh", 11, "7.4.61 śarpūrvāḥ khayaḥ"),
    ("cay", "c", 11, "8.4.48 cayo dvitīyāḥ śari pauṣkarasādeḥ"),
    ("yar", "y", 12, "8.4.45 yaro 'nunāsike 'nunāsiko vā"),
    ("jhar", "jh", 12, "8.4.65 jharo jhari savarṇe"),
    ("khar", "kh", 12, "8.4.55 khari ca"),
    ("car", "c", 12, "8.4.54 abhyāse car ca"),
    ("śar", "ś", 12, "7.4.61 śarpūrvāḥ khayaḥ"),
    ("hal", "h", 13, "1.3.3 halantyam"),
    ("val", "v", 13, "6.1.66 lopo vyor vali"),
    ("ral", "r", 13, "1.2.26 ral o vyupadhād dhalādeḥ saṁś ca"),
    ("jhal", "jh", 13, "8.2.26 jhalo jhali"),
    ("śal", "ś", 13, "3.1.45 śala igupadhād aniṭaḥ kṣaḥ"),
]

TO_58 = {"ṛ": "R", "ḷ": "L"}  # theorum/58 spells ṛ ḷ as R L
LONG_58 = {"a": "A", "i": "I", "u": "U"}  # theorum/58 spells ā ī ū as A I U


def t1_maheshvara_interval_code() -> dict[str, Any]:
    sounds = sorted(set(TOKENS))
    markers = [m for _, m in MAHESHVARA]
    marker_count = len(markers)
    pairs = sum(sum(1 for k in range(len(TOKENS)) if SUTRA_OF_TOKEN[k] <= j) for j in range(len(MAHESHVARA)))
    all_sets: dict[frozenset[str], list[tuple[int, int]]] = {}
    for j in range(len(MAHESHVARA)):
        for k in range(len(TOKENS)):
            if SUTRA_OF_TOKEN[k] <= j:
                all_sets.setdefault(frozenset(TOKENS[i] for i in range(k, len(TOKENS)) if SUTRA_OF_TOKEN[i] <= j), []).append((k, j))
    coincident = [v for v in all_sets.values() if len(v) > 1]
    # every coincidence of sound SETS among the 305 position pairs involves the last sūtra (ha l), whose only
    # sound h is already present: marker r vs marker l from any initial at or before the first h, and y..l = hal
    coincidences_explained = all(any(j == 13 for _, j in v) for v in coincident)
    used_sets = {name: set(pratyahara(x, j)) for name, x, j, _ in USED}
    by_name: dict[str, list[frozenset[str]]] = {}
    for name, x, j, _ in USED:
        by_name.setdefault(name, []).append(frozenset(pratyahara(x, j)))
    ambiguous = sorted(n for n, ss in by_name.items() if len(set(ss)) > 1)
    ik = tuple(TO_58.get(s, s) for s in pratyahara("i", 1))
    ac = pratyahara("a", 3)
    # theorum/58's ten vowels = 1.1.69 savarṇa closure (long forms) of a i u, plus e o ai au, with ṛ ḷ omitted by 58
    savarna_closure = [s for s in ac if s not in ("ṛ", "ḷ")]
    for s in ("a", "i", "u"):
        savarna_closure.insert(savarna_closure.index(s) + 1, LONG_58[s])
    tokens_by_sutra = [len(sounds_) for sounds_, _ in MAHESHVARA]
    checks = {
        "forty_three_tokens_forty_two_sounds_h_twice": len(TOKENS) == 43 and len(sounds) == 42 and TOKENS.count("h") == 2,
        "fourteen_markers_nava_panca": marker_count == 14 == 9 + 5,
        "every_marker_is_a_consonant_1_3_3": all(m not in ac for m in markers),
        "pairs_initial_before_marker_305": pairs == 305,
        "set_coincidences_among_the_305_pairs_all_come_from_the_second_h": coincidences_explained and len(coincident) == 10 and pairs - len(all_sets) == 11,
        "ik_equals_theorum_58_IK": ik == tuple(IK),
        "theorum_58_vowels_are_savarna_closure_of_ac_minus_r_l": tuple(savarna_closure) == tuple(VOWELS),
        "all_42_used_pratyaharas_are_intervals_of_the_token_order": all(_is_interval(pratyahara(x, j)) for _, x, j, _ in USED),
        "only_ambiguous_name_is_an": ambiguous == ["aṇ"],
        "forty_one_distinct_names": len(by_name) == 41,
        "pratyahara_counts_sound_tokens_only_markers_elided_1_3_9": all(len(pratyahara(x, j)) == len(pratyahara_positions(x, j)) for _, x, j, _ in USED),
        "hal_is_every_consonant_once": set(used_sets["hal"]) == set(TOKENS) - set(ac) and len(pratyahara("h", 13)) == 34,
        "yar_is_hal_without_h": used_sets["yar"] == used_sets["hal"] - {"h"},
        "val_is_hal_without_y_and_contains_the_second_h": used_sets["val"] == used_sets["hal"] - {"y"} and pratyahara("v", 13)[-1] == "h",
    }
    return {
        "checks": checks,
        "token_order": TOKENS,
        "tokens_per_sutra": tokens_by_sutra,
        "markers": markers,
        "distinct_sound_sets_over_all_305_pairs": len(all_sets),
        "coincident_position_pairs": [[list(x) for x in v] for v in coincident],
        "used": [{"name": n, "initial": x, "marker_sutra": j, "use": u, "sounds": list(pratyahara(x, j))} for n, x, j, u in USED],
    }


def _is_interval(seq: tuple[str, ...]) -> bool:
    start = TOKENS.index(seq[0])
    return tuple(TOKENS[start : start + len(seq)]) == seq


# ---------------------------------------------------------------- T2 the repeated h is necessary
SIX = ["ac", "aṭ", "yaṇ", "yar", "val", "hal"]


def pratyahara_positions(initial: str, marker_sutra: int) -> list[int]:
    start = TOKENS.index(initial)
    return [k for k in range(len(TOKENS)) if k >= start and SUTRA_OF_TOKEN[k] <= marker_sutra]


FIRST_H, SECOND_H = TOKENS.index("h"), len(TOKENS) - 1


def _label(k: int, split_h: bool) -> str:
    if split_h and k == FIRST_H:
        return "h1"
    if split_h and k == SECOND_H:
        return "h2"
    return TOKENS[k]


def _six_sets(split_h: bool) -> dict[str, frozenset[str]]:
    return {name: frozenset(_label(k, split_h) for k in pratyahara_positions(x, j)) for name, x, j, _ in USED if name in SIX}


def _atoms(universe: list[str], sets: dict[str, frozenset[str]]) -> list[frozenset[str]]:
    key = {}
    for s in universe:
        key.setdefault(tuple(s in sets[n] for n in SIX), []).append(s)
    return [frozenset(v) for v in key.values()]


def _interval_order_exists(atoms: list[frozenset[str]], sets: dict[str, frozenset[str]]) -> bool:
    for order in itertools.permutations(range(len(atoms))):
        ok = True
        for name in SIX:
            member = [k for k, i in enumerate(order) if atoms[i] <= sets[name]]
            assert all(atoms[i] <= sets[name] or not (atoms[i] & sets[name]) for i in order)
            if member and member != list(range(member[0], member[-1] + 1)):
                ok = False
                break
        if ok:
            return True
    return False


def t2_repeated_h_is_necessary() -> dict[str, Any]:
    one_h = _six_sets(split_h=False)
    universe_one = sorted(set(TOKENS))
    atoms_one = _atoms(universe_one, one_h)
    # with the two h's distinguished
    two_h = _six_sets(split_h=True)
    universe_two = sorted((set(TOKENS) - {"h"}) | {"h1", "h2"})
    atoms_two = _atoms(universe_two, two_h)
    # the Māheśvara order itself realizes the six sets with two h positions
    order_two = [_label(k, True) for k in range(len(TOKENS))]
    realized = all(_contiguous(order_two, two_h[n]) for n in SIX)
    checks = {
        "six_sets_cover_the_atoms_singleton_h_y_l": {"h", "y", "l"} <= {next(iter(a)) for a in atoms_one if len(a) == 1},
        "membership_atoms_with_one_h": len(atoms_one) == 6,
        "NO_linear_order_with_one_h_makes_all_six_intervals": not _interval_order_exists(atoms_one, one_h),
        "with_two_h_positions_an_order_exists": _interval_order_exists(atoms_two, two_h),
        "the_maheshvara_order_realizes_the_six_sets": realized,
        "h1_in_at_and_hal_not_val__h2_in_val_and_hal_not_at": ("h1" in two_h["aṭ"] and "h1" in two_h["hal"] and "h1" not in two_h["val"] and "h2" in two_h["val"] and "h2" in two_h["hal"] and "h2" not in two_h["aṭ"]),
    }
    return {"checks": checks, "atoms_one_h": [sorted(a) for a in atoms_one], "orders_searched_one_h": 720}


def _contiguous(order: list[str], subset: frozenset[str]) -> bool:
    pos = sorted(order.index(s) for s in subset)
    return pos == list(range(pos[0], pos[-1] + 1))


# ---------------------------------------------------------------- T3 Spanda turn group
def _exp_jet(D):
    n = len(D)
    u = [zeros(n, n), D] + [zeros(n, n) for _ in range(DEPTH - 1)]
    acc = j_const(eye(n))
    power = j_const(eye(n))
    fact = 1
    for k in range(1, DEPTH + 1):
        power = j_mul(power, u)
        fact *= k
        acc = j_add(acc, j_scale(Fraction(1, fact), power))
    return acc


def t3_spanda_turn_group() -> dict[str, Any]:
    R2, R3, R4 = star(R, R), star(star(R, R), R), star(star(R, R), star(R, R))
    minus_I = m_scale(Fraction(-1), I2)
    group = [I2, R, R2, R3]
    closed = all(star(a, b) in group for a in group for b in group)
    inverses = all(any(star(a, b) == I2 for b in group) for a in group)
    psi1 = mat([[sc(1)], [sc(0)]])
    orbit = [psi1]
    for _ in range(3):
        orbit.append(star(R, orbit[-1]))
    distinct = len({tuple(tuple(row) for row in v) for v in orbit}) == 4
    zero_turn = sum(1 for v in orbit if v[1][0] == sc(0))  # states with zero companion (turn) channel
    # Spanda 1.2 unobstructed: Exp(tD) Exp(-tD) = I in jets, for D = omega R and for the nilpotent control
    unobstructed = {}
    for label, D in (("omega_R", m_scale(Fraction(3, 2), R)), ("nilpotent_control", mat([[0, sc(0, 1)], [0, 0]]))):
        e, e_minus = _exp_jet(D), _exp_jet(m_scale(Fraction(-1), D))
        prod = j_mul(e, e_minus)
        unobstructed[label] = prod[0] == I2 and all(is_zero(prod[k]) for k in range(1, DEPTH + 1))
    # lopa (zero map on the marker sector, identity on the visible sector; theorum/56 B2) is obstructed: no right inverse
    P = mat([[1, 0], [0, 0]])
    no_right_inverse = all(star(P, X)[1][0] == sc(0) and star(P, X)[1][1] == sc(0) for X in (I2, R, mat([[sc(2, 3), sc(5)], [sc(7, 1), sc(0, 4)]])))
    checks = {
        "R_is_the_odd_generator_anti_self_dagger": is_anti_self_dagger(R),
        "R_squared_is_minus_I_pralaya": R2 == minus_I,
        "R_fourth_is_I_udaya": R4 == I2 and R != I2 and R2 != I2 and R3 != I2,
        "nimesha_is_R_cubed_equals_native_dagger_of_R": R3 == dagger(R),
        "unmesha_nimesha_are_mutual_inverses": star(R, dagger(R)) == I2 and star(dagger(R), R) == I2,
        "shakti_cakra_is_a_closed_group_of_order_four": closed and inverses and len({tuple(tuple(r) for r in g) for g in group}) == 4,
        "orbit_of_seed_has_four_states": distinct,
        "exactly_two_orbit_states_have_zero_turn_channel": zero_turn == 2,
        "exp_tD_exp_minus_tD_is_I_in_jets_omega_R": unobstructed["omega_R"],
        "exp_tD_exp_minus_tD_is_I_in_jets_nilpotent_control": unobstructed["nilpotent_control"],
        "lopa_projector_has_no_right_inverse_second_row_zero": no_right_inverse and is_zero(m_sub(star(P, P), P)),
    }
    return {"checks": checks}


# ---------------------------------------------------------------- T4 Pratyabhijñā recognition defect
Arrow = tuple[int, int]  # commutative base: one object, arrows (p, q) under addition


def omega_bilinear(B, b: Arrow, a: Arrow) -> Fraction:
    return sum(Fraction(B[i][k]) * b[i] * a[k] for i in range(2) for k in range(2))


def compose(b: Arrow, a: Arrow) -> Arrow:
    return (b[0] + a[0], b[1] + a[1])


def lifted_star(omega, nb, mb_):
    (n, b), (m, a) = nb, mb_
    return (n + m + omega(b, a), compose(b, a))


def path_memory(omega, path: list[Arrow]) -> tuple[Fraction, Arrow]:
    acc = (Fraction(0), (0, 0))
    for a in path:  # a_1 first, then a_2, ...
        acc = lifted_star(omega, (Fraction(0), a), acc)
    return acc


def t4_recognition_defect() -> dict[str, Any]:
    arrows = [(p, q) for p in range(3) for q in range(3)]
    B_turn = ((0, 0), (1, 0))  # omega((p',q'),(p,q)) = q' p : the turn cocycle
    B_sym = ((1, 2), (2, 1))  # a symmetric bilinear cocycle
    B_gen = ((1, 3), (-2, 2))  # a generic one
    cocycle_ok = all(
        omega_bilinear(B, c, compose(b, a)) + omega_bilinear(B, b, a) == omega_bilinear(B, compose(c, b), a) + omega_bilinear(B, c, b)
        for B in (B_turn, B_sym, B_gen)
        for a in arrows
        for b in arrows
        for c in arrows
    )
    normalized = all(omega_bilinear(B, (0, 0), a) == 0 == omega_bilinear(B, a, (0, 0)) for B in (B_turn, B_sym, B_gen) for a in arrows)
    # parenthesization independence (MR-03 Prop 5.1) on the lift: left fold = right fold
    assoc = True
    for B in (B_turn, B_gen):
        om = lambda b, a, B=B: omega_bilinear(B, b, a)
        for a, b, c in itertools.product(arrows[:4], repeat=3):
            left = lifted_star(om, (Fraction(0), c), lifted_star(om, (Fraction(0), b), (Fraction(0), a)))
            right = lifted_star(om, lifted_star(om, (Fraction(0), c), (Fraction(0), b)), (Fraction(0), a))
            assoc &= left == right
    # recognition defect between reorderings of one multiset depends only on the antisymmetric part
    gens = [(1, 0), (0, 1), (1, 1), (2, 0)]
    odd_only = True
    sym_blind = True
    witness_xy_yx = None
    for size in (2, 3, 4):
        for multiset in itertools.combinations_with_replacement(gens, size):
            perms = {p for p in itertools.permutations(multiset)}
            for B in (B_turn, B_sym, B_gen):
                S = tuple(tuple(Fraction(B[i][k] + B[k][i], 2) for k in range(2)) for i in range(2))
                A = tuple(tuple(Fraction(B[i][k] - B[k][i], 2) for k in range(2)) for i in range(2))
                mem = {p: path_memory(lambda b, a: omega_bilinear(B, b, a), list(p)) for p in perms}
                memS = {p: path_memory(lambda b, a: omega_bilinear(S, b, a), list(p)) for p in perms}
                memA = {p: path_memory(lambda b, a: omega_bilinear(A, b, a), list(p)) for p in perms}
                comps = {mem[p][1] for p in perms}
                assert len(comps) == 1  # same composite for every ordering (commutative base)
                for g, e in itertools.combinations(sorted(perms), 2):
                    dB = mem[g][0] - mem[e][0]
                    sym_blind &= memS[g][0] - memS[e][0] == 0
                    odd_only &= dB == memA[g][0] - memA[e][0]
    # explicit MR-03 Theorem 6.2 witness with the turn cocycle: xy vs yx
    om_turn = lambda b, a: omega_bilinear(B_turn, b, a)
    xy, yx = path_memory(om_turn, [(1, 0), (0, 1)]), path_memory(om_turn, [(0, 1), (1, 0)])
    witness_xy_yx = {"xy": [str(xy[0]), list(xy[1])], "yx": [str(yx[0]), list(yx[1])]}
    turn_distinguishes = xy[1] == yx[1] and xy[0] - yx[0] == 1
    # MR-03 §9 calibration omega(b,a) = b a on the integer monoid is symmetric: blind to reorderings
    om_int = lambda b, a: Fraction(b[0] * a[0])
    int_blind = all(
        len({path_memory(om_int, list(p))[0] for p in itertools.permutations(ms)}) == 1
        for size in (2, 3, 4)
        for ms in itertools.combinations_with_replacement([(1, 0), (2, 0), (3, 0)], size)
    )
    # coboundary gauge: omega' = omega + alpha(b∘a) − alpha(b) − alpha(a); same multiset ⇒ defect invariant
    alpha_table = {a: Fraction((a[0] * 7 + a[1] * 3) % 5 - 2) for a in [(p, q) for p in range(9) for q in range(9)]}
    alpha_table[(0, 0)] = Fraction(0)  # normalized 1-cochain (MR-03 §8): alpha(id) = 0
    alpha = lambda a: alpha_table[a]

    def om_gauged(b, a, B):
        return omega_bilinear(B, b, a) + alpha(compose(b, a)) - alpha(b) - alpha(a)

    gauge_invariant = True
    for size in (2, 3, 4):
        for ms in itertools.combinations_with_replacement(gens, size):
            perms = sorted({p for p in itertools.permutations(ms)})
            for B in (B_turn, B_gen):
                d0 = [path_memory(lambda b, a: omega_bilinear(B, b, a), list(p))[0] for p in perms]
                d1 = [path_memory(lambda b, a: om_gauged(b, a, B), list(p))[0] for p in perms]
                gauge_invariant &= all(d0[i] - d0[k] == d1[i] - d1[k] for i in range(len(perms)) for k in range(len(perms)))
    # different decompositions of one composite: the defect shifts by the gauge sums (obligation, recorded)
    g1, g2 = [(1, 0), (1, 0)], [(2, 0)]
    d_before = path_memory(lambda b, a: omega_bilinear(B_gen, b, a), g1)[0] - path_memory(lambda b, a: omega_bilinear(B_gen, b, a), g2)[0]
    d_after = path_memory(lambda b, a: om_gauged(b, a, B_gen), g1)[0] - path_memory(lambda b, a: om_gauged(b, a, B_gen), g2)[0]
    predicted_shift = (alpha((2, 0)) - 2 * alpha((1, 0))) - 0  # gamma_1 gauge sum minus gamma_2 gauge sum
    checks = {
        "bilinear_omega_satisfies_the_cocycle_identity_exhaustively": cocycle_ok,
        "bilinear_omega_is_normalized": normalized,
        "lifted_composition_is_associative_MR03_3_1": assoc,
        "symmetric_part_is_recognition_blind_on_reorderings": sym_blind,
        "defect_between_reorderings_equals_the_antisymmetric_turn_part": odd_only,
        "turn_cocycle_distinguishes_xy_from_yx_same_composite_MR03_6_2": turn_distinguishes,
        "MR03_section_9_integer_calibration_is_blind_to_reorderings": int_blind,
        "coboundary_gauge_leaves_the_defect_invariant_for_equal_multisets": gauge_invariant,
        "different_decompositions_shift_by_the_gauge_sums_as_predicted": d_after - d_before == predicted_shift and predicted_shift != 0,
    }
    return {"checks": checks, "witness_xy_yx": witness_xy_yx, "gauge_shift_example": {"before": str(d_before), "after": str(d_after), "predicted_shift": str(predicted_shift)}}


# ---------------------------------------------------------------- certificate
def build_certificate() -> dict[str, Any]:
    packets = {
        "t1_maheshvara_interval_code": t1_maheshvara_interval_code(),
        "t2_repeated_h_is_necessary": t2_repeated_h_is_necessary(),
        "t3_spanda_turn_group": t3_spanda_turn_group(),
        "t4_pratyabhijna_recognition_defect": t4_recognition_defect(),
    }
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_SHAIVA_SOURCES_NATIVIZED_CANDIDATE" if all(checks.values()) else "FAIL_SHAIVA_SOURCES_NATIVIZED_CANDIDATE"
    return {
        "schema": "rkf.shaiva_sources_nativized_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "Māheśvara interval code: 1.1.71 on the fourteen sūtras yields every traditional Aṣṭādhyāyī pratyāhāra as an interval of the 43-token order (two h positions); ik = theorum/58's IK; 58's ten vowels = 1.1.69 savarṇa closure of ac minus the ṛ ḷ that 58 itself omits; 305 (initial, later marker) pairs; aṇ is the only ambiguous name; markers (1.3.3 its, elided by 1.3.9) are never members — recognized initial + memory marker is the two-channel carrier of theorum/58",
                "The repeated h is necessary: with one h no linear order of the 42 sounds makes ac, aṭ, yaṇ, yar, val, hal all intervals (exhaustive over the six membership atoms, contraction lemma); with two h positions the Māheśvara order does",
                "Spanda turn group: the EMK odd generator R generates {I, R, -I, -R} of order exactly four, nimeṣa = R³ = R† (native dagger), R R† = I; the seed orbit has four states, exactly two with zero turn channel; Exp(tD)Exp(-tD) = I in jets for D = ωR and for the nilpotent control, while the 1.3.9 lopa projector has no right inverse",
                "Pratyabhijñā recognition defect (MR-03 extension): on a commutative base with a bilinear cocycle, the defect between reorderings of one arrow multiset depends only on the antisymmetric (turn) part, the symmetric part is recognition-blind, the defect is coboundary-gauge invariant for equal multisets; MR-03 §9's ω = ba is blind, the turn cocycle q'p gives δ(xy, yx) = 1 with equal composite",
            ],
            "NOT_claimed": [
                "Marker-count minimality of the fourteen sūtras (published classical theorem; not re-derived here)",
                "Any identification of breath, deity, ontology, or of Ω / π / δ with the five acts of Pratyabhijñā-hṛdaya 11 beyond the vocabulary recorded in the note",
                "Recognition across different elementary decompositions of one composite without a fixed memory gauge (recorded obligation)",
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
