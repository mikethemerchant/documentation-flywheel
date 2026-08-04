# Interview Brief — Tom Bergstrom

**Prepared:** 2026-08-04, refreshed after the
[infrastructure catchup](../meetings/2026-08-04-infrastructure-catchup.md)
**For:** DR review, quarterly — next in September
**Status:** Ready, and much shorter than it was
**Open questions on this brief:** 3 (Q-018, Q-024, and Q-007 as a party rather than an owner)

> Fictional, like everything else in this repository.

---

## What changed

Marcus caught him for seven minutes on 2026-08-04 and closed three of the five
questions that were on this brief. **Q-009, Q-013, and Q-017 are answered and
have dropped off.**

That was this brief working as designed. The previous version said Q-009 and
Q-013 were thirty-second questions that did not need a DR review and should be
asked in any conversation he was already in — and that is exactly how they got
answered, six weeks before the meeting they were prepped for. Worth keeping in
mind when the next brief is written: separating the questions that need a
meeting from the questions that need thirty seconds is most of the value.

**Q-007 has moved off him.** He has stated his position twice now, it has not
changed, and the blocker turned out not to be his to clear. It is Dana's —
see [dana-whitfield.md](dana-whitfield.md). Do not ask him for his position a
third time.

## Why Tom

Still recovery owner on eleven of seventeen applications, which is still one of
the findings. What is left for him is the shared-fate question and the shape of
the integration graph he can see and Sofia cannot.

## How he thinks

Recovery windows and blast radius. Every question becomes "how long until it's
back, and what else goes with it".

The August conversation confirmed the framing note that was already here: he is
exact about the difference between a number in an agreement and a number that
has been measured, and volunteered the sharper version of it unprompted —
*"it worries me more that they're written down in a way that looks like they've
been proven."* Ask him a precision question and you get a precise answer.

---

## The questions

### 1 — Q-024 · What else bypasses the integration platform?

> *"The endpoint tool has been pushing into the warehouse every night since we
> put it in and it wasn't written down anywhere. What else goes straight across
> like that? Anything vendor-to-vendor, anything you set up that never went
> through Sofia?"*

**Why it matters.** This is the direct consequence of Q-013 and the most
valuable question on the brief. Sofia sees everything that transits the
integration platform, which means the flows that *do not* transit it have no
natural observer. One turned up by accident. The question is whether it was the
only one.

**A good answer** is a list, or a confident "that's the only one" with a reason
attached. *"I'd have to think"* is also a good answer — leave it with him.

**Ask it as a memory question, not an audit question.** *"What did you set up
that never needed Sofia?"* gets an answer; *"what's missing from our
integration records"* gets a shrug.

### 2 — Q-018 · Does the model need a way to express shared fate?

> *"The DR plan treats the ERP and the WMS as independent systems. They're the
> same vendor in the same tenancy. If Meridian has a bad afternoon, how many of
> our Tier 1s are actually down?"*

**Why it matters.** Insight 9. Nothing in the record model can say "these two
share a fate", so the only place it is visible is by reading `by-vendor.md`
carefully and noticing.

**This was on the previous brief and was not asked** — the August conversation
ran out of time at seven minutes. It is genuinely a DR-review question rather
than a corridor one, so it can wait for September without cost.

**A good answer** tells us whether the DR plan should treat them as one
recovery unit — which is a bigger change than a schema field and probably needs
a decision record.

**This is Sofia's question too.** Whoever gets asked first closes it.

### 3 — Q-023 · Recovery-target provenance *(consulted, not owner)*

Dana approves anything touching RTO and RPO, so the decision is hers. Tom's
input is what a useful distinction would actually look like:

> *"If we're going to mark which recovery numbers have been tested and which
> haven't — what would you want the tested ones to say? Date last proven?
> Method? Or is a flag enough?"*

**A good answer** is the minimum that would stop the numbers reading as
verified. He has already made the argument; this is asking him to specify the
fix.

---

## If there is time

- Q-020 is Dana's question, but Tom is the person it is about as much as
  anyone: what happens to eleven recovery-owner assignments when he is on
  leave? Ask it as a practical question, not a succession-planning one.
- Whether the ERP's contractual RTO has ever been invoked. Sharper now that we
  know none of them have been tested.

---

## Names to chase

| Who | For | Ask |
|---|---|---|
| Meridian account manager | Q-018, shared tenancy | *"Who's our contact at Meridian? I want to ask them directly whether the ERP and WMS sit in the same tenancy."* |

**The plant contact has been removed from this brief.** It has been on it for
two rounds and asked in neither, and the boundary question no longer depends on
finding that person — it depends on Dana assigning someone an afternoon. The
row stays in the register's people-to-identify table, where the fact that it
keeps going unasked is now recorded.

---

## Do not ask

- **Where the historian runs.** Answered 2026-08-04 — on-prem, a physical
  appliance in the plant electrical room. He has stood next to it.
- **Whether the plant boundary is settled.** He has given his position twice.
  Asking a third time tells him the last two conversations went nowhere, which
  they did not.
- **Whether Endpoint Management has integrations.** Answered and recorded.
- **Whether recovery targets have been tested.** Answered — none of them. The
  live question is what to do about the records, which is Q-023 and Dana's.
- **What the ERP's RTO and RPO are.** Recorded, four hours and fifteen minutes.
- **Whether the WMS queue holds during an outage.** Answered and recorded.
- **Who owns hosting.** He does.

---

## Scheduling

No longer urgent. Three questions, none blocking another row, and the two that
matter are genuinely DR-review shaped. **September is fine** — which is a change
from the previous version of this brief, where five questions and a six-week
wait was the main risk on it.

---

## After the conversation

Mark which questions were actually asked. Then run
[prompt-process-transcript.md](../../templates/prompt-process-transcript.md).

---

*Last updated: 2026-08-04*
