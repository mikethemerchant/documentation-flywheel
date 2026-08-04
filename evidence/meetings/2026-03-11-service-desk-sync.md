# Service Desk Sync

**Date:** 2026-03-11
**Participants:** Marcus Iwu, Alan Petrov
**Transcript:** [`2026-03-11-service-desk-sync.vtt`](2026-03-11-service-desk-sync.vtt) — 5 minutes

> Fictional, like everything else in this repository.

---

## Purpose

Two follow-ups from the [integration review](2026-03-04-erp-integration-review.md)
a week earlier, asked while Alan was clearing the overnight ticket queue.

**Five minutes, two people, no agenda, and it produced a register row and a new
open question.** Worth keeping as the counterexample to the assumption that
this method needs formal sessions. It does not. It needs someone to ask.

---

## Key topics

### Electronic signature — still no name

| Question | Answer | Source |
|---|---|---|
| You flagged this originally? | Yes — via a ticket he could not route. It sat with him about a week. | Alan Petrov |
| What was the ticket? | Someone in HR could not get a document to send. Routine, except there was no owner to assign it to. | Alan Petrov |
| Who administers it? | "Somebody in contracts. That's as close as I've got." | Alan Petrov |
| Is there a name? | There is a name on the ticket of whoever resolved it, but it is not clear whether that is the administrator or just someone who knew a workaround. | Alan Petrov |
| Can it be found? | Yes — by pulling the ticket history and seeing who resolves them. Not a five-minute job. | Alan Petrov |

**Action taken:** Alan to pull the history. As of 2026-08-04 this has not
happened, and Q-001 remains blocked on it. That is not a criticism of Alan; it
is what an action item with no date does.

### An application nobody can name

Raised by Alan unprompted, which is the pattern worth noticing — the service
desk sees the parts of the portfolio nobody else does.

| Question | Answer | Source |
|---|---|---|
| What is it? | Something the distribution centres use for carrier rates. Two or three tickets a month. | Alan Petrov |
| Is it a separate application? | Unknown. It might be part of the WMS, it might be standalone. The screenshots do not look like the WMS but he is not confident enough to say. | Alan Petrov |
| Who does he route those tickets to? | Priya Raman, because it is warehouse-adjacent. She resolves them. He does not think it is hers. | Alan Petrov |
| Has he asked what it is? | Yes. The answer was, quoting: *"it's the rate thing."* | Alan Petrov |
| Is it on the inventory? | Not under any name he would recognise — but if it is a module of something else, it would not be. | Alan Petrov |

**Deliberately not added to the inventory.** It is not yet known whether this is
an application, a module of the WMS, or a vendor portal. Creating a record now
would be inventing a fact to make a list look complete, which is the exact
failure the schema gate exists to prevent
([DEC-011](../../decisions/decision-log.md)). It is a question, and it is
recorded as one.

---

## Insights surfaced

None new. Both topics reinforce insight 1 (ownership gap) rather than adding to
it — which is itself the correct outcome to record. Not every conversation
produces an insight, and a summary that manufactures one to look productive is
worse than a summary that says nothing new was found.

The exchange worth keeping is this one:

> **Marcus:** *"That's a good example of the thing I keep hitting. It works, so
> nobody looks at it, so we don't know what it is."*
> **Alan:** *"It works until whoever's fixing it stops."*

---

## Action items

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Pull the e-signature ticket history and identify who resolves them | Alan Petrov | Open — not done as of 2026-08-04 |
| 2 | Send Marcus the last few carrier-rate tickets, with screenshots | Alan Petrov | Open |
| 3 | Establish whether the carrier-rate tool is a separate application, a WMS module, or a vendor portal | Marcus Iwu | Open — blocked on item 2 |

---

## Documents updated as a result

- `evidence/question-register.md` — Q-021 opened; the *Contracts* row in the
  people-to-identify table moved from **Not started** to **Asked — no name yet**

No inventory record was created or changed. See above.

---

## Questions closed

None. Q-001 was pursued and remains open — the answer narrowed from "nobody
knows" to "somebody in Contracts, findable from the ticket history", which is
progress without being closure.

Recording a question as *pursued and still open* matters. A register row that
silently stays open looks untouched; one that shows it was chased and where it
got stuck tells you the next action.

---

## Open questions

| Q | Question | Who can answer |
|---|---|---|
| Q-001 | Who in the business administers Electronic Signature? | *Unidentified — Contracts*, via Alan's ticket history |
| Q-021 | Is the carrier-rate tool the DCs use a separate application, a WMS module, or a vendor portal? | Alan Petrov, then Priya Raman |

---

## Note on the transcript

Five minutes, one of them in a ticket queue, no preparation beyond two questions
carried over from the previous week. The transcript is forty cues long.

It is here because the shape of the method is easier to believe from the small
example than the large one. The [integration review](2026-03-04-erp-integration-review.md)
looks like a project. This looks like a Wednesday.

---

*Last updated: 2026-08-04*
