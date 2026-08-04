# Infrastructure catchup — endpoint feed, the historian's box, and untested recovery targets

**Date:** 2026-08-04
**Participants:** Marcus Iwu (Applications Manager), Tom Bergstrom (Infrastructure Lead)
**Transcript:** [`2026-08-04-infrastructure-catchup.vtt`](2026-08-04-infrastructure-catchup.vtt) — 7 minutes

> Fictional, like everything else in this repository.

---

## Purpose

Marcus caught Tom for ten minutes rather than wait for the September DR review,
because three of the five questions on Tom's brief did not need a DR review to
answer. Tom took it standing in the data centre. No agenda, no preparation on
his side, and nothing asked of him afterwards.

This is the case the brief explicitly anticipated: *"Q-009 and Q-013 are both
thirty-second questions and do not need a DR review; ask them at any point where
he is already in a conversation."* That is what happened, six weeks early.

---

## Key topics

### Endpoint Management is not standalone

| Question | Answer | Source |
|---|---|---|
| It shows up on the gap report with no integrations. Is that right? | *"No, that's wrong. It talks to the warehouse."* | Tom Bergstrom |
| Since when? | Since implementation. Asset and compliance data — device inventory, patch state, encryption status — pushed nightly into the EDW | Tom Bergstrom |
| How does it move? | REST, vendor-side push on a schedule, around 02:00. *"Straight across. It doesn't go through the integration platform."* | Tom Bergstrom |
| What if the EDW is down when it fires? | Nothing. The tool holds its own inventory and is the system of record for it; the next night's run carries the full state, not a delta. A day-stale dashboard is the whole impact | Tom Bergstrom |
| Why was it never written down? | *"It's not a thing anyone thinks about, it's just been running."* And later: *"That one's genuinely boring, which is why nobody wrote it down."* | Tom Bergstrom |

Sofia's team consume the feed in what Tom called an "endpoint compliance
dashboard". Whether that is a separate application, a BI report, or a
vendor-side view was not established, and it has **not** been added to the
inventory — Q-022.

### The Plant Historian runs on a box in the plant

| Question | Answer | Source |
|---|---|---|
| Where does it actually run? | *"It's an appliance. There's a physical box in the plant electrical room."* | Tom Bergstrom |
| Sure? The record says TBD | *"I'm sure about the box. I've stood next to it."* | Tom Bergstrom |
| So on-prem | *"On-prem. What I'm not sure about is whether it's mine."* | Tom Bergstrom |
| Has the boundary position changed since March? | No. His position: inside the plant network boundary, so plant. Ken's: an IP address on a corporate switch makes it Infrastructure. *"We're both partly right, which is the problem."* | Tom Bergstrom |
| What would settle it? | *"Somebody looking at where it physically terminates and making a call. It's an afternoon of work and nobody owns the afternoon."* | Tom Bergstrom |

The hosting answer took thirty seconds and the field had been TBD for five
months. It was never blocked on the boundary dispute; the two questions had been
collapsed into one.

### No recovery target has been tested

| Question | Answer | Source |
|---|---|---|
| Have any of the RTOs actually been tested? | *"Define tested."* — *"Somebody failed something over and timed it."* — *"Then no."* | Tom Bergstrom |
| None of them? | One partial on the pre-migration ERP. *"That system doesn't exist any more, so I wouldn't count it."* | Tom Bergstrom |
| So they're commitments, not measurements? | *"They're what somebody agreed to. Whether it happens on the day, I genuinely couldn't tell you."* | Tom Bergstrom |
| Does that worry you? | *"It worries me more that they're written down in a way that looks like they've been proven."* | Tom Bergstrom |
| What should we do about it? | *"Don't change the numbers. The numbers are what we're owed. Just say nobody's checked."* | Tom Bergstrom |

**No RTO or RPO value was changed**, on his instruction and in line with
[DEC-011](../../decisions/decision-log.md). The numbers are the commitment; what
was missing from the records was that nobody has verified any of them.

---

## Insights surfaced

