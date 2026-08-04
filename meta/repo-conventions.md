# Repository Conventions

How files are named, organized, and maintained.

---

## File Naming

| Type | Pattern | Example |
|---|---|---|
| Process docs | `kebab-case.md` | `change-control-process.md` |
| D2 diagrams | `kebab-case.d2` | `integration-landscape.d2` |
| Meeting summaries | `YYYY-MM-DD-description.md` | `2026-03-04-erp-integration-review.md` |
| AI session notes | `YYYY-MM-DD-description-ai.md` | `2026-03-01-repo-bootstrap-ai.md` |
| Inventory records | `kebab-case.yaml` | `warehouse-management.yaml` |
| Decision records | `DEC-NNN` prefix in `decisions/decision-log.md` | `DEC-001: Docs-as-Code` |

---

## Inventory Record Naming

These rules were learned the hard way. The rationale matters more than the rule.

- **The vendor goes in the `vendor` field, not the `name`.** Use `name: Warehouse Management (WMS)` + `vendor: Meridian Systems`, not `name: Meridian Warehouse Management`. A name carrying its vendor fights every filter and grouping built on top of it.
- **Put the common short name or acronym in parentheses** so it's searchable: `Product Name (ShortName)`. Omit it when there isn't a widely-used short form.
- **Slugs are internal identifiers and do not change** when a display name is reworded. Integration records reference apps by slug; renaming one silently breaks the graph. A slug may keep a legacy form its display name has moved on from — that's fine, and preferable to a broken reference.
- **Owners and SMEs are people, never groups.** `it_sme`, `it_technical_owner`, `it_manager`, and `recovery_owner` hold real individuals. When several people genuinely share a role, list them all as a YAML list. **Team-level accountability has its own field:** `it_team_accountable`.

  *Why this one is strict:* a group name in an owner field is a valid value that answers nothing. "Infrastructure owns it" doesn't tell you who to call, and it degrades invisibly — the record still looks complete long after everyone who knew the system has moved on. A person's name goes stale loudly, which is the behaviour you want.

| Field | Do | Don't |
|---|---|---|
| `name` | `Enterprise Data Warehouse (EDW)` | `Lumen Enterprise Data Warehouse` |
| `vendor` | `Lumen Analytics` | *(blank, or folded into the name)* |
| `it_sme` (shared) | `Priya Raman / Sofia Marchetti` | `Applications`, `Data team` |

---

## Folder Rules

| Folder | What goes here | What does NOT |
|---|---|---|
| `diagrams/source/` | `.d2` files only | Any rendered output |
| `diagrams/rendered/` | Pipeline-generated SVGs only | Hand-edited files |
| `evidence/meetings/` | Transcripts and their `.md` summaries | Process docs or decisions |
| `evidence/metrics/` | Raw data exports | Processed or edited data |
| `inventory/apps/data/` | One `.yaml` per application | Rendered markdown |
| `inventory/rendered/` | Generated views | Anything hand-written |
| `decisions/` | Immutable decision records | Drafts or working documents |
| `processes/` | Finalized process documentation | Meeting notes or evidence |

**Folders are created when first needed.** The README documents the full map; empty folders aren't committed.

---

## Generated vs. Authored

The single most important distinction in the repo. Editing a generated file wastes the edit — it's overwritten on the next merge.

| Generated (never edit) | Authored (edit freely) |
|---|---|
| `diagrams/rendered/*.svg` | `diagrams/source/*.d2` — except the one below |
| `diagrams/source/integration-landscape.d2` | `inventory/apps/data/*.yaml` |
| `inventory/rendered/*` | `inventory/integrations/data/*.yaml` |
| `inventory/apps/*.md` | `inventory/schema.yaml` |

---

## Commit Messages

- Pipeline auto-commits: `Auto-render diagrams and inventory [skip ci]`
- Human commits: descriptive, present tense — `Add tax engine integration records`
- No strict format enforced — keep it readable

**Branch per change; never commit to `main` directly.**

---

## Document Structure

**Process documents:** title and purpose → scope (what's covered, what isn't) → roles → step-by-step procedure → exceptions and edge cases → link to the related diagram.

**Meeting summaries:** date, participants, transcript link → purpose → key topics as tables → action items with owner and status → documents updated as a result.

**Decision records:** `DEC-NNN` → date and who decided → status (Active / Superseded by DEC-NNN) → the decision statement → rationale → trade-offs.

---

## Diagrams

- Author in D2 in `diagrams/source/`; the pipeline renders SVG on merge
- **Render with `python automation/render-diagrams.py`, never with `d2`
  directly.** D2 scopes each SVG's CSS with a generated class name derived
  per-platform, so a bare `d2` render on Windows and one on Linux differ in
  class names while being pixel-identical. Because the pipeline commits
  rendered output back, that difference becomes an auto-render commit on every
  push. The script pins the id to the diagram's filename. (`--salt` does not
  solve this — it changes the id without making it platform-independent.)
- Embed rendered SVGs with relative paths
- **Avoid tooltips and animations** — many markdown renderers sanitize them away. Put context in a notes section in the diagram source instead.
- Every `.d2` must produce an `.svg`; the pipeline fails the build if one doesn't

---

*Last updated: 2026-08-04*
