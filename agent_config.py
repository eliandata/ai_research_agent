from agents import Agent
from tools import web_search, calculator
from guardrails import no_profanity 

research_agent = Agent(
    name="Research Agent",
    instructions="You are a research assistant that answers user queries based on web search.",
    tools=[web_search.web_search]
)

math_agent = Agent(
    name="Math Agent",
    instructions="You help perform numeric calculations like averages.",
    tools=[calculator.calculate_average]
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Decide whether a user question needs research or numeric calculation and forward to the correct agent.",
    handoffs=[research_agent, math_agent],
    input_guardrails=[no_profanity]  
)
