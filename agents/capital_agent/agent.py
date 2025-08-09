from google.adk.agents.llm_agent import Agent

def get_capital_city(country: str) -> str:
    """Retrieve the capital city of a given country."""
    capitals = {"korea": "Seoul", "canada": "Ottawa"}
    return capitals.get(country.lower(), f"Sorry, I don't know the capital of {country}.")

# Create the root agent
# 무조건 변수가 root_agent 이어야 한다
root_agent = Agent(
    model='gemini-2.5-flash',
    name='capital_agent',
    description='Answer questions about capital cities.',
    instruction='You are a helpful assistant that provides information about capital cities.',
    tools=[get_capital_city] # agent tool
)
