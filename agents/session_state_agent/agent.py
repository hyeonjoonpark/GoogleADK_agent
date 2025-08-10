from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext

def set_preferences(category: str, value: str, tool_context: ToolContext) -> dict:
    """Set user preferences for a specific category."""
    preferences = tool_context.state.get('user_preferences', {})
    preferences[category] = value
    tool_context.state['user_preferences'] = preferences
    return {
        'status': 'success',
        'preferences': preferences
    }

def get_preferences(tool_context: ToolContext) -> dict:
    """Get user preferences for a specific category."""
    preferences = tool_context.state.get('user_preferences', {})
    return {
        'status': 'success',
        'preferences': preferences
    }

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[set_preferences, get_preferences]
)
