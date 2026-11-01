# Repository cleanup — 1 November 2026

The owner requested a clean canonical repository after integration. The earlier
integration preserved old branch references; this later maintenance pass removes
those merged references while keeping their commits reachable from `main`.

## Branches

Before deletion, all 30 non-default branch tips were checked as ancestors of
`c81ca4f1c14a10c817a889eafe3ef3f2083cbc08`. Their exact names and SHA values were
committed in [BRANCH_ARCHIVE_2026_11_01.json](BRANCH_ARCHIVE_2026_11_01.json)
at `4aae829f13377bfcd0080b9c6649e94035f6ed40`. The GitHub interface also showed
zero commits ahead for each branch when its reference was removed.

After cleanup, the GitHub branch collection contains only `main`. No release
tag or commit history was removed. A former branch can be recreated from its
recorded SHA using the ordinary GitHub branch-creation operation or Git:

```text
git fetch origin
git branch <recorded-branch-name> <recorded-commit-sha>
git push origin <recorded-branch-name>
```

Restore a reference only when work needs to resume; historical citation can use
the immutable commit link directly.

## Navigation and maintenance

The front page now provides a quick start, repository map, evidence scope and
direct links to verification, contribution and provenance guidance.
`CONTRIBUTING.md` documents a one-main/temporary-topic-branch lifecycle.
`VERIFY.md` separates current package checks from historical campaign replay.

Routine CI selects the affected existing contracts. Broad proof-lab replay is
manual, and foundation/MR-01–MR-03 triggers are scoped to their own inputs.
Routine checks use a read-only repository token. No theorem, executable
scientific source, archived certificate, expected hash, patent notice or
repository access policy is changed by this maintenance pass.

The public-release scanner previously flagged SE19's explicit negative
statement as an RH overclaim because the sentence wraps across two lines.
The scanner now recognizes only that reviewed complete statement at its exact
path. Changed wording and additional positive claims still fail, as do all
other audit categories. The source packet itself is untouched.

## Validation of this maintenance pass

- Eight existing mathematics-navigation tests pass under Python 3.12.
- Seven targeted scanner regressions and the repository public-release audit pass.
- All four updated/new guides have resolving local links; the README patent
  notice is byte-identical to the prior notice.
- All 15 workflow files parse, and ten direct routing scenarios cover document,
  engine, immutable archive, memory, R3/R4, SS1 and manual invocation behavior.
- The integration integrity check still passes: 367 imported files are
  byte-identical, the canonical engine is unchanged, and all recorded source
  bindings retain their current or explicitly historical match.
- All 30 archived branch tips remain ancestors of `main`.

Untouched engine and historical scientific campaigns were not rerun for this
maintenance pass. Their earlier results remain in the dated integration record.

The [earlier integration record](PENDING_WORK_2026_11_01.md) remains a dated
record of the merge and its tests; this cleanup supersedes only its statement
that the branch references were retained.
