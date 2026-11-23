# Secure-by-Design Addendum for SAP AI Solutions

Extends `02-reference/security-identity-reference.md`. That file remains the baseline; this addendum adds the AI-agent threat model, identity-chain design, tool-server (MCP) controls, secure SDLC and incident playbooks.

## 1. Framework mapping

| Framework | Use |
|---|---|
| OWASP Top 10 for LLM Applications (2025) | Threat checklist for every scenario (table below) |
| NIST AI RMF 1.0 (Govern, Map, Measure, Manage) | Maps to governance doc and lifecycle gates |
| ISO/IEC 42001 (AI management system) | Certifiable management-system option for clients that need it |
| MITRE ATLAS | Adversary technique vocabulary for red-team plans |
| SAP security guidelines for BTP / S/4 | Platform hardening **[VERIFY current guide versions]** |

| OWASP LLM risk | SAP-specific exposure | Control (where) |
|---|---|---|
| LLM01 Prompt injection | Vendor emails, invoice PDFs, ticket text, Teams messages processed by agents | Section 2 |
| LLM02 Sensitive information disclosure | Over-broad roles; PII in prompts and logs | Sections 3, 6, 8 |
| LLM03 Supply chain | Third-party models, MCP servers, libraries, prompt packs | Sections 4, 7 |
| LLM04 Data/model poisoning | Unapproved documents indexed; fine-tune data | Section 6 |
| LLM05 Improper output handling | Model output into OData `$filter`, SQL, URLs, HTML | Section 2 |
| LLM06 Excessive agency | Agent with write scope to payments or master data | Sections 2, 3 |
| LLM07 System prompt leakage | Secrets or logic placed in prompts | Engineering standards section 3 |
| LLM08 Vector/embedding weaknesses | Missing per-chunk ACL; cross-tenant retrieval | Section 6 |
| LLM09 Misinformation | Wrong numbers, wrong entity | Deterministic calculation, citations, evaluation |
| LLM10 Unbounded consumption | Looping agents, abusive users | Quotas, step limits, alerts |

## 2. Design rules that prevent the worst failures

1. **Rule of two.** An agent session must not combine all three: (a) access to private/sensitive data, (b) exposure to untrusted content (email, documents, web, user-uploaded files), and (c) ability to change state or communicate externally. If a design needs all three, insert a human approval step or split into separate agents with a sanitising hand-off.
2. **Authorization lives in tools, never in prompts.** Tools check the caller's rights on every call. "The model was told not to" is not a control.
3. **Treat retrieved and tool-returned content as untrusted data.** Delimit it, never let it change tool allow-lists or approval requirements, and strip or flag instruction-like text from documents where practical. Detection is a supplement, not the control.
4. **Sensitive actions always require approval (A2) in v1:** vendor bank-detail changes, payment release, master-data changes, user/role changes, external communications, HR decisions. Show a diff of what changes; approver cannot be the requesting user where SoD requires it.
5. **Validate model output before use.** Schema validation; allow-list for enumerations; parameterised queries; no model-built OData filters or SQL passed through raw; encode for the sink; resolve IDs against the system, not the model's memory.
6. **Hard limits in code:** max records per call, amount ceilings, max agent steps, max tokens per run, allowed destinations (egress allow-list) for any tool that makes network calls (prevents SSRF and exfiltration).
7. **Fail closed.** If identity, authorization or validation is uncertain, refuse and log.
8. **No secrets in model context.** Credentials remain in Credential Store/Destinations; tools hold them, the model never sees them.

## 3. Identity chain and agent identity

**Principal propagation must be proven at every hop**, not assumed:

```
User (IdP) → IAS → Joule → Studio skill/agent → (token exchange) → API Mgmt / Integration Suite
          → Cloud Connector (on-prem) → S/4 / ABAP (user mapped, authorizations checked)
```

