# PG66 — Implementation handoff at the unchanged T166 head

Monty · 7 November 2026

The companion branch `shaiva-sources-maheshvara-spanda-pratyabhijna` remains at **`edd98b0685b478cb39468e350b26783bb4cce7ff`**, T166, on the current remote read. Reuse the pinned PG64/65 report. The addressed engine text was read statically for this handoff; no grammar execution, generator comparison or certificate replay was performed.

## Current row boundary

At the pinned `proof_lab/ting_rule_table_engine.py`, line 515's 3.1.48 row selects caṅ from its gaṇa-10/current-affix state. Line 643's 7.4.94 row checks the copy and initial root vowel and then lengthens. Those predicates do not themselves encode PG66's M/K source-interpretation certificate. The new request must retain that certificate before either short or long copy is accepted. A current row's presence alone is not a completed reachability or source-policy proof.

The inspected `add` row declarations did not contain exact rule IDs 3.1.66, 6.4.62 or 6.4.104. This is a narrow observation about that row surface, not a claim that no related behavior exists elsewhere. PG66 requires the actual-ciṇ/ordinary-sic split and the separately owned O/C transport to be exposed in implementation evidence.

## Acceptance contracts for later execution

| Request | Required result or distinction |
| --- | --- |
| Ciri causal kartari luṅ P3sg, M versus K | **acicirayat** versus **acīcirayat**, with the chosen commentary certificate retained. |
| Jiri causal kartari luṅ A1sg, M versus K | **ajijiraye** versus **ajījiraye**; no iṭ, no san desire event. |
| Ciri causal kartari versus karmaṇi luṅ, 3sg | The M/K caṅ forms versus actual-ciṇ **acirāyi**. Voice selects the affix path before ending readout. |
| Basic ciri karmaṇi lṛṭ 3sg, O versus C | **cirayiṣyate / cirāyiṣyate**, ordinary guṇa versus transported ciṇ grade. |
| Causal ciri karmaṇi lṛṭ 3sg, O versus C | **cirāyayiṣyate / cirāyiṣyate**, retained versus lopped ṇic with distinct iṭ visibility. |
| San ciri karmaṇi lṛṭ 3sg, O versus C | Same word **cicirayiṣiṣyate**, two retained outer-iṭ histories, one spelling count. |
| Basic/causal ciri karmaṇi luṅ 3sg | **acirāyi** in both formations, one actual-ciṇ path each; patient/causal histories stay different. |
| San ciri karmaṇi luṅ 3sg versus 1sg | **acicirayiṣi** versus **acicirayiṣiṣi**; actual ciṇ-i versus the separate sic/iṭ/ending-i sequence. |
| Basic ciri karmaṇi luṅ 2pl | Four O/C × dh/ḍh spellings, with each augment and late sound choice addressed. |
| San ciri karmaṇi luṅ 2pl | **acicirayiṣidhvam**, two O/C histories; ṣ before the outer iṭ supplies no iṇ-triggered ḍh branch on the adopted policy. |
| San ciri karmaṇi blessing 3sg versus 3du | **cicirayiṣiṣīṣṭa / cicirayiṣiṣīyāstām**; suṭ after ī versus after ā. |
| Causal caṅ with an unspecified interpretation outside the declared family | Preserve an explicit source-policy request; do not choose copy length from a surface-only default. |

## Delivered boundary

The complete [register](STATE.json) contains 306 admitted request positions, 534 distinct spellings within positions and 622 paths across the expressly modelled branches. The new [derivation](DERIVATIONS.md) resolves PG65 H08 for the named M/K interpretations and supplies the passive branches. Runtime validation remains assigned to implementation. Wider source consensus, Vedic/accent coverage, remaining derived perfect/blessing domains and ṛkṣi admission remain separately tracked.
