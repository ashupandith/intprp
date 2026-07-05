# Additional Scenario-Based Interview Questions
## Optum Senior Cloud Architect / Azure / Healthcare / Consulting

Use this format while speaking:
**Clarify requirement → Explain architecture → Mention Azure services → Mention security/compliance → Explain trade-offs → Give recommendation**

---

## Scenario 1. A healthcare payer client has many legacy .NET Framework applications running on Windows servers. They want to move to Azure. How will you approach?

### What interviewer wants to check
They want to check whether you understand legacy modernization, cloud assessment, 6R migration, phased roadmap, risk reduction, and healthcare compliance.

### Senior Architect Answer
I would not directly start migration. First, I would perform an application portfolio assessment. I would capture the application technology stack, .NET Framework version, IIS dependency, database, integrations, authentication mechanism, batch jobs, file shares, certificates, secrets, monitoring, user base, business criticality, and PHI/PII data flow.

Then I would classify applications using the 6R approach. Some applications may be rehosted to Azure VMs if they are tightly coupled or need quick migration. Some can be replatformed to Azure App Service if compatible. High-value applications can be refactored to .NET 8, APIs, containers, or microservices depending on business value.

For target architecture, I would design Azure landing zone, hub-spoke network, identity using Entra ID, Key Vault for secrets, private endpoints for SQL/Storage/Key Vault, APIM for APIs, Application Insights for monitoring, and Azure Policy for governance.

Since this is healthcare, I would specifically identify PHI/PII data, apply encryption, RBAC, audit logging, masking where required, and ensure sensitive data is not logged.

Migration would be phased through waves, starting with low-risk applications to validate landing zone and deployment model, then moving critical applications with proper testing, cutover, rollback, and hypercare.

### Shortcut
**Assess → Classify → Modernize → Secure → Migrate → Monitor**

---

## Scenario 2. A client asks whether they should use AKS or App Service for a new healthcare API platform. What will you recommend?

### Senior Architect Answer
I would first clarify the workload characteristics. I would ask how many APIs or microservices are expected, whether they need container orchestration, service mesh, advanced deployment patterns, custom networking, autoscaling, and Kubernetes operational maturity.

If the requirement is to host a few standard .NET APIs with managed deployment, autoscaling, VNet integration, managed identity, deployment slots, and low operational overhead, I would recommend Azure App Service.

If the platform has many containerized microservices, needs Kubernetes-level control, service discovery, custom ingress, sidecars, advanced scaling, workload isolation, or portability, then AKS is a better choice.

For many enterprise teams, App Service or Azure Container Apps can be better than AKS because AKS adds operational complexity. AKS requires cluster upgrades, node pool management, ingress management, Kubernetes security, monitoring, networking, and platform engineering maturity.

For healthcare APIs, regardless of compute choice, I would use APIM, WAF, private networking, managed identity, Key Vault, logging, and PHI/PII controls.

### Strong Interview Line
I would not choose AKS just because it is popular. I would choose AKS only when Kubernetes-level orchestration is justified.

---

## Scenario 3. A claims processing API must respond within 1 second, but it depends on 4 downstream systems. How will you design it?

### Senior Architect Answer
First, I would clarify whether 1 second means average latency, p95, or p99. I would also understand downstream response times, payload size, business criticality, and whether all downstream calls are mandatory for the response.

If all downstream calls are independent and required, I would call them in parallel using async programming and `Task.WhenAll` instead of sequential calls. I would apply timeout, retry only for transient failures, and circuit breaker for failing dependencies.

If some data is reference data or not changing frequently, I would cache it using Redis or in-memory cache. If some downstream data is not required immediately, I would move that part to asynchronous processing using Service Bus and return the essential response first.

If the full operation cannot reliably finish within 1 second, I would design an async pattern where the API accepts the request, returns a tracking ID quickly, and processing continues in background.

### Shortcut
**Clarify SLA → Parallelize → Cache → Timeout → Circuit Breaker → Async if needed**

---

## Scenario 4. A client has sensitive healthcare documents in Blob Storage. Security team says public access must be disabled. How will you design access?

### Senior Architect Answer
For sensitive healthcare documents, I would use Azure Storage with public network access disabled and access through Private Endpoint.

I would create a private endpoint for the required storage subresource, such as Blob. I would configure the private DNS zone `privatelink.blob.core.windows.net` and link it to the VNet. Applications running in App Service, AKS, Functions, or VMs should access storage through private network.

For identity, I would avoid connection strings or storage keys where possible. I would use Managed Identity and assign least-privilege RBAC roles such as Storage Blob Data Reader or Contributor depending on need.

