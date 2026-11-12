# Four-hour written grammar run · 13 November 2026

Monty · 02:25–06:25 IST. This is the new run, distinct from the expired 12 November window.

Baseline: PG275, commit `3861c38680913b411b608cf43894c09813811954`, **50,108** written finite positions.

## Foreground handoff

The foreground releases branch writing with the PG284 packet. The 03:25 checkpoint or its next available worker should take the actual branch head and continue active sequential development through the next work hour, then hand off to the following checkpoint. Stop new development at 06:25 IST and do final verification/reporting then. Read ACTIVE_WRITTEN_RUN.json and CURRENT_WORK.md before writing. Do not write concurrently with a newly active writer.

The foreground packets PG276–PG284 add **426 finite positions and 456 selected readings**, with **zero nominal positions** and **two separately counted source observations**. Cumulative finite coverage is **50,534**. The two observations are one printed perfect-stem difference and one same-surface causing/narrating construction contrast; they are not finite-position credit.

| Stage | Published commit | New finite positions | Selected readings | New source observations |
| --- | --- | ---: | ---: | ---: |
| PG276 | eabd401d5f782d438603956893a66c71712cd028 | 72 | 72 | 0 |
| PG277 | 74ce05cda09dcd607d1bc0b0e99185538e3deeec | 48 | 48 | 0 |
| PG278 | 8eae280c91d35b1d0b93266f544a27017fd27885 | 24 | 30 | 1 |
| PG279 | 4c2407ab21d9627e81393380353603fbcbe8f8a3 | 36 | 36 | 0 |
| PG280 | 9d0ff6d996fed4b8f634af2b7aa3e1db617561be | 36 | 40 | 0 |
| PG281 | 18597dd4245d2542ad73dd31d632a2537f9827cf | 12 | 24 | 0 |
| PG282 | b86c0129c0370d2d3842fc3206752b0dab948ea2 | 54 | 58 | 0 |
| PG283 | d7115b9a546c155aff173fe6dfd443cfde483cea | 72 | 76 | 1 |
| PG284 | ec6327a682f6e21c90a093da4360a0b212a90016 | 72 | 72 | 0 |
| PG285 | 2f937575d47eecc1e012612039715f6cdbc5399e | 36 | 74 | 1 |
| PG286 | 1a90da52ce984cad40f3a611f7389bc9265f8002 | 90 | 94 | 0 |
| PG287 | cecf2171fbcf91cc3fc8db86d9ea8f3964137cdf | 180 | 188 | 0 |
| PG288 | 7a5653259b3097fdc57a27047723270005699398 | 90 | 102 | 0 |
| PG289 | e20c434aea4a81217e8238089e9c2ba8eb21cd81 | 90 | 90 | 0 |
| PG290 | d1f94ec31e7e24d1b266b246dccc8713d0e92fae | 2 | 2 | 0 |
| PG291 | 5d69ce35ecb629b74003e1e2c1a5c6d84e862ec9 | 1 | 1 | 1 |
| PG292 | b521f6b282a21d0e3e877c7b60b0f9c05c4f0941 | 2 | 2 | 0 |
| PG293 | 4fa495a6e9e5d573710a63f65d12ed979c308414 | 3 | 3 | 0 |
| PG294 | e585e9535280155aa1da3f8c7d641599a405f01a | 3 | 3 | 0 |
| PG295 | eea8863e254d452235cb6535b90d061b9d8052fb | 2 | 2 | 0 |
| PG296 | ff1741da44ca93da9676caaa46c6029c8ad9f48d | 87 | 87 | 0 |
| PG297 | e2561658d53929966f9adfad56479a173ae5ff84 | 2 | 2 | 0 |
| PG298 | b319f444f464bd9d82426a4783f5171ac6886e3d | 12 | 13 | 0 |
| PG299 | 9242461eba97160c0dbbba9eda72f902b4240064 | 1 | 1 | 0 |
| PG300 | d75e14ad6830a86e8ee4d699bcde9fbf9e4fb25b | 0 | 0 | 0 |
| PG301 | 64366413edb34322582de26ccb48f549243fe65d | 0 | 0 | 0 |
| PG302 | 94da5c32041e1676326e396413deb8531f648402 | 0 | 0 | 0 |
| PG303 | 0643a2c944d86a0c7ae17b798012753ca591f014 | 3 | 3 | 0 |
| PG304 | de5ca5d4411d8d95c7205cdf223467e8adfd6fdb | 0 | 0 | 0 |
| PG305 | 4178d17cf748ec8f6be652cfa025739e04098457 | 5 | 5 | 0 |
| PG306 | b527b6c8317fb1c6cf4222fed57054dedfda3c71 | 1 | 1 | 0 |
| PG307 | 515fc6a68cc4388cdfa80139cc9985515b0fd46e | 1 | 2 | 0 |
| PG308 | 966e7d6321009d4a5dfa88d7bffea684f49a7206 | 1 | 1 | 0 |
| PG309 | d73e79444df0e0607f882fa52060ab6b9affe972 | 2 | 2 | 0 |
| PG310 | 149ca82e056c146486f73d32fda4c2a0800bbb94 | 4 | 7 | 0 |
| PG311 | ff31aaf17b958d2e5f302085d5369b1505edc716 | 2 | 2 | 1 |

