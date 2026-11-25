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
INPUTS_SHA256 = "780ee0263849d278d6de08c5ff8dc3ed61565882a61b170b36bfba2ee2f5078e"
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


def prefix_junction(prefix, lakara):
    junction = None
    surface_prefix = "ā" if prefix == "āṅ" else prefix
    if lakara == "lrng":
        surface_prefix = JUNCTION[prefix]
        if prefix:
            junction = "VI_I_TO_Y_BEFORE_AT_A_6_1_77" if prefix == "vi" else "SAVARNA_LONG_A_6_1_101"

    return surface_prefix, junction


def root_factor(has_it, is_tas):
    if has_it:
        nasal = "M_RETAINED_BEFORE_IT"
        factor = "kramit" if is_tas else "kramiṣy"
    elif is_tas:
        nasal, factor = "LATE_DENTAL_N_BEFORE_T", "krant"
    else:
        nasal, factor = "ANUSVARA_BEFORE_NON_YAY_S", "kraṃsy"
    return factor, nasal


def word_stem(prefix, lakara, has_it):
    surface_prefix, _ = prefix_junction(prefix, lakara)
    factor, _ = root_factor(has_it, lakara == "lut")
    return surface_prefix + factor


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
    surface_prefix, junction = prefix_junction(prefix, lakara)

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
    factor, nasal = root_factor(has_it, is_tas)
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


def selected_profiles(state, profile=None, lakara=None, slot=None):
    """Intersect the query with each panel's individually certified domain."""
    for panel in state["position_accounting"]["panels"]:
        name = panel["profile"]
        if profile is not None and profile != name:
            continue
        spec = state["contextual_profiles"][name]
        labels = panel["lakaras"]
        slots = spec["slots"]
        if lakara is not None:
            if lakara not in labels:
                continue
            labels = (lakara,)
        if slot is not None:
            if slot not in slots:
                continue
            slots = (slot,)
        yield panel, spec, labels, slots


def iter_results(state, shared=True, decide=root_it, **filters):
    for panel, spec, labels, slots in selected_profiles(state, **filters):
        name = panel["profile"]
        if shared:
            profile_it = decide(spec)
        for lakara in labels:
            context = state["context_codes"][lakara]
            for slot in slots:
                has_it = profile_it if shared else decide(spec)
                key = name, lakara, slot
                yield key, derive(name, spec, panel["panel"], lakara, context, slot, has_it)


def evaluate(state, shared, decide=root_it):
    """Materialize the full keyed grid for callers requesting random access."""
    return dict(iter_results(state, shared, decide))


def iter_words(state, make_stem=word_stem, **filters):
    """Terminal word projection; keys retain distinct grammatical requests."""
    for panel, spec, labels, slots in selected_profiles(state, **filters):
        has_it = root_it(spec)
        prefix = "".join(spec["upasarga"])
        for lakara in labels:
            stem = make_stem(prefix, lakara, has_it)
            endings = ENDINGS[lakara, spec["pada"]]
            for slot in slots:
                yield (panel["profile"], lakara, slot), stem + endings[SLOTS.index(slot)]


def query_inputs(state):
    """Select just the immutable declarations needed to evaluate PG77 queries."""
    panels = [{k: p[k] for k in ("panel", "profile", "lakaras")}
              for p in state["position_accounting"]["panels"]]
    labels = {label for panel in panels for label in panel["lakaras"]}
    return {
        "source_sha256": STATE_SHA256,
        "contextual_profiles": state["contextual_profiles"],
        "position_accounting": {"panels": panels},
        "context_codes": {k: v for k, v in state["context_codes"].items() if k in labels},
    }


def read_pinned(path, digest):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != digest:
        raise ValueError(f"{path.name} differs from the pinned edition")
    return json.loads(raw)


