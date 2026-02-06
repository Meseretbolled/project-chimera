"""
Minimal CLI Dashboard (Frontend Placeholder)

Chimera does not ship a web UI yet.
This dashboard provides a lightweight interface
to run the governed influencer pipeline.
"""

from chimera.orchestrator import run_pipeline

if __name__ == "__main__":
    print("=== Chimera CLI Dashboard ===")
    result = run_pipeline()
    print("\nFinal Output Snapshot:\n")
    print(result)
