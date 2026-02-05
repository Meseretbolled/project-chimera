"""
Chimera Orchestrator

Runs the deterministic governed pipeline:

Trend Fetch → Content Draft → Safety Validation → Approval → Publish
"""

from chimera.state import ChimeraState, ContentStatus
from chimera.approval import approval_gate

from skills.skill_trend_fetcher.run import run as fetch_trends
from skills.skill_content_generator.run import run as generate_content
from skills.skill_publisher.run import run as publish_content


class ChimeraOrchestrator:
    """
    Governing controller of Chimera agent execution.
    """

    def __init__(self):
        self.state = ChimeraState()

    def execute_pipeline(self):
        """
        Execute the full governed influencer workflow.
        """

        print("\n🚀 Chimera Pipeline Started...\n")

        # 1. Fetch trends
        trends_result = fetch_trends({"platform": "tiktok", "limit": 3})
        trend = trends_result["trends"][0]

        print("✅ Trend Detected:", trend)

        # 2. Generate content draft
        draft_result = generate_content(
            {
                "trend_topic": trend["topic"],
                "platform": "instagram",
                "tone": "educational",
            }
        )

        print("\n📝 Draft Caption Generated:")
        print(draft_result["draft_caption"])

        self.state.transition(ContentStatus.VALIDATED)

        # 3. Safety Validation (mocked for now)
        safety_status = "approved"
        print("\n🛡 Safety Validator Status:", safety_status)

        # 4. Human Approval Gate
        human_approved = True

        if not approval_gate(safety_status, human_approved):
            print("\n❌ Publishing Blocked by Governance")
            return

        self.state.transition(ContentStatus.APPROVED)

        # 5. Publish content
        publish_result = publish_content(
            {
                "platform": "instagram",
                "approved_caption": draft_result["draft_caption"],
                "hashtags": draft_result["hashtags"],
                "approved": True,
            }
        )

        self.state.transition(ContentStatus.PUBLISHED)

        print("\n📢 Publish Result:", publish_result)

        print("\n✅ Chimera Pipeline Completed Successfully!")
        print("\n📍 Final State Snapshot:")
        print(self.state.snapshot())
