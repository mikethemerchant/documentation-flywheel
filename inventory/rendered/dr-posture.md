<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# DR Posture

The core transactional system of record is **Enterprise Resource Planning (ERP)**, derived from the integration records as the application the most other systems write into — not configured anywhere.

## What writes into Enterprise Resource Planning (ERP)

Ordered by how badly it goes if the flow is interrupted. This is the list you want in front of you before a failover, and the one that is hardest to reconstruct under pressure.

| Source | Connection | Middleware | DR impact | Failover behaviour |
|---|---|---|---|---|
| EDI Gateway | EDI | EDI Gateway | Cannot stop - data loss risk | Trading partners transmit on their own schedule and do not retry on a rejected connection. Documents arriving during an outage are lost at the partner end, not queued locally. |
| Legacy Order Entry | Flat File (Manual) | Manual | **Unknown** | Not characterized. The file is produced and loaded by hand, so behaviour during an outage depends entirely on what the person doing it decides to do, and nobody has been asked. |
| Expense Management | File Transfer (SFTP) | Direct (none) | Stoppable - manual reconciliation | Approved expenses are exported on a schedule for reimbursement through accounts payable. A missed file is not re-sent automatically; finance identifies the gap at period close and re-exports the range by hand. |
| Warehouse Management (WMS) | Message Queue | Direct (none) | Stoppable - manual reconciliation | Orders flow out to the warehouse and confirmations flow back over a durable queue. The warehouse keeps picking against what it already holds, so on recovery the two stock positions have diverged and are reconciled by hand before the queue is drained. |
| Customer Relationship Management (CRM) | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays | Accepted quotes are posted through the integration platform, which holds them in a durable queue and replays on recovery. Sales can keep quoting during an ERP outage; orders land late rather than not at all. |
| Human Capital Management (HCM) | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays | Employee and cost-centre records are pushed through the integration platform, which queues and replays. Changes made during an outage arrive in order once the ERP is back. |

## Flags

Applications on their way out that still carry live data flows.

| Application | Lifecycle | Flow | DR impact | SME |
|---|---|---|---|---|
| [Legacy Order Entry](../apps/legacy-order-entry.md) | Retiring | Legacy Order Entry → Enterprise Resource Planning (ERP) | **Unknown** | **Unknown** |

## Every flow, by impact

### Cannot stop - data loss risk

| Flow | Connection | Failover behaviour |
|---|---|---|
| EDI Gateway → Enterprise Resource Planning (ERP) | EDI | Trading partners transmit on their own schedule and do not retry on a rejected connection. Documents arriving during an outage are lost at the partner end, not queued locally. |
| Enterprise Resource Planning (ERP) ↔ Tax Engine | API (SOAP) | Synchronous call during order entry and invoicing. If the tax engine is unreachable the ERP will not complete the document, so the flow cannot be stopped without stopping order entry with it. |

### Unknown — not characterized

| Flow | Connection | Failover behaviour |
|---|---|---|
| Identity Provider (SSO) → Human Capital Management (HCM) | API (REST) | Not characterized. Provisioning and deprovisioning calls are made as identity events occur; whether missed events are retried, replayed, or dropped depends on vendor behaviour that has not been tested. |
| Legacy Order Entry → Enterprise Resource Planning (ERP) | Flat File (Manual) | Not characterized. The file is produced and loaded by hand, so behaviour during an outage depends entirely on what the person doing it decides to do, and nobody has been asked. |

### Stoppable - manual reconciliation

| Flow | Connection | Failover behaviour |
|---|---|---|
| Expense Management → Enterprise Resource Planning (ERP) | File Transfer (SFTP) | Approved expenses are exported on a schedule for reimbursement through accounts payable. A missed file is not re-sent automatically; finance identifies the gap at period close and re-exports the range by hand. |
| Warehouse Management (WMS) ↔ Enterprise Resource Planning (ERP) | Message Queue | Orders flow out to the warehouse and confirmations flow back over a durable queue. The warehouse keeps picking against what it already holds, so on recovery the two stock positions have diverged and are reconciled by hand before the queue is drained. |

### Stoppable - queued, replays

