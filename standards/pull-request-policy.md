# Pull Request Policy

The rules every change to this repository has to satisfy.

Deliberately short. A standard nobody reads is a standard nobody follows, and
most of what would otherwise be written here is enforced by the pipeline
instead — which is the point of
[automation over policy](../processes/documentation-flywheel.md).

---

## The rule

**Branch per change. Never commit to `main`.**

```bash
git checkout main
git pull
git checkout -b descriptive-branch-name
```

Re-check before every commit:

```bash
git branch --show-current
```

That second command is not decoration. Merging leaves you back on `main`
without saying so, and the next commit lands there.

---

## This is policy, not enforcement

Branch protection on `main` does **not** require pull requests, and cannot —
`render.yml` pushes generated output straight to the branch, and a
pull-request requirement rejects the bot with a 403 at the final step.
Recorded as [DEC-010](../decisions/decision-log.md).

So: anyone with write access *can* push directly to `main`. The convention
holds because people keep it, not because Git stops them. That is worth stating
plainly rather than implying a gate that is not there.

---

## What a pull request must satisfy

| # | Requirement | Enforced by |
|---|---|---|
| 1 | Validation passes — every record against the schema, every diagram parses | `validate.yml` |
| 2 | No hand-edits to generated files | Review |
| 3 | New controlled values are added to `schema.yaml` in the same PR | `validate.yml` fails without it |
| 4 | Claims from a conversation link to their evidence | Review |
| 5 | One logical change per PR | Review |
| 6 | Nothing sensitive, nothing real | Review |
| 7 | Approval per the decision-rights matrix | Review |

### 1. Validation passes

Run it before pushing rather than finding out in CI:

```bash
python automation/render-inventory.py --validate-only
python automation/render-diagrams.py --check
```

The gate catches unapproved vendors, team names in person-only fields,
undefined fields, malformed YAML, and dangling integration references — each
naming the file, the field, and the offending value.

### 2. No hand-edits to generated files

Never edited by hand:

- `inventory/rendered/*`
- `inventory/apps/*.md`
- `diagrams/rendered/*.svg`
- `diagrams/source/integration-landscape.d2`

Change the source data and re-render. A hand-edit here is not a policy
violation so much as wasted work — the next merge overwrites it. Full table in
[repo-conventions.md](../meta/repo-conventions.md).

**Render diagrams with the wrapper, never with `d2` directly:**

```bash
python automation/render-diagrams.py
```

A bare `d2` render produces a file with different CSS class names and identical
geometry, so it arrives in the diff looking like a change. See
[DEC-009](../decisions/decision-log.md).

### 3. New controlled values go in the same PR

A new vendor, person, team, or capability means editing
[schema.yaml](../inventory/schema.yaml) alongside the record that needs it.
This friction is the mechanism, not an accident — see
[DEC-003](../decisions/decision-log.md). Do not work around it by reusing a
near-enough existing value.

### 4. Claims link to their evidence

If a change came out of a conversation, link the summary in
`evidence/meetings/`. A record whose provenance is untraceable is an assertion,
and assertions are what this repository exists to replace.

### 5. One logical change per PR

One record, one process, one decision, one diagram. `render.yml` produces large
generated diffs from small source changes, so a PR that also touches three
unrelated things becomes unreviewable quickly.

**Review the source files, not the generated output.** The generated diff is
there to show consequence, not to be read line by line.

### 6. Nothing sensitive, nothing real

This repository is public and its dataset is entirely fictional. Every
application, vendor, person, transcript, and metric is invented and must stay
that way. No real organization's internal data, no credentials, no personal
data — and no plausible-looking detail borrowed from somewhere real, which is
the version of this mistake that actually happens.

### 7. Approval

Per [context/decision-rights.md](../context/decision-rights.md):

| Change | Approver |
|---|---|
| Inventory or integration record | One reviewer, plus the SME if a fact about their system changes |
| New controlled value in `schema.yaml` | Marcus Iwu |
| Process, standard, or decision record | Dana Whitfield |
| Automation or workflow change | Sofia Marchetti |

---

## Commit messages

Descriptive, present tense, readable. No format is enforced.

```
Add tax engine integration records
Correct DR impact on the legacy order path
```

The pipeline's own commits are `Auto-render diagrams and inventory [skip ci]`.
Do not imitate that message by hand — it is how a human commit gets mistaken
for machine output later.

---

## Merging

- Squash or merge commit, either is fine.
- Delete the branch after merging.
- **Do not amend or force-push a merged commit.** History here is the audit
  trail; a decision record's date is only worth something if the commit behind
  it is intact.
- After merge, `render.yml` runs and commits generated output back. If your
  next branch starts before that lands, you will have conflicts in generated
  files — resolve them by re-rendering, never by editing.

---

## Decision records are append-only

Never edit a past decision, not even to fix its reasoning. Add a new record
that supersedes it and mark the old one `Superseded by DEC-NNN`. A log that
quietly corrects itself cannot tell you why anything changed —
[DEC-008](../decisions/decision-log.md) is retained wrong on purpose for
exactly this reason.

---

*Last updated: 2026-08-04*
