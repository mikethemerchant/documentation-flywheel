# Insights Surfaced

A running register of organizational issues the documentation process exposed
as a byproduct. **Not problems with the documentation — problems the
documentation revealed.**

Nothing here was the goal of a piece of work. Each row is something that
became visible because somebody was asked a structured question about a
system and the answer was uncomfortable. This register is often more valuable
than the catalog it falls out of.

**Not to be confused with the question register.** This file holds what the
process *found out*; [`evidence/question-register.md`](../evidence/question-register.md)
holds what is still unknown and who can answer it. An insight often generates a
question — row 7 below is the reason Q-007 exists — but they are different
things and get read by different people. Insights are for whoever is deciding
what to fix. Questions are for whoever is booking the next conversation.

> All data in this repository is fictional. Northwind Traders does not exist.

---

| # | Category | Insight | Source |
|---|---|---|---|
| 1 | Ownership gap | Three applications in daily use have no SME recorded — nobody in IT can answer a question about them. Electronic Signature is used across three business functions and was bought on a departmental card. | `gap-analysis.py`, [2026-03-04 integration review](../evidence/meetings/2026-03-04-erp-integration-review.md) |
| 2 | Single point of failure | One person is sole SME and sole technical owner for both the integration platform and the EDI gateway — the two systems every inbound commercial flow passes through. | [2026-03-04 integration review](../evidence/meetings/2026-03-04-erp-integration-review.md) |
| 3 | Single point of failure | One person is the sole SME for the ERP, the WMS, and the tax engine. Losing that person takes the finance chain and the warehouse chain at the same time. | `by-owner.md` |
| 4 | Retirement with no date | Legacy Order Entry is marked Retiring, still writes orders into the ERP through an uncharacterized manual path, has no owner, and has no retirement date. The blocker is contract-pricing terms that only exist inside the system being retired. | [2026-03-04 integration review](../evidence/meetings/2026-03-04-erp-integration-review.md) |
| 5 | Unowned overlap | Two applications cover expense capture, and the evaluation of the second started without anyone asking whether the first already did the job. | `capability-map.md` |
| 6 | Undocumented dependency | The tax engine is tiered Important but is called synchronously inside a Critical transaction path. Tiers were assigned per application; nobody tiered the path. | [2026-03-04 integration review](../evidence/meetings/2026-03-04-erp-integration-review.md) |
| 7 | Boundary dispute | It is not settled whether the plant historian sits inside the plant network boundary or the corporate one. That answer determines who is accountable for patching it, and both teams currently believe it is the other's. | [2026-03-04 integration review](../evidence/meetings/2026-03-04-erp-integration-review.md) |
| 8 | Model gap | Every SaaS application authenticates through the identity provider, and none of those dependencies are in the integration records — authentication was not treated as an integration. The landscape diagram understates that application's blast radius. | `identity-provider.yaml` |
| 9 | Correlated risk | The ERP and the WMS share a vendor and a hosting tenancy, so a vendor-side outage takes both at once. The DR plan treats them as independent. | `by-vendor.md` |
| 10 | Classification too coarse | `dr_impact` records whether a flow is stoppable but not what stopping it costs. The warehouse queue and the expense export carry the same value; one is a half-day of manual counting and the other is a re-export. | [2026-03-04 integration review](../evidence/meetings/2026-03-04-erp-integration-review.md) |
| 11 | Undocumented dependency | A nightly integration had been running since the tool was implemented and appeared in no record. It surfaced only because the gap report flagged the application as having zero integrations. Point-to-point flows that bypass the integration platform have nobody whose job it is to notice they are missing. | [2026-08-04 infrastructure catchup](../evidence/meetings/2026-08-04-infrastructure-catchup.md) |
| 12 | Unowned work | The plant boundary dispute is not blocked on disagreement. Both leads agree what would settle it — establishing where the box physically terminates — and put it at an afternoon's work. It is blocked on nobody owning the afternoon. | [2026-08-04 infrastructure catchup](../evidence/meetings/2026-08-04-infrastructure-catchup.md) |
| 13 | Model gap | No recorded RTO or RPO has been tested end to end. The record model cannot distinguish a contractual commitment from a measured result, so an untested number is presented identically to a proven one — "written down in a way that looks like they've been proven". | [2026-08-04 infrastructure catchup](../evidence/meetings/2026-08-04-infrastructure-catchup.md) |
| 14 | Process gap | The historian's `hosting` sat at TBD for five months and took thirty seconds to answer. The field had been left blank to hold an unresolved ownership dispute it cannot express, and nobody had separated the two questions enough to ask the easy one. | [2026-08-04 infrastructure catchup](../evidence/meetings/2026-08-04-infrastructure-catchup.md) |

---

## How rows get here

After processing any interview transcript, ask:

1. Did the SME say "I don't know" or "you'd have to ask X" in a way that
   revealed an ownership gap?
2. Did they flag a single point of failure ("if X leaves…")?
3. Did they surface an application that wasn't on the list?
4. Did they describe something used across the business that nobody owns or
   has standardized?
5. Did they flag a retirement with no date attached?

If yes, add a row. Rows are appended, not edited — an insight that has since
been resolved is still evidence that the process found it.

Then ask the second question: **who could close it?** If there is an answer,
that is a row for [`question-register.md`](../evidence/question-register.md).
If there isn't — if the honest answer is "somebody in Contracts, we don't know
who" — that is a row for the register's people-to-identify table, and it is the
more urgent of the two.
