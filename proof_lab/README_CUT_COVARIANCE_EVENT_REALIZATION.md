# Cut-Covariance Event Realization v0.1

This stage derives the source second moment, boundary first moment and signed
covariance from one native event lift.

## Native chain

```text
native event lift Z
-> unit boundary event state p_partial
-> source S = Z*Z
-> boundary ell = p_partial* Z
-> cut memory M = (I-p_partial p_partial*) Z
-> covariance W = M*M = S-ell*ell
-> target observer only after cut-memory faithfulness.
```

## Exact calibrations

```text
1. one event lift generates source, boundary and covariance;
2. least-energy decoder burden is exactly 1/6;
3. memory rank is five and boundary-line blindness is absent;
4. beta_n=n/(n+1) approaches one while every finite packet remains strict;
5. correct rank-five observer action is zero;
6. wrong rank-five orientation action is 81/100;
7. an independently perturbed boundary row fails the covariance identity;
8. first moments, second moments and covariance converge under one orientation.
```

No RH data is used.

## Run in Jupyter

```python
%cd "C:\Users\abc\Desktop\New Folder (2)\New folder\PROVISNAL RELATED\RH framework\Recognition-Kernel-Framework"

!git fetch origin
!git switch agent/cut-memory-spectral-isomorphism
!git pull --ff-only origin agent/cut-memory-spectral-isomorphism

!python -m unittest -v proof_lab.test_cut_covariance_event_realization

!python -m proof_lab.cut_covariance_event_realization \
    --output proof_lab/CUT_COVARIANCE_EVENT_REALIZATION_ACTUAL.json
```

Expected:

```text
Ran 7 tests
OK
PASS_CUT_COVARIANCE_EVENT_REALIZATION_V0_1
```

## Canonical certificate hash

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/CUT_COVARIANCE_EVENT_REALIZATION_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual_bytes = Path(
    "proof_lab/CUT_COVARIANCE_EVENT_REALIZATION_ACTUAL.json"
).read_bytes()

actual = sha256(actual_bytes).hexdigest()
print("HASH_STABLE", expected == actual)
print("EXPECTED", expected)
print("ACTUAL  ", actual)
```

Expected:

```text
HASH_STABLE True
```

## Claim boundary

A pass proves the universal cut-covariance mechanism and the exact generalized
calibrations. It does not yet construct the native completed-Weil event lift,
identify the completed-Weil boundary event, prove completed-Weil no-blindness,
or prove RH.

The next domain stage is to build `Z_Weil_minus` coefficientwise from prime,
Gamma, completion-boundary and compatibility cut events, without defining it
from the desired signed form.
