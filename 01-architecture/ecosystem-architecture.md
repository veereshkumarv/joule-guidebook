# Ecosystem Architecture: Joule in the SAP and BTP Landscape

Diagrams use Mermaid (renders in GitHub, GitLab, VS Code, Confluence plugins). Product names reflect authoring date **[VERIFY]**.

## 1. Big picture: where Joule sits

```mermaid
flowchart TB
  subgraph Channels["User channels"]
    FLP["Fiori Launchpad / SAP Start"]
    WZ["SAP Build Work Zone"]
    MOB["Mobile apps"]
    COLLAB["Collaboration: Teams / Slack integration"]
  end

  subgraph JouleLayer["Joule (AI copilot and agents)"]
    JU["Joule UI / conversation"]
    JO["Orchestration: intent, skill routing, agent coordination"]
    JS["Joule Studio: custom skills and agents"]
  end

  subgraph Apps["SAP applications (embedded Joule scenarios)"]
    S4["S/4HANA Cloud / on-prem"]
    SF["SuccessFactors"]
    ARI["Ariba"]
    CX["Concur"]
    IBP["Integrated Business Planning"]
    SAC["SAP Analytics Cloud"]
    FSC["Fieldglass / C4C / CX"]
  end

  subgraph BTP["SAP Business Technology Platform"]
    GAH["Generative AI Hub (AI Core)"]
    AIL["AI Launchpad"]
    HVEC["HANA Cloud + Vector Engine"]
    INT["Integration Suite / API Mgmt"]
    EM["Event Mesh / Advanced Event Mesh"]
    BUILD["SAP Build: Apps, Process Automation, Code"]
    CAP["CAP on Cloud Foundry / Kyma"]
    DIE["Document AI / Doc Information Extraction"]
    WF["Workflow / Task Center"]
    OBS["Cloud ALM, Audit Log, Alert Notification"]
  end

  subgraph Data["Data foundation"]
    BDC["SAP Business Data Cloud / Datasphere"]
    KG["Knowledge graph / semantic layer"]
    DOCS["Document stores (SharePoint, S3, DMS)"]
  end

  subgraph Identity["Trust and identity"]
    IAS["Cloud Identity Services (IAS/IPS)"]
    IDP["Corporate IdP (Entra ID, Okta)"]
  end

  subgraph External["Non-SAP AI and systems"]
    LLM["External LLMs: Azure OpenAI, Bedrock, Vertex, Mistral, Anthropic"]
    NSAP["Non-SAP apps: Salesforce, ServiceNow, Workday"]
    MCP["MCP / agent-to-agent endpoints"]
  end

  Channels --> JU --> JO
  JO --> Apps
  JO --> JS
  JS --> BTP
  Apps --> BTP
  GAH --> LLM
  GAH --> HVEC
  JS --> INT --> NSAP
  JS --> MCP
  BTP --> Data
  Apps --> Data
  Identity -.SSO and propagation.-> JouleLayer
  Identity -.-> Apps
  Identity -.-> BTP
  IDP --> IAS
```

**Reading guide:** users enter through a channel; Joule interprets intent and routes to either a standard embedded scenario in an SAP application or a custom skill/agent built in Joule Studio. Custom logic calls BTP services (Generative AI Hub for model access, HANA Vector Engine for grounding, Integration Suite for APIs, Event Mesh for triggers). Identity is propagated end to end so data access follows the user's own authorizations.

## 2. Request flow: a grounded question with a governed action

```mermaid
sequenceDiagram
  actor U as User
  participant J as Joule
  participant ID as Identity (IAS)
  participant SK as Skill/Agent (Joule Studio)
  participant AI as Generative AI Hub
  participant V as HANA Vector Engine
  participant S4 as S/4HANA API
  participant WF as Approval workflow

  U->>J: "Why is invoice 5100234 blocked?"
  J->>ID: validate token, propagate user context
  J->>SK: route intent
  SK->>S4: read invoice + block reason (user's authorizations)
  SK->>V: retrieve relevant policy snippets
  SK->>AI: prompt with data + policy (masked fields)
  AI-->>SK: explanation + suggested action
  SK-->>J: answer with sources
  J-->>U: explanation, proposed "release block" action
  U->>J: confirm
  J->>WF: request approval (human in loop)
  WF->>S4: execute release after approval
  S4-->>J: result, logged in audit
```

