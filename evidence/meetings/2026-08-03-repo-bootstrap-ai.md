# Repository Bootstrap — AI Session

**Date:** 2026-08-03
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
| 1 | Publishing safety sweep before the repository goes public | Michael Bender | Open |
| 2 | Non-technical review pass | Michael Bender | Open |
| 3 | Video scrub checklist | Michael Bender | Open |
| 4 | Push `main` and set it as the default branch on the remote | Michael Bender | Open |
| 5 | Write the example transcripts and their summaries | Next session | Open |
| 6 | Decide whether an SSO trust belongs in the integration model, and record it as a decision | Next session | Open |

---

## Documents updated as a result

- `meta/ai-context.md` — session history row, focus areas, last-updated date
- `meta/ai-guidance.md`, `meta/repo-conventions.md` — last-updated dates
- `inventory/schema.yaml` — added the `capability` field
- `.github/workflows/render.yml` — create `diagrams/rendered/` before rendering
