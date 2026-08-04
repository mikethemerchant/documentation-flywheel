# Context, Decisions, Process, Standards, and Templates — AI Session

**Date:** 2026-08-04
**Type:** AI working session (no human participants beyond the reviewer)
**Reviewer:** Michael Bender
**Branch:** `add-process-docs`

---

## Purpose

Fill the folders the README advertises and the repository did not have.

Four of the ten folders in the README's structure table — `context/`,
`decisions/`, `processes/`, and `standards/` — did not exist on disk, along
with `templates/`, which the README describes as "a prompt per recurring job".
The convention is that folders are created when first needed, so this was
consistent rather than broken, but a reader following the table hit five
missing folders in a row.

Everything written here is fictional demonstration content in keeping with the
existing Northwind Traders dataset.

---

## What was built

| Folder | Files | What it holds |
|---|---|---|
| `context/` | 4 | The organization and its constraints, the cast and how each of them thinks, the systems landscape as narrative, and the approval matrix |
| `decisions/` | 1 | `decision-log.md`, DEC-001 to DEC-011 |
| `processes/` | 1 | The documentation flywheel itself |
| `standards/` | 1 | Pull request policy |
| `templates/` | 5 | Three prompts named by the README, one more for inventory records, and the meeting summary template |
| `diagrams/source/` | +1 | `documentation-flywheel.d2`, hand-authored, rendered to SVG |

### `context/`

| File | Answers |
|---|---|
| `organization.md` | Who Northwind is, the six fixed constraints, the stated assumptions, the non-goals, and what is known to be missing from the picture |
| `people.md` | The roster, and a paragraph per person on **how they think** — Priya answers in transaction paths, Tom in recovery windows, Alan in tickets |
| `systems-landscape.md` | The portfolio as narrative: the core, the two doors, vendor concentration, the reporting stack, identity, and the edges |
| `decision-rights.md` | Who approves what, the freeze window, spend thresholds, and five places the approval model leaks |

