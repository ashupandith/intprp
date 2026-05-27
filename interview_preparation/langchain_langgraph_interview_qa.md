# LangChain and LangGraph Interview Q&A

## Format

Each question follows this structure:

- Question Summary
- Crisp Answer
- Detailed Explanation
- Final Interview Answer

---

# 1. What problem does LangChain solve?

## Question Summary

Tests whether you understand why LangChain is used instead of calling LLM APIs directly.

## Crisp Answer

LangChain solves the problem of building LLM applications by connecting prompts, models, retrievers, vector stores, tools, memory, and output parsers into reusable workflows.

## Detailed Explanation

A direct LLM call is simple: user sends input and model returns output. But real enterprise AI applications need more than that. They may need RAG, prompt templates, document search, embeddings, tool calling, structured output, memory, and workflow orchestration. LangChain provides ready-made building blocks for these patterns.

For example, in a RAG application, LangChain can load documents, split them, generate embeddings, store them in a vector database, retrieve relevant chunks, pass context to the LLM, and parse the final response.

## Final Interview Answer

> LangChain solves the problem of building LLM-powered applications beyond simple model calls. It provides reusable components for prompt templates, retrievers, vector stores, tools, memory, chains, agents, and output parsing. I would use LangChain for RAG, document Q&A, summarization, extraction, tool integration, and simple agent workflows.

---

# 2. What problem does LangGraph solve beyond LangChain?

## Question Summary

Tests whether you understand why LangGraph is needed for controlled agent workflows.

## Crisp Answer

LangGraph solves the problem of building stateful, controlled, multi-step agent workflows with branching, retries, checkpoints, human approval, and pause/resume capability.

## Detailed Explanation

LangChain is useful for chains, RAG, and basic agents. But when agent workflows become complex, we need explicit state and control. For example, an agent may need to plan, retrieve documents, call tools, validate results, ask for approval, retry on failure, and resume later. LangGraph provides graph-based workflow control using nodes, edges, state, and conditional routing.

## Final Interview Answer

> LangGraph extends LangChain by providing graph-based orchestration for complex agent workflows. It is useful when we need explicit state, branching, retries, fallback, checkpointing, human-in-the-loop approval, and controlled multi-step execution. I would use LangGraph for production-grade Agentic AI workflows where a free-running agent is too risky.

---

# 3. LangChain vs LangGraph

## Question Summary

Tests whether you can clearly distinguish both frameworks.

## Crisp Answer

LangChain is mainly used for LLM pipelines like RAG, chains, prompts, tools, and simple agents. LangGraph is used for stateful, multi-step, controlled agent workflows.

## Detailed Explanation

LangChain helps build LLM applications using reusable components. It is good for predictable flows like document Q&A, summarization, extraction, and basic tool usage. LangGraph is better when the workflow needs explicit state, conditional routing, retries, approvals, checkpoints, and multi-agent coordination.

## Final Interview Answer

> I see LangChain as a framework for building LLM pipelines such as RAG, prompt chains, retrievers, and tool integrations. LangGraph is used when we need controlled agent workflows with state, nodes, edges, branching, retries, checkpointing, and human approval. LangChain is enough for simple RAG; LangGraph is better for complex Agentic AI workflows.

---

# 4. What is a chain?

## Question Summary

Tests whether you understand the basic execution unit in LangChain.

## Crisp Answer

A chain is a sequence of steps where output from one step becomes input to the next step.

## Detailed Explanation

A simple chain can include a prompt template, LLM call, and output parser. For example, input text goes into a prompt, the prompt goes to the LLM, and the output parser converts the answer into JSON or structured text. Chains are useful when the flow is predictable and linear.

## Final Interview Answer

> A chain is a predefined sequence of LLM-related steps. For example, a prompt template sends input to an LLM and an output parser formats the result. Chains are useful for predictable workflows like summarization, classification, extraction, and simple RAG flows.

---

# 5. What is an agent?

## Question Summary

Tests whether you understand dynamic decision-making in LLM applications.

## Crisp Answer

