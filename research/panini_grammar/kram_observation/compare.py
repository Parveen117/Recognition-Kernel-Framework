"""Compare direct and shared evaluation of PG77's root-facing iṭ decision."""

import argparse
import hashlib
import json
import statistics
import sys
from pathlib import Path
from time import perf_counter_ns

STATE = Path(__file__).resolve().parents[1] / "kram_future" / "STATE.json"
STATE_SHA256 = "94a6ee65fb2042480823239444bbc86b45cfdd4ea4d49c514f830db6e0e847df"
CONTRACT = "PG77_ORDERED_CAUSE_RECIPIENT_CONTRACT"
POLICY = "PG77_BASIC_ROOT_DEPENDENT_A_IT_RESTRICTION_WITH_PG16_TASI_POLICY"
SLOTS = ("3sg", "3du", "3pl", "2sg", "2du", "2pl", "1sg", "1du", "1pl")
# PG77 H07/H08 use the PG16 and PG31 tuples on the published stem factors.
ENDINGS = {
    ("lrt", "P"): "ati ataḥ anti asi athaḥ atha āmi āvaḥ āmaḥ".split(),
    ("lrt", "A"): "ate ete ante ase ethe adhve e āvahe āmahe".split(),
    ("lut", "P"): "ā ārau āraḥ āsi āsthaḥ āstha āsmi āsvaḥ āsmaḥ".split(),
    ("lut", "A"): "ā ārau āraḥ āse āsāthe ādhve āhe āsvahe āsmahe".split(),
    ("lrng", "P"): "at atām an aḥ atam ata am āva āma".split(),
    ("lrng", "A"): "ata etām anta athāḥ ethām adhvam e āvahi āmahi".split(),
}
JUNCTION = {"": "a", "upa": "upā", "parā": "parā", "vi": "vya", "pra": "prā", "āṅ": "ā"}
FIRST_A = {
    "lrt": "ENDING_I_TO_E_THEN_6_1_97",
    "lut": "ENDING_I_TO_E_TAS_S_TO_H_7_4_52",
    "lrng": "RETAINED_ENDING_I_THEN_6_1_87",
}
THIRD = {"3sg": "DA", "3du": "RAU", "3pl": "RAS"}
TAS_ACTION = {"3du": "7.4.51_LOPA_BEFORE_R", "3pl": "7.4.51_LOPA_BEFORE_R",
              "2sg": "7.4.50_LOPA_BEFORE_S"}


def root_it(profile):
    """H02 on a pre-admitted PG77 profile and its declared sya/tās domain."""
    if profile["lexical_id"] != "1010545" or profile["root"] != "kram":
        raise ValueError("outside the PG77 lexical domain")
    cause = profile["pada"], profile["pada_cause"]
    if cause == ("P", "SELECTED_RESIDUAL_P_NO_ACTUAL_A"):
        return True
    if cause == ("A", "QUALIFIED_BASIC_KRAM_ROOT"):
        return False
    raise ValueError(f"unsupported pada licence or cause: {cause}")


