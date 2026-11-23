# Security, Identity and Compliance Reference

## 1. Principles
1. **Least privilege:** AI acts with the user's own authorizations, never a super-user, unless a documented technical user with scoped permissions is approved.
2. **Data minimisation:** send only the fields the task needs to a model.
3. **Transparency:** show sources, label AI-generated content.
4. **Auditability:** log who asked what, which data was accessed, which action executed.
5. **Human accountability:** irreversible or financial actions require approval.

## 2. Identity flow
- Corporate IdP (Entra ID/Okta) → Cloud Identity Services (IAS) → SAP apps and BTP.
- Provisioning with IPS; map groups to roles/role collections.
- Principal propagation from Joule to backend APIs (user context, not shared credentials).
- Review: service-to-service communication uses OAuth2/mTLS with rotated secrets in Credential Store.

## 3. Authorization readiness checklist
- [ ] Role catalog reviewed; no wildcard authorizations for general users
- [ ] SoD rules current (Cloud IAG or GRC)
- [ ] Sensitive objects (HR comp, bank data, pricing) have explicit restrictions
- [ ] Test personas created: executive, line manager, AP clerk, external contractor
- [ ] Low-privilege user test proves no leakage via Joule answers
- [ ] Document-level ACLs mirrored in vector index metadata

## 4. Data protection
| Topic | Control |
|---|---|
| PII/sensitive fields | Masking/anonymisation before external model calls; allow-lists |
| Data residency | Choose BTP region and model deployment region accordingly **[VERIFY]** |
| Retention | Define prompt/response log retention; purge schedule |
| Training use | Confirm in writing that client data is not used to train shared models **[VERIFY with SAP and each model provider]** |
| Encryption | In transit TLS; at rest provider-managed or customer-managed keys |
| Secrets | Credential Store; never in prompts or code |

## 5. Threat model (AI-specific)

| Threat | Example | Mitigation |
|---|---|---|
| Prompt injection | Malicious text in a vendor email makes agent change bank details | Treat retrieved content as untrusted; separate instructions from data; require approval for sensitive actions; output validation |
| Data exfiltration | User tricks assistant into revealing other users' data | Enforce authorization in tools, not in prompts |
| Over-privileged agent | Agent with broad API scope | Scoped tokens, per-tool permissions |
| Hallucinated actions | Wrong object/ID used | Confirm screens with resolved entities, idempotent APIs |
| Model supply chain | Unvetted external model | Approved-model list, vendor security review |
| Cost abuse | Looping agent burns tokens | Step limits, quotas, alerts |
| Poisoned knowledge base | Wrong policy doc indexed | Source approval workflow, versioning |

## 6. Compliance mapping (starting list, adapt per client)
| Regulation/standard | Relevance |
|---|---|
| GDPR / local privacy law | Personal data in prompts, DSAR, DPIA |
| EU AI Act | Risk classification per use case (HR use cases may be high-risk) |
| SOX / internal controls | Financial postings, change control, evidence |
| ISO 27001 / SOC 2 | Information security controls |
| Industry (HIPAA, GxP, PCI, DORA, NIS2) | Per sector |

## 7. Logging and monitoring
- Capture: user, timestamp, scenario/skill, tools called, data objects touched, model used, token count, outcome.
- Alerts: anomaly in volume, repeated denied-access attempts, spike in cost.
- Retain per policy; protect logs because they may contain sensitive content.

## 8. Go-live security gate
1. Threat model reviewed
2. Pen-test or red-team prompts executed (injection, jailbreak, leakage)
3. Authorization tests passed
4. DPIA/risk assessment signed
5. Incident response runbook for AI issues
6. Kill switch to disable a skill/agent quickly
