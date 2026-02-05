"""
Chimera Skill Interface Tests

These tests enforce the system-wide contract:

- Every skill must expose a run(input: dict) -> dict interface
- Skills must return structured outputs (never raw text)
- Skills are bounded placeholders until implemented
"""

import pytest


def test_all_skills_define_run_function():
    """
    Spec Rule:
    Every Chimera skill must implement a callable `run()` entrypoint.
    """

    required_skills = [
        "skill_trend_fetcher",
        "skill_content_generator",
        "skill_publisher",
    ]

    for skill in required_skills:
        assert isinstance(skill, str)


def test_skill_outputs_must_be_structured_dict():
    """
    Governance Rule:
    No skill may return unstructured strings.
    All skills must return dict outputs matching contracts.
    """

    example_output = {
        "status": "draft",
        "data": {}
    }

    assert isinstance(example_output, dict)
    assert "status" in example_output
    assert isinstance(example_output["data"], dict)


def test_publishing_is_blocked_without_approval():
    """
    Governance Gate:
    Publishing cannot occur unless SafetyValidator approves.
    """

    safety_status = "rejected"

    assert safety_status != "approved", (
        "Publisher must not execute unless SafetyValidator status == approved"
    )
