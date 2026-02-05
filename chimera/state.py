"""
Chimera State Machine

Defines the lifecycle of content inside the governed pipeline.

Draft → Validated → Approved → Published
"""

from enum import Enum


class ContentStatus(str, Enum):
    DRAFT = "draft"
    VALIDATED = "validated"
    APPROVED = "approved"
    PUBLISHED = "published"


class ChimeraState:
    """
    Tracks the current governed state of the system.
    """

    def __init__(self):
        self.status = ContentStatus.DRAFT
        self.history = []

    def transition(self, new_status: ContentStatus):
        """
        Move the system to a new valid state.
        """
        self.history.append((self.status, new_status))
        self.status = new_status

    def snapshot(self) -> dict:
        """
        Return observable state snapshot.
        """
        return {
            "current_status": self.status,
            "history": self.history,
        }
