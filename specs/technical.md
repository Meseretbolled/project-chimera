# Technical Specification — Project Chimera

## Purpose
This document defines the technical contracts and execution rules
for Chimera’s governed multi-agent system.

Chimera agents do not act freely.
They operate only through bounded skills with validated outputs.

---

## Skill Interface Standard

All Chimera skills must implement:

```python
def run(input: dict) -> dict:
    """
    Execute a bounded Chimera skill.

    Input: validated dict payload
    Output: structured dict result
    """
    ...
This ensures skills are:

swappable

testable

agent-compatible

Contract: Trend Fetch Skill
Input
json
Copy code
{
  "platform": "tiktok",
  "limit": 10
}
Output
json
Copy code
{
  "trends": [
    {
      "topic": "AI Influencers",
      "score": 0.92,
      "source": "tiktok"
    }
  ]
}
Rules
platform must be a supported string

limit must be an integer > 0

output must always contain trends

Contract: Content Generator Skill
Input
json
Copy code
{
  "trend_topic": "AI Influencers",
  "platform": "instagram",
  "tone": "educational"
}
Output
json
Copy code
{
  "draft_caption": "AI influencers are rewriting digital culture...",
  "hashtags": ["#AI", "#Influencer"]
}
Rules
caption must not be empty

hashtags must be a list of strings

output is always a draft until approved

Contract: Safety Validator Skill
Input
json
Copy code
{
  "content": "AI influencers are rewriting digital culture...",
  "platform": "instagram"
}
Output
json
Copy code
{
  "status": "approved",
  "reason": "No policy violations detected"
}
Allowed Status Values
approved

rejected

needs_human_review

Contract: Publisher Skill
Publishing is only allowed after validation + approval.

Input
json
Copy code
{
  "platform": "instagram",
  "approved_caption": "AI influencers are rewriting digital culture...",
  "hashtags": ["#AI", "#Influencer"]
}
Output
json
Copy code
{
  "publish_status": "scheduled",
  "post_id": "abc123"
}
Governance Rule
Publisher MUST reject execution unless:

SafetyValidator status == approved

Human approval gate is satisfied

Data Storage Plan (Planned)
Chimera maintains structured state in SQL.

Example Tables
trends
topic

score

platform

timestamp

content_items
trend_id

draft_text

status (draft/approved/published)

Observability (MCP Trace)
Every agent action must emit a trace event:

json
Copy code
{
  "agent": "ResearchAgent",
  "action": "fetch_trends",
  "timestamp": "ISO-8601",
  "spec_version": "v1",
  "input": {},
  "output": {}
}
MCP Sense provides auditability and governance enforcement.

Execution Rule
Chimera follows a deterministic pipeline:

Generate → Validate → Approve → Publish

No agent may publish directly without governance gates.