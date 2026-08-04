# Prompt — Process a Meeting Transcript

The prompt for step 5 of
[the flywheel](../processes/documentation-flywheel.md): turning a recorded
conversation into reviewed, validated documentation.

**How to use it:** paste everything between the rulers into a fresh session
with this repository open, replacing `<TRANSCRIPT PATH>`. Do not summarize the
repository for the assistant first — the point is that
[README.md](../README.md) and [meta/](../meta/) already do that.

---

You are working in the `documentation-flywheel` repository.

Before doing anything, read `README.md`, then `meta/ai-context.md`,
`meta/ai-guidance.md`, and `meta/repo-conventions.md`. Then read
`context/organization.md`, `context/people.md`, and
`context/systems-landscape.md` so you can tell a new fact from a restatement of
one already recorded.

Your task is to process the transcript at **`<TRANSCRIPT PATH>`**.

## Step 1 — Read before proposing

Transcripts are WebVTT (`.vtt`), as exported from Teams — a `WEBVTT` header, then
cues of `<cue id>` / `<start> --> <end>` / `<v Speaker Name>text</v>`. Read the
speech; the timestamps matter only for citing a moment.

**Expect transcription errors and do not propagate them.** Proper nouns are the
usual casualty — *Meridien* for Meridian, *the I pass* for the iPaaS. Resolve
them from context and use the correct form in everything you write. **Never
edit the `.vtt`**: it is evidence, and correcting it edits the record of what
was said.

Read the full transcript. Then read the records it touches: the relevant files
in `inventory/apps/data/` and `inventory/integrations/data/`, the current
`inventory/insights-surfaced.md`, `evidence/question-register.md`, and any
process or decision document the conversation bears on.

The register tells you which questions this conversation was *meant* to answer.
Check them off explicitly, including the ones that went unasked — a question
that was on the list and did not get asked is worth knowing about.

Separate three things, and keep them separate:

- **New information** — something not currently recorded anywhere
- **Restatement** — something already recorded, said again
- **Contradiction** — something that conflicts with an existing record

Contradictions are the valuable ones and the ones most easily lost. Never
silently overwrite a record that has evidence behind it. Surface the conflict,
give both versions with their sources, and let the reviewer decide.

## Step 2 — Propose before you write

**Stop and produce a proposal. Do not edit any file yet.**

The proposal is a table: file path, what changes, and the quote or exchange from
the transcript that justifies it. Include what you considered and rejected —
"X said the historian might move to the plant network, but framed it as an
option rather than a decision, so no record change" is useful to a reviewer.

Wait for a response before continuing.

## Step 3 — Make the changes

Once the proposal is agreed:

**Inventory records** (`inventory/apps/data/`, `inventory/integrations/data/`)
- Only fields the transcript actually speaks to.
- Every value in a controlled field must already exist in `inventory/schema.yaml`.
  If it does not, add it to the schema **in the same change** and flag it in
  the summary as needing the approval named in `context/decision-rights.md`.
  Never substitute a near-enough existing value to avoid the gate.
- **Never invent a person.** If an owner is named who is not on the roster,
  that is a schema change with an approver, not a record edit you make quietly.
- Never rename a file to match a reworded display name — slugs are permanent
  identifiers (`DEC-005`).
- Add a dated line to the record's `notes` field for anything material, in the
  form already used there: `2026-03-04 (integration review): ...`

**Diagrams** (`diagrams/source/`)
- Hand-authored `.d2` only. `integration-landscape.d2` is generated — change
  the integration records instead and it redraws itself.

**Decisions** (`decisions/decision-log.md`)
- Only if something was actually decided by someone with the authority to
  decide it. "We should probably" is not a decision. Use
  `templates/prompt-write-decision-record.md`.

**Insights** (`inventory/insights-surfaced.md`)
- Append rows; never edit existing ones. Criteria in step 4.

**Question register** (`evidence/question-register.md`)
- Close what was answered, append what was raised. Full instructions in step 6.

**Processes and standards**
- Only if the conversation described how work actually happens differently from
  what is written. Note in the summary that it needs the approver from the
  matrix.

## Step 4 — Capture the insights

This is the step most likely to be skipped and most likely to produce the
thing worth reading. Go back through the transcript asking:

1. Did someone say "I don't know" or "you'd have to ask X" in a way that
   revealed an **ownership gap**?
2. Did they flag a **single point of failure** — "if X leaves", "only Y knows
   how that works"?
3. Did they mention an **application not on the list**?
4. Did they describe something used across the business that **nobody owns or
   has standardized**?
