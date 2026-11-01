# PG11 — Actual validation

Author: Monty. 1 November 2026.

Executed under Python 3.12 against the primary checkout pinned in
[SOURCE_PINS.json](SOURCE_PINS.json):

```sh
python3.12 -m research.panini_grammar.lexical_present.verify \
  --source-root /path/to/ashtadhyayi-data --write
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The verifier writes only PG11's result and coverage files. It reads the
frozen PG10 coverage for cumulative accounting without replaying its
suite or regenerating its certificate. The result binds SHA-256 hashes
of the four new Python modules and the coverage object.

| Direct check | Result |
| --- | --- |
| Literal primary Sanskrit word membership | 245 cases pass, covering 39 new roots |
| Unsupported requests | 40 expected refusals pass |
| Occurrences, source drift, ownership, ordering and dispatch | 107 controls pass |
| Literal citation anchors | 623 references / 571 unique anchors match |
| Pinned external source files | 8 unchanged |
| Historical repository files | 100 unchanged |
| Pinned Vidyut comparison | 405 cells / 420 branches, zero differences |
| Mathematics navigation | 8 tests pass |

The CLI was separately invoked with all nine cells, exact meanings and
supplied pada licenses for brū P, vid P, śī A and ṛ P. Every cell returned
`COMPLETE_IN_REVIEWED_LEXICAL_PRESENT_DOMAIN`. The respective summed cell
form counts were 14, 18, nine and nine. These checks exercise the public
command entry point and its branch presentation.

The direct controls reject ambiguous or wrongly cased bruvaḥ occurrences,
missing optional/īś inheritance, source-wording drift, loss of ṛ's source
tag and removal of cakṣ's conflicting note. Cakṣ retains the raw
preprocessing vowel and its source UID through the explicit marker
decision; nonfinal i does not trigger num.

Ending substitution checks distinguish original and replacement marker
evidence, retain laṭ features and reject repeated, wrong-slot, wrong-root
and wrong-pada substitution. Brū's sixth and first-person endings cannot
borrow āh; the āh path excludes inherited īṭ and preserves dental-th
ordering. Vid's ṇal path retains the original tip/pit relationship for
this present domain without introducing liṭ.

The augment checks distinguish val from y, admit the required apit iṭ
cases, enforce tiṅ/sārvadhātuka and brū's extra pit condition, and reject
wrong hosts, repeated insertion and reversed membership. Ruṭ cannot be
inserted before the actual jh substitution or lose its component's sound
identities. Its pronunciation-only u is not mislabeled as an it-lopa.

Lexical controls distinguish han's two deletions, lexical abhyasta from
physical copying, daridrā and śās environments, mṛj's optional weak-vowel
vṛddhi and the duh/dih bhaṣ conditions. Lih's local visibility edges are
removed or retargeted in negative controls. The ṛ copy retains its source
link and generated r history; its iy substitution must precede the root's
yaṇ junction. Wrong ślu state, repeated copying and unreviewed multiple
vowels are rejected.

Every one of the 420 branches is checked for resolved obligations, unique
visible sound identities, ending-augment ownership, retained ending source
features, absence of fabricated copies for lexical abhyasta, and agreement
between branch forms and reported forms. Readout is repeatable, cannot
mutate or alias its source and cannot feed back into the morphological
state. Only six inherited dispatch examples are invoked; untouched
predecessor suites are not replayed.

The generator and CLI read neither the expected-word packet nor the
external comparison table. The comparison is evidence of agreement with
one pinned implementation, not a Sanskrit soundness oracle. The 245
primary word cases are separate membership checks, not a proof that every
optional branch is attested. New pṛj and the six PG10 word-witness gaps
remain explicitly open in [SOURCE_REVIEW.md](SOURCE_REVIEW.md).

No new companion theorem certificate or untouched operator-engine suite
was replayed. Hosted CI and main merge remain deferred. Full native
operator lifting, typed zero-specialization compatibility and
quantum-calculator integration remain open.
