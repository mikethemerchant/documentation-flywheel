# Prompt — Write a Decision Record

For adding an entry to [decisions/decision-log.md](../decisions/decision-log.md).

Use it when something was **actually decided** — by a named person with the
authority to decide it, per
[context/decision-rights.md](../context/decision-rights.md). An intention, a
preference, or a thing everyone assumes is not a decision record.

---

You are working in the `documentation-flywheel` repository. Read `README.md`,
`meta/repo-conventions.md`, `context/decision-rights.md`, and the existing
`decisions/decision-log.md` before writing anything — match its voice and depth.

Write a decision record for:

> **<WHAT WAS DECIDED, and by whom, and where it was decided — meeting,
> transcript, or pull request>**

## Before you write, confirm all four

1. **Someone decided.** Not "we agreed it would be good if". A named person,
   with the authority for that class of decision under the matrix.
2. **It is not already recorded.** Search the log. If a related decision
   exists, this may be a supersession rather than a new entry.
3. **It closes something.** A decision record answers "why is it like this?"
   for someone arriving in two years. If it does not, it is an action item.
4. **It is durable.** Reversible with a keystroke and nobody would notice? Not
   a decision record.

If any fail, say which and stop. An over-full decision log is worse than a
short one — nobody reads a log where most entries do not matter.

## Structure

Append to the end of the log, and add a row to the index table at the top.
Next number in sequence; numbers are never reused.

```markdown
## DEC-NNN — <Decision as a statement, not a topic>

**Date:** YYYY-MM-DD · **Decided by:** <name> · **Proposed by:** <name, if different>
**Status:** Active

### Decision

<What was decided, in the present tense, as a rule someone could follow.
Two or three sentences. This is the part people read.>

### Rationale

<Why. Include what was considered and rejected, and what evidence settled it.
If the decision came out of something going wrong, say what went wrong —
that is usually the most useful paragraph in the entry.>

### Trade-offs

<What this costs. Every real decision costs something; an entry with no
trade-offs section has not been thought about, and a reader in two years will
assume it was obvious and reverse it.>

- <cost>
- <cost>
```

## Rules

- **Append-only.** Never edit a past entry, not even to correct its reasoning.
- **To reverse a decision**, write a new entry that supersedes it:
  - New entry gets `**Supersedes:** DEC-NNN`
  - Old entry's status becomes `**Superseded by [DEC-NNN](#anchor)**`, and a
    line under the heading: `*Retained unedited. It was wrong.*` or similar
  - Update both rows in the index table
  - **Change nothing else in the old entry.** It stays wrong on purpose.
    [DEC-008](../decisions/decision-log.md) is the worked example: a plausible,
    cheap, wrong fix, kept because the reasoning behind the reversal is worth
    more than the reversal.
- Statements, not topics. "Owner fields name people, never teams" — not
  "Ownership field discussion".
- Link outward: to the evidence in `evidence/meetings/`, to the records or
  scripts affected, to related decisions.
- Everything in this repository is fictional. Deciders come from the roster in
  `context/people.md`.

## After writing

- Confirm the approver in `context/decision-rights.md` — process and decision
  records need Dana Whitfield.
- If the decision changes a rule, update the document that states that rule
  (`meta/repo-conventions.md`, a standard, a process) in the same change. A
  decision nobody can find from the document it governs will be broken by
  someone acting in good faith.
- Branch, then open a pull request. Do not merge.

---

*Last updated: 2026-08-04*
