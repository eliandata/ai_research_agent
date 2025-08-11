# AI Research Agent
FastAPI service powered by the OpenAI Agents SDK that answers research questions and performs basic calculations.

It uses a triage system to route queries either to a Web Search Agent or a Math Agent, with guardrails to block offensive input.

# 📂 Repository structure
```
ai_agent_project/
├── tools/
│   ├── web_search.py       # Web search tool using DuckDuckGo
│   └── calculator.py       # Simple average calculator
├── agent_config.py         # Agents, routing logic, and guardrails
├── guardrails.py           # Input validation logic (profanity filter)
├── main.py                 # FastAPI application
├── .env                    # Environment variables
└── requirements.txt        # Dependencies
```
# 🚀 1. Clone the repository
```
git clone https://github.com/eliandata/ai_research_agent.git ai_agent_project
cd ai_agent_project
```

# 📦 2. Create and activate a virtual environment

## macOS / Linux
```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

## Windows 
```
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
```

To deactivate later:
```
deactive
```

# 📜 3. Install dependencies
```
pip install -r requirements.txt

```

# 🔑 4. Configure environment variables
```
OPENAI_API_KEY=sk-********************************
```

# ▶ 5. Run the API with Uvicorn
From the project root:
```
uvicorn main:app --reload
```

# 🧪 6. Quick test
**Using Swagger UI**
Go to http://127.0.0.1:8000/docs

Expand POST /ask

Click Try it out and enter:
```
{
  "question": "What were the main causes and consequences of the Chernobyl disaster?"
}

```

# 🛡 Guardrails
This agent includes an input guardrail that blocks offensive or inappropriate questions.

If triggered, the API will return a 400 Bad Request with an explanation.

# 📌 Example questions for testing
**✅ Valid research & calculation queries**

What were the main causes and consequences of the Chernobyl nuclear disaster in 1986?

Who was the first woman to win a Nobel Prize in Physics and for what discovery?

How has CRISPR gene-editing technology changed agricultural research in the last decade?

What scientific evidence supports the theory of continental drift proposed by Alfred Wegener?

Compute the average of [23, 45, 67, 89].






