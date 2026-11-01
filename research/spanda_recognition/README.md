# SP1: cyclic return, transported Smriti and an observable event count

Author: Monty. 1 November 2026.

The motivating question is whether a dance returning to the same visible pose
has also returned to the same retained state. Shiva's dance, Spanda and
Pratyabhijna suggest questions about activity, identity and recognition;
[SOURCES.md](SOURCES.md) records their actual textual contexts separately from
the mathematical construction.

The declared loop acts on Smriti by `m -> H m + b`. Its lasting translation is
the class of `b` in `M / im(I-H)`, rather than the raw increment `b`.

- A memory reset exists exactly when that class is zero.
- Over a rational algebra, a nonzero class rules out every finite-period
  memory state. A nonzero raw increment alone does not: `m -> -m+b` returns
  after two cycles and has fixed point `b/2`.
- On a finite cut-field carrier, a nonzero class supplies a scalar event count.
  An existing observer can read such a count exactly when its available rows
  include a suitable invariant covector. Existence and observability differ.
- All constructions commute with the declared zero-specialization. Nevertheless,
  that specialization can erase the obstruction and its event count.

An explicit full-family example has a four-step quarter-turn return on the
source and transported memory

\[
m_n=n\varepsilon e_2+\binom n2\varepsilon^2e_1,
\qquad \varepsilon^3=0.
\]

The source returns after each cycle. Memory retains both a cycle count and a
quadratic record. The first component looks unchanged after the first cycle,
then reveals the accumulated history. Its zero-specialization is stationary.
The coefficient of `epsilon` in the second component reads the count without
dividing by a nilpotent element. No physical duration is assigned.

Read [THEOREM.md](THEOREM.md) for six proof groups, the full native contract,
the example and the distinction between a repeatable state and literal word
history. [SCOPE.md](SCOPE.md) records assumptions and open work;
[VALIDATION.md](VALIDATION.md) records checks actually performed.

From the repository root:

```bash
python3.12 research/spanda_recognition/check_examples.py
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

This is an additive RKF research specialization of established affine-action,
quotient and observability mathematics. MR-03's central two-cocycle extension,
MR-04's future-complete observer and SE41's calibration law remain distinct
predecessors. The new packet connects transported cycle memory, reset
obstruction, observer access and a specialization that hides the count. It
does not replace the operator engine or assert external novelty.