I would enable encryption at rest, soft delete, versioning, lifecycle policies, diagnostic logs, and audit access. I would also ensure PHI/PII documents are not exposed through public URLs, and SAS tokens are restricted if used.

### Shortcut
**Private Endpoint + Private DNS + Managed Identity + RBAC + Audit**

---

## Scenario 5. A client wants to expose public APIs but keep backend services private. How will you design it?

### Senior Architect Answer
I would expose APIs through a controlled gateway layer and keep backend services private.

For internet-facing access, I can use Azure Front Door WAF or Application Gateway WAF in front of APIM. APIM will validate JWT tokens, apply rate limiting, quota, request validation, and API policies.

Backend services such as App Service, AKS, or Functions should not be directly public. They can be integrated with VNet and exposed privately using Private Endpoint or internal load balancer. APIM should have network connectivity to those backend services through VNet integration or internal deployment pattern.

I would also use private DNS, NSGs, Azure Firewall if required, managed identity between APIM/backend where possible, and Application Insights for tracing.

### Shortcut
**Public gateway, private backend**

---

## Scenario 6. A healthcare client wants a document Q&A chatbot over policy documents. How will you design it?

### Senior Architect Answer
I would design a secure RAG architecture.

Policy documents can be stored in Blob Storage or SharePoint. An ingestion pipeline extracts text, cleans it, chunks it, generates embeddings using Azure OpenAI, and stores chunks with metadata in Azure AI Search.

At runtime, the user asks a question through a secure API. The API authenticates the user using Entra ID, applies authorization and security trimming, retrieves relevant chunks using hybrid search, and sends only the selected context to Azure OpenAI. The model generates an answer with citations.

To reduce hallucination, I would instruct the model to answer only from provided context and say it does not know if evidence is not found. I would use citations, evaluation datasets, prompt testing, feedback, and monitoring.

For healthcare, I would protect PHI/PII using access controls, private endpoints, safe logging, audit trails, content filtering, and prompt injection protection.

### Shortcut
**RAG = Retrieve → Augment → Generate → Cite → Govern**

---

## Scenario 7. A cloud workload is running but monthly Azure cost is very high. What will you do?

### Senior Architect Answer
I would first create cost visibility. I would check Azure Cost Management by subscription, resource group, service, environment, application, and owner. If tagging is missing, I would fix tagging because without cost allocation we cannot manage cost properly.

Then I would identify unused and underutilized resources: stopped VMs with attached disks, oversized App Service plans, over-provisioned databases, unused public IPs, unattached disks, old snapshots, and non-production resources running continuously.

Optimization actions may include right-sizing compute, autoscaling, reserved instances or savings plans, shutting down dev/test environments after hours, storage lifecycle policies, database query optimization, caching, and choosing appropriate SKUs.

I would also create budgets, alerts, dashboards, and Azure Policy to prevent uncontrolled resource creation.

### Shortcut
**Visibility → Tagging → Right-size → Auto-scale → Reserve → Govern**

---

## Scenario 8. Production system has frequent failures because a third-party API is unstable. How will you design resilience?

### Senior Architect Answer
I would treat the third-party API as an unreliable dependency and design resilience around it.

First, I would add timeout so requests do not hang indefinitely. Then I would apply retry with exponential backoff and jitter only for transient errors such as 408, 429, 500, 502, 503, or 504. I would not retry validation errors, unauthorized errors, or business failures.

If the API continues failing, I would use circuit breaker to stop repeated calls temporarily and prevent cascading failure. If business allows, I would return fallback response or cached data.

For non-real-time operations, I would decouple using Service Bus. The API can accept the request and process third-party calls asynchronously in background.

I would monitor dependency failure rate, latency, timeout count, circuit breaker state, and business impact.

### Shortcut
**Timeout → Retry transient → Circuit breaker → Fallback → Queue if async possible**

---

## Scenario 9. A client wants multi-region deployment for a critical healthcare application. How will you design it?

### Senior Architect Answer
I would first clarify RTO and RPO. RTO defines how quickly the application must recover, and RPO defines how much data loss is acceptable.

If the application is mission-critical and needs very low RTO, I may design active-active deployment across two regions using Azure Front Door for global routing. Both regions run application services, and data replication is designed based on database choice.

If cost or data consistency is a concern, active-passive or warm standby may be better. In that case, primary region handles traffic and secondary region is ready for failover.

For data, Azure SQL failover groups, Cosmos DB multi-region replication, Storage GRS/RA-GRS, and backup/restore patterns can be used depending on the workload.

I would also include IaC-based environment recreation, monitoring, runbooks, DNS failover, DR testing, and compliance validation.

