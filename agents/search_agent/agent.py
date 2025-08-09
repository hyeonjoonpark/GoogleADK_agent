from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description="Google Search Agent",
    instruction='You are a helpful assistant that provides information about search queries.',
    tools=[google_search]  # agent tool
)
