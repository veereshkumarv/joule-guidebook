# Scenario Library: Industry-specific

Same column conventions as `01-functional-scenarios.md`. All tags are starting assumptions to verify.

## Manufacturing / Automotive / High-tech
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-MFG-01 | Supplier part-shortage cascade impact on production lines | P5,P3 | CB | P,F |
| IND-MFG-02 | Engineering-change to BOM-impact explanation | P3 | CB | P |
| IND-MFG-03 | Warranty-claim root-cause clustering | P8 | CB/HY | P,F |
| IND-MFG-04 | Variant-configuration sales assistant | P2,P3 | CB | E |
| IND-MFG-05 | Tier-n supplier visibility Q&A | P3,P11 | CB | P,S |
| IND-MFG-06 | Production-line changeover optimisation insights | P8 | CB | P |
| IND-MFG-07 | Recall-scope determination by batch/VIN | P3 | CB | S,P |

## Consumer Products / Retail / Wholesale
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-RET-01 | Promotion uplift analysis narrative | P3,P8 | CB | F,P |
| IND-RET-02 | Store replenishment exception handling | P5,P4 | CB | P,E |
| IND-RET-03 | Assortment recommendation by cluster | P8 | CB | F,P |
| IND-RET-04 | Markdown optimisation what-if | P8 | CB | F |
| IND-RET-05 | Shrink/loss pattern detection | P8 | CB | F,S |
| IND-RET-06 | Customer-service return triage | P3,P4 | ST | E |
| IND-RET-07 | Product-description and attribute enrichment | P3 | HY | E |
| IND-RET-08 | Vendor-compliance chargeback dispute assistant | P3,P4 | CB | F |
| IND-RET-09 | Demand sensing from external signals | P8,P11 | HY | P |

## Consumer goods / Food and Beverage
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-FNB-01 | Shelf-life and expiry risk alerts | P5,P8 | CB | F,P |
| IND-FNB-02 | Recipe/formulation compliance lookup | P2 | CB | S |
| IND-FNB-03 | Trade-promotion settlement validation | P3 | CB | F |
| IND-FNB-04 | Allergen and labelling regulation Q&A | P2 | CB | S |
| IND-FNB-05 | Cold-chain deviation triage | P5 | CB | S,P |

## Oil, Gas, Energy, Utilities, Mining
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-EN-01 | Field-asset maintenance briefing from history and manuals | P2,P3 | CB | P,E |
| IND-EN-02 | Outage-impact customer communication drafting | P3 | HY | E,P |
| IND-EN-03 | Joint-venture accounting Q&A | P3 | ST | F |
| IND-EN-04 | HSE incident analysis and trend | P3 | CB | S |
| IND-EN-05 | Meter-to-cash exception handling | P3,P4 | ST | F,E |
| IND-EN-06 | Permit-to-work checklist generation | P2 | CB | S |
| IND-EN-07 | Mining haul-fleet downtime analysis | P3,P8 | CB | P |
| IND-EN-08 | Grid-asset risk-based inspection planning | P8 | CB | P,S |

## Financial Services / Insurance / Public sector
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-FS-01 | Policy and claims document Q&A | P2 | CB/HY | E |
| IND-FS-02 | Claims triage and fraud flag | P8 | CB/HY | F,S |
| IND-FS-03 | Regulatory-reporting assistance | P2,P3 | CB | S |
| IND-FS-04 | Customer onboarding KYC document checks | P7 | CB/HY | S,E |
| IND-FS-05 | Public-budget execution Q&A | P3 | ST | F |
| IND-FS-06 | Grant/subsidy application review summary | P2,P3 | CB | E |
| IND-FS-07 | Citizen-service case summarisation | P3 | HY | E |
| IND-FS-08 | Procurement-law compliance check for tenders | P2 | CB | S |

## Life Sciences / Healthcare / Pharma
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-LS-01 | Batch-record review assistance (GxP: human sign-off mandatory) | P2,P3 | CB | S,P |
| IND-LS-02 | Deviation and CAPA trend analysis | P8,P3 | CB | S,P |
| IND-LS-03 | Serialisation/track-and-trace exception handling | P3,P4 | CB | S |
| IND-LS-04 | Clinical-supply forecasting narrative | P8 | CB | P |
| IND-LS-05 | Regulatory-submission document search | P2 | CB | E,S |
| IND-LS-06 | Hospital supply-chain stock Q&A | P3 | ST | P |
| IND-LS-07 | Medical-device complaint classification | P8 | CB/HY | S |

## Professional Services / Media / Telecom
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-PS-01 | Project status and margin Q&A | P3 | ST | F,P |
| IND-PS-02 | Time-entry completion nudges and draft timesheets | P5,P4 | ST | E |
| IND-PS-03 | Resource matching to project demand | P8 | CB | P |
| IND-PS-04 | Statement-of-work drafting | P2,P3 | HY | E |
| IND-TEL-01 | Billing-dispute summarisation | P3 | ST | E,F |
| IND-TEL-02 | Network-incident to customer-impact mapping | P5,P3 | CB | P |
| IND-TEL-03 | Revenue-assurance anomaly detection | P8 | CB | F,S |

## Construction / Engineering / Real Estate / Transportation
| ID | Scenario | Pattern | Tag | Pillars |
|---|---|---|---|---|
| IND-CON-01 | Project cost-to-complete forecast explanation | P8,P3 | CB | F,P |
| IND-CON-02 | Subcontractor invoice validation vs. progress | P3 | CB | F,S |
| IND-CON-03 | Site-safety observation summarisation | P3 | HY | S |
| IND-RE-01 | Lease-contract Q&A and renewals | P2 | CB | F,E |
| IND-RE-02 | Service-charge settlement explanation | P3 | ST | F |
| IND-TR-01 | Freight-cost audit and exception detection | P8,P3 | CB | F |
| IND-TR-02 | Fleet-maintenance prioritisation | P8 | CB | P |
| IND-TR-03 | Delivery-ETA exception communications | P5 | CB/HY | E,P |
