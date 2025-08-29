from pydantic import BaseModel
from connection import config
from agents import (Agent,
                     RunContextWrapper, 
                     Runner, 
                     function_tool, input_guardrail, 
                     GuardrailFunctionOutput, 
                     InputGuardrailTripwireTriggered)
import rich
import asyncio

#_________________________Structured Output___________________________

class InputStructuredType(BaseModel):
    response: str
    isBeyondQuery: bool

#_________________________Guardrail Agent___________________________

guardrail_agent = Agent(
     name= "Guardrail Agent",
     instructions="""
    Your task is to answer user queries related to frontend development , backend development and also answer for those queries for which function tools are available. Beyond these don't answer and reply user politely.
""",
output_type= InputStructuredType
)

#_________________________Guradrail Function___________________________

@input_guardrail
async def guardrail_function(ctx: RunContextWrapper, agent: Agent, input) -> GuardrailFunctionOutput:
    result= await Runner.run(
       guardrail_agent,
       input
    )
    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isBeyondQuery
    )

#_________________________Function Tools___________________________

@function_tool
def weather():
     return "Its very sunny today."

@function_tool
def dollar_rate():
     return "Dollar rate is 300."

#_________________________Sub Agents___________________________

frontend_developer=Agent(
    name= "Frontend Developer",
    instructions= "You are a frontend developer. Your task is to answer and solve user queries related to frontend development.",
    handoff_description="Handles all frontend related tasks such as HTML, CSS, JavaScript, React, Nextjs, UI design."
)

backend_developer=Agent( 
    name= "Backend Developer",
    instructions= "You are a backend developer. Your task is to answer and solve user queries related to backend development.",
    handoff_description="Handles backend tasks such as APIs, databases, authentication, server logic."
)

#_________________________Main Agent___________________________

triage_agent= Agent(
    name= "Triage Agent",
    instructions="""
    You are a triage agent. Your task is to fullfill user queries by using available tools and handoffs. Must use tools and handoffs.
    """,
    handoffs=[backend_developer, frontend_developer],
    tools=[weather, dollar_rate],
    input_guardrails=[guardrail_function]
)

#_________________________Main Runner___________________________

async def main():

    try:
        result= await Runner.run(
        triage_agent,
        # input= "what is server logic? and what is frontend development?  and what is dollar rate? and what is the weather? ",
        #input= " what is the weather and what is the dollar rate?",
        #input= "what is the dollar rate and  what is the weather?",
        #input= " What is frontend development and what is authentication?",
        #input= "What is authentictaion and what is frontend development",
        input= " Tell me roadmap for fullstack development.",
        run_config= config
    )
        rich.print("[bold green]Final Output:[/bold green]", result.final_output)
        rich.print("[bold blue]Last Agent:[/bold blue]", result.last_agent.name)

    except InputGuardrailTripwireTriggered:
        rich.print("[bold red]Exception Raised.............[/bold red]")


if __name__ == "__main__":
    asyncio.run(main())



