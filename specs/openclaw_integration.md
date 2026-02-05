# OpenClaw + MCP Integration Specification — Project Chimera

## Purpose

Project Chimera is designed as a governed autonomous influencer system.
Agents do not execute actions directly.

Instead, Chimera integrates with **OpenClaw + MCP servers** to provide:

- Safe tool execution
- Bounded authority
- Full observability
- Human approval gates

This document defines how Chimera connects to MCP infrastructure.

---

## What is MCP?

MCP (Model Context Protocol) is the execution layer that allows agents to:

- Call external tools safely
- Access structured skills
- Emit trace logs for governance

Chimera uses MCP as the **only allowed interface** to the outside world.

Agents cannot:

- Use raw API keys
- Post directly
- Access credentials
- Modify state without validation

---

## OpenClaw Role in Chimera

OpenClaw provides the agent runtime structure:

- Planner → Worker → Validator → Publisher
- Tool routing via MCP
- Skill modularity

OpenClaw is treated as the execution engine,
while Chimera governance defines the safety rules.

---

## Integration Architecture

Execution path:

Agent Request
↓
Skill Contract Check
↓
MCP Tool Invocation (OpenClaw)
↓
Trace Emission (MCP Sense)
↓
Validator + Judge Approval
↓
Commit to State (Publish)

No agent may bypass MCP.

---

## MCP Server Configuration

Example `mcp.json` entry:

```json
{
  "servers": {
    "tenxfeedbackanalytics": {
      "url": "https://mcppulse.10academy.org/proxy",
      "type": "http"
    }
  }
}
This enables Chimera agents to call:

Trend fetch tools

Feedback analytics

Observability traces

Skill Execution Rules

Every skill must:

Match its contract.json

Return structured output

Emit trace events

Example trace payload:
{
  "agent": "ResearchAgent",
  "action": "fetch_trends",
  "timestamp": "ISO-8601",
  "spec_version": "v1",
  "input": {
    "platform": "tiktok",
    "limit": 5
  },
  "output": {
    "trends": []
  }
}
Governance Enforcement

Publishing tools MUST reject execution unless:

SafetyValidator status == approved

Human gate is satisfied

Output contract is valid

Human-in-the-Loop Boundary

Human escalation is mandatory when:

Confidence is low

Platform policy is unclear

Sensitive content is detected

OpenClaw provides optional pause + review hooks.