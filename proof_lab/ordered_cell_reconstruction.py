"""SE46 ordered cell returns from detached native observer readings.

Python 3.12. This finite rational adapter reuses SE41's sensor and matrix
operations. It is neither a second operator engine nor a continuum/RH
certificate. All products have their displayed order, later actions left.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from proof_lab.endpoint_observer_index_certificate import add, eye, inv, mat, mul, scale
from proof_lab.ordered_return_feedback import (
    acquire, cayley, decode, encode, poly_add, poly_inverse_unit, poly_mul,
    poly_scale, poly_unit, power, squared_norm_at_most, unitary, zero,
)

ROOT = Path(__file__).resolve().parents[1]
RESULT = Path(__file__).with_name("ORDERED_CELL_RECONSTRUCTION_RESULT.json")
PINS = ROOT / "research/lambda_counting/SE46_SOURCE_PINS.json"


def vertex(i, j):
    return f"{i},{j}"


def edge_specs(width, height):
    for j in range(height + 1):
        for i in range(width):
            yield f"A:{i}:{j}", vertex(i, j), vertex(i + 1, j)
    for j in range(height):
        for i in range(width + 1):
            yield f"B:{i}:{j}", vertex(i, j), vertex(i, j + 1)


def grid(width, height, horizontal, vertical):
    edges = {key: copy.deepcopy(horizontal if key[0] == "A" else vertical)
             for key, _, _ in edge_specs(width, height)}
    return {"width": width, "height": height, "rank": len(horizontal), "edges": edges}


def acquire_grid(source, label, frames=None):
    """Fixture sensor; source maps are not passed to the decoder."""
    w, h, n = source["width"], source["height"], source["rank"]
    if frames is None:
        frames = {vertex(i, j): eye(n) for j in range(h + 1) for i in range(w + 1)}
    p = zero(n)
    p[0][0] = F(1)
    packets = []
    for key, u, v in edge_specs(w, h):
        local = mul(mul(inv(frames[v]), source["edges"][key]), frames[u])
        cut = mul(mul(inv(frames[v]), p), frames[v])
        packet = acquire(local, cut, label + "/" + key, [key], frames[v])
        packet.update({"edge": key, "source_vertex": u, "target_vertex": v,
                       "source_frame": encode(frames[u])})
        packets.append(packet)
    return encode({"source_id": label, "width": w, "height": h, "rank": n,
                   "frames": frames, "edge_readings": packets})


def decode_grid(bank):
    """Complete local maps are recovered only from serialized channels."""
    w, h, n = bank["width"], bank["height"], bank["rank"]
    if any(type(x) is not int or x < 1 for x in (w, h, n)):
        raise ValueError("positive grid sizes and response rank required")
    expected = {key: (u, v) for key, u, v in edge_specs(w, h)}
    vertices = {vertex(i, j) for j in range(h + 1) for i in range(w + 1)}
    if set(bank["frames"]) != vertices:
        raise ValueError("incomplete frame labels")
    for frame in bank["frames"].values():
        if len(frame) != n or any(len(row) != n for row in frame):
            raise ValueError("frame rank mismatch")
        inv(mat(frame))
    edges = {}
    for packet in bank["edge_readings"]:
        key = packet["edge"]
        if key not in expected or key in edges:
            raise ValueError("unmatched or duplicate edge")
        u, v = expected[key]
        if (packet["source_vertex"], packet["target_vertex"]) != (u, v):
            raise ValueError("edge endpoint mismatch")
        if (packet["source_frame"] != bank["frames"][u]
                or packet["frame"] != bank["frames"][v]):
            raise ValueError("unmatched endpoint calibration")
        p = mat(packet["cut"])
        if len(p) != n or any(len(row) != n for row in p) or mul(p, p) != p:
            raise ValueError("invalid declared cut")
        for reading in packet["readings"]:
            if (len(reading["accepted"]) != n or "complement" not in reading
                    or len(reading["complement"]) != n):
                raise ValueError("incomplete channel")
        edges[key] = decode(packet)
        inv(edges[key])
    if set(edges) != set(expected):
        raise ValueError("incomplete edge bank")
    return {"width": w, "height": h, "rank": n, "edges": edges}


def tree_transports(g, comb=True):
    w, h, n, e = g["width"], g["height"], g["rank"], g["edges"]
    t = {vertex(0, 0): eye(n)}
    if comb:
        for j in range(1, h + 1):
            t[vertex(0, j)] = mul(e[f"B:0:{j-1}"], t[vertex(0, j-1)])
        for j in range(h + 1):
            for i in range(1, w + 1):
                t[vertex(i, j)] = mul(e[f"A:{i-1}:{j}"], t[vertex(i-1, j)])
    else:
        for i in range(1, w + 1):
            t[vertex(i, 0)] = mul(e[f"A:{i-1}:0"], t[vertex(i-1, 0)])
        for i in range(w + 1):
            for j in range(1, h + 1):
                t[vertex(i, j)] = mul(e[f"B:{i}:{j-1}"], t[vertex(i, j-1)])
    return t


def normalize(g, t):
    e = {key: mul(mul(inv(t[v]), g["edges"][key]), t[u])
         for key, u, v in edge_specs(g["width"], g["height"])}
    return {**g, "edges": e}


def cell_returns(g, t):
    e, cells, raw = g["edges"], {}, {}
    for j in range(g["height"]):
        for i in range(g["width"]):
            p = mul(e[f"B:{i+1}:{j}"], e[f"A:{i}:{j}"])
            q = mul(e[f"A:{i}:{j+1}"], e[f"B:{i}:{j}"])
            key = vertex(i, j)
            raw[key] = mul(inv(q), p)
            cells[key] = mul(mul(inv(t[key]), raw[key]), t[key])
    return cells, raw


def cell_product(cells, width, height, n):
    total = eye(n)
    for j in range(height):
        row = eye(n)
        for i in range(width):
            row = mul(row, cells[vertex(i, j)])
        total = mul(row, total)
    return total


def boundary(g):
    e, w, h, n = g["edges"], g["width"], g["height"], g["rank"]
    p, q = eye(n), eye(n)
    for i in range(w):
        p = mul(e[f"A:{i}:0"], p)
    for j in range(h):
        p = mul(e[f"B:{w}:{j}"], p)
    for j in range(h):
        q = mul(e[f"B:0:{j}"], q)
    for i in range(w):
        q = mul(e[f"A:{i}:{h}"], q)
    return mul(inv(q), p)


def grid_from_cells(cells, width, height, n):
    g = grid(width, height, eye(n), eye(n))
    for j in range(height):
        for i in range(width):
            g["edges"][f"B:{i+1}:{j}"] = mul(g["edges"][f"B:{i}:{j}"], cells[vertex(i, j)])
    return g


def exp_monomial(x, m, depth):
    out = [zero(len(x)) for _ in range(depth + 1)]
    for j in range(depth // m + 1):
        out[m*j] = scale(F(1, factorial(j)), power(x, j))
    return out


def log_unit(a):
    ident = poly_unit(a)
    if a[0] != ident[0]:
        raise ValueError("formal logarithm requires constant term I")
    r, term, out = poly_add(a, ident, -1), ident, poly_scale(F(0), ident)
    for j in range(1, len(a)):
        term = poly_mul(term, r)
        out = poly_add(out, poly_scale(F((-1)**(j+1), j), term))
    return out


def product(items):
    out = eye(len(items[0]))
    for x in items:
        out = mul(out, x)
    return out


def poly_product(items):
    out = poly_unit(items[0])
    for x in items:
        out = poly_mul(out, x)
    return out


def lift_memory(a, k):
    """Faithful GL_2(Q_Sigma) x Z adapter with a declared central lift."""
    out = eye(5)
    for i in range(2):
        for j in range(2):
            out[i][j] = a[i][j]
    out[2][4] = F(k)
    return out


def projection(a):
    return [row[:2] for row in a[:2]]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def row_norm(a):
    return max(sum(abs(x) for x in row) for row in a)


def plane_turn(r, i, j, n=3):
    skew = zero(n)
    skew[i][j], skew[j][i] = -F(r), F(r)
    return cayley(skew)


def build():
    checks = []

    def check(name, condition, negative=False):
        if not condition:
            raise ArithmeticError(name)
        checks.append({"name": name, "kind": "negative" if negative else "positive", "pass": True})

    def rejects(action):
        try:
            action()
        except ValueError:
            return True
        return False

    a_gen, b_gen = mat([[0, 1], [0, 0]]), mat([[0, 0], [1, 0]])
    a_step, b_step = F(1, 3), F(1, 2)
    x, y = add(eye(2), scale(-a_step, a_gen)), add(eye(2), scale(-b_step, b_gen))
    source = grid(2, 2, x, y)
    base_bank = acquire_grid(source, "SE46-constant-count-connection")
    g = decode_grid(base_bank)
    t = tree_transports(g)
    normalized = normalize(g, t)
    cells, raw = cell_returns(g, t)
    h = boundary(g)
    check("complete cut/complement edge readings recover the supplied count transports", g == source)
    check("comb tree edges normalize to identity", all(
        normalized["edges"][key] == eye(2) for key, _, _ in edge_specs(2, 2)
        if key.startswith("A:") or key.startswith("B:0:")))
    check("four aligned faces recover all four independent chord matrices",
          grid_from_cells(cells, 2, 2, 2) == normalized)
    check("ordered transported cell product equals direct paired boundary",
          cell_product(cells, 2, 2, 2) == h == boundary(normalized))
    check("discarding connectors gives a wrong boundary", cell_product(raw, 2, 2, 2) != h, True)
    wrong_order = product([cells[vertex(i, j)] for j in range(2) for i in range(2)])
    check("reversing the specified row order changes the return", wrong_order != h, True)
    missing = copy.deepcopy(base_bank)
    missing["edge_readings"].pop()
    check("missing edge observation is rejected", rejects(lambda: decode_grid(missing)), True)
    bad_frame = copy.deepcopy(base_bank)
    bad_frame["edge_readings"][0]["source_frame"] = encode(add(eye(2), a_gen))
    check("inconsistent endpoint frame labels are rejected", rejects(lambda: decode_grid(bad_frame)), True)
    incomplete = copy.deepcopy(base_bank)
    incomplete["edge_readings"][0]["readings"][0].pop("complement")
    check("missing complementary channel is rejected", rejects(lambda: decode_grid(incomplete)), True)

    frames = {vertex(i, j): mul(add(eye(2), scale(F(i+1), a_gen)),
                               add(eye(2), scale(F(j+1, 3), b_gen)))
              for j in range(3) for i in range(3)}
    moving_bank = acquire_grid(source, "SE46-moving-vertex-frames", frames)
    moving = decode_grid(moving_bank)
    mt = tree_transports(moving)
    mf, _ = cell_returns(moving, mt)
    root = frames[vertex(0, 0)]
    conj = lambda a: mul(mul(inv(root), a), root)
    check("independent vertex frames give one common root conjugation of all cells",
          all(mf[key] == conj(cells[key]) for key in cells))
    check("moving-frame boundary and reconstructed product remain covariant",
          boundary(moving) == cell_product(mf, 2, 2, 2) == conj(h))
    alt_t = tree_transports(g, comb=False)
    alt_norm = normalize(g, alt_t)
    check("an alternative tree preserves the based boundary with its own path word",
          boundary(alt_norm) == h)
    alt_cells, _ = cell_returns(g, alt_t)
    check("reusing the comb scan with another tree is not a lawful replacement",
          cell_product(alt_cells, 2, 2, 2) != h, True)
    connector = t[vertex(1, 1)]
    relocated = mul(mul(connector, h), inv(connector))
    check("a relocated base has the same trace and reconstructs the original return",
          trace(relocated) == trace(h) and mul(mul(inv(connector), relocated), connector) == h)

    ident_cells = {vertex(i, j): eye(2) for j in range(2) for i in range(2)}
    flat = grid_from_cells(ident_cells, 2, 2, 2)
    check("all identity faces give identity normalized edges on the supplied grid",
          all(e == eye(2) for e in flat["edges"].values()))
    changed = copy.deepcopy(ident_cells)
    changed[vertex(1, 0)] = add(eye(2), a_gen)
    check("omitting one face leaves a boundary ambiguity in the unrestricted protocol",
          boundary(grid_from_cells(changed, 2, 2, 2)) != boundary(flat), True)

    aa, bb = add(eye(2), a_gen), add(eye(2), b_gen)
    spectrum_grids = [grid_from_cells({"0,0": aa, "1,0": z}, 2, 1, 2) for z in (bb, aa)]
    spectrum_banks = [acquire_grid(s, f"SE46-individual-conjugacy-blind-{i}")
                      for i, s in enumerate(spectrum_grids)]
    decoded_spectra = [decode_grid(bank) for bank in spectrum_banks]
    swap = mat([[0, 1], [1, 0]])
    check("both face banks have equal individual conjugacy classes",
          mul(mul(inv(swap), aa), swap) == bb and trace(aa) == trace(bb) == 2)
    check("individual cell spectra miss a different boundary trace",
          [trace(boundary(s)) for s in decoded_spectra] == [F(3), F(2)], True)

    fine_source = grid(4, 4, add(eye(2), scale(-a_step/2, a_gen)),
                       add(eye(2), scale(-b_step/2, b_gen)))
    fine_bank = acquire_grid(fine_source, "SE46-consistent-subdivision")
    fine = decode_grid(fine_bank)
    fine_cells, _ = cell_returns(fine, tree_transports(fine))
    check("source-consistent subdivision preserves edge products exactly",
          power(fine["edges"]["A:0:0"], 2) == x and power(fine["edges"]["B:0:0"], 2) == y)
    check("sixteen refined cells reconstruct the same four-cell boundary",
          cell_product(fine_cells, 4, 4, 2) == boundary(fine) == h)
    incompatible = grid(4, 4, x, y)
    check("refinement without consistent edge products can change the source",
          boundary(incompatible) != h, True)

    m, depth = 2, 8
    generators = [a_gen, b_gen, add(a_gen, scale(F(2), b_gen))]
    series = [exp_monomial(xi, m, depth) for xi in generators]
    formal = poly_product(series)
    logarithm = log_unit(formal)
    total = zero(2)
    correction = zero(2)
    for i, xi in enumerate(generators):
        total = add(total, xi)
        for xj in generators[i+1:]:
            correction = add(correction, scale(F(1, 2), add(mul(xi, xj), mul(xj, xi), -1)))
    check("formal logarithm retains the generator sum and ordered commutator correction",
          logarithm[m] == total and logarithm[2*m] == correction
          and all(logarithm[k] == zero(2) for k in range(3*m) if k not in (m, 2*m)))
    check("adding logarithms alone loses the nonzero second-order response",
          correction != zero(2), True)
    word_generators = [scale(-1, a_gen), scale(-1, b_gen), a_gen, b_gen]
    word = poly_product([exp_monomial(xi, m, depth) for xi in word_generators])
    bracket = add(mul(a_gen, b_gen), mul(b_gen, a_gen), -1)
    check("a closed order-only word is invisible below unit depth four",
          all(word[k] == zero(2) for k in range(1, 2*m)), True)
    check("unit depth four detects its exact nonzero commutator",
          word[2*m] == bracket != zero(2))
    horizontal = exp_monomial(scale(-2*a_step, a_gen), m, depth)
    vertical = exp_monomial(scale(-2*b_step, b_gen), m, depth)
    pq_return = poly_mul(poly_inverse_unit(poly_mul(horizontal, vertical)),
                         poly_mul(vertical, horizontal))
    check("forward T-then-V comparison reads the negative counting-curvature coefficient",
          pq_return[2*m] == scale(-4*a_step*b_step, bracket)
          and all(pq_return[k] == zero(2) for k in range(1, 2*m)))

    lifted_sources = [grid_from_cells({"0,0": lift_memory(aa, k),
                                      "1,0": lift_memory(inv(aa), 0)}, 2, 1, 5) for k in (1, 0)]
    memory_banks = [acquire_grid(s, f"SE46-retained-central-memory-{i}")
                    for i, s in enumerate(lifted_sources)]
    lifted = [decode_grid(bank) for bank in memory_banks]
    lifted_h = [boundary(s) for s in lifted]
    check("all projected edge and cell matrices coincide in the two lifted sources",
          all(projection(lifted[0]["edges"][key]) == projection(lifted[1]["edges"][key])
              for key in lifted[0]["edges"]))
    check("projected identity does not determine the retained central memory",
          projection(lifted_h[0]) == projection(lifted_h[1]) == eye(2)
          and lifted_h[0] != lifted_h[1], True)
    check("ordered full-channel reconstruction retains the integer memory",
          all(cell_product(cell_returns(s, tree_transports(s))[0], 2, 1, 5) == bh
              for s, bh in zip(lifted, lifted_h)) and [bh[2][4] for bh in lifted_h] == [1, 0])

    raw_returns = [plane_turn(F(1, 3), 0, 1), plane_turn(F(1, 4), 1, 2)]
    connectors = [plane_turn(F(1, 5), 0, 2), plane_turn(F(1, 6), 0, 1)]
    sensed_returns = [mul(plane_turn(F(1, 80), 0, 2), rh) for rh in raw_returns]
    sensed_connectors = [mul(plane_turn(F(1, 100), 1, 2), rt) for rt in connectors]
    eps_h, eps_t = F(1, 40), F(1, 50)
    factor_error, total_error = eps_h + 2*eps_t, 2*(eps_h + 2*eps_t)
    factors = [mul(mul(inv(rt), rh), rt) for rt, rh in zip(connectors, raw_returns)]
    sensed_factors = [mul(mul(inv(rt), rh), rt) for rt, rh in zip(sensed_connectors, sensed_returns)]
    p3 = mat([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    noise_packets = [acquire(ff, p3, f"SE46-noisy-aligned-cell-{i}", [str(i)], eye(3))
                     for i, ff in enumerate(sensed_factors)]
    decoded_factors = [decode(packet) for packet in noise_packets]
    noisy_h, true_h = product(decoded_factors), product(factors)
    check("declared sensor and connector bounds hold with unitary true and read maps",
          all(unitary(v) for v in raw_returns+connectors+sensed_returns+sensed_connectors)
          and all(squared_norm_at_most(add(u, v, -1), eps_h)
                  for u, v in zip(sensed_returns, raw_returns))
          and all(squared_norm_at_most(add(u, v, -1), eps_t)
                  for u, v in zip(sensed_connectors, connectors)))
    check("transported-cell error includes twice the connector uncertainty",
          all(squared_norm_at_most(add(u, v, -1), factor_error)
              for u, v in zip(decoded_factors, factors)))
    check("two unitary cell errors obey the exact product budget 13/100",
          total_error == F(13, 100) and squared_norm_at_most(add(noisy_h, true_h, -1), total_error))
    check("measured boundary residual exceeds the error budget and certifies nonidentity",
          not squared_norm_at_most(add(noisy_h, eye(3), -1), total_error) and true_h != eye(3))

    exact_factors = [aa, bb, inv(aa)]
    approx_factors = [add(aa, scale(F(1, 100), b_gen)), bb,
                      add(inv(aa), scale(F(1, 80), b_gen))]
    telescope, budget = zero(2), F(0)
    for k in range(3):
        prefix = product(approx_factors[:k]) if k else eye(2)
        suffix = product(exact_factors[k+1:]) if k < 2 else eye(2)
        error = add(approx_factors[k], exact_factors[k], -1)
        telescope = add(telescope, mul(mul(prefix, error), suffix))
        budget += row_norm(prefix)*row_norm(error)*row_norm(suffix)
    difference = add(product(approx_factors), product(exact_factors), -1)
    check("general nonunitary product obeys the exact telescoping identity and norm bound",
          telescope == difference and row_norm(difference) <= budget)
    check("a sub-budget reading can still come from a nonidentity source",
          plane_turn(F(1, 1000), 0, 1) != eye(3)
          and squared_norm_at_most(add(plane_turn(F(1, 1000), 0, 1), eye(3), -1), total_error), True)

    return encode({
        "stage": "SE46", "author": "Monty",
        "scope": "Exact finite ordered-cell and moving-frame readings in supplied native response representations; formal unit coefficients and retained declared memory. No continuum flatness, universal physical connection, RH sign or mass gap.",
        "base_grid": base_bank, "moving_grid": moving_bank,
        "aligned_cells": cells, "direct_boundary": h,
        "spectral_collision_grids": spectrum_banks,
        "spectral_collision_boundary_traces": [trace(boundary(s)) for s in decoded_spectra],
        "refined_grid": fine_bank,
        "formal": {"unit_order": m, "depth": depth, "generators": generators,
                   "logarithm": logarithm, "order_only_word": word,
                   "count_horizontal_return": pq_return},
        "lifted_memory_grids": memory_banks, "lifted_boundaries": lifted_h,
        "noise": {"raw_returns": raw_returns, "connectors": connectors,
                  "read_returns": sensed_returns, "read_connectors": sensed_connectors,
                  "aligned_reading_packets": noise_packets,
                  "return_error_bound": eps_h, "connector_error_bound": eps_t,
                  "factor_error_bound": factor_error, "product_error_bound": total_error,
                  "true_boundary": true_h, "read_boundary": noisy_h},
        "nonunitary_noise": {"factors": exact_factors, "read_factors": approx_factors,
                              "telescoped_error": telescope, "row_norm_bound": budget},
        "checks": checks, "check_count": len(checks),
        "negative_control_count": sum(c["kind"] == "negative" for c in checks),
    })


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        RESULT.write_text(json.dumps(result, indent=2)+"\n")
    if args.check:
        for pin in json.loads(PINS.read_text())["local_files"]:
            if hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest() != pin["sha256"]:
                raise ArithmeticError("source pin mismatch: "+pin["path"])
        archive = json.loads(RESULT.read_text())
        if archive != result:
            raise ArithmeticError("saved ordered-cell readings differ from replay")
        banks = [archive["base_grid"], archive["moving_grid"], archive["refined_grid"]]
        banks += archive["spectral_collision_grids"] + archive["lifted_memory_grids"]
        for bank in banks:
            g = decode_grid(bank)
            cells, _ = cell_returns(g, tree_transports(g))
            if cell_product(cells, g["width"], g["height"], g["rank"]) != boundary(g):
                raise ArithmeticError("archived cell reconstruction failed")
        for packet in archive["noise"]["aligned_reading_packets"]:
            decode(packet)
    print(f"PASS SE46: {result['check_count']} exact controls; "
          f"{result['negative_control_count']} negative controls; "
          f"archive={'matched' if args.check else 'written' if args.write else 'not requested'}")


if __name__ == "__main__":
    main()
