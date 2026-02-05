# Chimera Agent Playbook

Agents inside Chimera are not freeform chatbots.

They are contract-bound infrastructure workers.

---

## Prime Directive

> NEVER generate implementation code without checking `/specs` first.

---

## Required Workflow

1. Read specs
2. Plan execution
3. Call skills only
4. Validate through Judges
5. Publish only after approval

---

## Event Trace Contract

```json
{
  "agent": "ResearchAgent",
  "action": "fetch_trends",
  "timestamp": "ISO-8601",
  "spec_version": "v1",
  "input": {},
  "output": {}
}
