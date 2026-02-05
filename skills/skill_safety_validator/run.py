"""Safety Validator Skill

This skill validates generated content against simple safety heuristics
and returns a structured status for governance decisions.
"""

from chimera.trace import emit_trace


def run(input: dict) -> dict:
    """Validate `input` content and return `{status, reason}`.

    Expected input:
        { "content": "...", "platform": "instagram" }
    """

    content = input.get("content", "")
    platform = input.get("platform")

    # Basic validation
    if not content:
        result = {"status": "rejected", "reason": "empty content"}
        emit_trace(
            agent="SafetyValidator",
            action="validate_content",
            input_payload=input,
            output_payload=result,
        )
        return result

    # Heuristic checks (placeholder for real policy rules)
    lowered = content.lower()
    if any(word in lowered for word in ["kill", "bomb", "suicide"]):
        result = {"status": "rejected", "reason": "violence or self-harm detected"}
    elif any(word in lowered for word in ["politic", "election", "vote"]):
        result = {"status": "needs_human_review", "reason": "political content — human review required"}
    else:
        result = {"status": "approved", "reason": "No policy issues detected"}

    emit_trace(
        agent="SafetyValidator",
        action="validate_content",
        input_payload=input,
        output_payload=result,
    )

    return result
