# SAP Products and BTP Services Catalogue for AI Solutions

Quick "when to use" reference. **[VERIFY]** names, availability, pricing model on SAP Discovery Center before quoting.

## 1. AI and intelligence

| Service/Product | What it does | Use for | Pricing basis (typical) |
|---|---|---|---|
| Joule | Conversational copilot + agents across SAP apps | End-user assistant, process automation | Included/entitled per solution or AI units **[VERIFY]** |
| Joule Studio | Build custom skills and agents | Extend beyond standard scenarios | **[VERIFY]** |
| SAP AI Core | Run and serve ML/GenAI workloads | Custom models, orchestration | Capacity/consumption |
| Generative AI Hub | Unified access to multiple LLMs, prompt tools, orchestration, guardrails | Model choice, governance | Token/consumption |
| SAP AI Launchpad | Manage AI lifecycle, deployments, monitoring | MLOps | With AI Core |
| SAP HANA Cloud (Vector Engine) | Vector store, similarity search | RAG, semantic search | Capacity units |
| SAP foundation models (e.g. tabular/relational) | Prediction on business tables | Classification/forecast w/o heavy ML | **[VERIFY]** |
| Document Information Extraction | Extract fields from documents | Invoice/PO capture | Per document |
| Intelligent Scenario Lifecycle Mgmt | Manage embedded ML in S/4 | Predictive scenarios | Included in S/4 |
| Data Attribute Recommendation, Business Entity Recognition | Classification/entity services | Categorisation | Per call **[VERIFY availability]** |

## 2. Data

| Service | Use for |
|---|---|
| SAP Business Data Cloud / Datasphere | Harmonised business data products, semantic layer, cross-system queries |
| SAP Analytics Cloud | Planning, dashboards, predictive, Joule on analytics |
| SAP HANA Cloud | Operational/analytical store, graph, spatial, vector |
| SAP Master Data Governance | Data quality for master data feeding AI |
| SAP Information Lifecycle Mgmt, Data Privacy Integration | Retention, privacy requests |
| Knowledge graph / semantic metadata | Business context for LLM accuracy **[VERIFY]** |

## 3. Integration

| Service | Use for |
|---|---|
| SAP Integration Suite (Cloud Integration, API Mgmt, Open Connectors, Integration Advisor) | APIs, iFlows to SAP and non-SAP |
| Event Mesh / Advanced Event Mesh | Event-driven triggers |
| Cloud Connector | Secure on-prem connectivity |
| Destination service | Managed endpoints and credentials |
| SAP Graph | Unified API across SAP data **[VERIFY status]** |

## 4. Development and automation

| Service | Use for |
|---|---|
| SAP Build Apps | Low-code UIs |
| SAP Build Process Automation | Workflows, RPA bots, decisions, forms |
| SAP Build Code / Business Application Studio | Pro-code with AI assist |
| CAP (Cloud Application Programming Model) | Custom services on BTP |
| ABAP Cloud / Steampunk | Clean-core ABAP extension |
| Kyma runtime, Cloud Foundry runtime | Hosting side-by-side apps |
| SAP Build Work Zone | Unified entry point, Joule embedding |
| Task Center | Unified inbox across apps |

## 5. Security, identity, operations

| Service | Use for |
|---|---|
| Cloud Identity Services (IAS/IPS) | SSO, federation, user provisioning |
| SAP Cloud Identity Access Governance | SoD, access analysis |
| SAP Enterprise Threat Detection / Cloud security services **[VERIFY]** | Threat monitoring |
| Audit Log service | Audit trails |
| Credential Store, Key management | Secrets, encryption keys |
| Cloud ALM | Operations, monitoring, project mgmt |
| Alert Notification, Application Logging, Cloud Logging | Observability |
| Cloud Transport Management | Promotion across environments |
| Data Custodian / key control **[VERIFY]** | Sovereign controls |

## 6. SAP applications with Joule scenarios (examples; verify per release)

S/4HANA Cloud (Finance, Procurement, Sales, Manufacturing, Supply Chain, Asset Mgmt), SuccessFactors, Ariba, Concur, Fieldglass, IBP, SAP Customer Experience, SAP Build Work Zone, SAP Analytics Cloud, SAP Signavio, SAP LeanIX, SAP Datasphere/BDC, SAP Cloud ALM, SAP Business Network.

## 7. Selection guide: which component for which need

| Need | First choice | Alternative |
|---|---|---|
| Assistant in an SAP app | Embedded Joule | Joule Studio skill |
| Automate multi-step process | Joule agent + Build Process Automation | CAP service + workflow |
| Summarise/draft text | Generative AI Hub (chat model) | Joule standard |
| Search internal docs | HANA Vector + Gen AI Hub | Third-party search via API |
| Extract from documents | Document Information Extraction | LLM vision extraction |
| Forecast/classify | SAP foundation model / AI Core ML | SAC predictive |
| Cross-system analytics | BDC/Datasphere | Direct APIs |
| Non-SAP system action | Integration Suite + Studio action | MCP / agent protocol |
| Developer speed | Build Code / Joule for developers | Third-party code assistants (policy permitting) |
