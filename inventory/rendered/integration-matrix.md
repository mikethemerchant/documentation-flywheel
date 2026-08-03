<!-- GENERATED FILE — DO NOT EDIT.
     Written by automation/render-inventory.py from the YAML records in
     inventory/apps/data/ and inventory/integrations/data/.
     Edit the source records and re-render; edits here are overwritten. -->

# Integration Matrix

12 integration records across 13 of 17 applications.

## Grid

Rows are sources, columns are targets. ● is a one-way flow, ◆ is bidirectional.

| → target | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1.** Business Intelligence (BI) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **2.** Customer Relationship Management (CRM) |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| **3.** EDI Gateway |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| **4.** Enterprise Data Warehouse (EDW) | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| **5.** Enterprise Resource Planning (ERP) |  |  |  | ● |  |  |  |  |  |  |  | ◆ | ◆ |
| **6.** Expense Management |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| **7.** Human Capital Management (HCM) |  |  |  |  | ● |  |  |  |  | ● |  |  |  |
| **8.** Identity Provider (SSO) |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| **9.** Legacy Order Entry |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| **10.** Payroll |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **11.** Plant Historian |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| **12.** Tax Engine |  |  |  |  | ◆ |  |  |  |  |  |  |  |  |
| **13.** Warehouse Management (WMS) |  |  |  |  | ◆ |  |  |  |  |  |  |  |  |

## Every integration

`Direction` is stated relative to the core transactional system of record (Enterprise Resource Planning (ERP)) — **Inbound** means it writes into that system.

| Source | Target | Direction | Connection | Middleware | DR impact |
|---|---|---|---|---|---|
| [Customer Relationship Management (CRM)](../apps/customer-relationship-mgmt.md) | [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | Inbound | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays |
| [EDI Gateway](../apps/edi-gateway.md) | [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | Inbound | EDI | EDI Gateway | Cannot stop - data loss risk |
| [Enterprise Data Warehouse (EDW)](../apps/enterprise-data-warehouse.md) | [Business Intelligence (BI)](../apps/business-intelligence.md) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |
| [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | [Enterprise Data Warehouse (EDW)](../apps/enterprise-data-warehouse.md) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |
| [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | [Tax Engine](../apps/tax-engine.md) | Bidirectional | API (SOAP) | Direct (none) | Cannot stop - data loss risk |
| [Expense Management](../apps/expense-management.md) | [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | Inbound | File Transfer (SFTP) | Direct (none) | Stoppable - manual reconciliation |
| [Human Capital Management (HCM)](../apps/human-capital-management.md) | [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | Inbound | API (REST) | Integration Platform (iPaaS) | Stoppable - queued, replays |
| [Human Capital Management (HCM)](../apps/human-capital-management.md) | [Payroll](../apps/payroll.md) | Outbound | File Transfer (SFTP) | Direct (none) | Stoppable - no data loss |
| [Identity Provider (SSO)](../apps/identity-provider.md) | [Human Capital Management (HCM)](../apps/human-capital-management.md) | Outbound | API (REST) | Direct (none) | **Unknown** |
| [Legacy Order Entry](../apps/legacy-order-entry.md) | [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | Inbound | Flat File (Manual) | Manual | **Unknown** |
| [Plant Historian](../apps/plant-historian.md) | [Enterprise Data Warehouse (EDW)](../apps/enterprise-data-warehouse.md) | Outbound | Database Link | Direct (none) | Stoppable - no data loss |
| [Warehouse Management (WMS)](../apps/warehouse-management.md) | [Enterprise Resource Planning (ERP)](../apps/meridian-erp.md) | Bidirectional | Message Queue | Direct (none) | Stoppable - manual reconciliation |

## Applications with no integration records

Either genuinely standalone, or connected by something nobody has recorded yet. The inventory cannot tell you which, and that is worth saying out loud rather than rendering as an empty row.

| Application | Lifecycle | Team |
|---|---|---|
| [Electronic Signature](../apps/e-signature.md) | Active | Applications |
| [Endpoint Management](../apps/endpoint-management.md) | Active | Infrastructure |
| [Integration Platform (iPaaS)](../apps/integration-platform.md) | Active | Data & Integrations |
| [Travel & Expense (T&E)](../apps/travel-and-expense.md) | Evaluating | Applications |
