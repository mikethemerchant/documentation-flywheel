# ERP Integration Review

**Date:** 2026-03-04
**Participants:** Marcus Iwu (chair), Priya Raman, Sofia Marchetti, Tom Bergstrom
**Transcript:** [`2026-03-04-erp-integration-review.vtt`](2026-03-04-erp-integration-review.vtt) — 23 minutes

> Fictional, like everything else in this repository. Northwind Traders does
> not exist and neither does anyone named here.

---

## Purpose

A review of the integration landscape ahead of the change freeze starting
17 March. **It was not a documentation session** — it was a meeting that was
going to happen anyway, for its own reasons, and the documentation questions
were asked inside it.

That is the whole method in one line, and it is why four people who do not have
time to write documentation gave twenty-three minutes to it without anybody
having to be persuaded.

---

## Key topics

### EDI — the flow that cannot be stopped

| Question | Answer | Source |
|---|---|---|
| What happens to the EDI flow during an ERP outage? | Depends which component. If the ERP API is unresponsive the gateway holds documents. **If the gateway itself is down, documents are lost.** | Sofia Marchetti |
| Do trading partners retry? | Mostly no. There is no retry obligation in the agreements. A couple of the larger partners might; not something to rely on. | Sofia Marchetti |
| So the order is lost? | The *document* is lost. The order still exists at the partner's end and they believe they sent it — so nobody chases it. | Sofia Marchetti |
| How much volume? | ~40% of order lines arrive this way. | Sofia Marchetti |

Marcus had this recorded as safely stoppable. It is the opposite: the one flow
in the estate where data is genuinely gone rather than delayed.

> *"Everything else, worst case we reconcile by hand. That one there's nothing
> to reconcile from."* — Sofia Marchetti

### Ownership concentration on the integration paths

| Question | Answer | Source |
|---|---|---|
| Who else knows how the EDI gateway works? | Nobody, properly. Tom could get into the box but could not explain why a partner map is shaped the way it is. | Sofia Marchetti, confirmed by Tom Bergstrom |
| And the integration platform? | Same person. | Sofia Marchetti |

Both integration paths — everything commercial arriving from outside — have one
SME, one technical owner, and one recovery owner, and they are the same person.
Raised, not resolved; it needs the IT Director.

### Tax engine — a tier two system inside a tier one path

| Question | Answer | Source |
|---|---|---|
| What happens if the tax engine is unavailable? | Order entry stops. Not slows — stops. | Priya Raman |
| Why? | The call is synchronous. The ERP will not complete an order or an invoice without a tax result. | Priya Raman |
| But it is tiered Important, and order entry is Critical? | Confirmed as a mismatch by everyone in the room. | — |

The framing that mattered came from Priya, and it reframed the finding:

> *"I think the problem is you've tiered the applications. The path isn't
> tiered. I don't think of the tax engine as a system, really. It's a step in
> order entry. It just happens to be someone else's."*

**The tier was deliberately left unchanged.** Correcting one record would hide a
structural problem behind a fixed symptom. Whether tiering should apply to paths
rather than applications is a decision for Dana Whitfield.

### Legacy order entry — retiring, unowned, undated, still live

| Question | Answer | Source |
|---|---|---|
| How does it write into the ERP? | A flat file, produced and loaded by hand. | Priya Raman |
| By whom? | Unknown. "I know it gets done. I've never watched it happen." | Priya Raman |
| What happens if the ERP is down when they load it? | Nobody has asked. It may not even fail visibly — a file drop may just sit there. | Priya Raman, Sofia Marchetti |
| Who owns it? | Nobody. The previous owner left. | Priya Raman |
| Is there a retirement date? | No. It has been marked Retiring since Priya joined. | Priya Raman |
| Why has it not happened? | **Contract pricing terms for a handful of long-standing accounts exist only inside it.** Nobody has costed moving them, so it goes back on the list each time. | Priya Raman |
| Who in Sales understands those terms? | Unknown. | — |

Recorded as `dr_impact: Unknown` rather than guessed at. "Not characterized" is
a finding; a plausible value would have hidden it.

### Plant historian — an undecided boundary, not an incomplete record

Raised unprompted by Tom.

| Question | Answer | Source |
|---|---|---|
| Is the historian inside the plant network boundary or the corporate one? | Undecided, and it has been ambiguous since it was installed. It decides who patches it. | Tom Bergstrom |
| Where does it run? | Unknown — could be a box on the plant floor or something in the DC. | Tom Bergstrom |
| Does it have an owner? | No. | Tom Bergstrom |

> *"If it's inside the plant boundary it was never mine to inventory."* — Tom Bergstrom

Marcus's observation on this is the most transferable thing in the transcript:

> *"The record looks incomplete but the actual problem is that a decision was
> never made."*

### Electronic signature — nobody in IT can answer a question about it

Used in contracts, HR, and (probably) procurement for supplier onboarding.
Purchased below the approval threshold, so it never reached IT. None of the
three IT leads in the room owns it. It entered the inventory only because Alan
Petrov received a ticket he could not route.

### `dr_impact` records whether, not what it costs

