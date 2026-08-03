<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Electronic Signature

Signature collection on customer contracts, credit applications, and vendor agreements. Signed documents are downloaded and filed manually; nothing is automated into another system.

## Ownership

| Role | Who |
|---|---|
| SME (who to call) | **Unknown** |
| Technical owner | **Unknown** |
| Manager | Marcus Iwu |
| Accountable team | Applications |

## Profile

| Field | Value |
|---|---|
| Vendor | Quill |
| Capability | Document Signature |
| Primary users | Sales / Finance / Enterprise |
| Lifecycle | Active |
| Hosting | Cloud (SaaS) |

## Recovery

| Field | Value |
|---|---|
| Criticality | Tier 3 - Standard |
| RTO | 72 hours |
| RPO | — |
| Recovery owner | **Unknown** |

## Integration neighbourhood

`Direction` below is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)), which is why an arrow into this application can still read as Outbound.

### Flows in — this application is the target

_None._

### Flows out — this application is the source

_None._

## Notes

Bought by sales operations, renewed on a departmental card, and in daily use across three functions with no IT owner attached. Nothing is broken, which is the reason it stayed invisible — this record exists because the inventory asked who owned it and nobody could answer.
No RPO recorded: the vendor holds the signed documents and the retention terms have not been read.

---

Source record: [`inventory/apps/data/e-signature.yaml`](data/e-signature.yaml)
