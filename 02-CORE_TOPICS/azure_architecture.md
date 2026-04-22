# Azure Architecture Interview Guide

## What Interviewers Evaluate

- Ability to design secure, scalable, and cost-aware enterprise systems
- Decision quality across services, not just service knowledge
- Governance and operating model maturity
- Trade-off articulation under constraints

## Core Architecture Framework

Use this structure when answering scenario questions:

1. Business goals and constraints
2. Non-functional requirements (availability, latency, compliance, cost)
3. Target-state architecture (logical + deployment view)
4. Security and governance controls
5. Operations model (monitoring, SRE, incident response)
6. Migration path and phased rollout

## Azure Service Decision Anchors

- Compute:
  - App Service: managed web/API, fast delivery, lower ops burden
  - AKS: advanced orchestration, portability, platform engineering control
  - Functions: event-driven, burst workloads
  - Container Apps: microservices with less cluster management
- Integration:
  - Service Bus for reliable enterprise messaging
  - Event Grid for reactive event routing
  - Event Hubs for high-throughput telemetry streaming
  - APIM for API lifecycle, policy enforcement, and governance
- Data:
  - Azure SQL for relational transactional workloads
  - Cosmos DB for globally distributed low-latency applications
  - Blob/Data Lake for large-scale analytics and AI pipelines
  - Redis for latency reduction and resilience patterns

## Reliability Talking Points

- Define SLO/SLI, then architecture around them
- Use zone-redundant and region-redundant strategies where needed
- Separate control plane and data plane risk considerations
- Implement graceful degradation and backpressure
- Align DR strategy to business-critical tiering and RTO/RPO

## Cost and FinOps Talking Points

- Right-size and autoscale by workload profile
- Reservation and savings plans for steady-state workloads
- Unit economics for architecture choices (cost per transaction/request)
- Chargeback/showback model for enterprise platform teams

## Governance and Platform Engineering

- Landing zones and policy-as-code from day 1
- Management groups and RBAC boundaries by environment/business unit
- Golden paths and reference templates for delivery teams
- Security and compliance gates in CI/CD

