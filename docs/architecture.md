# Chimera Architecture

## 1. Purpose
Defines the high-level system shape, agent roles, boundaries, and data flows for Project Chimera.

## 2. Design Principles
- Spec-driven development
- Bounded agent authority
- Governance before optimization
- Observable by default

## 3. System Overview
you can find here ![Agent Architecture](agent_architecture.png)

# Architecture Overview

This diagram represents a hierarchical multi-agent architecture governed by a human Super-Orchestrator. The system emphasizes task decomposition, parallel execution, validation, and controlled state commitment, with optional human intervention.

## Flow

Human Super-Orchestrator  
→ Manager Agents  
→ Planner (Task Decomposition)  
→ Worker Swarms (Parallel Execution)  
→ Judges (Validation)  
→ Approve  
→ Commit to State (e.g., Publish Content)

## Key Components

- **Super-Orchestrator (Human):** Provides top-level oversight.
- **Manager Agents:** Coordinate domain workflows.
- **Planner:** Decomposes goals into tasks.
- **Worker Swarms:** Execute tasks concurrently.
- **Reusable Skills (via MCP):** e.g., trend fetch, posting, retrieval.
- **Judges:** Validate outputs against quality and policy.
- **Human Review (Optional):** Reject or escalate when needed.

## Properties

- Parallel and scalable execution  
- Bounded agent authority  
- Human-in-the-loop at safety boundaries  
- Deterministic state commitment  


All actions produce traces -> MCP Sense

## 4. Agent Roles

### Coordinator
- Delegates tasks
- Resolves conflicts
- Enforces contracts

### Research Agent
- Detects trends
- Validates sources

### Content Agent
- Generates scripts / captions

### Safety Agent
- Policy compliance
- Brand alignment

### Publishing Agent
- Platform-specific formatting
- Scheduling

## 5. Data Stores

- SQL: Specs, decisions, policies, agent states
- Object Storage: Media files
- Vector Store: Embeddings

## 6. Execution Flow

1. Research detects opportunity
2. Coordinator assigns content task
3. Content generates
4. Safety validates
5. Publishing posts
6. Metrics ingested

## 7. Observability

Every step emits:
- Input
- Output
- Agent ID
- Timestamp
- Spec version

## 8. Failure Handling

- Retry
- Fallback agent
- Human escalation

## 9. Security

- No agent has direct credentials
- Publishing via MCP server