## 3. Landscape variants

### 3.1 Public cloud (RISE with SAP / S/4HANA Cloud Public)
- Joule embedded scenarios available as delivered by SAP release **[VERIFY per release]**.
- Extensions via side-by-side BTP only (clean core), key-user extensibility for light changes.
- Identity: IAS with corporate IdP federation.

### 3.2 Private cloud / on-premise S/4HANA
```mermaid
flowchart LR
  OP["S/4HANA on-prem / private edition"] --- CC["Cloud Connector"]
  CC --- BTPX["BTP subaccount"]
  BTPX --- J2["Joule + Studio"]
  BTPX --- GAH2["Generative AI Hub"]
  OP --- SLT["SLT / Data replication"] --- BDC2["BDC / Datasphere"]
  BDC2 --> GAH2
```
- Expose APIs via OData/REST through Cloud Connector and API Management.
- Some Joule scenarios may require specific releases or add-ons **[VERIFY]**.
- Prefer event-based change feed or replication for analytical questions; use live APIs for transactional context.

### 3.3 Multi-system / heterogeneous landscape
```mermaid
flowchart TB
  J3["Joule"] --> ORCH["Orchestrator agent"]
  ORCH --> A1["S/4HANA agent"]
  ORCH --> A2["Ariba agent"]
  ORCH --> A3["SuccessFactors agent"]
  ORCH --> A4["Non-SAP agent (ServiceNow / Salesforce) via API or MCP"]
  A1 & A2 & A3 & A4 --> DATA["Shared semantic layer (BDC)"]
```

## 4. Layered view (for architecture decision records)

| Layer | Components | Decision owner |
|---|---|---|
| Experience | Joule UI, Work Zone, Teams/Slack | Product owner |
| Orchestration | Joule orchestration, Joule Studio agents, workflows | Solution architect |
| Intelligence | Generative AI Hub models, SAP foundation models, external LLMs, embeddings | AI architect |
| Knowledge | HANA Vector, BDC semantic models, document grounding | Data architect |
| Integration | Integration Suite, API Mgmt, Event Mesh, Cloud Connector | Integration architect |
| Trust | IAS/IPS, authorization, audit log, DPI, key management | Security architect |
| Operations | Cloud ALM, AI Launchpad, alerting, cost monitoring | Platform lead |

## 5. Reference architecture A: "Standard-first" (lowest effort)
Use embedded Joule in S/4HANA, SuccessFactors, Ariba, Concur. Add Work Zone as one entry point. Only configuration, enablement and training.
**Use when:** client wants fast value and scenario coverage matches pain points.

## 6. Reference architecture B: "Extended" (custom skills/agents)
A plus Joule Studio skills/agents calling S/4 APIs, Integration Suite flows, Workflow approvals, Generative AI Hub for text tasks, HANA Vector for document grounding.
**Use when:** process-specific automation not covered by standard.

## 7. Reference architecture C: "Data-driven" (analytics and cross-system)
B plus Business Data Cloud/Datasphere for harmonised data, SAC for planning, predictive/foundation models for forecasting or classification.
**Use when:** questions span SAP and non-SAP data, or need history and trends.

## 8. Reference architecture D: "Multi-AI hybrid"
C plus external LLMs through Generative AI Hub, MCP/agent interoperability with third-party agents. See `04-multi-ai/multi-ai-patterns.md`.
**Use when:** client has an enterprise AI platform standard or needs a specific model capability or residency.

## 9. Environment topology

| Env | Purpose | Notes |
|---|---|---|
| Sandbox/Trial | Demos, exploration | No client data |
| Dev | Skill/agent building | Synthetic or masked data |
| QA/Test | UAT, evaluation sets | Production-like authorizations |
| Prod | Live | Change control, monitoring, budgets/alerts |

Transport with Cloud Transport Management; keep prompts, skill definitions and evaluation sets in source control.

## 10. Non-functional targets (starting points, tune per client)

| Aspect | Starting target |
|---|---|
| Answer latency (simple Q&A) | < 5 to 8 s p90 |
| Availability | Aligned to underlying SAP cloud SLAs |
| Answer quality | ≥ 90% accepted on curated test set before go-live |
| Security | 0 cross-role data leakage in test |
| Cost | Monthly consumption alert at 80% of budget |
