# Scenario Library: Functional (cross-industry)

Columns: **ID | Scenario | Pattern (see integration-patterns.md) | Tag | Pillars**.
Tags: GA = [GA-Embedded], ST = [Studio], CB = [Custom-BTP], HY = [Hybrid-AI]. Tags are **starting assumptions: verify** current SAP coverage before proposing. Pillars: F, E, S, P.

## A. Finance: General Ledger, Close, Reporting
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| FIN-001 | Natural-language GL line-item and balance queries | P3 | GA/ST | E |
| FIN-002 | Close-task status and overdue summary | P3 | ST | F,E |
| FIN-003 | Variance explanation plan vs. actual | P3,P8 | ST/CB | F,P |
| FIN-004 | Journal entry draft from description | P4 | ST | E,F |
| FIN-005 | Journal entry anomaly detection | P8 | CB | F,S |
| FIN-006 | Intercompany mismatch explanation and proposal | P3,P4 | ST | F,E |
| FIN-007 | Accrual proposal assistant | P4,P8 | CB | F |
| FIN-008 | Reconciliation break explanation (bank, subledger) | P3 | ST | F,E |
| FIN-009 | Management commentary drafting for reports | P3 | CB/HY | E |
| FIN-010 | Narrative reporting for board packs | P3 | HY | E |
| FIN-011 | Account determination "why was this account used" | P3 | ST | E |
| FIN-012 | Foreign currency revaluation explanation | P3 | ST | F |
| FIN-013 | Fixed-asset query and capitalisation advice | P2,P3 | ST | F,E |
| FIN-014 | Lease accounting Q&A (IFRS16 policies) | P2 | CB | F,S |
| FIN-015 | Chart-of-accounts mapping suggestions during migration | P8 | CB/HY | E |
| FIN-016 | Period-end checklist auto-generation | P6 | ST | E |
| FIN-017 | Audit PBC request assistant | P2,P3 | CB | S,E |
| FIN-018 | Tax code determination explanation | P2,P3 | CB | F,S |
| FIN-019 | Statutory reporting Q&A | P2 | CB | S |
| FIN-020 | Consolidation elimination explanation | P3 | ST | F |

## B. Finance: Receivables, Payables, Treasury
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| AR-001 | Overdue receivables summary by customer/segment | P3 | GA/ST | F |
| AR-002 | Dunning letter draft personalised by history | P3 | CB/HY | F,E |
| AR-003 | Payment promise tracking and follow-up agent | P5,P6 | ST | F,E |
| AR-004 | Cash application matching suggestions | P8 | GA/CB | F,E |
| AR-005 | Dispute case summary and resolution proposal | P3 | ST | F,E |
| AR-006 | Credit limit review recommendation | P8 | CB | F,S |
| AR-007 | Customer risk score explanation | P8 | CB | F,P |
| AP-001 | Blocked invoice explanation and routing | P3,P4 | ST | F,E |
| AP-002 | Invoice capture from PDF/email to draft | P7 | GA/CB | E |
| AP-003 | Duplicate invoice detection | P8 | CB | F,S |
| AP-004 | Three-way match exception triage | P3,P4 | ST | E,F |
| AP-005 | Vendor bank-detail change fraud flagging | P8,P4 | CB | S,F |
| AP-006 | Early-payment discount optimiser | P8 | CB | F |
| AP-007 | Vendor statement reconciliation | P7,P3 | CB/HY | E,F |
| AP-008 | Payment run exception summary | P3 | ST | E |
| TRE-001 | Cash position Q&A | P3 | ST | F,P |
| TRE-002 | Cash-flow forecast narrative | P8 | CB | F,P |
| TRE-003 | Bank statement exception handling | P3,P4 | ST | E |
| TRE-004 | FX exposure explanation and hedge-policy lookup | P2,P3 | CB | F,S |
| TRE-005 | Working-capital improvement recommender | P8 | CB/HY | F,P |
| TRE-006 | Liquidity scenario "what-if" via natural language | P8 | CB | P,F |