def derive(name, profile, panel, lakara, context, slot, has_it):
    """Apply the supplied decision to this request's own affix, ending and path."""
    pada = profile["pada"]
    prefix = "".join(profile["upasarga"])
    is_tas = lakara == "lut"
    conditional = lakara == "lrng"
    first_a = pada == "A" and slot == "1sg"
    dental_dh = pada == "A" and slot == "2pl"
    substitute = THIRD.get(slot) if is_tas else None
    tas_action = None
    if is_tas:
        tas_action = TAS_ACTION.get(slot)
        if first_a:
            tas_action = "7.4.52_S_TO_H_BEFORE_E"
        elif dental_dh:
            tas_action = "8.2.25_SELECTED_SK_LOPA_BEFORE_DH"
    junction = None
    surface_prefix = "ā" if prefix == "āṅ" else prefix
    if conditional:
        surface_prefix = JUNCTION[prefix]
        if prefix:
            junction = "VI_I_TO_Y_BEFORE_AT_A_6_1_77" if prefix == "vi" else "SAVARNA_LONG_A_6_1_101"

    # Append the PG77 history in the packet's order. Only the Boolean above is shared.
    history = []
    lexical = {
        "original_teaching": "क्रमुँ", "removed_marker": "NASALIZED_U_1_3_2_9_RETAINED_IN_HISTORY",
        "lexical_valency_tag": "S", "lexical_valency_not_universal_frame": True,
    }
    history.append(("LEXICAL_TEACHING_AND_REMOVED_MARKER", lexical))
    frame = profile.get("dependent_frame", "RETAIN_ACTUAL_SUPPLIED_DEPENDENTS")
    history.append(("SEMANTIC_PREFIX_ROLE_CERTIFICATES", (name, profile["sense"], prefix, frame, profile["role_carrier"])))
    history.append(("PADA_AND_ACTUAL_ROOT_DEPENDENT_CAUSE", (pada, profile["pada_rule"], profile["pada_cause"])))
    history.append(("EXACT_FUTURE_OR_NONFULFILLMENT_CONTEXT", (lakara, context)))
    affix = {
        "future_affix": "tas" if is_tas else "sya", "future_affix_rule": "3.1.33",
        "future_affix_class": "ARDHADHATUKA", "present_vikarana": None, "root_dirgha": False,
        "tasi_i_policy": "UCCARANARTHA_BM_VAMANA" if is_tas else None,
        "root_it": "MANDATORY_7_2_35_SELECTED_P" if has_it else "PROHIBITED_7_2_36_ACTUAL_ROOT_DEPENDENT_A",
        "affix_it": "IT_OF_FOLLOWING_S_OR_T_INITIAL_FUTURE_AFFIX" if has_it else None,
        "it_protection": "1.1.6" if has_it else None, "krt_varttika_branch": False,
    }
    history.append(("FUTURE_AFFIX_AND_ROOT_IT_OWNER", affix))
    ending = ENDINGS[lakara, pada][SLOTS.index(slot)]
    ending_owners = {
        "ending_class": "SARVADHATUKA", "ending_aat": None, "ending_iit": None,
        "first_singular_ending_i": "ORIGINAL_A_IT_ENDING_NOT_ROOT_IT" if first_a else None,
        "first_singular_A_junction": FIRST_A[lakara] if first_a else None,
        "lut_third_substitute": substitute, "lut_third_pada_retained": bool(substitute),
        "lut_third_no_repeated_ti_e": bool(substitute) and pada == "A",
        "lut_ti_lopa": "6.4.143_AFTER_WHOLE_DA_AND_MARKER_DESIGNATION" if is_tas and slot == "3sg" else None,
        "lut_tas_s_action": tas_action, "second_plural_dh": "DENTAL" if dental_dh else None,
    }
    history.append(("ORIGINAL_ENDING_AND_SUBSTITUTE_TARGET", (pada, slot, ending_owners)))
    augment = {
        "initial_augment": "AT_AFTER_PREFIX_6_4_71" if conditional else None, "initial_aat": None,
        "prefix_augment_junction": junction,
        "prefix_at_intervention": "BM_1_3_17_AD_VYAVAYA_ADAPTER" if junction else None,
    }
    history.append(("AUGMENT_AND_PREFIX_JUNCTION", augment))
    if has_it:
        nasal = "M_RETAINED_BEFORE_IT"
        factor = "kramit" if is_tas else "kramiṣy"
    elif is_tas:
        nasal, factor = "LATE_DENTAL_N_BEFORE_T", "krant"
    else:
        nasal, factor = "ANUSVARA_BEFORE_NON_YAY_S", "kraṃsy"
    phonetics = {
        "sya_satva": "8.3.59_AFTER_IT" if has_it and not is_tas else None,
        "root_m_anusvara": None if has_it else "8.3.24_BEFORE_JHAL",
        "root_n_parasavarna": "8.4.58_BEFORE_T_NO_BACKWARD_NATVA_OR_N_LOPA" if is_tas and not has_it else None,
        "anusvara_retained": "S_NOT_YAY_8_4_58" if not is_tas and not has_it else None,
    }
    history.append(("ORDERED_NASAL_AND_SATVA_READOUT", phonetics))
    word = surface_prefix + factor + ending
    history.append(("WORD_OBSERVER_LAST", word))
    path = dict(history_label=f"{name}:{lakara}:{slot}:selected", reading=word, semantic_profile=name,
                source_policy=POLICY, root_grade="SHORT_A_NO_SIT_DIRGHA", root_it_present=has_it,
                nasal_readout=nasal, smriti_contract=CONTRACT)
    row = {
        "profile": name, "root": profile["root"], "lexical_id": profile["lexical_id"],
        "formation": "basic", "voice": "kartari", "pada": pada, "pada_rule": profile["pada_rule"],
        "pada_modality": profile["pada_modality"], "pada_cause": profile["pada_cause"],
        "lakara": lakara, "slot": slot, "panel": panel, "context": context,
        "upasarga": profile["upasarga"], "semantic_certificate": profile["sense"],
        "semantic_family": profile["semantic_family"], "controller": profile["controller"],
        "role_carrier": profile["role_carrier"], "dependent_frame": frame, "register": "CLASSICAL_NON_MANTRA",
        "prefix_evidence": "ACTUAL_KRIYAYOGA_REQUIRED" if prefix else "ABSENCE_CERTIFIED_NOT_MISSING",
        "readings": [word], "paths": [path], "new_position_credit": 1,
        "owners": lexical | affix | ending_owners | augment | phonetics,
    }
    return row, history


