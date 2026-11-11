# PG174 · Two Sanskrit dictionaries indexed against all 748 Uṇādi records

Monty · 11 November 2026

Apte’s *Practical Sanskrit-English Dictionary* and Monier-Williams’s *Sanskrit-English Dictionary* supply 1,797 explicitly tagged Uṇādi references in the two pinned Cologne transcriptions. Each is recorded with its dictionary, entry number, headword, page, and exact tag interval. The 748-row coverage table joins these references to the five-pāda grammar by their printed numbers. A tag belongs to a dictionary article, which can also discuss variants, other words and alternative analyses.

| Coverage in this Uṇādi edition | Number of rules |
| --- | ---: |
| At least one single, in-range rule number | 602 |
| Only a grouped locator, such as a range or slash pair | 6 |
| No in-range locator in these two tagged reference sets | 140 |
| **Total** | **748** |

For 171 rules a narrower check finds a single-number reference whose headword also occurs as an exact graphic token in the primary commentary. The table gives the character offsets of every such token. This is a reproducible text comparison. A homonym or a word in an explanatory gloss still needs lexical review. Sandhi, inflection and accent can prevent a literal match. The 140 rows without a pointer have their Sanskrit source text and commentary in PG172’s edition.

### Why a matching rule number needs a word check

Apte’s *yayuḥ* entry L26928 points to 1.21, where the commentary gives the sacrificial horse. The *babhru* entry L24440 also cites 1.21 in an alternative derivation. In the pinned Uṇādi text *babhru* is discussed at 1.22, while 1.21 concerns *yayu*. Both dictionary locators are preserved as printed. This discrepancy gives no basis for moving every subsequent dictionary reference by one. By contrast, *valgu* at L28701 points to 1.19; PG173 also located the dictionary’s cited poem word.

An abbreviated tag can inherit the dictionary name and part of its address from its own `n` attribute. The index retains that attribute. Explicit single numbers, inclusive hyphen ranges, slash pairs and comma lists have separate statuses. A trailing short range endpoint such as 155–6 expands to 155–156. A chapter without a rule, an isolated rule number without a chapter, a commentary-only reference, and a number outside this edition receive no single-number credit. They remain visible in the reference table.

Offsets for a dictionary tag are zero-based Unicode code-point intervals relative to the literal start of its `<L>` entry. A single period in the TSV marks an empty field. The ordinal counts every `<ls>` tag in that entry, starting at one. Commentary token offsets are zero-based, end-exclusive and relative to the exact `sk` field in the primary JSON. The token check maps contiguous Devanāgarī letters to SLP1 and compares them with the complete `k1` spelling. No ending, sandhi segment or headword prefix is removed. Neither a dictionary pointer nor a graphic match changes the number of source-qualified grammar derivations.

Zero new finite positions. Cumulative **40,379**.

[Machine relation](RELATION.json) · [State](STATE.json) · [Sources and exact pins](SOURCES.json) · [Dictionary references](DICTIONARY_REFERENCES.tsv) · [Per-rule coverage](RULE_COVERAGE.tsv)
