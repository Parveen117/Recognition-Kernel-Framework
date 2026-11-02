# PG13 — Source readings and concurrent work

Author: Monty. 2 November 2026.

Primary source: [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data),
commit `5744762f010d677cfb43f347a42d02796cf615d6`. The source preflight
matches 138 literal anchor references / 127 unique anchors, nine external
files and 130 frozen historical files. Source bytes and predecessor
evidence are unchanged.

## Fifteen bounded records

The new [records](RULE_RECORDS.json) bind Sanskrit wording, individual
source occurrences and grammatical cases for 1.1.46, 1.1.51, 1.3.78,
1.3.86, 1.4.13, 3.1.26, 3.1.32, 6.1.78, 6.4.92, 7.2.115, 7.2.116,
7.3.36, 7.3.37, 7.3.84 and 7.3.86. They reuse the frozen PG12 scope
compiler without new scope overlays. Repeated *kartari* occurrences at
1.3.86 remain separate.

Kāśikā 3.1.26 explains the prayojaka causative meaning. That meaning is
an explicit input license; the generator is not a semantic parser.
Kāśikā 3.1.32 designates the sanādi-final composite as a dhātu. The later
śap therefore follows this composite, and 1.4.13's relative aṅga includes
the original root, any owned augment and ṇic.

The [four source decisions](SOURCE_ADJUDICATIONS.json) retain:

- **Augment pronunciation.** Bālamanoramā at both 7.3.36 and 7.3.37
  distinguishes final-k it designation from pronunciation-only u and
  identifies kit placement as the root's final member. U is not silently
  nasalized or reclassified as an it marker.
- **Two pā identities.** The drinking root 1011074 receives yuk. The
  protecting root 1020051 has a distinct source discussion and pālayati
  path; this packet refuses it. An identical displayed root spelling is
  insufficient to select the same augment.
- **Pada context.** The simple root's A/P/U label remains a lexical fact.
  A causative needs its own licensed context. This packet implements only
  supplied P contexts; 1.3.86 is explicit for budh. It does not infer the
  full 1.3.74/86–89 semantic system or admit all A contexts.
- **Gam's mit license.** The source lexical note cites the am-final
  gaṇasūtra. The implementation retains intermediate gām and its licensed
  shortening, without treating root-final m as a teaching marker.

The selected 7.3.36 profile contains only ā-final sthā/dā. Its other
named roots, including hrī and ṛ, need additional ordering and guṇa review
before expansion. No universal augment scheduler is claimed.

## Literal evidence and comparison

The eleven exact words in [REFERENCE_CASES.json](REFERENCE_CASES.json)
come from selected relevant passages. Examples include nī/gam/vid/budh
at Kāśikā 1.4.52, hṛ at 1.4.53, bhū at Siddhāntakaumudī 3.1.26,
sthā at Laghusiddhāntakaumudī 7.3.36 and pā at Kāśikā 7.3.37.

In particular, the gamayati/gamayataḥ/gamayanti examples under 2.4.46
describe an iṇ substitution. They are **not** used as lexical-gam
witnesses. A word match alone cannot settle lexical or sense identity.
The generic dā example attests the word; its precise lexical row remains
separately declared and pinned.

Kṛṣ **1060006** has no separate exact-word witness in the selected
passages. Its source identity and guṇa/r-accompaniment rules are pinned,
and the full comparison agrees. This gap remains explicit. The 31 older
PG10–PG12 exact-word gaps are neither closed nor reclassified.

The pinned `dhatuforms_vidyut_nich_kartari.txt` comparison covers all
108 cells independently of runtime generation. Its agreement is not a
primary-text attestation of all those cells.

## the theorem branch's useful commits and retained findings

The reviewed branch snapshot is
[`0f489be`](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/0f489be0a1ab4ff9235e4dcf7fdfa508643dbc23).
[CONCURRENT_REVIEW.json](CONCURRENT_REVIEW.json) pins the selected files.
T105's twelve-root causative pattern is useful here. PG13 supplies exact
lexical IDs, independent licenses, full ownership and nine cells per root.
Its 36 displayed expectations are separately preserved in
[COMPANION_EXPECTATIONS.json](COMPANION_EXPECTATIONS.json); AST extraction
does not execute the companion module or replay its certificate.

T89's repair commit `dead06f` restores all eight stage-removal table keys
and guards `trc_agent` before entry lookup. The earlier findings are
statically repaired in that snapshot. The new certificate's reported pass
and pin are not independently replayed here; the old PG9 review remains
unchanged.

T105's puk explanation attributes u to 1.3.2, whereas the selected
Bālamanoramā calls it pronunciation-only. Its literal p output is
unaffected; PG13 carries the distinction explicitly. T107's theorem
attributes final l in ṇvul to 1.3.8; final-consonant designation is
1.3.3. Its runtime uses the existing marker interpreter, so this review
does not claim a corresponding output failure. T107's nineteen kṛt words
remain useful future nominal work, outside PG13's present count.

A final branch-inventory check observed the later tip
[`ca2b25f`](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/ca2b25f754aabe0d9b5a1621f93f0fe68311747b):
the theorem branch merged PG11–PG12 into that branch and added T108–T111 for
intensives, ugit at-stems, passive and feminine formations. The comparison
from the reviewed snapshot changes none of the five files pinned in
`CONCURRENT_REVIEW.json`. This later check is a commit/file inventory,
not a source or certificate audit of those four new theorem packets.
