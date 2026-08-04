# Interview Brief — Marcus Iwu

**Prepared:** 2026-08-04, from [question-register.md](../question-register.md)
**For:** Portfolio review, monthly
**Status:** Ready
**Open questions on this brief:** 4 (Q-003, Q-005, Q-014, Q-015)

> Fictional, like everything else in this repository.

---

## Why Marcus

He owns the business application portfolio and the commercial history behind
it. Two of the questions here are about applications nobody in IT can fully
account for, and he is the person most likely to know how they got here and who
would fight to keep them.

## How he thinks

Accountability. He describes systems by naming the person who gets called when
they break, and is visibly uncomfortable when that answer is a team. He knows
what things cost, who championed them, and which director will defend them.

**Lead with the ownership question, not the data question.** "Legacy Order
Entry has no SME recorded" is a records problem and he will treat it as one.
"If the legacy order path broke on a Friday afternoon, who gets called?" is his
question and he will answer it properly.

Wary of consolidation proposals that underestimate how hard a small user group
will fight for its tool. Expect that resistance on Q-015, and it is usually
right.

---

## The questions

### 1 — Q-005 · Who is authorized to set a retirement date?

> *"Legacy Order Entry has been Retiring since before the inventory existed.
> The matrix says Dana approves a retirement, but nothing says whose job it is
> to propose one. Is that you?"*

**Why it matters.** This is the structural version of insight 4 and probably
the most valuable question on the brief. `Retiring` with no date is a status
that describes an intention nobody owns, and the same gap will produce the same
outcome on the next system.

**A good answer** names a role, not just an instance. If the answer is "nobody,
really", that is a finding for `decision-rights.md` and possibly a decision
record.

### 2 — Q-003 · Who is the SME for Legacy Order Entry?

> *"Practically — if the file that feeds orders into the ERP didn't run
> tomorrow, who notices and who fixes it?"*

**Why it matters.** The record says `Unknown`. It is a retiring system on a live
path into the core, with an uncharacterized failure mode. Insight 1 and 4
together.

**A good answer** is a name. A partial win is a name for *who notices*, even if
nobody owns the fix — that person is the route to Q-004 and Q-006.

### 3 — Q-015 · Was Travel & Expense evaluated against Expense Management?

> *"There's a T&E product under evaluation and an expense management system
> already in production. Did the evaluation start from 'what do we already
> own', or from somewhere else?"*

**Why it matters.** This is the exact question the capability map exists to
force, and the dataset's planted overlap. Insight 5. The answer also tests
whether the capability map is doing its job or is a view nobody consults.

**A good answer** is honest about the origin. If it started with a business
sponsor who wanted a specific product, say so — that is the more useful finding
and it points at the evaluation gap in `decision-rights.md`.

**Ask gently.** This can land as a criticism of a decision he was part of. The
framing that works is process, not judgement: *"I'm trying to work out whether
the capability map would have caught it."*

### 4 — Q-014 · Where will Travel & Expense run, and does it have integrations?

> *"If T&E goes ahead — hosting, and does it need to talk to the ERP the way
> expense management does?"*

**Why it matters.** Two gap-report rows in one question, and the answer is
probably already known to him. Cheap.

**A good answer** is a hosting value and a yes/no on integrations. If it will
replicate the existing expense export, that is a second record covering the
same path and worth flagging back into Q-015.

---

## If there is time

- Q-002 — is Electronic Signature genuinely standalone, or connected to
  something nobody has written down?
- Whether anything has entered the portfolio since March that is not in the
  inventory. He is the second-best source for this after Alan.

---

## Names to chase

| Who | For | Ask |
|---|---|---|
| A Sales contact who understands the legacy contract-pricing terms | Q-006 — the actual blocker on the retirement | *"The pricing terms trapped in the legacy system — who on the Sales side actually understands what they are?"* |
| Whoever in Contracts administers electronic signature | Q-001 | *"Do you know who bought the e-signature tool, or who administers it now?"* Alan is the better route, but Marcus may know the commercial side. |

Q-006 is worth pushing on. It is the reason the retirement has not moved, and
it is currently blocked on nobody having gone looking for a person.

---

## Do not ask

- **What the legacy system does.** Recorded, and he will assume the inventory
  was not read.
- **Who owns the ERP or the WMS.** Priya is SME on both, recorded.
- **Whether the legacy path is still live.** It is; the March review confirmed
  it and it is in the DR posture view.

---

## After the conversation

Mark which questions were actually asked. Then run
[prompt-process-transcript.md](../../templates/prompt-process-transcript.md).

---

*Last updated: 2026-08-04*
