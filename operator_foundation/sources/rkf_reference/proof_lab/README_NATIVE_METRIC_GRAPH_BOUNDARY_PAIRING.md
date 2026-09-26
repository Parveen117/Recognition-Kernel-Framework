# Native Metric-Graph Boundary Pairing Stage 3C

Stage 3C constructs the actual completed-Weil boundary orientation in the native
metric graph and proves that the later source decoder needs to recover only its
recognition class modulo the graph-null seam.

## Native chain

```text
M_X = I + C* C
r_partial = M_X^-1 q_b
J_X f = (f,Cf)
p_X = (r_partial, C r_partial)

-> L_partial(f) = <p_X,J_X f>
-> source analysis Xi_0 = D_Sigma J_X
-> decoder condition p_X-D_Sigma* c_partial in ker(J_X*)
-> minimum-energy quotient decoder
-> cut covariance.
```

Literal equality of ambient event states is sufficient but not necessary. The
correct RSC object is the boundary recognition class in

```text
(graph carrier) / ker(J_X*).
```

## Files

```text
theorum/35_native_metric_graph_boundary_pairing.md
proof_lab/native_metric_graph_boundary_pairing.py
proof_lab/test_native_metric_graph_boundary_pairing.py
proof_lab/NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_EXPECTED.sha256
proof_lab/imported/NATIVE_WEIL_METRIC_GRAPH_PINS.json
```

## Exact calibrations

```text
metric-graph boundary energy                   7/20
source-adapted minimum decoder energy          7/80
odd graph-state energy                         1/40
quotient minimum decoder burden                2/3
full boundary seam-jet lower                   > 0.0011
```

The packet verifies that an event state may differ from the boundary graph
state by a nonzero vector in `ker(J*)` while producing exactly the same boundary
functional. It also rejects a same-norm state in a different quotient class.

## Pull and run in Jupyter

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch main
!git pull --ff-only origin main

!python -m unittest -v proof_lab.test_native_metric_graph_boundary_pairing

!python -m proof_lab.native_metric_graph_boundary_pairing \
    --output proof_lab/NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_ACTUAL.json
```

Expected:

```text
Ran 7 tests
OK
PASS_NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_STAGE3C
ACTUAL_SOURCE_EVENT_ADAPTER False
```

The final `False` is deliberate. The actual prime--Gamma--diagonal-debt source
adapter has not yet been written as `Xi_0=D_Sigma J_X`, and its quotient decoder
class has not yet been certified.

## Canonical hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/NATIVE_METRIC_GRAPH_BOUNDARY_PAIRING_ACTUAL.json"
    ).read_bytes()
).hexdigest()

print("HASH_STABLE", expected == actual)
print("EXPECTED", expected)
print("ACTUAL  ", actual)
```

Expected:

```text
HASH_STABLE True
```

Pinned hash:

```text
dce944ee8ee33cbb6fc5cb86794622a9f2293135e8bef652dca8b85ed5c7df32
```

## Main correction from Stage 3A

Stage 3A asked for a coefficientwise boundary orientation on every event. Stage
3C proves that this was stronger than necessary. The source adapter only needs
to recover the metric boundary state modulo `ker(J_X*)`. This is the native
recognition-quotient form of the decoder theorem.

## Next stage

Stage 3D is the Native Prime--Gamma--Debt Source-Adapter Theorem. It must
construct

```text
D_Sigma : graph(J_X) -> Y_Sigma
```

from the already declared positive prime mismatch, Gamma mismatch and exact
diagonal-debt channels and prove

```text
Xi_0 = D_Sigma J_X
p_X-D_Sigma* c_partial in ker(J_X*)
||c_partial||^2 < 1.
```

The transferred direct-unshifted envelope `0.8290856201657449` becomes terminal
only after those identities and their Recognition-complete transport are
certified.

## Claim boundary

A pass proves the metric-graph and recognition-quotient theorems plus the exact
calibrations. It does not yet prove the actual source adapter, completed-Weil
cut covariance, or RH.
