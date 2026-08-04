# AI Guidance

Instructions for AI assistants working in this repository. Read alongside [ai-context.md](ai-context.md) at the start of each session.

---

## Key Conventions

- **File naming:** `kebab-case.md` for docs, `YYYY-MM-DD-description.md` for meeting summaries, `-ai.md` suffix for AI session notes. Full rules in [repo-conventions.md](repo-conventions.md).
- **Diagrams:** author in D2 (`diagrams/source/`), pipeline renders to SVG. **Never edit a rendered SVG** — it is overwritten on every merge.
- **Decisions:** append-only. Never modify a past decision; add a new one that supersedes it, and mark the old one superseded.
- **Generated files:** anything in `inventory/rendered/`, `inventory/apps/*.md`, `diagrams/rendered/`, and `diagrams/source/integration-landscape.d2` is machine-written. Edit the source data, re-render, never hand-patch the output.
- **Everything here is fictional.** When adding records or examples, invent them in keeping with the existing demo cast and vendor set. Never introduce a real company's internal data.

---

## When Processing a Meeting Transcript

1. Read the full transcript from `evidence/meetings/`
2. Cross-reference existing docs to separate genuinely new information from restatement
3. **Propose changes before making them** — list the file paths and what changes in each
4. Update processes, D2 source, decisions, and inventory records as needed
5. **Always create a `.md` summary alongside the transcript.** This is the linkable artifact and the proof the transcript was processed. *A transcript without a summary has not been processed.*
6. Surface new questions and action items for the next conversation

Summary structure: date / participants / transcript link → purpose → key topics as tables → action items with owners → documents updated as a result.

---

## When Updating the Application Inventory

- One YAML file per application in `inventory/apps/data/`, validated against `inventory/schema.yaml`
- One YAML file per integration in `inventory/integrations/data/`
- Validate before committing: `python automation/render-inventory.py --validate-only`
- Render locally to check output: `python automation/render-inventory.py`
- Find what's still unknown: `python automation/gap-analysis.py`

**Adding a new controlled value** (a vendor, a person, a team) means editing `schema.yaml` in the same change. That's deliberate friction — it's what stops the roster drifting into free text.

**Slugs are permanent.** A filename is an internal identifier referenced by integration `source`/`target` fields. Rewording a display name never renames the file.

---

## When Capturing Insights

`inventory/insights-surfaced.md` is a running register of organizational issues the documentation process *exposed as a byproduct* — not problems with the docs, problems the docs revealed.

After processing any interview transcript, ask:

1. Did the SME say "I don't know" or "you'd have to ask X" in a way that revealed an ownership gap?
2. Did they flag a single point of failure ("if X leaves…")?
3. Did they surface an application that wasn't on the list?
4. Did they describe something used across the business that nobody owns or has standardized?
5. Did they flag a retirement with no date attached?

If yes — add a row with category, a one-line insight, and the source. This register is often more valuable than the catalog it falls out of.

---

## Style Guidelines

- **Keep it simple enough that people actually read it.** Complexity is the failure mode, not incompleteness.
- Tables for structured data, bullets for procedures
- Link to evidence wherever a claim came from a specific conversation
- Write for a reader browsing the rendered markdown, not just the raw file

---

## Git Workflow

- **Branch per change. Never commit directly to `main`.**
- Re-check `git branch --show-current` before every commit — a merge can leave you back on `main` without noticing.
- Descriptive commit messages; the pipeline's own commits are `Auto-render diagrams and inventory [skip ci]`.

---

*Last updated: 2026-08-04*
