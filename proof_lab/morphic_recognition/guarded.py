"""MR-06: exact finite guarded future equivalence and safe Lopa.

Partition refinement and pair-graph search are independent decision procedures.
Neither truncates the future at a chosen word length. Finite calibrations check
the implementation; the general finite-carrier proof lives in the theorem file.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from types import MappingProxyType
from typing import Hashable, Iterator, Mapping


def _labels(values: tuple[str, ...], name: str) -> tuple[str, ...]:
    result = tuple(values)
    if any(not isinstance(value, str) for value in result):
        raise ValueError(f"{name} must contain string labels")
    if len(set(result)) != len(result):
        raise ValueError(f"{name} contains duplicate labels")
    return result


def _hashable(value: Hashable) -> None:
    try:
        hash(value)
    except TypeError as error:
        raise ValueError("observations and retention labels must be hashable") from error
    if value != value:
        raise ValueError("observations and retention labels must be reflexive")


@dataclass(frozen=True)
class GuardedSystem:
    """Finite deterministic partial rules; a missing transition means disabled.

    State/action labels are strings. Observations use exact, hashable values
    with ordinary equivalence-relation equality (integers/strings/tuples are
    suitable). Inputs are copied and frozen so caller mutation cannot change
    a previously certified carrier.
    """

    states: tuple[str, ...]
    actions: tuple[str, ...]
    outputs: Mapping[str, Hashable]
    transitions: Mapping[tuple[str, str], str]

    def __post_init__(self) -> None:
        states = _labels(self.states, "states")
        actions = _labels(self.actions, "actions")
        if not states:
            raise ValueError("the finite carrier must be nonempty")
        outputs = dict(self.outputs)
        transitions = dict(self.transitions)
        if set(outputs) != set(states):
            raise ValueError("outputs must be defined exactly on the carrier")
        for output in outputs.values():
            _hashable(output)
        for key, target in transitions.items():
            if not isinstance(key, tuple) or len(key) != 2:
                raise ValueError("transition keys must be (state, action) pairs")
            source, action = key
            if source not in states or action not in actions or target not in states:
                raise ValueError("transition lies outside the declared carrier/alphabet")
        object.__setattr__(self, "states", states)
        object.__setattr__(self, "actions", actions)
        object.__setattr__(self, "outputs", MappingProxyType(outputs))
        object.__setattr__(self, "transitions", MappingProxyType(transitions))

    def enabled(self, state: str) -> tuple[str, ...]:
        if state not in self.outputs:
            raise ValueError("unknown state")
        return tuple(a for a in self.actions if (state, a) in self.transitions)


@dataclass(frozen=True)
class Partition:
    blocks: tuple[tuple[str, ...], ...]
    state_to_block: Mapping[str, int]
    strict_refinements: int


def _group(states: tuple[str, ...], signatures: Mapping[str, Hashable]) -> tuple[tuple[str, ...], ...]:
    groups: dict[Hashable, list[str]] = {}
    for state in states:
        groups.setdefault(signatures[state], []).append(state)
    return tuple(tuple(group) for group in groups.values())


def refine_partition(system: GuardedSystem) -> Partition:
    """Return the coarsest output/guard/successor-stable partition."""
    blocks = _group(system.states, {
        state: (system.outputs[state], system.enabled(state)) for state in system.states
    })
    strict_refinements = 0
    while True:
        classes = {state: i for i, block in enumerate(blocks) for state in block}
        signatures = {
            state: (classes[state], tuple(
                classes[system.transitions[state, action]]
                if (state, action) in system.transitions else -1
                for action in system.actions
            ))
            for state in system.states
        }
        refined = _group(system.states, signatures)
        if refined == blocks:
            return Partition(blocks, MappingProxyType(classes), strict_refinements)
        blocks = refined
        strict_refinements += 1


def distinguishing_word(system: GuardedSystem, left: str, right: str) -> tuple[str, ...] | None:
    """Shortest distinguishing word, or None after exhausting the pair graph.

    The empty tuple witnesses unequal current outputs. A word can instead
    witness that exactly one side permits the full word. Disabled successors
    are explicit terminal signals, never identity transitions.
    """
    if left not in system.outputs or right not in system.outputs:
        raise ValueError("unknown state")
    queue = deque([(left, right, ())])
    seen: set[tuple[str | None, str | None]] = {(left, right)}
    while queue:
        x, y, word = queue.popleft()
        if x is None or y is None:
            return word
        if system.outputs[x] != system.outputs[y]:
            return word
        for action in system.actions:
            u = system.transitions.get((x, action))
            v = system.transitions.get((y, action))
            if u is None and v is None:
                continue
            if (u, v) not in seen:
                seen.add((u, v))
                queue.append((u, v, word + (action,)))
    return None


def observe_word(system: GuardedSystem, state: str, word: tuple[str, ...]) -> tuple[bool, Hashable | None]:
    """Return (admissible, final observation), using an explicit boolean guard."""
    if state not in system.outputs:
        raise ValueError("unknown state")
    if any(action not in system.actions for action in word):
        raise ValueError("word contains an undeclared action")
    for action in word:
        successor = system.transitions.get((state, action))
        if successor is None:
            return False, None
        state = successor
    return True, system.outputs[state]


def minimal_quotient(system: GuardedSystem) -> tuple[GuardedSystem, Mapping[str, str]]:
    """Canonical behavioral quotient; all declared source states are represented."""
    partition = refine_partition(system)
    names = tuple(f"q{i}" for i in range(len(partition.blocks)))
    retained = {state: names[index] for state, index in partition.state_to_block.items()}
    outputs = {names[i]: system.outputs[block[0]] for i, block in enumerate(partition.blocks)}
    transitions = {}
    for i, block in enumerate(partition.blocks):
        representative = block[0]
        for action in system.enabled(representative):
            transitions[names[i], action] = retained[system.transitions[representative, action]]
    return GuardedSystem(names, system.actions, outputs, transitions), MappingProxyType(retained)


def _retention_labels(system: GuardedSystem, retained: Mapping[str, Hashable]) -> None:
    if set(retained) != set(system.states):
        raise ValueError("retention must be defined exactly on the carrier")
    for value in retained.values():
        _hashable(value)


def retention_is_faithful(system: GuardedSystem, retained: Mapping[str, Hashable]) -> bool:
    """Whether the retained record determines the canonical future class.

    This information criterion alone does NOT promise a deterministic update
    of arbitrary extra labels in the retained record; see the next function.
    """
    _retention_labels(system, retained)
    classes = refine_partition(system).state_to_block
    decoder: dict[Hashable, int] = {}
    for state in system.states:
        label = retained[state]
        if label in decoder and decoder[label] != classes[state]:
            return False
        decoder[label] = classes[state]
    return True


def retention_supports_updates(system: GuardedSystem, retained: Mapping[str, Hashable]) -> bool:
    """Whether output, guards AND next retained labels descend to the record."""
    _retention_labels(system, retained)
    records: dict[Hashable, Hashable] = {}
    for state in system.states:
        signature = (system.outputs[state], tuple(
            (True, retained[system.transitions[state, action]])
            if (state, action) in system.transitions else (False, None)
            for action in system.actions
        ))
        label = retained[state]
        if label in records and records[label] != signature:
            return False
        records[label] = signature
    return True


def systematic_systems() -> Iterator[GuardedSystem]:
    """All 1/2-state two-action and 3-state one-action partial binary-output systems.

    Exactly 8 + 324 + 512 = 844 labeled systems; no random seed or sampling.
    """
    for size, action_count in ((1, 2), (2, 2), (3, 1)):
        states = tuple(f"s{i}" for i in range(size))
        actions = tuple(f"a{i}" for i in range(action_count))
        slots = tuple(product(states, actions))
        for output_bits in product((0, 1), repeat=size):
            for targets in product((None,) + states, repeat=len(slots)):
                transitions = {slot: target for slot, target in zip(slots, targets) if target is not None}
                yield GuardedSystem(states, actions, dict(zip(states, output_bits)), transitions)


def verify_guarded_contract() -> dict:
    """Exact MR-06 calibration packet, suitable for the root certificate runner."""
    checks = []
    system_count = pair_count = equivalent_pairs = witness_count = transition_count = 0
    longest_witness = 0
    disagreement_count = invalid_witness_count = quotient_failure_count = 0
    for system in systematic_systems():
        system_count += 1
        partition = refine_partition(system)
        quotient, retained = minimal_quotient(system)
        if not retention_supports_updates(system, retained):
            quotient_failure_count += 1
        for state in system.states:
            if system.outputs[state] != quotient.outputs[retained[state]]:
                quotient_failure_count += 1
            for action in system.actions:
                source_next = system.transitions.get((state, action))
                quotient_next = quotient.transitions.get((retained[state], action))
                if (source_next is None) != (quotient_next is None):
                    quotient_failure_count += 1
                if source_next is not None:
                    transition_count += 1
                    if quotient_next != retained[source_next]:
                        quotient_failure_count += 1
        for left, right in product(system.states, repeat=2):
            pair_count += 1
            witness = distinguishing_word(system, left, right)
            same_class = partition.state_to_block[left] == partition.state_to_block[right]
            if same_class != (witness is None):
                disagreement_count += 1
            if witness is None:
                equivalent_pairs += 1
            else:
                witness_count += 1
                longest_witness = max(longest_witness, len(witness))
                if observe_word(system, left, witness) == observe_word(system, right, witness):
                    invalid_witness_count += 1

    def check(name: str, passed: bool, detail: dict) -> None:
        checks.append({"id": name, "status": "pass" if passed else "fail", "detail": detail})

    check("MR06-O1", system_count == 844 and pair_count == 5912 and disagreement_count == 0,
          {"systems": system_count, "ordered_pairs": pair_count, "disagreements": disagreement_count,
           "equivalent_pairs": equivalent_pairs, "distinguished_pairs": witness_count})
    check("MR06-O2", invalid_witness_count == 0,
          {"witnesses_checked": witness_count, "invalid_witnesses": invalid_witness_count,
           "longest_witness": longest_witness, "search": "exhaustive finite pair graph; no depth cutoff"})
    check("MR06-O3", quotient_failure_count == 0,
          {"quotients": system_count, "source_transitions": transition_count, "failures": quotient_failure_count})

    guarded = GuardedSystem(("enabled", "disabled"), ("a",),
                            {"enabled": 0, "disabled": 0}, {("enabled", "a"): "enabled"})
    guard_word = distinguishing_word(guarded, "enabled", "disabled")
    erased = {state: 0 for state in guarded.states}
    check("MR06-N1", guard_word == ("a",) and not retention_is_faithful(guarded, erased),
          {"guard_only_witness": list(guard_word) if guard_word is not None else None,
           "constant_observations": True, "output_only_erasure_rejected": not retention_is_faithful(guarded, erased)})
    totalized = GuardedSystem(guarded.states, guarded.actions, guarded.outputs,
                             {(state, "a"): state for state in guarded.states})
    check("MR06-N2", distinguishing_word(totalized, "enabled", "disabled") is None,
          {"silent_identity_totalization_changes_equivalence": guard_word is not None})

    memory = GuardedSystem(("marked", "retained", "erased", "hit"), ("a",),
                          {"marked": 0, "retained": 0, "erased": 0, "hit": 1},
                          {(state, "a"): ("erased" if state == "erased" else "hit")
                           for state in ("marked", "retained", "erased", "hit")})
    records = {"marked": "tail", "retained": "tail", "erased": "no-tail", "hit": "hit"}
    check("MR06-N3", retention_is_faithful(memory, records) and retention_supports_updates(memory, records)
          and distinguishing_word(memory, "marked", "retained") is None
          and distinguishing_word(memory, "marked", "erased") == ("a",),
          {"marker_erasure_with_tail_safe": True, "marker_and_tail_erasure_witness": ["a"]})

    finer = GuardedSystem(("x", "y", "u", "v"), ("a",), dict.fromkeys(("x", "y", "u", "v"), 0),
                         {("x", "a"): "u", ("y", "a"): "v", ("u", "a"): "u", ("v", "a"): "v"})
    extra_records = {"x": "start", "y": "start", "u": "left", "v": "right"}
    check("MR06-N4", retention_is_faithful(finer, extra_records)
          and not retention_supports_updates(finer, extra_records),
          {"information_sufficient": True, "arbitrary_extra_labels_updateable": False})
    return {
        "theorem_id": "MR-06",
        "status": "RNKE_CONTRACT_VERIFIED" if all(item["status"] == "pass" for item in checks) else "REJECTED",
        "checks": checks,
        "claim_boundary": {"finite_deterministic_partial_systems": True,
                           "formal_proof_assistant": False, "whole_sanskrit_grammar": False,
                           "smooth_extension": False, "novelty_certified": False},
    }
