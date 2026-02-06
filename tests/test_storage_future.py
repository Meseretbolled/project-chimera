import pytest

@pytest.mark.xfail(reason="Storage layer planned but not implemented yet")
def test_trends_are_persisted():
    from chimera.storage import StorageAdapter
    db = StorageAdapter()
    db.save_trend({"topic": "AI", "score": 0.9})
