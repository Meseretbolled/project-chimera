"""
Content Generator Skill

Generates a governed draft caption + hashtags from a trend topic.
Output is always a draft until validated and approved.
"""


def run(input: dict) -> dict:
    """
    Input:
        {
          "trend_topic": "AI Influencers",
          "platform": "instagram",
          "tone": "educational"
        }

    Output:
        {
          "draft_caption": "...",
          "hashtags": [...]
        }
    """

    topic = input.get("trend_topic")
    platform = input.get("platform", "instagram")
    tone = input.get("tone", "educational")

    if not topic:
        raise ValueError("trend_topic must not be empty")

    caption = (
        f"🔥 Trend Alert: {topic}\n\n"
        f"Creators on {platform} are using this trend to reshape digital culture.\n"
        f"Tone: {tone}.\n\n"
        "Chimera agents detect trends, generate content, validate safety, "
        "and publish responsibly through governance gates."
    )

    hashtags = ["#AI", "#Trends", "#Chimera", "#InfluencerNetwork"]

    return {
        "draft_caption": caption,
        "hashtags": hashtags,
    }