### Shortcut
**RTO/RPO → Active-active or active-passive → Data replication → Failover test**

---

## Scenario 10. A client says they want microservices. How will you validate if microservices are really needed?

### Senior Architect Answer
I would first understand the business and technical drivers. Microservices are useful when different domains need independent development, deployment, scaling, ownership, and technology evolution.

But microservices also add complexity: distributed transactions, observability, network latency, data consistency, DevOps maturity, API governance, versioning, and operational overhead.

I would assess the current application boundaries using domain-driven design, business capabilities, data ownership, team ownership, release bottlenecks, scalability needs, and integration complexity.

If the application is small or the team lacks DevOps maturity, a modular monolith may be better initially. If clear domain boundaries and independent scaling needs exist, microservices can be justified.

### Shortcut
**Microservices only when boundaries and independent scaling/deployment justify complexity**

---

## Scenario 11. A client wants to migrate database to Azure. How will you choose between Azure SQL, SQL Managed Instance, Cosmos DB, and Data Lake?

### Senior Architect Answer
I would choose based on workload type.

If the application uses relational data, transactions, joins, and SQL Server compatibility, Azure SQL Database is suitable. If it needs near-full SQL Server compatibility, SQL Agent, cross-database queries, or easier migration from on-prem SQL Server, SQL Managed Instance may be better.

If the application needs globally distributed, low-latency, NoSQL access with flexible schema and high scalability, Cosmos DB is suitable.

If the requirement is analytics, raw data storage, batch processing, data science, or AI/ML, then Data Lake is suitable.

For healthcare, I would also consider PHI/PII, encryption, access control, masking, audit logs, backup, retention, and data residency.

### Shortcut
**Relational app = Azure SQL; SQL compatibility = Managed Instance; NoSQL/global scale = Cosmos DB; Analytics/raw data = Data Lake**

---

## Scenario 12. A client asks to implement zero trust in Azure. What will you propose?

### Senior Architect Answer
Zero Trust means never trust by default and always verify. I would implement it across identity, network, application, data, and monitoring layers.

For identity, I would use Entra ID, MFA, Conditional Access, RBAC, PIM, and Managed Identity. For network, I would use private endpoints, segmentation, NSGs, Azure Firewall, WAF, and deny-by-default rules. For applications, I would validate tokens, enforce authorization, use secure APIs, and apply least privilege. For data, I would use encryption, masking, audit logging, and access policies.

I would also continuously monitor using Defender for Cloud, Azure Monitor, Sentinel if available, and audit logs.

### Shortcut
**Never trust → Always verify → Least privilege → Monitor continuously**

---

## Scenario 13. A team stores secrets in appsettings.json. What will you recommend?

### Senior Architect Answer
I would recommend moving secrets out of appsettings.json and storing them in Azure Key Vault. The application should use Managed Identity to access Key Vault, so no client secrets are stored in code or configuration.

For local development, developers can use user secrets or local secure configuration. For production, all secrets, certificates, keys, connection strings, and API keys should come from Key Vault or managed identity-based access.

I would also enable Key Vault logging, RBAC, private endpoint if required, soft delete, purge protection, and secret rotation process.

### Shortcut
**No secrets in config. Use Key Vault + Managed Identity.**

---

## Scenario 14. A client wants to use GenAI for claims approval. What risk controls will you suggest?

### Senior Architect Answer
I would be careful with GenAI in claims approval because it may directly impact members and payments. I would position AI as an assistive capability, not an autonomous decision-maker, unless governance is very mature.

AI can summarize claim documents, extract information, detect missing documents, provide policy references, and recommend possible next actions. But final approval/denial should be governed by business rules and human review for sensitive cases.

Controls should include grounded RAG, citations, audit trail, prompt injection protection, PHI/PII protection, access control, model evaluation, human-in-the-loop, confidence score, and decision explainability.

### Shortcut
**AI assists, rules/humans decide**

---

## Scenario 15. A client says their developers create Azure resources manually. What will you recommend?

### Senior Architect Answer
I would recommend Infrastructure as Code using Terraform, Bicep, or ARM templates depending on organization standard. Manual resource creation leads to inconsistency, drift, security gaps, and audit challenges.

With IaC, infrastructure becomes version-controlled, repeatable, reviewable, and auditable. I would also create CI/CD pipelines for infrastructure deployment, enforce Azure Policy for governance, use naming/tagging standards, and separate environment configurations.

For production, changes should go through pull request, approval, automated validation, and deployment pipeline.

### Shortcut
**Manual cloud = drift. IaC = repeatable and governed.**

---

