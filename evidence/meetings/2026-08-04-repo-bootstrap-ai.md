# Repository Bootstrap — AI Session

**Date:** 2026-08-04
**Type:** AI working session (no human participants beyond the reviewer)
**Reviewer:** Michael Bender

---

## Purpose

Seed the public `documentation-flywheel` repository from the prepared seed kit:
the README and `meta/` bootstrap layer, the inventory schema, the demo dataset,
the two automation scripts, and the CI workflows.

This repository is a clean-room rebuild. The method it demonstrates runs in
production elsewhere; **none of that system's data was in reach during this
session and none of it is in this repository.** Every application, vendor,
person, integration, and metric here is invented.

---

## What was built

| Area | Result |
|---|---|
| Structure | `inventory/`, `automation/`, `diagrams/`, `evidence/`, `meta/`, `.github/workflows/`. Only folders with content were created. |
| Schema | `inventory/schema.yaml` — controlled values for every enum field across both record types. |
| Applications | 17 records in `inventory/apps/data/`. |
| Integrations | 12 records in `inventory/integrations/data/`. |
| Renderer | `automation/render-inventory.py` — schema gate plus 7 summary views, 17 detail pages, and the landscape diagram source. |
| Gap report | `automation/gap-analysis.py` — plain-text register of what is still unknown. |
| Diagram | `diagrams/source/integration-landscape.d2` generated from the integration records; rendered to SVG with D2 v0.7.1, the version pinned in CI. |
| Insights | `inventory/insights-surfaced.md` seeded with 10 rows drawn from the dataset's own gaps. |

---

## Decisions taken during the session

| Decision | Rationale |
|---|---|
| Added a controlled `capability` field to the schema | `capability-map.md` was a required view and nothing in the schema could express what an application *does*. Grouping by `primary_users` answers "who uses it", not "what do we already own that does this". Controlled rather than free text, because as free text two records covering the same ground never collide and the overlap stays invisible. |
| Integration filenames use the full source and target slugs | `repo-conventions.md` states the `<source-slug>--<target-slug>` rule and ships publicly; the dataset design abbreviated one of them. The normative document wins. |
| Core system of record is derived, not configured | The renderer computes it as the application the most other systems write into. Hard-coding a slug would make the renderer wrong the first time the portfolio changed, and the integration records already carry the fact. |
| Landscape diagram lays out `down`, not `right` | Keeps the aspect ratio near 2:1 and puts the team containers side by side, so the flows converging on the core system are the first thing a reader sees. |
| Local branch renamed `master` → `main` | Both workflows, the README pipeline table, `ai-guidance.md`, and `repo-conventions.md` all reference `main`. One branch rename against five documents was the cheaper correction. |

---

## Deliberate imperfections, kept

The dataset is not clean, on purpose. A demo inventory with no gaps teaches the
wrong lesson and looks staged.

| Gap | Count | Where |
|---|---|---|
| Applications with no SME | 3 | Electronic Signature, Legacy Order Entry, Plant Historian |
| Hosting not determined | 2 | Plant Historian, Travel & Expense |
| Integrations with unknown DR impact | 2 | Legacy → ERP, SSO → HCM |
| Applications with no integration records | 4 | Electronic Signature, Endpoint Management, Integration Platform, Travel & Expense |
| Capability covered more than once | 4 capabilities | Expense Management is the planted one |

The headline case is **Legacy Order Entry**: marked Retiring, no owner, still
writing orders into the ERP through a manual flat file whose failure mode
nobody has characterized. The gap report and the DR posture view both surface
it from different directions. A spreadsheet inventory would show it as
Retiring and stop there.

`Integration Platform (iPaaS)` appearing in the unconnected list is a true
statement about the data and a false impression about the system — it is
middleware, so it is the path rather than an endpoint. That is worth pointing
at rather than tidying away.

---

## Verification performed

- `render-inventory.py --validate-only` passes: 17 applications, 12 integrations.
- The gate was tested by breaking records on purpose. An unapproved vendor, a
  team name in a person-only field, an undefined field, and a dangling
  integration target were all caught, each naming the file, the field, and the
  offending value. Records restored afterwards.
