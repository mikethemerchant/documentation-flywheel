# Interview Brief — Dana Whitfield

**Prepared:** 2026-08-04, from [question-register.md](../question-register.md)
**For:** Monthly one-to-one
**Status:** Ready — new brief
**Open questions on this brief:** 5 (Q-007, Q-023, Q-005, Q-016, Q-020)

> Fictional, like everything else in this repository.

---

## Why Dana, and why now

She has not been briefed before, and she should be. Four of these five questions
have been open since March and none of them is blocked on information — every
one is waiting on somebody with authority to make a call. That is the definition
of her queue.

The trigger is Q-007. The plant boundary has been described as a disagreement
between Tom and Ken since March. The
[2026-08-04 catchup](../meetings/2026-08-04-infrastructure-catchup.md) showed it
is not one: both leads agree what would settle it, both agree it is about an
afternoon of work, and neither owns the afternoon. Marcus committed to bringing
it to her rather than continuing to collect positions.

## How she thinks

**Exposure and defensibility.** The question underneath every answer is what
would be hard to explain to the CFO or an auditor afterwards. She will approve
an imperfect thing that is written down over a better thing that lives in
somebody's head, and says so often enough that the team quotes it back.

She pushes back hardest on anything that adds a step a person has to remember.
The standard challenge is *"what happens when whoever does this is on holiday?"*
— expect it, and have an answer before you need one.

**She reads the insight register before the inventory.** Open there, not in the
records. Rows 12, 13, and 14 are all hers and all new.

---

## The questions

### 1 — Q-007 · Who owns the afternoon?

> *"The plant historian boundary has been open since March. It isn't a
> disagreement any more — Tom and Ken both say the same thing about what would
> settle it: somebody walks down and establishes where the box physically
> terminates, then makes a call. It's an afternoon. Nobody owns the afternoon.
> Can you give it to someone?"*

**Why it matters.** It is blocking Q-008 outright and it is the reason a live
production system has no SME. It also has a patching consequence: both teams
currently believe the other patches it, which means the honest answer is that
nobody has confirmed anybody does.

**Frame it as assignment, not architecture.** This is the mistake the last five
months have made. She does not need to decide where the boundary *should* sit —
she needs to name who decides and by when. If it is framed as a network design
question she will correctly send it back to Tom and Ken, and it will sit for
another quarter.

**A good answer** is a name and a date. A partial win is a name.

**The patching exposure is the lever if she hesitates.** Not the documentation
gap — nobody has ever been moved by a documentation gap.

### 2 — Q-023 · Should a tested recovery target look different from a contracted one?

> *"Tom confirmed that none of our recorded RTOs or RPOs have ever been tested
> end to end — they all came out of contracts and vendor commitments. He asked us
> not to change the numbers, and he's right, they're what we're owed. But right
> now a number nobody has checked looks exactly like a number we've proven. Do
> you want the records to show the difference?"*

**Why it matters.** This is the most defensibility-shaped question in the
register and the one most likely to land with her immediately. Tom's own words
are the argument: *"it worries me more that they're written down in a way that
looks like they've been proven."* An RTO in a DR plan that has never been
measured is exactly the thing that is hard to explain afterwards.

**A good answer** is whether she wants it recorded at all, and at what
granularity — a flag, a date last proven, a method. Tom has offered to specify
the fix if she wants one.

**Do not propose a schema field.** Propose the problem. If she asks what it
would look like, then answer.

**Watch for the holiday question.** "Who marks a target as tested, and what
happens when they don't?" is exactly the objection she will raise, and the
honest answer is that nothing in the process currently does.

### 3 — Q-005 · Who is authorized to set a retirement date?

> *"The matrix says you approve a retirement. It doesn't say whose job it is to
> propose one — so Legacy Order Entry has been Retiring for years with no date
> and nothing has ever reached you. Is that a gap in the matrix or is it Marcus's
> job and he doesn't know it?"*

**Why it matters.** Insight 4, and the structural version of it. This is not
about the legacy system; it is about the next system that goes Retiring and does
the same thing. A `lifecycle_status` that describes an intention nobody owns will
keep producing this outcome.

**A good answer** names a role rather than an instance. If the answer is
"nobody, really", that is a finding for
[decision-rights.md](../../context/decision-rights.md) and probably a decision
record.

### 4 — Q-016 · Should tiering apply to paths rather than applications?

> *"The tax engine is Tier 2 and it's called synchronously inside order entry,
> which is Tier 1. Every individual tiering decision was correct. The result is
> still wrong. Is that something you want to fix in the model, or accept and
> document?"*

**Why it matters.** Insight 6. Accepting it is a legitimate answer — the point is
that it should be a decision rather than an artifact of how the schema happened
to be built.

**A good answer** is either direction, recorded. Priya is the other name on this
one and thinks in paths natively; she is worth having in the room if it goes
anywhere.

### 5 — Q-020 · Succession on the sole-owner systems

> *"Two systems have one person as SME, technical owner, and recovery owner.
> Tom is recovery owner on eleven of seventeen. What's the plan when one of them
> is on leave during a freeze?"*

**Why it matters.** Insight 2 and 3. Ask it as a practical availability question,
not a succession-planning one — it is the same question she asks everyone else,
turned around, and it will land better for it.

---

## If there is time

- Whether the two `context/` changes in this pull request are approved — the
  recovery-targets gap row now cites evidence rather than asserting, and the
  systems-landscape historian paragraph is corrected. Both need her signature per
  the matrix.

---

## Do not ask

- **What the approval matrix says.** It is recorded in
  [decision-rights.md](../../context/decision-rights.md) and she wrote most of
  it. Asking suggests it was not read.
- **Whether the freeze applies to documentation.** It does not, it is recorded,
  and it is the reason this work happens in the freeze at all.
- **Where the plant boundary should sit.** Not her call to make on the spot, and
  asking for it invites the deferral this brief exists to avoid. Ask who decides.
- **To change any RTO or RPO number.** Tom asked explicitly that they stand, and
  the request is that the records show what has been verified — not different
  numbers.

---

## Scheduling

Monthly one-to-one, and this fills it. Five questions is more than the usual
brief carries, but four of them are one sentence and a decision — this is a
different shape of conversation from an SME interview, and she is faster at it
than anyone else in the roster.

If time runs short, **Q-007 and Q-023 are the two that matter.** Q-007 unblocks
another row; Q-023 is the one she will care about most.

---

## After the conversation

Mark which questions were actually asked. Then run
[prompt-process-transcript.md](../../templates/prompt-process-transcript.md).

---

*Last updated: 2026-08-04*
