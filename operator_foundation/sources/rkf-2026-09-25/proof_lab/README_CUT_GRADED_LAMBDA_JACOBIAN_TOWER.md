# Cut-Graded Lambda-Jacobian Tower Candidate

This stacked development applies the certified cut-graded universal generator
to the recursive thermodynamic response structure of `arXiv:2603.20773v2`.

## Added

```text
theorum/42_cut_graded_lambda_jacobian_tower_theorem.md
proof_lab/cut_graded_lambda_jacobian_tower.py
proof_lab/test_cut_graded_lambda_jacobian_tower.py
proof_lab/CUT_GRADED_LAMBDA_JACOBIAN_TOWER_EXPECTED.sha256
proof_lab/README_CUT_GRADED_LAMBDA_JACOBIAN_TOWER.md
```

## Jupyter run

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch agent/cut-graded-lambda-jacobian-tower
!git pull --ff-only origin agent/cut-graded-lambda-jacobian-tower

!python -m unittest -v proof_lab.test_cut_graded_lambda_jacobian_tower

!python -m proof_lab.cut_graded_lambda_jacobian_tower \
    --output proof_lab/CUT_GRADED_LAMBDA_JACOBIAN_TOWER_ACTUAL.json
```

Expected:

```text
Ran 10 tests
OK

PASS_CUT_GRADED_LAMBDA_JACOBIAN_TOWER_CANDIDATE
RECURSIVE_TOWER True
JACOBIAN_BIGRADING True
CONNECTION_CURVATURE True
TOWER_OBSERVER True
RANK_CHANGE_CUT True
CERTIFICATE_SHA256 3d8db4f085a3b624192c45b9f6e0356b600834193967bc89478381b53ae44a3a
```

## Hash check

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/CUT_GRADED_LAMBDA_JACOBIAN_TOWER_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/CUT_GRADED_LAMBDA_JACOBIAN_TOWER_ACTUAL.json"
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

## Boundary

A pass certifies the abstract cut-graded tower, Jacobian bi-grading, constant
connection curvature calibration, finite observer repair, and rank-change
negative controls. It does not prove that the physical lambda map in the
source paper is globally antisymmetric or that its curvature already equals
entropy production.