`people.md` was written for a specific job beyond colour: an assistant
processing a transcript needs to know that a hedge from Tom ("roughly four
hours, but we've never tested it") carries information that the record's
`rto: 4 hours` destroys. The "how they think" column is what makes restatement
distinguishable from new information.

`systems-landscape.md` deliberately carries **no field values**. Everything
specific about an application lives in the records and is rendered; the file
holds only what the records cannot — history, intent, and why the graph has the
shape it does. A restated field value is a second copy that eventually
disagrees.

### `decisions/decision-log.md`

Eleven entries, each with decision / rationale / trade-offs per
`repo-conventions.md`.

DEC-001 to DEC-005 are method decisions: text in Git, D2 as source, the
controlled schema, people-not-teams in owner fields, permanent slugs.
DEC-006 to DEC-010 are the pipeline decisions actually taken while building
this repository — committing generated output, deriving the core system,
the D2 id problem, and why `main` cannot require pull requests. DEC-011 records
that the dataset keeps its gaps on purpose.

**DEC-008 is retained wrong.** The `--salt` fix for the D2 drift problem is
written up in full, with its original reasoning, and marked superseded by
DEC-009. That pair is the reason the log is append-only, and having a worked
example of a supersession in the demo dataset is worth more than a log where
every entry happens to be correct.

### `processes/documentation-flywheel.md`

The flywheel as a process document: purpose, scope, roles, the five steps,
why the summary is mandatory, why insights are a first-class output, and nine
exceptions and edge cases.

The step-2 framing is the load-bearing part and is stated as directly as
possible: **do not schedule a documentation session.** Find a meeting that is
already happening and ask the questions there. Every conventional approach
eventually asks the expert to write something, and that is the point at which
it stops.

### `standards/pull-request-policy.md`

Seven numbered requirements, each with what enforces it — the pipeline or a
reviewer. Deliberately short.

The section that matters most says the quiet part: branch protection on `main`
does not require pull requests and cannot, because `render.yml` pushes
generated output straight to the branch. **The main convention in the
repository is unenforced and holds by agreement.** Stating that plainly is
better than implying a gate that is not there.

### `templates/`

| File | For |
|---|---|
| `prompt-process-transcript.md` | Step 5 of the flywheel — seven steps, propose-before-writing, and the six-question insight checklist |
| `meeting-summary-template.md` | The document the prompt above produces |
| `prompt-write-decision-record.md` | Including the four tests a decision must pass before it earns an entry, and the supersession mechanics |
| `prompt-generate-diagram.md` | Hand-authored D2, opening with the question of whether it should be generated instead |
| `prompt-add-inventory-record.md` | Application and integration records, naming rules, and why `Unknown` beats a guess |

The transcript prompt ends with a short section addressed to the human running
it rather than to the model. The most useful line in it: if the assistant
proposes something wrong, ask why it thought that before correcting it — the
answer is often that a document in `meta/` or `context/` is misleading, which
is a bug worth fixing rather than a model error.

---

## Decisions taken during the session

| Decision | Rationale |
|---|---|
| The decision log is written **in-universe**, decided by the fictional cast | The alternative was two logs, or one log mixing Dana Whitfield with the repository's actual author. Mixing reads as a mistake. A note at the top says DEC-006 to DEC-010 are the real choices made while building this repository, recorded as one organization's log — honest, and more useful to someone stealing the method. |
| Decisions are dated across February to August rather than all on one day | Eleven entries dated identically reads as a batch import, not a log. The February and March dates match the 2026-03-04 integration review the insight register already cites, so the timeline holds together. |
| DEC-008 kept in full, unedited, and wrong | The convention is append-only supersession. A demo dataset that states the rule without ever exercising it does not demonstrate it. This is the same argument as DEC-011 applied to the decision log. |
| `context/systems-landscape.md` carries no field values | Anything that duplicates a record will disagree with it. The file was cut back twice to hold only what the records structurally cannot. |
| Wrote a flywheel diagram rather than reusing the README's ASCII | `repo-conventions.md` requires a process document to link its related diagram. The ASCII in the README is fine for a landing page and is not a diagram the repository maintains. It also gave the repo a second hand-authored `.d2`, which proves the id-pinning fix works for more than one file. |
| Five templates rather than the three the README names | The README names transcript, diagram, and decision. Inventory records are the highest-frequency recurring job in the repo and had no prompt; the summary template is the artifact the transcript prompt produces and was referenced in three places before it existed. |
| Left the change-control process unwritten | `repo-conventions.md` uses `change-control-process.md` as its filename example, so it is now the most conspicuous absence. Writing it was out of scope for this session; recorded as an open focus area instead of half-done. |

---

## Verification performed

- `render-inventory.py --validate-only` — passes, 17 applications, 12 integrations.
- Full render — regenerated every view and page with **no diff**. Generated
  output is unchanged by this session, which is the expected result: no source
  record was touched.
- `gap-analysis.py` — 12 open gaps, exits 0. Unchanged, as expected.
- `render-diagrams.py` — both diagrams render; `integration-landscape.svg` is
  byte-identical after a full re-render on Windows, confirming the DEC-009 fix
  still holds with a second diagram in the folder.
- `render-diagrams.py --check` — both sources parse.
- The `Verify rendered outputs` step from `render.yml` run locally against the
  working tree: 2 SVG, 7 rendered MD, full coverage, no empty files.
- Every relative markdown link in the 15 new and modified files resolves.
  The only unresolved targets are intentional: placeholders in the templates,
  and the summary template's `../../` paths, which resolve from
  `evidence/meetings/` where it gets copied.

---

## Open questions and action items

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Write the example transcripts and their summaries. This remains the largest gap — the input side of the flywheel is now described in detail and still not demonstrated. | Next session | **Done** — see the third addendum. Two `.vtt` transcripts with summaries. |
| 2 | Decide whether an SSO trust belongs in the integration model, and record it as a decision record | Next session | Open |
| 3 | Write `processes/change-control-process.md`, which `repo-conventions.md` names as its example | Next session | Open |
| 4 | Decide whether criticality tiering should apply to paths rather than applications — the tax engine case | Next session | Open |
| 5 | Settle the plant boundary question, which decides who patches the historian | Next session | Open |
| 6 | Consider whether the README's structure table should link the folders now that most of them exist | Michael Bender | Open |

Items 2, 4, and 5 are the dataset's own open questions. They have been recorded
as insights since bootstrap and are deliberately still undecided — a repository
where every question raised has already been answered would not look like one
anybody was actually using.

---

## Documents updated as a result

- `meta/ai-context.md` — focus areas rewritten against what now exists, and a
  session history row added

No source record, script, workflow, or generated file was modified.

---

## Addendum — the missing step, same day

Recorded after the session above, because review found the flywheel was
describing a loop it could not actually run.

### What was missing

The process as first written went straight from "docs surface gaps" to "record
a conversation", with the gaps existing only as `gap-analysis.py` output and
whatever the last summary happened to note. **Nothing held them between turns.**

That works exactly once. On the second turn you rediscover what the first turn
already knew was missing, and any question nobody happened to remember has
quietly disappeared. In practice the loop then runs on whoever remembers the
most — which is the single-owner failure this whole repository exists to
prevent, reintroduced at the process layer.

The reviewer had run a version of this method before, with a running markdown
file that collected gaps *and the people identified for interview*, and used it
to decide who to talk to next. That file was the missing step.

### What was added

**`evidence/question-register.md`** — the collector. Three tables:

| Table | Holds | Rows now |
|---|---|---|
| Open questions | What is unknown, who can answer, where the gap came from | 20 |
| **People to identify** | Roles named as "you'd have to ask…" and never resolved to a person | 5 |
| Answered | Closed questions with the conversation that closed them | 3 |

Populated from the dataset's own material: all 12 gaps from `gap-analysis.py`,
the questions implied by the 10 insight rows, and the open items from this
session. Questions are `Q-NNN`, matching the `DEC-NNN` convention.

Sorted by who can answer, the register **is** the interview list — which is the
whole function. The queue at the top carries a *next opportunity* column rather
than a priority score, because the useful ordering is not "most important
question" but "most important question I can ask this Thursday".

**The people-to-identify table is the part worth stealing.** Three of the
twenty open questions are blocked on finding a person rather than on scheduling
one, and nothing else in the repository would surface that. A question waiting
on a calendar gets asked eventually; a question waiting on somebody going
looking sits forever. Making that a separate table with its own status makes
the difference visible.

A role in that table deliberately does **not** go into `schema.yaml`. The
roster is the controlled list of people who own records; the register is a list
of people to find. They join the roster if they turn out to own something.

### What changed as a result

| File | Change |
|---|---|
| `processes/documentation-flywheel.md` | New step 2; steps renumbered to six. Register added to scope, roles, and the exceptions table. "Why it works" is now four properties — *the register is the memory* is the new one. |
| `diagrams/source/documentation-flywheel.d2` | Register node added, with a return edge from the drafting step. Three bold boxes now, not two. |
| `README.md` | Flywheel diagram redrawn with the register; the three load-bearing details are now three rather than two |
| `meta/ai-guidance.md` | Transcript step 6 rewritten; new Question Register section |
| `meta/repo-conventions.md` | `Q-NNN` naming convention; `evidence/` root folder rule |
| `templates/prompt-process-transcript.md` | Step 6 rewritten from "surface what is open" to "update the register", with the people-to-identify instruction |
| `templates/meeting-summary-template.md` | New Questions Closed section; open questions must be mirrored into the register |
| `inventory/insights-surfaced.md` | States the distinction — insights are what was found, questions are what is still unknown — and adds "who could close it?" as the second question after every insight |
| `context/people.md` | The roster is not everyone who matters, only everyone who owns a record |
| `context/decision-rights.md` | Three of the five approval leaks are blocked on a person, not a decision |

### Worth keeping as a note

The original process document was internally consistent, well cross-linked, and
described a loop that would have run down after one turn. Nothing in validation
would have caught that — it is prose, and prose passes every gate in this
repository. It took someone who had operated the method noticing that a step
they relied on was not on the page.

Which is a fair argument for the thing the repository already claims: the
pipeline can enforce structure, and only a person can tell you the process is
missing a step.

---

## Documents updated in the second addendum

Listed in the table above. Additionally:

- `evidence/question-register.md` — new
- `diagrams/rendered/documentation-flywheel.svg` — re-rendered via
  `render-diagrams.py`; `integration-landscape.svg` unchanged, confirming the
  DEC-009 id pinning still holds

---

## Second addendum — the prep, and where the gate belongs

Same day, same review. The register gave the loop a memory; it still did not
say who does the work, when, or what somebody actually walks into a room with.

### The two problems

**The register is not usable in a meeting.** It is a data structure — twenty
rows with IDs, sources, and statuses. Nobody has ever asked a good question by
reading a table row out loud. Something had to turn rows into speech, and
nothing did.

**The gate was in the wrong place.** The process had the human approving at the
*end* of a turn, after the conversation had been processed. That is the natural
place to put it and it is wrong: it means the interviewer walks into the
conversation with whatever is on a branch, unreviewed, and the published
documentation is one turn behind the room.

### What changed

**Steps 1 to 3 are now the assistant's prep, and they happen before the gate.**
Run the gap analysis, reconcile the register, write the briefs. **Step 4 is the
human gate, sitting in the middle of the loop rather than at the end.** On
merge, two things are true at once: the published documentation is current, and
the brief for the next conversation is live and reviewed. Steps 5 and 6 are the
conversation and its processing — and step 6 *is* steps 1 to 3 for the next
round.

**One pull request carries both the closeout of the last conversation and the
prep for the next one.** That is the whole shape of the change. After the first
turn it settles into three beats — approve, talk, process — and no beat ends
with "somebody should work out what happens next", which is where processes
like this normally stop.

**`evidence/interviews/<person-slug>.md`** — one living brief per person.
Three written, from the top of the register's queue:

| Brief | Meeting | Questions |
|---|---|---|
| `sofia-marchetti.md` | Integration standup, weekly | 4 — three of them about whether the model can describe what she operates |
| `tom-bergstrom.md` | DR review, quarterly | 5, plus a scheduling-risk note: two are thirty-second questions that should not wait six weeks |
| `marcus-iwu.md` | Portfolio review, monthly | 4, led by the retirement-authority question rather than the records question |

Three of eight people in the queue, deliberately. You brief the meetings that
are actually happening; a brief for a meeting with no date is a to-do list
wearing a costume.

Each brief carries: why this person, how they think (from `context/people.md`),
the questions written as speech, **what a good answer looks like** per question,
names to chase, and a **do not ask** section. That last one is the
load-bearing part — their time is the scarce resource the whole method runs on,
and asking something they answered in March tells them the last conversation
was wasted.

### Decisions taken

| Decision | Rationale |
|---|---|
| Briefs are **drafted, not generated** | Everything else derived here is machine-written and it was tempting to match. Two reasons not to: the register is prose rather than structured data, and the value is in the framing — knowing Tom answers in recovery windows and asking that way. That is judgment, so it goes through review like anything else. |
| Briefs are living files, not dated per meeting | `tom-bergstrom.md`, not `2026-09-14-tom-bergstrom.md`. What was asked is already recorded in the summary and the register's Answered table; a dated brief per meeting would be a third copy of the same fact. |
| The gate moved to the middle rather than being duplicated | Two gates — one before the conversation and one after — was the obvious alternative and doubles the review load for no gain. One gate that both closes and opens is the same merge doing two jobs. |
| Briefed three of eight, and said so in the register | An empty *brief* column against five people looks unfinished. It is not, and the register now says why, because someone would otherwise "fix" it. |

### The diagram cost more than the prose

Recorded because it is the kind of thing that gets rediscovered expensively.

The six-step version came out at 0.73:1 — half again taller than wide, which
is unreadable once markdown scales it to page width. Three attempts to fix it
by structure all failed, and the reasons are worth having written down:

- **`direction` is global, not per-container.** Dagre applies one direction to
  the entire diagram, so a nested `direction: right` inside a container is
  silently ignored. The containers were only adding padding. Switching to
  `layout: elk` did not help either.
- **Grid layouts drop every edge.** `grid-columns: 3` produced exactly the
  shape wanted, at 2.57:1, and drew no connections at all. For a diagram whose
  entire point is the handoffs between steps, that is not a trade.
- **The lever that works is label width.** Rewriting each label from three
  stacked lines to one wide `A — B` line moved it from 0.73:1 to 1.19:1 with no
  structural change at all.

Added to `templates/prompt-generate-diagram.md`, and the aspect-ratio guidance
there softened from "near 2:1" to "aim for 2:1, treat wider-than-tall as the
floor" — because for a six-step loop with labelled edges, 2:1 is not reachable
and guidance nobody can follow gets ignored rather than met.

### Files changed in the second addendum

| File | Change |
|---|---|
| `evidence/interviews/` | New — three briefs |
| `templates/prompt-prepare-interview.md` | New — steps 1 to 3 as a prompt |
| `templates/interview-brief-template.md` | New |
| `processes/documentation-flywheel.md` | Loop restructured: prep, gate, conversation, processing. New *steady state* section. Four new edge cases. Roles table now says the assistant does the prep, not just the drafting. |
| `diagrams/source/documentation-flywheel.d2` | Rewritten flat, with a comment block recording why containers and grids were abandoned |
| `README.md` | Flywheel redrawn with the gate boxed in the middle; three details rather than two |
| `templates/prompt-process-transcript.md` | New step 7 — prep the next round in the same PR |
| `templates/prompt-generate-diagram.md` | New *Layout, the hard way* section |
| `evidence/question-register.md` | Brief column on the queue; new *how rows reach a conversation* section |
| `meta/ai-guidance.md` | New Interview Briefs section; transcript flow now seven steps |
| `meta/repo-conventions.md` | `evidence/interviews/` folder rule; brief naming — not dated |

---

## Third addendum — the transcripts

Same day. This closes the item that has been at the top of the open list since
bootstrap: the flywheel's input side was described in detail and never
demonstrated.

### What was added

Two Teams-format WebVTT transcripts, each with a summary. Both are historical,
which matters — their consequences are **already** in the repository, so
nothing had to be retrofitted and the summaries could be checked against
records that already existed.

| Transcript | Length | Shape |
|---|---|---|
| [`2026-03-04-erp-integration-review.vtt`](2026-03-04-erp-integration-review.vtt) | 166 cues, 23 min, 4 participants | The one six insight rows already cited. A pre-freeze integration review that was happening anyway. |
| [`2026-03-11-service-desk-sync.vtt`](2026-03-11-service-desk-sync.vtt) | 40 cues, 5 min, 2 participants | The counterexample: no agenda, one person clearing a ticket queue |

The March review had been referenced seven times across the repository —
`insights-surfaced.md` rows 1, 2, 4, 6, 7, and 10, plus two rows in the
register's Answered table — and did not exist. Writing it is the first time
those citations resolve to anything. All six insights, both closed questions,
and the `dr_impact` values on the EDI and legacy flows were checked line by
line against what the transcript actually says.

### Why two, and why one of them is five minutes

The integration review looks like a project. Anyone reading it could reasonably
conclude the method needs four senior people and a scheduled hour.

The service desk sync exists to disprove that. Five minutes, two people, no
agenda, asked while Alan was clearing the overnight queue — and it produced a
register row, a status change on a person-to-identify, and a new open question.
**It looks like a Wednesday, which is the point.**

### Decisions taken

| Decision | Rationale |
|---|---|
| Transcripts are `.vtt`, committed exactly as exported | Teams format, cue IDs and all. It is what an organization actually has, and generating a tidy markdown transcript would be demonstrating a workflow nobody has. |
| **Transcription errors left in.** *Meridien* for Meridian, *the I pass* for the iPaaS | A transcript is evidence. Correcting it edits the record of what was said. Both summaries call the mangles out, and `prompt-process-transcript.md` now tells an assistant to resolve them from context and never write them forward. This is a real failure mode — a model that propagates *Meridien* into a vendor field gets caught by the schema gate, which is a good demonstration in itself. |
| The carrier-rate tool was **not** added to the inventory | Alan does not know whether it is an application, a WMS module, or a vendor portal. Creating a record would be inventing a fact to make a list look complete — the exact failure DEC-011 exists to prevent. It is Q-021, an open question. This also keeps the portfolio at 17, which the README and the bootstrap note both state. |
| The tax engine tier was left wrong | In-universe, Marcus explicitly declines to fix it: correcting one record would hide a structural problem behind a fixed symptom. That reasoning is in the transcript, not just the summary. |
| The service desk summary records that **no insight was surfaced** | Not every conversation produces one, and a summary that manufactures an insight to look productive is worse than one that says nothing new was found. |
| Six action items from March are shown still open in August | Left as-is and pointed at. Two are blocked on identifying a person rather than on doing work, which is the argument for the people-to-identify table stated as evidence rather than as a claim. |

### On generating them

Both `.vtt` files were produced by a throwaway script in the scratchpad that
took a list of `(speaker, line)` pairs and computed cue IDs and timestamps.
Hand-writing 206 cues with monotonic timestamps is a good way to ship a
malformed file.

**The script is not in the repository and should not be.** The transcript is
the authored artifact; the script was scaffolding. First pass came out at 14
minutes for 166 cues, which is faster than people talk — the fix was slowing
the words-per-second and widening the gap distribution to include the real
silences that fall between topics.

Both files were then checked programmatically: `WEBVTT` header, every cue's end
after its start, every cue starting no earlier than the previous one ended, and
every speaker name matching the roster in `schema.yaml`.

### Files changed in the third addendum

| File | Change |
|---|---|
| `evidence/meetings/2026-03-04-erp-integration-review.vtt` / `.md` | New |
| `evidence/meetings/2026-03-11-service-desk-sync.vtt` / `.md` | New |
| `evidence/question-register.md` | Q-021 opened; Contracts row moved to *Asked 2026-03-11, no name yet*; Answered rows now link the summary |
| `inventory/insights-surfaced.md` | Six citations of the March review now link to it |
| `meta/repo-conventions.md` | `.vtt` naming; folder rule says a transcript with no summary does not belong; note on why transcription errors stay in |
| `meta/ai-guidance.md` | Step 0 on VTT format and not editing transcripts |
| `templates/prompt-process-transcript.md` | VTT format and transcription-error handling |
| `templates/meeting-summary-template.md` | Transcript link is now `.vtt` |
| `meta/ai-context.md` | The largest open item is closed |

---

## Fourth addendum — `context/the-brief/`

Same day. Built the walkthrough: a deck, a recording script, thumbnails, and
staged demo input. Outline came from `templates/demo.md`.

### What was built

| File | What it is |
|---|---|
| `slides.html` | 19-slide deck, one self-contained HTML file. No CDN, no build step, no licence. Arrows navigate, **O** overview, **F** fullscreen, prints to PDF. |
| `demo-script.md` | Run-of-show: eight segments, ~15 minutes, exact commands, YouTube chapters, description and LinkedIn drafts. |
| `thumbnail.html` | Three YouTube thumbnail concepts at 1280×720 plus a 1200×630 share card, exported by devtools node screenshot. |
| `demo-inputs/` | Three **deliberately unprocessed** `.vtt` transcripts and an `expected-changes.md` answer key. |

### Decisions taken

| Decision | Rationale |
|---|---|
| The deck is **hand-written HTML**, not Marp markdown | Started as Marp-compatible markdown. Replaced rather than kept alongside — two copies of a deck is the drift this repo exists to prevent, and the markdown needed a renderer to look like anything. |
| The deck **references the flywheel SVG by relative path** instead of embedding it | An embedded copy goes stale the moment the diagram changes. This is the repo's own data-to-docs rule applied to the deck, and it is worth saying out loud on camera. |
| Demo inputs live in `context/the-brief/demo-inputs/`, **not** `evidence/meetings/` | The rule is that a transcript without a summary has not been processed. Three unprocessed transcripts sitting in `evidence/` would contradict it. They get copied into `evidence/meetings/` during the demo, which is also a better beat — "here's what came off Teams this morning." |
| Guardrails added in `ai-guidance.md` and `repo-conventions.md` | An assistant reading this repo would see three unprocessed transcripts and helpfully process them, destroying the demo. Both files now say not to. |
| The script was rewritten twice | First for a room, then for a screen recording once it became clear the target was YouTube and LinkedIn. The second version dropped the wifi fallbacks and Q&A, added a cold open, and gained chapters and post copy. Then the post-production advice was largely discarded again — the author's style is raw and unedited, which reads as someone using the thing rather than performing it. |

### The demo inputs, and why three

Each produces a different, verifiable outcome — checked against the records
before writing the answer key:

| Transcript | Produces | Gaps |
|---|---|---|
| Infrastructure catch-up (Marcus + Tom, 7 min) | A new integration record, so **the landscape diagram redraws**. Plant historian hosting resolved. | 12 → 10 |
| Access review (Marcus + Ken, 5 min) | SSO→HCM `dr_impact` moves from `Unknown` to a standing access exposure. **The answer makes the estate look worse**, which is what an honest pass does. | 12 → 11 |
| Legacy order entry follow-up (Marcus + Priya, 4 min) | Names a person **not on the roster**, so `schema.yaml` must change in the same PR. Run `--validate-only` first and it fails by name. | 12 → 10 |

The third exists purely to produce fifteen seconds of terminal output: *the
model didn't get to decide that a new person exists, it had to ask.*

`expected-changes.md` also documents the four likeliest ways the assistant gets
it wrong on camera — top of the list, editing the RTO numbers in the first
transcript despite Tom explicitly saying not to. Catching one of those live is
the human-review step doing its job in public rather than being described.

### Corrections found while writing the deck

Putting numbers on slides forced a check of claims that had been asserted in
prose, and two were wrong:

- **"Four questions blocked on finding a person"** was three — Q-001, Q-004,
  Q-006. The fourth was blocked on another question, not a person. It had
  propagated to five files.
- **"Five insight rows"** from the March review was six.

Both corrected everywhere. Worth recording because it is the failure this repo
is built to prevent, and prose is the one part of it no gate checks. The
counting was done by script against the actual files, not by re-reading.

### Files changed in the fourth addendum

`context/the-brief/` (new, 7 files) · `README.md` (structure table, and the
`context/` row now mentions the brief) · `meta/ai-context.md` ·
`meta/ai-guidance.md` · `meta/repo-conventions.md` ·
`evidence/question-register.md` · `processes/documentation-flywheel.md` ·
`inventory/insights-surfaced.md` · both March meeting summaries · this note.

---

*Last updated: 2026-08-04*