## C. Controlling, Planning, Analytics
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| CO-001 | Cost-centre overspend alert with explanation | P5,P3 | ST | F |
| CO-002 | Profitability analysis Q&A (product, customer) | P3 | ST | F,P |
| CO-003 | Allocation cycle explanation | P3 | ST | E |
| CO-004 | Product cost variance drivers | P3,P8 | CB | F,P |
| CO-005 | Planning assistant (draft budgets from drivers) | P8 | ST/CB | F,P |
| CO-006 | Forecast accuracy review | P3,P8 | CB | P |
| CO-007 | Natural-language dashboard creation in analytics | P3 | GA/ST | E |
| CO-008 | Story/slide generation from KPIs | P3 | HY | E |
| CO-009 | Scenario simulation (price, volume, FX) | P8 | CB | P,F |
| CO-010 | Cost-to-serve analysis | P3,P8 | CB | F,P |

## D. Procurement and Sourcing
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| PRO-001 | Purchase requisition creation by chat | P4 | GA/ST | E |
| PRO-002 | Catalog item search by description | P2,P3 | ST | E |
| PRO-003 | PO status and delivery tracking | P3 | GA/ST | E |
| PRO-004 | Supplier shortlist suggestion for RFQ | P3,P8 | ST/CB | E,F |
| PRO-005 | RFQ drafting and bid comparison summary | P3 | CB/HY | E |
| PRO-006 | Contract clause extraction and risk flags | P2,P7 | CB/HY | S,F |
| PRO-007 | Contract compliance check against PO | P3 | CB | S,F |
| PRO-008 | Spend analytics Q&A | P3 | ST | F,P |
| PRO-009 | Tail-spend consolidation recommender | P8 | CB | F |
| PRO-010 | Supplier risk monitoring with news and events | P5,P11 | CB/HY | S,P |
| PRO-011 | Supplier onboarding assistant and document checks | P4,P7 | ST/CB | E,S |
| PRO-012 | Supplier performance scorecard narration | P3 | ST | P |
| PRO-013 | Maverick-buying detection | P8 | CB | F,S |
| PRO-014 | Price-variance explanation on invoice | P3 | ST | F |
| PRO-015 | Sustainability/ESG supplier questionnaire analysis | P2,P7 | CB/HY | S |
| PRO-016 | Negotiation preparation brief | P3,P2 | HY | F |
| PRO-017 | Auto-classification of spend categories | P8 | CB | E |
| PRO-018 | Approval-chain explanation ("who must approve?") | P3 | ST | E |
| PRO-019 | Guided buying: policy-compliant alternatives | P2,P3 | ST | F,S |
| PRO-020 | Goods-receipt entry by chat or photo | P4,P7 | CB | E |

## E. Supply Chain, Logistics, Planning
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| SCM-001 | Stock-out risk Q&A | P3,P8 | ST | P,F |
| SCM-002 | Delayed inbound shipment impact on orders | P5,P3 | ST/CB | P,F |
| SCM-003 | Demand-forecast explanation | P8 | GA/CB | P |
| SCM-004 | Safety-stock parameter recommendation | P8 | CB | P,F |
| SCM-005 | Excess/obsolete stock identification | P3,P8 | CB | F,P |
| SCM-006 | Expedite vs. cost trade-off advisor | P8 | CB | F,P |
| SCM-007 | Transportation exception triage | P5,P4 | ST | P,E |
| SCM-008 | Carrier selection suggestions | P8 | CB | F,P |
| SCM-009 | ATP / delivery date explanation | P3 | ST | E,P |
| SCM-010 | Warehouse task prioritisation | P8 | CB | P,E |
| SCM-011 | Inventory count variance analysis | P3 | ST | F,S |
| SCM-012 | Supply-plan "what-if" scenario narration | P8 | ST | P |
| SCM-013 | Network disruption (weather, port, geopolitical) alert | P5,P11 | CB/HY | P,S |
| SCM-014 | Customs and trade compliance Q&A | P2 | CB | S |
| SCM-015 | Batch/serial traceability query | P3 | ST | S,P |
| SCM-016 | Recall impact analysis | P3 | CB | S,P |
| SCM-017 | Packaging/returns processing assistant | P4 | ST | E |
| SCM-018 | S&OP meeting summary and action capture | P3 | HY | E |
| SCM-019 | Lead-time deviation explanation | P3,P8 | CB | P |
| SCM-020 | Digital supply-chain twin Q&A | P3 | CB | P |

