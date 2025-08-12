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

#__________________________ GUARDRAILS_____________________________

# For Structured Output
class AdminTask(BaseModel):
    response: str
    isAdminTask: bool 

#____________________TEACHER (GUARDRAIL) AGENT_______________________
teacher_agent = Agent(
    name= "Teacher Agent",
    instructions= """
    You are a teacher agent. You will teach your students and answer their study related queries only, if any student ask or discuss you something admin related task, gracefully deny them and suggest them to go to admin for sorting out admin related tasks, return:
    - isAdminTask: true
    - response: Explain why to go admin

    If it's not admin task, return:
    - isAdminTask: false
    - response: Gracefully answer
    """,
    output_type= AdminTask
)

#_________________________INPUT GUARDRAILS_____________________________

@input_guardrail
async def teacher_input_guardrail(ctx: RunContextWrapper, agent: Agent, input)-> GuardrailFunctionOutput:
    result= await Runner.run(
        teacher_agent,
        input,
        run_config= config
    )

    rich.print("[blue]Input Check:[/blue]", result.final_output)

    return GuardrailFunctionOutput(
            output_info= result.final_output.response,
            tripwire_triggered=  result.final_output.isAdminTask
        )

#_________________________OUTPUT GUARDRAILS_____________________________

@output_guardrail
async def teacher_output_guardrail(ctx: RunContextWrapper, agent: Agent, output_text: str) -> GuardrailFunctionOutput:
    """
    Re-checks if the output content still includes any admin task handling.
    """
    result = await Runner.run(
        teacher_agent,
        output_text,
        run_config=config
    )
    rich.print("[yellow]Output Check:[/yellow]", result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isAdminTask
    )

#_________________________STUDENT (MAIN) AGENT_____________________________

student_agent = Agent(
    name = 'Student Agent',
    instructions="You are a student who wants to change your class timings.",
    input_guardrails=[teacher_input_guardrail],
    output_guardrails=[teacher_output_guardrail]
)

#_________________________MAIN RUNNER_____________________________

async def iog_main():
        try:
            result = await Runner.run(student_agent , 
                                      'I want to change my class timings 😭😭', 
                                      run_config=config)
            rich.print(result.final_output)
            rich.print("[green]Study Related Task..[/green]")

        except InputGuardrailTripwireTriggered:
            rich.print("[red]Input Blocked: This is an Admin Task![/red]")

        except OutputGuardrailTripwireTriggered:
             rich.print("[red]Output Blocked: Response includes Admin Task![/red]")


if __name__ == "__main__":
    asyncio.run(iog_main())

