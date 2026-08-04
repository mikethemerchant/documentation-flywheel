# Decision Log

Append-only record of decisions about how documentation, the inventory, and the
pipeline work.

**Nothing here is ever edited.** A decision that no longer holds is marked
`Superseded by DEC-NNN` and the replacement is appended. The old text stays,
wrong, on purpose — a log that quietly corrects itself cannot tell you why you
changed your mind, and the reasoning behind a reversal is usually worth more
than the reversal. [DEC-008](#dec-008--pin-d2s-generated-svg-id-with---salt) is
the example: it was plausible, cheap, and wrong.

Each entry: date and decider → status → the decision → why → what it costs.

> Northwind Traders is fictional and so is everyone named below. The technical
> decisions are not — DEC-006 through DEC-010 are the real choices made while
> building this repository, recorded in-universe so the log reads as one
> organization's log rather than two.

---

| # | Decision | Date | Status |
|---|---|---|---|
| [DEC-001](#dec-001--documentation-lives-in-git-as-plain-text) | Documentation lives in Git as plain text | 2026-02-11 | Active |
| [DEC-002](#dec-002--diagrams-are-source-code-svg-is-output) | Diagrams are source code; SVG is output | 2026-02-11 | Active |
| [DEC-003](#dec-003--inventory-values-are-controlled-by-a-schema) | Inventory values are controlled by a schema | 2026-02-25 | Active |
| [DEC-004](#dec-004--owner-fields-name-people-never-teams) | Owner fields name people, never teams | 2026-02-25 | Active |
| [DEC-005](#dec-005--slugs-are-permanent-identifiers) | Slugs are permanent identifiers | 2026-03-04 | Active |
| [DEC-006](#dec-006--generated-output-is-committed-to-the-repository) | Generated output is committed to the repository | 2026-03-18 | Active |
| [DEC-007](#dec-007--the-core-system-of-record-is-derived-not-configured) | The core system of record is derived, not configured | 2026-03-18 | Active |
| [DEC-008](#dec-008--pin-d2s-generated-svg-id-with---salt) | Pin D2's generated SVG id with `--salt` | 2026-08-04 | **Superseded by DEC-009** |
| [DEC-009](#dec-009--all-d2-rendering-goes-through-automationrender-diagramspy) | All D2 rendering goes through `render-diagrams.py` | 2026-08-04 | Active |
| [DEC-010](#dec-010--main-is-not-protected-against-direct-pushes) | `main` is not protected against direct pushes | 2026-08-04 | Active |
| [DEC-011](#dec-011--the-demonstration-dataset-keeps-its-gaps) | The demonstration dataset keeps its gaps | 2026-08-04 | Active |

---

## DEC-001 — Documentation lives in Git as plain text

**Date:** 2026-02-11 · **Decided by:** Dana Whitfield · **Proposed by:** Sofia Marchetti
**Status:** Active

### Decision

All architecture, process, and inventory documentation is authored as
human-readable text — Markdown and YAML — in one Git repository. No wiki, no
diagramming tool, no spreadsheet holds anything that is not also here.

### Rationale

The previous attempt failed the way they usually do: written once, in a tool
separate from the work, by one person who then owned it alone. Within two
quarters nobody trusted it, so nobody read it, so nobody updated it.

Text in Git fixes the specific mechanics of that failure. Changes are diffable
and reviewable, so a change can be checked by someone other than its author.
History is free. There is no licence, no seat count, and no export problem. And
it is readable by an AI assistant, which is what makes the drafting step of
[the flywheel](../processes/documentation-flywheel.md) possible at all — a
wiki's rendered HTML is not a working format for that.

The decisive argument was ownership. A repository can be handed over. A
spreadsheet on someone's drive is inherited.

### Trade-offs

- **Contributors need Git.** Real friction for non-technical stakeholders, and
  accepted deliberately: the people who maintain this are in IT, and the
  published site serves everyone else.
- **No WYSIWYG.** Authoring is slower for anyone used to a wiki editor.
- **No built-in access control below repository level.** Everything here is
  visible to everyone with access, which constrains what may be written down.
  Nothing sensitive goes in.
- Markdown tables are tedious to hand-write. Mitigated by generating most of
  them.

---

## DEC-002 — Diagrams are source code, SVG is output

**Date:** 2026-02-11 · **Decided by:** Dana Whitfield · **Proposed by:** Sofia Marchetti
**Status:** Active

### Decision

Architecture diagrams are authored in [D2](https://d2lang.com) in
`diagrams/source/`. The pipeline renders them to SVG in `diagrams/rendered/`.
Rendered files are never edited by hand.

### Rationale

Same argument as DEC-001, applied to pictures. A diagram in a drawing tool is a
binary nobody can review, that only its author can change, and that is wrong
within a month of the system changing.

D2 specifically, over Mermaid or Graphviz: it produces diagrams readable enough
to put in front of a director without hand-tuning, it supports containers
(which is how teams and boundaries get expressed), and its text form is
readable enough that a reviewer can follow a diff without rendering it.

The deeper reason is that a text diagram can be **generated**. The integration
landscape is written by `render-inventory.py` from the integration records —
nobody draws it, and it cannot disagree with the data it came from. That is not
possible with a drawing tool at any price.

### Trade-offs

- Another dependency in CI, and a version to pin.
- Layout is the engine's decision, not the author's. Fighting it wastes time; a
  diagram that has to look exactly one way is the wrong tool's problem.
- Contributors have to learn a syntax.
- D2's rendering is not perfectly reproducible across platforms, which cost
  real time later — see DEC-008 and DEC-009.

---

## DEC-003 — Inventory values are controlled by a schema

**Date:** 2026-02-25 · **Decided by:** Dana Whitfield · **Proposed by:** Marcus Iwu
**Status:** Active

### Decision

Every enum field on an application or integration record must use a value
defined in [inventory/schema.yaml](../inventory/schema.yaml). Adding a vendor, a
person, a team, or a capability means editing the schema **in the same pull
request** as the record that needs it. Validation runs on every pull request and
fails the build on an unapproved value.

### Rationale

Free text does not survive contact with more than one author. Three people
recording the same vendor produce three spellings, and every grouping built on
top of the field silently under-reports.

The friction is the point, and it does two jobs beyond spelling:

1. **It makes adding a value a visible act.** A new vendor appears in a diff
   with a reviewer attached, instead of arriving unremarked inside a record.
2. **It is what stops an AI assistant inventing a person into the roster.** A
   model drafting a record from a transcript cannot hallucinate an owner,
   because an unknown name fails validation. The gate does not depend on the
   model behaving well.

`capability` is controlled for a further reason: it is the field the
[capability map](../inventory/rendered/capability-map.md) is built on, and the
overlap question — *what do we already own that does this?* — only works if two
records covering the same ground collide on the same value. As free text they
never collide, and the overlap stays invisible.

`Unknown` and `TBD` are legal values. See DEC-011.

### Trade-offs

- Two-file changes for what feels like a one-file edit.
- The schema needs its own upkeep; a stale controlled list is its own problem.
- Genuinely novel values are briefly blocked by process, which is annoying in
  exactly the moment someone is trying to be helpful.

---

## DEC-004 — Owner fields name people, never teams

**Date:** 2026-02-25 · **Decided by:** Dana Whitfield · **Proposed by:** Marcus Iwu
**Status:** Active

### Decision

`it_sme`, `it_technical_owner`, `it_manager`, and `recovery_owner` hold named
individuals. Team names are rejected by validation. Where a role is genuinely
shared, all the individuals are listed. Team-level accountability has its own
field, `it_team_accountable`.

### Rationale

"Infrastructure owns it" is a valid-looking answer that answers nothing. Nobody
can call Infrastructure at 2am.

The real argument is about how the two fail. A group name **degrades
invisibly** — the record still looks complete years after everyone who
understood the system has moved on, and nothing in the data changes at the
moment the knowledge leaves. A person's name **goes stale loudly**: it names
someone who left, and anyone reading it knows immediately that the record needs
attention.

Loud staleness is the behaviour you want from a document nobody is paid to
maintain.

The rule also makes concentration visible. Grouping by owner is what surfaced
one person holding both integration paths and another holding the entire
finance and warehouse chain. Neither is visible when the same records say
"Data & Integrations" and "Applications".

### Trade-offs

- Records need updating when people change roles, and they will be missed.
- It puts individuals' names against systems in a public-facing document, which
  some organizations will not accept.
- Reads as blame-assignment if introduced without explaining it. It is a
  contact list, not a responsibility assignment, and that has to be said out
  loud more than once.

---

## DEC-005 — Slugs are permanent identifiers

**Date:** 2026-03-04 · **Decided by:** Marcus Iwu · **Proposed by:** Priya Raman
**Status:** Active

### Decision

An application record's filename is its permanent internal identifier.
Rewording a display name never renames the file. A slug may keep a legacy form
its display name has moved on from.

### Rationale

Integration records reference applications by slug in their `source` and
`target` fields. Renaming a file to match a reworded display name breaks every
reference to it — and the failure is quiet, because a graph with a missing node
still renders.

Decided the day it happened. An ERP record was renamed to drop the vendor from
its display name (per the naming rule in
[repo-conventions.md](../meta/repo-conventions.md)), the file was renamed to
match, and eight integration records lost their target. Validation now fails on
a dangling reference, and the ERP record still carries its original
vendor-flavoured slug with a comment at the top explaining why.

A slug that no longer matches its display name looks untidy and is strictly
better than a broken graph.

### Trade-offs

- Slugs drift from display names over time, which is confusing for newcomers.
- The mismatch has to be explained in a comment on every record where it
  occurs, or someone will eventually "fix" it.
- A genuinely wrong slug is expensive to correct — every referencing record has
  to change in the same commit.

---

## DEC-006 — Generated output is committed to the repository

**Date:** 2026-03-18 · **Decided by:** Dana Whitfield · **Proposed by:** Sofia Marchetti
**Status:** Active

### Decision

Rendered views, per-application pages, the generated landscape `.d2`, and all
SVGs are committed back to `main` by the pipeline rather than built at publish
time and discarded.

### Rationale

Someone browsing the repository on the web should see the rendered inventory,
not the machinery that would produce it. That is most of the audience most of
the time, and asking them to run Python to see a table is asking them not to
look.

Committing the output also means the diff shows the *consequence* of a change.
Adding one integration record produces a diff that includes the new row in the
matrix, the updated per-app pages on both ends, and the redrawn diagram. That
is a far better review artifact than the record on its own.

And it makes drift detectable. If generated output is committed, a
re-render that changes a file nobody edited is visible as a diff — which is how
the D2 platform problem behind DEC-008 was caught at all.

### Trade-offs

- **Noisy diffs.** One record change can touch a dozen generated files.
- The pipeline needs write access to `main`, which forces DEC-010.
- A contributor who edits generated output by hand loses the edit on the next
  merge. Mitigated by a header on every generated file and a table in
  [repo-conventions.md](../meta/repo-conventions.md), and it will still happen.
- Merge conflicts in generated files, which are resolved by re-rendering rather
  than by editing.

---

## DEC-007 — The core system of record is derived, not configured

**Date:** 2026-03-18 · **Decided by:** Marcus Iwu · **Proposed by:** Sofia Marchetti
**Status:** Active

### Decision

The DR posture view identifies the core transactional system by computing which
application the most other systems write into. It is not named in a config file
or hard-coded in the renderer.

### Rationale

The fact is already in the integration records. Writing it down a second time
creates something that can disagree with them — and it would, the first time
the portfolio changed shape.

There is a smaller argument that turned out to matter more: a derived answer
can surprise you. If the computation ever returns something other than the ERP,
that is a finding about the portfolio, not a bug in the script. A configured
value can never tell you that.

### Trade-offs

- Correct and non-obvious. Readers assume it was configured, so the view says
  explicitly that it was derived.
- Ties the view's correctness to the completeness of the integration records.
  With SSO trusts absent from the model, the derivation is working from a
  partial graph — see [systems-landscape.md](../context/systems-landscape.md).
- A tie between two applications has no defined behaviour yet. Not hit; will
  need a rule when it is.

---

## DEC-008 — Pin D2's generated SVG id with `--salt`

**Date:** 2026-08-04 · **Decided by:** Sofia Marchetti
**Status:** **Superseded by [DEC-009](#dec-009--all-d2-rendering-goes-through-automationrender-diagramspy)**

*Retained unedited. It was wrong.*

### Decision

Both workflows invoke `d2` with a fixed `--salt` value so that rendering the
same source on any machine produces the same SVG.

### Rationale

The first render on `main` committed back a 284-line SVG diff for a diagram
nobody had touched. Every markdown view and the `.d2` source were
byte-identical, the geometry matched exactly, and the `viewBox` was the same to
the pixel. The only difference was the CSS class name D2 generates to scope
each SVG, which is derived per-platform.

Left alone, every push to `main` would rewrite that SVG — precisely the drift
this repository claims to prevent. `d2 --salt <value>` documents itself as
controlling that generated id, so pinning the salt in both workflows should
make the output reproducible.

### Trade-offs

- A magic constant in two workflow files that must not drift apart.
- Every diagram shares one salt, so the ids are no longer unique per diagram.

---

## DEC-009 — All D2 rendering goes through `automation/render-diagrams.py`

**Date:** 2026-08-04 · **Decided by:** Sofia Marchetti · **Supersedes:** DEC-008
**Status:** Active

### Decision

Nothing calls `d2` directly — not the workflows, not contributors. Every render
goes through `automation/render-diagrams.py`, which renders each source file and
then rewrites D2's generated SVG id to one derived from the **diagram's
filename**. `--check` parses without writing, for the validation gate.

### Rationale

DEC-008 did not work. After it merged, the pipeline committed the same SVG back
a second time: a Windows laptop produced `d2-1594564165` and the runner produced
`d2-1681756903` — both salted, both different. `--salt` changes the generated id
without making it platform-independent, which the documentation does not say and
a single test would have shown.

What settled it was proving the id was the *only* difference. Normalizing it out
of both files gave byte-identical SVGs, so geometry, styling, and embedded fonts
were never in question, and the fix could be narrow with confidence.

Deriving the id from the filename gives both properties the salt could not:
**stable across platforms**, because nothing about the machine feeds into it,
and **still unique per diagram**, which is the property D2 wanted from the hash
originally. Putting it in a script rather than in workflow arguments means the
two workflows cannot drift apart in how they invoke D2, and a contributor's
local render matches CI by default rather than by discipline.

**The lesson is worth more than the fix.** The first remedy was plausible,
cheap, and wrong, and it took a second failure and a byte-level comparison to
find the real cause. "Generated files must not drift" is easy to write in a
README and takes real work to hold.

### Trade-offs

- A wrapper script between contributors and a tool they may already know, which
  has to be explained everywhere `d2` might be typed — the README,
  `repo-conventions.md`, and this entry.
- Coupled to the shape of D2's output. A future version that changes how it
  emits that id breaks the script, and the failure would be a returning diff
  rather than an error.
- Rendering by hand with `d2` still works and produces output that looks like a
  change. Nothing prevents it; only documentation does.

---

## DEC-010 — `main` is not protected against direct pushes

**Date:** 2026-08-04 · **Decided by:** Dana Whitfield · **Proposed by:** Sofia Marchetti
**Status:** Active

### Decision

Branch protection on `main` does **not** require pull requests. The validation
workflow runs on every pull request and may be marked a required check, but the
"require a pull request before merging" rule stays off.

### Rationale

Forced by DEC-006. `render.yml` pushes generated output directly to `main` using
`GITHUB_TOKEN`. With pull requests required, that push is rejected — the render
job runs green through every step and then fails with a 403 at the final one.

Two related facts, both learned by hitting them:

- Workflow permissions must be **Read and write** in repository settings. The
  `permissions: contents: write` block in the workflow can only narrow what the
  repository already allows; it cannot grant it.
- A required status check only becomes selectable in branch protection after it
  has run at least once, so the check must be allowed to run before it can be
  enforced.

The convention that every change goes through a branch and a pull request is
therefore **policy, not enforcement** — stated in
[standards/pull-request-policy.md](../standards/pull-request-policy.md) and in
[repo-conventions.md](../meta/repo-conventions.md), and kept by agreement.

### Trade-offs

- **The main convention in the repository is unenforced.** Anyone with write
  access can push to `main`, and the branch-per-change rule holds because
  people follow it.
- An accidental direct push is not blocked, only visible afterwards.
- A better arrangement would let the bot bypass the rule while enforcing it for
  humans. Available on some plans; not assumed here, because this repository is
  meant to be clonable by anyone without configuration.

---

## DEC-011 — The demonstration dataset keeps its gaps

**Date:** 2026-08-04 · **Decided by:** Dana Whitfield
**Status:** Active

### Decision

The demonstration inventory retains unknown owners, undetermined hosting,
uncharacterized failure modes, and duplicated capabilities. `Unknown` and `TBD`
are legal schema values rather than validation failures.

### Rationale

A demonstration inventory with no gaps in it teaches the wrong lesson. It
suggests the method's output is a clean catalogue, when the actual output — the
part that turns out to be most valuable — is a list of things the organization
did not know about itself.

If unknowns were invalid, they would be filled with something plausible to make
the build pass, which is the exact failure the whole system exists to prevent.
The `Unknown` value is not an absence of data; it is a recorded finding, and
`gap-analysis.py` reads it as one.

The planted cases each demonstrate something different, and are documented in
[insights-surfaced.md](../inventory/insights-surfaced.md): a retiring system
with no owner still on a live path, a capability covered twice, a synchronous
dependency tiered lower than the path containing it, and an application in
daily use across three functions that nobody in IT can answer a question about.

### Trade-offs

- Readers may mistake the gaps for carelessness. Called out in the README and
  the bootstrap session note, and it will still be misread sometimes.
- Validation cannot enforce completeness, only structure — a record can pass
  every check and say almost nothing.
- The distinction between "we do not know" and "not yet filled in" is not
  expressible in the schema. Both are `Unknown`.

---

*Last updated: 2026-08-04*
