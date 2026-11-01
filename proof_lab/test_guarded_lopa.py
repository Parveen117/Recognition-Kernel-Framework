"""MR-06 exact verification and adversarial checks; standard library only."""
import unittest

from proof_lab.morphic_recognition.guarded import (
    GuardedSystem, distinguishing_word, minimal_quotient, observe_word,
    refine_partition, retention_is_faithful, retention_supports_updates,
    verify_guarded_contract,
)


class GuardedLopaTests(unittest.TestCase):
    def test_systematic_independent_decisions_and_quotient_contract(self):
        packet = verify_guarded_contract()
        self.assertEqual(packet["status"], "RNKE_CONTRACT_VERIFIED", packet)
        self.assertTrue(all(item["status"] == "pass" for item in packet["checks"]))
        details = {item["id"]: item["detail"] for item in packet["checks"]}
        self.assertEqual(details["MR06-O1"]["systems"], 844)
        self.assertEqual(details["MR06-O1"]["ordered_pairs"], 5912)
        self.assertFalse(packet["claim_boundary"]["formal_proof_assistant"])

    def test_delayed_difference_is_not_lost_to_a_one_step_check(self):
        states = ("l0", "l1", "l2", "r0", "r1", "r2")
        outputs = dict.fromkeys(states, 0)
        outputs["l2"] = 1
        transitions = {(state, "a"): target for state, target in
                       zip(states, ("l1", "l2", "l2", "r1", "r2", "r2"))}
        system = GuardedSystem(states, ("a",), outputs, transitions)
        self.assertEqual(observe_word(system, "l0", ("a",)), observe_word(system, "r0", ("a",)))
        self.assertEqual(distinguishing_word(system, "l0", "r0"), ("a", "a"))
        partition = refine_partition(system)
        self.assertNotEqual(partition.state_to_block["l0"], partition.state_to_block["r0"])
        self.assertGreaterEqual(partition.strict_refinements, 2)

    def test_guard_only_difference_even_when_all_outputs_are_constant(self):
        system = GuardedSystem(("on", "off"), ("a",), {"on": 0, "off": 0}, {("on", "a"): "on"})
        self.assertEqual(distinguishing_word(system, "on", "off"), ("a",))
        self.assertEqual(observe_word(system, "on", ("a",)), (True, 0))
        self.assertEqual(observe_word(system, "off", ("a",)), (False, None))
        self.assertFalse(retention_is_faithful(system, {"on": 0, "off": 0}))

    def test_disabled_rule_is_not_silently_identity(self):
        partial = GuardedSystem(("on", "off"), ("a",), {"on": 0, "off": 0}, {("on", "a"): "on"})
        total = GuardedSystem(partial.states, partial.actions, partial.outputs,
                              {("on", "a"): "on", ("off", "a"): "off"})
        self.assertEqual(len(refine_partition(partial).blocks), 2)
        self.assertEqual(len(refine_partition(total).blocks), 1)

    def test_lopa_retains_necessary_effect(self):
        states = ("marker", "tail", "empty", "hit")
        system = GuardedSystem(states, ("use",), dict(zip(states, (0, 0, 0, 1))),
                               {(state, "use"): ("empty" if state == "empty" else "hit") for state in states})
        retained = {"marker": "tail", "tail": "tail", "empty": "empty", "hit": "hit"}
        self.assertTrue(retention_is_faithful(system, retained))
        self.assertTrue(retention_supports_updates(system, retained))
        self.assertIsNone(distinguishing_word(system, "marker", "tail"))
        self.assertEqual(distinguishing_word(system, "marker", "empty"), ("use",))
        quotient, recognition = minimal_quotient(system)
        self.assertEqual(len(quotient.states), 3)
        self.assertEqual(recognition["marker"], recognition["tail"])

    def test_information_sufficiency_does_not_update_arbitrary_extra_labels(self):
        system = GuardedSystem(("x", "y", "u", "v"), ("a",), dict.fromkeys(("x", "y", "u", "v"), 0),
                               {("x", "a"): "u", ("y", "a"): "v", ("u", "a"): "u", ("v", "a"): "v"})
        retained = {"x": "start", "y": "start", "u": "left", "v": "right"}
        self.assertTrue(retention_is_faithful(system, retained))
        self.assertFalse(retention_supports_updates(system, retained))

    def test_empty_action_alphabet_reduces_to_observation_equivalence(self):
        system = GuardedSystem(("x", "y", "z"), (), {"x": 0, "y": 0, "z": 1}, {})
        self.assertEqual(refine_partition(system).blocks, (("x", "y"), ("z",)))
        self.assertIsNone(distinguishing_word(system, "x", "y"))
        self.assertEqual(distinguishing_word(system, "x", "z"), ())

    def test_pair_search_returns_shortest_not_first_guard_it_sees(self):
        # The 'a' branch has a guard mismatch at depth 2; the 'b' branch has
        # an output mismatch at depth 1. BFS must return the shorter 'b'.
        states = ("x", "y", "u", "v", "p", "q")
        system = GuardedSystem(states, ("a", "b"), dict(zip(states, (0, 0, 0, 0, 0, 1))),
                               {("x", "a"): "u", ("y", "a"): "v", ("u", "a"): "u",
                                ("x", "b"): "p", ("y", "b"): "q"})
        self.assertEqual(distinguishing_word(system, "x", "y"), ("b",))

    def test_closed_cycles_terminate_without_depth_cutoff(self):
        system = GuardedSystem(("x", "y"), ("a",), {"x": 0, "y": 0},
                               {("x", "a"): "y", ("y", "a"): "x"})
        self.assertIsNone(distinguishing_word(system, "x", "y"))
        self.assertEqual(len(refine_partition(system).blocks), 1)

    def test_malformed_carriers_and_transitions_are_rejected(self):
        cases = [
            ((), (), {}, {}),
            (("x", "x"), (), {"x": 0}, {}),
            (("x",), ("a", "a"), {"x": 0}, {}),
            (("x",), ("a",), {}, {}),
            (("x",), ("a",), {"x": 0}, {("y", "a"): "x"}),
            (("x",), ("a",), {"x": 0}, {("x", "b"): "x"}),
            (("x",), ("a",), {"x": 0}, {("x", "a"): "y"}),
            (("x",), ("a",), {"x": 0}, {"x": "x"}),
            (("x",), (), {"x": float("nan")}, {}),
        ]
        for arguments in cases:
            with self.subTest(arguments=arguments), self.assertRaises(ValueError):
                GuardedSystem(*arguments)

    def test_source_mappings_are_copied_and_frozen(self):
        outputs = {"x": 0}
        transitions = {("x", "a"): "x"}
        system = GuardedSystem(("x",), ("a",), outputs, transitions)
        outputs["x"] = 1
        transitions.clear()
        self.assertEqual(observe_word(system, "x", ("a",)), (True, 0))
        with self.assertRaises(TypeError):
            system.outputs["x"] = 2


if __name__ == "__main__":
    unittest.main()