def compare(state, inputs=None):
    if inputs is None:
        inputs = query_inputs(state)
    assert inputs == query_inputs(state)
    forms = state["position_accounting"]["forms"]
    archived = {(r["profile"], r["lakara"], r["slot"]): r for r in forms}
    unseen = set(archived)
    assert len(unseen) == len(forms) == 171
    order = state["smriti_contracts"][CONTRACT]
    calls = {"direct": 0, "shared": 0, "stems": 0}

    def counted(mode):
        def decide(spec):
            calls[mode] += 1
            return root_it(spec)
        return decide

    def counted_stem(prefix, label, has_it):
        calls["stems"] += 1
        return word_stem(prefix, label, has_it)

    direct = iter_results(state, False, counted("direct"))
    shared = iter_results(inputs, True, counted("shared"))
    words = iter_words(inputs, counted_stem)
    for (key, reference), (shared_key, result), (word_key, word) in zip(direct, shared, words, strict=True):
        assert key == shared_key == word_key
        unseen.remove(key)
        assert result == reference, key
        row, history = result
        if row != archived[key]:
            fields = [k for k in row.keys() | archived[key].keys() if row.get(k) != archived[key].get(k)]
            raise ValueError(f"{key} differs from frozen row in {fields}")
        assert [stage for stage, _ in history] == order, key
        assert archived[key]["readings"] == [word], key
    assert not unseen
    assert calls == {"direct": 171, "shared": 7, "stems": 21}

    # Identical surfaces can have different futures and histories.
    example = {"profile": "PARA_EFFORT", "slot": "1sg"}
    selected = dict(iter_results(state, **example))
    simple = dict(iter_words(state, **example))
    assert len(simple) == len(selected) == 3
    future = ("PARA_EFFORT", "lrt", "1sg")
    conditional = ("PARA_EFFORT", "lrng", "1sg")
    assert simple[future] == simple[conditional] == "parākraṃsye"
    assert selected[future][1] != selected[conditional][1]
    assert selected[future][0]["owners"]["first_singular_A_junction"] == "ENDING_I_TO_E_THEN_6_1_97"
    assert selected[conditional][0]["owners"]["first_singular_A_junction"] == "RETAINED_ENDING_I_THEN_6_1_87"
    # Query restriction must not invent luminous-rise first-person cells.
    assert not list(iter_words(state, profile="A_JYOTIS_RISE", slot="1sg"))
    assert not list(iter_results(state, profile="A_JYOTIS_RISE", slot="1sg"))
    # A query selecting exactly one admitted cell needs one prefix/stem combination.
    calls["stems"] = 0
    example["lakara"] = "lrng"
    assert list(iter_words(state, counted_stem, **example)) == [(conditional, "parākraṃsye")]
    assert calls["stems"] == 1
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
    print("171 projected words match; 21 prefix/stem computations for the grid, one for the selected cell.")


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


def benchmark_queries(state):
    import gc
    import tracemalloc

    def full_words():
        return {key: row["readings"][0] for key, (row, _) in iter_results(state)}

    def projected_words():
        return dict(iter_words(state))

    assert full_words() == projected_words()
    samples = {full_words: [], projected_words: []}
    for index in range(24):
        modes = (full_words, projected_words) if index % 2 == 0 else (projected_words, full_words)
        for mode in modes:
            start = perf_counter_ns()
            for _ in range(24):
                mode()
            samples[mode].append((perf_counter_ns() - start) / 24_000_000)
    for mode in samples:
        print(f"{mode.__name__}: {statistics.median(samples[mode]):.4f} ms per keyed word grid (median)")

    forms = state["position_accounting"]["forms"]
    expected = {(r["profile"], r["lakara"], r["slot"]): r for r in forms}
    order = state["smriti_contracts"][CONTRACT]
    for mode in ("materialized", "streamed"):
        gc.collect()
        tracemalloc.start()
        try:
            if mode == "materialized":
                rows = evaluate(state, True).items()
            else:
                rows = iter_results(state)
            count = 0
            for key, (row, history) in rows:
                assert row == expected[key] and [tag for tag, _ in history] == order
                count += 1
            assert count == len(expected)
            peak = tracemalloc.get_traced_memory()[1]
        finally:
            tracemalloc.stop()
        del rows, row, history
        print(f"{mode}: {peak:,} peak traced Python bytes validating one complete history grid")


def query(state, args, parser):
    filters = dict(profile=args.profile, lakara=args.lakara, slot=args.slot)
    results = iter_words(state, **filters) if args.query == "words" else iter_results(state, **filters)
    found = False
    for (profile, lakara, slot), value in results:
        output = {"profile": profile, "lakara": lakara, "slot": slot}
        if args.query == "words":
            output["word"] = value
        else:
            output["row"], output["history"] = value
        print(json.dumps(output, ensure_ascii=False))
        found = True
    if not found:
        parser.error("no admitted PG77 cell matches the requested profile, lakara and slot")


if __name__ == "__main__":
    assert sys.version_info[:2] == (3, 12), "Python 3.12 is required"
    if not __debug__:
        raise RuntimeError("Run without Python optimization so all checks execute")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark", action="store_true", help="also measure entire 171-cell evaluations")
    inputs = read_pinned(Path(__file__).with_name("query_inputs.json"), INPUTS_SHA256)
    parser.add_argument("--query", choices=("words", "history"), help="emit one JSON record per admitted cell")
    parser.add_argument("--profile", choices=tuple(inputs["contextual_profiles"]))
    parser.add_argument("--lakara", choices=("lrt", "lut", "lrng"))
    parser.add_argument("--slot", choices=SLOTS)
    args = parser.parse_args()
    if args.query:
        if args.benchmark:
            parser.error("--benchmark and --query are separate operations")
        query(inputs, args, parser)
    else:
        if args.profile or args.lakara or args.slot:
            parser.error("--profile, --lakara and --slot select cells for --query")
        state = read_pinned(STATE, STATE_SHA256)
        compare(state, inputs)
        if args.benchmark:
            benchmark(state)
            benchmark_queries(state)
