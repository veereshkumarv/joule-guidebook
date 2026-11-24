# Research note: SAP HANA Cloud Knowledge Graph, SAP-sourced evidence

**Compiled:** 2026-11-24. **Purpose:** ground chapter `11-knowledge-graph/` in SAP's own material.
**Handling:** Source 2 is a partner-enablement portal that required a login (401 without it). Treat as **SAP partner material: paraphrase, do not redistribute verbatim**; the PDFs in this folder are for internal reading only. The workshop PDF also contains workshop user IDs and a system URL placeholder; none are reproduced here and none should be copied into client documents.

## Sources

| # | Source | Version/date | Evidence tier |
|---|---|---|---|
| 1 | SAP Help Portal: *SAP HANA Cloud, SAP HANA Database SPARQL Reference Guide* (landing page; PDF printout of 3 pages, `SAP HANA Cloud, SAP HANA Database SPARQL Reference Guide _ SAP Help Portal.pdf`) | Guide version "QRC 3/2026", retrieved 2026-11-24 | Vendor documentation (authoritative for capability and restrictions; landing page only, not the function reference pages) |
| 2 | *SAP HANA Cloud Knowledge Graph: Hands-On Workshop*, kg-partner-enablement portal (47-page PDF, `SAP HANA Cloud Knowledge Graph — Hands-On Workshop.pdf`), delivered by "GDH Data & AI, Customer Engagement & Adoption Team", November 2026 | Retrieved 2026-11-24 | Vendor/partner enablement; a teaching example on 65 rows of toy data, **not** evidence of accuracy, scale or business value |

## Facts confirmed by Source 1 (SPARQL reference landing page)

1. HANA Cloud (HANA database) supports **core SPARQL 1.1** syntax and built-in functions per the W3C recommendation, plus **SAP extensions** (extended SQL-like built-in functions).
2. The knowledge graph engine offers **SQL interoperability in both directions**: SQL engine or **vector engine can federate queries to the KG engine**, and the KG engine can federate to the SQL engine. SQL statements, procedures, functions and system views for the KG engine are documented in the SQL Syntax section of the HANA Database reference.
3. **HTTP is not supported in this release** for the SPARQL 1.1 Protocol and the SPARQL 1.1 Graph Store HTTP Protocol. Access is through SQL (see Source 2 for the calls used).
4. **SAP restriction:** SAP recommends **not** using KG-engine capabilities without training or certification in SPARQL, the semantic web and RDF. This is a staffing and risk point for any delivery plan.
5. The page lists the 11 W3C SPARQL 1.1 recommendations. Support status for each beyond the two HTTP items is **not stated on this page** (e.g. Update, Federated Query, Entailment Regimes): still VERIFY on the detailed pages.

## Facts shown in Source 2 (workshop), with the exact interfaces used

| Topic | What the workshop shows |
|---|---|
| Querying | `SELECT * FROM SPARQL_TABLE('<SPARQL SELECT>')`: results return as a normal SQL result set |
| Loading/updating | `CALL SPARQL_EXECUTE('<SPARQL Update>', '', ?, ?)` with `INSERT DATA { GRAPH <name> { ... } }` and `CLEAR GRAPH <name>` |
| Privileges | `SPARQL_EXECUTE` privilege, plus normal SELECT/INSERT/CREATE TABLE on the schema |
| Named graphs | Graph identified by a name string used as `GRAPH <kg_...>`; workshop isolates each participant in their own named graph |
| Idempotence | Reloading the same triples did not create duplicates (set semantics); `INSERT DATA` is additive, so stale triples persist unless the graph is cleared |
| Ontology storage | No separate ontology object/store: the ontology is **triples in a named graph** alongside everything else |
| Authoring in production | Turtle (`.ttl`) or RDF files in version control, loaded with the same `SPARQL_EXECUTE` pattern; some organisations author in **PowerDesigner or SAP Datasphere Business Builder** and export |
| Debugging | `SELECT (COUNT(*) AS ?cnt) WHERE { GRAPH <g> { ?s ?p ?o } }` to verify triple counts |
| AI link | A **custom AI agent connected to Joule Work via a connector** reads the graph; the agent queries it to discover schema paths, then Joule generates SQL |

## The pattern the workshop teaches: "graph as semantic layer / schema guide"

- The graph holds **metadata**, not the business rows: business entities and their relationships (Supplier supplies Ingredient, Order contains Product), the physical tables and columns with SQL names, foreign-key links between columns, attribute roles (name, price, quantity, status), decoded status codes, and a **bridge** from each business entity to its ID column.
- The business rows stay in ordinary HANA tables.
- At question time the agent runs a SPARQL query to **find the join path and the right tables/columns**, then **generates and runs SQL** for the actual answer.
- Worked scale: 8 tables, 65 rows, 161 triples. Questions answered include multi-hop ones (customers to notify if an ingredient is unavailable; suppliers of the ingredients of a product; revenue per product).
- The workshop explicitly says the same approach applies to S/4, Datasphere or other SAP sources.

## What the workshop does not show (gaps to treat as open)

1. **No accuracy measurement or baseline.** There is no comparison against an agent with the raw schema or with column descriptions only. The claim that the graph "grounds" the agent is demonstrated, not tested.
2. **No authorization model.** Everything runs under the workshop user's own schema; nothing on row-level security, aggregation leakage, or user propagation.
3. **No scale, freshness or performance evidence.** 65 rows and 161 triples.
4. **Metadata-only.** Instance-level graphs (individual suppliers, POs and their links) are not covered; any claim about them needs other evidence.
5. **Manual authoring.** Triples are hand-written. The workshop notes generation from PowerDesigner/Datasphere but gives no procedure or effort figures for S/4-scale schemas (thousands of tables/columns).
6. **Joule integration specifics** (connector configuration, how SQL generation is constrained or secured) appear only as screenshots of answers; the mechanism is not documented in the PDF.
7. The workshop's Joule "answers" are screenshots; correctness was not independently verified here beyond the row-count arithmetic in the sample data (e.g. product revenue figures are consistent with the order items listed).

## Implications for chapter 11

- Lead with the **semantic-layer (metadata) pattern**: cheap, safe to start, directly evidenced by SAP's own enablement; keep the **instance-graph pattern** as a second step justified by multi-hop questions the metadata pattern cannot answer.
- Use the confirmed call forms (`SPARQL_TABLE`, `SPARQL_EXECUTE`), design for **SQL-only access (no HTTP)**, and treat **named graphs** as the unit of loading, versioning and (partial) separation.
- Staff a SPARQL/RDF-trained person (SAP's own restriction).
- Pilot must measure **baseline vs. graph-guided SQL generation** on real questions; the workshop supplies no such evidence.
