# PG41 — PG40 and companion review

Author: Monty. 4 November 2026.

The immutable predecessor is
[PG40 at 4f745150](https://github.com/Parveen117/Recognition-Kernel-Framework/tree/4f7451502fd3bbef5e43f84e273f9c65f3f92b26/research/panini_grammar/anga_affix_abhyasa).
Its files remain unchanged. Navigation is extended in the new commit; older
navigation hashes are checked against the predecessor commit, not rewritten.

## P1. Direct integrity review

|Check|Observed result|
|---|---|
|Authored tables versus structured register|545 rows across 13 tables; every six-column value, file and line matches|
|Coverage baseline|2,561 combined IDs, 2,405 independent written IDs, 11,552 finite positions|
|Literal archive|1,691 fields present; 1,682 compared directly with retrieved pinned primary fields, zero differences|
|File pins|34 of 35 SHA-256/byte-count identities rechecked, zero differences among those checked|
|Unrechecked primary file|Nyāsa download failed; its existing Git tree blob identity and historical pin remain recorded|
|Companion ledger|Pinned T152 bytes rehashed successfully; no execution or import|

The nine Nyāsa fields in PG40—6.4.76, 127, 128, 158, 160, 166; 7.1.68;
7.4.55, 73—were not independently re-compared this turn. They remain inside
the byte-verified predecessor archive. This is a stated audit limitation,
not a newly verified source claim. The inherited file is 9,286,920 bytes,
with Git blob 8ecc8bbb657a42be8606fe07fa0c72c9cb7fa1b1; its exact historical
SHA-256 and edition are recorded as unrechecked in [coverage](COVERAGE.json).
PG41 uses no new Nyāsa field.

## P2. Eight targeted semantic rereads

|PG40 rule|Boundary rechecked against Kāśikā|PG41 consequence|
|---|---|---|
|7.4.1|Qualified root-upadhā shortening before copy, with nested णि extension|7.4.93/94 read the correct light-root view|
|7.4.2|अग्-loss history, शास् and ऋदित् exclusions|No blanket causative-aorist shortening|
|7.4.54|Actual स्-initial सन्; set branch excluded|Do not import special इस् into every desiderative|
|7.4.55|ज्ञपि णि loss before remaining-vowel ई; literal आपीप्सति damaged join|Retain earlier adopted ईप्सति and source distinction|
|7.4.57|Intransitive मुच् option owns its गुण/copy-loss branch|No independent cross-pairing with retained copy|
|7.4.58|Whole-copy deletion explicitly excluded from सन्वत् चङ्|7.4.93 retains qualified transfer rather than global copying|
|7.4.60|Copy's noninitial consonants removed; vowel-initial copy included|Root and copy reduction keep different addresses|
|7.4.61|शर् + खय् reduction, with source खर् extension for उच्छ्|Later copy जश्/चर् receives the intended surviving segment|

These rereads support the specific continuation. They are not an independent
validation of every PG40 interpretation.

## P3. Companion boundary

The companion branch remains at
[T152, 751dddec](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/751dddec31988299cdd5003ebffcbf701b1b0126).
The retrieved ledger reports 10 compiled, 169 meta, 434 hand-coded, 390 cited
and 2 misnumbered entries, totalling 1,005 records with 81 missing texts.
These are the companion's recorded labels, not PG41 verification results
or new finite positions. Existing T151/T152 semantic review is inherited;
there is no new companion change to review, replay or import.
