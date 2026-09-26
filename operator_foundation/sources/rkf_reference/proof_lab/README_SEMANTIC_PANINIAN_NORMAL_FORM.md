# Typed Semantic Paninian Normal Form, Stage 1

This stage introduces the first executable semantic carrier in the Recognition Kernel Framework.

It consumes **explicitly typed claims**, not unrestricted prose. The carrier preserves:

- surface text;
- subject, predicate, and object keys;
- polarity;
- time anchor;
- modality;
- grammatical markers;
- semantic/effect tags;
- precedence context;
- full rewrite and ledger history.

The normalization order is source-pinned to the Vedic repository:

1. ordered alias rewrites;
2. relation/type precedence guard;
3. explicit Bindu selection only for residual ambiguity;
4. seam-ledger capture;
5. grammatical Lopa of non-surface markers.

The stage distinguishes:

- canonical identity;
- left-to-right ontology entailment;
- right-to-left ontology entailment;
- polarity contradiction;
- time contradiction;
- functional-target contradiction;
- incomparability;
- unresolved ambiguity.

It deliberately does **not** certify truth, evidence, policy applicability, or unrestricted language understanding. Those require the later Nyaya, Mimamsa, Yukti, and semantic no-blindness gates.

## Reproduce

```bash
python -m proof_lab.semantic_paninian_normal_form \
  --output proof_lab/SEMANTIC_PANINIAN_NORMAL_FORM_ACTUAL.json
python -m unittest -v proof_lab.test_semantic_paninian_normal_form
```

Expected status:

```text
PASS_TYPED_SEMANTIC_PANINIAN_NORMAL_FORM_STAGE1
```

## Demonstrated controls

The fixture deliberately separates the following cases:

- `1889 World's Fair` and `1889 Universal Exposition`: canonical identity after alias normalization;
- `1889 World's Fair` and `exhibition`: entailment, not identity;
- `1889` and `1888`: typed time contradiction;
- positive and negated claims: polarity contradiction;
- `fair` without a selector: ambiguous Bindu and fail-closed normalization.

This is the carrier and normal-form stage only. The next stage is the Nyaya support/defeat route kernel.