Raised by Sofia as a small thing that had been bothering her.

The warehouse queue and the expense export both carry
`Stoppable - manual reconciliation`. They are not comparable:

| Flow | What reconciliation actually means |
|---|---|
| Expense export → ERP | Re-run the export. Ten minutes, one person at a keyboard. |
| WMS ↔ ERP | The DC has been picking against a stock position that diverged for the length of the outage. Half a day of counting, minimum, by people on a floor. |

> *"The field says whether we can stop it, but not what stopping it costs. And
> the thing you actually want to know when you're deciding what to bring back
> first is the cost."* — Sofia Marchetti

Recorded as a gap in the model, not a gap in the data.

---

## Insights surfaced

Six rows added to
[insights-surfaced.md](../../inventory/insights-surfaced.md). None of these was
the goal of the meeting; all six fell out of asking structured questions about
systems.

| # | Category | Insight |
|---|---|---|
| 1 | Ownership gap | Electronic Signature used across three functions, bought on a departmental card, no SME |
| 2 | Single point of failure | One person is sole SME, technical owner, and recovery owner for both integration paths |
| 4 | Retirement with no date | Legacy Order Entry: retiring, unowned, undated, still on a live path, blocked on pricing terms held inside it |
| 6 | Undocumented dependency | Tax engine tiered Important inside a Critical path; tiers were assigned per application, nobody tiered the path |
| 7 | Boundary dispute | Plant historian boundary undecided; both teams believe patching is the other's |
| 10 | Classification too coarse | `dr_impact` records whether a flow is stoppable, not what stopping it costs |

---

## Action items

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Get Ken Oyelaran and Tom Bergstrom in a room on the plant boundary | Marcus Iwu | Open — still open as of 2026-08-04 |
| 2 | Find who administers Electronic Signature | Marcus Iwu | Open — pursued 2026-03-11, no name yet |
| 3 | Find a Sales contact who understands the legacy contract-pricing terms | Marcus Iwu | Open |
| 4 | Put path-versus-application tiering to Dana Whitfield | Marcus Iwu | Open |
| 5 | Rough out the real cost of stopping each flow Sofia owns | Sofia Marchetti | Open |
| 6 | Raise the integration-path concentration with Dana Whitfield | Marcus Iwu | Open |

**Six action items, all still open five months later**, which is itself worth
looking at. Two of them — items 2 and 3 — are blocked on identifying a person
rather than on doing any work — see the people-to-identify table in
[question-register.md](../question-register.md).

---

## Documents updated as a result

- `inventory/integrations/data/edi-gateway--meridian-erp.yaml` — `dr_impact`
  corrected to `Cannot stop - data loss risk`, with the partner-retry behaviour
  written into `failover_behavior`
- `inventory/integrations/data/legacy-order-entry--meridian-erp.yaml` —
  `dr_impact: Unknown`, characterized as not characterized
- `inventory/apps/data/meridian-erp.yaml` — dated note on the manual legacy path
- `inventory/insights-surfaced.md` — rows 1, 2, 4, 6, 7, 10
- `evidence/question-register.md` — Q-001, Q-003 to Q-007, Q-015, Q-016,
  Q-018, Q-019, Q-020 opened; Q-A01 and Q-A03 closed

The tax engine tier was **not** changed. See above.

---

## Questions closed

| Q | Question | Answer |
|---|---|---|
| Q-A01 | What happens to EDI documents arriving during an ERP outage? | Partners do not retry; documents are lost at the partner end |
| Q-A03 | Is the tax engine call synchronous inside order entry? | Yes — and it produced Q-016 |

---

## Open questions

Appended to [question-register.md](../question-register.md), which is the
durable copy.

| Q | Question | Who can answer |
|---|---|---|
| Q-003 | Who is the SME for Legacy Order Entry? | Marcus Iwu |
| Q-004 | Who produces and loads the legacy order file, and what do they do during an outage? | *Unidentified — Order Management* |
| Q-005 | Who is authorized to set a retirement date? | Dana Whitfield, Marcus Iwu |
| Q-006 | Who understands the legacy contract-pricing terms? | *Unidentified — Sales* |
| Q-007 | Where does the plant boundary sit? | Ken Oyelaran, Tom Bergstrom, *plant contact* |
| Q-016 | Should tiering apply to paths rather than applications? | Dana Whitfield, Priya Raman |
| Q-019 | What does stopping each flow actually cost? | Sofia Marchetti |
| Q-020 | What is the succession plan for the sole-owner systems? | Dana Whitfield |

---

## Note on the transcript

Two things in the raw file are worth knowing about before anyone quotes it.

**Transcription mangles proper nouns.** "Meridian" appears as *Meridien*, and
the integration platform appears as *the I pass*. Both are obvious in context
and neither was corrected in the transcript — the transcript is evidence and
gets committed as it came out. Corrections belong here, in the summary.

**Nobody in the room used the word "documentation" once.** They discussed
systems they own, in the way they normally discuss them. Everything above was
extracted afterwards. That is the design working: the cost to the four experts
was twenty-three minutes of a meeting they were already in.

---

*Last updated: 2026-08-04*
