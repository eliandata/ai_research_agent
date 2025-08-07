from agents import Agent, Runner
from tools.web_search import web_search
from tools.calculator import calculate_average

# Agentes
research_agent = Agent(
    name="Research Agent",
    instructions="You are a research assistant that answers user queries based on web search.",
    tools=[web_search]
)

math_agent = Agent(
    name="Math Agent",
    instructions="You help perform numeric calculations like averages.",
    tools=[calculate_average]
)

# Agente triage para enrutamiento inteligente
triage_agent = Agent(
    name="Triage Agent",
    instructions="Decide whether a user question needs research or numeric calculation and forward to the correct agent.",
    handoffs=[research_agent, math_agent]
)

# ✅ Runner asociado al agente principal
triage_runner = triage_agent.as_runner()
