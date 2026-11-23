# Integration and Design Patterns

Each pattern: **Intent / When / Components / Watch-outs**.

## P1. Embedded standard scenario
- **Intent:** Use SAP-delivered Joule capability.
- **When:** Scenario exists for the client's release/edition.
- **Components:** Application + Joule enablement + IAS.
- **Watch-outs:** Release dependencies; role assignment; user training.

## P2. Retrieval-Augmented Generation (document grounding)
- **Intent:** Answer from policies, contracts, manuals.
- **Components:** Document store, chunking/embedding, HANA Cloud Vector Engine, Generative AI Hub (embedding + chat), access-control metadata per chunk.
- **Watch-outs:** Enforce document-level permissions at retrieval; version control of sources; show citations.

## P3. Read-only data Q&A over SAP data
- **Intent:** Natural-language queries on business data.
- **Components:** S/4 CDS/OData APIs or BDC semantic models; Joule skill; Generative AI Hub for summarisation.
- **Watch-outs:** Prefer curated semantic views over free-form SQL generation; row/column-level security.

## P4. Action with human approval
- **Intent:** AI proposes, human approves, system executes.
- **Components:** Joule skill, SAP Build Process Automation/Workflow, S/4 write API, audit.
- **Watch-outs:** Idempotency, rollback, clear confirmation text showing what changes.

## P5. Event-triggered proactive agent
- **Intent:** Agent reacts to business events (blocked invoice, delayed PO).
- **Components:** S/4 business events → Event Mesh → CAP/Kyma service → agent → notification (Joule, email, Teams).
- **Watch-outs:** Event storms/cost; dedupe; throttling.

## P6. Multi-agent orchestration
- **Intent:** Specialist agents per domain coordinated by one orchestrator.
- **Components:** Joule agents / Studio, shared context store, tool registry.
- **Watch-outs:** Loop control, max steps, per-agent permissions, trace logging.

## P7. Document-to-transaction (intelligent capture)
- **Intent:** Extract fields from invoices, orders, contracts and create drafts.
- **Components:** Document Information Extraction or LLM extraction, validation rules, S/4 draft API, exception queue.
- **Watch-outs:** Confidence thresholds; fallback to human; duplicate detection.

## P8. Predictive plus generative
- **Intent:** Numeric prediction (forecast, risk score) explained in language.
- **Components:** SAP foundation model / ML in AI Core / SAC predictive; Joule summarisation.
- **Watch-outs:** Do not let the LLM calculate numbers; compute in deterministic services and let the LLM narrate.

## P9. Side-by-side extension (clean core)
- **Intent:** Custom AI logic without modifying S/4 core.
- **Components:** CAP app on BTP, APIs/events from S/4, Generative AI Hub, Work Zone integration.
- **Watch-outs:** Stay on released APIs; avoid direct DB access.

## P10. Developer productivity (Joule for developers, Build Code)
- **Intent:** AI assists ABAP/CAP/Fiori development, test generation, code explanation.
- **Components:** ABAP Development Tools or Business Application Studio with AI assist **[VERIFY availability]**.
- **Watch-outs:** Code review still mandatory; IP and data policies.

## P11. Cross-vendor agent interoperability
- **Intent:** Joule agents collaborate with third-party agents (ServiceNow, Salesforce, Microsoft Copilot, custom).
- **Components:** Standard protocols (MCP, agent-to-agent) **[VERIFY SAP support status]**, API Management, token exchange.
- **Watch-outs:** Trust boundaries, least privilege, data minimisation, contract on data sharing.

## P12. Prompt and PII protection gateway
- **Intent:** Mask sensitive data before external model calls.
- **Components:** Data masking/anonymisation in Generative AI Hub **[VERIFY]**, custom pre-processor, allow-lists.
- **Watch-outs:** Re-identification risk; logging policy.

## P13. Evaluation and feedback loop
- **Intent:** Keep quality measurable.
- **Components:** Test question bank, automated eval runs, thumbs up/down capture, dashboards.
- **Watch-outs:** Re-run evaluation on every model, prompt or release change.

## P14. Cost and quota control
- **Intent:** Prevent runaway consumption.
- **Components:** Model deployment limits, per-app quotas, BTP usage alerts, caching of repeated queries, smaller models for simple tasks.

## P15. Fallback and degradation
- **Intent:** Graceful behaviour when AI is unavailable or low confidence.
- **Components:** Static help, deep link to classic transaction, "I'm not sure" responses with escalation path.

## Pattern selection matrix

| Need | Pattern(s) |
|---|---|
| Quick win, minimal build | P1 |
| Policy / knowledge Q&A | P2 |
| Business data questions | P3, P8 |
| Automating a process step | P4, P5, P7 |
| Cross-system processes | P6, P11 |
| Regulated data to external models | P12 + P14 |
| Dev team acceleration | P10 |