| Category | Insight |
|---|---|
| Undocumented dependency | A nightly integration ran for years in no record. It surfaced only because the gap report flagged zero integrations — point-to-point flows that bypass the platform have nobody whose job it is to miss them |
| Unowned work | The boundary dispute is not blocked on disagreement. Both leads agree what would settle it and cost it at an afternoon. It is blocked on nobody owning the afternoon |
| Model gap | The record model cannot distinguish a contracted recovery target from a measured one, so untested numbers read as proven ones |
| Process gap | `hosting: TBD` sat unanswered for five months holding an ownership dispute the field cannot express. Nobody had separated the two questions enough to ask the easy one |

Rows 11–14 in
[insights-surfaced.md](../../inventory/insights-surfaced.md).

---

## Action items

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Take the plant boundary to Dana as an assignment question — who owns the afternoon that settles it — rather than continuing to ask Tom and Ken for positions | Marcus Iwu | Open |
| 2 | Establish what the "endpoint compliance dashboard" actually is before anything about it enters the inventory (Q-022) | Sofia Marchetti | Open |
| 3 | Decide whether the schema should carry recovery-target provenance (Q-023) | Dana Whitfield | Open |

---

## Documents updated as a result

- `inventory/integrations/data/endpoint-management--enterprise-data-warehouse.yaml` — **new record**. REST, direct, outbound, stoppable with no data loss
- `inventory/apps/data/plant-historian.yaml` — `hosting` TBD → On-Prem; notes rewritten to separate the hosting fact from the boundary dispute
- `inventory/apps/data/endpoint-management.yaml` — dated note; no field changes, the record was correct and only its integration was missing
- `inventory/apps/data/enterprise-data-warehouse.yaml` — dated note recording a third inbound feed, and that `purpose` names only two
- `inventory/insights-surfaced.md` — rows 11–14
- `evidence/question-register.md` — Q-009, Q-013, Q-017 closed; Q-007 updated with the resolution path and escalated to Dana; Q-022, Q-023, Q-024 raised; Tom drops from first to fifth in the interview order
- `evidence/interviews/tom-bergstrom.md` — refreshed; three questions dropped off
- `evidence/interviews/dana-whitfield.md` — **new brief**, because the boundary question moved to her
- `context/organization.md` — the "recovery targets are aspirational" gap now cites evidence instead of asserting
- `context/systems-landscape.md` — historian and reporting-stack paragraphs corrected
- `diagrams/source/integration-landscape.d2` and the rendered views — regenerated; the new integration record redraws the landscape

Needs approval, per [decision-rights.md](../../context/decision-rights.md):
**Marcus Iwu** for the new integration record (he was in the room), **Dana
Whitfield** for the two `context/` changes. No schema change was required — every
value used already existed and no new person was named.

---

## Questions closed

| Q | Question | Answer |
|---|---|---|
| Q-009 | Where does the Plant Historian actually run? | On-prem — a vendor appliance in the plant electrical room |
| Q-013 | Is Endpoint Management genuinely standalone? | No. One nightly REST feed into the EDW, direct, now recorded |
| Q-017 | Have any recorded RTO/RPO values been tested? | None. All contractual. Numbers left unchanged; the gap is recorded instead |

---

## Open questions

| Q | Question | Who can answer |
|---|---|---|
| Q-007 | Where does the plant boundary sit? *No longer blocked on evidence — blocked on somebody being assigned the afternoon that settles it* | Dana Whitfield |
| Q-022 | Is the "endpoint compliance dashboard" an application, a report, or a vendor view? | Sofia Marchetti |
| Q-023 | Should the model distinguish a contracted recovery target from a tested one? | Dana Whitfield, Tom Bergstrom |
| Q-024 | What else bypasses the integration platform and so appears in nobody's view? | Sofia Marchetti, Tom Bergstrom |

Q-018 was on the brief and was not asked. Neither was the request for a plant
contact name — the second round running that it has gone unasked, which is
recorded in the register's people-to-identify table rather than left to be
noticed again next time.

---

## What this conversation is worth noticing for

Seven minutes, in a data centre, with no preparation on the expert's side. It
closed three questions, produced four insight rows, found an integration that
had been invisible for years, and moved the interview queue around. Nobody said
the word "documentation."

The most useful thing in it was an aside — *"nobody owns the afternoon"* — which
reframed a five-month-old dispute from a disagreement into a scheduling failure,
and changed who the next conversation is with.

---

*Last updated: 2026-08-04*
