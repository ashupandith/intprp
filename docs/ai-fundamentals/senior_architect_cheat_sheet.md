# Senior Architect Cheat Sheet: Enterprise AI

## 1) Core positioning
- Use **automation** for repeatable rule-based workflows.
- Use **RPA** for UI-driven legacy tasks without APIs.
- Use **ML** for prediction, classification, anomaly detection, and ranking.
- Use **GenAI** for unstructured language-heavy tasks.
- Use the **simplest safe solution** that meets the requirement.

## 2) One-line definitions
- **LLM**: A probabilistic language model that predicts the next token and can perform many language tasks.
- **Token**: A chunk of text used for processing, limits, cost, and latency.
- **Context window**: Total information the model can see in one request.
- **Embedding**: Vector representation of meaning used for semantic retrieval.
- **Inference**: Runtime generation by the model.
- **Grounding**: Anchoring responses to trusted data and tools.
- **Hallucination**: Confident but unsupported or incorrect output.

## 3) Fast decision rules
- If the workflow is exact and deterministic, prefer code or rules.
- If the task is prediction from historical data, prefer ML.
- If the task is language-heavy and ambiguous, consider GenAI.
- If the process is screen-based and API-poor, consider RPA.
- If enterprise knowledge changes often, prefer RAG over fine-tuning.

## 4) Copilot vs assistant vs agent
- **Copilot**: Human stays in control.
- **Assistant**: Conversational and reactive.
- **Agent**: Goal-driven and action-oriented.
- Start with **copilot**, then move to **agent** only if autonomy creates measurable value.

## 5) Single-agent vs multi-agent
- Default to **single-agent**.
- Choose **multi-agent** only if specialization clearly improves outcomes.
- Multi-agent adds complexity, tracing challenges, latency, and governance burden.

## 6) RAG essentials
- Ingestion quality matters as much as model quality.
- Use chunking, metadata, ACL tagging, embeddings, indexing, retrieval, reranking, citations.
- Prefer hybrid retrieval over vector-only retrieval in enterprise settings.
- Measure retrieval quality, not just answer fluency.

## 7) Fine-tuning vs prompting vs RAG
- **Prompting**: First lever for behavior shaping.
- **RAG**: First lever for knowledge grounding.
- **Fine-tuning**: Use for repeated task/style adaptation, not live enterprise knowledge.

## 8) Production guardrails
- Prompt guardrails
- Retrieval source controls
- Tool permission limits
- Output policy checks
- Human approval where needed
- Fallback paths for uncertain responses

## 9) When not to use LLMs
- Exact calculations
- Regulatory logic
- Stable rule engines
- High-volume simple workflows
- Scenarios with near-zero hallucination tolerance unless strong validation exists

## 10) Enterprise AI risk categories
- Privacy risk
- Security risk
- Accuracy risk
- Compliance/legal risk
- Bias/fairness risk
- Operational risk
- Governance risk
- Reputational risk

## 11) Security principles
- Least privilege for tool use
- Identity-aware retrieval and action execution
- Secret isolation and managed identity
- Private networking when sensitivity demands it
- Prompt injection defenses
- Output filtering and audit logging

## 12) Observability signals
- Prompt and response trace
- Retrieval hit quality
- Reranker effectiveness
- Tool call success/failure
- Latency per stage
- Token/cost usage
- User feedback
- Policy violation rate
- Fallback frequency

## 13) POC vs pilot vs production
- **POC**: Can it work?
- **Pilot**: Does it deliver value with real users?
- **Production**: Is it secure, governed, supported, scalable, and measurable?

## 14) Model selection lens
Choose based on:
- Task fit
- Quality
- Latency
- Cost
- Context needs
- Tool support
- Governance requirements
- Deployment constraints

## 15) Cost optimization levers
- Use the smallest capable model
- Reduce token bloat
- Improve retrieval precision
- Cache repeatable outputs
- Use routing for simple vs complex tasks
- Limit unnecessary conversation history

## 16) Architecture patterns to mention in interviews
- Knowledge copilot with RAG
- Workflow agent with approval gates
- AI enrichment pipeline for document processing
- Support assistant with tool calling
- Multi-model routing architecture
- Human-in-the-loop risk review pattern

## 17) Business framing lines
- “I choose the lightest architecture that safely solves the business problem.”
- “I do not use LLMs where deterministic systems are better.”
- “Enterprise AI success depends more on grounding, controls, and adoption than on the model alone.”
- “I start with use-case value and operational sustainability, not with model excitement.”

## 18) Interview-ready tradeoffs
- Accuracy vs speed
- Cost vs quality
- Flexibility vs governance
- Autonomy vs control
- Centralized platform vs team-level agility
- Fine-tuning vs retrieval freshness
- Public service convenience vs private deployment control

## 19) Strong closing answer
> My architecture approach is to first classify the problem correctly, then select the simplest safe solution. I use automation for deterministic workflows, ML for prediction, GenAI for unstructured reasoning, and RAG when enterprise knowledge grounding is required. I start with copilots before agents, single-agent before multi-agent, and I design security, governance, fallback, and observability from the beginning.

## 20) What interviewers want to hear
- Clear decision-making, not buzzwords
- Awareness of production failure modes
- Risk and governance thinking
- Business value orientation
- Real tradeoff thinking
- Simplicity over unnecessary complexity
