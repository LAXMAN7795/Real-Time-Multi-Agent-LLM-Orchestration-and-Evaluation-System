# Real-Time Multi-Agent LLM Orchestration and Evaluation System

## Overview

A production-oriented multi-agent orchestration platform built using FastAPI, LangGraph, Retrieval-Augmented Generation (RAG), evaluation pipelines, governance workflows, and real-time streaming observability.

The system coordinates multiple specialized AI agents responsible for retrieval, security analysis, critique, synthesis, evaluation, and self-improvement. It integrates external retrieval tools, streaming APIs, governance-aware prompt review workflows, Docker-based deployment infrastructure, and evaluation harnesses for robust orchestration.

This project demonstrates advanced AI systems engineering concepts including:

- Multi-agent orchestration
- Retrieval-Augmented Generation (RAG)
- Security-aware prompt handling
- Adversarial prompt blocking
- Evaluation and scoring pipelines
- Self-improving orchestration loops
- Governance approval/rejection workflows
- Real-time SSE observability
- Dockerized infrastructure deployment
- Execution tracing and orchestration analytics

---

# Repository Structure

```bash
.
├── app/
│   ├── api/
│   ├── orchestration/
│   ├── tools/
│   ├── evals/
│   ├── governance/
│   ├── rag/
│   ├── prompts/
│   └── main.py
│
├── assets/
│   ├── architecture/
│   ├── diagrams/
│   └── screenshots/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# System Architecture

## Overall Architecture Diagram

![System Architecture](assets/architecture/system_architecture_diagram.png)

---

# Orchestration Workflow

![Orchestration Workflow](assets/diagrams/orchestration_workflow_diagram.png)

---

# Evaluation and Governance Pipeline

## Evaluation and Self-Improvement Pipeline

![Evaluation Pipeline](assets/diagrams/evaluation_self_improvement_pipeline.png)

## Governance Workflow Diagram

![Governance Workflow](assets/diagrams/governance_workflow_diagram.png)

---

# Agent Architecture

The orchestration platform is composed of multiple specialized agents.

---

## 1. Retrieval Agent

### Responsibilities

- Retrieves relevant context using:
  - Tavily Search
  - Vector Store (RAG)
- Applies adaptive retrieval strategies
- Performs context-budget management
- Maintains retrieval provenance

### Decision Boundaries

The retrieval agent:

- CAN retrieve external context
- CAN retrieve vector embeddings
- CAN apply chunk filtering and budgeting
- CANNOT generate final answers
- CANNOT bypass governance policies
- CANNOT override security decisions

### Failure Conditions

- Poor retrieval quality
- Weak semantic matches
- External API failures
- Sparse knowledge-base coverage

---

## 2. Security Agent

### Responsibilities

- Detects adversarial prompts
- Detects prompt injection attempts
- Applies governance policies
- Blocks unsafe orchestration flows
- Prevents sensitive data leakage

### Decision Boundaries

The security agent:

- CAN block orchestration
- CAN classify malicious prompts
- CAN enforce security policies
- CANNOT generate user responses
- CANNOT rewrite prompts directly

### Examples of Blocked Behavior

- System prompt extraction
- Jailbreak attempts
- Role escalation attacks
- Instruction override attacks

---

## 3. Critique Agent

### Responsibilities

- Evaluates retrieved evidence quality
- Detects weak reasoning
- Identifies hallucination risk
- Flags unsupported claims

### Decision Boundaries

The critique agent:

- CAN analyze quality and gaps
- CAN detect hallucination patterns
- CANNOT retrieve external data
- CANNOT finalize orchestration outputs

---

## 4. Synthesis Agent

### Responsibilities

- Generates grounded final responses
- Maintains provenance tracking
- Produces citation-aware outputs
- Combines retrieved evidence into coherent responses

### Decision Boundaries

The synthesis agent:

- CAN generate final answers
- CAN include citations and provenance
- CANNOT bypass security restrictions
- CANNOT invent unsupported evidence intentionally

---

## 5. Evaluation Agent

### Responsibilities

- Scores orchestration quality
- Measures groundedness
- Measures relevance
- Measures citation accuracy
- Measures hallucination risk
- Generates evaluation metrics

### Decision Boundaries

The evaluation agent:

- CAN score orchestration outputs
- CAN recommend improvements
- CANNOT directly modify prompts
- CANNOT override governance decisions

---

## 6. Improvement Agent

### Responsibilities

- Generates rewrite proposals
- Produces improvement suggestions
- Recommends orchestration changes
- Supports self-improving workflows

### Decision Boundaries

The improvement agent:

- CAN suggest improvements
- CAN generate rewrite proposals
- CANNOT auto-deploy changes
- CANNOT bypass governance approval workflows

---

# API Endpoints

| Endpoint | Description |
|---|---|
| `/run-orchestrator` | Execute orchestration pipeline |
| `/stream-query` | Real-time SSE orchestration streaming |
| `/trace/{job_id}` | Retrieve execution traces |
| `/run-evals` | Execute evaluation harness |
| `/eval-summary` | Evaluation analytics summary |
| `/prompt-review` | Governance approval/rejection workflow |
| `/rerun-failed-evals` | Re-run failed evaluation cases |
| `/health` | Health check endpoint |

---

# Real-Time SSE Streaming

## SSE Streaming Observability

![SSE Streaming](assets/screenshots/real_time_sse_orchestration_stream.png)

The orchestration platform streams live execution events including:

- Retrieval events
- Security analysis
- Evaluation scoring
- Improvement workflows
- Final response generation
- Execution completion lifecycle

---

# Retrieval and Provenance

## Retrieval + Execution Trace

![Retrieval Trace](assets/screenshots/retrieval_security_execution_trace.png)

## Agent Synthesis and Retrieval

![Agent Synthesis](assets/screenshots/agent_synthesis_and_retrieval.png)

## Grounded Synthesis + Provenance

![Grounded Provenance](assets/screenshots/evaluation_metrics_and_provenance.png)

The orchestration system maintains:

- Source attribution
- Provenance tracking
- Retrieval evidence transparency
- Citation-aware synthesis

---

# Adversarial Robustness and Security

## Prompt Injection Detection

![Prompt Injection](assets/screenshots/prompt_injection_detection_retrieval.png)

## Security Blocking Workflow

![Security Blocking](assets/screenshots/security_policy_blocking_trace.png)

The security layer prevents:

- Prompt injection
- System prompt extraction
- Instruction override attacks
- Jailbreak attempts
- Sensitive information leakage

---

# Evaluation and Analytics

## Evaluation Summary Dashboard

![Evaluation Dashboard](assets/screenshots/evaluation_summary_analytics_dashboard.png)

The orchestration platform tracks:

- Pass/fail metrics
- Hallucination failures
- Security-policy blocks
- Groundedness scores
- Relevance scores
- Citation accuracy

---

# Prompt Governance Workflow

## Approval Workflow

![Approval Workflow](assets/screenshots/prompt_rewrite_approval_workflow.png)

## Rejection Workflow

![Rejection Workflow](assets/screenshots/prompt_rewrite_rejection_workflow.png)

The governance layer enables:

- Human-in-the-loop review
- Prompt rewrite approval
- Prompt rewrite rejection
- Auditability
- Safe orchestration evolution

---

# Dockerized Infrastructure

## Docker Compose Deployment

![Docker Deployment](assets/screenshots/docker_compose_service_orchestration.png)

## Containerized API System

![Containerized API](assets/screenshots/containerized_fastapi_orchestrator_api.png)

## Swagger API Overview

![Swagger API](assets/screenshots/swagger_api_overview.png)

The platform is fully containerized using:

- FastAPI
- PostgreSQL
- Redis
- Docker Compose

---

# Visual Demonstration Gallery

## Self-Improvement and Governance

![Self Improvement](assets/screenshots/self_improvement_and_governance.png)

The orchestration platform supports evaluation-driven prompt rewrites, governance-aware approval workflows, and controlled self-improving orchestration mechanisms.

---

# Full Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/LAXMAN7795/Real-Time-Multi-Agent-LLM-Orchestration-and-Evaluation-System.git

cd Real-Time-Multi-Agent-LLM-Orchestration-and-Evaluation-System
```

