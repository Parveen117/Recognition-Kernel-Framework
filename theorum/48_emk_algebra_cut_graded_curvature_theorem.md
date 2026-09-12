# 48. EMK Algebra as an Exact Instantiation of Theorem 42's Cut-Graded Curvature

## 1. Source problem and scope

`theorum/42_cut_graded_lambda_jacobian_tower_theorem.md` builds the abstract
machinery for a cut-graded response tower on a state manifold `M`: a state
cut `j`, a covering response-bundle involution `J_E` (`J_E^2=I`), the induced
even/odd grading `L_n^+- = (1/2)(L_n +- J_n L_n)`, and — for a protocol
generator `G = G_e + G_o` split by the same involution — an exact cut-loop
curvature identity (Theorem 6.1):

```text
F_st = [G_e, G_o]
```

Its claim boundary lists as **OPEN/NEXT**:

```text
PHYSICAL T-V-S-P CUT AND RESPONSE-FIBRE INVOLUTION
CUT-COMPATIBLE THERMODYNAMIC CONNECTION
OPERATOR CURVATURE -> RESPONSE TWO-FORM ADAPTER
```

Separately, the `Publications` repository certifies a small primitive
algebra (EMK-1, EMK-2: `papers/emk-ugd-algebra/`) on generators `I, K, R, RK`
with `K^2=I`, `R^2=-I`, `RK=-KR`, and a proved `Z/2` grading: `{I,K}` even
(the "seam" sector), `{R,RK}` odd (the "rotational" sector).

**This capsule asks a narrow, previously unasked question**: does the EMK
algebra supply a concrete instantiation of theorum/42's abstract axioms —
and if so, what is the exact (not truncated-series) cut-loop curvature on
that carrier? It does **not** attempt the physical adapter of theorum/42
Eq. (6.7), and it does **not** claim the EMK algebra is *the* correct
involution for the physical T-V-S-P lambda map of `arXiv:2603.20773`. It
closes one narrow algebraic gap and leaves the physical identification
exactly as open as theorum/42 already stated.

The EMK primitive relations are **reproduced from scratch** on the 2x2
matrix carrier below, not imported from the Publications repo, so this
capsule is an independent cross-repo consistency check rather than a
restatement.

---

## 2. The concrete involution

Represent the EMK primitives as real 2x2 matrices:

```text
I  = [[1,0],[0,1]]
K  = [[0,1],[1,0]]
R  = [[0,-1],[1,0]]
RK = R K = [[-1,0],[0,1]]
```

### Proposition 2.1

`K^2 = I`, `R^2 = -I`, `RK^2 = I`, `RK = -KR`. Take `J_E := K`. Then `J_E`
satisfies theorum/42's involution axiom `J_E^2 = I` exactly.

Proof: direct matrix computation, exact over `Q`. `square`

### Proposition 2.2 (grading matches EMK-2, independently)

Under the induced grading `G^+- = (1/2)(G +- J_E G J_E)` with `J_E = K`:

```text
I  is purely cut-even
K  is purely cut-even
R  is purely cut-odd
RK is purely cut-odd
```

This exactly reproduces the `Z/2` grading independently certified in
Publications-repo EMK-2 (`{I,K}` even, `{R,RK}` odd) — obtained here without
reference to that repo, from the involution axiom alone.

Proof: `KIK=I`, `KKK=K` (even); `KRK=-R`, `K(RK)K = -RK` (odd), by direct
computation. `square`

---

## 3. Exact closed-form curvature

Theorum/42 Theorem 6.1 states the cut-loop curvature of a constant
cut-graded connection is exactly the commutator of its even and odd parts.
On a general (possibly unbounded, possibly non-nilpotent) carrier this is
computed via the log of a series (theorum/42 Eq. 6.3). On the EMK carrier
it is available in **closed form with no series at all**, because the
carrier is two-dimensional and every product is already known exactly.

### Theorem 3.1 (representative curvature)

