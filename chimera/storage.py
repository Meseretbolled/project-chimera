"""
Storage layer (future).

Chimera will persist trend + content metadata here.
"""

class StorageAdapter:
    def save_trend(self, trend: dict):
        raise NotImplementedError("DB layer not implemented yet")

    def save_draft(self, draft: dict):
        raise NotImplementedError("DB layer not implemented yet")