Checkpoint through PG305 after prior-coverage correction: **1,035 finite positions, 1,128 selected readings, zero nominal positions and four source observations** in this run; cumulative finite coverage **51,143**. The 04:25 checkpoint contributes a corrected net **120 finite positions and 121 readings**, with zero new nominal positions or source observations.

## Concrete next work

PG285 completed the two result-qualified han NIC-P profiles at **180/180** positions. Its perfect keeps the ām host and all three auxiliary histories distinct under 3.1.35/40 and 6.4.55; its caṅ aorist records the 3.1.48, 6.1.11, 6.4.51, 7.4.1 and 7.4.93/94 sequence. PG286–PG289 then wrote four source-qualified residual or special-pada profiles. PG290 wrote the exact *ā + han* own-head/other-head present pair.

PG291 found an independent immutable *Śābdikābharaṇa* witness for **āhadhve**, contrasting with digital Mādhavīya entry 662's **ahadhve**. PG292 writes the same line's directly printed **āhase** and **āhane**; its **āghnāthe** remains uncounted pending collation. PG293 separately writes Kāśikā's three directly printed intransitive *ā + han* third-person forms. PG294 writes the parallel directly printed intransitive *ā + yam* triplet under its own route. PG295 keeps the two explicit object-bearing active controls as narrower clause profiles. PG296 completes the intransitive *ā + yam* grid by adding only the 87 cells not already credited in PG294. PG297 adds two further directly witnessed own-limb *ā + han* present cells while leaving 2du open. PG298 writes twelve directly printed outer third-person cells and preserves both aorist outputs. PG299 adds one literal negative *pra + jñā* active clause without widening it to an all-prefix schedule. PG300 adds the two literal unprefixed actor-result middle cells for cow and horse objects. PG301 adds six direct middle controls across denial, means, non-recollection and actor-result routes. PG302 keeps the three recollective *sam + jñā* active case controls separate. PG303 adds three direct desiderative cells distinguishing ordinary middle, transitive *anu*-active and intransitive *anu*-middle. PG304 removes eleven duplicate credits from PG300–PG302 after cross-checking PG79/PG80/PG81; their clauses remain corroboration only. PG305 adds five disjoint intensive/causative controls from a derived domain previously left open. It writes only that 2pl cell and counts the textual difference separately as one source observation. Printed Mādhavīya collation and the rest of the *ā + han* schedule remain open; the online *Śābdikābharaṇa* series' 3du spelling also needs collation before wider use.

PG282's prefixed ja/vadha words use an explicitly selected non-al lexical-membership reading of 1.1.56/8.4.17. They remain written derivations, not literal prefixed attestations. Preserve that distinction in future expansions. The same source policy is explicit for the new NIC words. Seek independent prefixed corroboration without inventing a witness.

Four primary Uṇādi 4.105 fields (*sya, ḍha, ḍaṭ, āṭac*) and the distinct effect, if any, of k at 5.56 remain open. Continue other documented grammar rather than forcing a witness.

## Checks and publishing

Python **3.12.14** document/provenance checks only. New key uniqueness, baseline/source byte pins, source excerpts, word-table agreement and count/navigation consistency were checked. NIC packets also had literal script/prefix-span projections against their archived Devanāgarī word tables. No Sanskrit generator, grammar execution, certificate replay, old suite or hardware job ran. Source-word comparisons and written derivations are distinguished.

Every grammar packet uses the same branch, `[skip ci]`, the actual current parent and non-forced compare-and-swap publication. The 06:25 final report must re-read actual branch state and report only published work in this run. Do not reuse the previous four-hour baseline or report future work as completed.
