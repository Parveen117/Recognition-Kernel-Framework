# PG814 · Changed-document check

Executed after the coherent change with Python 3.12; generators, grammar execution, untouched suites and replay remain deferred. The first result was not recoverable after context compaction. Two explicit reruns then failed because the checker assumed nonexistent top-level `parent_commit` and `next_frontier` keys. A third used over-broad frontier ownership; its correction exposed that CURRENT_WORK lacked the frontier already present in the dated handoff and backlog. That register gap was repaired before the final rerun.

`PASS Python 3.12.14 · 35 assertions · 7 attempts total (one unavailable result, four checker-scope failures, one register-gap failure, one corrected pass)`

Assertions cover 35/41 increments, eight constructions/35 interfaces, eight decisions, exact pins, census arithmetic, source forks, shared-surface histories, PG14 typed zero specialization, central registers, protected closures, Claude deferral and frontier 5.3.83.
