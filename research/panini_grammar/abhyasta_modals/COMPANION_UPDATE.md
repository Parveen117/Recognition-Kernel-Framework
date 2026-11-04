# PG25 — T143 integration and remaining runtime handoff

Author: Monty. 2 November 2026.

Companion branch: `shaiva-sources-maheshvara-spanda-pratyabhijna`.
Initial head was T142, `88244828de1ed8504886ce61c6fc15fd5df85aa6`.
The closing review found **T143,
`1d76875f21ae8f07e25c763bb6df1c798755feba`**, whose parent is T142.
PG25 reads its complete capsule, updated GENERALIZE.md, relevant changed
engine rows and the kernel diff. The prior T139–T142 review is retained.
This is a static, targeted review; no full reachable-path audit or
runtime replay is claimed. No merge or cherry-pick is performed.

## Useful repairs now credited

| Source boundary | Observed T143 repair | Written contract it supports |
|---|---|---|
| 7.3.87 | 7.3.84 no longer inherits the abhyasta + vowel-pit exclusion; 7.3.86 retains it | PG25 nenijāni versus final-ik bibharāṇi/bibhayāni/jihrayāṇi/piparāṇi |
| 7.1.102 /8.2.77 | resolved `strong()` replaces raw pit; lengthening reads `nxt()` | PG25 pipūryāt with actual modal y, distinguished from pipṛyāt |
| 8.2.25 | explicit root-s deletion before actual dhi | PG25/24 selected cakādhi account with its own source attribution |
| 7.2.77/78 | loṭ sva/dhvam are admitted with lakāra guards; bare laṅ/liṅ dhvam are excluded | PG24 īḍ/īś directed ending descent on the bounded domain |
| 7.2.114 | uses the resolved strong predicate | PG24 mṛjyāt; supersedes T140's mārjyāt residue label |
| 7.3.93 | uses the resolved strong predicate | PG23 brūyāt without the strong hal/pit īṭ |
| 6.4.36 /6.4.22 | han→ja before hi with a retained flag blocking 6.4.105 | PG23 jahi and source-window ownership |
| 6.4.119 | ghu before actual hi is admitted before its later dhi view | PG22 dehi/dhehi |

T143 also corrects the tiṅ apṛkta attribution to 6.1.68 and revises
pada-end operations. Those laṅ contexts are useful companion work,
but are not new PG25 paradigms. Its existing 6.4.118-before-6.4.113
order continues to support jahyāt. Copy guṇa and the root guṇa query
must keep their distinct owners.

## Reports and what their totals mean

T143 reports **5,373/5,373** open-lane agreements: 1,791 each for
laṅ, loṭ and liṅ. The fixed suite remains **908/908**, with **166
verbal rows** and three declared surface-coincident rows: 3.4.92,
7.1.58 and 8.4.56. These are companion reports, not PG25 executions.

The latest GENERALIZE.md section reports **7,015/7,052** unseen cells:
27 generator-empty cases, nine per present-system lakāra, and ten
remaining differences: nine gantā luṭ cells and one aidhidhvam luṅ
cell. Earlier sections and the old introductory hash remain historical;
use the T143 section and the newly pinned GENERALIZE.json for the
current report. The kernel reports **230 distinct rule IDs**, with
90 nominal and 158 verbal IDs sharing 18. Distinct IDs are not the
same unit as the 166 verbal row count. T142's nominal 94-row/861-cell
suite and 1,068/1,078 unseen report remain separately attributed.

The coverage union retains the construction branch's independent written/source records
and rebuilds the companion component from the T143 ledger. Its 498
operational-labelled IDs combine with the independent set and 6.4.117
to give 574. The new companion IDs are 7.3.88, 7.3.91, 8.2.73 and
8.2.74. T143 withdraws the T139 tiṅ use of 8.2.24, but that ID remains
in the combined reach through other nominal uses in the ledger; it is
not silently subtracted from all grammar. None of these counts proves
every context of a rule or counts as a new nonoverlapping verbal position.

## Remaining integration work

1. **Complete choice sets.** The engine still explicitly excludes full
   6.4.115/116 options and has no 6.4.117 row. PG25 requires both bhī
   weak-hal readings, both ordinary hāk weak-hal readings and all three
   actual-hi outcomes. Hrī does not inherit bhī's short-i option.
2. **Ending-dependent tāt fibres.** T143 records but does not claim
   7.1.35's tāt option. Hāk B 2sg is three hi readings plus two tāt
   readings, not a three-by-two product; jahātāt is excluded. Bhī's
   corresponding counts are four at B 2sg and three at B 3sg.
3. **Ṛ's copy history.** Copy iyaṅ for ṛ remains explicitly unclaimed.
   Retain copy i+r, its r-lopa and owned 6.4.78 iy, independently of
   the root's guṇa/yaṇ. Required distinctions include iyṛhi, iyratu,
   iyarāṇi and iyṛyāt.
4. **Source-view and native adapters.** Māṅ/hāṅ O A here removes root
   ā before resolved modal ī. The engine's historical `_siyut` guard
   can retain root ī and later merge ī+ī. Equal printed words do not
   identify those histories. Likewise T142's surface projection/pairing
   needs the explicit adapter to PG23–25's full history carrier and
   typed zero-specialization; no adapter is proved by a word comparison.
5. **Earlier optional contexts.** PG24's optional weak-vowel mṛj branch
   is still absent from the inspected 7.2.114 row. T143 also records
   without complete claims 8.4.65, 7.3.95 īṭ, 7.3.90's second
   alternative, 8.2.74 ru and 8.4.56 jaś. Keep those open where their
   source domains apply. None creates a new PG25 sound-collapse site.

Agreement of one emitted word with a permitted oracle set does not
establish equality of the full alternative sets or retained histories.
N2 permits reuse of ending/algebraic machinery only after the local
source guards and target ownership have been supplied.

## Work split

The construction branch continues written family closure, starting with the remaining
adādi vowel families and their īṭ/vṛddhi options. The theorem branch can integrate
the remaining source-qualified choice sets and native adapters into its
existing runtime. Tests and certificate replay remain deferred under
the current owner priority. Frozen pins are not overwritten. This is
a prepared handoff; no external message was sent.