## F. Manufacturing and Quality
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| MFG-001 | Production order status and delay root cause | P3 | ST | P,E |
| MFG-002 | Shift handover summary | P3 | CB/HY | E,P |
| MFG-003 | Work instruction retrieval for operators | P2 | CB | E,P |
| MFG-004 | Downtime cause analysis | P3,P8 | CB | P |
| MFG-005 | OEE narrative and improvement ideas | P8,P3 | CB | P |
| MFG-006 | Quality notification triage and classification | P8,P4 | CB | P,S |
| MFG-007 | Deviation/CAPA drafting assistance | P2,P4 | CB/HY | S,P |
| MFG-008 | Material shortage explanation and alternatives | P3,P8 | ST | P |
| MFG-009 | Routing/BOM change impact analysis | P3 | CB | P,F |
| MFG-010 | Scrap and yield variance explanation | P3 | ST | F,P |
| MFG-011 | Visual inspection result summary | P8 | HY | P |
| MFG-012 | Engineering change request summarisation | P2,P3 | CB | E |
| MFG-013 | Energy consumption anomalies | P8 | CB | F,P |
| MFG-014 | Safety incident lookup and trend | P3 | CB | S |
| MFG-015 | New-hire operator training assistant | P2 | CB | E |

## G. Asset Management and Maintenance
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| EAM-001 | Maintenance notification creation from natural language/photo | P4,P7 | ST/CB | E |
| EAM-002 | Failure-mode lookup from history and manuals | P2 | CB | P |
| EAM-003 | Predictive maintenance risk explanation | P8 | CB | P,F |
| EAM-004 | Spare-part availability and substitutes | P3 | ST | P |
| EAM-005 | Work-order summary and next steps for technicians | P3,P2 | CB | E |
| EAM-006 | Maintenance backlog prioritisation | P8 | CB | P |
| EAM-007 | Permit/safety checklist generation | P2 | CB | S |
| EAM-008 | Asset cost of ownership analysis | P3 | CB | F |

## H. Sales, Service, Customer Experience
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| SAL-001 | Sales order status and customer account summary | P3 | GA/ST | E |
| SAL-002 | Quote drafting from RFP text | P4,P7 | CB/HY | E,F |
| SAL-003 | Pricing/discount guidance within policy | P2,P3 | CB | F,S |
| SAL-004 | Backorder and delivery-risk communication drafting | P3 | ST/HY | E,P |
| SAL-005 | Next-best-action for accounts | P8 | CB | P,F |
| SAL-006 | Return/credit memo processing | P4 | ST | E |
| SAL-007 | Customer 360 brief before meeting | P3 | ST/HY | E |
| SAL-008 | Contract renewal opportunity detection | P8 | CB | F |
| SAL-009 | Product configuration assistance | P2,P3 | CB | E |
| SAL-010 | Sales-order entry from email | P7,P4 | CB | E |
| SRV-001 | Service-ticket summarisation and classification | P3,P8 | ST | E |
| SRV-002 | Suggested resolution from knowledge base | P2 | CB | E,P |
| SRV-003 | Field-service job briefing | P3,P2 | CB | E,P |
| SRV-004 | Warranty-claim validation | P3,P8 | CB | F,S |
| SRV-005 | Customer sentiment and churn indicators | P8 | HY | P,F |

