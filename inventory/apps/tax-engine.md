<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Tax Engine

Real-time sales and use tax determination for orders and invoices, plus jurisdiction rate maintenance. Called synchronously by the ERP during order entry and invoicing.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | Priya Raman |
| Technical owner | Sofia Marchetti |
| Manager | Marcus Iwu |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Ledger Labs |
| Capability | Financial Management |
| Primary users | Finance |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 2 - Important |
| RTO | 8 hours |
| RPO | 1 hour |
| Recovery owner | Sofia Marchetti |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

| From | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|
| Enterprise Resource Planning (ERP) | Bidirectional | API (SOAP) | Direct (none) | Cannot stop - data loss risk |

### Flows out — this application is the source

_None._

## Notes

Tiered as Important but coupled to the ERP synchronously, so in practice its availability is part of the ERP's. A Tier 2 dependency sitting inside a Tier 1 transaction path is the kind of thing this inventory exists to make visible; the tiers were assigned per-application and the coupling was not considered.

---

Source record: [`inventory/apps/data/tax-engine.yaml`](data/tax-engine.yaml)