An agent is an LLM-driven system that can decide the next step, use tools, retrieve information, maintain context, and complete a goal.

## Detailed Explanation

A chain follows a fixed path, but an agent can make decisions. For example, if a user asks, “Why is this order stuck?”, an agent may decide to call order status API, payment API, PoS status API, and search SOP documents before giving the final answer.

## Final Interview Answer

> An agent is an LLM-powered workflow that can reason, decide next steps, use tools, retrieve knowledge, and produce a final answer. In enterprise systems, agents must be controlled with tool allowlisting, authorization, explicit state, guardrails, observability, and human approval for risky actions.

---

# 6. What is a tool?

## Question Summary

Tests whether you understand how agents interact with external systems.

## Crisp Answer

A tool is a controlled function or API that an agent can call to retrieve data or perform an action.

## Detailed Explanation

LLMs do not automatically know live business data. Tools allow agents to call external systems. Examples include `get_order_status`, `check_payment_status`, `search_policy_docs`, `create_ticket`, or `create_refund_draft`. In production, tools should be small, specific, schema-bound, authorized, and audited.

## Final Interview Answer

> A tool is a function or API exposed to the agent. It allows the agent to interact with external systems, such as order APIs, payment APIs, search APIs, or ticketing systems. I would define tools with strict input schema, authorization checks, timeout, audit logging, and risk classification. The LLM can request a tool call, but backend policy should decide whether it is allowed.

---

# 7. What is a retriever?

## Question Summary

Tests whether you understand the retrieval part of RAG.

## Crisp Answer

A retriever is the component that fetches relevant documents or chunks based on the user query.

## Detailed Explanation

In RAG, the retriever sits between the user question and the LLM. It searches vector databases, Azure AI Search, or other knowledge stores and returns relevant chunks. The LLM then uses those chunks to generate a grounded answer.

## Final Interview Answer

> A retriever fetches relevant documents or chunks for a user query. In RAG, it provides the context that the LLM uses to answer. For enterprise RAG, I prefer hybrid retrieval with vector search, keyword search, metadata filtering, ACL trimming, and reranking to improve accuracy and security.

---

# 8. How do you build RAG using LangChain?

## Question Summary

Tests whether you understand the end-to-end RAG pipeline.

## Crisp Answer

Using LangChain, I build RAG by loading documents, splitting them into chunks, generating embeddings, storing them in a vector store, creating a retriever, and passing retrieved context to the LLM.

## Detailed Explanation

The RAG flow starts with document ingestion. Documents are loaded from PDFs, Word files, Blob Storage, SharePoint, or web pages. Then text splitters break documents into chunks. Embeddings are generated and stored in Azure AI Search or another vector store. At runtime, the retriever fetches relevant chunks for the user query, and the LLM answers using that context.

## Final Interview Answer

> I build RAG in LangChain by creating a pipeline for document loading, chunking, embedding generation, vector storage, retrieval, prompt construction, LLM response, and output parsing. In enterprise systems, I also add metadata, ACL trimming, citations, grounding validation, and evaluation to make the RAG system secure and reliable.

---

# 9. What are document loaders and text splitters?

## Question Summary

Tests whether you understand document ingestion in RAG.

## Crisp Answer

Document loaders read content from sources like PDFs, Word files, web pages, Blob Storage, or SharePoint. Text splitters divide large documents into smaller chunks for embedding and retrieval.

## Detailed Explanation

LLMs and vector search work better when documents are split into meaningful chunks. Document loaders bring content into the system, and text splitters prepare that content for indexing. Good splitting is important because poor chunking can lead to poor retrieval and hallucinated answers.

## Final Interview Answer

> Document loaders are used to ingest content from sources such as PDFs, Word files, HTML pages, Blob Storage, or SharePoint. Text splitters divide large documents into smaller chunks so they can be embedded and retrieved effectively. In RAG, good chunking directly impacts answer quality.

---

# 10. How do you decide chunk size and overlap?

## Question Summary

Tests whether you understand retrieval quality and token trade-offs.

## Crisp Answer

