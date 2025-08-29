import asyncio
from pydantic import BaseModel
import rich
from connection import config
from agents import Agent, RunContextWrapper, Runner

class Traveler(BaseModel):
    trip_type : str
    traveler_profile : str 
    
adventure = Traveler(trip_type= "Adventure", traveler_profile= "Solo")
cultural = Traveler(trip_type= "Cultural", traveler_profile= "Family")
business = Traveler(trip_type= "Business", traveler_profile= "Executive")

def my_dynamic_instructions(ctx: RunContextWrapper[Traveler], agent: Agent)->str:

    if ctx.context.trip_type == "Adventure" and ctx.context.traveler_profile == "Solo":
        return"""
    Suggest exciting activities, focus on safety tips, recommend social hostels and group tours for meeting people. 
    """
    elif ctx.context.trip_type == "Cultural" and ctx.context.traveler_profile == "Family":
        return"""
    Focus on educational attractions, kid-friendly museums, interactive experiences, family accommodations.
    """
    elif ctx.context.trip_type == "Business" and ctx.context.traveler_profile == "Executive":
        return"""
    Emphasize efficiency, airport proximity, business centers, reliable wifi, premium lounges.
    """

travel_planning_agent = Agent(
    name= "Travel Planning Agent",
    instructions= my_dynamic_instructions
)

async def main():
    
    prompt= "I have to go UK for company meeting."
    instruction = my_dynamic_instructions(RunContextWrapper(context=business), travel_planning_agent)

    result = await Runner.run(
        travel_planning_agent, 
        prompt,
        run_config=config,
        context= business
        )
    
    rich.print(f"\n[bold blue]Prompt: {prompt} [/bold blue]")
    rich.print(f"\n[bold green]Using Instructions:{instruction.strip()} [/bold green] ")
    rich.print(f"\n[bold yellow]Agent Output: {result.final_output} [/bold yellow]")

if __name__ == "__main__":
    asyncio.run(main())
