# Admissible Sector Factorization and Composition-Primitivity

## Provenance

```text
source repository: Parveen117/MP
source PR: #54
source theorem: adapters/common/ADMISSIBLE_SECTOR_FACTORIZATION.md
```

## 1. Ordered sector datum

A finite hierarchy-resolved sector is an ordered list of segments carrying

```text
source hierarchy state
target hierarchy state
su(2) connection increment
winding increment
memory token.
```

Its path-ordered holonomy is

\[
U_\Sigma=e^{A_n}\cdots e^{A_1}.
\]

The hierarchy state contains both the base state and the active response depth.

## 2. Admissible-cut theorem

An interior cut is admissible only when it is a return to the complete hierarchy base state and both factors reconstruct all active data:

- the ordered segment word;
- path-ordered holonomy;
- winding lift;
- memory word;
- seam-dagger transport;
- local curvature ledgers;
- cross-factor curvature memory.

For an admissible cut \(k\),

\[
U_\Sigma=U_{\mathrm{right}}U_{\mathrm{left}},
\]

\[
\nu(\Sigma)=\nu(\mathrm{left})+\nu(\mathrm{right}),
\]

and the memory words concatenate in order.

The full curvature ledger obeys

\[
\boxed{
\mathcal C(\Sigma)=
\mathcal C(\mathrm{left})
\sqcup
\mathcal C(\mathrm{right})
\sqcup
\mathcal C_{\mathrm{cross}}.
}
\]

The cross term retains commutators between segments lying on opposite sides of the cut. A decomposition that reproduces the endpoint matrix but discards this history is not admissible.

## 3. Composition-primitivity theorem

Within the declared finite ordered-word category,

\[
\boxed{
\Sigma\text{ is composition-primitive}
\iff
\text{there is no nontrivial intermediate return of the full hierarchy state}.
}
\]

A sector may be representation-irreducible but composition-composite. Thus irreducibility cannot substitute for the return-cut theorem.

## 4. Gauge invariance

Under constant \(SU(2)\) conjugation,

\[
A_j\mapsto GA_jG^{-1},
\qquad
U_\Sigma\mapsto GU_\Sigma G^{-1}.
\]

Hierarchy returns, winding, memory order, admissible cuts, and composition-primitivity remain unchanged. Curvature channels transform covariantly.

## 5. Tamper-rejection theorem

A proposed factorization is rejected if it:

- alters winding or memory data;
- cuts at a state that is not a complete hierarchy return;
- omits the cross-curvature ledger;
- reconstructs only the endpoint holonomy while losing ordered source history.

## 6. Preliminary positive length

The source records

\[
L_{\mathrm{act}}(\Sigma)=\sum_j\|A_j\|.
\]

It is positive, constant-gauge invariant, and additive across admissible macro cuts. At PR #54 it remains a candidate because subdivision and reparameterization invariance have not yet been proved.

## Claim boundary

```text
ADMISSIBLE COMPLETE-STATE RETURN CUT       PROVED
ORDERED HOLONOMY FACTORIZATION            PROVED
WINDING AND MEMORY RECONSTRUCTION         PROVED
CROSS-FACTOR CURVATURE REQUIREMENT        PROVED
COMPOSITION-PRIMITIVITY CRITERION         PROVED IN FINITE WORD CATEGORY
GAUGE INVARIANCE OF CUT SET               PROVED
TAMPERED FACTORIZATIONS                   REJECTED

REFINEMENT-STABLE LENGTH                  OPEN AT THIS STAGE
CONTINUUM FACTORIZATION                   OPEN AT THIS STAGE
ARITHMETIC PRIMALITY                      NOT IMPLIED
```
