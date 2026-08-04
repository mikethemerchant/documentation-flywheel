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

0. Transcripts are WebVTT (`.vtt`), as Teams exports them. **Never edit one** — it is evidence. Transcription mangles proper nouns (*Meridien*, *the I pass*); resolve from context and write the correct form everywhere else

> **The three `.vtt` files in `context/the-brief/demo-inputs/` are deliberately
> unprocessed.** They are staged live-demo input and are the only transcripts in
> the repo that correctly have no summary. Do not process them unprompted — the
> expected output of each is documented in that folder's `expected-changes.md`,
> and processing them ahead of time destroys the demo. If asked to run one,
> copy it into `evidence/meetings/` first.
1. Read the full transcript from `evidence/meetings/`
2. Cross-reference existing docs — including `evidence/question-register.md`, which says what this conversation was meant to answer — to separate genuinely new information from restatement
3. **Propose changes before making them** — list the file paths and what changes in each
4. Update processes, D2 source, decisions, and inventory records as needed
5. **Always create a `.md` summary alongside the transcript.** This is the linkable artifact and the proof the transcript was processed. *A transcript without a summary has not been processed.*
6. **Update `evidence/question-register.md`** — close what was answered, append what was raised, and record anyone named only as a role in the people-to-identify table
7. **Prep the next round in the same pull request** — re-run the gap analysis, reconcile the register, refresh the briefs in `evidence/interviews/`

Summary structure: date / participants / transcript link → purpose → key topics as tables → questions closed → action items with owners → documents updated as a result → open questions.

Full prompts: [`templates/prompt-process-transcript.md`](../templates/prompt-process-transcript.md), then [`templates/prompt-prepare-interview.md`](../templates/prompt-prepare-interview.md).

**Step 7 is the one that keeps the loop turning.** A pull request that closes out a conversation without prepping the next one leaves somebody to work out what happens next, and that is where these processes stall.

---

## The Question Register

`evidence/question-register.md` is the collector that drives the loop. It is
the durable copy of what is unknown; a meeting summary's open-questions section
is a snapshot of it.

Three tables, and the middle one is the one people skip:

| Table | Holds |
|---|---|
| Open questions | What is not known, who can answer it, where the gap came from |
| **People to identify** | Roles named as "you'd have to ask…" and never resolved to a person |
| Answered | Closed questions with the conversation that closed them — kept, never deleted |

Sorted by who can answer, the register **is** the interview list. Rows arrive
from `gap-analysis.py`, from `insights-surfaced.md`, and from conversations
that raised more than they closed.

A role in the people-to-identify table does **not** go into `schema.yaml`. The
roster is the controlled list of people who own records; the register is a list
of people to find. They join the roster if they turn out to own something.

Never close a row by filling the underlying field with a plausible guess.

---

## Interview Briefs

`evidence/interviews/<person-slug>.md` — one living file per person, refreshed
every round. This is what the register is *for*: a backlog nobody turns into a
prepared question stays a backlog.

Prompt: [`templates/prompt-prepare-interview.md`](../templates/prompt-prepare-interview.md).
Template: [`templates/interview-brief-template.md`](../templates/interview-brief-template.md).

Four things a brief must do that a filtered register view does not:

1. **Rewrite each question as speech.** `Q-009 — hosting: TBD` becomes *"Where
   does the historian actually run — is there a box in the plant, or is it in
   the DC?"* Nobody asks a useful question by reading a table row aloud.
2. **Carry the framing from [`context/people.md`](../context/people.md).** Tom
   answers in recovery windows; the same question asked as a modelling question
   gets a shrug and asked as a recovery question gets an answer.
3. **Say what a good answer looks like**, per question. Knowing when to stop
   pushing is the hard part live and cannot be improvised.
4. **Include a *do not ask* section.** Their time is the scarce resource in this
   whole method. Asking something they answered two months ago tells them the
   last conversation was wasted, and that is the one move that damages the
   relationship the process runs on.

**Only brief people with a meeting actually coming up.** Three or four per
round. Briefs for meetings that are not happening are the start of the pile of
documents nobody reads.

**Briefs are drafted, not generated** — unlike almost everything else derived
here. The register is prose rather than structured data, and the value is in
the framing, which is a judgment call. So a human reviews them like anything
else.

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