I decide chunk size and overlap based on document structure, retrieval quality, context requirement, and token cost.

## Detailed Explanation

Chunk size controls how much text is stored in each chunk. Overlap helps preserve meaning across chunk boundaries. A common starting point is 500–1000 tokens with 10–20% overlap, but the final value should be decided through evaluation. Policy documents may work better with section-based chunking, while FAQs may need smaller chunks.

## Final Interview Answer

> I decide chunk size based on document type, semantic boundaries, retrieval quality, and token cost. I usually start with 500–1000 tokens and 10–20% overlap, then evaluate retrieval quality. I avoid using one fixed chunk size blindly for all documents.

---

# 11. How do you implement source citations?

## Question Summary

Tests whether you can make RAG answers verifiable.

## Crisp Answer

I implement citations by storing metadata with each chunk and returning that metadata with retrieved context.

## Detailed Explanation

Each chunk should store metadata like document name, page number, section, URL, version, and last updated date. When the retriever returns chunks, the final answer includes citations based on this metadata. The model should not invent citations.

## Final Interview Answer

> I implement source citations by storing metadata with every indexed chunk, such as file name, page number, section, URL, document version, and last updated date. When the retriever returns chunks, the response includes citations from that metadata. I do not rely on the LLM to invent citation details.

---

# 12. How do you reduce hallucination in RAG?

## Question Summary

Tests whether you understand RAG quality and grounding controls.

## Crisp Answer

I reduce hallucination by using trusted sources, hybrid search, reranking, metadata filters, strict prompts, citations, grounding validation, and evaluation datasets.

## Detailed Explanation

RAG reduces hallucination but does not eliminate it. Wrong chunks, stale documents, poor prompts, or weak retrieval can still cause wrong answers. The system should answer only from retrieved context. If evidence is missing, it should say it does not know instead of inventing.

## Final Interview Answer

> I reduce hallucination by grounding answers in retrieved context, using hybrid search, metadata filtering, reranking, citations, and strict prompts. I also validate whether the answer is supported by retrieved chunks. If the context does not contain the answer, the system should say it cannot answer rather than guessing.

---

# 13. How do you secure RAG with ACL trimming?

## Question Summary

Tests whether you understand user-level authorization in enterprise RAG.

## Crisp Answer

ACL trimming ensures the retriever returns only those document chunks that the authenticated user is allowed to access.

## Detailed Explanation

During ingestion, each document or chunk should be stored with access metadata such as user IDs, group IDs, department, role, tenant, or classification. At query time, the retriever applies filters based on the user’s identity and permissions. This prevents the LLM from seeing unauthorized content.

## Final Interview Answer

> I secure RAG using ACL trimming. Each document chunk is indexed with access metadata such as allowed users, groups, roles, tenant, or classification. At query time, the retriever filters results based on the authenticated user’s permissions. This ensures the LLM only receives authorized context and prevents data leakage.

---

# 14. How do you define tools safely?

## Question Summary

Tests whether you understand secure tool design for agents.

## Crisp Answer

I define tools as small, specific, schema-bound, authorized, auditable functions with clear risk classification.

## Detailed Explanation

Tools should expose narrow business capabilities. For example, `get_order_status(orderId)` is safer than `execute_sql(query)`. Each tool should have strict input schema, authorization, timeout, retry policy, audit logging, and risk level. Read tools and write tools should be separated.

## Final Interview Answer

> I define tools safely by keeping them small, specific, and schema-bound. Each tool should have a clear purpose, strict input validation, authorization check, timeout, audit logging, and risk classification. I avoid broad tools like generic SQL execution or arbitrary API calls.

---

# 15. How do you prevent dangerous tool execution?

## Question Summary

Tests whether you understand agent safety and governance.

## Crisp Answer

I prevent dangerous tool execution using tool allowlisting, backend authorization, schema validation, risk classification, human approval, audit logs, and rate limits.

## Detailed Explanation

Dangerous actions include refunds, cancellations, external emails, data deletion, or production changes. The model should not execute these directly. It can request a tool call, but backend policy should validate whether the action is allowed and whether approval is required.

