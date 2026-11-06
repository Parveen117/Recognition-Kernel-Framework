# PG64 — Companion review and implementation handoff

Monty · 6 November 2026

The checked companion head on `shaiva-sources-maheshvara-spanda-pratyabhijna` is `edd98b0685b478cb39468e350b26783bb4cce7ff`. T166 follows PG63's reviewed T165 head `bf1228fd5262baf9f3257de19547aab51eb260cc` directly. This review uses the new theorem and the relevant implementation rows as static sources. [T166 report](https://github.com/Parveen117/Recognition-Kernel-Framework/blob/edd98b0685b478cb39468e350b26783bb4cce7ff/theorum/166_rows_by_sutra_group_pusadi_mucadi_satva_theorem.md)

T166 reports 101 new divādi/tudādi entries and 334 Dhātupāṭha entries in its declared set. It introduced an ordered-entry check for puṣādi. The `dcode` state and the `PUSADI_FROM` range show how equal spellings in different slots can take different branches. T166 also records the two early entries and the two oracle-selected exclusions for source adjudication. Those results belong to Claude's declared run. PG64 uses the entry-order idea for a distinct svādi scope question, coupled to an explicitly chosen grammatical source.

At this head the previous ām observation is at line 532 of the tiṅ table. Its selection uses `AM_LIT`, `AM_SLU` or gaṇa 10 for liṭ. The row itself has no named KRM-ciri register or anekāc input. The table also has local ṇic-lopa and root-lengthening rows (lines 639 and 695). Their existence alone does not establish that the role- and source-qualified PG64 requests reach those rows. [Pinned implementation](https://github.com/Parveen117/Recognition-Kernel-Framework/blob/edd98b0685b478cb39468e350b26783bb4cce7ff/proof_lab/ting_rule_table_engine.py#L532)

| Handoff item | Required behavior and concrete acceptance pair |
| --- | --- |
| Register source | Match lexical ID **and** selected scope policy. Jiri under KRM 603 stays on its chāndasa branch. The reported ah-only reading in the Dhātukāvya commentary admits P11 in the aligned order. |
| Address the owner at yak | P2 basic **cirīyate**, P7 causal **cirāyyate**, P10 desire **cicirayiṣyate**. Preserve the causal role and the deleted ṇic owner. |
| Separate iṭ events | P5 **cirāyayiṣyati** has one outer iṭ. P9 **cicirayiṣiṣyati** also has a prior san-iṭ. Source disagreement on a printed participle has its own record. |
| Keep result and controller | The causal luṭ third singular coincides across P/A. At first singular compare **cirāyayitāsmi / cirāyayitāhe** across the two completed frames. |
| Bind the conditional | A counterfactual desire request specifies failure of the desire event. An impediment to the embedded injury alone leaves that request open. |
| Optional endings and accounting | Admit both u branches only at the six listed direct v/m contacts. Report 360 distinct request keys and 366 table readings. Quoted ṛkṣi forms have separate evidence status. |

The authored cells and their context keys are in [STATE.json](STATE.json). Grammar execution, generator comparison and certificate replay are deferred to implementation.
