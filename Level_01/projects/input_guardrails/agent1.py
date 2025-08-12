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
class SchoolStudent(BaseModel):
    response: str
    isNotStudent: bool

# Guardrails Agent
gate_keeper_agent = Agent(
    name= "Gate Keeper Agent",
    instructions= """
    Your task is to allowed students only to enter of this *The Smart School*.. Deny others school students !
    """,
    output_type= SchoolStudent
)

@input_guardrail
async def gate_keeper_guardrail(ctx: RunContextWrapper, agent: Agent, input)-> GuardrailFunctionOutput:
    result= await Runner.run(
        gate_keeper_agent,
        input,
        run_config= config
    )

    rich.print(result.final_output)

    return GuardrailFunctionOutput(
            output_info= result.final_output.response,
            tripwire_triggered=result.final_output.isNotStudent
        )

# Main agent
student_agent = Agent(
    name = 'Student Agent',
    instructions="You are a student agent",
    input_guardrails=[gate_keeper_guardrail]
)
async def ig_main():
        try:
            result = await Runner.run(student_agent , 
                                      """I am *Hoor Bai School* Student could I visit this *The Smart School* for my research work?""", 
                                      run_config=config)
            rich.print(result.final_output)
            rich.print("You are allowed to come inside this school")

        except InputGuardrailTripwireTriggered:
            rich.print('You are not allowed to come inside this school')

if __name__ == "__main__":
    asyncio.run(ig_main())