---

## 2. Create Virtual Environment

```bash
python -m venv orchestrator
```

### Windows

```bash
orchestrator\Scripts\activate
```

### Linux / macOS

```bash
source orchestrator/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env` file:

```env
TAVILY_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
DATABASE_URL=your_database_url
REDIS_URL=your_redis_url
```

---

## 5. Run Locally

```bash
uvicorn app.main:app --reload
```

API Docs:

```bash
http://localhost:8000/docs
```

---

# Docker Deployment

## Build and Run

```bash
docker compose up --build
```

## Check Running Containers

```bash
docker compose ps
```

---

# Evaluation Harness

The evaluation framework supports:

- Baseline evaluation
- Ambiguous query testing
- Adversarial robustness testing
- Security policy testing
- Hallucination analysis
- Groundedness evaluation

Example test categories:

- Baseline queries
- Ambiguous prompts
- Adversarial prompts
- Empty input robustness
- Governance workflows

---

# Known Limitations

This project intentionally documents realistic limitations.

## 1. External Retrieval Dependency

The orchestration quality depends heavily on external retrieval quality.

Potential issues:

- Retrieval drift
- Incomplete web results
- API outages
- Weak semantic matches

---

## 2. Hallucination Is Reduced, Not Eliminated

Although grounded synthesis and critique agents reduce hallucinations, they cannot guarantee complete factual correctness.