- Full render produces 7 views, 17 detail pages, and the `.d2` source.
- D2 v0.7.1 compiles the generated source to SVG.
- `gap-analysis.py` returns 12 open gaps and exits 0.
- The `Verify rendered outputs` step from `render.yml` was run locally against
  the working tree and passes.

---

## Action items

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Publishing safety sweep | Michael Bender | Open — repository was published before this ran |
| 2 | Non-technical review pass | Michael Bender | Open |
| 3 | Video scrub checklist | Michael Bender | Open |
| 4 | Push `main` and set it as the default branch on the remote | Michael Bender | **Done** — `main` pushed and set as default |
| 5 | Write the example transcripts and their summaries | Next session | Open |
| 6 | Decide whether an SSO trust belongs in the integration model, and record it as a decision | Next session | Open |
| 7 | Delete the `master` branch once the default has moved to `main` | Michael Bender | **Done** — deleted; it was an ancestor of `main` |
| 8 | Confirm the render loop stays quiet — a push to `main` should produce no auto-render commit | Next session | **Done** — Render #3 committed nothing back |

---

## Addenda — first push, same day

Recorded after the session above, because the pipeline's first real run
disproved one of its conclusions.

### The seed kit lives outside the repository

`EXAMPLES.md` (the dataset design — portfolio table, integration table, the
people roster, and the specification of which gaps are deliberate) and the
original bootstrap prompt were moved to **`c:\repos\documentation-flywheel-seed\`**.
Neither ships. `EXAMPLES.md` is the reference to reach for when extending the
dataset.

### GitHub Actions setup, confirmed rather than predicted

- **Settings → Actions → General → Workflow permissions must be "Read and
  write."** The `permissions: contents: write` block in `render.yml` can only
  narrow what the repository already allows; it cannot grant it. Without the
  repository setting, the render job runs green through every step and then
  fails with a 403 on the push.
- The branch rename left the local branch tracking `refs/heads/master`.
  `git branch -m` preserves the old upstream, so a plain `git push` silently
  pushed to `master` and **no workflow fired at all** — both triggers are
  `main`-only.
- `validate.yml` runs on pull requests but does not block merges until the
  check is marked required in branch protection, and it only becomes selectable
  there after it has run once.
- **Do not require pull requests on `main`.** `render.yml` pushes generated
  output straight to the branch with `GITHUB_TOKEN`; that rule blocks the bot
  and the job 403s at the final step.

### The pipeline caught derived-file drift on its first run

The first render on `main` committed back a 284-line SVG diff. Every markdown
view and the `.d2` source were byte-identical and the diagram geometry matched
exactly — the `viewBox` was the same to the pixel. The only difference was the
CSS class name D2 generates to scope each SVG, which is derived per-platform.

Left alone, every push to `main` would have rewritten that SVG, which is
precisely the drift this repository claims to prevent.

**The first fix was wrong.** `d2 --salt <value>` looked like the answer and is
not: it changes the generated id without making it platform-independent. After
merging it, the pipeline committed the SVG back a second time — Windows
produced `d2-1594564165` and the runner produced `d2-1681756903`, both salted,
both different.

What settled it was proving the id is the *only* difference. Normalizing the id
out of both files gave byte-identical SVGs, so the geometry, styling, and
embedded fonts were never in question. `automation/render-diagrams.py` now
renders every diagram and rewrites D2's generated id to one derived from the
diagram's filename — stable across platforms because nothing about the machine
feeds into it, and still unique per diagram, which is the property D2 wanted
from the hash in the first place. Both workflows call that script, so they
cannot drift apart in how they invoke D2.

Worth keeping as a story rather than just a fix, for two reasons. The
verification step existed to catch a half-rendered catalog, and what it
actually caught was the pipeline disagreeing with a contributor's laptop about
a file neither of them had edited. And the first remedy was plausible, cheap,
and wrong — it took a second failure and an actual byte-level comparison to
find the real cause. "Generated files must not drift" is easy to write in a
README and takes real work to hold.

---

## Documents updated as a result

- `meta/ai-context.md` — session history row, focus areas, last-updated date
- `meta/ai-guidance.md`, `meta/repo-conventions.md` — last-updated dates
- `inventory/schema.yaml` — added the `capability` field
- `.github/workflows/render.yml` — create `diagrams/rendered/` before rendering
