"""
Chimera Demo Runner

This is the ONE command evaluators will run:

python demo/run_demo.py
"""

from chimera.orchestrator import ChimeraOrchestrator


if __name__ == "__main__":
    orchestrator = ChimeraOrchestrator()
    orchestrator.execute_pipeline()
