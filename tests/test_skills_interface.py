"""
Skill Interface Tests — Project Chimera

These tests enforce governance contracts:

- Every skill must define run()
- Outputs must be structured dicts
- Publishing must be blocked unless approved
"""

from skills.skill_trend_fetcher.run import run as fetch_trends
from skills.skill_content_generator.run import run as generate_content
from skills.skill_publisher.run import run as publish_content
from skills.skill_safety_validator.run import run as validate_safety


def test_all_skills_define_run_function():
    assert callable(fetch_trends)
    assert callable(generate_content)
    assert callable(validate_safety)
    assert callable(publish_content)


def test_skill_outputs_must_be_structured_dict():
    result = fetch_trends({"platform": "tiktok", "limit": 1})
    assert isinstance(result, dict)
    assert "trends" in result


def test_safety_validator_returns_status():
    result = validate_safety(
        {"content": "AI is changing everything", "platform": "instagram"}
    )

    assert "status" in result
    assert result["status"] in ["approved", "rejected", "needs_human_review"]


def test_publishing_is_blocked_without_approval():
    result = publish_content(
        {
            "platform": "instagram",
            "approved_caption": "Draft content",
            "hashtags": ["#AI"],
            "approved": False,
        }
    )

    assert result["publish_status"] == "blocked"


def test_publishing_succeeds_with_approval():
    result = publish_content(
        {
            "platform": "instagram",
            "approved_caption": "Approved content",
            "hashtags": ["#AI"],
            "approved": True,
        }
    )

    assert result["publish_status"] == "scheduled"
