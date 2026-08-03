# Insights Surfaced

A running register of organizational issues the documentation process exposed
as a byproduct. **Not problems with the documentation — problems the
documentation revealed.**

Nothing here was the goal of a piece of work. Each row is something that
became visible because somebody was asked a structured question about a
system and the answer was uncomfortable. This register is often more valuable
than the catalog it falls out of.

> All data in this repository is fictional. Northwind Traders does not exist.

---

| # | Category | Insight | Source |
|---|---|---|---|
| 1 | Ownership gap | Three applications in daily use have no SME recorded — nobody in IT can answer a question about them. Electronic Signature is used across three business functions and was bought on a departmental card. | `gap-analysis.py`, 2026-03-04 integration review |
| 2 | Single point of failure | One person is sole SME and sole technical owner for both the integration platform and the EDI gateway — the two systems every inbound commercial flow passes through. | 2026-03-04 integration review |
| 3 | Single point of failure | One person is the sole SME for the ERP, the WMS, and the tax engine. Losing that person takes the finance chain and the warehouse chain at the same time. | `by-owner.md` |
| 4 | Retirement with no date | Legacy Order Entry is marked Retiring, still writes orders into the ERP through an uncharacterized manual path, has no owner, and has no retirement date. The blocker is contract-pricing terms that only exist inside the system being retired. | 2026-03-04 integration review |
| 5 | Unowned overlap | Two applications cover expense capture, and the evaluation of the second started without anyone asking whether the first already did the job. | `capability-map.md` |
| 6 | Undocumented dependency | The tax engine is tiered Important but is called synchronously inside a Critical transaction path. Tiers were assigned per application; nobody tiered the path. | 2026-03-04 integration review |
| 7 | Boundary dispute | It is not settled whether the plant historian sits inside the plant network boundary or the corporate one. That answer determines who is accountable for patching it, and both teams currently believe it is the other's. | 2026-03-04 integration review |
| 8 | Model gap | Every SaaS application authenticates through the identity provider, and none of those dependencies are in the integration records — authentication was not treated as an integration. The landscape diagram understates that application's blast radius. | `identity-provider.yaml` |
| 9 | Correlated risk | The ERP and the WMS share a vendor and a hosting tenancy, so a vendor-side outage takes both at once. The DR plan treats them as independent. | `by-vendor.md` |
| 10 | Classification too coarse | `dr_impact` records whether a flow is stoppable but not what stopping it costs. The warehouse queue and the expense export carry the same value; one is a half-day of manual counting and the other is a re-export. | 2026-03-04 integration review |

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
