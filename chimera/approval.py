"""
Approval Gate

Chimera enforces governance:

No publishing unless:
- Safety validated
- Human approval satisfied
"""

def approval_gate(safety_status: str, human_approved: bool) -> bool:
    """
    Final approval boundary.

    Returns True only if:
    - safety_status == "approved"
    - human_approved == True
    """

    if safety_status != "approved":
        return False

    if not human_approved:
        return False

    return True