5. Did they flag a **retirement with no date**, or a plan with no owner?
6. Did they describe a **dependency the model cannot express** — a shared
   vendor, a shared tenancy, a synchronous call inside a higher-tier path?

For each: append a row to `inventory/insights-surfaced.md` with a category, a
one-line insight, and the source.

Watch for the ones that arrive as asides. "That's always been a bit of a grey
area" and "we've never actually tested that" are the phrases that most often
sit on top of a finding.

## Step 5 — Write the summary

**Mandatory. A transcript without a summary has not been processed.**

Create `evidence/meetings/YYYY-MM-DD-description.md` alongside the transcript,
following `templates/meeting-summary-template.md`. Same date and description as
the transcript filename, without the `-ai` suffix unless this was an AI working
session.

The summary is what people will actually read; nobody reads a transcript twice.
Write it for someone who was not in the room and will not open the recording.

## Step 6 — Update the question register

**Do not skip this. It is what makes the loop self-driving**, and it is the
step most easily lost because the summary feels like the deliverable.

Open `evidence/question-register.md` and reconcile it against the transcript:

**Close what was answered.** Move the row to the Answered table with the person
who answered and a link to this summary. Never delete it — being able to show
that a question was asked, and when, is what makes an old record still worth
trusting.

**Append what was raised.** Every question this conversation opened and could
not close becomes a row, with a name against it. A question with no name does
not get asked.

**Record who could not be identified.** Any "you'd have to ask X" where X is a
role rather than a person goes in the people-to-identify table, with who might
know the name. These rows are the highest-value ones in the file: a question
waiting on scheduling gets asked eventually, a question waiting on *finding
somebody* sits untouched until a person goes looking.

Do **not** add such a role to `inventory/schema.yaml`. The roster is people who
own records; the register is people to find.

**Tag model questions.** Anything the conversation revealed that the current
record model cannot express — a shared vendor tenancy, a synchronous call
inside a higher-tier path — stays open and gets tagged *model question*. That
is a finding about the schema, not missing data, and it should not be quietly
worked around.

Then mirror the open rows into the summary's Open Questions section. The two
should agree; the register is the durable copy and the summary is the snapshot.

If a brief exists for the person who was interviewed, reconcile it: which
questions were actually asked, and which were on the brief and never came up. A
question that keeps being briefed and never asked is telling you something.

## Step 7 — Prep the next round

**In the same pull request.** The closeout and the prep belong together — that
is what makes the merge hand the interviewer a briefed conversation instead of
a to-do.

Run `templates/prompt-prepare-interview.md`: re-run the gap analysis against
the records you just updated, reconcile the register, and refresh the briefs in
`evidence/interviews/`.

Refresh in place — briefs are living files, not one per meeting. Answered
questions drop off, newly raised ones land against whoever can answer them, and
anyone whose meeting has passed with nothing scheduled next gets their brief
deleted or marked *unscheduled*.

## Step 8 — Validate and hand over

```bash
python automation/render-inventory.py --validate-only
python automation/render-inventory.py
python automation/gap-analysis.py
python automation/render-diagrams.py
```

Then:

- Confirm you are **not on `main`** — `git branch --show-current`. Branch per
  change, per `standards/pull-request-policy.md`.
- Report what changed, what still needs approval and from whom, and what you
  chose not to change and why.
- **Do not merge.** Draft and hand over. A human reviews and commits
  everything.

## Constraints

- Everything in this repository is fictional. Northwind Traders does not exist.
  Invent nothing that implies otherwise, and never introduce a real
  organization's data.
- Never edit generated files: `inventory/rendered/`, `inventory/apps/*.md`,
  `diagrams/rendered/`, `diagrams/source/integration-landscape.d2`.
- Never call `d2` directly — use `automation/render-diagrams.py` (`DEC-009`).
- Prefer `Unknown` to a plausible guess. An honest gap is a finding; a filled
  field that is wrong is a lie the pipeline cannot catch (`DEC-011`).
- Keep it simple enough that people actually read it. Complexity is the failure
  mode here, not incompleteness.

---

## Notes for the human running this

- The proposal step in 2 is where most of the value is. It is much cheaper to
  correct an intent than a set of edits.
- If the assistant proposes something wrong, ask *why* it thought that before
  correcting it. Often the answer is that a document in `meta/` or `context/`
  is misleading — which is a bug worth fixing, not a model error.
- Expect to reject insight rows. Over-generating them is better than
  under-generating; the register is append-only, so a bad row is expensive.

---

*Last updated: 2026-08-04*