| Decision | Standard |
|---|---|
| User context | Default: act on behalf of the user via token exchange/principal propagation; backend authorizations decide |
| Technical user | Only by ADR: scoped role, owner named, secret in Credential Store, rotation ≤ 90 days, usage logged and reviewed monthly; never for write actions on behalf of ordinary users unless the approval step captures the human identity |
| Agent identity | Each agent has its own non-human identity for audit; its permissions are the intersection of the user's rights and the agent's scope |
| SoD | Agent actions included in SoD analysis (Cloud IAG/GRC). Maker-checker: the agent proposes, a different human approves where SoD requires |
| Access reviews | Agents, service identities, destinations, and OAuth clients included in periodic access recertification |
| Proof test (Sprint 1) | Run the same request as five personas (executive, line manager, AP clerk, contractor, user with no access) at every hop; verify backend logs show the *user*, not a service account |
| Session/token | Short token lifetime; no token passthrough to downstream systems that did not issue the audience; revoke on logoff/offboarding |

## 4. Tool servers and MCP (if used) **[VERIFY SAP support status]**

| Threat | Control |
|---|---|
| Unauthenticated or weakly authenticated tool server | OAuth 2.x with audience-bound tokens; mTLS between services; API Management in front |
| **Token passthrough / confused deputy** | Server must not forward the client's token to other APIs; use token exchange scoped to the downstream audience; validate audience on every request |
| Tool description/metadata poisoning | Only allow-listed servers; pin versions and hash tool manifests; review descriptions as code; re-approve on change |
| Over-broad tool scopes | Per-tool scopes; separate read and write servers |
| Third-party/unknown servers | Approved-server register (owner, version, data flows, security review); no public registry servers in production by default |
| Command/SQL injection in tool implementation | Parameterised queries, no shell, input validation |
| Session hijack/replay | Non-guessable session IDs, bind to user, expiry |
| Local servers on developer machines | Not permitted for production data access |
| Logging gaps | Log every tool invocation with user, params (masked), result |

Spec and incident context (researched 2026-11-23, `_research/forecasting-kg-mcp-evidence.md`): the current MCP revision (2026-07-28) keeps authorization optional and defines an OAuth 2.1 profile (protected-resource metadata, resource indicators, audience validation, no token passthrough, issuer validation); tool descriptions must be treated as untrusted unless from a trusted server. Documented problems include critical tooling CVEs (CVE-2025-6514, CVSS 9.6; CVE-2025-49596, CVSS 9.4), tool-poisoning and rug-pull demonstrations, and a registry study flagging 833 vulnerable servers of 67,057. Whether SAP's MCP servers implement the MCP OAuth profile is unverified (register V6).

Agent-to-agent protocols: treat as untrusted network boundaries; same controls; do not make production commitments before SAP confirms support.

## 5. Model and provider controls
- Approved-model register: provider, model, version, region, data terms, retention, security review date, retirement date.
- Contractual confirmations in writing: no training on client data, retention limits (zero-retention where available), sub-processor list, breach notification, residency. Record the clause reference in the ADR.
- Masking/anonymisation gateway for any external model call (pattern P12); data classification determines allowed models (e.g. Restricted data → SAP-hosted or private deployment only).
- Model change = change request + evaluation re-run + security check on terms.

| Data class | Allowed model routing (example policy; tune per client) |
|---|---|
| Public | Any approved model |
| Internal | Approved models in approved regions |
| Confidential (financial, contracts) | SAP-governed access with residency-compliant deployment; masking |
| Restricted (HR comp, health, bank data, trade secrets) | Private/sovereign deployment or no LLM; deterministic report instead |

## 6. Knowledge base and vector store
- Per-chunk ACL metadata (source document ACL, classification, owner) and **query-time filtering using the caller's identity**; test with persona suite.
- Source approval workflow and versioning; index only approved, owned sources; record source hash.
- Re-index on document change/deletion; deletion propagates to chunks within the agreed window (supports erasure requests).
- Poisoning controls: reject documents from uncontrolled upload paths; scan for instruction-like content; alert on large or sudden corpus changes.
- Separate indexes per classification and per tenant; encrypt at rest; restrict admin access.
- Embeddings can leak source text; treat the vector index as sensitive as the source.

