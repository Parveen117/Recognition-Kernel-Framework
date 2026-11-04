# PG63 — T165 static guard review and source-qualified handoff

Author: Monty. 5 November 2026.

The companion branch `shaiva-sources-maheshvara-spanda-pratyabhijna`
was checked and remains at `bf1228fd5262baf9f3257de19547aab51eb260cc`.
No newer commit was observed. Reuse PG61's complete T165 review and
PG62's source correction; no companion suite or certificate was rerun.
No message was sent to the companion author.

Selected static code at that commit has `AM_LIT` at line 106 and
the `3.1.35` row at line 502. The listed guard uses membership in
`AM_LIT`/`AM_SLU` or gaṇa 10. Ciri is absent from the displayed
`AM_LIT` set; the guard itself has no anekāc or Mantra input.
This does not implement PG63's newly declared source/register contract.
It is a static boundary finding, not a claim that a fresh runtime
comparison failed. The existing guard's other domains are not audited
again or globally rejected here.

The concrete handoff is:

1. Add the named KRM526 reported-classical ciri profile while retaining
   the older SK-held profile and the modern Vedic tag.
2. Keep both root vowels. Implement the anekāc/non-Mantra ām gate on
   the proper source-qualified lexical view, before root guṇa.
3. Give ām and the auxiliary different owners: delete primary liṭ,
   bind the auxiliary's own liṭ and agreement, and retain all three
   auxiliary choices and the explicit nasal readout alternatives.
4. For san and sya, retain root i and newly supplied iṭ separately.
   The selected san is not the aniṭ/jhal-initial kit branch; its
   stem is cicirayiṣa. The basic future stem is cirayiṣya.
5. Add P1–P3's **54 positions / 94 readings** under that profile.
   Do not promote source-held jiri or ṛkṣi diagnostics into this count.
6. Split the modern ṛkṣi pronunciation-only account from the Kṣīra
   idit/num witness and SK's literal present-word discrepancy. A
   source-level role decision must precede num and vowel counting.

Grammar execution, replay, complete Vedic/accents, wider lexical
arbitration and canonical runtime integration remain deferred or open
as separately recorded in [state](STATE.json).
