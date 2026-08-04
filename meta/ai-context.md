# AI Context

Context for AI assistants working in this repository. See also [ai-guidance.md](ai-guidance.md) for workflow instructions and [repo-conventions.md](repo-conventions.md) for naming and structure rules.

---

## Project Overview

This repository is a **docs-as-code system** for application architecture, change control, and DevOps documentation — a public reference implementation of a method running in production elsewhere.

**Core principle:** documentation should be readable and usable by both humans and AI models. The repository *is* the context — model memory doesn't persist, so continuity lives in these files.

**The demonstration dataset is fictional.** Northwind Traders is a made-up mid-market building-products distributor. Every application, vendor, person, and transcript in this repo is invented. Do not treat any of it as a real system of record, and do not add anything that implies otherwise.

**The documentation flywheel:**
1. Docs are updated, gaps identified, questions drafted
2. A meeting is recorded with whoever knows the answer
3. Transcript saved to `evidence/meetings/`
4. AI reads the transcript → updates docs, diagrams, processes, decisions
5. New questions surface → repeat

---

## The Demo Cast

Fictional. Used consistently across owner fields, decision records, and example transcripts so the dataset holds together.

| Name | Role | Appears as |
|---|---|---|
| **Dana Whitfield** | IT Director | Approver on decisions and process changes |
| **Marcus Iwu** | Applications Manager | `it_manager` on business applications |
| **Priya Raman** | ERP Analyst | `it_sme` on ERP and finance systems |
| **Sofia Marchetti** | Data & Integrations Lead | `it_sme` on integration platform, EDW, EDI |
| **Tom Bergstrom** | Infrastructure Lead | `it_technical_owner` on hosting and endpoint tools |
| **Ken Oyelaran** | Security Lead | Owner of identity and endpoint security records |
| **Rachel Nkemdirim** | HR Systems Analyst | `it_sme` on HCM and payroll |
| **Alan Petrov** | Service Desk Lead | Owner of service-management tooling |

---

## Technology Stack

| Tool | Purpose |
|---|---|
| **D2** | Diagram-as-code (Terrastruct) — source of all architecture diagrams |
| **Python + PyYAML** | Inventory validation and rendering |
| **GitHub Actions** | Validation gate on PR; render, verify, and publish on merge |
| **Git** | Version control and the audit trail |
| **Markdown + YAML** | Every artifact in the repo |

No databases, no external services, no secrets. Clone and it runs.

---

## D2 Diagram Workflow

1. Author diagrams in `diagrams/source/*.d2`
2. Pipeline renders to `diagrams/rendered/*.svg`
3. SVGs are embedded in markdown with relative paths

`diagrams/source/integration-landscape.d2` is **generated** by `automation/render-inventory.py` from the integration records — do not hand-edit it. Everything else in `source/` is hand-authored.

---

## Current Focus Areas

- [x] Repository skeleton and `meta/` bootstrap layer
- [x] Inventory schema and demo dataset
- [x] Validation and render workflows
- [x] Insights log with worked examples — `inventory/insights-surfaced.md`
- [x] `context/` — the organization, the cast and how each of them thinks, the
      systems landscape as narrative, and the approval matrix
- [x] `decisions/decision-log.md` — DEC-001 to DEC-011, the method and pipeline
      decisions, including one superseded pair kept as a worked example
- [x] `processes/` — the flywheel itself, with a hand-authored diagram
- [x] `evidence/question-register.md` — the collector that drives the loop:
      open questions, people still to be identified, and what has been answered
- [x] `evidence/interviews/` — one prepped brief per person, drafted from the
      register. Three of the eight people in the queue are briefed, which is the
      intended state: you brief the meetings that are actually happening
- [x] `standards/` — pull request policy and PR requirements
- [x] `templates/` — a prompt per recurring job plus the summary template
- [x] Example transcripts and their summaries — two Teams `.vtt` transcripts in
      `evidence/meetings/`, each with a summary. The 2026-03-04 integration
      review is the source six insight rows already cited; the 2026-03-11
      service desk sync is the five-minute counterexample
- [ ] Decision records for the questions the dataset raises — whether an SSO
      trust belongs in the integration model, where the plant boundary sits,
      whether tiering should apply to paths rather than applications. All three
      are recorded as insights and open questions, none is decided
- [ ] `processes/` beyond the flywheel — `repo-conventions.md` uses
      `change-control-process.md` as its worked example and it does not exist
- [x] `context/the-brief/` — the briefing. `slides.html` is a self-contained
      22-slide deck (no build step, no CDN; arrows navigate, **O** overview,
      **F** fullscreen, prints to PDF) and `demo-script.md` is the run-of-show
      with timings, live-demo commands, fallbacks, and the questions the room
      asks. Outline came from `templates/demo.md`.
      **The deck pulls the flywheel diagram by relative path** rather than
      embedding a copy — so it always shows the current render.
      `thumbnail.html` holds three YouTube thumbnail concepts and an OG share
      card. `demo-inputs/` holds **deliberately unprocessed** transcripts with
      an `expected-changes.md` answer key — do not process them. **Two remain:**
      the access review and the legacy order entry follow-up. The infrastructure
      catchup was processed on request on 2026-08-04 and copied into
      `evidence/meetings/`; its staged copy is untouched, so the demo still runs
- [ ] Optional GitHub Pages publishing surface

---

## Session History

AI working sessions are recorded in `evidence/meetings/` with an `-ai` suffix. Add a row here after each one — this table is how the next session catches up.

| Date | File | Topics Covered |
|---|---|---|
| 2026-08-04 | [`2026-08-04-repo-bootstrap-ai.md`](../evidence/meetings/2026-08-04-repo-bootstrap-ai.md) | Initial repo seeding — schema, 17 app and 12 integration records, both automation scripts, generated landscape diagram, CI workflows. Addenda: first push, GitHub Actions setup, and pinning D2 output with a fixed salt |
| 2026-08-04 | [`2026-08-04-context-and-process-seed-ai.md`](../evidence/meetings/2026-08-04-context-and-process-seed-ai.md) | Filled the four folders the README advertised and the repo did not have — `context/`, `decisions/`, `processes/`, `standards/` — plus `templates/`. Decision log DEC-001..011, the flywheel process and its diagram, PR policy, four prompts and the summary template. **Addenda:** the flywheel was missing its collector step (added `evidence/question-register.md`), then its prep and gate ordering (added `evidence/interviews/`, moved the human gate to the middle of the loop, six steps settling into three beats) |

---

*Last updated: 2026-08-04*
