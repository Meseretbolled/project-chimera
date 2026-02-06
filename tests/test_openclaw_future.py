def test_openclaw_status_broadcast_not_implemented_yet():
    """
    Future slot: Chimera should broadcast its availability
    to the OpenClaw agent social network.
    """
    from chimera.orchestrator import broadcast_status

    result = broadcast_status()

    assert result["network"] == "openclaw"
