from chimera.trace import emit_trace

"""
Publisher Skill

Publishing is strictly governed.
This skill only schedules content if approved=True.
"""


def run(input: dict) -> dict:
    approved = input.get("approved", False)

    if not approved:
        return {
            "publish_status": "blocked",
            "reason": "Governance rule: cannot publish without approval",
        }

    platform = input.get("platform")
    caption = input.get("approved_caption")
    hashtags = input.get("hashtags", [])

    if not platform or not caption:
        raise ValueError("platform and approved_caption are required")

    return {
        "publish_status": "scheduled",
        "platform": platform,
        "post_id": "demo_post_001",
        "hashtags": hashtags,
    }