## Final Interview Answer

> I prevent dangerous tool execution by allowing only approved tools, validating input schema, checking user authorization, classifying action risk, and requiring human approval for high-risk actions. The LLM can request an action, but the backend decides whether it can actually execute. All tool calls should be logged and auditable.

---

# 16. What is state in LangGraph?

## Question Summary

Tests whether you understand how LangGraph tracks workflow progress.

## Crisp Answer

State in LangGraph is the structured data shared between workflow nodes, such as intent, context, tool results, retries, approval status, errors, and final response.

## Detailed Explanation

Agent workflows need memory of what has happened so far. State allows each node to read and update workflow information. For example, after an order status API call, the tool result can be added to state and used by the next node.

## Final Interview Answer

> State in LangGraph is the shared structured object passed across nodes. It tracks user intent, current step, retrieved context, tool results, retry count, errors, approval status, risk level, and final response. Explicit state makes agent workflows controllable, debuggable, and production-ready.

---

# 17. How do you model state in LangGraph?

## Question Summary

Tests whether you can design disciplined state for agent workflows.

## Crisp Answer

I model state as a typed, minimal, structured object containing only required workflow fields.

## Detailed Explanation

Good state design separates transient workflow data from persistent audit/checkpoint data. State may include user context, intent, current node, retrieved document references, tool outputs, retry count, risk level, approval status, and final response. Avoid storing unnecessary sensitive data.

## Final Interview Answer

> I model LangGraph state as a typed object with fields like user intent, authenticated user context, current step, retrieved document references, tool results, retry count, error details, approval status, risk level, and final answer. I keep state minimal and avoid storing sensitive data unnecessarily.

---

# 18. What are nodes and edges in LangGraph?

## Question Summary

Tests whether you understand the graph-based workflow model.

## Crisp Answer

Nodes are workflow steps, and edges define how the workflow moves from one step to another.

## Detailed Explanation

A node can be intent detection, retrieval, tool call, validation, approval, or final response. An edge connects nodes. Conditional edges route the workflow based on state. For example, if `approvalRequired=true`, route to approval node; otherwise execute the tool directly.

## Final Interview Answer

> In LangGraph, nodes represent workflow steps and edges represent transitions between those steps. Conditional edges allow routing based on state. For example, after risk evaluation, the workflow can route either to human approval or direct tool execution.

---

# 19. How do you implement planner-executor pattern?

## Question Summary

Tests whether you understand structured agent orchestration.

## Crisp Answer

Planner-executor separates planning from execution. The planner creates the steps, and the executor runs only approved steps.

## Detailed Explanation

The planner interprets the user goal and breaks it into tasks. The executor performs those tasks using tools, RAG, or APIs. A policy layer validates whether the plan and tool calls are allowed. A verifier checks the result before the final answer.

## Final Interview Answer

> I implement planner-executor by separating the reasoning phase from the execution phase. The planner creates a step-by-step plan, the policy layer validates it, the executor runs approved tools or retrieval steps, and the verifier checks the result. This gives better control than allowing the agent to act freely.

---

# 20. How do you implement supervisor pattern?

## Question Summary

Tests whether you understand multi-agent coordination.

## Crisp Answer

The supervisor pattern uses a central supervisor to coordinate specialist agents or workflow nodes.

## Detailed Explanation

A supervisor can route work to a RAG agent, tool agent, policy agent, or response agent. It manages state, validates outputs, handles fallback, and aggregates final response. This prevents uncontrolled agent-to-agent behavior.

## Final Interview Answer

> I implement supervisor pattern by using a central supervisor node that routes tasks to specialist agents or nodes. For example, one agent handles retrieval, another handles tool calls, and another validates policy. The supervisor controls routing, state, validation, fallback, and final response aggregation.

---

# 21. How do you implement human-in-the-loop?

## Question Summary

Tests whether you can design approval workflows for risky actions.

## Crisp Answer

Human-in-the-loop pauses the workflow for approval before executing risky actions.

