import asyncio
from pydantic import BaseModel
import rich
from connection import config
from agents import Agent, RunContextWrapper, Runner

class Passenger(BaseModel):
    seat_preference : str
    travel_experience : str | int
    
passenger_one= Passenger(seat_preference= "Window", travel_experience= "First time")
passenger_two= Passenger(seat_preference= "Middle", travel_experience= "Frequent")
passenger_three= Passenger(seat_preference= "Any", travel_experience= "Premium")

def my_dynamic_instructions(ctx: RunContextWrapper[Passenger], agent: Agent)->str:

    if ctx.context.seat_preference == "Window" and ctx.context.travel_experience == "First time":
        return"""
    Explain window benefits, mention scenic views, reassure about flight experience.
    """
    elif ctx.context.seat_preference == "Middle" and ctx.context.travel_experience == "Frequent":
        return"""
    Acknowledge the compromise, suggest strategies, offer alternatives.
    """
    elif ctx.context.seat_preference == "Any" and ctx.context.travel_experience == "Premium":
        return"""
    Highlight luxury options, upgrades, priority boarding
    """
    else:
        return "Provide general seat options and tips."

airline_booking_agent = Agent(
    name= "Airline Booking Agent",
    instructions= my_dynamic_instructions
)

async def main():

    prompt = "Is the window seat good for a first-time flyer?"

    instruction = my_dynamic_instructions(RunContextWrapper(context=passenger_one), airline_booking_agent)
    
    result = await Runner.run(
        airline_booking_agent,
        prompt,
        run_config=config,
        context=passenger_one #Local context
    )
    
    rich.print(f"\n[bold blue]Prompt: {prompt} [/bold blue]")
    rich.print(f"\n[bold green]Using Instructions:{instruction.strip()} [/bold green] ")
    rich.print(f"\n[bold yellow]Agent Output: {result.final_output} [/bold yellow]")

if __name__ == "__main__":
    asyncio.run(main())
