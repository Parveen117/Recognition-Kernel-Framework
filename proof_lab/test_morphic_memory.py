"""Independent finite contract probes for exact typed linear Smriti closure."""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import json
import unittest

from proof_lab.morphic_recognition.memory import (
    Edge, Matrix, MemoryClosure, TypedGraph, coordinates, future_memory, identity, kernel_witness,
    nullspace, rank, row_basis, seam_repair, stack, verify_memory_contract,
)


def direct_apply(rows, vector):
    """Separate tuple-level evaluation, without Matrix.apply or matrix products."""
    return tuple(sum((x * y for x, y in zip(row, vector)), Q(0)) for row in rows)


class MorphicMemoryTests(unittest.TestCase):
    def setUp(self):
        self.E = Matrix(((1, 0),), 2)
        self.A = Matrix(((1, 1), (0, 1)), 2)
        self.B = Matrix(((1, 0), (1, 1)), 2)

    def shear_graph(self):
        return TypedGraph({"q": 2}, {"q": self.E},
                          (Edge("A", "q", "q", self.A), Edge("B", "q", "q", self.B)))

    def test_exact_rational_basis_coordinates_and_nullspace(self):
        matrix = Matrix(((Q(1, 2), Q(1, 3), 0), (1, Q(2, 3), 0), (0, 1, Q(2, 5))), 3)
        basis = row_basis(matrix)
        self.assertEqual(basis.rows, (matrix.rows[0], matrix.rows[2]))
        self.assertEqual(coordinates(matrix.rows[1], basis), (2, 0))
        self.assertEqual(rank(matrix), 2)
        kernel = nullspace(matrix)
        self.assertEqual(len(kernel), 1)
        self.assertEqual(direct_apply(matrix.rows, kernel[0]), (0, 0, 0))
        with self.assertRaises(ValueError):
            coordinates((1, 0, 0), basis)
        with self.assertRaises(ValueError):
            coordinates((1, 0, 0), matrix)

    def test_seam_compatible_and_minimal_repair(self):
        compatible = seam_repair(self.E, self.E, self.B)
        self.assertTrue(compatible.compatible)
        self.assertIsNone(compatible.witness)
        repair = seam_repair(self.E, self.E, self.A)
        self.assertFalse(repair.compatible)
        self.assertEqual(repair.minimum_channels, 1)
        self.assertEqual(repair.memory.rows, ((1, 1),))
        self.assertEqual(repair.repaired_decoder @ repair.repaired_basis, self.E @ self.A)
        target_row, vector = repair.witness
        self.assertEqual(direct_apply(self.E.rows, vector), (0,))
        self.assertNotEqual(direct_apply((self.E @ self.A).rows, vector)[target_row], 0)

    def test_redundant_observers_do_not_overcount_memory(self):
        E = Matrix(((2, 0), (1, 0), (0, 0)), 2)
        graph = TypedGraph({"q": 2}, {"q": E}, (Edge("A", "q", "q", self.A),))
        result = future_memory(graph)
        self.assertEqual(result.initial_ranks, {"q": 1})
        self.assertEqual(result.minimum_channels, {"q": 1})
        self.assertEqual(result.bases["q"].rows, ((2, 0), (2, 2)))
        self.assertEqual(result.output_decoders["q"].shape, (3, 2))
        self.assertEqual(result.output_decoders["q"] @ result.bases["q"], E)
        self.assertTrue(all(result.verify().values()))

    def test_shear_future_words_match_reduced_outputs(self):
        result = future_memory(self.shear_graph())
        matrices = {"A": self.A.rows, "B": self.B.rows}
        for length in range(5):
            for word in product(("A", "B"), repeat=length):
                for vector in ((1, 0), (0, 1), (Q(2, 3), Q(-5, 7))):
                    original = vector
                    reduced = direct_apply(result.bases["q"].rows, vector)
                    for edge in word:
                        original = direct_apply(matrices[edge], original)
                        reduced = direct_apply(result.edge_maps[edge].rows, reduced)
                    self.assertEqual(direct_apply(self.E.rows, original),
                                     direct_apply(result.output_decoders["q"].rows, reduced))
        self.assertEqual(result.minimum_channels, {"q": 1})
        self.assertEqual(result.growth_rounds, 1)

    def test_order_and_delayed_visibility_are_detected(self):
        result = future_memory(self.shear_graph())
        witness = result.distinguishing_future("q")
        self.assertEqual(witness.path, ("A",))
        self.assertEqual(self.E.apply(witness.vector), (0,))
        self.assertNotEqual(witness.future_value, 0)
        e1 = (1, 0)
        self.assertEqual(self.E.apply(e1), self.E.apply(self.B.apply(e1)))
        self.assertNotEqual(self.E.apply(self.A.apply(e1)), self.E.apply(self.A.apply(self.B.apply(e1))))
        self.assertIsNone(result.distinguishing_future("q", result.bases["q"]))

    def test_three_node_backward_propagation_and_raw_provenance(self):
        graph = TypedGraph({"i": 2, "j": 2, "k": 2},
                           {"i": self.E, "j": self.E, "k": Matrix(((0, 3),), 2)},
                           (Edge("ij", "i", "j", identity(2)), Edge("jk", "j", "k", identity(2))))
        result = future_memory(graph)
        self.assertEqual(result.rank_history, ({"i": 1, "j": 1, "k": 1},
                                              {"i": 1, "j": 2, "k": 1},
                                              {"i": 2, "j": 2, "k": 1}))
        record = result.records["i"][1]
        self.assertEqual(record.path, ("ij", "jk"))
        self.assertEqual(record.row, (0, 3))  # raw observation, not normalized RREF
        self.assertEqual(record.terminal, "k")
        self.assertEqual(result.edge_maps["jk"].shape, (1, 2))
        self.assertTrue(all(result.verify().values()))

    def test_delayed_four_dimensional_observation_requires_three_rounds(self):
        shift = Matrix(((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0)), 4)
        graph = TypedGraph({"q": 4}, {"q": Matrix(((1, 0, 0, 0),), 4)}, (Edge("S", "q", "q", shift),))
        result = future_memory(graph)
        self.assertEqual([r["q"] for r in result.rank_history], [1, 2, 3, 4])
        self.assertEqual([len(r.path) for r in result.records["q"]], [0, 1, 2, 3])
        for keep in range(1, 4):
            compression = Matrix(result.bases["q"].rows[:keep], 4)
            witness = result.distinguishing_future("q", compression)
            self.assertEqual(witness.path, ("S",) * keep)
            self.assertTrue(all(x == 0 for x in direct_apply(compression.rows, witness.vector)))
            self.assertEqual(witness.future_value, 1)
        self.assertEqual(result.minimum_channels, {"q": 3})

    def test_different_carrier_dimensions_and_rational_transport(self):
        E = Matrix(((0, 1, 0),), 3)
        F = Matrix(((Q(1, 3), 0, Q(2, 7)), (0, Q(3, 5), 0)), 3)
        graph = TypedGraph({"s": 3, "t": 2},
                           {"s": E, "t": Matrix(((Q(2, 3), 0), (0, 0)), 2)},
                           (Edge("f", "s", "t", F),))
        result = future_memory(graph)
        self.assertEqual(result.minimum_channels, {"s": 1, "t": 0})
        self.assertEqual(result.records["s"][1].row, (Q(2, 9), 0, Q(4, 21)))
        vector = (Q(3, 2), Q(-1, 6), 4)
        expected = direct_apply(graph.observations["t"].rows, direct_apply(F.rows, vector))
        reduced = direct_apply(result.edge_maps["f"].rows, direct_apply(result.bases["s"].rows, vector))
        self.assertEqual(expected, direct_apply(result.output_decoders["t"].rows, reduced))

    def test_zero_observations_and_empty_output_spaces(self):
        graph = TypedGraph({"q": 2}, {"q": Matrix((), 2)}, (Edge("A", "q", "q", self.A),))
        result = future_memory(graph)
        self.assertEqual(result.bases["q"].shape, (0, 2))
        self.assertEqual(result.edge_maps["A"].shape, (0, 0))
        self.assertEqual(result.growth_rounds, 0)
        self.assertEqual(result.minimum_channels, {"q": 0})
        self.assertIsNone(result.distinguishing_future("q"))
        # Empty current output can still need memory for a future node.
        graph2 = TypedGraph({"s": 2, "t": 2},
                            {"s": Matrix((), 2), "t": self.E},
                            (Edge("f", "s", "t", identity(2)),))
        self.assertEqual(future_memory(graph2).minimum_channels, {"s": 1, "t": 0})

    def test_zero_dimensional_carriers_and_empty_graph(self):
        graph = TypedGraph({"z": 0, "x": 2},
                           {"z": Matrix(((), ()), 0), "x": self.E},
                           (Edge("up", "z", "x", Matrix(((), ()), 0)),
                            Edge("down", "x", "z", Matrix((), 2))))
        result = future_memory(graph)
        self.assertEqual(result.bases["z"].shape, (0, 0))
        self.assertEqual(result.output_decoders["z"].shape, (2, 0))
        self.assertTrue(all(result.verify().values()))
        self.assertEqual(future_memory(TypedGraph({}, {}, ())).minimum_channels, {})
        self.assertEqual(nullspace(Matrix((), 0)), ())

    def test_disconnected_nodes_and_closure_stability(self):
        graph = TypedGraph({"q": 2, "isolated": 3},
                           {"q": self.E, "isolated": Matrix(((0, 1, 0),), 3)},
                           (Edge("A", "q", "q", self.A),))
        result = future_memory(graph)
        stable = future_memory(TypedGraph(graph.dimensions, result.bases, graph.edges))
        self.assertEqual(stable.growth_rounds, 0)
        self.assertEqual(stable.bases, result.bases)
        self.assertEqual(stable.minimum_channels, {"q": 0, "isolated": 0})

    def test_bad_compression_and_tampered_intertwiner_are_rejected(self):
        result = future_memory(self.shear_graph())
        bad = result.distinguishing_future("q", Matrix(((1, 0), (2, 0)), 2))
        self.assertIsNotNone(bad)
        corrupted = replace(result, edge_maps={**result.edge_maps, "A": identity(2)})
        self.assertFalse(corrupted.verify()["edge_intertwining"])
        bad_output = replace(result, output_decoders={"q": Matrix(((0, 0),), 2)})
        self.assertFalse(bad_output.verify()["output_factorization"])

    def test_forged_empty_coverage_and_malformed_certificates_fail_closed(self):
        graph = TypedGraph({"q": 2}, {"q": self.E}, ())
        forged = MemoryClosure(graph, {}, {}, {}, {}, {}, ({},))
        self.assertFalse(forged.verify()["structure_and_coverage"])
        correct = future_memory(self.shear_graph())
        for changes in (
            {"edge_maps": {}}, {"initial_ranks": {"q": 0}}, {"rank_history": ()},
            {"rank_history": ({"q": 1}, {"q": 1})}, {"records": {"q": ()}},
            {"records": {"q": (replace(correct.records["q"][0], output_row=-1), correct.records["q"][1])}},
            {"records": {"q": (replace(correct.records["q"][0], terminal="absent"), correct.records["q"][1])}},
        ):
            with self.subTest(changes=changes):
                self.assertFalse(replace(correct, **changes).verify()["structure_and_coverage"])
        with self.assertRaises(TypeError):
            graph.dimensions["q"] = 99

    def test_minimality_every_retained_memory_channel_is_needed(self):
        result = future_memory(self.shear_graph())
        for node, basis in result.bases.items():
            E = result.graph.observations[node]
            self.assertEqual(rank(stack(E, result.memories[node])), basis.nrows)
            for k in range(result.initial_ranks[node], basis.nrows):
                reduced = Matrix(basis.rows[:k] + basis.rows[k + 1:], basis.ncols)
                witness = kernel_witness(reduced, basis)
                self.assertIsNotNone(witness)
                self.assertEqual(direct_apply(reduced.rows, witness[1]), (0,) * reduced.nrows)

    def test_input_validation(self):
        for value in (1.0, True, "1", complex(1)):
            with self.subTest(value=value), self.assertRaises(TypeError):
                Matrix(((value,),), 1)
        for d in (-1, 2.0, True):
            with self.subTest(d=d), self.assertRaises(ValueError):
                Matrix((), d)
        with self.assertRaises(ValueError):
            Matrix(((1,), (1, 2)), 2)
        with self.assertRaises(ValueError):
            self.A @ Matrix(((1,),), 1)
        with self.assertRaises(ValueError):
            self.A.apply((1,))
        invalid = (
            ({"q": 2}, {}, ()),
            ({"q": 2}, {"q": Matrix(((1,),), 1)}, ()),
            ({"": 2}, {"": self.E}, ()),
            ({"q": 2}, {"q": self.E}, (Edge("a", "q", "missing", self.A),)),
            ({"q": 2}, {"q": self.E}, (Edge("a", "q", "q", Matrix(((1,),), 1)),)),
            ({"q": 2}, {"q": self.E}, (Edge("a", "q", "q", self.A), Edge("a", "q", "q", self.B))),
        )
        for args in invalid:
            with self.subTest(args=args), self.assertRaises(ValueError):
                TypedGraph(*args)
        with self.assertRaises(ValueError):
            seam_repair(self.E, self.E, Matrix(((1,),), 1))
        with self.assertRaisesRegex(ValueError, "guards"):
            TypedGraph({"q": 2}, {"q": self.E},
                       (Edge("guarded", "q", "q", self.A, guard=lambda x: x[0] > 0),))
        graph = self.shear_graph()
        with self.assertRaises(ValueError):
            graph.path_matrix("q", ("unknown",))
        with self.assertRaises(ValueError):
            graph.path_matrix("missing", ())
        result = future_memory(graph)
        with self.assertRaises(ValueError):
            result.distinguishing_future("missing")
        with self.assertRaises(ValueError):
            result.distinguishing_future("q", Matrix((), 3))

    def test_certificate_is_derived_and_json_safe(self):
        result = verify_memory_contract()
        self.assertTrue(result["passed"])
        self.assertEqual(result["status"], "RNKE_CONTRACT_VERIFIED")
        self.assertEqual([t["theorem_id"] for t in result["theorems"]], ["MR-04", "MR-05"])
        for theorem in result["theorems"]:
            self.assertTrue(all(check["passed"] for check in theorem["checks"]))
        json.dumps(result, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
