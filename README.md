# AI Research Agent
FastAPI service powered by the OpenAI Agents SDK that answers research questions and performs basic calculations.
It uses a triage system to route queries either to a Web Search Agent or a Math Agent, with guardrails to block offensive input.

# 📂 Repository structure
ai_agent_project/
├── tools/
│   ├── web_search.py       # Web search tool using DuckDuckGo
│   └── calculator.py       # Simple average calculator
├── agent_config.py         # Agents, routing logic, and guardrails
├── guardrails.py           # Input validation logic (profanity filter)
├── main.py                 # FastAPI application
├── .env                    # Environment variables
└── requirements.txt        # Dependencies
