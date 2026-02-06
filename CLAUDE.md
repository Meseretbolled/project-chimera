# 🧠 Project Chimera — Agent Rules & Spec Governance

This repository is **Project Chimera**:  
a **Spec-Driven Autonomous AI Influencer System**.

Chimera is designed to detect trends, generate content, validate safety,
and publish only through governance approval gates.

This is not a prototype.
This is an engineering-grade, governed agent architecture.

---

## 🎯 Project Context

Chimera simulates an **Agent Social Network Influencer Pipeline**:

- Trend Detection Agent
- Caption + Hashtag Generation Agent
- Safety Validator Agent
- Governed Publisher Agent
- Orchestrator with lifecycle state machine
- MCP-style trace logging for observability

The goal is reliability, traceability, and scalable autonomous execution.

---

## 🚨 PRIME DIRECTIVE (Spec-First Development)

**NEVER generate or modify implementation code without checking `/specs` first.**

Specs are the single source of truth.

Before writing code, always:

1. Open the relevant spec file
2. Confirm the contract requirements
3. Match input/output formats exactly

If specs are missing or unclear → request clarification, do NOT guess.

---

## 📌 Execution Rules for Agents

When asked to implement a feature:

1. Summarize the requirement
2. Identify the spec section that governs it
3. Explain your plan step-by-step
4. Only then write minimal, contract-aligned code

No hallucinated modules.
No invented APIs.
No undocumented behavior.

---

## 🛡 Governance & Safety Requirements

Chimera enforces responsible autonomy:

- Content must pass safety validation
- Publishing must be blocked unless approved
- Approval gates are mandatory
- All actions must remain auditable

Publishing without approval is considered a critical failure.

---

## 🔧 Skills vs Tools Separation

Chimera distinguishes:

### Skills (Runtime Capabilities)
Reusable agent modules under `/skills/`

Each skill must:

- Define `run(input: dict) -> dict`
- Follow its `contract.json`
- Return structured outputs only

### Developer Tools (MCP)
External development bridges (filesystem, git, telemetry)
Documented in `docs/research/tooling_strategy.md`

---

## 🧪 Testing Discipline (TDD)

Tests define the contract boundaries.

- Existing skills must pass tests
- Future capabilities may have placeholder failing tests
  (ex: OpenClaw broadcast integration slot)

Do not remove failing tests that represent roadmap intent.

---

## 📡 Traceability (MCP Black Box)

Every major agent action should emit trace events:

- Agent name
- Action performed
- Input payload
- Output payload
- Timestamp

This repository is built for agent observability and governance.

---

## ✅ Agent Success Criteria

A correct contribution must:

- Align with specs/
- Respect governance approval flow
- Preserve skill modularity
- Maintain structured contracts
- Keep the system reproducible via Docker + CI

---

## Final Reminder

**Specs define intent.  
Tests define truth.  
Governance defines safety.  
Traceability defines trust.**

Operate accordingly.
