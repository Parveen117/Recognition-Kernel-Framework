# PG65 — Implementation handoff after the unchanged T166 head

Monty · 7 November 2026

The development branch starts at PG64 commit `fc830a181954fb5c3060b175396c98a7235a91d1`. The companion branch `shaiva-sources-maheshvara-spanda-pratyabhijna` was read again and remains at **`edd98b0685b478cb39468e350b26783bb4cce7ff`**, T166. Its previous full review is reused from [PG64](../ciri_continuations/COMPANION_REVIEW.md). The selected engine rows were read statically for this handoff. No grammar runner, independent generator or certificate replay was invoked.

## Addressed integration work

| Existing surface at the pinned head | PG65 contract |
| --- | --- |
| `AM_LIT` / the 3.1.35 row | Include the explicit anekāc supplement and source-qualified jiri admission before auxiliary construction. A generic list membership does not express the report's provenance or the non-Mantra guard. |
| 3.1.44, 7.2.1 and ordinary iṭ rows | Route basic ciri/jiri through seṭ sic while preserving the original vowel-final root view for the vṛddhi/prohibition decision. |
| 3.1.7 and the outer ārdhadhātuka path | Finish and retain the san-derived dhātu, then introduce outer sic and its distinct iṭ. Keep the deleted san a for the preceding-vowel query. |
| 7.3.96 and 8.2.28 rows | Only the two P apṛkta-hal slots receive ending īṭ. Delete the addressed sic s, then perform the licensed i+ī coalescence; retain the earlier san ṣ. |
| 3.1.48, 6.1.11, 7.4.93/94 rows | Keep ciri/jiri caṅ word construction held until the multi-vowel scope interpretation is explicit. The presence of a generic caṅ row is insufficient to resolve the source-policy choice. |

The engine text contains relevant sic, caṅ and ending rows. This static observation is not evidence that the new qualified inputs reach them with the required owners or produce the new tables. No test counts from T166 are reported as new PG65 results.

## Targeted acceptance requests for later implementation

| Input contrast | Written acceptance or held outcome |
| --- | --- |
| Jiri, basic, future lṛṭ versus san future lṛṭ, 3sg P | jiray-i-ṣya-ti → **jirayiṣyati**; ji-jiray-i-san plus outer iṭ/sya → **jijirayiṣiṣyati**. |
| Causal jiri 3sg kartari A versus karmaṇi A | **jirāyayate** with causer agreement versus **jirāyyate** with expressed-patient agreement. |
| Basic jiri luṭ P versus A causal luṭ, 1sg | **jirayitāsmi** versus **jirāyayitāhe**; derivation and pada both remain explicit. |
| Basic ciri luṅ 3sg versus 3du | **acirāyīt** versus **acirāyiṣṭām**; retain root āy and the original iṭ/īṭ ownership. |
| San ciri luṅ 3sg versus 3du | **acicirayiṣīt** versus **acicirayiṣiṣṭām**; outer sic s alone disappears in the singular. |
| San jiri luṅ 2sg versus 1sg | **ajijirayiṣīḥ** versus **ajijirayiṣiṣam**; mip→am does not satisfy the apṛkta-hal test. |
| Jiri basic liṭ, 1sg, kṛ auxiliary | Both cakara/cakāra and the listed ṃ/ñ boundary readouts, all within one requested position. |
| Jiri san past versus san conditional | Past occurrence of desire under H02 versus failure of the selected desire event under the full 3.3.147/139 context. |
| Ciri/jiri causal luṅ | Caṅ selection established; complete word/position remains **HELD_SCOPE_7_4_93_94**. |
| Ṛkṣi from a mixed register/segmentation source | **HELD_SOURCE_COMBINATION** under the inherited policy. |

The [state register](STATE.json) contains all admitted requests and their written words. These are future acceptance data, not executed tests. Optional phonetic doubling and broad Vedic/accent readouts remain outside the declared table.
