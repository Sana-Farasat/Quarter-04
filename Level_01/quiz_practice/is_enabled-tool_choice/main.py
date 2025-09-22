from connection import config
from agents import (Agent, ModelSettings, Runner, enable_verbose_stdout_logging, function_tool, trace)
import rich
import asyncio

enable_verbose_stdout_logging()

#_________________________Function Tools___________________________

@function_tool(is_enabled= True)
def weather():
     return "Its very sunny today."

@function_tool(is_enabled= True)
def dollar_rate():
     return "Dollar rate is 300."

frontend_developer=Agent(
     name="Frontend Developer",
     instructions="Your task is to answer frontend developemnt related queries.."
)

@function_tool
def search_flights(): return "Flight to NYC: $200, Airport: JFK"

@function_tool  
def book_hotel(airport): return f"Hotel near {airport}: $150"

#_________________________Sub Agents___________________________

backend_developer=Agent(
     name="Backend Developer",
     instructions="Your task is to answer backend development related queries.."
)

#_________________________Main Agent___________________________

triage_agent= Agent(
    name= "Triage Agent",
    instructions="""
    You are a triage agent. Your task is to fullfill user queries 
    by using available tools and sub agents.
    """,
    tools=[weather, dollar_rate, search_flights, book_hotel],
    model_settings=ModelSettings(tool_choice= "required"),
    #tool_use_behavior= "stop_on_first_tool",
    handoffs=[frontend_developer, backend_developer]
)

#_________________________Main Runner___________________________

async def main():

    with trace("is_enabled-tool_choice"):

            result= await Runner.run(
            triage_agent,
            #input= "What is today's dollar rate? and what is today's weather? and what is frontend development?",
            input="Search flight for me and book hotel",
            run_config= config
    )
            rich.print(result.final_output)
            rich.print(result.last_agent.name)
            #rich.print(result.new_items)

if __name__ == "__main__":
    asyncio.run(main())



