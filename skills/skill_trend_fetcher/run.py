"""
Trend Fetcher Skill

Governed skill that returns trending topics.
Includes MCP trace emission for observability.
"""

from datetime import datetime
from chimera.trace import emit_trace


def run(input: dict) -> dict:
    """
    Input:
        {
          "platform": "tiktok",
          "limit": 3
        }

    Output:
        {
          "trends": [
            {"topic": "...", "score": ..., "source": "..."}
          ]
        }
    """

    platform = input.get("platform", "tiktok")
    limit = input.get("limit", 5)

    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("limit must be an integer > 0")

    trends = [
        {
            "topic": "AI Influencers",
            "score": 0.92,
            "source": platform,
            "timestamp": datetime.utcnow().isoformat(),
        },
        {
            "topic": "Smart Productivity Tools",
            "score": 0.88,
            "source": platform,
            "timestamp": datetime.utcnow().isoformat(),
        },
        {
            "topic": "Future of Work with Agents",
            "score": 0.84,
            "source": platform,
            "timestamp": datetime.utcnow().isoformat(),
        },
    ]

    result = {"trends": trends[:limit]}

    emit_trace(
        agent="ResearchAgent",
        action="fetch_trends",
        input_payload=input,
        output_payload=result,
    )

    return result
