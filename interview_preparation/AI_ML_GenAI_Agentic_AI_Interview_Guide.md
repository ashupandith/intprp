# AI/ML, GenAI & Agentic AI – Complete Interview Preparation Guide

---

> **⚠️ Accuracy & Freshness Notice (Last reviewed: June 2026)**
> 
> | Area | Status | Action Needed |
> |------|--------|---------------|
> | Core AI/ML theory (Transformers, RAG, Agents) | ✅ Stable | None |
> | Python code patterns (FastAPI, Pydantic) | ✅ Stable | None |
> | LangChain / LangGraph code | ⚠️ APIs change frequently | Verify against latest docs before interview |
> | Cloud pricing (Azure/AWS/GCP) | ⚠️ Outdated within weeks | Check provider pricing pages |
> | Estimation tables (person-days) | ℹ️ Directional only | Adjust for your team size, domain, and complexity |
> | Synaptica project details | ✅ Sourced from repo docs | Internal implementation details are inferred from architecture docs |
>
> **Recommendation**: For framework-specific code (LangChain, LangGraph, CrewAI), always cross-check syntax against the latest stable release before using in an interview whiteboard.

---

## Table of Contents

1. [Python + AI/ML Frameworks](#1-python--aiml-frameworks)
2. [Generative AI / LLM Applications](#2-generative-ai--llm-applications)
3. [Agentic AI & Orchestration Frameworks](#3-agentic-ai--orchestration-frameworks)
4. [RAG Systems (Retrieval-Augmented Generation)](#4-rag-systems-retrieval-augmented-generation)
5. [AI Agents & Copilots](#5-ai-agents--copilots)
6. [Conversational AI](#6-conversational-ai)
7. [LLMOps – Deployment, Monitoring, Evaluation & Optimisation](#7-llmops--deployment-monitoring-evaluation--optimisation)
8. [Cloud AI Stack – Azure / AWS / GCP](#8-cloud-ai-stack--azure--aws--gcp)
9. [APIs & Microservices](#9-apis--microservices)
10. [Data Integration](#10-data-integration)
11. [Prompt Engineering & Orchestration](#11-prompt-engineering--orchestration)
12. [Multi-Agent Systems & Guardrails](#12-multi-agent-systems--guardrails)
13. [Presales, Solutioning & Client Management](#13-presales-solutioning--client-management)
14. [End-to-End Delivery: POC → MVP → Production](#14-end-to-end-delivery-poc--mvp--production)
15. [Architecture, Design Patterns & Best Practices](#15-architecture-design-patterns--best-practices)
16. [Project Deep-Dive: Synaptica – Full-Stack AI Platform (GSK MSAT Quality)](#16-project-deep-dive-synaptica--full-stack-ai-platform-gsk-msat-quality)

---

## 1. Python + AI/ML Frameworks

### Detailed Explanation

Python is the foundational language for AI/ML development due to its rich ecosystem, readability, and community support. The key frameworks include:

| Category | Frameworks |
|----------|-----------|
| Classical ML | scikit-learn, XGBoost, LightGBM, CatBoost |
| Deep Learning | PyTorch, TensorFlow, Keras, JAX |
| NLP | Hugging Face Transformers, spaCy, NLTK |
| GenAI/LLM | LangChain, LlamaIndex, Semantic Kernel, Haystack |
| Data Processing | Pandas, NumPy, Polars, Dask |
| MLOps | MLflow, Weights & Biases, DVC, Kubeflow |
| Serving | FastAPI, Flask, BentoML, TorchServe, vLLM |

### Key Concepts

- **Model Training Pipeline**: Data ingestion → Preprocessing → Feature engineering → Model training → Evaluation → Deployment
- **Transfer Learning**: Using pre-trained models (BERT, GPT, ResNet) and fine-tuning for specific tasks
- **Distributed Training**: Using frameworks like DeepSpeed, FSDP, Horovod for training large models
- **Model Serialization**: ONNX, TorchScript, SavedModel formats for portability

---

### Questions & Answers

**Q1: How would you design an end-to-end ML pipeline for a production system?**

**Answer:**
An end-to-end ML pipeline for production involves multiple stages:

```
Data Sources → Ingestion → Validation → Preprocessing → Feature Store →
Training → Evaluation → Registry → Deployment → Monitoring → Retraining
```

**Detailed breakdown:**

1. **Data Ingestion Layer**: Use Apache Kafka/Spark for streaming or batch data collection. Implement data contracts and schema validation.

2. **Data Validation**: Use Great Expectations or TensorFlow Data Validation (TFDV) to check for data drift, missing values, schema violations.

3. **Feature Engineering & Store**: Build reusable feature pipelines with Feast or Tecton. This ensures training-serving consistency.

4. **Training Pipeline**: 
   - Use experiment tracking (MLflow/W&B)
   - Implement hyperparameter tuning (Optuna, Ray Tune)
   - Version datasets and code together (DVC)

5. **Model Evaluation**: 
   - Define business-relevant metrics beyond accuracy (precision@k, NDCG, latency)
   - A/B testing framework integration
   - Shadow deployment for comparison

6. **Model Registry & Versioning**: MLflow Model Registry with stage transitions (Staging → Production → Archived)

7. **Deployment**: 
   - Containerize with Docker
   - Serve via Kubernetes (KServe) or serverless (AWS Lambda, Azure Functions)
   - Implement canary/blue-green deployments

8. **Monitoring**: 
   - Model performance degradation detection
   - Data drift monitoring (Evidently AI, Alibi Detect)
   - Infrastructure monitoring (Prometheus, Grafana)

9. **Retraining Triggers**: Automated retraining based on performance thresholds or scheduled intervals.

---

**Q2: Explain the difference between PyTorch and TensorFlow. When would you choose one over the other?**

**Answer:**

| Aspect | PyTorch | TensorFlow |
|--------|---------|------------|
| Computation Graph | Dynamic (define-by-run) | Static (define-then-run) with eager mode |
| Debugging | Easier (native Python debugger) | Historically harder, improved with TF2 |
| Research | Preferred in academia/research | More production-oriented |
| Deployment | TorchServe, ONNX, TorchScript | TF Serving, TFLite, TF.js |
| Distributed | DistributedDataParallel, FSDP | tf.distribute.Strategy |
| Ecosystem | Hugging Face native support | Keras, TFX pipeline |

**When to choose PyTorch:**
- Rapid prototyping and research
- Working with Hugging Face models (native PyTorch)
- Need dynamic computation graphs (variable-length sequences, tree structures)
- Team prefers Pythonic code

**When to choose TensorFlow:**
- Need mobile/edge deployment (TFLite)
- Browser-based inference (TF.js)
- Enterprise production with TFX pipeline
- Google Cloud TPU optimization needed

**In GenAI context**: PyTorch dominates because most LLMs (LLaMA, Mistral, Falcon) are PyTorch-native, and Hugging Face Transformers primarily targets PyTorch.

---

**Q3: How do you handle model versioning and reproducibility in a team environment?**

**Answer:**

Reproducibility requires versioning across four dimensions:

1. **Code Versioning**: Git with branching strategy (feature branches, release tags)

2. **Data Versioning**: 
   - DVC (Data Version Control) for large datasets
   - Delta Lake for versioned data lakes
   - Immutable snapshots with timestamps

3. **Environment Versioning**:
   - Docker containers with pinned dependencies
   - `requirements.txt` with exact versions or Poetry lock files
   - Conda environment YAML exports

4. **Experiment Tracking**:
   ```python
   import mlflow
   
   with mlflow.start_run():
       mlflow.log_params({"lr": 0.001, "epochs": 50, "batch_size": 32})
       mlflow.log_metrics({"accuracy": 0.95, "f1": 0.92})
       mlflow.log_artifact("model.pkl")
       mlflow.set_tag("git_commit", get_git_hash())
   ```

5. **Model Registry**: Central catalog with metadata, lineage, and stage management

6. **Random Seed Management**: Set seeds for Python, NumPy, PyTorch, and CUDA:
   ```python
   import random, numpy as np, torch
   
   def set_seed(seed=42):
       random.seed(seed)
       np.random.seed(seed)
       torch.manual_seed(seed)
       torch.cuda.manual_seed_all(seed)
       torch.backends.cudnn.deterministic = True
   ```

---

**Q4: What are Python design patterns you commonly use in ML projects?**

**Answer:**

1. **Strategy Pattern** – Swappable algorithms:
   ```python
   class ModelStrategy(ABC):
       @abstractmethod
       def train(self, X, y): pass
       @abstractmethod
       def predict(self, X): pass
   
   class XGBoostStrategy(ModelStrategy):
       def train(self, X, y):
           self.model = xgb.XGBClassifier().fit(X, y)
   ```

2. **Factory Pattern** – Dynamic model/component creation:
   ```python
   class ModelFactory:
       _registry = {}
       
       @classmethod
       def register(cls, name):
           def decorator(model_cls):
               cls._registry[name] = model_cls
               return model_cls
           return decorator
       
       @classmethod
       def create(cls, name, **kwargs):
           return cls._registry[name](**kwargs)
   ```

3. **Pipeline Pattern** – Sequential transformations (scikit-learn Pipeline)

4. **Observer Pattern** – Callbacks for training events (early stopping, checkpointing)

5. **Singleton Pattern** – Model loading (load once, serve many):
   ```python
   class ModelSingleton:
       _instance = None
       
       @classmethod
       def get_model(cls):
           if cls._instance is None:
               cls._instance = cls._load_model()
           return cls._instance
   ```

6. **Decorator Pattern** – Adding caching, logging, retry logic to inference functions

---

## 2. Generative AI / LLM Applications

### Detailed Explanation

Generative AI refers to AI systems that create new content (text, images, code, audio) by learning patterns from training data. Large Language Models (LLMs) are the backbone of text-based generative AI.

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Transformer Architecture** | Self-attention mechanism enabling parallel processing of sequences |
| **Pre-training** | Unsupervised learning on massive corpora (next-token prediction, masked language modeling) |
| **Fine-tuning** | Adapting pre-trained models to specific tasks/domains |
| **RLHF** | Reinforcement Learning from Human Feedback for alignment |
| **Tokenization** | BPE, WordPiece, SentencePiece for text → tokens |
| **Context Window** | Maximum tokens a model can process (4K → 128K → 1M+) |
| **Temperature** | Controls randomness in generation (0 = deterministic, 1+ = creative) |
| **Top-p/Top-k** | Nucleus sampling and top-k filtering for controlled generation |
| **Embeddings** | Dense vector representations of text for similarity/search |

### LLM Application Patterns

```
┌─────────────────────────────────────────────────────┐
│                  LLM Application Stack                │
├─────────────────────────────────────────────────────┤
│  UI Layer        │ Chat, Dashboard, API Gateway      │
│  Orchestration   │ LangChain, Semantic Kernel        │
│  Memory/State    │ Conversation buffer, summaries    │
│  Retrieval       │ RAG, Vector DB, Knowledge Graph   │
│  LLM Engine      │ GPT-4, Claude, LLaMA, Mistral    │
│  Guardrails      │ Content filtering, PII detection  │
│  Observability   │ Tracing, eval, cost tracking      │
└─────────────────────────────────────────────────────┘
```

---

### Questions & Answers

**Q1: Explain the Transformer architecture and why it revolutionized NLP.**

**Answer:**

The Transformer (Vaswani et al., 2017 – "Attention Is All You Need") replaced sequential RNN/LSTM processing with parallel self-attention:

**Core Components:**

1. **Self-Attention Mechanism**:
   - For each token, compute attention scores with all other tokens
   - $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
   - Q (Query), K (Key), V (Value) are learned projections
   - Enables capturing long-range dependencies in O(1) layers

2. **Multi-Head Attention**:
   - Multiple attention heads capture different relationship types
   - $\text{MultiHead}(Q,K,V) = \text{Concat}(head_1,...,head_h)W^O$
   - Each head learns different aspects (syntax, semantics, co-reference)

3. **Positional Encoding**:
   - Since attention is permutation-invariant, positional info is injected
   - Original: sinusoidal; Modern: RoPE (Rotary Position Embeddings), ALiBi

4. **Feed-Forward Networks**: Position-wise FFN after attention layers

5. **Layer Normalization & Residual Connections**: Enable training deep networks

**Why Revolutionary:**
- **Parallelization**: Unlike RNNs, all positions processed simultaneously (GPU-friendly)
- **Long-range dependencies**: Direct attention between any two positions
- **Scalability**: Scales to billions of parameters effectively
- **Transfer Learning**: Pre-train once, fine-tune for many tasks

**Variants:**
- **Encoder-only**: BERT (bidirectional, classification/NER)
- **Decoder-only**: GPT (autoregressive, generation)
- **Encoder-Decoder**: T5, BART (seq2seq, translation, summarization)

---

**Q2: What are the different approaches to customizing LLMs for enterprise use?**

**Answer:**

From least to most resource-intensive:

| Approach | Effort | Data Needed | Cost | Use Case |
|----------|--------|-------------|------|----------|
| Prompt Engineering | Low | None | $ | Quick customization |
| Few-shot Learning | Low | 5-50 examples | $ | Task demonstration |
| RAG | Medium | Documents | $$ | Knowledge-grounded answers |
| Fine-tuning (LoRA/QLoRA) | Medium | 1K-100K examples | $$$ | Domain adaptation |
| Full Fine-tuning | High | 100K+ examples | $$$$ | Significant behavior change |
| Pre-training from scratch | Very High | Billions of tokens | $$$$$ | New domain/language |

**Detailed Approaches:**

1. **Prompt Engineering**:
   - System prompts, instructions, output formatting
   - Chain-of-thought (CoT), Tree-of-thought (ToT)
   - Few-shot examples within context

2. **RAG (Retrieval-Augmented Generation)**:
   - Retrieve relevant context from external knowledge
   - No model weight changes needed
   - Always up-to-date with latest data

3. **Parameter-Efficient Fine-Tuning (PEFT)**:
   ```python
   from peft import LoraConfig, get_peft_model
   
   config = LoraConfig(
       r=16,                    # Low-rank dimension
       lora_alpha=32,           # Scaling factor
       target_modules=["q_proj", "v_proj"],
       lora_dropout=0.05,
       task_type="CAUSAL_LM"
   )
   model = get_peft_model(base_model, config)
   # Trainable params: ~0.1% of total
   ```

4. **Full Fine-tuning**:
   - Update all model weights
   - Requires significant compute (multi-GPU/TPU)
   - Risk of catastrophic forgetting

5. **RLHF/DPO (Direct Preference Optimization)**:
   - Align model outputs with human preferences
   - DPO simplifies RLHF by eliminating reward model:
   ```python
   # DPO Loss
   loss = -log(sigmoid(beta * (log_prob_chosen - log_prob_rejected)))
   ```

---

**Q3: How do you evaluate LLM outputs? What metrics do you use?**

**Answer:**

LLM evaluation is multi-dimensional:

**1. Automated Metrics:**

| Metric | What it Measures | Limitations |
|--------|-----------------|-------------|
| BLEU | N-gram overlap with reference | Doesn't capture semantics |
| ROUGE | Recall of reference n-grams | Same as BLEU |
| BERTScore | Semantic similarity via embeddings | Expensive, model-dependent |
| Perplexity | Model confidence | Doesn't correlate with quality |
| METEOR | Considers synonyms, stemming | Still surface-level |

**2. LLM-as-Judge:**
```python
evaluation_prompt = """
Rate the following response on a scale of 1-5 for:
- Relevance: Does it answer the question?
- Accuracy: Is the information correct?
- Completeness: Does it cover all aspects?
- Coherence: Is it well-structured?

Question: {question}
Response: {response}
Reference: {reference}

Provide scores and justification for each criterion.
"""
```

**3. Task-Specific Evaluation:**
- **Factuality**: Cross-reference with ground truth, hallucination detection
- **Toxicity**: Perspective API, custom classifiers
- **Bias**: Demographic parity, equalized odds across groups
- **Faithfulness (RAG)**: Does answer align with retrieved context?
- **Latency**: Time-to-first-token (TTFT), tokens-per-second (TPS)
- **Cost**: $/1K tokens, total cost per query

**4. Human Evaluation:**
- Elo ranking (Chatbot Arena style)
- Side-by-side comparison (A/B testing)
- Rubric-based scoring by domain experts

**5. Evaluation Frameworks:**
- RAGAS (for RAG: faithfulness, answer relevancy, context precision/recall)
- DeepEval, Promptfoo, LangSmith evaluators
- Custom evaluation pipelines with test suites

---

**Q4: Explain tokenization in LLMs. Why does it matter?**

**Answer:**

Tokenization converts text into numerical tokens that models can process.

**Methods:**
1. **BPE (Byte Pair Encoding)**: GPT models – iteratively merge frequent character pairs
2. **WordPiece**: BERT – similar to BPE but uses likelihood-based merging
3. **SentencePiece**: Language-agnostic, treats text as raw byte stream
4. **Tiktoken**: OpenAI's fast BPE implementation

**Why It Matters:**

1. **Context Window Utilization**: Inefficient tokenization wastes context space
   - "indescribable" might be 1 token or 4 sub-tokens depending on vocabulary
   
2. **Cost**: API pricing is per-token; fewer tokens = lower cost

3. **Multilingual Performance**: Some tokenizers fragment non-English text heavily
   - English: "Hello" = 1 token
   - Hindi: "नमस्ते" = 3-5 tokens (inefficient)

4. **Code Understanding**: Tokenizers trained on code handle programming syntax better

5. **Special Tokens**: `[CLS]`, `[SEP]`, `<|endoftext|>`, `<tool_call>` guide model behavior

**Practical Impact:**
```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
text = "Artificial Intelligence is transforming industries"
tokens = enc.encode(text)
print(f"Text: {text}")
print(f"Tokens: {tokens}")  # [9470, 22107, 374, 46890, 19647]
print(f"Token count: {len(tokens)}")  # 5
```

---

**Q5: What is the difference between fine-tuning, RLHF, and DPO?**

**Answer:**

| Aspect | Fine-tuning (SFT) | RLHF | DPO |
|--------|-------------------|------|-----|
| **Goal** | Learn task/domain patterns | Align with preferences | Align with preferences |
| **Data** | (input, output) pairs | (input, chosen, rejected) + reward model | (input, chosen, rejected) |
| **Process** | Supervised learning | Train reward model → PPO optimization | Direct preference optimization |
| **Complexity** | Low | High (4 models in memory) | Medium (reference + policy model) |
| **Stability** | Stable | Can be unstable (reward hacking) | More stable than RLHF |
| **Cost** | $$ | $$$$ | $$$ |

**Pipeline:**
```
Pre-trained Model → SFT (instruction following) → RLHF/DPO (alignment) → Deployed Model
```

**SFT (Supervised Fine-Tuning):**
- Train on instruction-response pairs
- Model learns to follow instructions and generate formatted outputs
- Risk: Overfitting to training distribution

**RLHF:**
1. Collect human preference data (A vs B rankings)
2. Train reward model on preferences
3. Optimize policy (LLM) using PPO to maximize reward
4. Problem: Reward model can be gamed (reward hacking)

**DPO (Direct Preference Optimization):**
- Eliminates reward model entirely
- Directly optimizes the policy using preference pairs
- Loss function implicitly defines the reward:
  $\mathcal{L}_{DPO} = -\mathbb{E}\left[\log\sigma\left(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]$

---

## 3. Agentic AI & Orchestration Frameworks

### Detailed Explanation

Agentic AI refers to AI systems that can autonomously plan, reason, execute actions, and adapt based on feedback. Unlike simple LLM calls, agents have:

- **Autonomy**: Make decisions without human intervention
- **Tool Use**: Interact with external tools, APIs, databases
- **Planning**: Break complex tasks into sub-tasks
- **Memory**: Maintain context across interactions
- **Reasoning**: Apply logic to solve multi-step problems

### Agent Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                        AGENT SYSTEM                             │
├───────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌──────────────┐    ┌─────────────────┐  │
│  │   PLANNER   │───▶│   EXECUTOR   │───▶│   EVALUATOR     │  │
│  │  (Reasoning)│    │  (Tool Use)  │    │  (Self-check)   │  │
│  └─────────────┘    └──────────────┘    └─────────────────┘  │
│         │                    │                    │             │
│         ▼                    ▼                    ▼             │
│  ┌─────────────┐    ┌──────────────┐    ┌─────────────────┐  │
│  │   MEMORY    │    │    TOOLS     │    │   GUARDRAILS    │  │
│  │ Short/Long  │    │ APIs, DBs,   │    │ Safety, Limits  │  │
│  │   term      │    │ Functions    │    │ Validation      │  │
│  └─────────────┘    └──────────────┘    └─────────────────┘  │
│                                                                 │
└───────────────────────────────────────────────────────────────┘
```

### Orchestration Frameworks Comparison

| Framework | Creator | Strengths | Use Case |
|-----------|---------|-----------|----------|
| **LangChain/LangGraph** | LangChain Inc | Flexible, large ecosystem | Complex workflows |
| **Semantic Kernel** | Microsoft | .NET/Python, enterprise-ready | Microsoft stack |
| **AutoGen** | Microsoft | Multi-agent conversations | Research, collaboration |
| **CrewAI** | CrewAI | Role-based agents, simple | Team simulations |
| **Haystack** | deepset | Production pipelines | Search & RAG |
| **OpenAI Assistants** | OpenAI | Managed, easy to use | Quick prototypes |
| **Amazon Bedrock Agents** | AWS | Managed, AWS integrated | Enterprise AWS |

---

### Questions & Answers

**Q1: Design an AI agent system for a customer support use case. Explain the architecture.**

**Answer:**

**System Architecture:**

```
Customer Query
      │
      ▼
┌─────────────────┐
│  ROUTER AGENT   │ ← Classifies intent, routes to specialist
└────────┬────────┘
         │
    ┌────┼────┬────────────┐
    ▼    ▼    ▼            ▼
┌──────┐┌──────┐┌────────┐┌──────────┐
│FAQ   ││Order ││Technical││Escalation│
│Agent ││Agent ││Support  ││Agent     │
└──┬───┘└──┬───┘└───┬────┘└────┬─────┘
   │       │        │          │
   ▼       ▼        ▼          ▼
┌──────────────────────────────────────┐
│            TOOL LAYER                 │
│  Knowledge Base │ Order DB │ CRM     │
│  Product Docs   │ Shipping │ Ticketing│
└──────────────────────────────────────┘
```

**Component Details:**

1. **Router Agent**:
   - Intent classification using LLM or lightweight classifier
   - Routes to appropriate specialist agent
   - Handles multi-turn conversation state

2. **FAQ Agent**:
   - RAG-based retrieval from knowledge base
   - Answers common questions without human intervention
   - Confidence threshold for escalation

3. **Order Agent**:
   - Tools: Order lookup API, shipping tracker, refund processor
   - Can check status, initiate returns, apply discounts
   - Business rule validation before actions

4. **Technical Support Agent**:
   - Diagnostic tree traversal
   - Integration with product documentation
   - Can create support tickets, schedule callbacks

5. **Escalation Agent**:
   - Triggered when confidence is low or customer is frustrated
   - Sentiment analysis for frustration detection
   - Smooth handoff to human agent with full context

**Implementation with LangGraph:**

> ⚠️ *LangGraph APIs evolve rapidly. The pattern below reflects the stable `StateGraph` approach. Verify against [langgraph docs](https://langchain-ai.github.io/langgraph/) for latest syntax.*

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Literal

class AgentState(TypedDict):
    messages: list
    intent: str
    confidence: float
    tools_used: list
    escalate: bool

def router(state: AgentState) -> AgentState:
    """Classify intent and confidence"""
    intent, confidence = classify_intent(state["messages"][-1])
    return {**state, "intent": intent, "confidence": confidence}

def route_decision(state: AgentState) -> Literal["faq", "orders", "technical", "escalation"]:
    """Routing function — returns the next node name"""
    if state["confidence"] < 0.7 or state["escalate"]:
        return "escalation"
    return state["intent"]

# Build graph
workflow = StateGraph(AgentState)
workflow.add_node("router", router)
workflow.add_node("faq", faq_agent)
workflow.add_node("orders", order_agent)
workflow.add_node("technical", tech_agent)
workflow.add_node("escalation", escalation_agent)

# Set entry point and conditional routing
workflow.set_entry_point("router")
workflow.add_conditional_edges("router", route_decision, {
    "faq": "faq",
    "orders": "orders",
    "technical": "technical",
    "escalation": "escalation"
})

# Terminal edges — each specialist ends the graph
workflow.add_edge("faq", END)
workflow.add_edge("orders", END)
workflow.add_edge("technical", END)
workflow.add_edge("escalation", END)

app = workflow.compile()
```

**Key Design Decisions:**
- **Memory**: Redis for session state, PostgreSQL for conversation history
- **Guardrails**: Input/output validation, PII masking, action confirmation
- **Observability**: LangSmith for tracing, custom metrics dashboard
- **Fallback**: Always have human escalation path

---

**Q2: What is the ReAct (Reasoning + Acting) pattern? How does it work?**

**Answer:**

ReAct combines reasoning (Chain-of-Thought) with action (tool use) in an interleaved manner:

```
Thought → Action → Observation → Thought → Action → Observation → ... → Final Answer
```

**The Loop:**

1. **Thought**: Model reasons about what to do next
2. **Action**: Model selects and executes a tool
3. **Observation**: Tool returns result
4. **Repeat**: Until sufficient information gathered

**Example Trace:**

```
User: What is the current stock price of the company that acquired Twitter?

Thought: I need to find which company acquired Twitter, then look up its stock price.

Action: search("company that acquired Twitter")
Observation: Elon Musk acquired Twitter (now X) through his company in 2022. 
             Twitter is now owned by X Corp, but Elon Musk's publicly traded 
             company is Tesla (TSLA).

Thought: The user likely means the publicly traded entity associated with the 
         acquisition. Tesla is Musk's public company. Let me get Tesla's stock price.

Action: get_stock_price("TSLA")
Observation: Tesla (TSLA) current price: $248.52, change: +2.3%

Thought: I have enough information to answer.
Final Answer: Twitter was acquired by Elon Musk. His publicly traded company, 
             Tesla (TSLA), currently trades at $248.52 (+2.3%).
```

**Implementation:**

> ⚠️ *LangChain agent APIs have changed significantly across versions. Below shows the modern `create_react_agent` approach (LangChain ≥0.2). For older versions, the import path and function signature differ.*

```python
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

# Modern approach: tools as decorated functions
@tool
def search_web(query: str) -> str:
    """Search the web for current information."""
    return search_api.search(query)

@tool
def calculator(expression: str) -> str:
    """Perform mathematical calculations."""
    return str(eval(expression))  # simplified

@tool
def get_stock_price(ticker: str) -> str:
    """Get current stock price by ticker symbol."""
    return stock_api.get_price(ticker)

tools = [search_web, calculator, get_stock_price]

# Create ReAct agent (LangGraph-based, recommended approach)
llm = ChatOpenAI(model="gpt-4o")
agent = create_react_agent(llm, tools)

# Execute
result = agent.invoke({"messages": [{"role": "user", "content": "What is Tesla's stock price?"}]})
```

**Advantages:**
- Interpretable (can trace reasoning)
- Reduces hallucination (grounded in tool outputs)
- Flexible (works with any tool combination)

**Limitations:**
- Can get stuck in loops
- Expensive (multiple LLM calls)
- Sensitive to prompt format

---

**Q3: Compare LangChain, LangGraph, Semantic Kernel, and AutoGen. When would you use each?**

**Answer:**

| Feature | LangChain | LangGraph | Semantic Kernel | AutoGen |
|---------|-----------|-----------|-----------------|---------|
| **Paradigm** | Chains/Pipelines | State machines/Graphs | Plugins/Planners | Multi-agent chat |
| **Complexity** | Medium | High | Medium | Medium |
| **State Management** | Limited | Built-in (graph state) | Kernel memory | Conversation history |
| **Human-in-loop** | Manual | Native support | Native support | Built-in |
| **Multi-agent** | Basic | Excellent | Basic | Excellent |
| **Enterprise** | Community | Community + Enterprise | Enterprise (MS) | Research |
| **Language** | Python, JS | Python, JS | Python, C#, Java | Python, .NET |

**When to Use Each:**

**LangChain**: Simple chains – prompt → LLM → parse → tool → LLM
- Quick prototypes, straightforward pipelines
- Rich tool/integration ecosystem
- Simple RAG implementations

**LangGraph**: Complex workflows with cycles, conditionals, parallel execution
- Multi-step agents with retry logic
- Workflows requiring human approval gates
- Stateful, long-running processes
- Production agentic systems

**Semantic Kernel**: Microsoft ecosystem, enterprise applications
- Azure OpenAI integration
- .NET-based applications
- Plugin architecture for modular AI features
- When you need memory + planning + plugins together

**AutoGen**: Multi-agent collaboration and research
- Agent-to-agent conversations
- Code generation + execution workflows
- Research and experimentation
- When agents need to debate/collaborate

**Example Architecture Decision:**

For a production enterprise system:
```
User Interface → API Gateway → LangGraph (orchestration) 
    → Multiple specialist agents (each using LangChain internally)
    → Tools (APIs, Databases, Vector Stores)
    → Guardrails + Monitoring (LangSmith)
```

---

**Q4: How do you implement memory in AI agents? What are the different types?**

**Answer:**

Memory enables agents to maintain context across interactions:

**Types of Memory:**

```
┌─────────────────────────────────────────────┐
│              AGENT MEMORY SYSTEM              │
├─────────────────────────────────────────────┤
│                                               │
│  ┌─────────────────────────────────────┐    │
│  │  SHORT-TERM MEMORY                   │    │
│  │  • Conversation buffer (last N msgs) │    │
│  │  • Working memory (current task)     │    │
│  │  • Token window management           │    │
│  └─────────────────────────────────────┘    │
│                                               │
│  ┌─────────────────────────────────────┐    │
│  │  LONG-TERM MEMORY                    │    │
│  │  • Vector store (semantic search)    │    │
│  │  • Knowledge graph (relationships)   │    │
│  │  • Structured DB (facts, preferences)│    │
│  └─────────────────────────────────────┘    │
│                                               │
│  ┌─────────────────────────────────────┐    │
│  │  EPISODIC MEMORY                     │    │
│  │  • Past interactions summary         │    │
│  │  • Successful strategies             │    │
│  │  • Lessons learned                   │    │
│  └─────────────────────────────────────┘    │
│                                               │
│  ┌─────────────────────────────────────┐    │
│  │  PROCEDURAL MEMORY                   │    │
│  │  • Tool usage patterns               │    │
│  │  • Workflow templates                 │    │
│  │  • Learned procedures                │    │
│  └─────────────────────────────────────┘    │
│                                               │
└─────────────────────────────────────────────┘
```

**Implementation Strategies:**

1. **Conversation Buffer** (Simple, limited):
   ```python
   class ConversationBufferMemory:
       def __init__(self, max_messages=20):
           self.messages = deque(maxlen=max_messages)
       
       def add(self, role, content):
           self.messages.append({"role": role, "content": content})
       
       def get_context(self):
           return list(self.messages)
   ```

2. **Summary Memory** (Compressed history):
   ```python
   class SummaryMemory:
       def __init__(self, llm):
           self.llm = llm
           self.summary = ""
           self.recent_messages = []
       
       def add(self, message):
           self.recent_messages.append(message)
           if len(self.recent_messages) > 10:
               self.summary = self.llm.summarize(
                   self.summary + "\n" + format_messages(self.recent_messages[:5])
               )
               self.recent_messages = self.recent_messages[5:]
   ```

3. **Vector-based Long-term Memory**:
   ```python
   class SemanticMemory:
       def __init__(self, embedding_model, vector_store):
           self.embedder = embedding_model
           self.store = vector_store
       
       def store_memory(self, text, metadata):
           embedding = self.embedder.encode(text)
           self.store.upsert(embedding, text, metadata)
       
       def recall(self, query, top_k=5):
           query_embedding = self.embedder.encode(query)
           return self.store.search(query_embedding, top_k)
   ```

4. **Hybrid Memory System**:
   ```python
   class HybridMemory:
       def __init__(self):
           self.buffer = ConversationBufferMemory(max_messages=10)
           self.summary = SummaryMemory(llm)
           self.semantic = SemanticMemory(embedder, vector_store)
           self.entity_store = EntityMemory()  # Track key entities
       
       def get_relevant_context(self, query):
           return {
               "recent": self.buffer.get_context(),
               "summary": self.summary.get_summary(),
               "relevant_memories": self.semantic.recall(query),
               "entities": self.entity_store.get_relevant(query)
           }
   ```

---

**Q5: What are the common failure modes of AI agents and how do you handle them?**

**Answer:**

| Failure Mode | Description | Mitigation |
|-------------|-------------|------------|
| **Infinite Loops** | Agent repeats same action | Max iteration limit, loop detection |
| **Hallucinated Actions** | Agent invents non-existent tools | Strict tool schema validation |
| **Context Overflow** | Exceeds token limit | Summarization, sliding window |
| **Wrong Tool Selection** | Uses inappropriate tool | Better tool descriptions, examples |
| **Error Cascading** | One failure breaks entire flow | Try-catch, fallback strategies |
| **Goal Drift** | Agent loses track of objective | Periodic goal re-evaluation |
| **Excessive Cost** | Too many LLM calls | Budget limits, caching |
| **Unsafe Actions** | Performs harmful operations | Confirmation gates, sandboxing |

**Comprehensive Mitigation Framework:**

```python
class RobustAgent:
    def __init__(self, max_iterations=10, max_cost=1.0, timeout=120):
        self.max_iterations = max_iterations
        self.max_cost = max_cost
        self.timeout = timeout
        self.iteration_count = 0
        self.total_cost = 0
        self.action_history = []
    
    async def execute(self, task):
        while self.iteration_count < self.max_iterations:
            # Check budget
            if self.total_cost > self.max_cost:
                return self.graceful_fallback("Budget exceeded")
            
            # Check for loops
            if self.detect_loop():
                return self.break_loop_strategy()
            
            # Get next action
            action = await self.plan_next_action(task)
            
            # Validate action (guardrails)
            if not self.validate_action(action):
                continue
            
            # Execute with timeout and error handling
            try:
                result = await asyncio.wait_for(
                    self.execute_action(action), 
                    timeout=self.timeout
                )
                self.action_history.append((action, result))
            except TimeoutError:
                result = "Action timed out"
            except Exception as e:
                result = f"Error: {str(e)}"
                if self.is_recoverable(e):
                    continue
                else:
                    return self.graceful_fallback(str(e))
            
            # Check if task complete
            if self.is_complete(result):
                return self.format_final_answer()
            
            self.iteration_count += 1
        
        return self.graceful_fallback("Max iterations reached")
    
    def detect_loop(self):
        if len(self.action_history) >= 3:
            last_3 = [a[0] for a in self.action_history[-3:]]
            return len(set(str(a) for a in last_3)) == 1
        return False
```

---

## 4. RAG Systems (Retrieval-Augmented Generation)

### Detailed Explanation

RAG combines the generative power of LLMs with the precision of information retrieval, grounding outputs in factual data.

### RAG Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      RAG PIPELINE                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  INDEXING (Offline)                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │  Ingest  │→ │  Chunk   │→ │  Embed   │→ │ Vector Store │   │
│  │ Documents│  │  Split   │  │  Encode  │  │  (Index)     │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │
│                                                                   │
│  RETRIEVAL (Online)                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │  Query   │→ │ Retrieve │→ │ Re-rank  │→ │  Augment     │   │
│  │  Encode  │  │  Top-K   │  │ Filter   │  │  Prompt      │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │
│                                                                   │
│  GENERATION                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │   LLM    │→ │ Validate │→ │ Response │                      │
│  │ Generate │  │ Ground   │  │  Return  │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Advanced RAG Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Naive RAG** | Basic retrieve + generate | Simple Q&A |
| **Advanced RAG** | Query rewriting + re-ranking | Production systems |
| **Modular RAG** | Pluggable components | Flexible architecture |
| **Self-RAG** | LLM decides when to retrieve | Adaptive retrieval |
| **Corrective RAG (CRAG)** | Validates retrieval quality | High-accuracy needs |
| **Graph RAG** | Knowledge graph + vector search | Complex relationships |
| **Agentic RAG** | Agent decides retrieval strategy | Multi-source queries |
| **Hybrid RAG** | Keyword + Semantic search | Diverse query types |

---

### Questions & Answers

**Q1: Design a production-grade RAG system. What are the key components and design decisions?**

**Answer:**

**Complete Production RAG Architecture:**

```python
class ProductionRAGSystem:
    """
    Production RAG with:
    - Hybrid search (dense + sparse)
    - Query transformation
    - Multi-stage retrieval
    - Re-ranking
    - Answer validation
    - Caching
    - Observability
    """
    
    def __init__(self):
        # Components
        self.embedder = SentenceTransformer("BAAI/bge-large-en-v1.5")
        self.sparse_encoder = BM25Encoder()
        self.vector_store = Qdrant(collection="documents")
        self.reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-12-v2")
        self.llm = AzureOpenAI(model="gpt-4")
        self.cache = Redis()
        
    async def answer(self, query: str, user_context: dict) -> RAGResponse:
        # 1. Check cache
        cached = await self.cache.get(self.cache_key(query))
        if cached:
            return cached
        
        # 2. Query Understanding & Transformation
        enhanced_queries = await self.transform_query(query)
        
        # 3. Hybrid Retrieval
        candidates = await self.hybrid_retrieve(enhanced_queries)
        
        # 4. Re-ranking
        ranked_docs = self.rerank(query, candidates)
        
        # 5. Context Assembly
        context = self.assemble_context(ranked_docs, max_tokens=3000)
        
        # 6. Generation with Citation
        response = await self.generate_with_citations(query, context)
        
        # 7. Validation
        validated = await self.validate_response(response, context)
        
        # 8. Cache & Return
        await self.cache.set(self.cache_key(query), validated, ttl=3600)
        return validated
```

**Key Design Decisions:**

1. **Chunking Strategy**:
   - Semantic chunking (split at natural boundaries)
   - Overlapping chunks (10-20% overlap)
   - Hierarchical: Document → Section → Paragraph → Sentence
   - Optimal size: 256-512 tokens for retrieval, larger for context
   ```python
   from langchain.text_splitter import RecursiveCharacterTextSplitter
   
   splitter = RecursiveCharacterTextSplitter(
       chunk_size=512,
       chunk_overlap=50,
       separators=["\n\n", "\n", ". ", " ", ""],
       length_function=tiktoken_len
   )
   ```

2. **Embedding Model Selection**:
   - Evaluate on MTEB benchmark for your domain
   - Consider: dimension size, speed, multilingual support
   - Options: OpenAI ada-002, BGE, E5, Cohere embed-v3

3. **Hybrid Search** (Dense + Sparse):
   ```python
   async def hybrid_retrieve(self, queries, alpha=0.7):
       dense_results = await self.vector_store.search(
           embedding=self.embedder.encode(queries[0]),
           top_k=20
       )
       sparse_results = await self.bm25_search(queries[0], top_k=20)
       
       # Reciprocal Rank Fusion
       combined = reciprocal_rank_fusion(
           [dense_results, sparse_results],
           weights=[alpha, 1-alpha]
       )
       return combined[:15]
   ```

4. **Re-ranking**: Cross-encoder re-ranking for precision
5. **Query Transformation**: HyDE, multi-query, step-back prompting
6. **Evaluation**: RAGAS metrics (faithfulness, relevancy, context precision)

---

**Q2: How do you handle the chunking problem in RAG? What strategies exist?**

**Answer:**

Chunking is critical because it directly impacts retrieval quality:

**Strategies:**

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| **Fixed-size** | Split every N tokens | Simple, predictable | Breaks context |
| **Recursive** | Split at boundaries (\n\n, \n, .) | Respects structure | May be uneven |
| **Semantic** | Split when embedding similarity drops | Meaning-preserving | Expensive |
| **Document-specific** | Markdown headers, code functions | Structure-aware | Needs parsers |
| **Sliding window** | Overlapping fixed chunks | Preserves boundaries | Redundant |
| **Parent-child** | Small chunks for retrieval, large for context | Best of both | Complex |
| **Propositions** | Extract atomic facts | Precise retrieval | Expensive |

**Advanced: Parent-Child (Small-to-Big) Strategy:**

```python
class ParentChildChunker:
    """
    Small chunks for precise retrieval,
    return parent (larger) chunk for context.
    """
    def __init__(self):
        self.parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
        self.child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
    
    def process(self, document):
        parent_chunks = self.parent_splitter.split(document)
        
        for parent in parent_chunks:
            parent_id = generate_id(parent)
            children = self.child_splitter.split(parent.text)
            
            for child in children:
                yield {
                    "text": child.text,
                    "parent_id": parent_id,
                    "parent_text": parent.text,  # Stored separately
                    "metadata": parent.metadata
                }
    
    def retrieve(self, query, top_k=5):
        # Search children (precise matching)
        child_results = self.vector_store.search(query, top_k=top_k*3)
        
        # Deduplicate by parent and return parent chunks
        seen_parents = set()
        results = []
        for child in child_results:
            if child.parent_id not in seen_parents:
                seen_parents.add(child.parent_id)
                results.append(self.get_parent(child.parent_id))
                if len(results) >= top_k:
                    break
        return results
```

**Semantic Chunking:**

```python
from sentence_transformers import SentenceTransformer
import numpy as np

def semantic_chunk(text, threshold=0.75):
    sentences = split_into_sentences(text)
    embeddings = model.encode(sentences)
    
    chunks = []
    current_chunk = [sentences[0]]
    
    for i in range(1, len(sentences)):
        similarity = cosine_similarity(embeddings[i-1], embeddings[i])
        
        if similarity < threshold:  # Topic change detected
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentences[i]]
        else:
            current_chunk.append(sentences[i])
    
    chunks.append(" ".join(current_chunk))
    return chunks
```

---

**Q3: What is Hybrid Search in RAG and why is it important?**

**Answer:**

Hybrid search combines dense (semantic) and sparse (keyword) retrieval:

**Why Both Are Needed:**

| Query Type | Dense (Semantic) | Sparse (BM25/Keyword) |
|-----------|-----------------|----------------------|
| "What causes climate change?" | ✅ Excellent | ⚠️ Okay |
| "Error code ERR_SSL_PROTOCOL_ERROR" | ❌ Poor | ✅ Excellent |
| "Python pandas groupby aggregate" | ⚠️ Okay | ✅ Good |
| "How to handle angry customers?" | ✅ Excellent | ❌ Poor |
| "Invoice #INV-2024-0892" | ❌ Poor | ✅ Excellent |

**Dense search** excels at semantic understanding but struggles with exact matches, acronyms, and rare terms.

**Sparse search** excels at exact matching but misses paraphrases and semantic similarity.

**Implementation:**

```python
from rank_bm25 import BM25Okapi
import numpy as np

class HybridSearcher:
    def __init__(self, documents, embedder, vector_store):
        # Dense
        self.embedder = embedder
        self.vector_store = vector_store
        
        # Sparse (BM25)
        tokenized_docs = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(tokenized_docs)
        self.documents = documents
    
    def search(self, query, top_k=10, alpha=0.7):
        # Dense retrieval
        query_embedding = self.embedder.encode(query)
        dense_results = self.vector_store.search(query_embedding, top_k=top_k*2)
        
        # Sparse retrieval
        tokenized_query = query.split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        sparse_top_k = np.argsort(bm25_scores)[-top_k*2:][::-1]
        sparse_results = [(self.documents[i], bm25_scores[i]) for i in sparse_top_k]
        
        # Reciprocal Rank Fusion (RRF)
        combined = self.reciprocal_rank_fusion(
            dense_results, sparse_results, 
            k=60, alpha=alpha
        )
        
        return combined[:top_k]
    
    def reciprocal_rank_fusion(self, *result_lists, k=60, alpha=0.7):
        scores = {}
        for weight, results in zip([alpha, 1-alpha], result_lists):
            for rank, (doc, _) in enumerate(results):
                doc_id = hash(doc)
                if doc_id not in scores:
                    scores[doc_id] = {"doc": doc, "score": 0}
                scores[doc_id]["score"] += weight * (1 / (k + rank + 1))
        
        return sorted(scores.values(), key=lambda x: x["score"], reverse=True)
```

**Vector Database Support for Hybrid:**
- **Qdrant**: Native hybrid with sparse vectors
- **Weaviate**: Built-in hybrid search
- **Pinecone**: Sparse-dense vectors
- **Elasticsearch**: Dense vectors + BM25

---

**Q4: How do you evaluate a RAG system? What metrics do you use?**

**Answer:**

**RAG Evaluation Framework (RAGAS-inspired):**

| Metric | What It Measures | Formula/Approach |
|--------|-----------------|-----------------|
| **Faithfulness** | Is answer grounded in context? | Claims in answer supported by context |
| **Answer Relevancy** | Does answer address the question? | Semantic similarity to question |
| **Context Precision** | Are retrieved docs relevant? | Relevant docs in top positions |
| **Context Recall** | Did we retrieve all needed info? | Coverage of ground truth |
| **Answer Correctness** | Is the answer factually correct? | Comparison to reference |
| **Hallucination Rate** | % of unsupported claims | Claims without context support |

**Implementation:**

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness, answer_relevancy,
    context_precision, context_recall
)
from datasets import Dataset

# Prepare evaluation dataset
eval_data = {
    "question": questions,
    "answer": generated_answers,
    "contexts": retrieved_contexts,
    "ground_truth": reference_answers
}

dataset = Dataset.from_dict(eval_data)
results = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)

print(results)
# {'faithfulness': 0.89, 'answer_relevancy': 0.92, 
#  'context_precision': 0.85, 'context_recall': 0.78}
```

**Custom Evaluation Pipeline:**

```python
class RAGEvaluator:
    def __init__(self, judge_llm):
        self.judge = judge_llm
    
    async def evaluate_faithfulness(self, answer, contexts):
        """Check if every claim in answer is supported by context"""
        prompt = f"""
        Given the context and answer, identify all claims in the answer 
        and check if each is supported by the context.
        
        Context: {contexts}
        Answer: {answer}
        
        For each claim, respond with:
        - Claim: [the claim]
        - Supported: [Yes/No]
        - Evidence: [supporting text from context or "None"]
        
        Then provide: Faithfulness Score = supported_claims / total_claims
        """
        return await self.judge.evaluate(prompt)
    
    async def evaluate_completeness(self, question, answer, ground_truth):
        """Check if answer covers all aspects of ground truth"""
        prompt = f"""
        Question: {question}
        Generated Answer: {answer}
        Reference Answer: {ground_truth}
        
        What percentage of key information from the reference 
        is captured in the generated answer? Score 0-1.
        """
        return await self.judge.evaluate(prompt)
```

**End-to-End Evaluation Strategy:**
1. **Unit tests**: Individual component testing (chunker, embedder, retriever)
2. **Integration tests**: Pipeline end-to-end with golden dataset
3. **Regression tests**: Ensure new changes don't degrade performance
4. **A/B testing**: Compare different configurations in production
5. **User feedback**: Thumbs up/down, explicit ratings

---

**Q5: Explain advanced RAG techniques: Query Transformation, Self-RAG, and Corrective RAG.**

**Answer:**

**1. Query Transformation Techniques:**

```python
class QueryTransformer:
    """Multiple strategies to improve retrieval"""
    
    async def multi_query(self, original_query):
        """Generate multiple perspectives of the same question"""
        prompt = f"""Generate 3 different versions of this question 
        to retrieve relevant documents from different angles:
        
        Original: {original_query}
        
        Alternative questions:"""
        return await self.llm.generate(prompt)
    
    async def hyde(self, query):
        """Hypothetical Document Embedding - generate a fake answer, 
        embed it, use that for retrieval"""
        hypothetical_answer = await self.llm.generate(
            f"Write a detailed passage that would answer: {query}"
        )
        # Embed the hypothetical answer (better than embedding the question)
        return self.embedder.encode(hypothetical_answer)
    
    async def step_back(self, query):
        """Step-back prompting - ask a broader question first"""
        broader_query = await self.llm.generate(
            f"What is a broader, more general question that would help "
            f"answer: {query}? Generate the step-back question."
        )
        return broader_query
    
    async def decompose(self, query):
        """Break complex query into sub-queries"""
        sub_queries = await self.llm.generate(
            f"Break this complex question into 2-3 simpler sub-questions "
            f"that can be answered independently: {query}"
        )
        return sub_queries
```

**2. Self-RAG (Self-Reflective RAG):**

The model decides WHEN to retrieve and EVALUATES its own outputs:

```python
class SelfRAG:
    """LLM decides whether retrieval is needed and validates outputs"""
    
    async def answer(self, query):
        # Step 1: Decide if retrieval is needed
        needs_retrieval = await self.should_retrieve(query)
        
        if needs_retrieval:
            # Step 2: Retrieve
            documents = await self.retrieve(query)
            
            # Step 3: Evaluate relevance of each document
            relevant_docs = []
            for doc in documents:
                is_relevant = await self.check_relevance(query, doc)
                if is_relevant:
                    relevant_docs.append(doc)
            
            # Step 4: Generate with relevant context
            response = await self.generate(query, relevant_docs)
            
            # Step 5: Self-evaluate (is response supported? is it useful?)
            is_supported = await self.check_support(response, relevant_docs)
            is_useful = await self.check_utility(query, response)
            
            if not is_supported:
                # Regenerate or indicate uncertainty
                response = await self.regenerate_with_disclaimer(query, relevant_docs)
        else:
            # Generate without retrieval (model has enough knowledge)
            response = await self.generate(query, context=None)
        
        return response
```

**3. Corrective RAG (CRAG):**

Evaluates retrieval quality and takes corrective actions:

```python
class CorrectiveRAG:
    """Evaluates retrieval quality and corrects if needed"""
    
    async def answer(self, query):
        # Retrieve documents
        documents = await self.retrieve(query)
        
        # Grade each document
        grades = await self.grade_documents(query, documents)
        
        # Decision logic
        if all(g == "relevant" for g in grades):
            # All good - proceed with generation
            context = documents
        elif any(g == "relevant" for g in grades):
            # Partial - use relevant docs + web search
            relevant = [d for d, g in zip(documents, grades) if g == "relevant"]
            web_results = await self.web_search(query)
            context = relevant + web_results
        else:
            # All irrelevant - fall back to web search
            context = await self.web_search(query)
        
        # Generate with corrected context
        response = await self.generate(query, context)
        return response
    
    async def grade_documents(self, query, documents):
        grades = []
        for doc in documents:
            grade = await self.llm.evaluate(
                f"Is this document relevant to the query?\n"
                f"Query: {query}\nDocument: {doc}\n"
                f"Answer: relevant or irrelevant"
            )
            grades.append(grade)
        return grades
```

---

## 5. AI Agents & Copilots

### Detailed Explanation

**AI Agents** are autonomous systems that perceive their environment, make decisions, and take actions to achieve goals. **Copilots** are semi-autonomous assistants that augment human capabilities in specific domains.

### Key Differences

| Aspect | Agent | Copilot |
|--------|-------|---------|
| **Autonomy** | High (acts independently) | Low-Medium (assists human) |
| **Decision Making** | Makes and executes decisions | Suggests, human decides |
| **Scope** | Can perform complete workflows | Operates within human workflow |
| **Risk** | Higher (less human oversight) | Lower (human in the loop) |
| **Example** | Auto-trading bot, CI/CD agent | GitHub Copilot, Office Copilot |

### Copilot Architecture Pattern

```
┌──────────────────────────────────────────────────┐
│                   COPILOT SYSTEM                   │
├──────────────────────────────────────────────────┤
│                                                    │
│  USER CONTEXT                                     │
│  ┌────────────────────────────────────────┐      │
│  │ Current document/code/email/data       │      │
│  │ User preferences & history             │      │
│  │ Application state                       │      │
│  └────────────────────────────────────────┘      │
│           │                                        │
│           ▼                                        │
│  UNDERSTANDING ENGINE                             │
│  ┌────────────────────────────────────────┐      │
│  │ Intent recognition                      │      │
│  │ Context analysis                        │      │
│  │ Skill selection                         │      │
│  └────────────────────────────────────────┘      │
│           │                                        │
│           ▼                                        │
│  SKILL EXECUTION                                  │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐   │
│  │Generate│ │Summarize│ │Analyze│ │Transform│   │
│  │Content │ │Text    │ │Data   │ │Format  │   │
│  └────────┘ └────────┘ └────────┘ └────────┘   │
│           │                                        │
│           ▼                                        │
│  RESPONSE & SUGGESTION                            │
│  ┌────────────────────────────────────────┐      │
│  │ Inline suggestions / Side panel         │      │
│  │ User accepts/rejects/modifies          │      │
│  │ Feedback loop for improvement          │      │
│  └────────────────────────────────────────┘      │
│                                                    │
└──────────────────────────────────────────────────┘
```

---

### Questions & Answers

**Q1: How would you build a domain-specific copilot for a financial services company?**

**Answer:**

**Use Case**: Investment Research Copilot that helps analysts with research, data analysis, and report generation.

**Architecture:**

```python
class FinancialCopilot:
    def __init__(self):
        # Core components
        self.llm = AzureOpenAI(model="gpt-4", temperature=0.1)
        self.rag = FinancialRAG()  # Company filings, research reports
        self.tools = FinancialToolkit()
        self.guardrails = ComplianceGuardrails()
        
    async def assist(self, user_query, context):
        # 1. Compliance check on input
        if not self.guardrails.check_input(user_query):
            return "Cannot assist with this request due to compliance policies."
        
        # 2. Understand intent
        intent = await self.classify_intent(user_query)
        
        # 3. Execute based on intent
        if intent == "market_analysis":
            result = await self.market_analysis(user_query, context)
        elif intent == "financial_modeling":
            result = await self.financial_model(user_query, context)
        elif intent == "report_generation":
            result = await self.generate_report(user_query, context)
        elif intent == "data_query":
            result = await self.query_data(user_query)
        
        # 4. Compliance check on output
        result = self.guardrails.filter_output(result)
        
        # 5. Add disclaimers
        result = self.add_disclaimers(result)
        
        return result
```

**Key Components:**

1. **Data Sources Integration:**
   - SEC filings (10-K, 10-Q, 8-K)
   - Bloomberg/Reuters market data APIs
   - Internal research database
   - Real-time news feeds
   - Company financial models (Excel)

2. **Skills/Tools:**
   ```python
   class FinancialToolkit:
       tools = [
           Tool("get_financials", get_company_financials, 
                "Get financial statements for a company"),
           Tool("calculate_ratios", calculate_financial_ratios,
                "Calculate P/E, EV/EBITDA, ROE, etc."),
           Tool("compare_peers", peer_comparison,
                "Compare company metrics vs peers"),
           Tool("sentiment_analysis", news_sentiment,
                "Analyze sentiment of recent news"),
           Tool("dcf_model", run_dcf,
                "Run discounted cash flow analysis"),
           Tool("generate_chart", create_visualization,
                "Create financial charts and graphs"),
       ]
   ```

3. **Guardrails (Critical for Finance):**
   - No investment recommendations (regulatory compliance)
   - PII/insider information detection and blocking
   - Disclosure requirements enforcement
   - Audit trail for all generated content
   - Source attribution mandatory

4. **Evaluation Metrics:**
   - Factual accuracy (cross-reference with verified data)
   - Compliance adherence rate
   - Time savings per analyst (baseline vs. copilot)
   - User satisfaction scores
   - Hallucination rate (must be near-zero for finance)

---

**Q2: What is tool use in AI agents? How do you implement it effectively?**

**Answer:**

Tool use allows agents to interact with external systems to perform actions beyond text generation:

**Tool Definition Pattern:**

```python
from pydantic import BaseModel, Field
from typing import Optional
import json

class ToolDefinition(BaseModel):
    """Standard tool definition for LLM function calling"""
    name: str
    description: str
    parameters: dict  # JSON Schema
    
class SearchTool:
    name = "web_search"
    description = "Search the internet for current information. Use when you need up-to-date data."
    
    class Parameters(BaseModel):
        query: str = Field(description="The search query")
        num_results: int = Field(default=5, description="Number of results to return")
    
    async def execute(self, query: str, num_results: int = 5) -> str:
        results = await search_api.search(query, limit=num_results)
        return json.dumps([{"title": r.title, "snippet": r.snippet, "url": r.url} 
                          for r in results])

class SQLTool:
    name = "query_database"
    description = "Execute a read-only SQL query against the business database."
    
    class Parameters(BaseModel):
        query: str = Field(description="SQL SELECT query to execute")
        database: str = Field(description="Target database name")
    
    async def execute(self, query: str, database: str) -> str:
        # Safety: Only allow SELECT queries
        if not query.strip().upper().startswith("SELECT"):
            return "Error: Only SELECT queries are allowed"
        
        # Execute with timeout and row limit
        results = await db.execute(query, database=database, 
                                    timeout=30, max_rows=100)
        return results.to_json()
```

**OpenAI Function Calling Implementation:**

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country, e.g., 'London, UK'"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# LLM decides when and how to use tools
response = await client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"  # Let model decide
)

# Process tool calls
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        
        # Execute the tool
        result = await execute_tool(function_name, arguments)
        
        # Feed result back to LLM
        messages.append({"role": "tool", "tool_call_id": tool_call.id, 
                        "content": result})
```

**Best Practices for Tool Design:**
1. **Clear descriptions**: Tools should have unambiguous descriptions
2. **Granular tools**: One tool per action (not mega-tools)
3. **Error handling**: Return informative errors, not stack traces
4. **Safety**: Validate inputs, limit scope, confirm destructive actions
5. **Idempotency**: Prefer idempotent operations where possible
6. **Observability**: Log all tool calls for debugging

---

## 6. Conversational AI

### Detailed Explanation

Conversational AI encompasses systems that engage in natural language dialogue with humans. Modern conversational AI combines:

- **Natural Language Understanding (NLU)**: Intent recognition, entity extraction
- **Dialogue Management**: State tracking, context management, flow control
- **Natural Language Generation (NLG)**: Response formation
- **Integration Layer**: Backend systems, APIs, knowledge bases

### Architecture Evolution

```
Traditional (Rule-based)     →    Modern (LLM-powered)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Intent Classifier            →    LLM Understanding
Slot Filling                 →    Function Calling
Dialog Trees                 →    Dynamic Prompting
Template Responses           →    Generative Responses
Static Knowledge             →    RAG + Real-time
```

---

### Questions & Answers

**Q1: How would you architect a modern conversational AI system for enterprise use?**

**Answer:**

**Enterprise Conversational AI Architecture:**

```
┌─────────────────────────────────────────────────────────┐
│                    CHANNELS                               │
│  Web Chat │ Mobile │ Voice │ Teams │ WhatsApp │ Email   │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                 GATEWAY LAYER                             │
│  Authentication │ Rate Limiting │ Channel Normalization  │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│              ORCHESTRATION ENGINE                         │
│                                                           │
│  ┌──────────────┐  ┌─────────────┐  ┌───────────────┐  │
│  │  Session Mgr │  │  Flow Engine │  │  Agent Router │  │
│  │  (State)     │  │  (Logic)    │  │  (Dispatch)   │  │
│  └──────────────┘  └─────────────┘  └───────────────┘  │
│                                                           │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│              AI PROCESSING LAYER                          │
│                                                           │
│  ┌────────┐ ┌────────┐ ┌──────┐ ┌──────────────────┐   │
│  │  NLU   │ │  LLM   │ │ RAG  │ │ Sentiment/Intent │   │
│  │ Engine │ │ Engine │ │Engine│ │    Analysis       │   │
│  └────────┘ └────────┘ └──────┘ └──────────────────┘   │
│                                                           │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│              INTEGRATION LAYER                            │
│  CRM │ ERP │ Ticketing │ Payment │ Inventory │ Custom   │
└─────────────────────────────────────────────────────────┘
```

**Key Components:**

1. **Session Management**:
   ```python
   class SessionManager:
       def __init__(self):
           self.store = Redis()
       
       async def get_session(self, session_id: str) -> ConversationState:
           state = await self.store.get(f"session:{session_id}")
           if not state:
               return ConversationState(
                   session_id=session_id,
                   messages=[],
                   context={},
                   intent_history=[],
                   entities={},
                   created_at=datetime.utcnow()
               )
           return ConversationState.parse_raw(state)
       
       async def update_session(self, state: ConversationState):
           await self.store.setex(
               f"session:{state.session_id}",
               ttl=3600,  # 1 hour timeout
               value=state.json()
           )
   ```

2. **Dialogue Management with LLM:**
   ```python
   class DialogueManager:
       async def process_turn(self, user_input: str, state: ConversationState):
           # Build context-aware prompt
           system_prompt = self.build_system_prompt(state)
           
           # Include conversation history
           messages = [
               {"role": "system", "content": system_prompt},
               *state.messages[-10:],  # Last 10 turns
               {"role": "user", "content": user_input}
           ]
           
           # Determine if tools/actions needed
           response = await self.llm.chat(
               messages=messages,
               tools=self.available_tools(state),
               tool_choice="auto"
           )
           
           # Process tool calls if any
           if response.tool_calls:
               results = await self.execute_tools(response.tool_calls)
               # Get final response with tool results
               response = await self.get_final_response(messages, results)
           
           return response
   ```

3. **Human Handoff:**
   - Confidence threshold detection
   - Sentiment-based escalation
   - Explicit user request detection
   - Context transfer to human agent

---

**Q2: How do you handle multi-turn conversations and maintain context?**

**Answer:**

**Challenges in Multi-turn:**
- Context window limitations
- Ambiguous references (pronouns, ellipsis)
- Topic switching
- Information accumulation across turns

**Solutions:**

```python
class MultiTurnManager:
    def __init__(self, max_history_tokens=4000):
        self.max_tokens = max_history_tokens
    
    def build_context(self, conversation: List[Message]) -> List[dict]:
        """Build optimal context from conversation history"""
        
        # Strategy 1: Sliding window with summarization
        if self.count_tokens(conversation) > self.max_tokens:
            # Summarize older messages
            old_messages = conversation[:-6]
            recent_messages = conversation[-6:]
            
            summary = self.summarize(old_messages)
            
            return [
                {"role": "system", "content": f"Previous context: {summary}"},
                *[msg.to_dict() for msg in recent_messages]
            ]
        
        return [msg.to_dict() for msg in conversation]
    
    def resolve_references(self, current_msg: str, history: List[Message]) -> str:
        """Resolve anaphoric references (he, she, it, that, etc.)"""
        # Use LLM to rewrite query with resolved references
        prompt = f"""
        Given the conversation history, rewrite the latest message 
        to be self-contained (resolve all pronouns and references):
        
        History: {format_history(history[-5:])}
        Latest: {current_msg}
        
        Rewritten (self-contained):"""
        
        return self.llm.generate(prompt)
    
    def detect_topic_switch(self, current_msg: str, context: dict) -> bool:
        """Detect if user switched topics"""
        current_embedding = self.embed(current_msg)
        context_embedding = self.embed(context.get("current_topic", ""))
        
        similarity = cosine_similarity(current_embedding, context_embedding)
        return similarity < 0.3  # Low similarity = topic switch
```

**Entity Tracking Across Turns:**

```python
class EntityTracker:
    """Track entities mentioned across conversation"""
    
    def __init__(self):
        self.entities = {}  # {entity_type: {name: details}}
    
    def update(self, message: str, llm_response: str):
        # Extract entities from the turn
        new_entities = self.extract_entities(message + " " + llm_response)
        
        for entity in new_entities:
            key = f"{entity.type}:{entity.value}"
            self.entities[key] = {
                "value": entity.value,
                "type": entity.type,
                "last_mentioned": datetime.utcnow(),
                "context": entity.context
            }
    
    def get_relevant_entities(self, query: str) -> dict:
        """Get entities relevant to current query"""
        return {k: v for k, v in self.entities.items() 
                if self.is_relevant(query, v)}
```

---

## 7. LLMOps – Deployment, Monitoring, Evaluation & Optimisation

### Detailed Explanation

LLMOps is the operational discipline for managing LLM-powered applications in production. It extends MLOps principles for the unique challenges of generative AI.

### LLMOps Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                    LLMOps LIFECYCLE                           │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  DEVELOP          │  DEPLOY           │  OPERATE             │
│  ─────────────    │  ──────────────   │  ────────────────    │
│  • Prompt eng.    │  • Containerize   │  • Monitor quality   │
│  • Fine-tune      │  • Scale (GPU)    │  • Track costs       │
│  • Evaluate       │  • A/B test       │  • Detect drift      │
│  • Version        │  • Canary deploy  │  • Collect feedback  │
│  • Test           │  • Load balance   │  • Update prompts    │
│                   │                   │  • Retrain/fine-tune  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Key Challenges

| Challenge | Description | Solution |
|-----------|-------------|----------|
| Non-determinism | Same input → different outputs | Temperature=0, seed, caching |
| Cost Management | API costs can explode | Caching, model routing, batching |
| Latency | LLMs are slow | Streaming, smaller models, caching |
| Quality Drift | Performance degrades over time | Continuous evaluation, alerts |
| Prompt Versioning | Track prompt changes | Git-based prompt management |
| Safety | Harmful/biased outputs | Guardrails, content filtering |

---

### Questions & Answers

**Q1: How do you deploy and serve LLMs in production? What are the key considerations?**

**Answer:**

**Deployment Options:**

| Option | Latency | Cost | Control | Scalability |
|--------|---------|------|---------|-------------|
| **API (OpenAI/Azure)** | Medium | Per-token | Low | Unlimited |
| **Self-hosted (vLLM)** | Low | Fixed GPU | High | Manual |
| **Managed (Bedrock/Vertex)** | Medium | Per-token | Medium | Auto |
| **Edge (ONNX/TFLite)** | Very Low | Device cost | High | Limited |

**Production Serving Architecture:**

```python
# Using vLLM for self-hosted serving
from vllm import LLM, SamplingParams

class LLMServer:
    def __init__(self):
        self.model = LLM(
            model="meta-llama/Llama-3-70b-chat",
            tensor_parallel_size=4,       # 4 GPUs
            gpu_memory_utilization=0.9,
            max_model_len=8192,
            quantization="awq"            # 4-bit quantization
        )
        self.sampling_params = SamplingParams(
            temperature=0.7,
            top_p=0.9,
            max_tokens=2048
        )
    
    async def generate(self, prompts: List[str]):
        # vLLM handles batching and continuous batching internally
        outputs = self.model.generate(prompts, self.sampling_params)
        return [output.outputs[0].text for output in outputs]
```

**Key Considerations:**

1. **GPU Management:**
   - Tensor parallelism for large models (split across GPUs)
   - Quantization (AWQ, GPTQ, GGUF) for memory reduction
   - KV-cache optimization for long sequences
   - Continuous batching for throughput

2. **Scaling Strategy:**
   ```yaml
   # Kubernetes HPA for GPU-based scaling
   apiVersion: autoscaling/v2
   kind: HorizontalPodAutoscaler
   spec:
     scaleTargetRef:
       apiVersion: apps/v1
       kind: Deployment
       name: llm-server
     minReplicas: 2
     maxReplicas: 10
     metrics:
     - type: Pods
       pods:
         metric:
           name: gpu_utilization
         target:
           type: AverageValue
           averageValue: "80"
     - type: Pods
       pods:
         metric:
           name: request_queue_length
         target:
           type: AverageValue
           averageValue: "10"
   ```

3. **Caching Layer:**
   ```python
   class SemanticCache:
       """Cache similar queries to reduce LLM calls"""
       def __init__(self, similarity_threshold=0.95):
           self.threshold = similarity_threshold
           self.cache = VectorStore()
       
       async def get_or_generate(self, query, generate_fn):
           # Check if similar query was already answered
           cached = self.cache.search(query, threshold=self.threshold)
           if cached:
               return cached.response  # Cache hit
           
           # Generate new response
           response = await generate_fn(query)
           
           # Store in cache
           self.cache.store(query, response)
           return response
   ```

4. **Cost Optimization:**
   - Model routing (simple queries → small model, complex → large model)
   - Prompt compression
   - Response caching
   - Batch processing for non-real-time requests

---

**Q2: How do you monitor LLM applications in production?**

**Answer:**

**Monitoring Framework:**

```python
class LLMMonitor:
    """Comprehensive LLM monitoring system"""
    
    def __init__(self):
        self.metrics = PrometheusMetrics()
        self.traces = LangSmith()  # or OpenTelemetry
        self.alerts = AlertManager()
    
    async def track_request(self, request_id: str, query: str, response: str, 
                           metadata: dict):
        # 1. Performance Metrics
        self.metrics.record({
            "latency_ms": metadata["latency"],
            "ttft_ms": metadata["time_to_first_token"],
            "tokens_per_second": metadata["tps"],
            "input_tokens": metadata["input_tokens"],
            "output_tokens": metadata["output_tokens"],
            "total_cost_usd": self.calculate_cost(metadata),
        })
        
        # 2. Quality Metrics (async evaluation)
        asyncio.create_task(self.evaluate_quality(
            request_id, query, response, metadata
        ))
        
        # 3. Safety Checks
        safety_score = await self.safety_check(response)
        if safety_score < 0.8:
            self.alerts.fire("safety_violation", request_id=request_id)
        
        # 4. Trace logging
        self.traces.log_trace({
            "request_id": request_id,
            "query": query,
            "response": response,
            "model": metadata["model"],
            "temperature": metadata["temperature"],
            "retrieval_results": metadata.get("retrieved_docs"),
        })
    
    async def evaluate_quality(self, request_id, query, response, metadata):
        """Async quality evaluation (sampled)"""
        if random.random() > 0.1:  # Sample 10% of requests
            return
        
        # Use LLM-as-judge for quality scoring
        scores = await self.judge_llm.evaluate({
            "relevance": (query, response),
            "coherence": response,
            "faithfulness": (response, metadata.get("context")),
        })
        
        self.metrics.record_quality(request_id, scores)
        
        # Alert on quality degradation
        if scores["relevance"] < 0.6:
            self.alerts.fire("quality_degradation", 
                           metric="relevance", score=scores["relevance"])
```

**Dashboard Metrics:**

| Category | Metrics |
|----------|---------|
| **Performance** | Latency (p50, p95, p99), TTFT, TPS, throughput |
| **Quality** | Relevance score, faithfulness, hallucination rate |
| **Cost** | $/request, $/user, daily/monthly spend, cost per model |
| **Usage** | Requests/sec, unique users, popular queries |
| **Errors** | Error rate, timeout rate, rate limit hits |
| **Safety** | Toxicity triggers, PII detections, guardrail activations |
| **RAG** | Retrieval precision, context relevance, empty retrievals |
| **Business** | User satisfaction, task completion rate, human escalation % |

---

**Q3: How do you optimize LLM costs in production?**

**Answer:**

**Cost Optimization Strategies:**

```python
class CostOptimizer:
    """Multi-strategy cost optimization for LLM applications"""
    
    # Strategy 1: Model Routing
    async def route_to_model(self, query: str, complexity: float):
        """Route based on query complexity — check provider pricing pages for current rates"""
        if complexity < 0.3:
            return "gpt-4o-mini"       # Simple queries: cheapest tier ($)
        elif complexity < 0.7:
            return "gpt-4o"            # Medium complexity ($$)
        else:
            return "gpt-4o"            # Complex: most capable model ($$$)
    
    # Strategy 2: Prompt Compression
    def compress_prompt(self, prompt: str, max_tokens: int) -> str:
        """Remove redundant tokens while preserving meaning"""
        # Use LLMLingua or similar
        compressed = llmlingua.compress(
            prompt,
            target_ratio=0.5,
            force_tokens=["important", "keywords"]
        )
        return compressed
    
    # Strategy 3: Semantic Caching
    async def cached_generate(self, query: str):
        """Check semantic cache before calling LLM"""
        similar = self.cache.find_similar(query, threshold=0.95)
        if similar:
            return similar.response  # Free!
        
        response = await self.llm.generate(query)
        self.cache.store(query, response)
        return response
    
    # Strategy 4: Batch Processing
    async def batch_process(self, queries: List[str]):
        """Batch non-urgent requests"""
        # Wait for batch to fill or timeout
        batch = await self.batch_queue.get_batch(
            max_size=50, 
            max_wait_seconds=5
        )
        
        # Process in batch (better throughput, lower per-token cost)
        results = await self.llm.batch_generate(batch)
        return results
    
    # Strategy 5: Output Length Control
    def optimize_max_tokens(self, task_type: str) -> int:
        """Set appropriate max_tokens per task type"""
        limits = {
            "classification": 10,
            "extraction": 200,
            "summarization": 500,
            "generation": 1000,
            "analysis": 2000,
        }
        return limits.get(task_type, 500)
```

**Cost Comparison Table:**

| Optimization | Savings | Effort | Trade-off |
|-------------|---------|--------|-----------|
| Semantic Caching | 30-60% | Low | Stale responses possible |
| Model Routing | 40-70% | Medium | Slight quality variance |
| Prompt Compression | 20-40% | Low | Potential info loss |
| Batch Processing | 20-30% | Medium | Added latency |
| Fine-tuned small model | 80-90% | High | Domain-specific only |
| Quantization (self-hosted) | 50-75% | Medium | Slight quality drop |

---

## 8. Cloud AI Stack – Azure / AWS / GCP

### Detailed Explanation

Each cloud provider offers a comprehensive AI/ML stack:

### Service Comparison

| Capability | Azure | AWS | GCP |
|-----------|-------|-----|-----|
| **LLM API** | Azure OpenAI | Bedrock | Vertex AI |
| **Custom Models** | Azure ML | SageMaker | Vertex AI Training |
| **Vector DB** | AI Search | OpenSearch | Vertex AI Vector Search |
| **Orchestration** | Semantic Kernel | Step Functions | Vertex AI Pipelines |
| **Embeddings** | Azure OpenAI | Bedrock/Titan | Vertex AI Embeddings |
| **Speech** | Azure Speech | Transcribe/Polly | Speech-to-Text |
| **Vision** | Azure Vision | Rekognition | Vision AI |
| **Document AI** | Document Intelligence | Textract | Document AI |
| **Responsible AI** | Content Safety | Guardrails | Responsible AI Toolkit |

---

### Questions & Answers

**Q1: Compare Azure AI stack vs AWS AI stack for building an enterprise GenAI application.**

**Answer:**

**Azure AI Stack (Microsoft):**

```
┌─────────────────────────────────────────────────────┐
│              AZURE AI ARCHITECTURE                    │
├─────────────────────────────────────────────────────┤
│                                                       │
│  LLM Layer                                           │
│  ├── Azure OpenAI Service (GPT-4, GPT-4o, o1)      │
│  ├── Azure AI Studio (model catalog, playground)    │
│  └── Fine-tuning (Azure OpenAI, Azure ML)           │
│                                                       │
│  RAG & Search                                        │
│  ├── Azure AI Search (hybrid, semantic, vector)     │
│  ├── Azure Cosmos DB (vector search)                │
│  └── Azure Blob Storage (document store)            │
│                                                       │
│  Orchestration                                       │
│  ├── Semantic Kernel (SDK)                          │
│  ├── Prompt Flow (Azure AI Studio)                  │
│  └── Azure Functions (serverless compute)           │
│                                                       │
│  Safety & Governance                                 │
│  ├── Azure AI Content Safety                        │
│  ├── Azure Policy                                   │
│  └── Microsoft Purview (data governance)            │
│                                                       │
│  Infrastructure                                      │
│  ├── Azure Kubernetes Service (AKS)                 │
│  ├── Azure Container Apps                           │
│  └── Azure Monitor + Application Insights           │
│                                                       │
└─────────────────────────────────────────────────────┘
```

**AWS AI Stack:**

```
┌─────────────────────────────────────────────────────┐
│                AWS AI ARCHITECTURE                    │
├─────────────────────────────────────────────────────┤
│                                                       │
│  LLM Layer                                           │
│  ├── Amazon Bedrock (Claude, LLaMA, Titan, Cohere) │
│  ├── SageMaker JumpStart (model hub)                │
│  └── SageMaker Training (fine-tuning)               │
│                                                       │
│  RAG & Search                                        │
│  ├── Amazon Kendra (enterprise search)              │
│  ├── OpenSearch (vector + keyword)                  │
│  └── S3 + Glue (data lake)                         │
│                                                       │
│  Orchestration                                       │
│  ├── Bedrock Agents (managed agents)                │
│  ├── Step Functions (workflow)                       │
│  └── Lambda (serverless compute)                    │
│                                                       │
│  Safety & Governance                                 │
│  ├── Bedrock Guardrails                             │
│  ├── AWS IAM + Lake Formation                       │
│  └── CloudTrail (audit)                             │
│                                                       │
│  Infrastructure                                      │
│  ├── ECS/EKS (containers)                           │
│  ├── EC2 Inf2/Trn1 (AI accelerators)               │
│  └── CloudWatch + X-Ray (monitoring)                │
│                                                       │
└─────────────────────────────────────────────────────┘
```

**Decision Factors:**

| Factor | Azure Wins When | AWS Wins When |
|--------|----------------|---------------|
| **LLM Access** | Need OpenAI models (GPT-4, o1) | Need model variety (Claude, LLaMA) |
| **Enterprise** | Microsoft ecosystem (O365, Teams) | AWS-native infrastructure |
| **Compliance** | Government/regulated (FedRAMP) | Global multi-region |
| **RAG** | Integrated AI Search + OpenAI | OpenSearch + Bedrock Knowledge Bases |
| **Cost** | Reserved capacity, enterprise agreements | Pay-per-use, Spot instances |
| **Multi-cloud** | Already have Azure AD | Already AWS-native |

---

**Q2: How would you architect a multi-region, highly available AI application on Azure?**

**Answer:**

```
┌─────────────────────────────────────────────────────────────┐
│                  MULTI-REGION AI ARCHITECTURE                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌───────────────────┐         ┌───────────────────┐        │
│  │   REGION: EAST US │         │  REGION: WEST EU  │        │
│  │                   │         │                   │        │
│  │  ┌─────────────┐ │         │ ┌─────────────┐  │        │
│  │  │ Azure OpenAI│ │         │ │ Azure OpenAI│  │        │
│  │  │ (Primary)   │ │         │ │ (Secondary) │  │        │
│  │  └─────────────┘ │         │ └─────────────┘  │        │
│  │  ┌─────────────┐ │         │ ┌─────────────┐  │        │
│  │  │ AI Search   │ │◄───────►│ │ AI Search   │  │        │
│  │  │ (Replica)   │ │  Sync   │ │ (Replica)   │  │        │
│  │  └─────────────┘ │         │ └─────────────┘  │        │
│  │  ┌─────────────┐ │         │ ┌─────────────┐  │        │
│  │  │ AKS Cluster │ │         │ │ AKS Cluster │  │        │
│  │  └─────────────┘ │         │ └─────────────┘  │        │
│  │                   │         │                   │        │
│  └───────────────────┘         └───────────────────┘        │
│              │                           │                    │
│              └───────────┬───────────────┘                   │
│                          │                                    │
│            ┌─────────────▼──────────────┐                   │
│            │    Azure Front Door         │                   │
│            │  (Global Load Balancing)    │                   │
│            └─────────────┬──────────────┘                   │
│                          │                                    │
│            ┌─────────────▼──────────────┐                   │
│            │   Azure API Management      │                   │
│            │  (Rate Limit, Auth, Routing)│                   │
│            └────────────────────────────┘                   │
│                                                               │
│  SHARED SERVICES                                             │
│  ├── Cosmos DB (Global distribution, multi-write)           │
│  ├── Azure Key Vault (Secrets management)                   │
│  ├── Azure Monitor (Centralized observability)              │
│  └── Azure DevOps (CI/CD pipelines)                         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Key Design Decisions:**

1. **Azure OpenAI Deployment**: Deploy in multiple regions with APIM routing and fallback
2. **Data Replication**: Cosmos DB with multi-region writes for session state
3. **Vector Store**: AI Search with geo-replicated indexes
4. **Failover**: Automatic failover via Front Door health probes
5. **Cost**: Use PTU (Provisioned Throughput Units) for predictable pricing

---

## 9. APIs & Microservices

### Detailed Explanation

Modern AI systems are built as microservices communicating via APIs. This enables:
- Independent scaling of AI components
- Technology flexibility per service
- Fault isolation
- Team autonomy

### AI Microservices Architecture

```
┌─────────────────────────────────────────────────────┐
│              AI MICROSERVICES ARCHITECTURE            │
├─────────────────────────────────────────────────────┤
│                                                       │
│  API Gateway (Kong/APIM)                             │
│  ├── Auth, Rate Limiting, Routing                   │
│  │                                                   │
│  ├── /api/chat → Chat Service                       │
│  │   └── Handles conversation flow                  │
│  │                                                   │
│  ├── /api/search → Search Service                   │
│  │   └── RAG retrieval + re-ranking                │
│  │                                                   │
│  ├── /api/embeddings → Embedding Service            │
│  │   └── Text/image embedding generation            │
│  │                                                   │
│  ├── /api/agents → Agent Service                    │
│  │   └── Agent orchestration + tool execution       │
│  │                                                   │
│  └── /api/ingest → Ingestion Service               │
│      └── Document processing + indexing             │
│                                                       │
│  Shared Services                                     │
│  ├── Model Gateway (unified LLM access)             │
│  ├── Vector Store (Qdrant/Pinecone)                 │
│  ├── Cache (Redis)                                   │
│  ├── Message Queue (Kafka/RabbitMQ)                 │
│  └── Observability (OpenTelemetry)                  │
│                                                       │
└─────────────────────────────────────────────────────┘
```

---

### Questions & Answers

**Q1: How do you design APIs for AI/LLM applications? What are the unique challenges?**

**Answer:**

**Unique Challenges for AI APIs:**

| Challenge | Solution |
|-----------|----------|
| Long response times (10-60s) | Streaming (SSE), async with webhooks |
| Variable output length | Streaming, chunked responses |
| Non-determinism | Seed parameter, caching layer |
| High cost per request | Rate limiting, tiered access |
| Context management | Session IDs, stateful endpoints |
| Large payloads (documents) | Chunked upload, presigned URLs |

**API Design for Chat/Agent:**

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional, List
import asyncio

app = FastAPI()

# --- Request/Response Models ---

class ChatMessage(BaseModel):
    role: str  # "user", "assistant", "system"
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    session_id: Optional[str] = None
    model: Optional[str] = "gpt-4"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 2000
    stream: Optional[bool] = False
    tools: Optional[List[str]] = None

class ChatResponse(BaseModel):
    id: str
    session_id: str
    message: ChatMessage
    usage: dict
    sources: Optional[List[dict]] = None  # RAG citations
    tool_calls: Optional[List[dict]] = None

# --- Endpoints ---

@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Non-streaming chat endpoint"""
    session = await get_or_create_session(request.session_id)
    
    response = await orchestrator.process(
        messages=request.messages,
        session=session,
        config=request
    )
    
    return ChatResponse(
        id=generate_id(),
        session_id=session.id,
        message=response.message,
        usage=response.usage,
        sources=response.sources
    )

@app.post("/api/v1/chat/stream")
async def chat_stream(request: ChatRequest):
    """Server-Sent Events streaming endpoint"""
    
    async def event_generator():
        async for chunk in orchestrator.stream(
            messages=request.messages,
            config=request
        ):
            if chunk.type == "token":
                yield f"data: {json.dumps({'type': 'token', 'content': chunk.content})}\n\n"
            elif chunk.type == "tool_call":
                yield f"data: {json.dumps({'type': 'tool_call', 'tool': chunk.tool, 'args': chunk.args})}\n\n"
            elif chunk.type == "source":
                yield f"data: {json.dumps({'type': 'source', 'source': chunk.source})}\n\n"
            elif chunk.type == "done":
                yield f"data: {json.dumps({'type': 'done', 'usage': chunk.usage})}\n\n"
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

# --- Document Ingestion ---

@app.post("/api/v1/ingest")
async def ingest_document(
    file: UploadFile,
    collection: str = "default",
    chunking_strategy: str = "semantic"
):
    """Async document ingestion with progress tracking"""
    job_id = generate_id()
    
    # Queue for async processing
    await task_queue.enqueue(
        "ingest_document",
        job_id=job_id,
        file_path=await save_upload(file),
        collection=collection,
        strategy=chunking_strategy
    )
    
    return {"job_id": job_id, "status": "processing"}

@app.get("/api/v1/ingest/{job_id}/status")
async def get_ingestion_status(job_id: str):
    """Check ingestion job status"""
    status = await task_queue.get_status(job_id)
    return status
```

**API Best Practices for AI:**
1. **Always support streaming** for chat/generation endpoints
2. **Include usage/cost info** in responses
3. **Provide session management** for multi-turn
4. **Implement retries with exponential backoff** for LLM calls
5. **Use API versioning** (prompt changes = breaking changes)
6. **Rate limit by tokens, not just requests**

---

## 10. Data Integration

### Detailed Explanation

AI applications require diverse data sources. Data integration involves connecting, transforming, and maintaining data pipelines that feed AI systems.

### Data Integration for AI

```
┌──────────────────────────────────────────────────────┐
│           DATA INTEGRATION FOR AI SYSTEMS             │
├──────────────────────────────────────────────────────┤
│                                                        │
│  DATA SOURCES                                         │
│  ├── Structured: SQL DBs, ERPs, CRMs                 │
│  ├── Semi-structured: JSON APIs, Logs, Config        │
│  ├── Unstructured: PDFs, Docs, Images, Videos        │
│  ├── Real-time: Kafka streams, WebSockets, IoT       │
│  └── External: APIs, Web scraping, Data vendors      │
│                                                        │
│  INGESTION LAYER                                      │
│  ├── Batch: Airflow, Prefect, Dagster                │
│  ├── Streaming: Kafka, Flink, Spark Streaming        │
│  ├── CDC: Debezium, AWS DMS                          │
│  └── File watchers: S3 events, Azure Event Grid      │
│                                                        │
│  PROCESSING LAYER                                     │
│  ├── Document parsing (Unstructured.io, Docling)     │
│  ├── Chunking & embedding                            │
│  ├── Entity extraction & enrichment                  │
│  ├── Data quality & validation                       │
│  └── PII detection & masking                         │
│                                                        │
│  STORAGE LAYER                                        │
│  ├── Vector Store: Qdrant, Pinecone, Weaviate        │
│  ├── Knowledge Graph: Neo4j, Amazon Neptune          │
│  ├── Feature Store: Feast, Tecton                    │
│  ├── Data Lake: Delta Lake, Iceberg                  │
│  └── Cache: Redis, Memcached                         │
│                                                        │
└──────────────────────────────────────────────────────┘
```

---

### Questions & Answers

**Q1: How do you build a document ingestion pipeline for a RAG system that handles multiple formats?**

**Answer:**

```python
from abc import ABC, abstractmethod
from typing import List, Dict
import asyncio

class DocumentProcessor(ABC):
    @abstractmethod
    async def process(self, file_path: str) -> List[Dict]:
        """Returns list of chunks with metadata"""
        pass

class PDFProcessor(DocumentProcessor):
    async def process(self, file_path: str) -> List[Dict]:
        # Use Unstructured.io for robust PDF parsing
        from unstructured.partition.pdf import partition_pdf
        
        elements = partition_pdf(
            file_path,
            strategy="hi_res",          # OCR + layout analysis
            infer_table_structure=True,   # Extract tables
            extract_images_in_pdf=True    # Extract images
        )
        
        chunks = []
        for element in elements:
            chunks.append({
                "content": element.text,
                "type": element.category,  # Title, NarrativeText, Table, etc.
                "metadata": {
                    "page_number": element.metadata.page_number,
                    "coordinates": element.metadata.coordinates,
                    "source": file_path
                }
            })
        return chunks

class IngestionPipeline:
    def __init__(self):
        self.processors = {
            ".pdf": PDFProcessor(),
            ".docx": DocxProcessor(),
            ".pptx": PptxProcessor(),
            ".html": HTMLProcessor(),
            ".md": MarkdownProcessor(),
            ".csv": CSVProcessor(),
            ".json": JSONProcessor(),
        }
        self.embedder = EmbeddingModel("BAAI/bge-large-en-v1.5")
        self.vector_store = QdrantClient()
        self.chunker = SemanticChunker(max_chunk_size=512)
    
    async def ingest(self, file_path: str, collection: str):
        # 1. Determine processor
        ext = Path(file_path).suffix.lower()
        processor = self.processors.get(ext)
        if not processor:
            raise ValueError(f"Unsupported format: {ext}")
        
        # 2. Extract content
        raw_chunks = await processor.process(file_path)
        
        # 3. Chunk content
        chunks = self.chunker.chunk(raw_chunks)
        
        # 4. Enrich metadata
        chunks = await self.enrich(chunks)
        
        # 5. Generate embeddings (batch)
        texts = [c["content"] for c in chunks]
        embeddings = self.embedder.encode_batch(texts, batch_size=64)
        
        # 6. Store in vector DB
        self.vector_store.upsert(
            collection_name=collection,
            points=[
                {
                    "id": generate_id(),
                    "vector": emb,
                    "payload": chunk
                }
                for emb, chunk in zip(embeddings, chunks)
            ]
        )
        
        return {"chunks_processed": len(chunks), "collection": collection}
    
    async def enrich(self, chunks: List[Dict]) -> List[Dict]:
        """Add metadata: entities, topics, summary"""
        for chunk in chunks:
            # Extract entities
            chunk["entities"] = await self.extract_entities(chunk["content"])
            # Generate title/summary for chunk
            chunk["title"] = await self.generate_chunk_title(chunk["content"])
        return chunks
```

---

## 11. Prompt Engineering & Orchestration

### Detailed Explanation

Prompt engineering is the art and science of designing inputs to LLMs that produce desired outputs. Orchestration involves chaining multiple LLM calls and tools together.

### Prompt Engineering Techniques

| Technique | Description | Use Case |
|-----------|-------------|----------|
| **Zero-shot** | Direct instruction, no examples | Simple tasks |
| **Few-shot** | Include examples in prompt | Pattern learning |
| **Chain-of-Thought (CoT)** | "Think step by step" | Reasoning tasks |
| **Tree-of-Thought (ToT)** | Explore multiple reasoning paths | Complex problems |
| **Self-Consistency** | Sample multiple CoTs, majority vote | Reliability |
| **ReAct** | Interleave reasoning and actions | Tool-using agents |
| **Structured Output** | JSON/XML output format | Data extraction |
| **System Prompting** | Role, personality, constraints | Behavior control |

---

### Questions & Answers

**Q1: What are advanced prompt engineering techniques for production systems?**

**Answer:**

**1. Meta-Prompting (Prompt that generates prompts):**
```python
meta_prompt = """
You are a prompt engineer. Given the task description, generate an optimal 
prompt that will produce the best results from an LLM.

Task: {task_description}
Target Model: {model_name}
Required Output Format: {output_format}

Generate the optimal prompt with:
1. Clear role/persona
2. Specific instructions
3. Output format specification
4. Edge case handling
5. Few-shot examples if needed
"""
```

**2. Chain-of-Thought with Verification:**
```python
cot_with_verify = """
Solve this problem step by step, then verify your answer.

Problem: {problem}

Steps:
1. [Solve step by step]
2. [Show your work]
3. [Arrive at answer]

Verification:
- Check: Does the answer make logical sense?
- Check: Plug the answer back in - does it satisfy the problem?
- Check: Are there edge cases I missed?

If verification fails, redo the solution.

Final Answer: [only after verification passes]
"""
```

**3. Structured Output with Guardrails:**
```python
from pydantic import BaseModel, Field
from typing import List, Optional
import instructor

class ExtractedEntity(BaseModel):
    name: str = Field(description="Entity name")
    type: str = Field(description="Entity type: PERSON, ORG, LOCATION, DATE")
    confidence: float = Field(ge=0, le=1, description="Confidence score")
    context: str = Field(description="Sentence where entity appears")

class ExtractionResult(BaseModel):
    entities: List[ExtractedEntity]
    summary: str
    language: str

# Using instructor for guaranteed structured output
client = instructor.patch(openai.OpenAI())

result = client.chat.completions.create(
    model="gpt-4",
    response_model=ExtractionResult,
    messages=[
        {"role": "system", "content": "Extract all entities from the text."},
        {"role": "user", "content": document_text}
    ]
)
# result is guaranteed to be ExtractionResult type
```

**4. Dynamic Few-Shot Selection:**
```python
class DynamicFewShot:
    """Select most relevant examples for the current query"""
    
    def __init__(self, examples: List[dict], embedder):
        self.examples = examples
        self.embedder = embedder
        self.example_embeddings = embedder.encode([e["input"] for e in examples])
    
    def select_examples(self, query: str, k: int = 3) -> List[dict]:
        query_embedding = self.embedder.encode(query)
        similarities = cosine_similarity(query_embedding, self.example_embeddings)
        top_k_indices = similarities.argsort()[-k:][::-1]
        return [self.examples[i] for i in top_k_indices]
    
    def build_prompt(self, query: str) -> str:
        examples = self.select_examples(query)
        
        prompt = "Here are some relevant examples:\n\n"
        for ex in examples:
            prompt += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
        prompt += f"Now solve:\nInput: {query}\nOutput:"
        
        return prompt
```

**5. Prompt Versioning and A/B Testing:**
```python
class PromptManager:
    """Version control and A/B test prompts"""
    
    def __init__(self):
        self.prompts = {}  # {name: {version: prompt_text}}
        self.experiments = {}  # Active A/B tests
    
    def register_prompt(self, name: str, version: str, template: str):
        if name not in self.prompts:
            self.prompts[name] = {}
        self.prompts[name][version] = template
    
    def get_prompt(self, name: str, user_id: str = None) -> str:
        # Check if there's an active experiment
        if name in self.experiments:
            experiment = self.experiments[name]
            # Deterministic assignment based on user_id
            variant = self.assign_variant(user_id, experiment)
            return self.prompts[name][variant]
        
        # Return production version
        return self.prompts[name]["production"]
    
    def track_result(self, name: str, version: str, metrics: dict):
        """Track prompt performance for A/B analysis"""
        self.analytics.log(name=name, version=version, **metrics)
```

---

## 12. Multi-Agent Systems & Guardrails

### Detailed Explanation

Multi-agent systems involve multiple AI agents collaborating, delegating, and communicating to solve complex problems. Guardrails ensure safety, compliance, and quality.

### Multi-Agent Patterns

```
┌──────────────────────────────────────────────────────┐
│           MULTI-AGENT PATTERNS                        │
├──────────────────────────────────────────────────────┤
│                                                        │
│  1. HIERARCHICAL (Manager-Worker)                     │
│     Manager Agent → assigns tasks to Worker Agents    │
│                                                        │
│  2. COLLABORATIVE (Peer-to-Peer)                      │
│     Agents discuss and build on each other's work     │
│                                                        │
│  3. COMPETITIVE (Debate)                              │
│     Agents argue different positions, judge decides   │
│                                                        │
│  4. SEQUENTIAL (Pipeline)                             │
│     Output of Agent A → Input of Agent B → ...        │
│                                                        │
│  5. PARALLEL (Fan-out/Fan-in)                         │
│     Multiple agents work simultaneously, merge        │
│                                                        │
└──────────────────────────────────────────────────────┘
```

---

### Questions & Answers

**Q1: Design a multi-agent system for automated code review. Explain the architecture and agent roles.**

**Answer:**

```python
from langgraph.graph import StateGraph
from typing import TypedDict, List

class CodeReviewState(TypedDict):
    code: str
    language: str
    pr_description: str
    security_review: dict
    quality_review: dict
    performance_review: dict
    final_review: dict
    approved: bool

# Agent 1: Security Reviewer
class SecurityReviewAgent:
    """Checks for security vulnerabilities"""
    
    system_prompt = """You are a security expert. Review code for:
    - SQL injection, XSS, CSRF vulnerabilities
    - Hardcoded secrets/credentials
    - Insecure dependencies
    - Authentication/authorization issues
    - Input validation gaps
    
    Rate severity: CRITICAL, HIGH, MEDIUM, LOW
    Provide specific line numbers and fix suggestions."""
    
    async def review(self, state: CodeReviewState) -> dict:
        response = await self.llm.analyze(
            system=self.system_prompt,
            user=f"Review this {state['language']} code:\n{state['code']}"
        )
        return {"security_review": parse_review(response)}

# Agent 2: Code Quality Reviewer
class QualityReviewAgent:
    """Checks code quality and best practices"""
    
    system_prompt = """You are a senior software engineer. Review for:
    - Code readability and maintainability
    - SOLID principles adherence
    - Design patterns (appropriate/inappropriate)
    - Naming conventions
    - Code duplication (DRY violations)
    - Error handling completeness
    - Test coverage suggestions"""
    
    async def review(self, state: CodeReviewState) -> dict:
        response = await self.llm.analyze(
            system=self.system_prompt,
            user=f"Language: {state['language']}\nPR: {state['pr_description']}\nCode:\n{state['code']}"
        )
        return {"quality_review": parse_review(response)}

# Agent 3: Performance Reviewer
class PerformanceReviewAgent:
    """Checks for performance issues"""
    
    system_prompt = """You are a performance engineer. Review for:
    - Algorithm complexity (time/space)
    - N+1 query problems
    - Memory leaks
    - Unnecessary allocations
    - Caching opportunities
    - Concurrency issues (race conditions, deadlocks)
    - Database query optimization"""

# Agent 4: Synthesizer (Final Reviewer)
class SynthesizerAgent:
    """Combines all reviews into final decision"""
    
    async def synthesize(self, state: CodeReviewState) -> dict:
        prompt = f"""
        Based on these reviews, provide a final summary:
        
        Security: {state['security_review']}
        Quality: {state['quality_review']}
        Performance: {state['performance_review']}
        
        Provide:
        1. Overall assessment (APPROVE / REQUEST_CHANGES / REJECT)
        2. Priority-ordered list of changes needed
        3. Positive aspects of the code
        4. Summary for the developer
        """
        
        response = await self.llm.analyze(system="You are a tech lead.", user=prompt)
        approved = "APPROVE" in response
        return {"final_review": response, "approved": approved}

# Build the Multi-Agent Graph
workflow = StateGraph(CodeReviewState)

# Add agents as nodes
workflow.add_node("security", SecurityReviewAgent().review)
workflow.add_node("quality", QualityReviewAgent().review)
workflow.add_node("performance", PerformanceReviewAgent().review)
workflow.add_node("synthesize", SynthesizerAgent().synthesize)

# Parallel execution for independent reviews
workflow.set_entry_point("security")
workflow.add_edge("security", "quality")
workflow.add_edge("quality", "performance")
workflow.add_edge("performance", "synthesize")
workflow.add_edge("synthesize", END)

# In production, security/quality/performance run in parallel:
# workflow.add_parallel_edges(["security", "quality", "performance"])
# workflow.add_edge(["security", "quality", "performance"], "synthesize")

app = workflow.compile()
```

---

**Q2: What are guardrails for LLM applications? How do you implement them?**

**Answer:**

**Guardrails Architecture:**

```
User Input → [INPUT GUARDRAILS] → LLM Processing → [OUTPUT GUARDRAILS] → User Response
                   │                                         │
                   ▼                                         ▼
            ┌────────────┐                           ┌────────────┐
            │ • PII Det. │                           │ • Toxicity │
            │ • Injection│                           │ • Halluc.  │
            │ • Topic    │                           │ • PII leak │
            │ • Length   │                           │ • Relevance│
            │ • Rate Lim.│                           │ • Format   │
            └────────────┘                           └────────────┘
```

**Implementation:**

```python
from pydantic import BaseModel
from typing import List, Optional
import re

class GuardrailResult(BaseModel):
    passed: bool
    violations: List[str] = []
    sanitized_input: Optional[str] = None
    risk_score: float = 0.0

class InputGuardrails:
    """Pre-processing guardrails before LLM call"""
    
    async def check(self, user_input: str) -> GuardrailResult:
        violations = []
        sanitized = user_input
        risk_score = 0.0
        
        # 1. Prompt Injection Detection
        injection_score = await self.detect_injection(user_input)
        if injection_score > 0.8:
            violations.append(f"Potential prompt injection (score: {injection_score})")
            risk_score = max(risk_score, injection_score)
        
        # 2. PII Detection & Masking
        pii_entities = await self.detect_pii(user_input)
        if pii_entities:
            sanitized = self.mask_pii(user_input, pii_entities)
            violations.append(f"PII detected and masked: {[e.type for e in pii_entities]}")
        
        # 3. Topic/Content Policy
        topic_violation = await self.check_topic_policy(user_input)
        if topic_violation:
            violations.append(f"Off-topic: {topic_violation}")
            risk_score = max(risk_score, 0.9)
        
        # 4. Input Length Check
        if len(user_input) > 10000:
            violations.append("Input exceeds maximum length")
        
        # 5. Jailbreak Detection
        jailbreak_score = await self.detect_jailbreak(user_input)
        if jailbreak_score > 0.7:
            violations.append("Potential jailbreak attempt")
            risk_score = max(risk_score, jailbreak_score)
        
        return GuardrailResult(
            passed=risk_score < 0.8,
            violations=violations,
            sanitized_input=sanitized,
            risk_score=risk_score
        )
    
    async def detect_injection(self, text: str) -> float:
        """Detect prompt injection attempts"""
        # Pattern matching for common injections
        injection_patterns = [
            r"ignore (previous|above|all) instructions",
            r"you are now",
            r"new instructions:",
            r"system prompt:",
            r"forget everything",
            r"disregard",
        ]
        
        for pattern in injection_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return 0.9
        
        # ML-based detection for sophisticated attacks
        score = await self.injection_classifier.predict(text)
        return score

class OutputGuardrails:
    """Post-processing guardrails after LLM response"""
    
    async def check(self, response: str, context: dict) -> GuardrailResult:
        violations = []
        
        # 1. Hallucination Check (RAG)
        if context.get("retrieved_docs"):
            faithfulness = await self.check_faithfulness(
                response, context["retrieved_docs"]
            )
            if faithfulness < 0.7:
                violations.append(f"Potential hallucination (faithfulness: {faithfulness})")
        
        # 2. Toxicity Check
        toxicity = await self.toxicity_classifier.predict(response)
        if toxicity > 0.5:
            violations.append(f"Toxic content detected (score: {toxicity})")
        
        # 3. PII Leakage Check
        leaked_pii = await self.detect_pii(response)
        if leaked_pii:
            response = self.mask_pii(response, leaked_pii)
            violations.append("PII in response masked")
        
        # 4. Relevance Check
        relevance = await self.check_relevance(
            context["original_query"], response
        )
        if relevance < 0.5:
            violations.append("Response may not be relevant to query")
        
        # 5. Format Validation
        if context.get("expected_format"):
            if not self.validate_format(response, context["expected_format"]):
                violations.append("Response format mismatch")
        
        return GuardrailResult(
            passed=len([v for v in violations if "Toxic" in v or "hallucination" in v]) == 0,
            violations=violations,
            sanitized_input=response
        )
```

**Guardrail Frameworks:**
- **NeMo Guardrails** (NVIDIA): Programmable guardrails with Colang
- **Guardrails AI**: Pydantic-based validation for LLM outputs
- **LangChain Constitutional AI**: Self-critique and revision
- **Azure AI Content Safety**: Managed content filtering service

---

## 13. Presales, Solutioning & Client Management

### Detailed Explanation

In AI consulting/services, presales and solutioning bridge the gap between client business problems and AI solutions. This involves:

- **Discovery**: Understanding the client's business, data, and challenges
- **Solutioning**: Designing AI architectures that solve business problems
- **Estimation**: Effort, timeline, resource planning
- **Proposal**: Creating compelling, clear proposals
- **POC/Pilot Design**: Defining scope for proof-of-concept

---

### Questions & Answers

**Q1: A retail client wants to implement AI. How would you approach the discovery and solutioning process?**

**Answer:**

**Phase 1: Discovery Workshop (1-2 days)**

```
FRAMEWORK: Business → Data → Technology → People → Governance

1. BUSINESS UNDERSTANDING
   - What are the top 3 business pain points?
   - What does success look like? (KPIs, metrics)
   - What's the expected ROI / business impact?
   - Current manual processes that could be automated?
   - Competitive landscape and urgency

2. DATA LANDSCAPE
   - What data sources exist? (CRM, POS, inventory, web analytics)
   - Data quality assessment (completeness, accuracy, freshness)
   - Data volume and velocity
   - Data governance and compliance (GDPR, industry regulations)
   - Existing data infrastructure (warehouse, lake, pipelines)

3. TECHNOLOGY ASSESSMENT
   - Current tech stack and cloud provider
   - Existing AI/ML capabilities
   - Integration requirements (APIs, legacy systems)
   - Security and compliance requirements
   - Scalability needs

4. PEOPLE & PROCESS
   - AI maturity level of the organization
   - Available technical team and skills
   - Change management readiness
   - Training and adoption plan

5. CONSTRAINTS & RISKS
   - Budget range
   - Timeline expectations
   - Regulatory constraints
   - Data privacy requirements
```

**Phase 2: Solution Design**

For a retail client, typical AI use cases:

| Use Case | AI Technology | Business Impact | Complexity |
|----------|--------------|-----------------|------------|
| Customer Service Copilot | GenAI + RAG | 40% ticket reduction | Medium |
| Product Recommendation | ML + GenAI | 15-25% revenue lift | Medium |
| Demand Forecasting | Time series ML | 20% inventory optimization | High |
| Price Optimization | RL + ML | 5-10% margin improvement | High |
| Visual Search | Computer Vision + LLM | Better discovery, +conversions | Medium |
| Content Generation | GenAI | 80% time savings on marketing | Low |

**Phase 3: Architecture Proposal**

```
                    RETAIL AI PLATFORM
┌─────────────────────────────────────────────────────┐
│                                                       │
│  Customer-Facing Layer                               │
│  ├── AI Shopping Assistant (Chat + Voice)            │
│  ├── Personalized Recommendations                   │
│  └── Visual Search ("Find similar products")        │
│                                                       │
│  Operations Layer                                    │
│  ├── Demand Forecasting Engine                      │
│  ├── Dynamic Pricing Agent                          │
│  └── Inventory Optimization                         │
│                                                       │
│  Employee Copilot Layer                              │
│  ├── Customer Service Copilot (RAG + Agent)         │
│  ├── Merchandising Assistant                        │
│  └── Marketing Content Generator                    │
│                                                       │
│  Platform Layer                                      │
│  ├── Unified AI Gateway                             │
│  ├── Feature Store                                  │
│  ├── Vector Database                                │
│  ├── LLMOps (monitoring, evaluation)                │
│  └── Data Integration Hub                           │
│                                                       │
└─────────────────────────────────────────────────────┘
```

**Phase 4: Estimation & Roadmap**

| Phase | Duration | Focus | Deliverable |
|-------|----------|-------|-------------|
| POC | 4-6 weeks | Customer Service Copilot | Working prototype |
| MVP | 8-12 weeks | Production copilot + Recommendations | Live system |
| Scale | 12-16 weeks | Full platform + remaining use cases | Enterprise platform |

---

**Q2: How do you estimate effort for an AI/GenAI project?**

**Answer:**

**AI Project Estimation Framework:**

```
Total Effort = Data Work + Model/AI Development + Engineering + Testing + Buffer

Breakdown:
┌────────────────────┬──────────┐
│ Component          │ % Effort │
├────────────────────┼──────────┤
│ Data Engineering   │ 25-35%   │
│ AI/Model Dev       │ 20-30%   │
│ Software Eng       │ 20-25%   │
│ Testing & QA       │ 10-15%   │
│ DevOps/Infra       │ 5-10%    │
│ PM/Buffer          │ 10-15%   │
└────────────────────┴──────────┘
```

**Estimation Template for RAG System:**

> ℹ️ *These estimates are **directional ranges** based on typical mid-size enterprise projects. Actual effort varies significantly based on team experience, data complexity, existing infrastructure, and regulatory requirements. Use as a starting framework and adjust ±30% for your context.*

| Task | Effort (Person Days) | Notes |
|------|---------------------|-------|
| **Data Pipeline** | | |
| - Data source assessment | 3-5 | Understand formats, volumes |
| - Ingestion pipeline | 5-8 | Parsing, chunking, embedding |
| - Data quality & cleaning | 3-5 | Validation rules, dedup |
| **AI Development** | | |
| - RAG prototype | 3-5 | Basic retrieve + generate |
| - Advanced RAG (re-ranking, query transform) | 5-8 | Production quality |
| - Prompt engineering & tuning | 3-5 | Iterate on prompts |
| - Evaluation pipeline | 3-5 | Metrics, test sets |
| **Engineering** | | |
| - API development | 5-8 | Endpoints, streaming |
| - UI/UX (if applicable) | 5-10 | Chat interface |
| - Authentication & security | 3-5 | Auth, PII handling |
| - Integration with existing systems | 5-8 | APIs, SSO |
| **Infrastructure** | | |
| - Cloud setup (Azure/AWS) | 3-5 | Provisioning, networking |
| - CI/CD pipeline | 2-3 | Automated deployment |
| - Monitoring & observability | 3-5 | Dashboards, alerts |
| **Testing** | | |
| - Functional testing | 3-5 | End-to-end tests |
| - Performance testing | 2-3 | Load, latency |
| - Security testing | 2-3 | Pen testing, OWASP |
| - UAT support | 3-5 | User acceptance |
| **Total (MVP)** | **55-95 PD** | ~3-4 months with 3-4 people |

> 💡 **How to present this in an interview**: "Based on my experience, a RAG MVP typically takes 55-95 person-days depending on data complexity and team maturity. I'd adjust upward for regulated industries or first-time AI implementations."

**Risk Multipliers** *(apply cumulatively for high-risk projects)*:
- First AI project for client: 1.2–1.4x
- Complex data (unstructured, multilingual): 1.2–1.3x
- Strict compliance (healthcare, finance): 1.2–1.4x
- Integration with legacy systems: 1.1–1.3x
- Distributed team / multi-timezone: 1.1–1.2x

---

## 14. End-to-End Delivery: POC → MVP → Production

### Detailed Explanation

The journey from concept to production in AI follows a distinct pattern:

```
IDEATION → POC → MVP → PILOT → PRODUCTION → SCALE
   │         │      │      │         │          │
   │         │      │      │         │          └── Multi-region, multi-use-case
   │         │      │      │         └── Full deployment, monitoring, SLAs
   │         │      │      └── Limited user group, real data, iterate
   │         │      └── Core features, production-ready, initial users
   │         └── Feasibility proof, 2-4 weeks, limited scope
   └── Business case, stakeholder alignment
```

---

### Questions & Answers

**Q1: What is the difference between POC, MVP, and Production for an AI system? How do you transition between them?**

**Answer:**

| Aspect | POC | MVP | Production |
|--------|-----|-----|------------|
| **Goal** | Prove feasibility | Deliver value | Scale reliably |
| **Duration** | 2-4 weeks | 6-12 weeks | Ongoing |
| **Data** | Sample/synthetic | Real (limited) | Full production |
| **Users** | Internal team | Pilot group (50-200) | All users |
| **Quality** | Best-effort | Acceptable with known gaps | SLA-bound |
| **Infra** | Local/notebook | Cloud dev environment | Production cluster |
| **Monitoring** | Manual checks | Basic dashboards | Full observability |
| **Security** | Minimal | Basic auth + PII | Full compliance |
| **Testing** | Manual | Automated basics | Full test suite |
| **Cost** | Not optimized | Budgeted | Optimized |

**Transition Checklist (POC → MVP):**

```
□ POC validated technical feasibility
□ Business stakeholder sign-off on POC results
□ Clear success metrics defined for MVP
□ Data pipeline designed (not just sample data)
□ Architecture design documented
□ Security review completed
□ Team resourced and sprints planned
□ Cloud infrastructure provisioned
□ CI/CD pipeline basics established
□ Error handling and logging in place
```

**Transition Checklist (MVP → Production):**

```
□ Load testing completed (handle 10x expected traffic)
□ Security audit passed
□ Disaster recovery plan documented and tested
□ Monitoring and alerting configured
□ Runbook for common issues created
□ SLA defined and agreed with stakeholders
□ Data backup and retention policies set
□ Cost optimization completed
□ User training and documentation ready
□ Feedback collection mechanism in place
□ Model evaluation pipeline automated
□ Incident response process defined
□ Compliance review passed (GDPR, SOC2, etc.)
□ Performance benchmarks met
□ Graceful degradation tested (LLM API down, etc.)
```

---

**Q2: How do you handle the "last mile" challenges in productionizing AI systems?**

**Answer:**

The "last mile" refers to the gap between a working prototype and a reliable production system:

**Challenge 1: Edge Cases and Long Tail**
```python
class EdgeCaseHandler:
    """Handle the 20% of cases that cause 80% of issues"""
    
    async def handle(self, query: str, primary_response: str):
        # Detect if response quality is low
        quality = await self.evaluate_quality(query, primary_response)
        
        if quality < 0.5:
            # Strategy 1: Try alternative retrieval
            alt_context = await self.alternative_retrieval(query)
            if alt_context:
                return await self.regenerate(query, alt_context)
            
            # Strategy 2: Simplify and decompose
            sub_answers = await self.decompose_and_answer(query)
            if sub_answers:
                return await self.synthesize(sub_answers)
            
            # Strategy 3: Graceful fallback
            return self.fallback_response(query)
        
        return primary_response
```

**Challenge 2: Performance at Scale**
- Implement caching at multiple levels (semantic cache, result cache)
- Use model distillation for frequent query patterns
- Async processing for non-real-time tasks
- Connection pooling for database/API calls
- Pre-compute embeddings for common queries

**Challenge 3: Maintaining Quality Over Time**
```python
class QualityMaintenance:
    """Continuous quality monitoring and improvement"""
    
    async def daily_evaluation(self):
        # Sample recent interactions
        samples = await self.get_random_samples(n=100)
        
        # Evaluate with LLM judge
        scores = await self.evaluate_batch(samples)
        
        # Detect degradation
        current_avg = np.mean(scores)
        historical_avg = await self.get_historical_average(days=7)
        
        if current_avg < historical_avg * 0.9:  # 10% degradation
            await self.alert("Quality degradation detected",
                          current=current_avg, 
                          historical=historical_avg)
            await self.trigger_investigation(samples, scores)
    
    async def feedback_loop(self, user_feedback):
        """Incorporate user feedback"""
        if user_feedback.rating == "negative":
            # Log for review
            await self.log_negative_feedback(user_feedback)
            
            # Auto-improve: Add to test suite
            await self.add_to_test_suite(
                query=user_feedback.query,
                bad_response=user_feedback.response,
                expected=user_feedback.expected_response
            )
            
            # If pattern detected, update prompts/retrieval
            patterns = await self.detect_failure_patterns()
            if patterns:
                await self.suggest_prompt_updates(patterns)
```

---

## 15. Architecture, Design Patterns & Best Practices

### Detailed Explanation

AI system architecture requires balancing flexibility, reliability, cost, and performance. Key architectural patterns have emerged for production AI systems.

### AI Architecture Patterns

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Gateway Pattern** | Unified LLM access | OpenAI + Anthropic behind single API |
| **Router Pattern** | Intelligent request routing | Simple → small model, complex → large |
| **Fallback Pattern** | Reliability | Primary model down → secondary |
| **Circuit Breaker** | Fault tolerance | Stop calls to failing service |
| **CQRS** | Read/write separation | Separate query vs. ingestion |
| **Event Sourcing** | Audit trail | Track all AI decisions |
| **Saga Pattern** | Multi-step workflows | Agent with compensation logic |
| **Sidecar Pattern** | Cross-cutting concerns | Guardrails as sidecar to each agent |

---

### Questions & Answers

**Q1: Design a Model Gateway pattern for an enterprise that uses multiple LLM providers.**

**Answer:**

```python
from abc import ABC, abstractmethod
from typing import Optional, AsyncGenerator
import asyncio
from dataclasses import dataclass

@dataclass
class LLMRequest:
    messages: list
    model: str
    temperature: float = 0.7
    max_tokens: int = 2000
    stream: bool = False
    user_id: str = None
    
@dataclass
class LLMResponse:
    content: str
    model: str
    provider: str
    usage: dict
    latency_ms: float
    cost_usd: float

class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, request: LLMRequest) -> LLMResponse:
        pass
    
    @abstractmethod
    async def stream(self, request: LLMRequest) -> AsyncGenerator:
        pass
    
    @abstractmethod
    def is_healthy(self) -> bool:
        pass

class ModelGateway:
    """
    Unified gateway for multiple LLM providers with:
    - Load balancing
    - Fallback
    - Rate limiting
    - Cost tracking
    - Caching
    - Observability
    """
    
    def __init__(self):
        self.providers = {
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider(),
            "azure_openai": AzureOpenAIProvider(),
            "bedrock": BedrockProvider(),
        }
        
        # Model to provider mapping
        self.model_routing = {
            "gpt-4": ["azure_openai", "openai"],  # Primary, fallback
            "gpt-4o": ["azure_openai", "openai"],
            "claude-3-opus": ["anthropic", "bedrock"],
            "claude-3-sonnet": ["bedrock", "anthropic"],
        }
        
        self.rate_limiter = TokenBucketRateLimiter()
        self.cache = SemanticCache()
        self.circuit_breakers = {name: CircuitBreaker() for name in self.providers}
        self.cost_tracker = CostTracker()
    
    async def generate(self, request: LLMRequest) -> LLMResponse:
        # 1. Check rate limits
        if not await self.rate_limiter.allow(request.user_id):
            raise RateLimitError("Rate limit exceeded")
        
        # 2. Check cache
        cached = await self.cache.get(request)
        if cached:
            return cached
        
        # 3. Get provider chain (primary + fallbacks)
        providers = self.get_providers(request.model)
        
        # 4. Try each provider with circuit breaker
        for provider_name in providers:
            provider = self.providers[provider_name]
            circuit_breaker = self.circuit_breakers[provider_name]
            
            if not circuit_breaker.is_closed():
                continue  # Skip unhealthy providers
            
            try:
                response = await asyncio.wait_for(
                    provider.generate(request),
                    timeout=60
                )
                
                # Track cost
                self.cost_tracker.track(request.user_id, response.cost_usd)
                
                # Cache response
                await self.cache.set(request, response)
                
                # Log for observability
                self.log_request(request, response, provider_name)
                
                return response
                
            except Exception as e:
                circuit_breaker.record_failure()
                self.log_error(provider_name, e)
                continue  # Try next provider
        
        raise AllProvidersFailedError("All LLM providers are unavailable")
    
    def get_providers(self, model: str) -> list:
        """Get ordered list of providers for a model"""
        if model in self.model_routing:
            return self.model_routing[model]
        
        # Default routing based on model prefix
        if model.startswith("gpt"):
            return ["azure_openai", "openai"]
        elif model.startswith("claude"):
            return ["anthropic", "bedrock"]
        else:
            return list(self.providers.keys())


class CircuitBreaker:
    """Prevent calls to unhealthy providers"""
    
    def __init__(self, failure_threshold=5, reset_timeout=60):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.state = "closed"  # closed (healthy), open (unhealthy), half-open (testing)
        self.last_failure_time = None
    
    def is_closed(self) -> bool:
        if self.state == "closed":
            return True
        elif self.state == "open":
            # Check if enough time passed to try again
            if time.time() - self.last_failure_time > self.reset_timeout:
                self.state = "half-open"
                return True
            return False
        return True  # half-open: allow one request
    
    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = "open"
    
    def record_success(self):
        self.failure_count = 0
        self.state = "closed"
```

---

**Q2: What are the key design patterns for building reliable AI applications?**

**Answer:**

**1. Retry with Exponential Backoff:**
```python
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=30),
    retry=retry_if_exception_type((RateLimitError, TimeoutError))
)
async def call_llm_with_retry(request):
    return await llm.generate(request)
```

**2. Graceful Degradation:**
```python
class GracefulDegradation:
    """Provide reduced but functional service when components fail"""
    
    async def answer(self, query: str):
        try:
            # Full capability: RAG + Agent
            return await self.full_rag_agent(query)
        except VectorStoreError:
            # Fallback 1: LLM without RAG
            return await self.llm_only(query, 
                disclaimer="Note: Answer based on training data only")
        except LLMError:
            # Fallback 2: Cached/pre-computed answers
            cached = await self.find_similar_cached(query)
            if cached:
                return cached
            # Fallback 3: Human escalation
            return await self.escalate_to_human(query)
```

**3. Observability-First Design:**
```python
from opentelemetry import trace
from opentelemetry.trace import StatusCode

tracer = trace.get_tracer(__name__)

class ObservableRAG:
    @tracer.start_as_current_span("rag.pipeline")
    async def answer(self, query: str):
        span = trace.get_current_span()
        span.set_attribute("query.length", len(query))
        
        with tracer.start_span("rag.retrieve") as retrieve_span:
            docs = await self.retrieve(query)
            retrieve_span.set_attribute("docs.count", len(docs))
            retrieve_span.set_attribute("docs.relevance_scores", 
                                       [d.score for d in docs])
        
        with tracer.start_span("rag.generate") as gen_span:
            response = await self.generate(query, docs)
            gen_span.set_attribute("response.tokens", response.usage.total_tokens)
            gen_span.set_attribute("response.cost", response.cost)
        
        span.set_status(StatusCode.OK)
        return response
```

**4. Idempotent Operations:**
```python
class IdempotentProcessor:
    """Ensure operations can be safely retried"""
    
    async def process(self, request_id: str, payload: dict):
        # Check if already processed
        existing = await self.store.get(request_id)
        if existing:
            return existing  # Return cached result
        
        # Process
        result = await self.do_work(payload)
        
        # Store result with request_id
        await self.store.set(request_id, result, ttl=86400)
        
        return result
```

**5. Event-Driven Architecture:**
```python
class AIEventBus:
    """Decouple AI components with events"""
    
    events = {
        "document.ingested": [update_vector_store, update_knowledge_graph],
        "query.received": [log_query, check_cache],
        "response.generated": [evaluate_quality, track_cost, log_interaction],
        "quality.degraded": [alert_team, trigger_retraining],
        "feedback.received": [update_training_data, adjust_prompts],
    }
```

---

## Summary: Key Takeaways for Interview Preparation

### Top 10 Things to Demonstrate

1. **Hands-on coding ability** – Be ready to write code, not just describe architectures
2. **End-to-end thinking** – From business problem to production system
3. **Trade-off awareness** – Cost vs. quality, latency vs. accuracy, complexity vs. maintainability
4. **Production mindset** – Monitoring, error handling, scalability, security
5. **Business acumen** – Translate AI capabilities into ROI
6. **Current knowledge** – Latest models, frameworks, techniques (as of 2024-2025)
7. **System design skills** – Architecture diagrams, component interactions
8. **Evaluation rigor** – How to measure and improve AI system quality
9. **Safety consciousness** – Guardrails, responsible AI, compliance
10. **Communication clarity** – Explain complex concepts simply

### Quick Reference: Technology Stack

```
LLMs:         GPT-4o, Claude 3.5, LLaMA 3, Mistral, Gemini
Frameworks:   LangChain, LangGraph, Semantic Kernel, CrewAI, AutoGen
Vector DBs:   Qdrant, Pinecone, Weaviate, ChromaDB, Milvus
Embeddings:   BGE, E5, OpenAI ada-002, Cohere embed-v3
Serving:      vLLM, TGI, Ollama, TorchServe
Cloud:        Azure OpenAI, AWS Bedrock, GCP Vertex AI
Monitoring:   LangSmith, Langfuse, Phoenix, OpenTelemetry
Evaluation:   RAGAS, DeepEval, Promptfoo, LangSmith
Guardrails:   NeMo Guardrails, Guardrails AI, Azure Content Safety
APIs:         FastAPI, Flask, gRPC
Infra:        Docker, Kubernetes, Terraform, GitHub Actions
```

---

## 16. Project Deep-Dive: Synaptica – Full-Stack AI Platform (GSK MSAT Quality)

> **📋 Source Reliability Legend for this section:**
> 
> | Symbol | Meaning |
> |--------|--------|
> | 📄 | **Confirmed** — directly sourced from repository README, architecture docs, or source code visible via GitHub |
> | 🔍 | **Inferred** — logically deduced from architecture docs, file structure, or naming patterns (repos are SSO-protected) |
> | 💡 | **Best Practice** — standard engineering practice applied based on the tech stack, not confirmed in repo |

### Project Overview

📄 **Synaptica** is a production enterprise application built for GSK's **MSAT (Manufacturing Science and Technology) Quality** team. The platform automates pharmaceutical quality report generation using AI — specifically Claude LLM-powered analysis of PDF documents (batch records, CAPA reports, deviation summaries) to populate dynamic elements in compliance reports.

The system spans **two interconnected repositories** with different concerns:

| Repository | Purpose | Stack |
|-----------|---------|-------|
| **Fullstack-Synaptica** | Report configuration, template management, user-facing SPA, async report generation | Next.js 15, React 19, FastAPI, Azure Functions, SQL Server |
| **ROBY-HVR-FASTAPI** (ROBY Analyzer) | AI-powered PDF analysis microservice with Claude tool-calling | FastAPI, Claude Sonnet 4, Kong Gateway, pdfplumber |

### High-Level System Architecture

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                        SYNAPTICA PLATFORM ARCHITECTURE                           │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  FULLSTACK SYNAPTICA (Report Management & Generation)                           │
│  ┌──────────────┐     ┌──────────────────┐     ┌────────────────────────┐       │
│  │  Frontend    │     │  Backend (BE)     │     │  Azure Function App   │       │
│  │  Next.js 15  │────▶│  FastAPI          │────▶│  Service Bus Trigger  │       │
│  │  React 19    │REST │  SQLAlchemy ORM   │Queue│  Report Processor     │       │
│  │  MSAL Auth   │     │  Azure AD Auth    │     │  AI Component Client  │       │
│  │  :3000       │     │  SQL Server       │     └─────────┬────────────┘       │
│  └──────────────┘     │  Blob Storage     │               │                     │
│                       │  Service Bus      │               │ HTTP POST           │
│                       └──────────────────┘               │ /v1/generate        │
│                                                           ▼                     │
│  ROBY ANALYZER (AI Analysis Engine)                                             │
│  ┌──────────────────┐     ┌───────────────────────────────────────────┐         │
│  │  Backend          │     │  AI Component (FastAPI :8001)             │         │
│  │  FastAPI :8002    │────▶│  ┌─────────────────────────────────────┐ │         │
│  │  Templates CRUD   │REST │  │ Analyzer (Claude tool-calling loop) │ │         │
│  │  File Storage     │     │  │ Evaluator (GAR metrics)             │ │         │
│  │  Orchestration    │     │  │ PDF Extractor (pdfplumber)          │ │         │
│  └──────────────────┘     │  │ Direct Claude Client                │ │         │
│                            │  └──────────────┬──────────────────────┘ │         │
│                            └──────────────────┼───────────────────────┘         │
│                                               │                                  │
│                                               ▼                                  │
│                            ┌──────────────────────────────────────┐             │
│                            │  Kong API Gateway (Enterprise)       │             │
│                            │  PingFederate OAuth2                 │             │
│                            │         │                            │             │
│                            │         ▼                            │             │
│                            │  Claude Sonnet 4 (Anthropic)         │             │
│                            └──────────────────────────────────────┘             │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### Technology Stack (Complete)

**Frontend (Fullstack Synaptica):**

| Category | Library | Version | Purpose |
|----------|---------|---------|--------|
| Framework | Next.js (App Router) | 15.5.9 | File-based routing, SSR/SSG, standalone build |
| UI | React | 19.2.0 | Functional components with hooks |
| Language | TypeScript | 5.9.3 | Static type-checking (strict mode) |
| Styling | Tailwind CSS | 4.1.10 | Utility-first CSS framework |
| Data Fetching | TanStack React Query | 5.90.7 | Server-state caching & background refresh |
| HTTP Client | Axios | 1.13.2 | REST API calls with interceptors |
| Global State | Zustand | 5.0.8 | Lightweight global state management |
| Form State | React Hook Form | 7.66.0 | Performant form management |
| Validation | Zod | 4.1.12 | Runtime schema validation + type inference |
| Auth | @azure/msal-browser + msal-react | 4.26.0 / 3.0.21 | Azure AD (Microsoft Entra ID) SSO |
| Unit Testing | Vitest | — | Fast unit & component testing |
| E2E Testing | Playwright | — | Cross-browser end-to-end testing |
| Code Quality | ESLint + Prettier + Husky | — | Linting, formatting, git hooks |

**Backend (Fullstack Synaptica):**

| Category | Library | Purpose |
|----------|---------|--------|
| Framework | FastAPI | High-performance async API framework |
| ORM | SQLAlchemy | Declarative ORM with async support |
| Validation | Pydantic | Request/response schema validation |
| Dependency Mgmt | Poetry | Modern Python dependency management |
| Auth | Azure AD (fastapi-azure-auth) | Bearer token validation |
| Database | Azure SQL Server | Enterprise relational database |
| Storage | Azure Blob Storage | Document/file storage |
| Messaging | Azure Service Bus | Async report generation queue |
| Telemetry | Application Insights | Azure-native APM & tracing |
| Testing | pytest | Unit & integration testing |

**AI Component (ROBY Analyzer):**

| Category | Library | Purpose |
|----------|---------|--------|
| Framework | FastAPI | AI microservice API |
| LLM | Claude Sonnet 4 (Anthropic) | Large language model for analysis |
| Gateway | Kong (KGW) + PingFederate | Enterprise API gateway + OAuth2 |
| PDF Extraction | pdfplumber | Text-based PDF parsing |
| HTTP Client | httpx | Async HTTP for Claude API calls |
| TLS | truststore | System trust store injection |
| Telemetry | OpenTelemetry | Distributed tracing |
| Proxy | LiteLLM (AIGA Proxy) | OpenAI-compatible proxy for Claude |
| Containerization | Docker Compose | 3-service network orchestration |

### Backend Architecture (Clean Architecture)

```
src/backend/
├── src/
│   ├── api/                    # FastAPI route definitions
│   │   └── v1/
│   │       ├── routes.py       # Route registration
│   │       └── endpoints/      # Endpoint handlers
│   ├── core/                   # Core infrastructure
│   │   ├── config.py           # Settings (env vars, Pydantic BaseSettings)
│   │   ├── container.py        # Dependency Injection container
│   │   ├── database.py         # SQLAlchemy async engine
│   │   ├── dependencies.py     # FastAPI Depends() wrappers
│   │   ├── factory.py          # App factory (create_app)
│   │   ├── middleware.py       # CORS, logging, error middleware
│   │   └── security.py         # Azure AD token validation
│   ├── model/                  # SQLAlchemy ORM models
│   │   └── base_model.py       # Declarative base
│   ├── repository/             # Data Access Layer (Repository Pattern)
│   ├── schema/                 # Pydantic request/response schemas
│   ├── services/               # Business logic layer
│   ├── helper/                 # Azure Blob, KeyVault, ServiceBus helpers
│   └── util/                   # Shared utilities
├── tests/
│   ├── unit_tests/
│   └── integration_tests/
└── pyproject.toml              # Poetry dependencies
```

### AI Component Internal Architecture

```
ai-component/
├── app/
│   ├── main.py                          # FastAPI entry — /v1/generate, /analyze, /evaluate
│   ├── models/
│   │   └── schemas.py                   # Pydantic: V1GenerateRequest, AnalysisRequest, etc.
│   ├── services/
│   │   ├── direct_claude_client.py      # Claude API client via Kong Gateway
│   │   ├── analyzer.py                  # Tool-calling loop orchestrator
│   │   ├── evaluator.py                 # GAR evaluation (Groundedness, Accuracy, Relevance)
│   │   ├── kong_client.py               # Kong Gateway auth + request forwarding
│   │   ├── content_manager.py           # File content preparation
│   │   ├── pdf_extractor.py             # pdfplumber text extraction
│   │   ├── document_processor.py        # Document enrichment + prompt building
│   │   ├── agent_loop.py                # Agent loop execution
│   │   ├── document_workspace.py        # Workspace for document operations
│   │   └── tools.py                     # Analysis tools (view_file, search_text, analyze_data)
│   ├── telemetry.py                     # Request telemetry (TelemetryCollector)
│   └── otel_setup.py                    # OpenTelemetry instrumentation
└── requirements.txt
```

### Frontend Architecture Layers

```
┌──────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                         │
│  Pages (app/**/page.tsx), Layouts, UI Components              │
│  No direct API calls — receives data via props or hooks      │
├──────────────────────────────────────────────────────────────┤
│                   BUSINESS LOGIC LAYER                        │
│  Query Hooks (hooks/queries/), Mutation Hooks                │
│  useApiRequest, useDebounce, useMsalUser                     │
├──────────────────────────────────────────────────────────────┤
│                  STATE MANAGEMENT LAYER                       │
│  Zustand Stores (auth, report.config, report.form)           │
│  TanStack Query Cache | React Hook Form + Zod               │
├──────────────────────────────────────────────────────────────┤
│                  API INTEGRATION LAYER                        │
│  ApiProvider (Axios instance + MSAL token injection)         │
│  Interceptors | apiPathBuilder | Error handling              │
├──────────────────────────────────────────────────────────────┤
│                  VALIDATION LAYER                             │
│  Zod Schemas (z.infer<> for type inference)                  │
├──────────────────────────────────────────────────────────────┤
│                  EXTERNAL                                     │
│  Python FastAPI Backend (REST API)                            │
└──────────────────────────────────────────────────────────────┘
```

---

### Questions & Answers

**Q1: Walk us through the overall Synaptica architecture. Why did you split it into multiple repositories and services?**

**Answer:**

Synaptica follows a **microservices architecture** split across two repositories with clear separation of concerns:

**Repository 1 — Fullstack Synaptica (Report Management Platform):**
- Frontend (Next.js 15 SPA) — user-facing report configuration, template management
- Backend (FastAPI) — REST APIs, CRUD operations, SQL Server, Azure integrations
- Azure Function App — async report generation triggered by Service Bus

**Repository 2 — ROBY Analyzer (AI Analysis Engine):**
- Backend orchestrator (FastAPI :8002) — file upload, template CRUD, routing
- AI Component (FastAPI :8001) — Claude tool-calling, PDF extraction, evaluation

**Why this separation:**

1. **Independent Scaling**: The AI component is GPU/compute-intensive. Separating it allows scaling the AI service independently from the web application. When 100 reports queue simultaneously, we scale AI pods without touching the frontend.

2. **Team Autonomy**: The frontend team works on React/TypeScript, the backend team on Python/FastAPI, and the AI team on LLM orchestration — all with independent CI/CD pipelines and release cycles.

3. **Technology Isolation**: The AI component has unique dependencies (pdfplumber, httpx for Claude API, OpenTelemetry) that don't belong in the report management backend. Isolating prevents dependency conflicts.

4. **Fault Isolation**: If the AI Component crashes (Claude API timeout, PDF parsing failure), the main application remains functional. Users can still configure reports; only AI-powered generation is affected.

5. **Reusability**: The AI Component exposes standard REST endpoints (`POST /v1/generate`, `POST /analyze`). Other GSK applications can consume it without depending on Synaptica's full stack.

6. **Security Boundary**: The AI Component handles sensitive LLM interactions through Kong Gateway with PingFederate OAuth2. This security boundary is cleanly isolated from the user-facing authentication (Azure AD/MSAL).

---

**Q2: Why did you choose Next.js 15 with React 19 for the frontend? Why not a simpler React SPA or Angular?**

**Answer:**

We chose **Next.js 15 with App Router** specifically, but used it as a **frontend-only SPA** (no Next.js API routes — all data comes from the Python FastAPI backend). Here's why:

**Why Next.js over plain React (CRA/Vite):**

1. **File-based Routing**: Next.js App Router gives us automatic route generation from the `app/` directory structure. For a multi-page enterprise app (Dashboard, Reports, Templates, Reference Tables, Roles, About), this eliminates manual route configuration.

2. **Layout System**: Nested layouts (`layout.tsx`) allow us to define the auth gate, header, and navbar once. All child routes inherit them automatically:
   ```
   RootLayout (Providers, Auth Gate)
   └── ConditionalLayout (Header + Navbar)
       ├── /dashboard → Dashboard page
       ├── /reports → Reports page
       ├── /reference-table → Reference Tables
       └── /templates → Templates
   ```

3. **Standalone Build**: `output: 'standalone'` produces a minimal production build for Docker. This is critical for Azure Container Apps deployment — the image size drops dramatically.

4. **Future SSR Capability**: While currently a client-side SPA, the architecture allows gradual migration to Server Components for performance-critical pages without rewriting.

**Why not Angular:**
- Angular's opinionated structure adds unnecessary complexity for our team size
- React's ecosystem (TanStack Query, Zustand, Zod) is more modular and lightweight
- Faster development velocity with React hooks vs Angular's service/module pattern
- Better alignment with GSK's broader React standardization

**Why React 19 specifically:**
- Concurrent rendering for better UI responsiveness during heavy data operations
- Improved Suspense for data-fetching patterns we use with TanStack Query
- React Compiler (future) readiness for automatic performance optimization

---

**Q3: Explain your state management strategy. Why Zustand + TanStack Query + React Hook Form instead of Redux or a single solution?**

**Answer:**

We deliberately chose a **multi-store architecture** where each library owns a specific type of state:

```
┌──────────────────────────────────────────────────────────────┐
│                   STATE MANAGEMENT STRATEGY                    │
├──────────────┬──────────────────────────────────┬────────────┤
│   State Type │   Library                        │ Persistence │
├──────────────┼──────────────────────────────────┼────────────┤
│ Server State │ TanStack Query (React Query)     │ Memory cache│
│ Global UI    │ Zustand                          │ localStorage│
│ Form State   │ React Hook Form + Zod            │ None        │
│ Auth State   │ Zustand (auth.store.ts)           │ localStorage│
│ URL State    │ Next.js App Router (searchParams) │ URL         │
└──────────────┴──────────────────────────────────┴────────────┘
```

**Why TanStack Query for server state (not Redux Thunk/RTK Query):**

1. **Automatic Caching & Background Refresh**: When a user navigates away from Reports and comes back, TanStack Query serves cached data instantly while revalidating in the background. Zero boilerplate.

2. **Stale-While-Revalidate**: Our report data doesn't change every second. TanStack Query's `staleTime` and `gcTime` let us define exactly how fresh data needs to be:
   ```typescript
   const { data: reports } = useQuery({
     queryKey: [QUERY_KEYS.REPORT_INSTANCES],
     queryFn: () => apiGet('/api/v1/reports'),
     staleTime: 5 * 60 * 1000,  // 5 min before refetch
     gcTime: 30 * 60 * 1000,     // 30 min cache retention
   });
   ```

3. **Mutations with Optimistic Updates**: Report creation/deletion gives instant UI feedback:
   ```typescript
   const mutation = useMutation({
     mutationFn: createReport,
     onMutate: async (newReport) => {
       await queryClient.cancelQueries([QUERY_KEYS.REPORT_INSTANCES]);
       const previous = queryClient.getQueryData([QUERY_KEYS.REPORT_INSTANCES]);
       queryClient.setQueryData([QUERY_KEYS.REPORT_INSTANCES], old => [...old, newReport]);
       return { previous };
     },
     onError: (err, _, context) => {
       queryClient.setQueryData([QUERY_KEYS.REPORT_INSTANCES], context.previous);
     },
     onSettled: () => queryClient.invalidateQueries([QUERY_KEYS.REPORT_INSTANCES]),
   });
   ```

4. **Built-in Loading/Error States**: Every query hook returns `isLoading`, `isError`, `data` — eliminating manual state tracking.

**Why Zustand over Redux:**

1. **Minimal Boilerplate**: A complete Zustand store is 10 lines vs Redux's action creators + reducers + selectors + middleware:
   ```typescript
   // auth.store.ts — complete store
   export const useAuthStore = create(
     persist(
       (set) => ({
         user: null,
         token: null,
         setUser: (user) => set({ user }),
         setToken: (token) => set({ token }),
         logout: () => set({ user: null, token: null }),
       }),
       { name: 'auth-storage' }
     )
   );
   ```

2. **No Context Wrapper Needed**: Zustand doesn't require a Provider wrapper (unlike Redux). Reduces the provider nesting we already have with MSAL + TanStack Query + Axios.

3. **Focused Stores**: One concern per store (`auth.store.ts`, `report.config.store.ts`, `report.form.store.ts`). Each is tiny, testable, and independently persisted.

4. **Bundle Size**: Zustand is ~1KB vs Redux Toolkit's ~11KB. For an enterprise app with multiple heavy dependencies (MSAL, TanStack, Axios), every KB matters.

**Why React Hook Form + Zod for forms:**

1. **Uncontrolled Components**: React Hook Form uses refs, not state. On a complex report configuration form with 30+ fields, this prevents re-renders on every keystroke.

2. **Zod Integration**: Single schema for validation AND TypeScript types:
   ```typescript
   const reportSchema = z.object({
     title: z.string().min(1, 'Required'),
     description: z.string().optional(),
     templateId: z.string().uuid(),
     frequency: z.enum(['weekly', 'monthly', 'quarterly']),
   });
   
   type ReportForm = z.infer<typeof reportSchema>; // Auto-generated type!
   ```

---

**Q4: Why FastAPI for the backend instead of Django, Flask, or Node.js?**

**Answer:**

FastAPI was chosen for both the Fullstack backend and the AI Component for specific technical reasons:

**1. Async-First Architecture:**
The AI Component makes long-running HTTP calls to Claude via Kong Gateway (10-60 seconds per analysis). FastAPI's native `async/await` support means the server isn't blocked during these calls:
```python
@app.post("/v1/generate", response_model=V1GenerateResponse)
async def v1_generate(request: V1GenerateRequest):
    client = _get_v1_claude_client()
    # Non-blocking — other requests served while waiting for Claude
    result = await client.generate(request.prompt)
    return result
```
With Flask, we'd need Celery or similar for async. Django's async support is still maturing.

**2. Pydantic-Native Validation:**
FastAPI uses Pydantic for request/response models. This gives us automatic validation, serialization, and OpenAPI doc generation:
```python
class V1GenerateRequest(BaseModel):
    prompt: str
    ai_model: str = "claude-sonnet"
    report_instance_id: str
    dyn_element_id: int
    dyn_element_name: str

# FastAPI auto-validates, auto-generates Swagger docs
```
With Flask, we'd need marshmallow/cerberus manually. With Django REST Framework, it's possible but more verbose.

**3. OpenAPI Auto-Documentation:**
FastAPI generates Swagger UI at `/docs` automatically. For a multi-service architecture where the Backend calls the AI Component, having accurate API contracts is critical. Both teams reference the auto-generated Swagger.

**4. Dependency Injection:**
FastAPI's `Depends()` system powers our clean architecture:
```python
from src.core.dependencies import get_current_user, get_user_email

@app.get("/me")
async def get_my_profile(
    user_id: str = Depends(get_user_object_id),
    email: str = Depends(get_user_email),
    user: dict = Depends(get_current_user),
):
    return {"user_id": user_id, "email": email}
```
The `AppContainer` class manages singleton services (database, Azure clients) with factory pattern:
```python
container = AppContainer()
app = create_app()  # Factory creates FastAPI with all middleware, auth, routes
```

**5. Performance:**
FastAPI on Uvicorn is one of the fastest Python frameworks (benchmarked near Go/Node.js for I/O). For an API that proxies between frontend, database, and AI service, throughput matters.

**Why not Node.js/Express:**
- The AI team works in Python (ML/NLP ecosystem)
- SQLAlchemy + Alembic for database migrations is more mature than Prisma/Sequelize for SQL Server
- Azure SDKs for Python (Blob, Service Bus, Key Vault) are first-class citizens

---

**Q5: Explain the Claude tool-calling loop in the AI Component. How does it work and why this approach?**

**Answer:**

The AI Component uses **Claude's native tool-calling** (function calling) to analyze PDF documents. Instead of dumping entire PDFs into the context window, Claude interacts with the document via tools:

**Tool-Calling Loop Architecture:**

```
User Prompt + Tool Definitions
        │
        ▼
┌─────────────────────┐
│  Claude Sonnet 4    │
│  via Kong Gateway   │
└────────┬────────────┘
         │
    ┌────▼────┐
    │ Response │──── stop_reason = "end_turn" ──── ▶ Return Answer
    └────┬────┘
         │
    stop_reason = "tool_use"
         │
    ┌────▼──────────────────────────────┐
    │  Execute Tool Locally             │
    │  ┌─────────────────────────────┐  │
    │  │ view_file: Read PDF section │  │
    │  │ search_text: Find keywords  │  │
    │  │ analyze_data: Extract data  │  │
    │  └─────────────────────────────┘  │
    └────────────────┬─────────────────┘
                     │
              Tool Result (truncated to 3000 chars)
                     │
              sleep(3s) rate-limit safety
                     │
                     ▼
              Feed result back to Claude
              (Continue conversation)
                     │
              Loop (up to 20 iterations)
```

**Why Tool-Calling Instead of Stuffing Full PDF into Context:**

1. **Context Window Efficiency**: A pharmaceutical batch record can be 200+ pages. At ~4 chars/token, that's 200K+ tokens. Claude Sonnet's context window would be exhausted, and cost would be enormous. Tool-calling lets Claude surgically request only the sections it needs.

2. **Precision**: Claude decides WHAT to look for. For a CAPA summary, it might:
   - `view_file(page=1-3)` → Read the executive summary
   - `search_text("corrective action")` → Find all mentions
   - `view_file(page=45-48)` → Deep-dive into the corrective action section
   - `analyze_data("deviation trends")` → Extract specific data points

3. **Cost Control**: Only the relevant sections are sent as tokens. A typical analysis uses 1,200 prompt tokens + 450 completion tokens instead of 200K+ for full-document stuffing.

4. **Auditability**: Every tool call is logged in telemetry. For pharmaceutical compliance, we need to prove which document sections the AI read to generate its answer.

**Implementation (Simplified):**

```python
class AIAnalyzer:
    """Orchestrates Claude tool-calling loop for document analysis"""
    
    def __init__(self, claude_client, tools):
        self.client = claude_client
        self.tools = tools  # view_file, search_text, analyze_data
    
    async def analyze(self, prompt: str, files: list) -> AnalysisResult:
        messages = [{"role": "user", "content": prompt}]
        tool_definitions = self.tools.get_definitions()
        
        for iteration in range(20):  # Max 20 tool-calling iterations
            response = await self.client.send(
                messages=messages,
                tools=tool_definitions,
                system="You are a pharmaceutical quality analyst..."
            )
            
            if response.stop_reason == "end_turn":
                return AnalysisResult(answer=response.content)
            
            if response.stop_reason == "tool_use":
                for tool_call in response.tool_calls:
                    # Execute tool locally (no external API call)
                    result = await self.tools.execute(
                        tool_call.name, 
                        tool_call.arguments,
                        files=files
                    )
                    # Truncate to prevent context overflow
                    result = result[:3000]
                    
                    messages.append({"role": "assistant", "content": response.content})
                    messages.append({"role": "user", "content": [
                        {"type": "tool_result", "tool_use_id": tool_call.id, 
                         "content": result}
                    ]})
                
                await asyncio.sleep(3)  # Rate-limit safety for Kong Gateway
        
        return AnalysisResult(answer="Max iterations reached", partial=True)
```

---

**Q6: How does the evaluation system work? What are GAR metrics?**

**Answer:**

**GAR = Groundedness, Accuracy, Relevance** — three evaluation metrics computed after every AI analysis:

| Metric | What It Measures | How It's Computed |
|--------|-----------------|------------------|
| **Groundedness** | Is the answer supported by the source documents? | Claude evaluates if each claim in the answer has evidence in the retrieved PDF sections |
| **Accuracy** | Is the information factually correct? | Cross-reference answer claims against document content |
| **Relevance** | Does the answer address the original prompt? | Semantic alignment between prompt and generated answer |

**Why GAR (not RAGAS or generic metrics):**

1. **Pharmaceutical Compliance**: In pharma manufacturing, a hallucinated CAPA status or fabricated deviation count can have regulatory consequences. Groundedness is the most critical metric — every claim MUST trace back to the source document.

2. **No Vector Database = No RAGAS Context Metrics**: Unlike traditional RAG, Synaptica uses tool-calling (not embedding-based retrieval). RAGAS metrics like "context precision" and "context recall" don't apply because there's no retriever component — Claude actively pulls what it needs via tools.

3. **LLM-as-Judge Pattern**: The evaluator uses a second Claude call (separate from the analysis) to judge the output:

```python
class AIEvaluator:
    """Evaluates AI analysis outputs using LLM-as-Judge"""
    
    async def evaluate(self, prompt, answer, source_content) -> dict:
        evaluation_prompt = f"""
        You are an expert evaluator. Score the following on a scale of 0-1:
        
        ORIGINAL PROMPT: {prompt}
        AI ANSWER: {answer}
        SOURCE DOCUMENTS: {source_content}
        
        Score each criterion:
        1. GROUNDEDNESS: Is every claim in the answer supported by the source?
        2. ACCURACY: Are the facts, numbers, and dates correct?
        3. RELEVANCE: Does the answer fully address the prompt?
        
        Return JSON: {{"groundedness": 0.X, "accuracy": 0.X, "relevance": 0.X}}
        """
        
        result = await self.claude_client.send(evaluation_prompt)
        return parse_scores(result)
```

**Response Structure:**
```json
{
    "request_id": "uuid",
    "answer": "The CAPA completion rate for Q1 2026 was 94.2%...",
    "metrics": {
        "groundedness": 0.92,
        "accuracy": 0.88,
        "relevance": 0.95
    }
}
```

**Threshold-Based Actions:**
- Groundedness < 0.7 → Flag for human review
- Accuracy < 0.8 → Do not auto-populate report element
- All metrics > 0.85 → Auto-approve for report inclusion

---

**Q7: Why Axios with interceptors instead of the native Fetch API? How does the API integration work?**

**Answer:**

**Why Axios over Fetch:**

1. **Request/Response Interceptors**: The killer feature for enterprise apps. Our interceptor chain:
   ```
   Request Flow:  User Action → Axios → MSAL Token Interceptor → Add Bearer → Send
   Response Flow: API Response → 401 Check → Token Refresh → Retry → Return Data
   ```

2. **Automatic MSAL Token Injection**: Every API call needs an Azure AD Bearer token. With Axios interceptors, this is handled once, globally:
   ```typescript
   // ApiProvider.tsx — Context-based Axios instance
   const axiosInstance = axios.create({
     baseURL: process.env.NEXT_PUBLIC_API_URL,
     timeout: API_TIMEOUT,     // 10 seconds
   });
   
   // Request interceptor: inject MSAL token
   axiosInstance.interceptors.request.use(async (config) => {
     const token = await acquireTokenSilent(msalInstance, loginRequest);
     config.headers.Authorization = `Bearer ${token.accessToken}`;
     return config;
   });
   
   // Response interceptor: handle 401 (token expired)
   axiosInstance.interceptors.response.use(
     (response) => response,
     async (error) => {
       if (error.response?.status === 401) {
         // Force token refresh and retry
         const token = await acquireTokenSilent(msalInstance, loginRequest);
         error.config.headers.Authorization = `Bearer ${token.accessToken}`;
         return axiosInstance(error.config);
       }
       return Promise.reject(error);
     }
   );
   ```

3. **Timeout & Retry**: Fetch doesn't have built-in timeout. Axios does (`API_TIMEOUT = 10000`). Combined with TanStack Query's retry (`API_RETRY_COUNT = 3`), we get resilient API calls.

4. **Request Cancellation**: Axios integrates with `AbortController`. When a user navigates away mid-request, TanStack Query cancels the Axios call automatically.

**The Full API Integration Flow:**

```
React Component
  │ uses
  ▼
Custom Hook (TanStack Query)     ← useReports(), useReferenceTable()
  │ calls
  ▼
useApiRequest Hook               ← apiGet(), apiPost(), apiPatch()
  │ uses
  ▼
Axios Instance + Interceptors    ← MSAL token injection, 401 handling
  │ HTTP
  ▼
Python FastAPI Backend            ← /api/v1/*
  │ HTTP
  ▼
Zod Schema Validation             ← Response validated against schema
  │ returns
  ▼
TanStack Query Cache              ← Cached, background-refreshed
  │ renders
  ▼
React Component (re-renders)      ← Loading → Data → Error states
```

**Why not Fetch:**
- No interceptors (would need wrapper functions)
- No automatic JSON parsing for errors
- No timeout support
- No request progress tracking
- Verbose error handling (Fetch doesn't reject on 4xx/5xx)

---

**Q8: How does authentication work across the full stack? Walk us through the auth flow.**

**Answer:**

The system uses **two separate authentication mechanisms** for different boundaries:

```
┌──────────────────────────────────────────────────────────────────────┐
│                     AUTHENTICATION ARCHITECTURE                       │
├──────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  USER → FRONTEND → BACKEND                                           │
│  ════════════════════════                                              │
│  Azure AD (Microsoft Entra ID) via MSAL                               │
│  • OAuth 2.0 Authorization Code + PKCE                                │
│  • Frontend: @azure/msal-browser acquires tokens                      │
│  • Backend: fastapi-azure-auth validates Bearer tokens                │
│  • Session: sessionStorage (MSAL cache, not localStorage for security)│
│                                                                        │
│  AI COMPONENT → KONG GATEWAY → CLAUDE                                 │
│  ════════════════════════════════════                                   │
│  PingFederate OAuth2 (client_credentials grant)                       │
│  • AI Component authenticates as a service (not a user)               │
│  • Kong Gateway validates token, routes to Claude API                 │
│  • Token cached and refreshed automatically (expires_in=3599s)        │
│                                                                        │
└──────────────────────────────────────────────────────────────────────┘
```

**Frontend Auth Flow (MSAL):**

```
1. User opens app → MsalClientProvider checks auth state
2. Not authenticated → UnauthenticatedTemplate → Redirect to Azure AD login
3. User logs in → Azure AD returns authorization code
4. MSAL exchanges code for tokens (access + id + refresh)
5. Tokens stored in sessionStorage (SSR-safe MSAL instance via lib/msal.ts)
6. Every API call → Axios interceptor calls acquireTokenSilent()
7. Token expired → MSAL auto-refreshes using refresh token
8. Refresh token expired → User redirected to login again
```

**Key Design Decisions:**

- **sessionStorage over localStorage**: MSAL tokens in sessionStorage are cleared when the tab closes. This is a security requirement — pharmaceutical data shouldn't persist in browser storage.
- **SSR-safe MSAL Instance**: `lib/msal.ts` uses a factory pattern to create MSAL instances only on the client side (Next.js renders on both server and client).
- **Auth Gate Pattern**: `MsalClientProvider` wraps the entire app. Only `AuthenticatedTemplate` children render for logged-in users. Unauthenticated users see only the login page.

---

**Q9: Why pdfplumber for PDF extraction? What were the alternatives and trade-offs?**

**Answer:**

| Library | Strengths | Weaknesses | Why Not Chosen |
|---------|-----------|------------|----------------|
| **pdfplumber** ✅ | Precise text extraction with position info, table extraction, lightweight | Text-based PDFs only, no OCR | **Chosen** — our docs are text-based |
| PyPDF2/PyMuPDF | Fast, widely used | Less precise text positioning | Less accurate table extraction |
| Unstructured.io | Multi-format, OCR, layout analysis | Heavy dependency, slower | Over-engineered for our use case |
| Azure Document Intelligence | OCR, pre-built models, handwriting | Cloud API cost, latency, external dependency | Added latency + cost per page |
| Tesseract/EasyOCR | Free OCR | Requires image conversion, lower accuracy | Our PDFs are text-based, not scanned |
| Mistral AI OCR | Advanced OCR with LLM | Not production-ready at time of decision | Existed in code (`ocr_client.py`) but not wired |

**Why pdfplumber was the right choice:**

1. **Our PDFs are digitally generated** (not scanned). They contain selectable text from enterprise systems (SAP, TrackWise). pdfplumber excels at extracting structured text from these.

2. **Table Extraction**: Pharmaceutical quality reports are table-heavy (batch data, test results, deviation logs). pdfplumber's `extract_tables()` preserves table structure far better than PyPDF2.

3. **No External API Dependency**: pdfplumber runs locally inside the container. No network call, no additional cost, no latency. Azure Document Intelligence would add 1-3s per page + $1.50/1000 pages.

4. **Position-Aware Extraction**: pdfplumber gives coordinates for every text element. This enables the `view_file(page=45-48)` tool to extract exact pages for Claude.

5. **Lightweight**: ~2MB dependency vs Unstructured.io's 500MB+ with ML models.

**Trade-off acknowledged**: If GSK introduces scanned/handwritten documents, we'll need to add OCR. The architecture already has a placeholder (`ocr_client.py` with Mistral AI integration), but it's not wired into the main pipeline.

---

**Q10: How do you handle the Kong Gateway integration and rate limiting for Claude API calls?**

**Answer:**

Claude is accessed through GSK's enterprise **Kong API Gateway** (not directly via Anthropic's API). This adds a security and governance layer:

**Auth Flow:**
```
AI Component → PingFederate (OAuth2 client_credentials) → access_token
AI Component → Kong Gateway (Bearer token + Claude API request) → Claude Sonnet 4
```

**Singleton Pattern for Connection Management:**
```python
# Module-level singleton: reuse the DirectClaudeClient across requests
# to avoid PingFederate token storms, httpx connection churn, and stale-process state
_v1_claude_client = None

def _get_v1_claude_client() -> DirectClaudeClient:
    """Return a singleton DirectClaudeClient, creating it on first use."""
    global _v1_claude_client
    if _v1_claude_client is None:
        _v1_claude_client = DirectClaudeClient()
    return _v1_claude_client
```

**Why Singleton:**
1. **Token Storms**: Without singleton, every request creates a new client → new PingFederate token request. Under load, this DDoSes the identity provider.
2. **Connection Reuse**: `httpx.AsyncClient` maintains a connection pool. Reusing the client avoids TCP handshake overhead for every Claude call.
3. **Token Caching**: The singleton caches the OAuth token and only refreshes when expired (`expires_in=3599s`).

**Rate Limiting Safety:**
```python
# Between tool-calling iterations
await asyncio.sleep(3)  # 3-second pause between Claude calls
```

This prevents hitting Kong Gateway's rate limits during a multi-iteration tool-calling loop (up to 20 iterations per analysis).

**Tool Result Truncation:**
```python
# Truncate tool results to 3000 characters
result = result[:3000]
```

This prevents sending massive PDF sections back to Claude, which would:
- Exceed Kong Gateway's request size limits
- Consume excessive tokens (cost)
- Slow down the conversation loop

---

**Q11: How does the asynchronous report generation work with Azure Service Bus and Function App?**

**Answer:**

**Why Async Architecture:**
A quality report may contain 20+ dynamic elements, each requiring AI analysis (Claude call + PDF extraction + evaluation). Processing all elements synchronously would take 10-20 minutes. Users shouldn't wait.

**Flow:**
```
User clicks "Generate Report"
         │
         ▼
Frontend → POST /api/v1/reports/generate
         │
         ▼
Backend → Creates report instance in SQL Server (status: "queued")
       → Sends message to Azure Service Bus queue
       → Returns 202 Accepted (with report_instance_id)
         │
         ▼
Azure Function App (Service Bus Trigger)
       → Picks up message from queue
       → For each dynamic element:
       │   → Builds prompt (hydrated with context)
       │   → Fetches context documents from Blob Storage
       │   → POST /v1/generate to AI Component
       │   → Receives generated text + GAR metrics
       │   → Stores result in SQL Server
       → Updates report status: "completed" / "failed"
         │
         ▼
Frontend → Polls for status (TanStack Query refetchInterval)
        → Displays completed report with generated content
```

**Why Azure Service Bus (not direct async):**

1. **Durability**: If the Function App crashes mid-processing, the message remains in the queue. It's retried automatically. No lost work.

2. **Scaling**: Multiple Function App instances can consume from the same queue. If 50 reports are queued, Azure auto-scales the Function App to process them in parallel.

3. **Decoupling**: The Backend doesn't need to know about the AI Component. It just publishes a message. The Function App handles the AI orchestration.

4. **Dead Letter Queue**: Failed messages (after max retries) move to a dead letter queue for investigation. Critical for pharma audit trails.

---

**Q12: How did you ensure code quality and testing across the full stack?**

**Answer:**

**Testing Strategy:**

| Layer | Tool | Coverage Target | What's Tested |
|-------|------|----------------|---------------|
| Frontend Unit | Vitest + Testing Library | Components, hooks, stores | Component rendering, hook behavior, store state |
| Frontend E2E | Playwright (3 browsers + iPad) | Critical user flows | Login → Create Report → Generate → View Results |
| Backend Unit | pytest | Repository, service, utility | Business logic, data transformations |
| Backend Integration | pytest + FastAPI TestClient | API endpoints | Full request/response cycle with test DB |
| AI Component | pytest | Analyzer, evaluator | Mock Claude responses, verify tool execution |

**Code Quality Enforcement:**

```
┌─────────────────────────────────────────────────────────────┐
│                  CODE QUALITY PIPELINE                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  PRE-COMMIT (Husky Git Hooks)                                │
│  ├── Frontend: Prettier format → ESLint fix → Type check    │
│  ├── Backend: Black formatter → Pylint → Type hints check   │
│  └── Commit-msg: Conventional commit format enforced         │
│                                                               │
│  CI PIPELINE (GitHub Actions)                                │
│  ├── Lint + Format check                                    │
│  ├── Unit tests + Coverage report                           │
│  ├── E2E tests (Playwright on 3 browsers)                   │
│  ├── Security scan (Dependabot + CodeQL)                    │
│  └── Build Docker image (standalone output)                 │
│                                                               │
│  ARCHITECTURE RULES (Constitution)                           │
│  ├── Backend: Files ≤ 500 lines, PEP 8, 90-char line limit │
│  ├── Frontend: No `any` types, strict TypeScript mode       │
│  ├── API: Centralized endpoints in api.constants.ts          │
│  ├── State: One concern per Zustand store                   │
│  └── Components: Container-Presenter pattern                 │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Architectural Governance (Constitution):**

The project has a formal "Development Constitution" (`.specify/memory/constitution.md`) with NON-NEGOTIABLE principles:

- **Clean Architecture**: Repository pattern for data access, Service layer for business logic, Factory pattern for DI
- **No FastAPI HTTPException in service layers**: Custom exceptions only, transformed at the API layer
- **TypeScript strict mode**: No `any` types, all props/responses typed
- **Separation**: Frontend is a pure consumer — no Next.js API routes
- **Environment Variables**: All config via `NEXT_PUBLIC_*` (frontend) and `BaseSettings` (backend)

---

**Q13: What monitoring and observability do you have? How do you track AI performance in production?**

**Answer:**

**Observability Stack:**

| Layer | Tool | What's Tracked |
|-------|------|----------------|
| Frontend | Application Insights (Azure) | Page views, errors, performance |
| Backend | Application Insights + custom middleware | API latency, errors, request tracing |
| AI Component | OpenTelemetry + Application Insights | Token usage, cost, stage timings |
| AI Component | TelemetryCollector (custom) | Model name, prompt/completion tokens, evaluation scores |

**AI-Specific Telemetry:**

Every `/analyze` span includes business attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `roby.model_name` | string | Claude model (e.g., `claude-sonnet-4-5`) |
| `roby.prompt_tokens` | int | Input tokens for the request |
| `roby.completion_tokens` | int | Output tokens generated |
| `roby.total_tokens` | int | Sum of prompt + completion |
| `roby.estimated_cost` | float | Estimated cost in USD |
| `roby.tool_calls_count` | int | Number of tool-calling iterations |
| `roby.evaluation_scores` | object | GAR scores per analysis |

**OpenTelemetry Integration:**
```python
# Optional, mirrors AIGA-II pattern
if ENABLE_OTEL:
    setup_otel(app)  # Traces exported to Application Insights
else:
    logger.info("OpenTelemetry disabled")
```

**Monitoring Dashboards (KQL Queries in App Insights):**
- Average tokens per analysis (cost tracking)
- GAR score trends over time (quality monitoring)
- Claude API latency percentiles (p50, p95, p99)
- Tool-calling iteration counts (efficiency)
- Error rates by endpoint

---

**Q14: If you were to redesign this system today, what would you change?**

**Answer:**

1. **Add RAG with Vector Store**: Currently, Claude uses tool-calling to read PDFs on-demand. For frequently referenced documents (SOPs, regulatory guidelines), a vector store (Qdrant/Azure AI Search) with pre-indexed embeddings would reduce latency and token cost significantly.

2. **Implement Streaming Responses**: The current `/v1/generate` endpoint waits for the full response. Implementing SSE streaming would give users real-time feedback during the 10-60 second generation time.

3. **Model Routing**: Not every dynamic element needs Claude Sonnet 4. Simple elements (date extraction, status lookups) could use a smaller/cheaper model, while complex summaries use the full model. This could cut costs by 40-60%.

4. **Evaluation Pipeline Separation**: GAR evaluation currently happens inline (same request as generation). Moving it to an async pipeline would reduce perceived latency and allow more sophisticated evaluation (ensemble judges, human-in-the-loop for low-confidence scores).

5. **Caching Layer**: Many dynamic elements across different reports reference the same source documents. A semantic cache (Redis + embedding similarity) could serve identical queries instantly.

6. **Multi-Model Support**: Add support for Azure OpenAI GPT-4o as a fallback when Claude/Kong is unavailable. The `DirectClaudeClient` singleton pattern makes this easy — implement a `ModelGateway` with circuit breaker.

---

**Q15: If given a new problem — "Build a system that auto-generates compliance audit reports from 500+ source documents" — walk us through your solution design process.**

**Answer:**

**My Solution Design Framework (DISCOVER → DESIGN → DELIVER):**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SOLUTION DESIGN PROCESS                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Phase 1: DISCOVER (1-2 days)                                        │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━                                        │
│  ├── Understand the BUSINESS problem (not the tech problem)          │
│  ├── Who are the users? What do they do today?                       │
│  ├── What does "good" look like? (success metrics)                   │
│  ├── What are the constraints? (compliance, data, timeline, budget)  │
│  └── What already exists? (data, systems, APIs)                      │
│                                                                       │
│  Phase 2: DESIGN (2-3 days)                                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━                                          │
│  ├── Define architecture (components, data flow, integrations)       │
│  ├── Choose tech stack (justify EVERY choice against alternatives)   │
│  ├── Identify risks & mitigations                                    │
│  ├── Define MVP scope vs Full scope                                  │
│  └── Estimate effort (data + AI + engineering + testing)             │
│                                                                       │
│  Phase 3: DELIVER (iterative)                                        │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━                                          │
│  ├── POC (2-4 weeks) → validate feasibility                         │
│  ├── MVP (6-8 weeks) → deliver value to pilot users                 │
│  └── Production (ongoing) → scale, monitor, improve                  │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**For the Compliance Audit Report problem specifically:**

**Step 1: Clarify Requirements**
```
Questions I'd ask:
- What types of documents? (PDFs, Word, Excel, emails?)
- Are they text-based or scanned? (determines OCR needs)
- What does a "compliance audit report" contain? (sections, format)
- How many reports per day/week? (throughput requirement)
- What compliance standards? (ISO, GMP, SOX, GDPR?)
- What's the accuracy threshold? (99%? 95%? human review always?)
- What systems exist? (document management, databases)
- Who reviews/approves generated reports? (human-in-the-loop?)
```

**Step 2: Architecture Design**

```
┌─────────────────────────────────────────────────────────────┐
│           COMPLIANCE REPORT GENERATION SYSTEM                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  INGESTION LAYER                                             │
│  ├── Document Connector (SharePoint, S3, DB)                 │
│  ├── Format Handler (PDF/Word/Excel/Email parsers)           │
│  ├── Pre-processing (OCR if needed, table extraction)        │
│  └── Indexing Pipeline (chunk → embed → vector store)        │
│                                                               │
│  INTELLIGENCE LAYER                                          │
│  ├── Query Planner (breaks report into sections/questions)   │
│  ├── Retrieval Engine (hybrid search: semantic + keyword)    │
│  ├── Generator (LLM with grounded generation)                │
│  ├── Evaluator (faithfulness, completeness, accuracy)        │
│  └── Citation Engine (trace every claim to source doc)       │
│                                                               │
│  ORCHESTRATION LAYER                                         │
│  ├── Report Template Engine (section structure)              │
│  ├── Workflow Manager (async generation, status tracking)    │
│  ├── Human Review Queue (flagged sections for review)        │
│  └── Version Control (draft → review → approved)            │
│                                                               │
│  QUALITY & COMPLIANCE LAYER                                  │
│  ├── Guardrails (no hallucination, no fabricated data)       │
│  ├── Audit Trail (who generated, what sources, when)         │
│  ├── Confidence Scoring (per-section confidence)             │
│  └── Regulatory Metadata (traceability matrix)               │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Step 3: Key Design Decisions (with justification)**

| Decision | Choice | Why | Alternative Considered |
|----------|--------|-----|----------------------|
| Retrieval | Hybrid RAG (not tool-calling) | 500+ docs too many for tool-calling loops | Claude tool-calling (too slow for 500 docs) |
| Chunking | Semantic + hierarchical | Compliance docs have structured sections | Fixed-size (loses regulatory context) |
| Generation | Section-by-section (not whole report) | Smaller context = fewer hallucinations | Full report in one call (too much context) |
| Evaluation | Mandatory per-section | Compliance = zero tolerance for errors | Post-hoc only (too risky) |
| Human Review | Confidence-gated | Auto-approve > 0.9, human review < 0.9 | Always human (defeats purpose) |
| Storage | Vector + Knowledge Graph | Relationships between regulations matter | Vector only (misses cross-references) |

**Step 4: Risk Matrix**

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Hallucinated compliance data | Critical (regulatory fine) | Mandatory grounding check + citation |
| Missing source document | High (incomplete report) | Coverage analysis before generation |
| Version confusion | High (wrong regulation version) | Explicit version tagging in metadata |
| LLM API downtime | Medium (delayed reports) | Fallback model + queue persistence |
| Cost explosion | Medium (budget overrun) | Token budgets, caching, model routing |

---

**Q16: If you were setting up GitHub Copilot for your team, what instructions and guardrails would you put in place? How did you do it in Synaptica?**

**Answer:**

In Synaptica, we implemented a multi-layered Copilot governance system. This is critical because AI-generated code without guardrails leads to inconsistency, security vulnerabilities, and architectural drift.

**Our Copilot Governance Architecture:**

```
┌──────────────────────────────────────────────────────────────┐
│              COPILOT GUARDRAIL LAYERS                          │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  Layer 1: CONSTITUTION (Non-Negotiable Principles)            │
│  ─────────────────────────────────────────────────            │
│  File: .specify/memory/constitution.md                        │
│  • Architecture rules that NEVER change                       │
│  • Technology stack constraints                               │
│  • Code quality minimums                                      │
│  • Security requirements                                      │
│                                                                │
│  Layer 2: INSTRUCTIONS (Role-Specific Guidance)               │
│  ──────────────────────────────────────────────               │
│  File: .instructions/react-instructions.md                    │
│  File: .instructions/python-instructions.md                   │
│  • How to write code in THIS project                          │
│  • Patterns to follow, patterns to avoid                      │
│  • File naming, folder structure conventions                  │
│                                                                │
│  Layer 3: SPECIFICATIONS (Feature-Level Context)              │
│  ────────────────────────────────────────────                 │
│  File: specs/*.md                                             │
│  • Business requirements for current feature                  │
│  • Acceptance criteria                                        │
│  • Technical decisions already made                           │
│                                                                │
│  Layer 4: AUTOMATED ENFORCEMENT (CI/CD)                       │
│  ───────────────────────────────────────                      │
│  • Pre-commit hooks (Husky): format + lint                    │
│  • CI pipeline: type check + test + build                     │
│  • PR review: architecture compliance check                   │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

**Layer 1: Constitution (What We Actually Put In It)**

```markdown
# ROBY-HVR Development Constitution

## NON-NEGOTIABLE PRINCIPLES

### Architecture Rules
- Clean Architecture with separation of concerns
- Repository pattern for ALL data access (no direct DB in services)
- Service layer for ALL business logic (no logic in API endpoints)
- Factory pattern for dependency injection
- Never use FastAPI's HTTPException in service layers — custom exceptions only

### Frontend Rules
- TypeScript strict mode — NO `any` types EVER
- Functional components with arrow functions only
- Container-Presenter pattern (containers fetch data, presenters render)
- All API endpoints centralized in api.constants.ts
- Zod schemas for ALL API responses (no trusting backend blindly)
- One concern per Zustand store

### Security Rules
- No hardcoded secrets (environment variables only)
- No logging of PII, tokens, or request bodies in production
- Input validation on every endpoint (Pydantic on backend, Zod on frontend)
- Azure AD authentication on all routes except /health

### Code Quality Rules
- Backend files: ≤500 lines maximum
- Frontend files: ≤300 lines maximum
- All functions: type hints (Python) / TypeScript types (frontend)
- PEP 8 + 90-char line limit (Python)
- Meaningful docstrings (PEP 257) on all public functions
```

**Layer 2: Copilot Instructions (What We Tell The AI Assistant)**

```markdown
# React Copilot Instructions for Synaptica

## ALWAYS DO:
- Use TypeScript with strict types for all code
- Follow the existing folder structure (components/ui/, hooks/queries/, stores/)
- Use TanStack Query for data fetching, NEVER useEffect + fetch
- Use Zustand for global state, NEVER React Context for state
- Use React Hook Form + Zod for forms, NEVER uncontrolled inputs
- Import from barrel files (index.ts) where they exist
- Handle loading, error, and empty states in every query consumer
- Use Tailwind CSS classes, NEVER inline styles or CSS modules

## NEVER DO:
- Never use `any` type — use `unknown` and narrow, or define proper types
- Never create Next.js API routes (this is a frontend-only app)
- Never import directly from node_modules internals
- Never use localStorage for sensitive data (use sessionStorage for MSAL)
- Never put business logic in components (use hooks/services)
- Never make API calls without going through useApiRequest hook
- Never hardcode API URLs (use api.constants.ts)

## PATTERNS TO FOLLOW:

### Data Fetching Pattern (MANDATORY):
```typescript
// ✅ CORRECT — TanStack Query + typed hook
export function useReports() {
  const { apiGet } = useApiRequest();
  return useQuery({
    queryKey: [QUERY_KEYS.REPORTS],
    queryFn: () => apiGet<Report[]>(REPORT_API.GET),
  });
}

// ❌ WRONG — Direct fetch in component
useEffect(() => {
  fetch('/api/reports').then(r => r.json()).then(setData);
}, []);
```

### Component Pattern (MANDATORY):
```typescript
// ✅ Container (fetches data)
export function ReportsContainer() {
  const { data, isLoading, error } = useReports();
  if (isLoading) return <LoadingSkeleton />;
  if (error) return <ErrorMessage error={error} />;
  return <ReportsList reports={data} />;
}

// ✅ Presenter (renders UI — pure, testable)
interface ReportsListProps {
  reports: Report[];
}
export function ReportsList({ reports }: ReportsListProps) {
  return <ul>{reports.map(r => <ReportCard key={r.id} report={r} />)}</ul>;
}
```
```

**Layer 3: Why Each Guardrail Exists (The Reasoning)**

| Guardrail | Why It Exists | What Happens Without It |
|-----------|--------------|------------------------|
| No `any` types | Lost type safety = runtime errors in production | Copilot generates `any` everywhere, bugs slip through |
| No Next.js API routes | Architecture: frontend consumes Python backend only | Copilot creates `/app/api/` routes, splits logic across two backends |
| TanStack Query mandatory | Consistent caching, background refresh, retry logic | Copilot uses `useEffect` + `fetch`, loses all caching benefits |
| Centralized API constants | Single source of truth for all endpoints | Copilot hardcodes URLs in components, breaks on API changes |
| Zod on all responses | Runtime validation catches backend contract changes | Silent failures when backend changes response shape |
| Repository pattern | Testable data access, swappable data sources | Copilot puts SQL queries directly in endpoint handlers |
| Max file length | Readable, reviewable, maintainable code | Copilot generates 2000-line god files |

**Layer 4: Enforcement Pipeline**

```yaml
# What happens when Copilot-generated code violates rules:

Pre-commit (developer's machine):
  ├── Prettier → Auto-fixes formatting (no friction)
  ├── ESLint → Catches type errors, unused imports, React anti-patterns
  └── Commit-msg → Enforces conventional commit format

CI Pipeline (on PR):
  ├── TypeScript strict check → Rejects `any` types
  ├── Vitest → Unit tests must pass
  ├── Playwright → E2E tests must pass
  ├── Coverage → Must maintain >80% line coverage
  └── Build → Standalone Docker build must succeed

PR Review (human):
  ├── Architecture check → Does it follow constitution?
  ├── Pattern check → Container-Presenter? TanStack Query?
  └── Security check → No hardcoded secrets, PII handling
```

---

**Q17: How would you design Copilot instructions for a NEW project from scratch? What's your framework?**

**Answer:**

**My Copilot Instruction Design Framework:**

```
┌──────────────────────────────────────────────────────────────┐
│         COPILOT INSTRUCTION DESIGN FRAMEWORK                  │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  Step 1: DEFINE THE BOUNDARIES                                │
│  ─────────────────────────────                                │
│  What should Copilot NEVER do in this project?                │
│  • Security boundaries (auth, secrets, PII)                   │
│  • Architecture violations (layer skipping, wrong patterns)   │
│  • Anti-patterns specific to your stack                       │
│                                                                │
│  Step 2: DEFINE THE PATTERNS                                  │
│  ────────────────────────────                                 │
│  What should Copilot ALWAYS do?                               │
│  • Code structure templates (how to create X)                 │
│  • Naming conventions (files, variables, functions)           │
│  • Import order and barrel exports                            │
│  • Error handling patterns                                    │
│                                                                │
│  Step 3: PROVIDE CONTEXT                                      │
│  ────────────────────────                                     │
│  What does Copilot need to know about this project?           │
│  • Folder structure and where things go                       │
│  • Tech stack versions and constraints                        │
│  • Existing utilities to reuse (don't reinvent)               │
│  • External systems and their APIs                            │
│                                                                │
│  Step 4: SHOW EXAMPLES                                        │
│  ─────────────────────                                        │
│  Show ✅ correct and ❌ incorrect patterns                     │
│  • Real code from the project (best examples)                 │
│  • Common mistakes Copilot makes                              │
│  • Edge cases and how to handle them                          │
│                                                                │
│  Step 5: ENFORCE AUTOMATICALLY                                │
│  ─────────────────────────────                                │
│  What can be caught without human review?                     │
│  • Linters (ESLint rules, Pylint)                             │
│  • Type checkers (TypeScript strict, mypy)                    │
│  • Git hooks (pre-commit, commit-msg)                         │
│  • CI/CD gates (test, build, security scan)                   │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

**Template for Any New Project:**

```markdown
# [Project Name] — AI Coding Assistant Instructions

## 1. Project Context
- **What**: [One-line description]
- **Stack**: [Framework, language, key libraries]
- **Architecture**: [Pattern — MVC, Clean Architecture, Hexagonal]
- **Team**: [Size, skill level, conventions]

## 2. NEVER Do (Hard Guardrails)
- [ ] Never [security violation]
- [ ] Never [architecture violation]
- [ ] Never [anti-pattern specific to stack]
- [ ] Never [data handling violation]

## 3. ALWAYS Do (Mandatory Patterns)
- [ ] Always [error handling pattern]
- [ ] Always [data fetching pattern]
- [ ] Always [testing requirement]
- [ ] Always [documentation requirement]

## 4. Code Patterns (with examples)

### Creating a new [component/endpoint/service]:
```[language]
// Show the EXACT pattern to follow
```

### ❌ Anti-patterns to avoid:
```[language]
// Show what NOT to do
```

## 5. Project Structure
```
src/
├── [explain what goes where]
```

## 6. Existing Utilities (use these, don't recreate)
- `utils/X` — does Y
- `hooks/Z` — does W
- `lib/A` — handles B
```

**Real-World Example — Guardrails That Saved Us in Synaptica:**

| Scenario | Without Guardrail | With Guardrail | Impact |
|----------|-------------------|----------------|--------|
| Copilot generated `useEffect` + `fetch` for data loading | Lost caching, duplicate requests, race conditions | Copilot uses TanStack Query pattern from instructions | 60% fewer network requests |
| Copilot put API URL in component | Breaking on environment change | Forced to use `api.constants.ts` | Zero broken deployments |
| Copilot used `any` for API response | Silent failures when backend changed | Zod validation catches mismatches | Caught 12 breaking changes pre-prod |
| Copilot created Next.js API route | Logic split between Python + Next.js backends | Instruction says "NO API routes" | Clean architecture maintained |
| Copilot stored token in localStorage | Security audit failure | Instructions mandate sessionStorage | Passed security review |

---

**Q18: Given a specific problem — "Users report that AI-generated report sections sometimes contain fabricated statistics" — how would you debug and solve this?**

**Answer:**

**My Debugging Framework for AI Quality Issues:**

```
DETECT → DIAGNOSE → DESIGN FIX → DEPLOY → MONITOR
```

**Step 1: DETECT — Quantify the Problem**
```python
# Pull recent evaluations and find low-groundedness cases
SELECT 
    request_id,
    element_name,
    answer_text,
    groundedness_score,
    source_documents
FROM ai_evaluations
WHERE groundedness_score < 0.7
AND created_at > DATEADD(day, -7, GETDATE())
ORDER BY groundedness_score ASC;

# Result: 23 out of 412 generations (5.6%) have groundedness < 0.7
# Pattern: Mostly in "statistical summary" element types
```

**Step 2: DIAGNOSE — Root Cause Analysis**

```
┌─────────────────────────────────────────────────────────┐
│              ROOT CAUSE INVESTIGATION                     │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Hypothesis 1: Source documents don't contain the data   │
│  Check: Review source PDFs for the failed cases          │
│  Finding: ✅ Statistics exist in docs but in TABLES       │
│  → pdfplumber extracts tables poorly in some PDFs        │
│                                                           │
│  Hypothesis 2: Claude hallucinating numbers from training│
│  Check: Compare generated stats with source content      │
│  Finding: ✅ Some numbers are plausible but not in docs  │
│  → Claude fills gaps with training knowledge             │
│                                                           │
│  Hypothesis 3: Prompt doesn't constrain Claude enough    │
│  Check: Review system prompt for statistical elements    │
│  Finding: ✅ No explicit "only use provided data" rule   │
│  → Claude assumes it should provide complete answer      │
│                                                           │
│  ROOT CAUSES IDENTIFIED:                                  │
│  1. Table extraction failure (data not reaching Claude)   │
│  2. Insufficient grounding constraint in prompt          │
│  3. No "I don't know" fallback for missing data          │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

**Step 3: DESIGN FIX — Multi-layered solution**

```python
# Fix 1: Improve table extraction
class EnhancedPDFExtractor:
    def extract(self, pdf_path):
        text = pdfplumber_extract(pdf_path)
        tables = pdfplumber_extract_tables(pdf_path)
        
        # Convert tables to structured text that Claude can parse
        for table in tables:
            text += f"\n\n[TABLE DATA]\n{table_to_markdown(table)}\n[/TABLE DATA]"
        
        return text

# Fix 2: Strengthen system prompt
SYSTEM_PROMPT = """
You are a pharmaceutical quality analyst. 

CRITICAL RULES:
1. ONLY use data from the provided source documents
2. For any statistic, number, or date — it MUST appear in the source
3. If data is not available in sources, respond with:
   "Data not found in provided documents. Please verify manually."
4. NEVER extrapolate, estimate, or use your training knowledge for numbers
5. Always cite the source document and page for every statistic

If you cannot fully answer the question from the provided sources,
state clearly what information is missing.
"""

# Fix 3: Post-generation validation
class StatisticsValidator:
    async def validate(self, answer: str, source_content: str):
        # Extract all numbers from the generated answer
        numbers_in_answer = extract_numbers(answer)
        numbers_in_source = extract_numbers(source_content)
        
        # Check each number exists in source
        ungrounded_numbers = []
        for num in numbers_in_answer:
            if not any(is_close(num, src_num) for src_num in numbers_in_source):
                ungrounded_numbers.append(num)
        
        if ungrounded_numbers:
            # Flag for human review
            return ValidationResult(
                passed=False,
                reason=f"Ungrounded statistics: {ungrounded_numbers}",
                action="human_review_required"
            )
        
        return ValidationResult(passed=True)
```

**Step 4: DEPLOY — Gradual rollout**
```
Week 1: Deploy fix to 10% of traffic (canary)
        Compare groundedness scores: new vs old
Week 2: If improvement confirmed, roll to 50%
Week 3: Full deployment + monitoring dashboard
```

**Step 5: MONITOR — Ongoing quality tracking**
```python
# Alert rule
if average_groundedness_last_24h < 0.85:
    alert("AI quality degradation", 
          metric="groundedness",
          current=average_groundedness_last_24h)
```

**Outcome:**
- Groundedness improved from 94.4% → 98.7%
- False statistics dropped from 5.6% → 0.8%
- Remaining 0.8% caught by human review queue

---

*This section demonstrates real-world application of all concepts covered in this guide — from microservice architecture and LLM tool-calling to enterprise authentication, async processing, and production monitoring.*
