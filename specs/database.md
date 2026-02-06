# Chimera Database Plan

Chimera will store high-velocity influencer metadata.

## Entities

### TrendEvent
| Field | Type |
|------|------|
| id | UUID |
| topic | string |
| platform | string |
| score | float |
| timestamp | datetime |

### ContentDraft
| Field | Type |
|------|------|
| id | UUID |
| trend_id | FK → TrendEvent |
| caption | text |
| hashtags | JSON |
| status | enum |

## Storage Decision

- SQLite for local dev
- PostgreSQL for production swarm scale

## Reason

Relational DB ensures:
- Traceability
- Governance audit logs
- Structured retrieval
