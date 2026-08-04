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
- [ ] Example transcripts and their summaries — the flywheel's input side is
      described but not yet demonstrated, which is the largest remaining gap
- [ ] `templates/` — a prompt per recurring job, referenced by the README
- [ ] `decisions/` — the open questions the dataset raises are recorded as
      insights but not yet as decision records
- [ ] Optional GitHub Pages publishing surface

---

## Session History

AI working sessions are recorded in `evidence/meetings/` with an `-ai` suffix. Add a row here after each one — this table is how the next session catches up.

| Date | File | Topics Covered |
|---|---|---|
| 2026-08-04 | [`2026-08-04-repo-bootstrap-ai.md`](../evidence/meetings/2026-08-04-repo-bootstrap-ai.md) | Initial repo seeding — schema, 17 app and 12 integration records, both automation scripts, generated landscape diagram, CI workflows. Addenda: first push, GitHub Actions setup, and pinning D2 output with a fixed salt |

---

*Last updated: 2026-08-04*