Potential failure cases:

- Weak retrieval evidence
- Contradictory external sources
- Ambiguous user intent
- Sparse domain coverage

---

## 3. Self-Improvement Is Governance-Constrained

The improvement loop:

### CAN:

- Suggest rewrites
- Recommend improvements
- Generate governance proposals

### CANNOT:

- Automatically deploy policy changes
- Modify prompts without approval
- Override human governance review

This limitation is intentional for safety.

---

## 4. Security Layer Is Rule-Guided

The security layer can detect many adversarial patterns but is not guaranteed to detect all novel jailbreak strategies.

Potential bypass areas:

- Highly obfuscated prompts
- Multi-turn jailbreak chains
- Adversarial prompt encoding

---

## 5. Context Window Constraints

Long-context orchestration remains constrained by token limits.

The platform mitigates this using:

- Chunk filtering
- Token budgeting
- Context compression
- Adaptive retrieval

---

# What the Self-Improving Loop Does

The self-improvement pipeline:

- Evaluates orchestration quality
- Detects weaknesses
- Proposes rewrite suggestions
- Generates governance review proposals
- Supports continuous improvement workflows

---

# What the Self-Improving Loop Does NOT Do

The self-improvement loop does NOT:

- Autonomously rewrite production prompts
- Auto-deploy governance policies
- Override human reviewers
- Mutate orchestration logic without approval
- Self-modify infrastructure

This is intentionally governance-constrained.

---

# What I Would Build Next

Future roadmap areas include:

## Planned Improvements

- Multi-modal orchestration
- Long-term memory systems
- Agent-to-agent negotiation
- Advanced retry strategies
- Tool confidence scoring
- Dynamic orchestration planning
- Multi-tenant deployment
- Kubernetes deployment support
- Observability dashboards
- OpenTelemetry integration
- Distributed orchestration execution
- Fine-grained policy engines
- Human feedback reinforcement loops
- Advanced adversarial simulation harnesses

---

# Tech Stack

| Layer | Technologies |
|---|---|
| Backend | FastAPI, Python |
| Orchestration | LangGraph |
| LLM Integration | OpenAI APIs |
| Retrieval | Tavily Search, RAG |
| Database | PostgreSQL |
| Caching | Redis |
| Streaming | SSE |
| Deployment | Docker, Docker Compose |
| Evaluation | Custom Evaluation Harness |
| Governance | Prompt Approval Workflow |

---

# Conclusion

This project demonstrates a production-oriented approach to building reliable multi-agent AI orchestration systems with governance-aware workflows, evaluation pipelines, observability tooling, security analysis, and continuous improvement mechanisms.

The focus of the system is not merely response generation, but robust orchestration engineering with:

- transparency
- safety
- observability
- governance
- evaluation
- deployment readiness
- continuous improvement

---

# Author

**Laxman Sannu Gouda**

GitHub Repository:

https://github.com/LAXMAN7795/Real-Time-Multi-Agent-LLM-Orchestration-and-Evaluation-System
