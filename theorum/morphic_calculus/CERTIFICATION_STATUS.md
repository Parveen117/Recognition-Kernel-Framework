# Morphic Calculus Certification Status

## Source identity

- uploaded source: `Morphic calculus complete(1).tex`
- SHA-256: `ccc376bd423bb7266f9d66c2fb163596d35373f92790666767d60a01d115ffc1`
- theorem environments observed in the source audit: 12
- axiom environments observed in the source audit: 0

## Verification rule

The manuscript is not certified merely because exact examples or software tests pass.

For transfer into the verified publication surface, use four gates:

1. **source integrity** — exact source hash and provenance;
2. **LaTeX integrity** — clean deterministic build after non-semantic repairs;
3. **mathematical obligation audit** — every theorem and major derived claim classified;
4. **RNKE proof contract** — exact obligations plus negative controls, hash-bound and reproducible.

## Current gate table

| Gate | Status | Note |
|---|---|---|
| source identity | PASS | exact SHA pinned |
| terminology preservation | PASS/REQUIRED | Recognition, Śūnya, Cut, Morphic/Morphisum, clock and measure terminology retained |
| raw-source compile | FAIL | unconfigured Unicode `⇒` encountered after the source reaches the body |
| non-semantic compile repair | OPEN | repair must preserve visible terminology/equations |
| theorem obligation extraction | OPEN | 12 theorem environments require classification |
| flat-clock claim audit | OPEN | distinguish unresolved rate from native closure |
| RNKE full-manuscript contract | OPEN | not issued |
| verified `main.tex` transfer | BLOCKED | waits on certification gates |

## Relation to the new MR branch

MR-01 through MR-03 consume ideas from Morphic Calculus and Morphic Algebra only after restating them under explicit assumptions and proof contracts. Their successful RNKE certificate does **not** certify the complete historical Morphic Calculus manuscript.

The verification process changes proof status, not the native terminology.
