# SAP Joule and SAP AI Implementation Repository

Internal source repository for designing, pitching and delivering Joule and SAP AI solutions, including hybrid designs that use non-SAP models.

> **Status: DRAFT v0.3 (2026-11-23).** v0.3 adds the delivery guide for development leads, an evidence-gated business-case model, and chapters on forecasting/shortage prediction and client confidence. Costs in the original guidebook remain **unvalidated placeholders**. Items marked **[VERIFY]** are tracked in `07-sdlc-guide/05-verify-register.md`. SAP renames and repackages AI products frequently; treat product names as of authoring date.

## Repository map

| Path | Purpose | Audience |
|---|---|---|
| `Joule_Implementation_Guidebook.md` | Pre-sales guide: value, samples, budget, roadmap, deck outline. **Part 5.3 ROI table is superseded by `08-value-cases/`** | Sales, architects, client sponsors |
| `01-architecture/` | Reference architectures (Mermaid) and 15 reusable patterns | Architects |
| `02-reference/` | BTP/SAP services catalogue; identity, security and compliance baseline | Everyone; security architects |
| `03-scenarios/` | Scenario library (241 scenarios) by function and industry, with prioritisation | Pre-sales, consultants |
| `04-multi-ai/` | Generative AI Hub with non-SAP models, MCP/agent interoperability, selection guide | AI architects |
| `05-templates/` | One-pager, readiness checklist, estimation worksheet, test-question bank, business case, ADR, demo script, tool register entry, system card | Delivery teams |
| `06-governance/` | Operating model, risk tiers, evaluation, cost control | Leadership, architects |
| **`07-sdlc-guide/`** | **Gap analysis; SDLC playbook with gates; engineering standards; secure-by-design addendum; 90-day lead runbook; VERIFY register** | **Development leads, architects** |
| **`08-value-cases/`** | **Evidence register with quality tiers; runnable business-case model (`value_model.py`); use-case value cards; objection-handling guide** | **Sales, engagement leads, finance** |
| **`09-forecasting-shortage/`** | **Knowledge graph, MCP and AI-concept design for demand forecasting and shortage prediction** | **Architects, supply-chain leads** |
| **`10-client-confidence/`** | **`01`: what clients distrust, what the evidence supports for graphs/MCP/other techniques, SAP trust artefacts, scorecard. `02`: Trust Stack architecture, Trust Pack artefacts, confidence ladder, dev-lead checklist. `03`: per-scenario playbook (when a graph, semantic layer or MCP earns its place), worked AP example, tool register example, 30-minute confidence demo, talk track** | **Engagement leads, architects, security counterparts** |
| **`11-knowledge-graph/`** | **General build guide for a knowledge graph on S/4HANA + SAP HANA Cloud (RDF, property graph, vector), ontology, pipeline, tool layer, GraphRAG and other AI usage patterns, authorization, ADRs, client positioning. Draft: product details are VERIFY items** | **Architects, knowledge engineers, engagement leads** |
| `_archive/` | Superseded drafts kept for reference (`10-confidence-by-design`, merged into `10-client-confidence/` on 2026-11-23) | n/a |
| `_research/` | Source research (read-only evidence files with URLs, dates, confidence). Each figure in chapters 08 to 10 traces here | Everyone |

## How to use

1. **Pre-sales:** pick scenarios in `03-scenarios/`, fill template T1, and build the case with `08-value-cases/` (use the objection guide; present the model's conservative, base and upside cases and break-even requirement; never quote tier D figures as expected results).
2. **Design:** pick patterns in `01-architecture/`, run the readiness checklist, write the starter ADRs from `07-sdlc-guide/01-sdlc-playbook.md`.
3. **Delivery:** follow `07-sdlc-guide/04-lead-implementation-runbook.md`, apply the engineering standards and secure-by-design addendum, and report against the scorecard in `10-client-confidence/`.
4. **Forecasting/shortage engagements:** start with section 0 of `09-forecasting-shortage/01-design-guide.md` (standard-first check against IBP).
5. **Contribute:** every new scenario or pattern uses the templates and carries a maturity tag; every new figure carries a source, date and evidence tier.

## Read first (the five things that matter most)
1. The original ROI table was not supported by its own samples; the rebuilt model shows evidence-backed benefits cover only part of what a roughly EUR 1M programme must return. Design for cost discipline, cash-linked benefits and gated funding (`08-value-cases/02-business-case-model.md`).
2. Independent evidence for SAP-specific benefits (Joule, ABAP AI, supply-chain agents) does not yet exist; SAP customer figures are unaudited and sometimes inconsistent. Pilots are how we create the evidence.
3. No licence prices have been confirmed. Get SAP's written quote before showing any budget.
4. Knowledge graphs and MCP are tools to test, not claims to sell (`10-client-confidence/`).
5. Identity propagation must be proven end to end in the first sprint (`07-sdlc-guide/04-lead-implementation-runbook.md`).

## Maturity tags used throughout

- **[GA-Embedded]**: standard, delivered by SAP in the application (verify the release/edition).
- **[Studio]**: buildable with Joule Studio / SAP Build (low-code) **[VERIFY availability]**.
- **[Custom-BTP]**: custom build on BTP (CAP/Kyma, Generative AI Hub, Integration Suite).
- **[Hybrid-AI]**: involves a non-SAP model or service.
- **[Roadmap]**: announced but not confirmed generally available; never promise to a client.

## Pillar tags

**F** Finance, **E** Efficiency, **S** Security/Compliance, **P** Performance.

## Evidence tiers (used in `08-value-cases/`)

**A/B** independent measured or surveyed; **C** customer-reported, unaudited; **D** vendor/consultancy claim or modelled; **client pilot data** overrides all. See `08-value-cases/01-evidence-register.md`.
