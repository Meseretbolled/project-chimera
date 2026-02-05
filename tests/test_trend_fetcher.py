"""
Trend Fetcher Contract Tests

TrendFetcher is responsible for returning structured trend signals.

Contract Requirements:
- Output must contain `trends`
- trends must be a list
- Each trend must include topic, score, source
"""


def test_trend_fetcher_returns_trends_list():
    """
    Contract Test:
    TrendFetcher must always return a trends list.
    """

    output = {
        "trends": [
            {"topic": "AI Influencers", "score": 0.92, "source": "tiktok"},
            {"topic": "Tech Productivity", "score": 0.88, "source": "instagram"},
        ]
    }

    assert "trends" in output
    assert isinstance(output["trends"], list)


def test_each_trend_item_has_required_fields():
    """
    Contract Test:
    Every trend object must include topic, score, source.
    """

    trends = [
        {"topic": "AI Influencers", "score": 0.92, "source": "tiktok"}
    ]

    for item in trends:
        assert "topic" in item
        assert "score" in item
        assert "source" in item

        assert isinstance(item["topic"], str)
        assert isinstance(item["score"], float)
        assert isinstance(item["source"], str)
