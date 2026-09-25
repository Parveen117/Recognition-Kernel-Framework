# Singularity Calculus Theory v5 — General Normal-Crossing Complex

```text
STATUS: RNKE_VERIFIED_SINGULARITY_THEORY_V5_WITH_EXCLUSIONS
```

The v5 extension adds:

- **SC-16** — General Normal-Crossing Jump-Complex Theorem;
- **SC-17** — Total Stratified Differential Theorem;
- **SC-18** — General Realizability Obstruction and Jump Cohomology Theorem.

The central normal-crossing identity is

\[
\boxed{D_\Delta^2=0.}
\]

For a bigraded stratum complex whose internal differential commutes with the jump
maps, define

\[
\boxed{\mathbb D=d+(-1)^pD_\Delta.}
\]

Then

\[
\boxed{\mathbb D^2=0.}
\]

The general fail-closed realizability law is

\[
\boxed{
D_\Delta c\neq0
\Longrightarrow
c\notin\operatorname{im}D_\Delta.
}
\]

Passing \(D_\Delta c=0\) is necessary only. Global exactness is governed by the
jump cohomology class

\[
H^k_\Delta=\ker D_\Delta/\operatorname{im}D_\Delta
\]

and is not assumed.

## Verification

Validated theorem/proof head:

```text
6e113dec673920a9c201041542e125d26777025f
```

GitHub Actions run:

```text
31262484822
```

Results:

```text
legacy SC-01..SC-15 tests       23/23 PASS
general-complex tests            7/7 PASS
combined tests                   30/30 PASS
legacy exact controls               18 PASS
triple exact controls                3 PASS
general exact controls               6 PASS
combined exact controls             27 PASS
D_Delta^2 exact cases n=2..8        28 PASS
Python 3.11                        PASS
Python 3.12                        PASS
```

Negative controls also passed: wrong alternating signs, wrong totalization sign,
and corrupted derived packets are all detected.

## Freeze decision

The finite normal-crossing vertical development is now frozen at the general
complex level. Future Singularity Calculus work should not add bespoke formulas
for codimension four, five, and so on; those are instances of SC-16.

A new Singularity theorem should require genuinely new mathematics such as
nontransverse strata, infinite seam-family analysis, analytic convergence, or a
new domain adapter.

## Boundary

```text
FINITE TRANSVERSE NORMAL CROSSINGS          VERIFIED
D_DELTA^2 = 0                              PROVED
TOTAL DIFFERENTIAL mathbb D^2 = 0          PROVED UNDER DECLARED COMMUTATION
GENERAL NONREALIZABILITY GATE              PROVED
JUMP COHOMOLOGY                            DEFINED
ACYCLICITY                                 NOT CLAIMED
GLOBAL RECONSTRUCTION                      NOT CLAIMED
NONTRANSVERSE STRATA                       OPEN
INFINITE SEAM FAMILIES                     OPEN
AUTOMATIC PHYSICAL/TOPOLOGICAL MEANING     NOT CLAIMED
```
