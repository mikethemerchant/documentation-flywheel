# Documentation Flywheel

A working reference implementation of **documentation that maintains itself** — architecture decisions, process documentation, system diagrams, and an application inventory, all held as plain text in one Git repository, validated by CI, and published automatically.

The dataset here is synthetic. The method is not — it's a cleaned-up version of a system running in production inside a mid-market manufacturer, where it documents a few hundred applications and their integrations.

---

## The idea

Most architecture documentation dies the same way: it's written once, in a tool separate from the work, by someone who then becomes the only person who maintains it. Six months later nobody trusts it, so nobody reads it, so nobody updates it.

This repo is built on three commitments that break that loop:

- **Text-as-source** — everything is a human-readable file. Diffable, reviewable, versioned, and readable by an AI assistant. Nothing lives only in a diagramming tool, a spreadsheet, or someone's head.
- **Data-to-docs** — structured source data is *transformed* into views and diagrams automatically. Nothing derived is maintained by hand, so nothing derived can drift.
- **Automation over policy** — the pipeline enforces the rules. A record with an unapproved value doesn't get a stern comment in review; it fails the build.

The published site is a **projection of this repository**, not a separate thing to maintain.

---

## The flywheel

The method that keeps it current:

```
   ┌─────────────────────────────────────────────┐
   │                                             │
   ▼                                             │
docs surface gaps  →  record a meeting you were  │
                      already having             │
                              │                  │
                              ▼                  │
              AI reads the transcript and drafts │
              docs, diagrams, decisions          │
                              │                  │
                              ▼                  │
              human reviews and commits;         │
              pipeline validates and publishes   │
                              │                  │
                              ▼                  │
                    new questions surface  ───────┘
```

The load-bearing detail is step two: **it creates no homework for the expert.** They have a conversation they were going to have anyway. That's why the loop compounds instead of stalling the way documentation initiatives usually do.

The second detail is that **a human reviews and commits everything.** The AI drafts; it does not publish. And the schema is a hard gate — it cannot invent a person into the owner roster, because that roster is a controlled list and an unknown value fails validation.

---

## Repository structure

Each folder answers a question, rather than naming a document type.

| Folder | Question it answers |
|---|---|
| `context/` | What world are we operating in? Constraints, assumptions, non-goals. |
| `decisions/` | Why is it like this? Append-only decision records. |
| `processes/` | How is change supposed to work? The intended operating model. |
| `diagrams/` | How do systems actually connect? `.d2` source is authoritative; SVG is generated. |
| `evidence/` | Show me what actually happened. Transcripts, summaries, metrics. |
| `inventory/` | What applications exist, who owns them, and how do they connect? |
| `standards/` | What rules must every change follow? |
| `templates/` | How do I start a new decision / summary / diagram? |
| `automation/` | What renders and validates all of this? |
| `meta/` | How does this repo work — for humans and for AI assistants? |

---

## The inventory

`inventory/` is the part that demonstrates the most. One YAML file per application, validated against a controlled schema, rendered into every view anybody actually asks for:

| View | Answers |
|---|---|
| `all-applications` | What do we have? |
| `by-vendor` / `by-owner` / `by-team` | Who owns it, who do we buy from, who's accountable? |
| `capability-map` | **What do we already own that does this?** — the overlap question, asked before you buy |
| `integration-matrix` | What talks to what? |
| `dr-posture` | What writes into our core system, and what happens if it's down? |
| per-app pages | Everything known about one application, with its integration neighbourhood |

None of these are written. All of them are generated from the same records, which means they cannot disagree with each other.

**The integration landscape diagram is generated too.** `render-inventory.py` writes a `.d2` file from the integration records, and a later pipeline step renders it to SVG. Nobody draws that diagram. Add an integration record, and the picture redraws itself on merge.

Run `python automation/gap-analysis.py` and it tells you what you don't know yet — which is what feeds the next turn of the flywheel.

---

## Running it

```bash
pip install pyyaml
python automation/render-inventory.py --validate-only   # schema gate
python automation/render-inventory.py                   # generate all views
python automation/gap-analysis.py                       # what's still unknown
```

Diagrams need [D2](https://d2lang.com):

```bash
python automation/render-diagrams.py            # render every .d2 to SVG
python automation/render-diagrams.py --check    # parse only, write nothing
```

That wrapper exists for one reason: D2 scopes each SVG's CSS with a generated
class name that is derived per-platform, so rendering the same source on
Windows and on Linux gives you two files with identical geometry and different
class names. Since the pipeline commits rendered output back, calling `d2`
directly means every push rewrites a diagram nobody edited. The script pins
that id to the diagram's filename instead. Use it rather than `d2` by hand, or
your render will look like a change.

CI does all of this on every push. No secrets, no external services, no accounts — clone it and it works.

### The pipeline

| Workflow | Trigger | What it does |
|---|---|---|
| `validate.yml` | pull request | Validates every record against the schema and parses every diagram. **No writes.** A bad value fails here, before merge. |
| `render.yml` | push to `main` | Renders inventory views, generates the landscape diagram, renders all D2 to SVG, verifies the outputs, commits them back, publishes. |

The verification step is the unglamorous part that makes the rest trustworthy: every app record has a rendered page, every diagram source has an SVG, no generated file is empty. If any of that isn't true, the build fails rather than publishing a half-rendered catalog.

---

## Working with an AI assistant

This repo is designed to be worked on with an AI coding assistant, and `meta/` is how that works. The premise:

> **The repository is the context.** Model memory is per-session, per-machine, and lossy. Continuity has to live in files.

An assistant starting fresh reads `README.md`, then `meta/ai-context.md` (what this project is, who's involved, what's in flight), then `meta/ai-guidance.md` (how to do each recurring task), then `meta/repo-conventions.md` (naming, structure, commit style). It's then current — and so is a new human, which is the same problem solved once.

`templates/` holds a prompt per recurring job — processing a transcript, generating a diagram, writing a decision record. That's what makes the method repeatable rather than personal.

---

## Honest scope

**This is a reference implementation, not a product.** It's here to show a method concretely enough to steal. Issues and discussion are welcome; PRs probably won't be merged, because keeping it small is the point.

**The data is fictional.** Northwind Traders doesn't exist, and neither does anyone in the owner roster. The portfolio is deliberately small (~17 applications) so the generated diagrams stay readable, and deliberately imperfect — a few records have unknown owners, because a demo dataset with no gaps in it teaches the wrong lesson.

**What it's not:** an enterprise architecture tool, a CMDB, or a replacement for one. If you need lifecycle workflows, cost modelling, and a hundred stakeholders in a UI, buy something. This is for the case where you have none of that, need the answers anyway, and would rather own portable text than a subscription.

---

## License

MIT. Take it apart.
