from __future__ import annotations

"""Exact certificate (theorum/83): THE ŚIKṢĀ VEDĀṄGA — the Pāṇinīya Śikṣā quoted,
and theorum/79's manner rows and theorum/81's sthāna / prayatna table derived
from its verses instead of declared.

Quoted verses (Pāṇinīya Śikṣā, 60-verse Yajus recension; two independent
printed texts agree on every verse used):

  3  triṣaṣṭiś catuḥṣaṣṭir vā varṇāḥ sambhavato matāḥ /
     prākṛte saṁskṛte cāpi svayaṁ proktāḥ svayambhuvā
  4  svarā viṁśatir ekaś ca sparśānāṁ pañcaviṁśatiḥ /
     yādayaś ca smṛtā hy aṣṭau catvāraś ca yamāḥ smṛtāḥ
  5  anusvāro visargaś ca ×k ×pau cāpi parāśritau /
     duḥspṛṣṭaś ceti vijñeyo ḷkāraḥ pluta eva ca
 11  udāttaś cānudāttaś ca svaritaś ca svarās trayaḥ /
     hrasvo dīrghaḥ pluta iti kālato niyamā aci
 13  aṣṭau sthānāni varṇānām uraḥ kaṇṭhaḥ śiras tathā /
     jihvāmūlaṁ ca dantāś ca nāsikoṣṭhau ca tālu ca
 17  kaṇṭhyāv ahāv icuyaśās tālavyā oṣṭhajāv upū /
     syur mūrdhanyā ṛṭuraṣā dantyā ḷtulasāḥ smṛtāḥ
 18  jihvāmūle tu kuḥ prokto dantyoṣṭhyo vaḥ smṛto budhaiḥ /
     e ai tu kaṇṭhatālavyā o au kaṇṭhoṣṭhajau smṛtau
 21  svarāṇām ūṣmaṇāṁ caiva vivṛtaṁ karaṇaṁ smṛtam /
     tebhyo 'pi vivṛtāv eṅau tābhyām aicau tathaiva ca
 38  aco 'spṛṣṭā yaṇas tv īṣan nemaspṛṣṭāḥ śalaḥ smṛtāḥ /
     śeṣāḥ spṛṣṭā halaḥ proktā nibodhānupradānataḥ
 39  ñamo 'nunāsikā nahro nādino hajhaṣaḥ smṛtāḥ /
     īṣannādā yaṇo jaś ca śvāsinas tu khaphādayaḥ
 40  īṣacchvāsāṁś caro vidyād ...

 T1  THE COUNT.  Verse 4's 21 + 25 + 8 + 4 = 58, verse 5's six additions,
     and verse 3's 63 / 64 are reproduced by enumeration on the carrier:
     21 vowels = {a i u ṛ} × {hrasva dīrgha pluta} + ḷ + {e ai o au} × {dīrgha
     pluta}; the 25 stops are theorum/79's grid; the eight yādi are
     theorum/78's tokens y r l v ś ṣ s h.
 T2  THE PLACE TABLE IS DERIVED.  Verses 13, 17, 18 give theorum/81's STHANA
     table on every sound except the ka-varga, which the Śikṣā puts at
     jihvāmūla (18) where the Siddhānta-kaumudī puts it at kaṇṭha; the
     1.1.9 savarṇa classes computed from the Śikṣā table equal theorum/81's
     classes exactly, so the difference is invisible to savarṇa.
 T3  THE MANNER ROWS ARE DERIVED.  Verses 39–40's anupradāna classes
     (anunāsika ñ m ṅ ṇ n; nādin h + jhaṣ; īṣannāda yaṇ + jaś; śvāsin
     kh ph …; īṣacchvāsa car) restricted to the 25 stops are exactly the
     five manner rows of theorum/79.
 T4  THE AI/AU GAP CLOSES; THE 1.1.10 VERDICT IS A READING.  Verse 21 grades
     openness: vowels and ūṣman vivṛta, eṅ (e, o) more open, aic (ai, au)
     more open still.  With this grade as the internal effort, e/ai and
     o/au separate from the text (theorum/81 had to declare a proportion
     attribute), and a vowel and an ūṣman of one place share the effort —
     so 1.1.10 is load-bearing (a–h, i–ś).  With verse 38's four contact
     grades instead (aspṛṣṭa / īṣat / nema / spṛṣṭa), the same classes
     result but 1.1.10 becomes redundant.  Both are computed; the Kāśikā's
     reading (vivṛta shared) is the one under which 1.1.10 does work.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_samjna_sound_layer import NASAL, STHANA as STHANA_81, VOWELS_IAST, savarna_classes as savarna_81
from proof_lab.shaiva_sources_nativized import TOKENS
from proof_lab.shaiva_sources_varga_crystal import MANNER, VARGAS

SOURCES = {
    "PŚ 3": "triṣaṣṭiś catuḥṣaṣṭir vā varṇāḥ sambhavato matāḥ / prākṛte saṁskṛte cāpi svayaṁ proktāḥ svayambhuvā",
    "PŚ 4": "svarā viṁśatir ekaś ca sparśānāṁ pañcaviṁśatiḥ / yādayaś ca smṛtā hy aṣṭau catvāraś ca yamāḥ smṛtāḥ",
    "PŚ 5": "anusvāro visargaś ca ×k ×pau cāpi parāśritau / duḥspṛṣṭaś ceti vijñeyo ḷkāraḥ pluta eva ca",
    "PŚ 11": "udāttaś cānudāttaś ca svaritaś ca svarās trayaḥ / hrasvo dīrghaḥ pluta iti kālato niyamā aci",
    "PŚ 13": "aṣṭau sthānāni varṇānām uraḥ kaṇṭhaḥ śiras tathā / jihvāmūlaṁ ca dantāś ca nāsikoṣṭhau ca tālu ca",
    "PŚ 17": "kaṇṭhyāv ahāv icuyaśās tālavyā oṣṭhajāv upū / syur mūrdhanyā ṛṭuraṣā dantyā ḷtulasāḥ smṛtāḥ",
    "PŚ 18": "jihvāmūle tu kuḥ prokto dantyoṣṭhyo vaḥ smṛto budhaiḥ / e ai tu kaṇṭhatālavyā o au kaṇṭhoṣṭhajau smṛtau",
    "PŚ 21": "svarāṇām ūṣmaṇāṁ caiva vivṛtaṁ karaṇaṁ smṛtam / tebhyo 'pi vivṛtāv eṅau tābhyām aicau tathaiva ca",
    "PŚ 38": "aco 'spṛṣṭā yaṇas tv īṣan nemaspṛṣṭāḥ śalaḥ smṛtāḥ / śeṣāḥ spṛṣṭā halaḥ proktā nibodhānupradānataḥ",
    "PŚ 39": "ñamo 'nunāsikā nahro nādino hajhaṣaḥ smṛtāḥ / īṣannādā yaṇo jaś ca śvāsinas tu khaphādayaḥ",
    "PŚ 40": "īṣacchvāsāṁś caro vidyād gor dhāmaitat pracakṣate",
    "Aṣṭādhyāyī 1.1.9": "tulyāsyaprayatnaṁ savarṇam", "Aṣṭādhyāyī 1.1.10": "nājjhalau", "Aṣṭādhyāyī 1.1.8": "mukhanāsikāvacano 'nunāsikaḥ",
}

STOPS = tuple(s for v in VARGAS.values() for s in v)
YADI = ("y", "r", "l", "v", "ś", "ṣ", "s", "h")           # verse 4: yādayaḥ aṣṭau
USMAN = ("ś", "ṣ", "s", "h")
YAN = ("y", "v", "r", "l")

# ---------------------------------------------------------------- T1 the count of verses 3–5
def t1_count() -> dict[str, Any]:
    base = ("a", "i", "u", "ṛ")
    vowels21 = [(v, k) for v in base for k in ("hrasva", "dīrgha", "pluta")] + [("ḷ", "hrasva")] + [(v, k) for v in ("e", "ai", "o", "au") for k in ("dīrgha", "pluta")]
    eight_places = ("uras", "kaṇṭha", "śiras", "jihvāmūla", "danta", "nāsikā", "oṣṭha", "tālu")
    n58 = len(vowels21) + len(STOPS) + len(YADI) + 4                                    # verse 4 (+ 4 yamas)
    additions5 = ("anusvāra", "visarga", "jihvāmūlīya", "upadhmānīya", "duḥspṛṣṭa-ḷ", "ḷ-pluta")   # verse 5
    checks = {
        "verse_4_twenty_one_vowels_by_kala_on_the_carrier": len(vowels21) == 21 and len(set(vowels21)) == 21,
        "verse_4_twenty_five_sparsa_are_theorum_79_grid": len(STOPS) == 25 and set(STOPS) == {s for r in MANNER.values() for s in r},
        "verse_4_eight_yadi_are_theorum_78_tokens": all(y in TOKENS for y in YADI) and len(YADI) == 8,
        "verse_4_total_58_with_four_yamas": n58 == 58,
        "verse_3_sixty_three_or_sixty_four_with_verse_5_additions": n58 + 5 == 63 and n58 + 6 == 64,
        "verse_13_eight_places": len(eight_places) == 8,
    }
    return {"checks": checks, "vowels_21": [f"{v}-{k}" for v, k in vowels21], "additions_verse_5": additions5, "eight_places": eight_places}


# ---------------------------------------------------------------- T2 the place table from verses 13, 17, 18
STHANA_SIKSA: dict[str, str] = {}
for s in ("a", "ā", "h"):
    STHANA_SIKSA[s] = "kaṇṭha"                                        # 17 kaṇṭhyāv ahau
for s in ("i", "ī") + VARGAS["ca"] + ("y", "ś"):
    STHANA_SIKSA[s] = "tālu"                                          # 17 icuyaśās tālavyāḥ
for s in ("u", "ū") + VARGAS["pa"]:
    STHANA_SIKSA[s] = "oṣṭha"                                         # 17 oṣṭhajāv upū
for s in ("ṛ", "ṝ") + VARGAS["ṭa"] + ("r", "ṣ"):
    STHANA_SIKSA[s] = "mūrdhan"                                       # 17 mūrdhanyā ṛṭuraṣāḥ
for s in ("ḷ", "ḹ") + VARGAS["ta"] + ("l", "s"):
    STHANA_SIKSA[s] = "danta"                                         # 17 dantyā ḷtulasāḥ
for s in VARGAS["ka"]:
    STHANA_SIKSA[s] = "jihvāmūla"                                     # 18 jihvāmūle tu kuḥ
STHANA_SIKSA.update({"v": "danta-oṣṭha", "e": "kaṇṭha-tālu", "ai": "kaṇṭha-tālu", "o": "kaṇṭha-oṣṭha", "au": "kaṇṭha-oṣṭha"})   # 18

# internal effort, two readings
def prayatna_karana(s: str) -> str:
    """Verse 21 (openness as karaṇa) with verse 38 for the contact consonants."""
    if s in ("e", "o"):
        return "vivṛta-2"                                             # tebhyo 'pi vivṛtāv eṅau
    if s in ("ai", "au"):
        return "vivṛta-3"                                             # tābhyām aicau
    if s in VOWELS_IAST or s in USMAN:
        return "vivṛta"                                               # svarāṇām ūṣmaṇāṁ caiva vivṛtam
    if s in YAN:
        return "īṣat-spṛṣṭa"                                          # 38 yaṇas tv īṣat
    return "spṛṣṭa"                                                   # 38 śeṣāḥ spṛṣṭā halaḥ


def prayatna_sparsa(s: str) -> str:
    """Verse 38's four contact grades alone (vowels aspṛṣṭa, yaṇ īṣat, śal nema, the rest spṛṣṭa), with verse 21's grades on eṅ/aic."""
    if s in ("e", "o"):
        return "aspṛṣṭa-2"
    if s in ("ai", "au"):
        return "aspṛṣṭa-3"
    if s in VOWELS_IAST:
        return "aspṛṣṭa"
    if s in YAN:
        return "īṣat-spṛṣṭa"
    if s in USMAN:
        return "nema-spṛṣṭa"
    return "spṛṣṭa"


def classes(sounds: tuple[str, ...], sthana: dict[str, str], prayatna, apply_1_1_10: bool) -> set[frozenset[str]]:
    out: dict[tuple, set[str]] = {}
    for s in sounds:
        out.setdefault((sthana[s], prayatna(s), (s in VOWELS_IAST) if apply_1_1_10 else None), set()).add(s)
    return {frozenset(v) for v in out.values()}


SOUNDS = VOWELS_IAST + tuple(dict.fromkeys(t for t in TOKENS if t not in VOWELS_IAST))


def t2_place_table() -> dict[str, Any]:
    diff = sorted(s for s in SOUNDS if STHANA_SIKSA[s] != STHANA_81[s])
    siksa = classes(SOUNDS, STHANA_SIKSA, prayatna_karana, True)
    t81 = set(savarna_81(SOUNDS, True))
    checks = {
        "siksa_table_covers_every_carrier_sound": all(s in STHANA_SIKSA for s in SOUNDS),
        "siksa_table_equals_theorum_81_except_ka_varga_at_jihvamula": diff == sorted(VARGAS["ka"]),
        "savarna_classes_from_siksa_table_equal_theorum_81_classes": siksa == t81,
        "ka_varga_is_a_1_1_9_class_under_both_tables": frozenset(VARGAS["ka"]) in siksa and frozenset(VARGAS["ka"]) in t81,
    }
    return {"checks": checks, "differences": diff, "classes": sorted(sorted(c) for c in siksa)}


# ---------------------------------------------------------------- T3 the manner rows from verses 39–40
def t3_manner_rows() -> dict[str, Any]:
    jhas = tuple(v[3] for v in VARGAS.values())       # jhaṣ = 4th of each varga (gh jh ḍh dh bh)
    jas = tuple(v[2] for v in VARGAS.values())        # jaś = 3rd (g j ḍ d b)
    kha = tuple(v[1] for v in VARGAS.values())        # khaphādayaḥ = 2nd (kh ch ṭh th ph)
    car = tuple(v[0] for v in VARGAS.values()) + ("ś", "ṣ", "s")   # car = 1st of each varga + ś ṣ s
    anupradana = {
        "anunāsika (39: ñamaḥ)": set(NASAL),
        "nādin (39: ha-jhaṣaḥ)": {"h"} | set(jhas),
        "īṣannāda (39: yaṇ, jaś)": set(YAN) | set(jas),
        "śvāsin (39: khaphādayaḥ)": set(kha),
        "īṣacchvāsa (40: car)": set(car),
    }
    on_stops = {k: frozenset(v & set(STOPS)) for k, v in anupradana.items()}
    rows79 = {k: frozenset(v) for k, v in MANNER.items()}
    expected = {"anunāsika (39: ñamaḥ)": "nasal", "nādin (39: ha-jhaṣaḥ)": "voiced_aspirate", "īṣannāda (39: yaṇ, jaś)": "voiced", "śvāsin (39: khaphādayaḥ)": "voiceless_aspirate", "īṣacchvāsa (40: car)": "voiceless"}
    all_sounds = set().union(*anupradana.values())
    checks = {
        "anupradana_classes_restricted_to_stops_are_exactly_theorum_79_manner_rows": all(on_stops[k] == rows79[expected[k]] for k in expected) and set(on_stops.values()) == set(rows79.values()),
        "anupradana_classes_are_disjoint": sum(len(v) for v in anupradana.values()) == len(all_sounds),
        "anupradana_covers_all_33_consonants": all_sounds == set(STOPS) | set(YADI),
        "verse_39_nasals_equal_1_1_8_NASAL_of_theorum_81": set(NASAL) == anupradana["anunāsika (39: ñamaḥ)"],
    }
    return {"checks": checks, "classes": {k: sorted(v) for k, v in anupradana.items()}}


# ---------------------------------------------------------------- T4 the ai/au gap and the 1.1.10 verdict under two readings
def t4_openness_and_1_1_10() -> dict[str, Any]:
    k_with = classes(SOUNDS, STHANA_SIKSA, prayatna_karana, True)
    k_without = classes(SOUNDS, STHANA_SIKSA, prayatna_karana, False)
    s_with = classes(SOUNDS, STHANA_SIKSA, prayatna_sparsa, True)
    s_without = classes(SOUNDS, STHANA_SIKSA, prayatna_sparsa, False)
    singles = all(frozenset({x}) in k_with for x in ("e", "ai", "o", "au")) and all(frozenset({x}) in s_with for x in ("e", "ai", "o", "au"))
    checks = {
        "verse_21_grades_separate_e_ai_and_o_au_without_a_declared_attribute": singles and all((STHANA_SIKSA[a] == STHANA_SIKSA[b]) for a, b in (("e", "ai"), ("o", "au"))),
        "karana_reading_vowels_and_usman_share_vivrta_so_1_1_10_is_load_bearing": k_with != k_without and any({"a", "h"} <= c for c in k_without) and any({"i", "ś"} <= c for c in k_without),
        "sparsa_reading_verse_38_makes_1_1_10_redundant": s_with == s_without,
        "both_readings_give_the_same_classes_with_1_1_10": k_with == s_with,
    }
    return {"checks": checks, "karana_without_1_1_10_merged": sorted(sorted(c) for c in k_without if len(c) > 1 and any(x in VOWELS_IAST for x in c) and any(x not in VOWELS_IAST for x in c))}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_count": t1_count(), "t2_place_table": t2_place_table(), "t3_manner_rows": t3_manner_rows(), "t4_openness_and_1_1_10": t4_openness_and_1_1_10()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_PANINIYA_SIKSHA_SOURCES_CANDIDATE" if all(checks.values()) else "FAIL_PANINIYA_SIKSHA_SOURCES_CANDIDATE"
    return {
        "schema": "rkf.paniniya_siksha_sources_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "verses 3–5 counts (21 + 25 + 8 + 4 = 58; 63 / 64) reproduced by enumeration on the carrier",
                "verses 13, 17, 18 give theorum/81's STHANA table except ka-varga (jihvāmūla vs kaṇṭha); the 1.1.9 classes are identical",
                "verses 39–40 anupradāna classes restricted to the 25 stops are exactly theorum/79's five manner rows; verse 39 nasals = theorum/81's 1.1.8 set",
                "verse 21's openness grades separate e/ai and o/au from the text; under the karaṇa reading 1.1.10 is load-bearing (a–h, i–ś), under verse 38's contact reading it is redundant; the classes with 1.1.10 coincide",
            ],
            "NOT_claimed": [
                "yamas, anusvāra, visarga, jihvāmūlīya, upadhmānīya, duḥspṛṣṭa ḷ and pluta are counted, not carried",
                "accent (udātta / anudātta / svarita, verse 11) and mātrā durations (verses 19–20) are cited, not modelled",
                "which prayatna reading Pāṇini intended is not decided here; both are computed and the Kāśikā's is named",
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