| Flow | Connection | Failover behaviour |
|---|---|---|
| Customer Relationship Management (CRM) → Enterprise Resource Planning (ERP) | API (REST) | Accepted quotes are posted through the integration platform, which holds them in a durable queue and replays on recovery. Sales can keep quoting during an ERP outage; orders land late rather than not at all. |
| Human Capital Management (HCM) → Enterprise Resource Planning (ERP) | API (REST) | Employee and cost-centre records are pushed through the integration platform, which queues and replays. Changes made during an outage arrive in order once the ERP is back. |

### Stoppable - no data loss

| Flow | Connection | Failover behaviour |
|---|---|---|
| Endpoint Management → Enterprise Data Warehouse (EDW) | API (REST) | Vendor-side push on a nightly schedule, around 02:00. The endpoint management tenant holds its own device inventory and remains the system of record for it, so a missed run loses nothing — the next night's push carries the full state again rather than a delta. The visible effect of an outage is a compliance dashboard that is a day stale. |
| Enterprise Data Warehouse (EDW) → Business Intelligence (BI) | Database Link | Dashboards read live from the warehouse. During an outage they serve the last cached result and carry a staleness indicator; nothing is written and nothing is lost. |
| Enterprise Resource Planning (ERP) → Enterprise Data Warehouse (EDW) | Database Link | Nightly extract against a read replica. A missed run is re-run the following night with no loss, because the ERP remains the authoritative copy of everything this flow moves. |
| Human Capital Management (HCM) → Payroll | File Transfer (SFTP) | Employee, rate, and time changes move as a scheduled file drop. A missed drop is re-sent; the HCM stays authoritative and the payroll run reads whatever landed most recently. |
| Plant Historian → Enterprise Data Warehouse (EDW) | Database Link | Scheduled pull of aggregated tag data. The historian retains its own time-series locally, so a missed window is backfilled on the next run. |

## Application recovery targets

| Application | Tier | RTO | RPO | Recovery owner |
|---|---|---|---|---|
| [EDI Gateway](../apps/edi-gateway.md) | Tier 1 - Critical | 4 hours | 1 hour | Sofia Marchetti |
| [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | Tier 1 - Critical | 4 hours | 15 minutes | Tom Bergstrom |
| [Identity Provider (SSO)](../apps/identity-provider.md) | Tier 1 - Critical | 1 hour | 15 minutes | Ken Oyelaran |
| [Integration Platform (iPaaS)](../apps/integration-platform.md) | Tier 1 - Critical | 4 hours | 1 hour | Sofia Marchetti |
| [Warehouse Management (WMS)](../apps/warehouse-management.md) | Tier 1 - Critical | 4 hours | 15 minutes | Tom Bergstrom |
| [Customer Relationship Management (CRM)](../apps/customer-relationship-mgmt.md) | Tier 2 - Important | 24 hours | 4 hours | Tom Bergstrom |
| [Endpoint Management](../apps/endpoint-management.md) | Tier 2 - Important | 24 hours | 8 hours | Tom Bergstrom |
| [Enterprise Data Warehouse (EDW)](../apps/enterprise-data-warehouse.md) | Tier 2 - Important | 24 hours | 24 hours | Tom Bergstrom |
| [Human Capital Management (HCM)](../apps/human-capital-management.md) | Tier 2 - Important | 24 hours | 8 hours | Tom Bergstrom |
| [Payroll](../apps/payroll.md) | Tier 2 - Important | 24 hours | 24 hours | Tom Bergstrom |
| [Plant Historian](../apps/plant-historian.md) | Tier 2 - Important | 24 hours | 4 hours | Tom Bergstrom |
| [Tax Engine](../apps/tax-engine.md) | Tier 2 - Important | 8 hours | 1 hour | Sofia Marchetti |
| [Business Intelligence (BI)](../apps/business-intelligence.md) | Tier 3 - Standard | 72 hours | 24 hours | Tom Bergstrom |
| [Electronic Signature](../apps/e-signature.md) | Tier 3 - Standard | 72 hours | — | **Unknown** |
| [Expense Management](../apps/expense-management.md) | Tier 3 - Standard | 72 hours | 24 hours | Tom Bergstrom |
| [Legacy Order Entry](../apps/legacy-order-entry.md) | Tier 3 - Standard | Best effort | Best effort | **Unknown** |
| [Travel & Expense (T&E)](../apps/travel-and-expense.md) | — | — | — | — |
