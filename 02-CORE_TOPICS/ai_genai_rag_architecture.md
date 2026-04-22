# AI / GenAI / RAG Architecture Interview Guide

## Enterprise GenAI Answer Structure

1. Use case and business KPI
2. Data boundaries and governance controls
3. Model strategy (hosted model vs custom model)
4. Retrieval strategy and grounding
5. Safety, compliance, and evaluation
6. Deployment and operational model
7. Cost optimization and value realization

## RAG Architecture Blueprint

- Ingestion:
  - Source connectors (documents, knowledge bases, data systems)
  - Cleansing, deduplication, PII handling
- Indexing:
  - Chunking strategy aligned to document semantics
  - Embedding generation pipeline
  - Vector index with metadata filters
- Retrieval:
  - Hybrid retrieval (keyword + semantic)
  - Re-ranking and context compression
- Generation:
  - Prompt templates with policy and instruction hierarchy
  - Guardrails and output schema checks
- Post-processing:
  - Citation enforcement and confidence scoring
  - Human-in-the-loop for high-risk workflows

## Azure AI Reference Components

- Azure OpenAI for model serving
- AI Search / vector-capable index for retrieval
- Blob/Data Lake for corpus storage
- APIM for policy, throttling, and auth control
- Key Vault and managed identities for secrets and access
- App Insights + monitoring stack for telemetry

## Responsible AI and Risk Controls

- Prompt injection defenses and context isolation
- Content filtering and policy-based moderation
- Red-team scenarios and adversarial testing
- Groundedness evaluation with benchmark datasets
- Model/version governance and rollback path

## Interview Narrative Example

"For a regulated enterprise copilot, I design RAG with strict data-domain isolation, managed identity-based access, and policy-enforced APIs. I optimize for grounded responses with citations and confidence thresholds, and route low-confidence/high-risk outputs to human review. I treat quality and safety metrics as production SLOs, not just model metrics."

