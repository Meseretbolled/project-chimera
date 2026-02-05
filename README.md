# 🚀 Project Chimera — Governed AI Skill Pipeline

Project Chimera is a modular AI-agent orchestration system that detects trends,
generates content drafts, validates safety through governance rules,
and publishes only when approved.

It demonstrates **contract-enforced agent pipelines** with MCP-style tracing,
approval gates, and responsible publishing workflows.

---

## ✨ Key Features

- ✅ Modular skill-based agent architecture  
- 📈 Trend detection skill (Trend Fetcher)  
- 📝 Caption + hashtag generation (Content Generator)  
- 🛡 Safety validation governance gate  
- 🚫 Publishing blocked unless explicitly approved  
- 📢 Publisher skill schedules approved content  
- 📡 MCP-style trace logging for transparency  
- 🧪 Full contract enforcement via pytest  

---

## 📂 Repository Structure

project-chimera/
│
├── chimera/                  # Core orchestration + governance engine
│   ├── __init__.py
│   ├── orchestrator.py       # Main pipeline coordinator
│   ├── approval.py           # Approval gate enforcement
│   ├── state.py              # Content lifecycle + status tracking
│   └── trace.py              # MCP-style tracing events
│
├── skills/                   # Modular skill agents
│   ├── __init__.py
│   │
│   ├── skill_trend_fetcher/
│   │   ├── contract.json
│   │   ├── README.md
│   │   └── run.py            # Detects trending topics
│   │
│   ├── skill_content_generator/
│   │   ├── contract.json
│   │   ├── README.md
│   │   └── run.py            # Generates captions + hashtags
│   │
│   ├── skill_safety_validator/
│   │   ├── contract.json
│   │   ├── README.md
│   │   ├── __init__.py
│   │   └── run.py            # Safety governance validation
│   │
│   └── skill_publisher/
│       ├── contract.json
│       ├── README.md
│       └── run.py            # Publishes only if approved
│
├── demo/
│   └── run_demo.py           # End-to-end runnable pipeline demo
│
├── tests/                    # Contract + governance enforcement tests
│   ├── test_skills_interface.py
│   └── test_trend_fetcher.py
│
├── docs/                     # Architecture + diagrams + reports
│   ├── diagram/
│   ├── reports/
│   └── research/
│
├── GOVERNANCE.md             # Governance rules and policies
├── AGENT_PLAYBOOK.md         # Agent behavior + coordination guide
├── Dockerfile                # Container support (optional)
├── Makefile                  # Automation helpers
├── pyproject.toml            # Project configuration
└── README.md                 # Main documentation



---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Meseretbolled/project-chimera.git
cd project-chimera
```

2. Create and Activate a Virtual Environment
```python3 -m venv .venv
source .venv/bin/activate
```
3. Install Dependencies

Install the project locally:

```pip install -e .```

✅ Run Governance Contract Tests

All skills must satisfy structured contract outputs.

Run the full test suite:

```pytest -v```


Expected output:

7 passed

▶️ Run the Chimera Demo Pipeline

Execute the full orchestrator demo:

```python demo/run_demo.py```


This runs the complete governed pipeline:

📈 Fetch Trends

📝 Generate Draft Caption

🛡 Validate Safety

📢 Publish Only If Approved

Example Output

🚀 Chimera Pipeline Started...

✅ Trend Detected: AI Influencers

📝 Draft Caption Generated:
🔥 Trend Alert: AI Influencers...

🛡 Safety Validator Status: approved

📢 Publish Result: scheduled

✅ Chimera Pipeline Completed Successfully!

🛡 Governance + Approval Rule

Publishing is blocked unless approval is granted.

Without Approval:
```{
  "approved": false
}
```

Result:

```{
  "publish_status": "blocked",
  "reason": "Governance rule: cannot publish without approval"
}
```
With Approval:
```{
  "approved": true
}

```
Result:

```{
  "publish_status": "scheduled",
  "post_id": "demo_post_001"
}
```

📌 Implemented Skills
Skill Agent	Purpose
Trend Fetcher	Returns trending topics with scores + timestamps
Content Generator	Creates captions + hashtags from trends
Safety Validator	Ensures content meets governance standards
Publisher	Publishes only when approved
📡 MCP Trace Transparency

Chimera emits structured trace events such as:

Agent name

Action performed

Input payload

Output result

Timestamp

This provides auditability and responsible AI governance.

✅ Project Status

Project Chimera successfully demonstrates:

Modular governed skill pipelines

Approval-based publishing control

End-to-end orchestration demo

Full contract validation through tests

MCP-style transparency tracing

👩‍💻 Author

Built by Meseret ✨
Project Chimera — Governed Agent Pipeline Demo