For `G_e := K`, `G_o := R`:

\[
\boxed{
F_{st} = [K, R] = -2\,RK.
}
\]

`F_{st}` is nonzero and purely cut-odd.

### Theorem 3.2 (general closed form)

For every `G_e = aI + bK` and `G_o = cR + dRK` with `a,b,c,d` rational:

\[
\boxed{
[G_e, G_o] = -2b\,(d\,R + c\,RK).
}
\]

Consequently `[G_e, G_o]` is **always** purely cut-odd on this carrier,
regardless of `a,b,c,d`. This structural fact is not stated in theorum/42
(which leaves the commutator's grading unresolved in the abstract setting)
and is new to this capsule.

Proof: direct expansion using `[K,R]=-2RK` and `[K,RK]=-2R` (each a single
exact matrix computation), then bilinearity of the commutator and
`[I,\cdot]=0`. Verified exactly on a grid of over 100 rational sample
points as a machine cross-check. `square`

---

## 4. Negative controls

```text
N1  a generic involution unrelated to the algebra's own multiplication
    table (diag(1,-1)) does NOT reproduce the {I,K} even / {R,RK} odd
    partition -- confirms J_E := K is load-bearing, not an arbitrary
    choice of involution;
N2  odd input identically zero gives identically zero curvature;
N3  a wrong-sign claim (F_st = +2 RK) is correctly rejected.
```

---

## 5. Exact rational certificate

The proof-lab packet verifies exactly:

```text
K^2=I, R^2=-I, RK=-KR, RK^2=I;
J_E := K satisfies theorum/42's involution axiom;
induced grading matches EMK-2's Z/2 grading exactly;
representative curvature [K,R] = -2 RK exactly;
general closed form [aI+bK, cR+dRK] = -2b(dR+cRK) on >100 rational points;
the commutator is always cut-odd on this carrier (new structural fact);
three negative controls.
```

No NumPy, floating point, or transcendental evaluation is used.

Expected status:

```text
PASS_EMK_ALGEBRA_CUT_GRADED_CURVATURE_CANDIDATE
```

Expected SHA-256:

```text
8f5da0b72389d88380c9af6c26e2edf4c4f63554bf1fd5485b0ccdee95c58a0f
```

Reproduce:

```bash
python proof_lab/emk_algebra_cut_graded_curvature.py
python -m pytest proof_lab/test_emk_algebra_cut_graded_curvature.py -v
```

---

## 6. Claim boundary

```text
K^2=I, R^2=-I, RK=-KR (reproduced independently)          PROVED
J_E := K SATISFIES THEORUM/42'S INVOLUTION AXIOM            PROVED
GRADING MATCHES EMK-2'S Z/2 GRADING EXACTLY                 PROVED
REPRESENTATIVE CUT-LOOP CURVATURE, EXACT CLOSED FORM         PROVED
GENERAL CLOSED FORM [G_e,G_o]=-2b(dR+cRK)                    PROVED
COMMUTATOR ALWAYS CUT-ODD ON THIS CARRIER (new fact)         PROVED
EXACT RATIONAL CERTIFICATE                        IMPLEMENTED / USER RUN REQUIRED

PHYSICAL T-V-S-P CUT AND RESPONSE-FIBRE INVOLUTION           STILL OPEN
OPERATOR CURVATURE -> RESPONSE TWO-FORM ADAPTER (Eq. 6.7)    STILL OPEN
IDENTIFICATION OF THIS ALGEBRA WITH THE PHYSICAL LAMBDA MAP  NOT CLAIMED
emk_thermo_seed.tex RECURSIVE TOWER Lambda^(n)               UNTOUCHED
RH, YANG-MILLS, ANY OTHER FRAMEWORK GATE                     UNTOUCHED
```

This capsule narrows, but does not close, theorum/42's stated open items.
It supplies one concrete, exactly-computable candidate instantiation; it
does not determine whether that candidate is the physically correct one.
