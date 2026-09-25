# Cut-Variational Minimal Observer v0.1

This stage derives the observer from cut-memory energy instead of assuming a five-label packet.

## Native theorem chain

```text
cut-generated memory lift M
-> observer action ||(I-P)M||^2
-> zero action iff target faithfulness
-> minimal faithful rank = memory rank
-> target-relative blind dimension
-> finite seam matrix only after the observer is derived.
```

## Exact calibrations

```text
1. rank-five memory: rank-5 action 0, rank-4 action 1/25;
2. wrong rank-five orientation: action 1/25;
3. exact ordered-product 50/45/5 source restriction;
4. split-occurrence determinant -2592 and repaired rank 50;
5. Recognition-complete observer residual 1/10 -> 1/18 -> 0;
6. Hilbert-Schmidt variational tail by observer rank.
```

No RH data is used.

## Run in Jupyter

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch main
!git pull --ff-only origin main

!python -m unittest -v proof_lab.test_cut_variational_minimal_observer

!python -m proof_lab.cut_variational_minimal_observer \
    --output proof_lab/CUT_VARIATIONAL_MINIMAL_OBSERVER_ACTUAL.json
```

Expected:

```text
Ran 6 tests
OK
PASS_CUT_VARIATIONAL_MINIMAL_OBSERVER_V0_1
```

## Byte-stable comparison

```python
from pathlib import Path

expected = Path(
    "proof_lab/CUT_VARIATIONAL_MINIMAL_OBSERVER_EXPECTED.json"
).read_bytes()
actual = Path(
    "proof_lab/CUT_VARIATIONAL_MINIMAL_OBSERVER_ACTUAL.json"
).read_bytes()
print("BYTE_STABLE", expected == actual)
```

Expected:

```text
BYTE_STABLE True
```

## Claim boundary

A pass certifies the universal cut-variational theorem and exact generalized calibrations. It does not prove that the completed-Weil adverse memory range has dimension five, does not construct the RH-specific observer, and does not prove RH.
