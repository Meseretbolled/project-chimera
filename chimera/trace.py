"""
MCP Trace Emitter — Project Chimera

All governed agent actions must emit structured trace events.

This simulates MCP Sense observability.
"""

import json
from datetime import datetime


def emit_trace(agent: str, action: str, input_payload: dict, output_payload: dict):
    """
    Emit a structured trace event.

    This is the audit record of Chimera execution.
    """

    trace_event = {
        "timestamp": datetime.utcnow().isoformat(),
        "agent": agent,
        "action": action,
        "input": input_payload,
        "output": output_payload,
    }

    print("\n📡 MCP TRACE EVENT:")
    print(json.dumps(trace_event, indent=2))
