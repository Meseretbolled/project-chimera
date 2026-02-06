# 🧠 Project Chimera — Governed Agentic Content Pipeline

Project Chimera is a **spec-driven, governed multi-agent content automation system** designed to simulate Autonomous AI Influencers.

It detects social trends, generates platform-ready content, validates safety, and publishes only through **human-in-the-loop approval gates**.

This repository was built as part of the **Project Chimera 3-Day Architecture Challenge**, emphasizing:

- Spec-Driven Development (SDD)
- Agent skill contract enforcement
- Governance-first automation
- MCP-style traceability
- CI/CD + Docker reproducibility
- Test-defined future expansion slots

---

## 🚀 What Chimera Does

Chimera simulates an autonomous influencer pipeline:

1. **Trend Detection Agent**  
   Fetches trending topics from a platform source.

2. **Content Generation Agent**  
   Produces caption drafts and hashtags.

3. **Safety Validator Agent**  
   Ensures generated content meets governance rules.

4. **Publishing Agent (Governed)**  
   Blocks publishing unless explicitly approved.

5. **Orchestrator**  
   Executes the full lifecycle with state transitions.

---

## 📌 Spec-Driven Development (SDD)

Chimera follows **Spec-Driven Development**, meaning:

- All system intent is defined first inside `specs/`
- Skills must match structured contracts
- Agents are forbidden to “vibe-code” outside specification boundaries

Specifications are the single source of truth for:

- Skill input/output schemas  
- Governance rules  
- OpenClaw integration roadmap  
- Metadata + publishing workflows  

---

## 👤 Human-in-the-Loop Governance

Publishing is never automatic.

Chimera enforces a mandatory approval gate:

This ensures responsible automation and controlled deployment.

📂 Repository Structure
```
project-chimera/
│
├── chimera/                     # Core orchestrator + governance engine
│   ├── orchestrator.py           # Executes full pipeline
│   ├── state.py                  # Content lifecycle state machine
│   ├── approval.py               # Governance approval gate logic
│   └── trace.py                  # MCP-style trace event logger
│
├── skills/                      # Modular runtime skill agents
│   ├── skill_trend_fetcher/      # Detects trends
│   ├── skill_content_generator/  # Generates captions + hashtags
│   ├── skill_safety_validator/   # Validates content safety
│   └── skill_publisher/          # Governed publishing enforcement
│
├── specs/                       # Executable project intent (SDD source)
│   ├── _meta.md
│   ├── functional.md
│   ├── technical.md
│   └── openclaw_integration.md
│
├── tests/                       # Contract + governance enforcement tests
│   ├── test_skills_interface.py
│   ├── test_trend_fetcher.py
│   └── test_openclaw_future.py  # Intentional failing future slot
│
├── demo/
│   └── run_demo.py              # Runs the full Chimera pipeline
│
├── Dockerfile                   # Containerized reproducibility
├── Makefile                     # Standard execution commands
├── .github/workflows/main.yml   # CI pipeline (make test)
├── GOVERNANCE.md                # Governance + safety policy
└── README.md
```
⚙️ Installation (Local)

Clone the repository:
```git clone https://github.com/Meseretbolled/project-chimera.git
cd project-chimera
```
Create and activate a virtual environment:

``` python3 -m venv .venv
source .venv/bin/activate
```


Install dependencies:

``` pip install -e .````

✅ Running Unit Tests (TDD + Future Slot)

Run all tests:

``` pytest -v ```


Expected result:

Core skills + governance tests pass

One test may fail intentionally:

``` test_openclaw_future.py ```

This defines a future integration slot for broadcasting Chimera status to the OpenClaw Agent Social Network.

Example:

``` 1 failed, 7 passed ```


This is intentional and demonstrates true TDD:

The test defines the next capability boundary before implementation.

🎬 Running the Full Demo Pipeline

Run Chimera end-to-end:

```python demo/run_demo.py```


Example output:

🚀 Chimera Pipeline Started...
✅ Trend Detected: AI Influencers
📝 Draft Caption Generated...
🛡 Safety Validator Status: approved
📢 Publish Result: scheduled
✅ Chimera Pipeline Completed Successfully!

🐳 Running Chimera with Docker

Build the container:

``` docker build -t chimera .
```

Run the test suite inside Docker:

``` docker run chimera ```

🛠 Makefile Commands

Standardized developer commands:
```
make install       # Install project locally
make test          # Run pytest suite
make demo          # Run full orchestrator pipeline
make docker-build  # Build Docker image
make docker-run    # Run tests inside Docker
```
🔁 CI/CD & AI Governance

Chimera includes an automated governance pipeline:

GitHub Actions runs make test on every push

Workflow defined in:
```
.github/workflows/main.yml
```

Future expansion includes AI reviewer enforcement (CodeRabbit-style spec alignment).

📡 MCP Trace Logging

Each agent emits structured trace events:
```
{
  "agent": "ContentAgent",
  "action": "generate_caption",
  "input": {...},
  "output": {...}
}
```

This provides full observability across the autonomous pipeline.

🎥 Loom Walkthrough (Submission)

The Loom demo covers:

Spec structure + governance intent

Skill modularity + contracts

Approval-based publishing enforcement

TDD approach with future failing slot

Docker reproducibility

OpenClaw integration roadmap

📌 Loom Video Link: (to be added before submission)

✅ Challenge Completion Summary

This repository satisfies the Project Chimera Challenge requirements:

Spec-driven architecture (specs/)

Modular agent skills (skills/)

Governance enforcement + approval gates

Contract-based testing (tests/)

Intentional future slot test for OpenClaw expansion

Docker + Makefile automation

CI pipeline via GitHub Actions

MCP-style traceability + observability