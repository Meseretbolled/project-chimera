# Security & Safety Model

## Secrets Management
All API keys must be stored in env vars or GitHub Secrets.

## AuthN/AuthZ (Planned)
Publishing endpoints require OAuth2 authentication.

## Rate Limiting
Trend ingestion limited to prevent abuse.

## Moderation Pipeline
Safety Validator returns:
- approved
- flagged (human review)
- blocked (reject content)

## Escalation Threshold
Flagged content cannot publish automatically.
