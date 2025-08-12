import asyncio
import datetime
from agents import Agent, Runner, function_tool
from connection import config, model

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"

@function_tool
def get_date_time():
    return datetime.date.today()

# Helper Agent
helper = Agent(
    name="Helper agent",
    # instructions="Always respond in haiku form",
    instructions="You are an helpful assistant",
    model= model,
    tools=[get_weather, get_date_time],
)

async def main():
    result = await Runner.run(helper, "What is Date today?", 
                              run_config=config
                              )
    # print(result.new_items[2])
    print(result.final_output)
    # print(result.new_items[1].raw_item)
    
if __name__ == "__main__":
    asyncio.run(main())