## Scenario 16. A client has multiple teams deploying APIs inconsistently. How will you standardize?

### Senior Architect Answer
I would define an API governance framework.

It should include API design standards, naming conventions, versioning strategy, authentication and authorization standards, error response format, pagination, correlation ID, logging, rate limiting, documentation, OpenAPI specification, and APIM onboarding process.

I would also define reusable templates and reference implementation so teams can follow common patterns. CI/CD pipelines should validate API contracts, security checks, code quality, and deployment standards.

APIM should be used as central API gateway to enforce policies consistently.

### Shortcut
**Standards + templates + APIM + CI/CD validation**

---

## Scenario 17. A healthcare client wants auditability for every data access. How will you design it?

### Senior Architect Answer
I would design auditability at application, API, database, and infrastructure levels.

At API level, I would log user identity, action, timestamp, correlation ID, request metadata, and outcome. I would avoid logging sensitive PHI/PII values unless required and protected.

At data level, I would enable database auditing, access logs, storage diagnostics, Key Vault access logs, and monitor administrative operations.

At identity level, Entra ID sign-in logs and audit logs should be retained. Logs should go to Log Analytics or SIEM like Microsoft Sentinel if available.

Audit logs should be immutable or protected from tampering, retained based on compliance policy, searchable, and monitored for anomalies.

### Shortcut
**Who accessed what, when, from where, and what happened**

---

## Scenario 18. A client has one monolithic application with multiple modules. How will you modernize it?

### Senior Architect Answer
I would not immediately break the monolith into microservices. First, I would understand business domains, module dependencies, database coupling, release bottlenecks, performance issues, and team ownership.

If the monolith is stable but difficult to deploy, I may first improve CI/CD, observability, configuration, and infrastructure by moving it to App Service or containers.

Then I would identify bounded contexts and extract high-value or high-change modules gradually using strangler pattern. For example, authentication, notification, reporting, or claims document processing can be separated first if they have clear boundaries.

I would keep data consistency, integration, transactions, and rollback strategy in mind.

### Shortcut
**Stabilize first, then extract modules gradually using strangler pattern**

---

## Scenario 19. A client asks how to handle data consistency across microservices.

### Senior Architect Answer
In microservices, each service should own its own data. We should avoid distributed transactions across services where possible.

For consistency, I would use event-driven communication, Saga pattern, outbox pattern, idempotent consumers, and eventual consistency.

For example, if claim creation triggers payment validation and provider validation, each service performs local transaction and publishes events. If a later step fails, compensating action can be triggered.

Outbox pattern ensures events are reliably published after database changes.

### Shortcut
**Local transaction + events + saga + outbox + idempotency**

---

## Scenario 20. A client asks for production readiness checklist before go-live.

### Senior Architect Answer
My production readiness checklist includes architecture review, security review, performance testing, load testing, DR and backup validation, monitoring and alerting, logging and correlation ID, secrets in Key Vault, managed identity, network restrictions, private endpoints, cost alerts, runbooks, CI/CD pipelines, rollback plan, health checks, API documentation, compliance validation, support ownership, and incident management process.

For healthcare, I also check PHI/PII logging, audit trails, access review, data retention, and encryption.

### Shortcut
**Security + Performance + Monitoring + DR + Runbook + Rollback**

---

# Final Scenario Revision Cheat Sheet

```text
Legacy migration:
Assess → 6R → Landing Zone → Migration Waves → Secure → Monitor

AKS vs App Service:
App Service for simple APIs, AKS for Kubernetes-scale microservices

1-sec API:
Parallelize, cache, timeout, circuit breaker, async if needed

Sensitive Storage:
Private Endpoint, Private DNS, Managed Identity, RBAC

Public API/private backend:
WAF/APIM public, backend private

RAG:
Chunk, embed, search, ground, cite, secure

Cost:
Tag, analyze, right-size, autoscale, reserve, govern

Third-party failure:
Timeout, retry, circuit breaker, fallback, queue

Multi-region:
RTO/RPO, active-active/passive, data replication, DR testing

Microservices:
Use only when boundaries and independent scaling justify complexity

Data platform:
Azure SQL, MI, Cosmos, Data Lake based on workload

Zero Trust:
Verify identity, least privilege, private access, monitor

Secrets:
Key Vault + Managed Identity

GenAI:
AI assists, human/rules decide

IaC:
Terraform/Bicep, no manual drift

API governance:
Standards, APIM, templates, validation

Audit:
Who, what, when, where, outcome

Monolith:
Stabilize, then strangler pattern

Consistency:
Saga, outbox, idempotency

Go-live:
Security, performance, monitoring, DR, rollback, runbook
```
