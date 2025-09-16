from connection import config
from agents import (Agent, ModelSettings, Runner, function_tool, trace)
import rich
import asyncio

#_________________________Function Tools___________________________

@function_tool(is_enabled= True)
def weather():
     return "Its very sunny today."

@function_tool(is_enabled= True)
def dollar_rate():
     return "Dollar rate is 300."

#_________________________Main Agent___________________________

triage_agent= Agent(
    name= "Triage Agent",
    instructions="""
    You are a triage agent. Your task is to fullfill user queries 
    by using available tools.
    """,
    tools=[weather, dollar_rate],
    model_settings=ModelSettings(tool_choice= "auto"),
)

#_________________________Main Runner___________________________

async def main():

    with trace("is_enabled-tool_choice"):

            result= await Runner.run(
            triage_agent,
            input= "What is today's dollar rate?",
            run_config= config
    )
            rich.print(result.final_output)
            rich.print(result.last_agent.name)
            rich.print(result.new_items)

if __name__ == "__main__":
    asyncio.run(main())