## 7. Secure SDLC controls (map to playbook gates)
| Phase | Control |
|---|---|
| Requirements | Abuse cases written beside use cases; data classification set |
| Design | Threat model workshop (STRIDE + OWASP LLM), identity chain design, ADRs for exceptions |
| Build | Secure coding standard, secret scanning, dependency and licence scanning, SBOM, signed builds, protected branches, reviewer separation |
| Test | Authorization suite, injection/exfiltration suite (direct and indirect), tool abuse tests, cost-abuse tests; independent tester for tier 3 |
| Release | Security sign-off, config review (destinations, scopes, role collections), kill switch test |
| Operate | Log monitoring, anomaly alerts, quarterly access recertification, patching, periodic red-team (at least annual; after major change for tier 3) |
| Retire | Credential/destination removal, log retention and purge |

**Red-team scope (minimum prompt set):** direct injection to override rules; indirect injection planted in an invoice PDF/email/ticket/document; cross-user data requests; role escalation phrasing; multi-turn extraction; tool parameter tampering; output-sink injection; denial-of-wallet loops; system-prompt extraction; encoded/multilingual evasion.

## 8. Logging, privacy, incidents

**Logging and privacy**
- Define retention for prompts, responses, tool traces and vector logs; default shortest period that serves audit/quality (propose 90 days detailed, 12 months aggregated; client policy overrides).
- Logs are classified at the highest level of data they may contain; access restricted; encrypted; export controlled.
- Support DSAR/erasure: be able to locate and remove a data subject's content from logs, feedback stores and indexes, or document why not feasible.
- DPIA for scenarios processing personal data, especially HR; consult employee representatives where required.

**Incident playbooks (each has owner, severity, containment, evidence, notification, fix)**
| Incident | Immediate containment |
|---|---|
| Suspected prompt injection with action taken | Disable skill via flag; freeze pending approvals; preserve traces; review affected transactions |
| Cross-role data exposure | Kill switch; identify scope from logs; notify privacy officer; fix authorization; add test |
| Wrong financial/master-data action | Reverse via compensating transaction; halt A2/A3 for that tool; root-cause |
| Runaway cost | Quota cut-off; identify loop; patch step limits |
| Model/provider regression or outage | Switch to fallback model/deep link; re-run eval before returning |
| Compromised credential/tool server | Rotate secrets; revoke tokens; block server; review logs back to last known good |
Run a tabletop drill at least once before go-live and annually.

## 9. Regulatory notes (verify before relying) **[VERIFY]**
- **EU AI Act:** obligations phase in over 2025 to 2027. HR/employment, credit-related, and some safety uses are high-risk categories; transparency duties apply to AI interacting with people. Confirm current application dates, including any adopted postponement of high-risk obligations, with legal counsel before fixing the roadmap.
- **GDPR:** lawful basis, DPIA, automated decision-making limits (Art. 22), data subject rights, international transfer mechanism for any non-EU model processing.
- **SOX/financial controls:** change control evidence, SoD for AI-initiated postings, retention of approvals.
- **Sector:** DORA, NIS2, HIPAA, GxP, PCI per client.
- Maintain an AI system inventory (scenario, tier, model, data, owner) as the compliance backbone.

## 10. Security go-live checklist (extends baseline gate)
- [ ] Threat register reviewed; no open critical items
- [ ] Rule of two satisfied or compensated by approval
- [ ] Identity-chain proof test passed for all personas; technical users ADR-approved
- [ ] All write tools: approval, idempotency, limits, audit verified
- [ ] Red-team suite executed; high findings fixed
- [ ] Vector ACL tests passed; sources approved
- [ ] Model/provider terms recorded; masking verified for external calls
- [ ] Secrets in Credential Store; scanning clean; SBOM stored
- [ ] Quotas, step limits, cost alerts active
- [ ] Logging, retention, access controls configured
- [ ] Kill switch tested; incident playbooks and on-call assigned; tabletop done
- [ ] DPIA / AI Act classification recorded; AI inventory updated