def evaluate(state, shared, decide=root_it):
    results = {}
    for panel in state["position_accounting"]["panels"]:
        name = panel["profile"]
        profile = state["contextual_profiles"][name]
        if shared:
            profile_it = decide(profile)
        for lakara in panel["lakaras"]:
            context = state["context_codes"][lakara]
            for slot in profile["slots"]:
                has_it = profile_it if shared else decide(profile)
                key = name, lakara, slot
                results[key] = derive(name, profile, panel["panel"], lakara, context, slot, has_it)
    return results


def compare(state):
    archived = {(r["profile"], r["lakara"], r["slot"]): r for r in state["position_accounting"]["forms"]}
    order = state["smriti_contracts"][CONTRACT]
    assert len(archived) == len(state["position_accounting"]["forms"]) == 171
    counts = {}
    for shared in (False, True):
        calls = 0

        def counted(profile):
            nonlocal calls
            calls += 1
            return root_it(profile)

        results = evaluate(state, shared, counted)
        assert results.keys() == archived.keys()
        for key, (row, history) in results.items():
            if row != archived[key]:
                fields = [k for k in row.keys() | archived[key].keys() if row.get(k) != archived[key].get(k)]
                raise ValueError(f"{key} differs from frozen row in {fields}")
            assert [stage for stage, _ in history] == order, key
        counts[shared] = calls
        if not shared:
            direct = results
    assert direct == results
    assert counts == {False: 171, True: 7}
    # Same spelling, different endings and temporal histories. Dropping the trace
    # or keying on the surface would lose a certified alternative analysis.
    future, future_history = results["PARA_EFFORT", "lrt", "1sg"]
    conditional, conditional_history = results["PARA_EFFORT", "lrng", "1sg"]
    assert future["readings"] == conditional["readings"] == ["parākraṃsye"]
    assert future_history != conditional_history
    assert future["owners"]["first_singular_A_junction"] == "ENDING_I_TO_E_THEN_6_1_97"
    assert conditional["owners"]["first_singular_A_junction"] == "RETAINED_ENDING_I_THEN_6_1_87"
    # Unsupported causes must never obtain an iṭ decision from pada alone.
    wrong_cause = dict(state["contextual_profiles"]["BARE_ORDINARY_A"], pada_cause="UNKNOWN")
    try:
        root_it(wrong_cause)
    except ValueError:
        pass
    else:
        raise AssertionError("admitted an unsupported cause")
    print("171 frozen rows, accepted readings, labelled paths and nine-stage histories match.")
    print("Root-facing iṭ evaluations: direct 171, shared 7.")


def benchmark(state):
    import platform

    rounds, batches = 24, 24
    samples = {False: [], True: []}
    for shared in (False, True):
        evaluate(state, shared)
    for index in range(rounds):
        for shared in ((False, True) if index % 2 == 0 else (True, False)):
            start = perf_counter_ns()
            for _ in range(batches):
                evaluate(state, shared)
            samples[shared].append((perf_counter_ns() - start) / (batches * 1_000_000))
    print(f"Python {platform.python_version()}, {platform.machine()}, {rounds} paired blocks x {batches} grids per mode")
    for mode, label in ((False, "direct"), (True, "shared")):
        times = samples[mode]
        low, _, high = statistics.quantiles(times, n=4, method="inclusive")
        print(f"{label}: median {statistics.median(times):.4f} ms/grid, IQR [{low:.4f}, {high:.4f}]")
    ratios = [a / b for a, b in zip(samples[False], samples[True])]
    print(f"Paired median direct/shared runtime ratio: {statistics.median(ratios):.4f}")


if __name__ == "__main__":
    assert sys.version_info[:2] == (3, 12), "Python 3.12 is required"
    if not __debug__:
        raise RuntimeError("Run without Python optimization so all checks execute")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark", action="store_true", help="also measure entire 171-cell evaluations")
    args = parser.parse_args()
    raw = STATE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != STATE_SHA256:
        raise ValueError("PG77 reference differs from the pinned edition")
    state = json.loads(raw)
    compare(state)
    if args.benchmark:
        benchmark(state)
