from __future__ import annotations

"""Exact certificate (theorum/85): THE NIRUKTA VEDĀṄGA — "nāmāny ākhyātajāni"
computed: from one dhātu, the nāma (kta + sup, 22 forms) and the ākhyāta
(śap + tiṅ, 9 forms) on the pinned carriers of theorum/82, 63 and 64; Yāska's
four padajātis as a partition of the computed padas.

Quoted sources:

 Nirukta 1.12   tatra nāmāny ākhyātajānīti śākaṭāyano nairuktasamayaś ca /
                na sarvāṇīti gārgyo vaiyākaraṇānāṁ caike
                (verified against a printed citation in this session)
 Nirukta 1.1    tad yāny etāni catvāri padajātāni nāmākhyāte copasarganipātāś ca
                bhāvapradhānam ākhyātam / sattvapradhānāni nāmāni
                (standard printed text; cited for the four classes only)

 Aṣṭādhyāyī
 3.1.91  dhātoḥ                      (adhikāra) after a dhātu
 3.1.93  kṛd atiṅ                    an affix other than tiṅ (after a dhātu) is kṛt
 1.1.26  ktaktavatū niṣṭhā           kta and ktavatu are niṣṭhā
 3.2.102 niṣṭhā                      (bhūte) niṣṭhā in the past
 1.2.46  kṛttaddhitasamāsāś ca       kṛt-, taddhita-ending forms and compounds are prātipadika
 4.1.1   ṅyāpprātipadikāt            (adhikāra) after a stem ending in ṅī, āp, or a prātipadika
 4.1.2   svaujasamauṭchaṣṭābhyāmbhis… the sup affixes
 1.4.14  suptiṅantaṁ padam           what ends in sup or tiṅ is a pada
 6.4.37  anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti
                                     nasal-final roots of the list lose the nasal before a jhal-initial kit / ṅit affix
 7.2.10  ekāca upadeśe 'nudāttāt     no iṭ after a monosyllabic root taught anudātta (the aniṭ roots)
 1.4.57  cādayo 'sattve ; 1.4.58 prādayaḥ ; 1.4.59 upasargāḥ kriyāyoge    nipāta and upasarga

 T1  NĀMA FROM DHĀTU.  gamḷ~, bhū, ḍukṛñ (theorum/82 its) + kta (1.3.8: ta,
     kit) with 6.4.37 (gam → ga) and 7.2.10 (no iṭ) give the prātipadikas
     gata, bhūta, kṛta (1.2.46); theorum/63's pinned sup ladder derives all
     22 forms of each — 66 forms — equal to the rāma paradigm with the stem
     exchanged and the 8.4.2 ṇatva absent (the t of the stem intervenes).
 T2  ĀKHYĀTA FROM THE SAME DHĀTU.  theorum/64's pinned laṭ derivation gives
     gacchati … gacchāmaḥ and bhavati … bhavāmaḥ from the same roots.
 T3  THE PADAJĀTI PARTITION.  Every computed form is a pada by 1.4.14; the
     sup-anta ones are nāma, the tiṅ-anta ones ākhyāta; the two sets are
     disjoint and jointly exhaust the computed padas; upasarga (1.4.58, 22
     items) and nipāta (1.4.57) are cited lists, not derived.
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from proof_lab.paninian_it_samjna_compiled import its
from proof_lab.sup_vibhakti_resolver_ladder import ORACLE as ORACLE63, RULES as RULES63, SUP, derive as derive63, paradigm_domains, st as st63, surface as surface63
from proof_lab import sup_vibhakti_resolver_ladder as T63
from proof_lab.ting_lat_parasmaipada import ORACLE as ORACLE64, RULES as RULES64, TING, derive as derive64, grammar_wide_domains, inputs as inputs64, st as st64, surface as surface64

SOURCES = {
    "Nirukta 1.12": "tatra nāmāny ākhyātajānīti śākaṭāyano nairuktasamayaś ca / na sarvāṇīti gārgyo vaiyākaraṇānāṁ caike",
    "Nirukta 1.1": "tad yāny etāni catvāri padajātāni nāmākhyāte copasarganipātāś ca ; bhāvapradhānam ākhyātam / sattvapradhānāni nāmāni",
    "3.1.91": "dhātoḥ", "3.1.93": "kṛd atiṅ", "1.1.26": "ktaktavatū niṣṭhā", "3.2.102": "niṣṭhā", "1.2.46": "kṛttaddhitasamāsāś ca",
    "4.1.1": "ṅyāpprātipadikāt", "4.1.2": "svaujasamauṭchaṣṭābhyāmbhisṅebhyāmbhyasṅasibhyāmbhyasṅasosāmṅyossup", "1.4.14": "suptiṅantaṁ padam",
    "6.4.37": "anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti", "7.2.10": "ekāca upadeśe 'nudāttāt",
    "1.4.57": "cādayo 'sattve", "1.4.58": "prādayaḥ", "1.4.59": "upasargāḥ kriyāyoge",
}

IAST_TO_CODE = {"ā": "A", "ī": "I", "ū": "U", "ṛ": "R", "ḷ": "L", "ś": "S", "ṣ": "z", "ṇ": "N", "ñ": "J", "ṅ": "G", "ṭ": "T", "ḍ": "D"}
ROOTS = {"gam": "gamḷ~", "bhū": "bhū", "kṛ": "ḍukṛñ"}           # upadeśa forms (Dhātupāṭha)
ANUDATTOPADESA_NASAL = ("gam", "yam", "ram", "nam", "van", "tan", "man", "han")   # 6.4.37's list (the anudātta-taught nasal-final roots; cited)
ANIT = ("gam", "bhū", "kṛ")                                       # 7.2.10: monosyllabic, taught anudātta → no iṭ (declared from the Dhātupāṭha accent)
JHAL_INITIAL = {"t", "th", "d", "dh", "k", "kh", "g", "gh", "c", "ch", "j", "jh", "ṭ", "ṭh", "ḍ", "ḍh", "p", "ph", "b", "bh", "ś", "ṣ", "s", "h"}
UPASARGAS_1_4_58 = ("pra", "parā", "apa", "sam", "anu", "ava", "nis", "nir", "dus", "dur", "vi", "āṅ", "ni", "adhi", "api", "ati", "su", "ud", "abhi", "prati", "pari", "upa")


def code(sounds: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(IAST_TO_CODE.get(s, s) for s in sounds)


def kta_pratipadika(root: str) -> dict[str, Any]:
    """dhātu (theorum/82 its) + kta (1.3.8 k it → ta, kit) → prātipadika (1.2.46), with 6.4.37 and 7.2.10."""
    dh = its(ROOTS[root], "dhatu")["remaining_sounds"]
    aff = its("kta", "pratyaya")
    body = aff["remaining_sounds"]
    kit = "k" in aff["its"]
    steps = [f"{ROOTS[root]} → {''.join(dh)} (1.3.2/1.3.3/1.3.5/1.3.9)", f"kta → {''.join(body)}, kit (1.3.8, 1.3.9)"]
    stem = dh
    if root in ANIT:
        steps.append("no iṭ (7.2.10)")
    if root in ANUDATTOPADESA_NASAL and stem[-1] in ("m", "n") and body[0] in JHAL_INITIAL and kit:
        stem = stem[:-1]
        steps.append(f"nasal lost before jhal-initial kit affix (6.4.37) → {''.join(stem)}")
    prat = stem + body
    steps.append(f"prātipadika {''.join(prat)} (1.2.46 kṛttaddhitasamāsāś ca; 3.1.93 kṛd atiṅ)")
    return {"pratipadika": "".join(prat), "sounds": prat, "steps": steps}


def t1_nama_from_dhatu() -> dict[str, Any]:
    dom = paradigm_domains(RULES63)
    out, ok_all, n = {}, True, 0
    for root in ROOTS:
        p = kta_pratipadika(root)
        stem = code(p["sounds"])
        stem_s = "".join(stem)
        forms = {}
        for c, aff, feats in SUP:
            aff = tuple(aff)
            fe = set(feats) | {"sup"}
            if c == "7p":
                aff = ("s", "u")
            W, _ = derive63(st63(stem, aff, fe), RULES63, dom=dom)
            got = surface63(W)
            exp = (stem_s[:-1] + ORACLE63[c][3:]).replace("N", "n")   # rāma paradigm with the stem exchanged; no 8.4.2 ṇatva (t intervenes)
            forms[c] = got
            ok_all &= got == exp
            n += 1
        out[root] = {"derivation": p["steps"], "pratipadika": p["pratipadika"], "forms": forms}
    checks = {
        "gata_bhuta_krta_are_the_kta_pratipadikas": [out[r]["pratipadika"] for r in ROOTS] == ["gata", "bhūta", "kṛta"],
        "6_4_37_fires_only_on_gam": ("6.4.37" in " ".join(out["gam"]["derivation"])) and all("6.4.37" not in " ".join(out[r]["derivation"]) for r in ("bhū", "kṛ")),
        "theorum_63_ladder_derives_all_66_sup_forms_equal_to_the_exchanged_rama_paradigm": ok_all and n == 66,
    }
    return {"checks": checks, **out}


def t2_akhyata_from_dhatu() -> dict[str, Any]:
    out, ok = {}, True
    dom = grammar_wide_domains(inputs64(), T63)   # theorum/64's own domain construction (grammar-wide with the nominal sector)
    for rn, root in (("gam", ("g", "a", "m")), ("bhU", ("b", "h", "U"))):
        forms = {}
        for c, ting in TING:
            W, _ = derive64(st64(root, ("S", "a", "p"), ting, {"tiN", "laT"}), RULES64, dom=dom)
            forms[c] = surface64(W)
            ok &= forms[c] == ORACLE64[rn][c]
        out[rn] = forms
    checks = {"theorum_64_derives_the_18_lat_forms_of_gam_and_bhu_from_the_same_roots": ok}
    return {"checks": checks, **out}


def t3_padajati_partition(t1: dict[str, Any], t2: dict[str, Any]) -> dict[str, Any]:
    nama = {f for r in ROOTS for f in t1[r]["forms"].values()}
    akhyata = {f for rn in ("gam", "bhU") for f in t2[rn].values()}
    checks = {
        "nama_sup_anta_and_akhyata_ting_anta_are_disjoint": not (nama & akhyata),
        "every_computed_form_is_a_pada_1_4_14_and_falls_in_exactly_one_class": len(nama) + len(akhyata) == len(nama | akhyata),
        "one_dhatu_gives_both_classes_gam_bhu": all(any(f.startswith(p) for f in nama) and any(f.startswith(q) for f in akhyata) for p, q in (("gat", "gacch"), ("bhUt", "bhav"))),
        "upasarga_list_1_4_58_has_22_items_cited_not_derived": len(UPASARGAS_1_4_58) == 22,
    }
    return {"checks": checks, "nama": sorted(nama), "akhyata": sorted(akhyata), "upasargas_1_4_58": UPASARGAS_1_4_58}


def build_certificate() -> dict[str, Any]:
    t1 = t1_nama_from_dhatu()
    t2 = t2_akhyata_from_dhatu()
    t3 = t3_padajati_partition(t1, t2)
    packets = {"t1_nama_from_dhatu": t1, "t2_akhyata_from_dhatu": t2, "t3_padajati_partition": t3}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_NIRUKTA_NAMA_AKHYATAJANI_CANDIDATE" if all(checks.values()) else "FAIL_NIRUKTA_NAMA_AKHYATAJANI_CANDIDATE"
    return {
        "schema": "rkf.nirukta_nama_akhyatajani_candidate.v1",
        "status": status,
        "sources": SOURCES,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                "from gamḷ~, bhū, ḍukṛñ: theorum/82 its + kta + 6.4.37 / 7.2.10 give gata, bhūta, kṛta; theorum/63's pinned ladder derives all 66 sup forms (= rāma paradigm with the stem exchanged, no ṇatva)",
                "theorum/64's pinned laṭ derivation gives the 18 ākhyāta forms of gam and bhū from the same roots",
                "the computed padas split exactly into nāma (sup-anta) and ākhyāta (tiṅ-anta), disjoint — Śākaṭāyana's thesis realized on three roots, not in general",
            ],
            "NOT_claimed": [
                "Gārgya's 'na sarvāṇi' (not all nouns) is not refuted: three roots and one kṛt affix are a sample",
                "6.4.37's root list and 7.2.10's aniṭ status are declared from the Dhātupāṭha, not derived (accent is not on the carrier)",
                "Nirukta 1.1's text is the standard printed one; only 1.12 was verified against a printed citation in this session",
                "upasarga (1.4.58) and nipāta (1.4.57) are cited lists; the six bhāvavikāras and nirvacana are not modelled",
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
