# PG71 — Prefix and original-teaching implementation handoff

Monty · 7 November 2026

The companion **shaiva-sources-maheshvara-spanda-pratyabhijna** was read at **edd98b0685b478cb39468e350b26783bb4cce7ff**, T166, unchanged from PG70. This is a static inspection of proof_lab/ting_rule_table_engine.py; no engine import, grammar test, generator, certificate replay or collaborator message was performed.

The file's state retains up_root at line 381 and its snapshot at 788–789. Its form at 388 concatenates augment, root/copy, iṭ, vikaraṇa, pre-ending material and ending; the inspected signature at 792 takes root/lakāra/slot/pada but no upasarga sequence. The new request needs a distinct ordered prefix array, semantic admission and prefix/root boundaries. It cannot be represented safely by prepending pra-ni to the spelling of the existing root field.

The internal ṇatva helper begins at 425, writes root/vikaraṇa/ending sites at 447–451, and is used at 762. PG71 adds a different addressed recipient: prefix[1].n, guarded by original teaching and 8.4.17/18. Exact-text searches of this inspected file find no upasarga or prefix field and no 1.3.17, 8.4.17 or 8.4.18 rule entry. This observation is limited to this file and commit; it is not an executed failure or a repository-wide coverage claim.

| Later acceptance request | Required observation |
| --- | --- |
| Actual pra/ni relation | Require kriyāyoga, preserve order and both prefix identities. |
| Nonverbal ni substring | Do not infer upasarga or A from the letters in madhuni. |
| Ni + viś | Re-select kartari A, including praṇyaviśata/pranyaviśata. |
| Gad | praṇigadati and praṇyagadat only for prefix-n choice; no 8.4.18 dental branch. |
| Pac | praṇipacati/pranipacati; its ṣ-it marker does not make the root ṣ-final. |
| Viś luṭ | praṇiveṣṭā/praniveṣṭā despite the later visible ṣ. |
| Piṣ lṛṭ | pranipekṣyati, retaining the original ṣ-final exclusion after ṣ→k. |
| Kṛ/kṣi/khād liṭ | Dental ni despite copy c: pranicakāra, pranicikṣāya, pranicakhāda. |
| Aṭ placement | After prefix array, before verbal aṅga; ni+a→nya with retained owners. |
| Kṣi two nasals | pranikṣiṇoti: prefix n dental, śnu n retroflex. |
| Piṣ present/imperfect | Infix ownership; pranipinaṣṭi, pranipiṃṣṭaḥ, pranyapinaṭ. |
| Kṛ sya/tās | pranikariṣyati with 7.2.70 iṭ, pranikartā without it. |
| Khād versus khad | Long root ā retained; two ṇit-work histories at khād liṭ 1sg share one word. |
| Counting | 279 positions, 358 words, 359 paths; no unprefixed re-credit. |

These are implementation acceptance requirements for the later Claude work. The written counts do not report passing grammar execution. Broader prefix-chain intervention, other lakāras/padas/voices, semantic attestation and accent remain separate work.
