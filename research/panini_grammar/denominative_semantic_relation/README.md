# PG133 — From a Sanskrit clause to a formal predicate

Monty · 11 November 2026

The word **putrīyati** can express wanting a son or treating someone like a son. In **putrīyati chātram** the attached patient binds that second participant to the pupil. Conversely, the first meaning also admits **putrakāmyati**. [RELATION.json](RELATION.json) stores both directions as typed arguments and literal source witnesses. It references the previously written finite-word records and adds zero position credit.

| Supplied input | Result in the selected relation |
| --- | --- |
| putrīyati | WANT_FOR_SELF(x, son, x) or TREAT_AS(x, z, son) |
| putrīyati chātram, with patient attachment | TREAT_AS(x, pupil, son) |
| WANT_FOR_SELF(x, son, x) | putrīyati or putrakāmyati |
| prāsādīyati kuṭyām | ACT_IN_AS_IF(x, hut, palace) |
| kumudaṃ puṣkarāyate | BEHAVE_LIKE(kumuda, puṣkara) |
| udaka with drinking/thirst specified | THIRST(x), read out as udanyati |
| udaka for bathing or irrigation | WANT_FOR_SELF(x, water, x), read out as udakīyati |

The table translates the relations to English for readability. Machine constants retain their Sanskrit lemmas. There are 7 predicate signatures, 15 source-backed lexical analyses, 14 finite-word spellings and 11 named queries. See the [domain and proof](DOMAIN_AND_NATIVE.md) and [source fields](SOURCE_EXCERPTS.json).
