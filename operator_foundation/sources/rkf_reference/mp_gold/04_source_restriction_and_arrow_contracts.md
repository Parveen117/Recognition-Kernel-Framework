# MP Gold 04: Source Restriction, Minimal Lift and Arrow Contracts

## Source PRs

```text
MP PR #204  Prove recognition source-restriction and minimal-lift theorem
MP PR #205  Add machine-readable RH proof graph and arrow contracts
```

## Why this is gold

These results are not the final RH proof, but they are governance gold. They stop finite packets from being promoted through hidden blind kernels. They also force every proof arrow to declare its domain, codomain, source restriction and terminal status.

## Source-restriction rank formula

For a rich split representation `S(q)P` and consumed source restriction `B`, define

```text
A(q) = B S(q) P,
S(q) = sum_s q^s D_s.
```

The exact all-parameter rank is

```text
rank vertical_stack_s(B D_s P),
```

and the exact blind kernel is

```text
intersection_s ker(B D_s P).
```

If

```text
S(q)=qI+O(q^2)
```

and `P` is injective, then the rich split representation is generically complete. Any blind kernel of the collapsed map is typed as a source-restriction defect rather than automatically blamed on the target.

## Minimal lift theorem

For supplemental scalar observations `G`, the augmented map is injective exactly when

```text
ker A intersect ker G = {0}.
```

Thus at least

```text
dim ker A
```

scalar supplemental observations are necessary. The target-relative version only requires the residual kernel to lie inside the target kernel.

## Degree-five calibration

The degree-five packet has

```text
formal coordinates  50
collapsed rank      45
blind dimension      5.
```

Five split probes restrict to the blind basis through a matrix with determinant

```text
-2592.
```

Therefore five probes repair the full defect and four cannot.

## Machine-readable arrow contract

Every consumed arrow must declare:

```text
id
source / target
domain / codomain
lawful nullspace
source module
source restriction
blind kernel
target relevance
target map
decoder or lift
path relations
completion topology
uniform margin
claim status
```

The validator rejects:

```text
type mismatches;
source restriction without blind kernel;
target-relevant blind kernel without lift;
completed arrow without certified positive margin;
false terminal promotion.
```

## Reuse in RKF

Use this as the proof-governance layer for all future theorem chains. Every finite capsule, source readout, endpoint projection or seam matrix must declare its blind kernel and lift before being treated as target-faithful.

## Claim boundary

```text
general source-restriction rank formula       PROVED
general blind-kernel formula                  PROVED
minimal scalar lift theorem                   PROVED
degree-five five-probe lift                   EXACTLY CALIBRATED
machine-readable arrow schema                 PROVED
typed graph validator                         PROVED
terminal blocker ledger                       PROVED FOR DECLARED GRAPH
RH terminal signs                             NOT PROVED HERE
```