## Detailed Explanation

Actions like refund, cancellation, external email, data deletion, or production change should not execute automatically. The graph can route to an approval node, checkpoint the state, show evidence and recommendation to the reviewer, and resume after approval.

## Final Interview Answer

> I implement human-in-the-loop by classifying actions by risk. If an action is high-risk, the workflow routes to an approval node, saves checkpointed state, and waits for reviewer approval. Only after approval does the workflow execute the action. Rejections and modifications are also logged.

---

# 22. How do you prevent infinite loops?

## Question Summary

Tests whether you understand operational safety in agent workflows.

## Crisp Answer

I prevent infinite loops using max iteration limits, retry budgets, timeouts, explicit stop conditions, fallback paths, and human escalation.

## Detailed Explanation

Agent workflows can loop if they repeatedly fail to decide or call tools. Each loop should update state and have a maximum limit. If the workflow cannot progress after defined attempts, it should stop safely, fallback, or escalate.

## Final Interview Answer

> I prevent infinite loops by defining maximum iterations, retry budgets, timeouts, explicit stop conditions, and fallback paths. If the graph cannot make progress, it should stop safely or escalate to a human instead of continuing indefinitely.

---

# 23. How do you checkpoint and resume workflows?

## Question Summary

Tests whether you understand long-running and recoverable workflows.

## Crisp Answer

Checkpointing saves workflow state so the process can resume after failure, delay, or human approval.

## Detailed Explanation

Long-running workflows cannot depend only on memory. Before risky actions or approval waits, the system should persist state. After approval or recovery, the workflow resumes from the checkpoint instead of starting again.

## Final Interview Answer

> Checkpointing means persisting graph state at important points so the workflow can resume after failure, pause, or human approval. I would checkpoint after tool calls, before approval waits, and before risky actions. For enterprise systems, checkpoint state should be stored in durable storage like Cosmos DB, SQL, or Redis.

---

# 24. How do you monitor LangGraph workflows?

## Question Summary

Tests whether you understand observability for agent workflows.

## Crisp Answer

I monitor LangGraph workflows at node level and workflow level using correlation ID, logs, metrics, traces, tool-call status, retries, latency, cost, and policy violations.

## Detailed Explanation

Monitoring only final API latency is not enough. We need to know which node failed, which tool was called, how long it took, how many retries happened, whether approval was needed, and how much token/cost was consumed.

## Final Interview Answer

> I monitor LangGraph workflows by logging each node execution with correlation ID, node name, input type, output status, latency, retry count, tool-call result, and errors. I also track token usage, cost, approval rate, fallback rate, policy violations, and final quality metrics using Application Insights or similar observability tools.

---

# 25. How do you deploy LangChain/LangGraph on Azure?

## Question Summary

Tests whether you can design production deployment for LangChain/LangGraph applications on Azure.

## Crisp Answer

I deploy LangChain or LangGraph inside a FastAPI/Python backend on Azure App Service, AKS, or Container Apps, with APIM, Entra ID, Azure OpenAI, Azure AI Search, Cosmos DB/SQL, Service Bus, Functions, Key Vault, and Application Insights.

## Detailed Explanation

The frontend should not directly call Azure OpenAI. Requests should come through APIM and backend API. The backend hosts LangChain/LangGraph orchestration. Azure OpenAI handles reasoning and embeddings. Azure AI Search supports RAG. Cosmos DB or SQL stores state and checkpoints. Service Bus and Functions handle async work. Key Vault stores secrets. Application Insights monitors latency, tool calls, token usage, and errors.

## Final Interview Answer

> I would deploy LangChain or LangGraph as part of a FastAPI/Python backend hosted on Azure App Service, AKS, or Container Apps. APIM would sit in front for authentication, throttling, and governance. The backend integrates with Azure OpenAI, Azure AI Search for RAG, Cosmos DB or SQL for state and checkpoints, Service Bus and Functions for async actions, Key Vault for secrets, and Application Insights for observability. I would also add token limits, cost monitoring, tool allowlists, and human approval for risky actions.
