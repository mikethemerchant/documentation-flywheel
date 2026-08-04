# Interview Brief — Sofia Marchetti

**Prepared:** 2026-08-04, from [question-register.md](../question-register.md)
**For:** Integration standup, weekly — Thursday
**Status:** Ready
**Open questions on this brief:** 4 (Q-011, Q-012, Q-018, Q-019)

> Fictional, like everything else in this repository.

---

## Why Sofia

She owns both integration paths — the iPaaS and the EDI gateway — as SME,
technical owner, and recovery owner. Three of the four questions here are about
whether the *model* is capable of describing what she actually operates, and
she is the only person who can say.

## How she thinks

Flows, failure modes, and replay. She will answer "what happens to in-flight
data?" before you have finished asking a question about anything else.
Skeptical of any hop without an owner.

**Phrase model questions as operational ones.** "Should SSO be an integration
record?" gets a shrug. "If the IdP is down for an hour, which of these flows
actually stops?" gets a real answer, and the model conclusion falls out of it.

---

## The questions

### 1 — Q-011 · Should SSO trusts be integration records?

> *"Every SaaS app authenticates through the IdP, and none of that is in the
> integration records. If Northgate has an outage tomorrow morning, what
> actually stops working — and would the landscape diagram have told anyone
> that?"*

**Why it matters.** The diagram currently shows the identity provider with one
connection. In reality most of the portfolio is unreachable without it. The
model started from data flows and a trust relationship does not move data in
the sense it had in mind.

**A good answer** names which systems break and distinguishes *authentication
fails* from *the application is down*. If she starts drawing the distinction
between the two, that is the answer — and it probably means a new field rather
than sixteen new integration records.

**Watch for:** a scope answer. If she says "that's really sixteen records for
one fact", the finding is that the model needs a different shape, not more rows.

### 2 — Q-019 · What does stopping each flow actually cost?

> *"`dr_impact` tells us whether a flow can be stopped. The warehouse queue and
> the expense export both say 'manual reconciliation'. Are those the same
> amount of pain?"*

**Why it matters.** They are not — one is half a day of counting in a
distribution centre, the other is re-running an export. The field is too coarse
to be used for the thing it exists for, which is deciding what to restore
first. Insight 10.

**A good answer** is two or three concrete examples with a rough number of
hours and who does the work. That is enough to know whether this wants a new
field, a scale, or just better `failover_behavior` prose.

### 3 — Q-018 · Does the model need a way to express shared fate?

> *"ERP and WMS are both Meridian, same tenancy. iPaaS and EDI are both Conduit,
> and both yours. Is there anything today that would tell someone reading the
> inventory that those pairs go down together?"*

**Why it matters.** There is not. It is visible only by squinting at
`by-vendor.md`, and the DR plan treats the ERP and WMS as independent.
Insights 2 and 9.

**A good answer** tells us whether this is one relationship or several — shared
vendor, shared tenancy, shared owner, and shared network path are four
different failure shapes and may not want one field.

**This is Tom's question too.** Whoever gets asked first closes it.

### 4 — Q-012 · Is the iPaaS correctly absent from the integration records?

> *"The gap report flags the integration platform as having no integrations,
> which reads like an error. It's middleware — it's the path, not an endpoint.
> Do you want that left as-is, or does it bother you?"*

**Why it matters.** Low stakes, quick to close, and it removes a permanent
piece of noise from the gap report — or confirms the noise is worth keeping as
a talking point.

**A good answer** is a preference plus a reason. Either is fine.

---

## If there is time

- Have the RTO and RPO values on the EDI gateway and iPaaS ever been tested,
  or are they contractual? (Q-017 is Tom's, but she owns two of the Tier 1
  systems in it.)
- Anything she has noticed since the March review that is not written down
  anywhere.

---

## Names to chase

Nothing on her. She is unlikely to know who administers electronic signature or
who produces the legacy order file.

---

## Do not ask

Her time is the scarce resource. These are already recorded and asking again
signals that the last conversation was not read:

- **What happens to EDI documents during an ERP outage.** Answered 2026-03-04:
  partners do not retry, documents are lost at the partner end. Closed as Q-A01.
- **Whether the iPaaS queues and replays.** Recorded on both flows that use it.
- **Who owns the integration platform.** She does, and the record says so. The
  interesting version of that question is the succession one, and it belongs to
  Dana (Q-020), not to her.

---

## After the conversation

Mark which questions were actually asked before the end of the day. Then run
[prompt-process-transcript.md](../../templates/prompt-process-transcript.md) —
it closes the register rows, refreshes this brief, and preps the next one.

---

*Last updated: 2026-08-04*
