from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="gemma2-9b-it"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


### Add agents to the list (DO NOT REMOVE agents_list) ###
# This list is used in app.py to create the Playground object
# and pass the agents to the Playground object.
# Add new agents to this list as needed.
agents_list = [web_agent]
