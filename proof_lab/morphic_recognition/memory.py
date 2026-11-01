"""Exact finite typed linear Smriti closure and seam-repair certificates.

All states in each declared Q^d carrier are covered by the matrix identities.
Reachability restrictions, nonlinear guards and physical adapters are excluded.
The executable examples calibrate MR-04/MR-05; their universal proofs live in
the theorem capsules. Only integers and fractions are accepted (never floats).
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from types import MappingProxyType
from typing import Iterable, Mapping


def _rational(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("matrix entries must be int or Fraction")
    return Fraction(value)


def _dimension(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("dimensions must be nonnegative integers")
    return value


@dataclass(frozen=True, init=False)
class Matrix:
    rows: tuple[tuple[Fraction, ...], ...]
    ncols: int

    def __init__(self, rows: Iterable[Iterable[int | Fraction]], ncols: int):
        width = _dimension(ncols)
        data = tuple(tuple(_rational(x) for x in row) for row in rows)
        if any(len(row) != width for row in data):
            raise ValueError("ragged matrix or incorrect declared width")
        object.__setattr__(self, "rows", data)
        object.__setattr__(self, "ncols", width)

    @property
    def nrows(self) -> int:
        return len(self.rows)

    @property
    def shape(self) -> tuple[int, int]:
        return self.nrows, self.ncols

    def __matmul__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix) or self.ncols != other.nrows:
            raise ValueError("matrix multiplication dimension mismatch")
        return Matrix(
            (tuple(sum((a[k] * other.rows[k][j] for k in range(self.ncols)), Fraction(0))
                   for j in range(other.ncols)) for a in self.rows), other.ncols)

    def apply(self, vector: Iterable[int | Fraction]) -> tuple[Fraction, ...]:
        v = tuple(_rational(x) for x in vector)
        if len(v) != self.ncols:
            raise ValueError("state dimension mismatch")
        return tuple(sum((a * b for a, b in zip(row, v)), Fraction(0)) for row in self.rows)


def identity(dimension: int) -> Matrix:
    d = _dimension(dimension)
    return Matrix(((int(i == j) for j in range(d)) for i in range(d)), d)


def stack(*matrices: Matrix) -> Matrix:
    if not matrices:
        raise ValueError("stack needs a matrix with declared width")
    width = matrices[0].ncols
    if any(m.ncols != width for m in matrices):
        raise ValueError("stack dimension mismatch")
    return Matrix((row for m in matrices for row in m.rows), width)


def _rref(matrix: Matrix) -> tuple[Matrix, tuple[int, ...]]:
    data = [list(row) for row in matrix.rows]
    pivots: list[int] = []
    next_row = 0
    for col in range(matrix.ncols):
        pivot = next((r for r in range(next_row, len(data)) if data[r][col]), None)
        if pivot is None:
            continue
        data[next_row], data[pivot] = data[pivot], data[next_row]
        scale = data[next_row][col]
        data[next_row] = [x / scale for x in data[next_row]]
        for r in range(len(data)):
            if r != next_row and data[r][col]:
                factor = data[r][col]
                data[r] = [x - factor * y for x, y in zip(data[r], data[next_row])]
        pivots.append(col)
        next_row += 1
        if next_row == len(data):
            break
    return Matrix(data, matrix.ncols), tuple(pivots)


def rank(matrix: Matrix) -> int:
    return len(_rref(matrix)[1])


def row_basis(matrix: Matrix) -> Matrix:
    """Select original rows, retaining their interpretation; never return RREF rows."""
    selected: list[tuple[Fraction, ...]] = []
    for row in matrix.rows:
        candidate = Matrix((*selected, row), matrix.ncols)
        if rank(candidate) > len(selected):
            selected.append(row)
    return Matrix(selected, matrix.ncols)


def coordinates(row: Iterable[int | Fraction], basis: Matrix) -> tuple[Fraction, ...]:
    """Unique coefficients expressing row in an independent row basis."""
    target = tuple(_rational(x) for x in row)
    if len(target) != basis.ncols:
        raise ValueError("coordinate dimension mismatch")
    if rank(basis) != basis.nrows:
        raise ValueError("coordinate basis must be independent")
    # Solve basis.T * coefficients = target by exact augmented elimination.
    augmented = Matrix(
        ((*[basis.rows[j][i] for j in range(basis.nrows)], target[i])
         for i in range(basis.ncols)), basis.nrows + 1)
    reduced, pivots = _rref(augmented)
    if basis.nrows in pivots:
        raise ValueError("row is outside the declared span")
    result = [Fraction(0)] * basis.nrows
    for r, pivot in enumerate(pivots):
        result[pivot] = reduced.rows[r][-1]
    answer = tuple(result)
    if Matrix((answer,), basis.nrows) @ basis != Matrix((target,), basis.ncols):
        raise AssertionError("coordinate reconstruction failed")
    return answer


def nullspace(matrix: Matrix) -> tuple[tuple[Fraction, ...], ...]:
    reduced, pivots = _rref(matrix)
    free_columns = [j for j in range(matrix.ncols) if j not in pivots]
    vectors = []
    for free in free_columns:
        vector = [Fraction(0)] * matrix.ncols
        vector[free] = Fraction(1)
        for r, pivot in enumerate(pivots):
            vector[pivot] = -reduced.rows[r][free]
        vectors.append(tuple(vector))
    return tuple(vectors)


def kernel_witness(observer: Matrix, targets: Matrix) -> tuple[int, tuple[Fraction, ...]] | None:
    """Return (target row index, vector) with E vector=0, target row vector!=0."""
    if observer.ncols != targets.ncols:
        raise ValueError("witness dimension mismatch")
    for index, row in enumerate(targets.rows):
        for vector in nullspace(observer):
            if sum((a * b for a, b in zip(row, vector)), Fraction(0)):
                return index, vector
    return None


@dataclass(frozen=True)
class SeamRepair:
    compatible: bool
    source_basis: Matrix
    memory: Matrix
    repaired_basis: Matrix
    target_pullback: Matrix
    repaired_decoder: Matrix
    witness: tuple[int, tuple[Fraction, ...]] | None

    @property
    def minimum_channels(self) -> int:
        return self.memory.nrows


def seam_repair(source_observer: Matrix, target_observer: Matrix,
                transition: Matrix) -> SeamRepair:
    """MR-05: minimal one-seam repair of E_target F through E_source.

    The decoder acts on an independent repaired observer basis, so it is unique.
    No uniqueness is asserted for decoders on redundant raw output coordinates.
    """
    if transition.ncols != source_observer.ncols or transition.nrows != target_observer.ncols:
        raise ValueError("seam dimensions do not match")
    source = row_basis(source_observer)
    pullback = target_observer @ transition
    repaired = row_basis(stack(source, pullback))
    memory = Matrix(repaired.rows[source.nrows:], source.ncols)
    decoder = Matrix((coordinates(row, repaired) for row in pullback.rows), repaired.nrows)
    if decoder @ repaired != pullback:
        raise AssertionError("seam factorization failed")
    return SeamRepair(not memory.nrows, source, memory, repaired, pullback,
                      decoder, kernel_witness(source_observer, pullback))


@dataclass(frozen=True)
class Edge:
    name: str
    source: str
    target: str
    transition: Matrix
    guard: object | None = None


@dataclass(frozen=True, init=False)
class TypedGraph:
    dimensions: Mapping[str, int]
    observations: Mapping[str, Matrix]
    edges: tuple[Edge, ...]

    def __init__(self, dimensions: Mapping[str, int], observations: Mapping[str, Matrix],
                 edges: Iterable[Edge]):
        dims = dict(dimensions)
        obs = dict(observations)
        if any(not isinstance(node, str) or not node for node in dims):
            raise ValueError("nodes must have nonempty string names")
        for d in dims.values():
            _dimension(d)
        if set(obs) != set(dims):
            raise ValueError("every node needs exactly one observation matrix")
        for node, matrix in obs.items():
            if not isinstance(matrix, Matrix) or matrix.ncols != dims[node]:
                raise ValueError("observation carrier dimension mismatch")
        edge_tuple = tuple(edges)
        names: set[str] = set()
        for edge in edge_tuple:
            if not isinstance(edge, Edge):
                raise TypeError("graph transitions must be Edge objects")
            if edge.guard is not None:
                raise ValueError("state-dependent guards are outside the total-edge datum")
            if not isinstance(edge.name, str) or not edge.name or edge.name in names:
                raise ValueError("edge names must be nonempty and unique")
            if edge.source not in dims or edge.target not in dims:
                raise ValueError("edge has unknown source or target")
            if not isinstance(edge.transition, Matrix) or edge.transition.shape != (dims[edge.target], dims[edge.source]):
                raise ValueError("edge carrier dimension mismatch")
            names.add(edge.name)
        object.__setattr__(self, "dimensions", MappingProxyType(dims))
        object.__setattr__(self, "observations", MappingProxyType(obs))
        object.__setattr__(self, "edges", edge_tuple)

    def path_matrix(self, start: str, path: Iterable[str]) -> tuple[str, Matrix]:
        if start not in self.dimensions:
            raise ValueError("unknown start node")
        current = start
        matrix = identity(self.dimensions[start])
        edge_map = {edge.name: edge for edge in self.edges}
        for name in path:
            if name not in edge_map or edge_map[name].source != current:
                raise ValueError("path is not a composable directed edge word")
            edge = edge_map[name]
            matrix = edge.transition @ matrix
            current = edge.target
        return current, matrix


@dataclass(frozen=True)
class FutureRow:
    row: tuple[Fraction, ...]
    path: tuple[str, ...]
    terminal: str
    output_row: int


@dataclass(frozen=True)
class FutureWitness:
    node: str
    vector: tuple[Fraction, ...]
    path: tuple[str, ...]
    terminal: str
    output_row: int
    future_value: Fraction


@dataclass(frozen=True)
class MemoryClosure:
    graph: TypedGraph
    records: dict[str, tuple[FutureRow, ...]]
    bases: dict[str, Matrix]
    output_decoders: dict[str, Matrix]
    edge_maps: dict[str, Matrix]
    initial_ranks: dict[str, int]
    rank_history: tuple[dict[str, int], ...]

    @property
    def growth_rounds(self) -> int:
        return len(self.rank_history) - 1

    @property
    def minimum_channels(self) -> dict[str, int]:
        return {i: self.bases[i].nrows - self.initial_ranks[i] for i in self.bases}

    @property
    def memories(self) -> dict[str, Matrix]:
        return {i: Matrix(self.bases[i].rows[self.initial_ranks[i]:], self.graph.dimensions[i])
                for i in self.bases}

    def distinguishing_future(self, node: str, compression: Matrix | None = None) -> FutureWitness | None:
        if node not in self.bases:
            raise ValueError("unknown witness node")
        observer = self.graph.observations[node] if compression is None else compression
        if not isinstance(observer, Matrix) or observer.ncols != self.graph.dimensions[node]:
            raise ValueError("compression carrier dimension mismatch")
        witness = kernel_witness(observer, self.bases[node])
        if witness is None:
            return None
        index, vector = witness
        record = self.records[node][index]
        terminal, transport = self.graph.path_matrix(node, record.path)
        actual = (self.graph.observations[terminal] @ transport).apply(vector)[record.output_row]
        if terminal != record.terminal or not actual or any(observer.apply(vector)):
            raise AssertionError("future witness validation failed")
        return FutureWitness(node, vector, record.path, terminal, record.output_row, actual)

    def verify(self) -> dict[str, bool]:
        """Check exact identities on full ambient carriers, not sampled states."""
        g = self.graph
        checks = {key: False for key in (
            "structure_and_coverage", "output_factorization", "edge_intertwining",
            "independent_bases", "future_row_provenance", "finite_growth_bound",
            "strict_growth_history", "minimum_memory_rank_on_kernel")}
        # A caller may construct a candidate MemoryClosure directly. Coverage and
        # dimensions must be checked before comprehensions can pass vacuously.
        try:
            if not isinstance(g, TypedGraph):
                return checks
            nodes = set(g.dimensions)
            if any(set(mapping) != nodes for mapping in
                   (self.bases, self.records, self.output_decoders, self.initial_ranks)):
                return checks
            if set(self.edge_maps) != {e.name for e in g.edges} or not self.rank_history:
                return checks
            actual_initial = {i: rank(g.observations[i]) for i in nodes}
            if dict(self.initial_ranks) != actual_initial:
                return checks
            for node in nodes:
                basis = self.bases[node]
                if not isinstance(basis, Matrix) or basis.ncols != g.dimensions[node]:
                    return checks
                decoder = self.output_decoders[node]
                if not isinstance(decoder, Matrix) or decoder.shape != (g.observations[node].nrows, basis.nrows):
                    return checks
                if len(self.records[node]) != basis.nrows or basis.nrows < actual_initial[node]:
                    return checks
                for index, record in enumerate(self.records[node]):
                    if not isinstance(record, FutureRow) or len(record.row) != basis.ncols:
                        return checks
                    if record.terminal not in nodes or isinstance(record.output_row, bool) or not isinstance(record.output_row, int):
                        return checks
                    if not 0 <= record.output_row < g.observations[record.terminal].nrows:
                        return checks
                    if not isinstance(record.path, tuple) or len(record.path) > self.growth_rounds:
                        return checks
                    if index < actual_initial[node] and record.path:
                        return checks
            for edge in g.edges:
                induced = self.edge_maps[edge.name]
                if not isinstance(induced, Matrix) or induced.shape != (self.bases[edge.target].nrows, self.bases[edge.source].nrows):
                    return checks
            final_ranks = {i: self.bases[i].nrows for i in nodes}
            if dict(self.rank_history[0]) != actual_initial or dict(self.rank_history[-1]) != final_ranks:
                return checks
            for step, counts in enumerate(self.rank_history):
                if set(counts) != nodes:
                    return checks
                for node, count in counts.items():
                    if isinstance(count, bool) or not isinstance(count, int) or not actual_initial[node] <= count <= g.dimensions[node]:
                        return checks
                    if count != sum(len(record.path) <= step for record in self.records[node]):
                        return checks
            for previous, current in zip(self.rank_history, self.rank_history[1:]):
                if any(current[i] < previous[i] for i in nodes) or sum(current.values()) <= sum(previous.values()):
                    return checks
        except (TypeError, ValueError, KeyError, IndexError, AttributeError):
            return checks
        checks["structure_and_coverage"] = True
        output_ok = all(self.output_decoders[i] @ self.bases[i] == g.observations[i] for i in self.bases)
        edges_ok = all(self.edge_maps[e.name] @ self.bases[e.source] ==
                       self.bases[e.target] @ e.transition for e in g.edges)
        independent = all(rank(b) == b.nrows for b in self.bases.values())
        provenance = True
        for node, records in self.records.items():
            if self.bases[node].rows != tuple(record.row for record in records):
                provenance = False
            for record in records:
                try:
                    terminal, transport = g.path_matrix(node, record.path)
                except (TypeError, ValueError, KeyError):
                    provenance = False
                    continue
                response = g.observations[terminal] @ transport
                if terminal != record.terminal or response.rows[record.output_row] != record.row:
                    provenance = False
        bound = sum(g.dimensions.values()) - sum(self.initial_ranks.values())
        termination = self.growth_rounds <= bound
        history_growth = all(sum(b.values()) > sum(a.values())
                             for a, b in zip(self.rank_history, self.rank_history[1:]))
        # Compute the target rank on ker(E), independently of the rank difference.
        minimality = True
        for node, basis in self.bases.items():
            kernel = nullspace(g.observations[node])
            restricted = Matrix((tuple(sum((x * y for x, y in zip(row, v)), Fraction(0))
                                       for v in kernel) for row in basis.rows), len(kernel))
            minimality &= rank(restricted) == self.minimum_channels[node]
        return {"structure_and_coverage": True, "output_factorization": output_ok, "edge_intertwining": edges_ok,
                "independent_bases": independent, "future_row_provenance": provenance,
                "finite_growth_bound": termination, "strict_growth_history": history_growth,
                "minimum_memory_rank_on_kernel": minimality}


def future_memory(graph: TypedGraph) -> MemoryClosure:
    """MR-04/MR-05: synchronous closure of all future observation row spaces."""
    if not isinstance(graph, TypedGraph):
        raise TypeError("expected TypedGraph")
    records: dict[str, list[FutureRow]] = {i: [] for i in graph.dimensions}

    def append_independent(node: str, record: FutureRow, bank: dict[str, list[FutureRow]]) -> None:
        current = Matrix((r.row for r in bank[node]), graph.dimensions[node])
        if rank(stack(current, Matrix((record.row,), current.ncols))) > current.nrows:
            bank[node].append(record)

    for node, observation in graph.observations.items():
        for index, row in enumerate(observation.rows):
            append_independent(node, FutureRow(row, (), node, index), records)
    initial = {i: len(bank) for i, bank in records.items()}
    history = [initial.copy()]
    while True:
        updated = {i: list(bank) for i, bank in records.items()}
        for edge in graph.edges:
            for record in records[edge.target]:
                pulled = Matrix((record.row,), graph.dimensions[edge.target]) @ edge.transition
                append_independent(edge.source, FutureRow(pulled.rows[0], (edge.name,) + record.path,
                                                         record.terminal, record.output_row), updated)
        counts = {i: len(bank) for i, bank in updated.items()}
        if counts == history[-1]:
            break
        records = updated
        history.append(counts)
    bases = {i: Matrix((r.row for r in bank), graph.dimensions[i]) for i, bank in records.items()}
    outputs = {i: Matrix((coordinates(row, bases[i]) for row in graph.observations[i].rows), bases[i].nrows)
               for i in bases}
    edge_maps = {
        e.name: Matrix((coordinates(row, bases[e.source]) for row in (bases[e.target] @ e.transition).rows),
                       bases[e.source].nrows) for e in graph.edges}
    result = MemoryClosure(graph, {i: tuple(bank) for i, bank in records.items()}, bases, outputs,
                           edge_maps, initial, tuple(history))
    if not all(result.verify().values()):
        raise AssertionError("constructed memory closure did not verify")
    return result


def _json_matrix(matrix: Matrix) -> list[list[str]]:
    return [[str(x) for x in row] for row in matrix.rows]


def _check(identifier: str, passed: bool, detail: object) -> dict:
    return {"id": identifier, "passed": bool(passed), "status": "pass" if passed else "fail", "detail": detail}


def verify_memory_contract() -> dict:
    """Small exact calibration packet; this does not certify all possible inputs."""
    E = Matrix(((1, 0),), 2)
    A = Matrix(((1, 1), (0, 1)), 2)
    B = Matrix(((1, 0), (1, 1)), 2)
    failed_seam = seam_repair(E, E, A)
    safe_seam = seam_repair(E, E, B)
    witness = failed_seam.witness
    graph = TypedGraph({"q": 2}, {"q": E}, (Edge("A", "q", "q", A), Edge("B", "q", "q", B)))
    closed = future_memory(graph)
    late = closed.distinguishing_future("q")
    chain = TypedGraph({"i": 2, "j": 2, "k": 2},
                       {"i": E, "j": E, "k": Matrix(((0, 1),), 2)},
                       (Edge("ij", "i", "j", identity(2)), Edge("jk", "j", "k", identity(2))))
    chained = future_memory(chain)
    future = chained.distinguishing_future("i")
    shift = Matrix(((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0)), 4)
    delayed = future_memory(TypedGraph({"q": 4}, {"q": Matrix(((1, 0, 0, 0),), 4)},
                                      (Edge("shift", "q", "q", shift),)))
    # Explicit bad compression erases a future-visible direction.
    bad = delayed.distinguishing_future("q", Matrix(((1, 0, 0, 0), (0, 1, 0, 0)), 4))
    full = closed.bases["q"]
    rank_witnesses = [kernel_witness(Matrix(full.rows[:i] + full.rows[i + 1:], 2), full)
                      for i in range(full.nrows)]
    _, word_ba = graph.path_matrix("q", ("B", "A"))
    _, word_ab = graph.path_matrix("q", ("A", "B"))
    reduced_ba = closed.edge_maps["A"] @ closed.edge_maps["B"]
    x = (1, 0)
    ba_value, ab_value = (E @ word_ba).apply(x)[0], (E @ word_ab).apply(x)[0]
    single_checks = [
        _check("MR04-O1", all(closed.verify().values()) and all(delayed.verify().values()),
               {"shear": closed.verify(), "shift": delayed.verify(),
                "shift_rank_history": list(delayed.rank_history)}),
        _check("MR04-O2", closed.output_decoders["q"] @ full == E and
               all(closed.edge_maps[e.name] @ full == full @ e.transition for e in graph.edges) and rank(full) == full.nrows,
               {"R": _json_matrix(full), "C": _json_matrix(closed.output_decoders["q"]),
                "actions": {name: _json_matrix(m) for name, m in closed.edge_maps.items()}}),
        _check("MR04-O3", all(w is not None for w in rank_witnesses),
               {"rank": full.nrows, "deleted_basis_row_witnesses":
                [[str(x) for x in w[1]] if w else None for w in rank_witnesses]}),
        _check("MR04-O4", closed.verify()["minimum_memory_rank_on_kernel"] and
               rank(stack(E, closed.memories["q"])) == full.nrows,
               {"minimum_channels": closed.minimum_channels, "memory": _json_matrix(closed.memories["q"])}),
        _check("MR04-O5", bad is not None and 0 < len(bad.path) <= delayed.growth_rounds and bool(bad.future_value),
               {"future_word": list(bad.path) if bad else None, "response": str(bad.future_value) if bad else None}),
        _check("MR04-O6", word_ba == A @ B and word_ab == B @ A and reduced_ba @ full == full @ word_ba,
               {"chronological_BA": _json_matrix(word_ba), "chronological_AB": _json_matrix(word_ab)}),
        _check("MR04-N1", E.apply(x) == E.apply(B.apply(x)) and E.apply(A.apply(x)) != E.apply(A.apply(B.apply(x))),
               {"x": list(x), "Bx": [str(v) for v in B.apply(x)], "next_outputs": [str(ab_value), str(ba_value)]}),
        _check("MR04-N2", delayed.growth_rounds == 3 and bad is not None and len(bad.path) == 2,
               {"rank_history": list(delayed.rank_history), "one_step_compression_failure_word": list(bad.path) if bad else None}),
        _check("MR04-N3", late is not None and not any(E.apply(late.vector)) and bool(late.future_value),
               {"future_word": list(late.path) if late else None,
                "kernel_vector": [str(x) for x in late.vector] if late else None}),
        _check("MR04-N4", ba_value != ab_value,
               {"chronological_BA_response": str(ba_value), "chronological_AB_response": str(ab_value)}),
    ]
    parallel = future_memory(TypedGraph({"s": 1, "t": 1},
        {"s": identity(1), "t": identity(1)},
        (Edge("plus", "s", "t", identity(1)), Edge("minus", "s", "t", Matrix(((-1,),), 1)))))
    parallel_outputs = {name: (parallel.output_decoders["t"] @ matrix @ parallel.bases["s"]).apply((1,))[0]
                        for name, matrix in parallel.edge_maps.items()}
    E3 = Matrix(((1, 0, 0),), 3)
    target3 = Matrix(((0, 1, 0), (0, 0, 1)), 3)
    two_channel = seam_repair(E3, target3, identity(3))
    incomplete = Matrix(((1, 0, 0), (0, 1, 0)), 3)
    local_bad = kernel_witness(incomplete, target3)
    guards_refused = False
    try:
        TypedGraph({"s": 1, "t": 1}, {"s": Matrix((), 1), "t": identity(1)},
                   (Edge("guarded", "s", "t", identity(1), guard=lambda state: state[0] > 0),))
    except ValueError as exc:
        guards_refused = "guards" in str(exc)
    node_minimality = {}
    for node, basis in chained.bases.items():
        node_minimality[node] = all(kernel_witness(Matrix(basis.rows[:i] + basis.rows[i + 1:], basis.ncols), basis)
                                       is not None for i in range(basis.nrows))
    network_checks = [
        _check("MR05-O1", all(chained.verify().values()),
               {"verification": chained.verify(), "rank_history": list(chained.rank_history)}),
        _check("MR05-O2", chained.verify()["finite_growth_bound"] and
               all(rank(stack(chained.bases[e.source], chained.bases[e.target] @ e.transition)) ==
                   chained.bases[e.source].nrows for e in chain.edges),
               {"strict_rounds": chained.growth_rounds,
                "bound": sum(chain.dimensions.values()) - sum(chained.initial_ranks.values()), "final_equality_checked": True}),
        _check("MR05-O3", all(chained.verify()[key] for key in
               ("output_factorization", "edge_intertwining", "independent_bases")),
               {"edge_maps": {name: _json_matrix(m) for name, m in chained.edge_maps.items()}}),
        _check("MR05-O4", all(node_minimality.values()) and chained.verify()["minimum_memory_rank_on_kernel"],
               {"deletion_witnesses_at_every_node": node_minimality, "minimum_channels": chained.minimum_channels}),
        _check("MR05-O5", safe_seam.compatible and safe_seam.witness is None and
               safe_seam.repaired_decoder @ safe_seam.repaired_basis == E @ B and
               not failed_seam.compatible and witness is not None and not any(E.apply(witness[1])) and any((E @ A).apply(witness[1])),
               {"compatible_decoder": _json_matrix(safe_seam.repaired_decoder),
                "incompatible_kernel_vector": [str(x) for x in witness[1]] if witness else None}),
        _check("MR05-O6", two_channel.minimum_channels == rank(stack(E3, target3)) - rank(E3) == 2 and
               two_channel.repaired_decoder @ two_channel.repaired_basis == target3,
               {"minimum_channels": two_channel.minimum_channels, "memory": _json_matrix(two_channel.memory)}),
        _check("MR05-N1", chained.growth_rounds == 2 and future is not None and future.path == ("ij", "jk"),
               {"rank_history": list(chained.rank_history), "future_word": list(future.path) if future else None}),
        _check("MR05-N2", local_bad is not None and not any(incomplete.apply(local_bad[1])) and any(target3.apply(local_bad[1])),
               {"kernel_vector": [str(x) for x in local_bad[1]] if local_bad else None}),
        _check("MR05-N3", parallel_outputs["plus"] != parallel_outputs["minus"],
               {"outputs_by_edge": {name: str(value) for name, value in parallel_outputs.items()}}),
        _check("MR05-N4", guards_refused, {"guarded_input_refused": guards_refused}),
    ]
    results = []
    for identifier, checks in (("MR-04", single_checks), ("MR-05", network_checks)):
        passed = all(check["status"] == "pass" for check in checks)
        results.append({"theorem_id": identifier, "passed": passed,
                        "status": "RNKE_CONTRACT_VERIFIED" if passed else "REJECTED", "checks": checks})
    passed = all(result["passed"] for result in results)
    return {"status": "RNKE_CONTRACT_VERIFIED" if passed else "REJECTED", "passed": passed,
            "arithmetic": "exact rational", "theorems": results,
            "claim_boundary": "finite exact calibration; universal proofs in theorem capsules; not formalized"}
