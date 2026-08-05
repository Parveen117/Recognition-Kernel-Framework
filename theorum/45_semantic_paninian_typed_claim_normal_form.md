# 45. Typed Semantic Paninian Normal-Form Theorem

## Status

`PROVED_FOR_EXPLICIT_FINITE_PRESENTATION`

This theorem concerns an explicitly supplied finite semantic presentation. It does not claim unrestricted natural-language parsing or historical truth.

## Carrier

A typed claim is

\[
C=(x,s,p,o,\epsilon,\tau,\mu,M,E,\pi,h),
\]

where:

- \(x\) is surface text;
- \(s,p,o\) are subject, predicate, and object keys;
- \(\epsilon\in\{+1,-1\}\) is polarity;
- \(\tau\) is an optional time anchor;
- \(\mu\) is modality;
- \(M\) is the marker set;
- \(E\) is the effect-tag set;
- \(\pi\) is precedence context;
- \(h\) is an optional explicit Bindu hint.

A finite semantic presentation supplies alias relations, entity types, ontology-parent edges, relation type guards, functional-target declarations, and source pins.

## Normalization order

The semantic normal form is computed in the order

\[
\boxed{
\text{ordered rewrite}
\to
\text{precedence/type guard}
\to
\text{residual Bindu selection}
\to
\text{seam ledger}
\to
\text{grammatical Lopa}.
}
\]

No ambiguous alias is silently selected. Markers are captured in the ledger before Lopa erasure.

## Theorem

Let \(P\) be a finite semantic presentation with deterministic singleton alias rules, explicit guarded Bindu selectors for every admitted ambiguous rule, an acyclic finite ontology relation, and total relation type specifications on the admitted carrier.

Then the Paninian semantic normalizer

\[
\operatorname{NF}_P:C\to \widehat C\cup\{\mathrm{OPEN}\}
\]

is deterministic. Moreover:

1. alias-equivalent surfaces normalize to the same canonical claim;
2. ontology specialization remains distinguishable from canonical identity;
3. polarity and non-overlapping time anchors remain visible coordinates;
4. unresolved ambiguity maps to `OPEN`, not to an invented canonical state;
5. Lopa erasure cannot remove ledgered derivational evidence.

## Proof

Each stage is deterministic on its declared domain.

- Singleton alias rules have a unique image.
- Ambiguous rules have no image unless the supplied Bindu hint names one admitted candidate.
- Relation type guards are Boolean and total on the admitted carrier.
- The finite ontology transitive closure is deterministic.
- Ledger capture is append-only before marker erasure.

Composition of these deterministic stages is deterministic. Alias-equivalent surfaces therefore share canonical coordinates. Ontology parenthood is stored as an order relation rather than equality, so entailment cannot become identity. Polarity and time are retained in the canonical carrier and are therefore not erased by surface normalization. An unresolved alias never reaches a canonical object, establishing fail-closed ambiguity. Finally, every erased marker has a prior ledger entry, so grammatical Lopa cannot destroy the derivation witness.

## Claim boundary

Proved here:

- deterministic normalization for the explicit finite presentation;
- identity/entailment separation;
- typed polarity and time contradiction channels;
- fail-closed ambiguity;
- ledger-before-Lopa preservation.

Still open:

- unrestricted natural-language parsing;
- Nyaya evidential support and defeat;
- Mimamsa context and priority;
- Yukti proof transport;
- injectivity of the complete semantic observer;
- truth certification.

## Executable witness

- `proof_lab/semantic_paninian_types.py`
- `proof_lab/semantic_paninian_normalizer.py`
- `proof_lab/semantic_paninian_normal_form.py`
- `proof_lab/test_semantic_paninian_normal_form.py`
- `proof_lab/imported/SEMANTIC_PANINIAN_SOURCE_PINS.json`
- `proof_lab/SEMANTIC_PANINIAN_NORMAL_FORM_EXPECTED.sha256`
