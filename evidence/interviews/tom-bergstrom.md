# Interview Brief — Tom Bergstrom

**Prepared:** 2026-08-04, from [question-register.md](../question-register.md)
**For:** DR review, quarterly — next in September
**Status:** Ready — but the meeting is six weeks out; see *scheduling risk* below
**Open questions on this brief:** 5 (Q-007, Q-009, Q-013, Q-017, Q-018)

> Fictional, like everything else in this repository.

---

## Why Tom

He is named as recovery owner on eleven of the seventeen applications, which is
itself one of the findings. He holds the contractual recovery numbers, and he
is one half of the plant boundary dispute that is currently blocking two other
questions.

## How he thinks

Recovery windows and blast radius. Every question becomes "how long until it's
back, and what else goes with it".

**He is careful about the difference between a number in an agreement and a
number that has been tested, and will correct you every time you blur it.**
That is exactly the distinction Q-017 is chasing, so lean into it rather than
around it. His corrections usually arrive as a question; that is agreement, not
pushback.

---

## The questions

### 1 — Q-017 · Have any recovery targets actually been tested?

> *"Every application record carries an RTO and an RPO. How many of those
> numbers has anyone actually proven, versus how many came out of a contract
> when we moved the ERP to vendor hosting?"*

**Why it matters.** `context/organization.md` states that the targets are
aspirational, and that claim currently rests on nobody having contradicted it.
If it is true, it should be visible in the records rather than in a paragraph
of prose that only someone reading context files will find.

**A good answer** is a split — these were tested, these were not, this one we
tested two years ago and the system has changed since. Anything that lets us
mark the difference.

**Watch for:** he may have tested things that were never written down. That is
the best possible outcome and the least likely to be volunteered.

### 2 — Q-007 · Where does the plant boundary sit?

> *"Is the historian inside the plant network or the corporate one? Ken thinks
> it's yours; I want to hear your version before I put anything in writing."*

**Why it matters.** It decides who patches it, and it is blocking Q-008 (who is
the SME) and shaping Q-009 (where it runs). It has been contested since March
and neither side has moved. Insight 7.

**A good answer** is not necessarily a resolution — it is a clear statement of
his position and, more usefully, *what would settle it*. Ask that explicitly if
he does not offer it: **"what would have to happen for this to be decided?"**

**Handle with care.** This is a live disagreement between two team leads. Take
his version down as his version, not as the answer, and put the same question
to Ken. Do not present Ken's position as settled.

### 3 — Q-009 · Where does the Plant Historian actually run?

> *"Separately from who owns it — is there a physical box on the plant floor,
> is it in the DC, is it a vendor appliance? `hosting` is TBD and has been since
> the record was created."*

**Why it matters.** It is the easiest of the historian questions and may not
actually be blocked on the boundary dispute. Worth asking even if Q-007 goes
nowhere, because a hosting answer narrows who could plausibly own it.

**A good answer** is one of the schema's `hosting` values, or a clear statement
that it is genuinely more than one thing.

### 4 — Q-018 · Does the model need a way to express shared fate?

> *"The DR plan treats the ERP and the WMS as independent systems. They're the
> same vendor in the same tenancy. If Meridian has a bad afternoon, how many of
> our Tier 1s are actually down?"*

**Why it matters.** Insight 9. Nothing in the record model can say "these two
share a fate", so the only place it is visible is by reading `by-vendor.md`
carefully and noticing.

**A good answer** tells us whether the DR plan should treat them as one
recovery unit — which is a bigger change than a schema field and probably needs
a decision record.

**This is Sofia's question too.** Whoever gets asked first closes it.

### 5 — Q-013 · Is Endpoint Management genuinely standalone?

> *"It shows up with no integration records. Is that right, or is it talking to
> something we haven't written down — the IdP, an inventory feed, anything?"*

**Why it matters.** Small, and the kind of thing that turns out not to be true.
Bundled here because it costs thirty seconds in a meeting that is already
happening.

**A good answer** is yes or no. If no, it is a new integration record.

---

## If there is time

- Q-020 is Dana's question, but Tom is the person it is about as much as
  anyone: what happens to eleven recovery-owner assignments when he is on
  leave? Ask it as a practical question, not a succession-planning one.
- Whether the ERP's contractual RTO has ever been invoked.

---

## Names to chase

| Who | For | Ask |
|---|---|---|
| Plant controls engineer or plant manager | Q-007, and the historian's owner | *"Who on the plant side would I talk to about the historian? I don't need the org chart, just a name."* |
| Meridian account manager | Q-018, shared tenancy | *"Who's our contact at Meridian? I want to ask them directly whether the ERP and WMS sit in the same tenancy."* |

The first of these has been asked once already and produced no name. If it
comes up empty again, that is worth recording as its own finding — a system
nobody on either side can name a contact for.

---

## Do not ask

- **What the ERP's RTO and RPO are.** Recorded, four hours and fifteen minutes.
  The live question is whether they have been tested (Q-017), which is a
  different question and he will notice the difference.
- **Whether the WMS queue holds during an outage.** Answered and recorded in
  the failover behaviour notes.
- **Who owns hosting.** He does.

---

## Scheduling risk

The DR review is six weeks out, and five open questions is a long time to wait
— two of them are blocking other rows. **Q-009 and Q-013 are both
thirty-second questions** and do not need a DR review; ask them at any point
where he is already in a conversation. If the boundary dispute is still open in
two weeks, Q-007 probably deserves its own short conversation with Ken present,
which is the one case in this process where scheduling a meeting is justified.

---

## After the conversation

Mark which questions were actually asked. Then run
[prompt-process-transcript.md](../../templates/prompt-process-transcript.md).

---

*Last updated: 2026-08-04*
