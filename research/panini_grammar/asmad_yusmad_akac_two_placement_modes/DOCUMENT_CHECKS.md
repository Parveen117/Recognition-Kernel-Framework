# PG657 document checks

Status: **PASS** — Python 3.12.14, 104 assertions, 3 attempts. Attempt 1 stopped on an assertion token that expected unsandhied `आवकयोर्` where the pinned Kāśikā has fused `आवकयोरित्यत्र`; no authored grammar result changed. Attempt 2 found a missing census line in `WRITTEN_BACKLOG.md`; that necessary tracker edit was made. Attempt 3 passed.

The check covers JSON parsing, exact TSV rows/credits, totals, source snapshot pins and required source strings, dependency bytes/hash/blob pins, tracker mentions, full-carrier proof tokens and preservation of Open/Excluded boundaries. It does not execute Sanskrit generators, grammar code, untouched old suites or certificate replay.
