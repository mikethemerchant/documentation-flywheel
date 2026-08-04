# Prompt — Prepare the Next Round of Interviews

Steps 1 to 3 of [the flywheel](../processes/documentation-flywheel.md): run the
gap analysis, reconcile the question register, and produce the briefs for the
conversations that are actually coming up.

**Run this after processing a transcript, in the same pull request.** The
closeout of the last conversation and the prep for the next one belong
together — that is what makes the merge in step 4 hand you a briefed interview
rather than a to-do.

---

You are working in the `documentation-flywheel` repository.

Read `README.md`, then `meta/ai-context.md`, `meta/ai-guidance.md`, and
`meta/repo-conventions.md`. Then read `context/people.md` — you will need it —
and `evidence/question-register.md`.

Prepare the next round.

## Step 1 — Ask the machine what is missing

```bash
python automation/gap-analysis.py
```

Every gap it reports should have a row in the register. Where one does not,
either add it or record why the gap is acceptable. Also re-read
`inventory/insights-surfaced.md` — each insight implies a question, and the
useful one is usually *who could close this?*

Report what changed since the last run. A gap that closed is as interesting as
one that opened.

## Step 2 — Reconcile the register

Work through `evidence/question-register.md`:

- **Add** rows for new gaps. Give each a `Q-NNN`, a name, and a source.
- **Update** status on rows that moved. A question that was asked and not
  answered is not the same as one nobody has raised.
- **Check the blocked rows.** Anything blocked on another question should
  unblock when that one closes; anything blocked on *finding a person* stays in
  the people-to-identify table.
- **Re-sort the queue at the top.** Order by what each conversation unblocks,
  not by row count — one question that unblocks three others beats four
  independent ones.

**Every row needs a name.** If nobody can be identified, record the *role* in
the people-to-identify table with who might know. A question with no name does
not get asked.

## Step 3 — Decide who to brief

**Only people with a conversation actually coming up.** Check the *next
opportunity* column. Three or four briefs is a healthy round; if you are
writing eight, you are producing documents nobody will read.

Say which people you are briefing and which you are skipping, and why, before
you write anything.

## Step 4 — Write the briefs

One file per person: `evidence/interviews/<person-slug>.md`, following
`templates/interview-brief-template.md`. Slug matches the person's name in
kebab-case. Refresh existing files in place rather than creating new ones —
these are living documents.

The work is turning register rows into something usable in a room. That means:

**Rewrite every question as speech.** The register says
`Q-009 — hosting: TBD on the plant historian`. The brief says *"Where does the
historian actually run — is there a box in the plant, or is it in the DC?"*
Nobody has ever asked a useful question by reading a table row aloud.

**Pull the framing from `context/people.md`.** This is the section that makes a
brief worth more than a filtered list. Tom answers in recovery windows, so a
tiering question asked as a recovery question gets a real answer and the same
question asked as a modelling question gets a shrug. State the consequence, not
just the trait.

**Say what a good answer looks like.** Per question. Knowing when you have
enough and can stop pushing is the hard part live, and it cannot be improvised.

**Write the *do not ask* section.** Go through what is already recorded about
that person's systems and list what would be a restatement. This is the section
that protects the thing the whole method depends on: their willingness to keep
turning up. Asking someone a question they answered two months ago tells them
the last conversation was wasted.

**Demote honestly.** Three to five questions in the main list. Everything else
goes under *if there is time*. A brief with nine equally-weighted questions
produces a conversation that covers four of them at random.

**Include names to chase**, with the actual wording. Asking for a name is
socially harder than asking for a fact, and a prepared phrasing helps.

**Flag scheduling risk** where it exists — a meeting weeks out with blocking
questions on it, or short questions that could be asked anywhere and should not
wait for it.

## Step 5 — Hand over

- Confirm you are **not on `main`** — `git branch --show-current`.
- Validate and render: `python automation/render-inventory.py --validate-only`,
  then `python automation/render-diagrams.py --check`.
- Report: what the gap analysis says now, what changed in the register, who is
  briefed and who was skipped, and which questions are blocked on finding a
  person rather than on scheduling one.
- **Do not merge.** A human approves the briefs before anyone walks into a room
  with one.

## Constraints

- Everything in this repository is fictional. Invent nothing that implies
  otherwise.
- A role in the people-to-identify table does **not** go into
  `inventory/schema.yaml`. The roster is people who own records; the register is
  people to find.
- Never close a register row by filling the underlying field with a plausible
  guess (`DEC-011`).
- Briefs are drafted, not generated. If you find yourself producing the same
  brief mechanically from the same rows, the framing work is being skipped and
  the brief is worth less than the register it came from.

---

## Notes for the human running this

- The *do not ask* section is the one to check most carefully. It is the only
  part of the brief with a social cost when it is wrong.
- Skipping people is a feature. If the assistant briefs everyone in the queue,
  push back — the constraint is which meetings exist, not which questions do.
- A register row that keeps reappearing on briefs without being asked is
  telling you something: either the question is not actually important, or the
  meeting where it fits is not happening.

---

*Last updated: 2026-08-04*
