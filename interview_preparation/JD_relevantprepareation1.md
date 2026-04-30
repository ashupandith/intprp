# JD Relevant Preparation Mapping

This file maps your requested topics to existing pages in this repo and identifies where new pages were added for missing coverage.

## Coverage Legend
- Covered: Good dedicated coverage already exists.
- Partial: Mentioned, but not deep enough as a primary study page.
- Added now: Newly created page for this gap.

## Azure Platform and Architecture Topics

| Topic | Status | Relevant page(s) |
| --- | --- | --- |
| Azure App Services vs Functions vs AKS | Covered | `docs/compute/compute_architecture.md`, `docs/azure/azure_topic_master.md` |
| Azure Functions and Durable Functions | Covered | `docs/compute/compute_architecture.md`, `docs/azure/azure_topic_master.md` |
| Event-driven architecture (Service Bus, Event Grid, Event Hub, Kafka) | Covered | `docs/integration/apim_messaging_eventing.md`, `docs/integration-architecture/api_messaging_eventing_patterns.md` |
| API Management (JWT, rate limit, versioning, private APIs) | Covered | `docs/integration/apim_messaging_eventing.md` |
| Azure networking (hub-spoke, Private Endpoints, NSG, Firewall, App Gateway, Front Door) | Covered | `docs/networking/azure_networking_and_hybrid_connectivity.md`, `docs/security/security_iam_networking.md` |
| Security (Managed Identity, Key Vault, RBAC, Zero Trust, Defender for Cloud) | Covered | `docs/security/security_iam_networking.md`, `docs/security-architecture/zero_trust_identity_network_controls.md` |
| Migration (rehost, replatform, refactor, modernization roadmap) | Covered | `docs/migration-architecture/migration_strategies_azure_migrate.md` |
| Governance (Landing Zone, policy, tagging, cost control, architecture board) | Covered | `docs/cloud-architecture/azure_landing_zone_and_platform.md`, `docs/governance/azure_governance_policy_and_cost_controls.md` |

## GenAI / RAG / LLM Topics

| Topic | Status | Relevant page(s) |
| --- | --- | --- |
| RAG architecture (ingestion, chunking, embeddings, retrieval, reranking, answer generation) | Covered | `docs/data-ai/rag_openai_ai_search.md`, `docs/data-ai/rag_retrieval_engineering_architecture.md` |
| Azure OpenAI (models, deployment, quota, cost, safety) | Covered | `docs/data-ai/rag_openai_ai_search.md`, `docs/data-ai/llm_selection_routing_fallback_architecture.md` |
| Azure AI Search (hybrid, semantic, filters, security trimming) | Covered | `docs/data-ai/rag_openai_ai_search.md` |
| Vector databases (Azure AI Search, Pinecone, Weaviate, FAISS, Chroma) | Covered | `docs/data-ai/rag_retrieval_engineering_architecture.md` |
| Prompt engineering (system prompt, few-shot, structured output, JSON mode) | Covered | `docs/data-ai/rag_openai_ai_search.md`, `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| Guardrails (PII masking, prompt injection defense, content filtering) | Covered | `docs/data-ai/guardrails_security_privacy_responsible_ai.md` |
| Evaluation (faithfulness, relevance, hallucination, groundedness) | Covered | `docs/data-ai/llmops_observability_evaluation_langsmith_arize.md` |
| Observability (tracing, token usage, latency, feedback loop) | Covered | `docs/data-ai/llmops_observability_evaluation_langsmith_arize.md` |

## Agent Framework Topics

| Topic | Status | Relevant page(s) |
| --- | --- | --- |
| LangChain | Covered | `docs/data-ai/agentic_ai_langchain_langgraph.md` |
| LangGraph | Covered | `docs/data-ai/agentic_ai_langchain_langgraph.md` |
| AutoGen | Added now | `docs/data-ai/agent_frameworks_autogen_crewai_openai_agents_sdk.md` |
| crewAI | Added now | `docs/data-ai/agent_frameworks_autogen_crewai_openai_agents_sdk.md` |
| OpenAI Agents SDK | Added now | `docs/data-ai/agent_frameworks_autogen_crewai_openai_agents_sdk.md` |

## Backend Engineering and Delivery Topics

| Topic | Status | Relevant page(s) |
| --- | --- | --- |
| FastAPI | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| async/await | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| Pydantic | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| requests/httpx | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| environment configuration | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| logging | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| retry handling | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| OpenAI/Azure OpenAI SDK | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |
| Docker | Covered | `docs/data-ai/genai_deployment_docker_kubernetes_terraform_cicd.md` |
| unit testing | Covered | `docs/data-ai/python_fastapi_async_backend_for_genai.md` |

## AI SDLC / Enterprise Ops Topics

| Topic | Status | Relevant page(s) |
| --- | --- | --- |
| CI/CD | Covered | `docs/data-ai/genai_deployment_docker_kubernetes_terraform_cicd.md`, `docs/azure/cicd_azure_devops.md` |
| Prompt versioning | Covered | `docs/data-ai/llmops_observability_evaluation_langsmith_arize.md` |
| Model evaluation | Covered | `docs/data-ai/llmops_observability_evaluation_langsmith_arize.md` |
| Monitoring | Covered | `docs/data-ai/llmops_observability_evaluation_langsmith_arize.md` |
| Feedback loop | Covered | `docs/data-ai/llmops_observability_evaluation_langsmith_arize.md` |
| Human-in-the-loop | Covered | `docs/data-ai/guardrails_security_privacy_responsible_ai.md`, `docs/data-ai/rag_openai_ai_search.md` |
| Security | Covered | `docs/data-ai/guardrails_security_privacy_responsible_ai.md`, `docs/security/security_iam_networking.md` |
| Cost control | Covered | `docs/data-ai/llm_selection_routing_fallback_architecture.md`, `docs/governance/azure_governance_policy_and_cost_controls.md` |

## Leadership, Presales, and Architecture Communication Topics

| Topic | Status | Relevant page(s) |
| --- | --- | --- |
| Roadmap creation | Covered | `docs/research/priority_execution_plan.md`, `docs/migration-architecture/migration_strategies_azure_migrate.md` |
| Stakeholder management | Covered | `03-QUESTION_BANK/behavioral_and_leadership.md` |
| Architecture governance | Covered | `docs/governance/documentation_blueprinting_delivery_governance.md` |
| Delivery leadership | Covered | `03-QUESTION_BANK/behavioral_and_leadership.md` |
| Business value | Covered | `03-QUESTION_BANK/behavioral_and_leadership.md`, `docs/governance/azure_governance_policy_and_cost_controls.md` |
| Pre-sales (proposal, estimation, client presentation) | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| How to respond to RFP | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| How to create solution architecture | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| How to estimate effort | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| How to present options to leadership | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| Build vs buy comparison | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| Show ROI | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| Handle risk and assumptions | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |
| 8-step architecture approach (problem to success metrics) | Added now | `docs/cloud-architecture/rfp_solution_architecture_estimation_and_roi.md` |

