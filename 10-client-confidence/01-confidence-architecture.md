# Building Client Confidence: Knowledge Graphs, MCP and Related AI Concepts

Status: DRAFT v0.1. Evidence references point to `_research/*.md` (agent-gathered, each figure read at the cited source; see each file's confidence column). SAP product capabilities marked **[VERIFY]** are tracked in `07-sdlc-guide/05-verify-register.md`. This chapter changes how the technology is *used and shown*, not just what is built.

## 1. Start from what clients actually distrust

Confidence cannot be asserted; it has to be produced by evidence the client can inspect. The research shows the concerns are specific, measured, and mostly reasonable:

| Client concern | What the evidence says (source in `_research/independent-roi-evidence.md` unless noted) | Implication |
|---|---|---|
| "AI doesn't return value for cost" | PwC 2026 (4,454 CEOs): 56% see no significant financial benefit to date. McKinsey 2026: 37% attribute any EBIT impact. Deloitte 2025: satisfactory ROI typically takes 2 to 4 years vs 7 to 12 months for usual tech. | Do not promise fast payback; prove value in stages and let the client stop early. |
| "It will be wrong and confidently so" | Stack Overflow 2025: 45.7% of developers distrust AI accuracy vs 32.7% who trust it (`comparable-cases.md`). Deloitte Australia refunded fees on a report with nonexistent citations (Guardian, Oct 2025). | Every claim traceable to a source; abstain when unsure; verify citations automatically. |
| "Our data will leak" | HMRC Copilot evaluation: 46% of non-users cited security/privacy (`comparable-cases.md`). | Show the authorization and data-flow proof, not a policy slide. |
| "Who is accountable?" | Deloitte 2026: for 23% of respondents accountability for a negative AI outcome is unclear. | Named owners and decision rights per scenario (governance doc). |
| "Costs will run away" | Gartner (Aug 2026): inference cost per agentic workflow to rise more than fivefold through 2028. Deloitte 2026: 71% track total AI spend, only 44% track per-unit cost. | Per-interaction unit economics visible from day one. |
| "Nobody will use it" | UK DBT pilot: weekly active 64%, no evidence time savings improved productivity; Treasury trial: most used it 2 to 3 times a week or less (`comparable-cases.md`). BCG 2026: 66% of frontline users get little or no guidance on using saved time. | Adoption and workflow redesign are part of the proof, not an afterthought. |
| "Vendors overpromise" | Gartner: only about 130 of thousands of agentic vendors are real ("agent washing"). | Show working, measured behaviour on the client's own data. |
| "Replacing people backfires" | Klarna rehired human agents after quality dropped; CBA reversed 45 job cuts after its voice-bot raised call volumes. | Position AI as augmentation with human fallback; avoid headcount-reduction narratives. |

**Use this table as a workshop tool.** In the first client session, list these concerns (plus any of their own) and ask each stakeholder to rank them. The ranking decides which proof artefacts are built first (section 11 maps gap to lead technique; `02-trust-stack-and-trust-pack.md` lists the artefacts).

Honest framing for sponsors: the sceptical headlines are weaker than they look (e.g. MIT's "95%" rests on 52 interviews and a six-month, deployment-with-KPIs definition), but the direction across independent sources is consistent. Show the client you have read both sides.

### 1a. How strong is the evidence for the practices in this chapter?

Be candid with clients about this; it is itself a confidence builder.

- **Where trust is low is well documented.** KPMG/University of Melbourne (48,340 people, 47 countries, 2025): 46% willing to trust AI systems. Gartner (survey of IT application leaders, reported by The Register, Oct 2025): only 19% had high trust in vendors' ability to protect against hallucinations, 74% saw agents as a new attack vector. BCG 2026: more than half still have privacy and cybersecurity concerns; 41% worry about lack of control or understanding of AI decisions.
- **Which interventions raise trust or adoption is not well documented.** The research found **no controlled or quasi-experimental enterprise study** showing that explanations, citations, staged rollout, governance programmes or training raise adoption or ROI. The supporting evidence is self-reported correlation (e.g. BCG: positive sentiment 15% to 55% with strong leadership support), stated intent (Edelman, US: 59% say transparency about inaccuracies would raise their enthusiasm), and small lab studies (explanations reduce over-reliance only when they make verification cheaper).
- **Grounding does not remove errors.** The one independent test of RAG-grounded commercial tools (legal research, 2024 versions) found they still hallucinated 17% to 33% of the time, against vendor claims of "hallucination-free". No equivalent independent test exists for ERP, finance or procurement copilots, so **we must measure it on the client's own data** rather than cite it.
- **Therefore:** treat every practice below as a **design hypothesis that we test and show results for in the pilot**, not as a proven lever. The commitment to the client is "we will measure and show you", not "this technique makes AI trustworthy".

## 2. A working definition: confidence = five verifiable properties

| Property | Client question | Proof artefact |
|---|---|---|
| **Verifiable** | "How do I know this answer is right?" | Citations, source objects, reproducible tool outputs, evaluation scorecard |
| **Controlled** | "Can it only do what it should?" | Authorization tests, scoped tools, approval workflow, autonomy level |
| **Contained** | "If it fails, how bad is it?" | Kill switch drill, rollback, blast-radius limits, incident playbooks |
| **Valuable** | "Is it worth the money?" | Baselines, control groups, benefit register, unit economics |
| **Transparent** | "Can I audit and understand it?" | Audit logs, AI inventory, model register, decision records, dashboards |

Each technology below is justified by which property it strengthens and what evidence it produces. If it produces no client-visible evidence, it does not belong in the confidence story.

## 3. Knowledge graphs: where they build confidence, and where they don't

**What they provide**
1. **Provenance and explainable paths.** An answer such as "Order 4711 is at risk" can be shown as a path: order → material → BOM component → supplier PO → late shipment. The client can inspect each hop and click through to the S/4 object. That is a stronger verification experience than a paragraph of prose.
2. **Deterministic relationship logic.** Impact, dependency and "who owns this" are computed by graph traversal, not generated, so the same question yields the same answer.
3. **One business vocabulary.** The ontology defines "critical customer", "at-risk order", "tier-2 supplier" once; agents and reports use identical definitions, which removes a common source of disputed numbers.
4. **Scoped grounding.** Retrieval limited to the entities the user is allowed to see (with access control applied at query time).

**Honest limits (say these to the client), from `_research/forecasting-kg-mcp-evidence.md`**
- Evidence that graph grounding improves answer accuracy is **narrower than vendor narratives suggest**. Independent text-corpus benchmarks show graphs help on multi-hop and summarisation questions and are neutral or worse on single-hop lookups (single-hop F1: vector RAG 64.78 vs KG-triplet GraphRAG 34.28; fact-retrieval accuracy 60.92 vs 60.14), and graph methods can cost many more query tokens (about 38,700 vs 879 prompt tokens in one configuration). Microsoft's own 72% to 83% win rates measure breadth of summaries judged by an LLM, not factual accuracy.
- The strongest enterprise-data result (GPT-4 zero-shot, SQL 16% vs knowledge-graph layer 54%, insurance schema) is a preprint abstract by authors from a graph vendor; a follow-up reached 72% **including 8% "I don't know"**.
- **No source tested SAP Knowledge Graph, the HANA Cloud knowledge graph engine, or Joule on SAP data.** Any SAP-specific accuracy claim needs SAP evidence or our own pilot measurement.
- Two different things share the name: the HANA Cloud knowledge graph engine (RDF/SPARQL; runs on a single compute node per SAP documentation) and "SAP Knowledge Graph" used by Joule Work and Studio. No opened source links them.
- **Citations and graph paths raise acceptance, not necessarily correctness.** Explanations made users accept AI recommendations whether or not they were correct (Bansal et al.), reduced over-reliance only when they made checking cheap (Vasconcelos et al.), and an audit of generative search engines found only 74.5% of citations supported their sentence. No source measured trust effects of graph paths specifically. So design for **cheap verification** (one click to the source record, a short path, a number the user can recompute) and sample-audit citation correctness.
- A graph built on bad master data produces confident, wrong paths. Data-quality dashboards must ship with it.

**Design hypothesis: a governed semantic layer (business glossary mapped to SAP objects) is the lowest-cost way to get most of the graph's benefit.** The only enterprise-data result found (16% to 54%, above) is a semantic-layer setting, not a multi-hop traversal one, which suggests the mechanism that matters may be *shared, governed meaning* rather than graph traversal as such. This is an inference from one vendor-authored preprint, so treat it as something to test. Practical MVP, before any multi-domain ontology:
- **Glossary as data:** 50 to 150 core business terms for the pilot domain (`Metric`, `Dimension`, `BusinessObject`, `Synonym`), each mapped to a source CDS view or BDC data product and an owner.
- **Resolve, then query:** the agent resolves the user's words to glossary terms, asks when ambiguous, calls a governed query tool with resolved identifiers, then narrates. The model never writes free-form SQL against raw tables.
- **Show the interpretation:** "Interpreted *net revenue* as `NetRevenue_Recognised` (owner: Group Controlling), company codes 1010 and 1020, fiscal Q3." It lets the user catch a wrong reading in seconds, which is the cheap-verification property the research says matters.
- **Policy as metadata:** classification and ownership on terms and entities lets the tool layer enforce rules consistently and explain refusals. Enforcement stays in the tools using the user's identity; the graph supplies metadata and never a bypass.
- **Lineage and freshness:** each answer can carry source object, extraction time and owner, and stale data is flagged or refused. This answers an auditor's "where did this number come from?".
- **One vocabulary across assistants:** Joule, SAC and a third-party copilot use identical definitions, so two tools do not give two answers to one question.
- **When not to build it:** single-object, single-system questions already answered by a CDS view or a standard Joule capability; no owner for glossary maintenance; or when data quality, not meaning, is the problem.

**Confidence-building practice: run a visible bake-off.** In the pilot, evaluate the same 100-question set four ways: (a) LLM with direct API tools only, (b) plus vector RAG, (c) plus the governed semantic layer without graph traversal, (d) plus knowledge-graph traversal. Report **accuracy, abstention rate and tokens per answer separately** (an "I don't know" is not a correct answer), per question class. The independent evidence predicts the graph helps on multi-hop dependency, impact and traceability questions and not on single lookups; test that prediction on the client's data, keep the graph where it wins and drop it where it doesn't. A client that watched you test your own assumption trusts the result more than one that was sold a technique.

## 4. MCP and the tool layer: what it contributes to confidence

**What a standard tool interface gives the client**
- **A single, inspectable catalogue of what the AI can do.** Each tool has a schema, owner, scope and risk tier. The security team reviews a list of tools, not free-form model behaviour.
- **Vendor-neutral exit.** Business capabilities exposed as governed tools can be called by Joule, a client's chosen copilot or another agent platform. This directly reduces lock-in anxiety (see exit plan in `04-multi-ai/multi-ai-patterns.md`).
- **Uniform audit.** Every call is logged at one choke point with user, tool, parameters and result.
- **Separation of read, prepare and execute.** Read tools are open; "prepare" tools return a preview; execution goes through approval.

**What it does not give you for free** (important for credibility with a CISO)
- In the MCP specification (current revision 2026-07-28) **authorization is still optional**; over HTTP it defines an OAuth 2.1 resource-server profile with protected-resource metadata, resource indicators, audience validation, an explicit ban on token passthrough, and (new) issuer validation. So *we* mandate it by standard (`07-sdlc-guide/03-secure-by-design.md` section 4).
- The ecosystem has real security problems, so say so before the client's CISO does: critical vulnerabilities in tooling (CVE-2025-6514 in `mcp-remote`, CVSS 9.6; CVE-2025-49596 in MCP Inspector, CVSS 9.4), demonstrated tool-poisoning and "rug pull" attacks, and a registry study (DSN 2026) that flagged 833 vulnerable servers out of 67,057. No confirmed enterprise data breach through an MCP server was found either way. Hence: approved-server register, pinned and reviewed tool descriptions, no public-registry servers in production.
- SAP's own position is uneven: MCP is documented for developer tooling and for adding servers to Joule Studio agents; Joule Work states MCP and A2A support but is in phased rollout; MCP access policies in Joule Work Desktop are "disabled by default"; a TechEd 2026 sample for an Integration Suite MCP gateway demonstrates principal propagation and human approval; A2A is not documented on help.sap.com. **Whether SAP's MCP servers implement the MCP OAuth profile was not verified.** Do not promise MCP-based production capability until confirmed for the client's edition and tested [VERIFY V6]. The design works with Studio actions or API Management as a fallback.

**Confidence-building practice:** publish a **Tool Register** to the client (tool, owner, data touched, autonomy level, approval, rate limit, last security review). Walk the CISO through a live denied-access demonstration for each persona.

## 5. Other AI concepts that make confidence demonstrable

| Concept | Property | What the client sees |
|---|---|---|
| **Evaluation as acceptance testing** | Verifiable | A scorecard on a held-out question set built jointly with the client's process owners, re-run on every change; failures visible, not hidden |
| **Citations with automatic verification** | Verifiable | Every factual claim links to a source object; a checker confirms the cited record exists and supports the claim (the Deloitte refund case is a failure of exactly this check). Citations reduce but do not eliminate errors (17% to 33% hallucination in the legal-tool study), so measure the residual rate and show it |
| **Deterministic computation for numbers** | Verifiable | Amounts, dates, aggregates come from tools; the model narrates (pattern P8) |
| **Abstention and uncertainty display** | Verifiable | "I'm not sure, here is the report" is a designed, measured behaviour; ranges and data freshness shown |
| **Shadow mode** | Valuable, Contained | AI runs alongside humans for N weeks with its output hidden or compared; agreement rate and disagreement analysis shown before anything goes live |
| **Champion/challenger** | Valuable | New model or prompt must beat the incumbent on the held-out set before promotion |
| **Staged autonomy (trust ladder)** | Controlled, Contained | A0 inform → A1 suggest → A2 act with approval → A3 bounded autonomy; promotion criteria written in advance (`01-sdlc-playbook.md`) |
| **Meaningful human oversight** | Controlled | Approval screens show resolved entities and the diff; approval rate and override reasons tracked to detect rubber-stamping. EU AI Act Art. 14 explicitly names automation bias; the one lab study found explanations cut over-reliance only when they made checking cheaper, so design the approval screen for fast verification, not for explanation volume. KPMG reports 66% of surveyed workers rely on AI output without evaluating accuracy (respondent base not stated on the page read) |
| **Guardrails and red-teaming** | Controlled | Published injection/leakage test results; remediation log |
| **Observability ("flight recorder")** | Transparent | Every interaction traceable end to end; client can replay an incident |
| **Unit-economics dashboard** | Valuable | Cost per interaction, per accepted answer, per completed transaction vs the manual alternative |
| **Model routing and small/open models for routine steps** | Valuable | Gartner (Nov 2026, via The Register, medium confidence) says routine steps can run on open-weight models at a fraction of the cost; show the routing policy and its measured quality |
| **AI inventory, risk tiers, governance board** | Transparent | One register of scenarios, owners, tiers, models, data; aligns to NIST AI RMF and ISO/IEC 42001 |
| **Kill switch and incident drills** | Contained | A rehearsed shutdown, run in front of the client |

### 5a. SAP's own trust artefacts: cite with attribution, request the paper

Source: `_research/forecasting-kg-mcp-evidence.md` section 3.4 (help.sap.com excerpts and SAP News Center, read 2026-11-23). These are **vendor statements**. Say "SAP states...", ask the account team for the underlying document, and do not extend the wording.

| Artefact | What SAP states (verbatim scope) | What to request / how to use |
|---|---|---|
| ISO/IEC 42001 | "ISO/IEC 42001 certification for AI governance has been achieved, covering Joule, SAP AI Core, and SAP AI Launchpad" (one help.sap.com excerpt) | Certificate, certifying body and scope statement; the certificate was not opened |
| Training use | "Your employee and customer data is never shared with third parties to train AI models" (SuccessFactors Responsible AI page); SAP publicly says it does not share customer data to train or improve LLMs | Contract/DPA clause and each model provider's terms [VERIFY V5] |
| Prompt routing | Joule Work desktop "routes all AI prompts through SAP AI Core" | Data-flow diagram for the client's edition |
| Guardrails | AI Core offers content filtering, data masking and document grounding, but the extra modules are on the **extended** plan only; masking entity coverage is limited by profile (test non-English, non-US data) | Confirm plan and cost [V9, V10] |
| Authorization and audit | Joule Work agents "respect established authorizations" and keep audit trails; agents are "first-class principals" (phased rollout) | Prove with the persona test in the client's tenant; do not rely on the statement |
| Human approval | Data Management Assistant executes corrections "only after human approval"; the IBP Exception Management Agent proposes mitigations | Confirm GA status per assistant (several were "planned for Q4 2026") |
| Scoping disclaimers | AI Launchpad: SAP not responsible for model output quality; Batch Release Hub: "Joule is not a decision-making system for GxP-critical actions" | Use to set tier-3 scope honestly |

A client's CISO will notice if you present these as proof. Present them as *claims to be verified in your tenant*, then show the verification.

## 6. Commercial confidence (risk transfer, not just risk description)

Clients' cost concern is partly about who bears the risk. Structures that make risk visible and shared:
1. **Fixed-fee readiness phase** that ends with a signed baseline and a go/no-go the client can walk away from.
2. **Tranche funding with kill criteria** agreed up front (adoption, accepted-answer rate, KPI delta), so stopping is an expected outcome, not a failure.
3. **Benefits owned by Finance**: classification into cashable, redeployable (named work), soft, risk avoided; only the first two in the base case.
4. **Fee-at-risk or outcome-linked component** tied to the agreed KPI delta against a control group where feasible. The research found only a vendor price page (Intercom prices its support agent per resolved conversation) and **no independent study** of whether outcome-based pricing improves ROI or project success. Deloitte 2026 also finds only 44% of firms track per-unit inference cost, so many buyers cannot yet price outcomes well. Treat it as a design option to negotiate carefully, not a proven norm.
5. **Cost caps and budget alerts** on consumption, with monthly unit-cost review.

## 7. Who needs which proof

| Stakeholder | Core question | Show them |
|---|---|---|
| CFO | "Where is the money?" | Baseline, benefit register classification, discounted model, sensitivity, kill criteria (`08-value-cases/`) |
| CISO | "Can it be abused?" | Identity-chain proof by persona, threat register, red-team results, tool register, kill-switch drill |
| Process owner (COO, controller, supply-chain head) | "Will my team trust it and will it work on our data?" | Shadow-mode agreement rates on their cases, scorecard by question class, planner override analysis |
| CIO / architecture | "Does it fit, will it lock us in?" | ADRs, reference architecture, tool catalogue and exit plan, clean-core compliance, run-cost model |
| Data protection officer / legal | "Is it lawful?" | DPIA, data-flow map, model/provider terms, AI Act classification, retention |
| Internal audit | "Can I test it?" | Audit-log sample, approval evidence, change records, inventory |
| Employees / works council | "Is this about replacing me?" | Role-based training, clear statement of what AI will and will not do, champions network, consultation record |
| Board | "Is the risk controlled?" | One-page confidence scorecard (section 8) quarterly |

## 8. The Client Confidence Scorecard (one page, updated at every gate)

| Property | Metric | Threshold (set with client) | Current |
|---|---|---|---|
| Verifiable | Accepted-answer rate on held-out set; citation validity rate; variance across 3 runs | e.g. ≥ 90%; ≥ 95% | |
| Verifiable | Abstention correctness (refuses when it should) | e.g. 100% on must-refuse list | |
| Controlled | Cross-role leakage in tests | 0 | |
| Controlled | Share of write actions with approval; approval override rate | 100%; tracked | |
| Contained | Time to kill switch; last drill date | < 5 min; < 90 days | |
| Contained | Open Sev1/Sev2 incidents | 0 | |
| Valuable | KPI delta vs baseline (and vs control) | per charter | |
| Valuable | Cost per accepted answer / per transaction vs manual | below manual | |
| Valuable | Weekly active users / invited | e.g. ≥ 60% | |
| Transparent | Scenarios in AI inventory with owner and tier | 100% | |
| Transparent | Models on approved register | 100% | |

## 9. Proof calendar for the first six months

| When | Evidence delivered |
|---|---|
| Week 4 | Signed baseline; readiness RAG; threat model; kill criteria |
| Week 6 | Identity-chain proof by persona (live denied-access demo) |
| Week 10 | First evaluation scorecard on the client's own questions; graph vs no-graph bake-off if used |
| Week 14 | Shadow-mode results: agreement rate, disagreement review with process owners |
| Week 16 | Security gate: red-team results, tool register, kill-switch drill |
| Week 20 to 24 | Pilot results against control group; unit economics; go/no-go |
| Quarterly after | Scorecard to the board; retire or expand decisions |

## 10. Anti-patterns that destroy confidence
- **Demo-only proof** on curated data with no measured accuracy.
- **Benefit claims from vendor material** presented as the client's expected results.
- **Hiding failures.** The scorecard shows failing question classes; the fix log is shared.
- **Autonomy before evidence** (skipping shadow mode or A2).
- **Headcount-reduction framing**, then reversing (Klarna, CBA).
- **Unverified citations or numbers** in client deliverables, including ours; run the same checks on our own documents.
- **Overselling unconfirmed SAP capabilities** (MCP, graph engine, Joule Studio editions) before the VERIFY register is cleared.
- **Technique worship:** adding a knowledge graph or agents because they are fashionable, with no measurable property improved.

## 11. Decision guide: which concept for which confidence gap

| If the client's gap is... | Lead with | Then |
|---|---|---|
| Wrong answers | Evaluation scorecard, citations, deterministic tools | Knowledge graph for multi-hop questions (after bake-off) |
| Data exposure | Identity-chain proof, tool register, classification-based model routing | Red-team results |
| Runaway cost | Unit economics, quotas, model routing | Tranche funding |
| Lock-in | Tool layer (MCP or equivalent), approved-model register, exit plan | Open formats for graph and prompts |
| Accountability and audit | Observability, AI inventory, approval evidence | ISO/IEC 42001 alignment |
| Low adoption | Shadow mode with the actual users, champions, in-flow feedback | Workflow redesign |
| Doubts about value | Baseline and control group, kill criteria | Outcome-linked fees |

For how these choices play out per scenario (GL queries, variance explanation, blocked invoices, contracts, HR self-service, developer tooling), with a worked example, a tool register entry, a 30-minute demo and a talk track, see `03-scenario-playbook.md`.
