import rich
import asyncio
from main import config
from pydantic import BaseModel

from agents import (Agent, OutputGuardrailTripwireTriggered,RunContextWrapper, 
Runner, 
input_guardrail,
GuardrailFunctionOutput,
InputGuardrailTripwireTriggered, 
output_guardrail
)

#_________________________INPUT GUARDRAILS_____________________________

# For Structured Output
class AC(BaseModel):
    response: str
    isTooCold: bool 

# Guardrails Agent
father_agent = Agent(
    name= "Father Agent",
    instructions= """
    You are a strict father. Your child should never run the AC below 26°C.
    If the input message shows the child is setting the AC below 26°C, return:
    - isTooCold: true
    - response: Explain why it's not allowed

    If it's 26°C or above, return:
    - isTooCold: false
    - response: Approve the setting
    """,
    output_type= AC
)

@input_guardrail
async def father_guardrail(ctx: RunContextWrapper, agent: Agent, input)-> GuardrailFunctionOutput:
    result= await Runner.run(
        father_agent,
        input,
        run_config= config
    )

    rich.print(result.final_output)

    return GuardrailFunctionOutput(
            output_info= result.final_output.response,
            tripwire_triggered=  result.final_output.isTooCold
        )

# Main agent
child_agent = Agent(
    name = 'Child Agent',
    instructions="You are a child who wants to run the AC.",
    input_guardrails=[father_guardrail]
)

async def ig_main():
        try:
            result = await Runner.run(child_agent , 
                                      'I set AC on 16 degree to chill room fully', 
                                      run_config=config)
            rich.print(result.final_output)
            rich.print("[green]AC is now ON.[/green]")

        except InputGuardrailTripwireTriggered:
            rich.print("[red]AC is OFF – it's set too low![/red]")


if __name__ == "__main__":
    asyncio.run(ig_main())

