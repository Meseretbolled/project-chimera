import json
from pathlib import Path

import pytest


def _load_schema(name: str):
    p = Path(__file__).resolve().parent.parent / "specs" / "schemas" / f"{name}.json"
    return json.loads(p.read_text())


def _require_jsonschema():
    try:
        import jsonschema

        return jsonschema
    except Exception:
        pytest.skip("jsonschema not installed; skip contract schema validation")


def test_trend_fetcher_matches_schema():
    jsonschema = _require_jsonschema()
    from skills.skill_trend_fetcher.run import run as fetch_trends

    schema = _load_schema("trend_fetcher")
    result = fetch_trends({"platform": "tiktok", "limit": 1})
    jsonschema.validate(result, schema)


def test_content_generator_matches_schema():
    jsonschema = _require_jsonschema()
    from skills.skill_content_generator.run import run as gen

    schema = _load_schema("content_generator")
    result = gen({"trend_topic": "AI", "platform": "instagram", "tone": "educational"})
    jsonschema.validate(result, schema)


def test_safety_validator_matches_schema():
    jsonschema = _require_jsonschema()
    from skills.skill_safety_validator.run import run as validate

    schema = _load_schema("safety_validator")
    result = validate({"content": "test content", "platform": "instagram"})
    jsonschema.validate(result, schema)


def test_publisher_matches_schema():
    jsonschema = _require_jsonschema()
    from skills.skill_publisher.run import run as publish

    schema = _load_schema("publisher")
    # test blocked and scheduled cases
    result_blocked = publish({"platform": "instagram", "approved_caption": "x", "hashtags": [], "approved": False})
    jsonschema.validate(result_blocked, schema)

    result_ok = publish({"platform": "instagram", "approved_caption": "x", "hashtags": [], "approved": True})
    jsonschema.validate(result_ok, schema)
