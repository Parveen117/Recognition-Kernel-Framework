# PG62 — T165 source correction and following-sound handoff

Author: Monty. 5 November 2026.

The companion branch `shaiva-sources-maheshvara-spanda-pratyabhijna`
still points to `bf1228fd5262baf9f3257de19547aab51eb260cc` (T165).
No newer commit was observed. Reuse [PG61's full T165 review](../hi_rdh_reduplication/COMPANION_REVIEW.md)
and its attributed counts; do not treat this turn as a fresh lane,
suite or certificate run. Selected 3.1.83/7.1.100/102/8.2.77 guards
were read statically. No message was sent to the companion author.

## The newly established source boundary

T165 treats svṝ 09.0070 as outside its pvādi list and derives a
long svūrṇ- present path. PG12 also used that placement and the
modern metadata's वरणे. The cited primary book instead has **svṝ,
हिंसायाम्, svṛṇāti**, entry 18, followed by **vṝ, वरणे**, entry 19.
The three archived pages establish its position within the relevant
subdivision and the P declaration. This is a source correction to
the written line as well as a handoff for the engine.

Do not merge the newly admitted `DP_1919_KRYADI_18_SVR_HIMSA` profile
with a svṝ/varaṇa request. Preserve 1090070 as a discrepant modern
lookup association and record the primary identity explicitly.
The source-held old present requests and the new nine present
requests have different sense/profile keys. Śṝñ continues to use
PG60's short `KSHIRA_SHRNJ_1090015` witness.

## The observed row order has a second, independent issue

At the pinned engine bytes, the 8.2.77 row is at line 620 and the
3.1.83 row at line 683. The former lengthens i/u before an n-initial
śit vikaraṇa. The latter accepts nā/nī + actual hi after a consonant
and replaces that vikaraṇa by āna. T165's capsule reports the resulting
svūrāṇa/śīrāṇa against Vidyut's svūrṇīhi/śīrṇīhi as unresolved.

Even if a separate source licensed its initial long-root profile and
the śānac decision, retaining the earlier lengthening is not justified
by 8.2.77: the new following vowel ā removes its hal condition.
The source-qualified affix decision must precede that tripādī
readout, with the source/condition retained. This static diagnosis
does not claim that moving one row universally solves the scheduler.

For the positively witnessed short profiles, the earlier problem is
already absent: source-qualified 7.3.80 gives ṛ; 3.1.83's hal
condition fails; the selected P imperatives are **svṛṇīhi/śṛṇīhi**.
The engine's reported “clean” lane declarations do not certify this
source correction, and the wider unshortened-source question remains
outside PG62's admitted grammar.

## Concrete implementation handoff

1. Add a source/sense-qualified svṝ profile and withhold the old
   svṝ/varaṇa claim under this selected witness. Keep neighboring
   vṝ 1090023 and the source's entry 19 separate.
2. Admit the selected svṝ to the correct source-relative pvādi range;
   preserve the independently pinned short śṝñ profile. A modern
   append order is not the historical range order.
3. Use actual hi and the rule-relative root ending for 3.1.83.
   Do not expand every ṛ into a hal-ending token using 7.4.71's
   unrelated r-component explanation. Respect 3.4.87's explicit apit.
4. Evaluate 8.2.77 against the following sound after the admitted
   earlier affix construction. Retain the original premise in the
   trace so a later branch cannot silently reuse a discarded n.
5. Integrate H05's 54 loṭ/vidhiliṅ positions and H06's nine corrected
   present requests. Compare source-qualified keys, not only strings.
   Keep hypothetical svurāṇa/śirāṇa diagnostic and unadmitted.

Full B-context registers, Vedic accents, broader variant arbitration
and runtime integration remain open, together with inherited PG57–PG61
and the separate PG19 obligations. Grammar tests, generators, replay
and navigation/operator suites remain deferred; only changed-document
checks use Python 3.12 here.
