<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# EDI Gateway

Translates and routes EDI documents to and from trading partners — purchase orders, acknowledgements, and invoices. The commercial boundary of the business: an outage here is visible to customers within hours.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Sofia Marchetti |
| Technical owner | Sofia Marchetti |
| Manager | Marcus Iwu |
| Accountable team | Data & Integrations |

## Profile

| Field | Value |
|---|---|
| Vendor | Conduit |
| Capability | EDI & Trading Partner Exchange / Integration & Middleware |
| Primary users | Supply Chain / Sales |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 1 - Critical |
| RTO | 4 hours |
| RPO | 1 hour |
| Recovery owner | Sofia Marchetti |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

| To | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Resource Planning (ERP) | Inbound | EDI | EDI Gateway | Cannot stop - data loss risk |

## Notes

Carries the only inbound flow in the portfolio classified as unstoppable. Partners transmit on their own schedule and do not retry, so a document that arrives during an outage is lost at their end rather than queued at ours.
2026-03-04 (integration review): partner onboarding runbook exists only as a document on the vendor portal, not in this repository. Action item open.

---

Source record: [`inventory/apps/data/edi-gateway.yaml`](data/edi-gateway.yaml)