## I. Human Resources
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| HR-001 | Employee self-service Q&A (leave, benefits) | P2,P3 | GA | E |
| HR-002 | Job description generation | P3 | GA | E |
| HR-003 | Candidate summary and interview question suggestions | P3 | GA | E (EU AI Act: high-risk, review) |
| HR-004 | Onboarding checklist and buddy assistant | P4,P6 | ST | E |
| HR-005 | Learning recommendations | P8 | GA | P |
| HR-006 | Goal and performance-review drafting assistance | P3 | GA | E |
| HR-007 | Compensation-policy Q&A for HRBPs | P2 | CB | S,E |
| HR-008 | Workforce analytics Q&A | P3 | ST | P |
| HR-009 | Attrition-risk insight (privacy-sensitive) | P8 | CB | P,S |
| HR-010 | Policy change impact summaries | P2 | CB | S |
| HR-011 | Contingent-workforce request handling | P4 | ST | E,F |
| HR-012 | Payroll exception explanation | P3 | ST | F,E |
| HR-013 | Time-sheet anomaly detection | P8 | CB | F,S |
| HR-014 | Internal mobility matching | P8 | GA/CB | P |
| HR-015 | Manager-coaching prompts | P3 | HY | P |

## J. Travel and Expense
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| TE-001 | Expense report draft from receipts | P7 | GA | E |
| TE-002 | Policy compliance check | P2 | GA/ST | S,F |
| TE-003 | Duplicate/fraud-pattern expense detection | P8 | GA/CB | S,F |
| TE-004 | Trip planning within policy | P4 | ST | E,F |
| TE-005 | Travel-spend analytics Q&A | P3 | ST | F |

## K. IT, Basis, Security, GRC (SAP landscape operations)
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| SEC-001 | SoD conflict explanation and remediation options | P3,P4 | CB | S |
| SEC-002 | Access-request recommendation and risk summary | P3 | CB | S,E |
| SEC-003 | Periodic access-review preparation | P3 | CB | S,E |
| SEC-004 | Firefighter/emergency access log review | P3,P8 | CB | S |
| SEC-005 | Policy/control Q&A | P2 | CB | S,E |
| SEC-006 | Audit-evidence collection agent | P6 | CB | S,E |
| SEC-007 | Security alert triage summary | P3,P8 | CB/HY | S |
| SEC-008 | Role design suggestions from usage | P8 | CB | S,E |
| SEC-009 | Data-privacy request (DSAR) assistance | P3,P4 | CB | S |
| SEC-010 | Third-party/vendor risk questionnaire answers from policies | P2 | HY | S,E |
| OPS-001 | Incident summary and probable-cause suggestion | P3,P2 | CB | P,E |
| OPS-002 | Job-monitoring: failed batch job diagnosis | P3 | CB | P,E |
| OPS-003 | Interface/IDoc error explanation and fix proposal | P3,P4 | CB | E,P |
| OPS-004 | Transport-risk analysis | P3 | CB | S,P |
| OPS-005 | Cloud cost and consumption Q&A | P3 | CB | F |
| OPS-006 | Release-notes impact analysis for client config | P2,P3 | CB/HY | P,E |
| OPS-007 | Runbook retrieval | P2 | CB | E |
| OPS-008 | Performance bottleneck explanation (SQL/ABAP traces) | P3 | CB/HY | P |

## L. Development and Migration
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| DEV-001 | ABAP code explanation and documentation | P10 | GA | E |
| DEV-002 | ABAP unit test generation | P10 | GA | E,P |
| DEV-003 | Custom-code clean-core remediation suggestions | P10 | CB/HY | P,E |
| DEV-004 | CAP/Fiori app scaffolding with AI | P10 | GA | E |
| DEV-005 | Functional spec to technical spec drafting | P10 | HY | E |
| DEV-006 | Data-migration mapping suggestions | P8 | CB/HY | E |
| DEV-007 | Test-case generation from process docs | P10 | HY | E,P |
| DEV-008 | Code review assistant for security patterns | P10 | HY | S |
| DEV-009 | Release-note and change-log generation | P10 | HY | E |
| DEV-010 | Landscape documentation from LeanIX/Signavio models | P3 | ST/CB | E |

## M. Sustainability and Compliance
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| ESG-001 | Carbon footprint query by product/site | P3 | ST/CB | S,P |
| ESG-002 | ESG disclosure drafting (CSRD) | P2,P3 | HY | S |
| ESG-003 | Supplier ESG risk Q&A | P3,P2 | CB | S |
| ESG-004 | Energy-saving recommendation | P8 | CB | F,P |
| ESG-005 | Regulation-change impact summary | P2 | HY | S |
