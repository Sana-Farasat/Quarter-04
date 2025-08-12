import asyncio
from agents import Agent, Runner, function_tool
import requests
from connection import config, model

@function_tool
def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    res = requests.get(url)
    return res.text

# Weather Agent
weather = Agent(
    name="Weather agent",
    # instructions="Always respond in haiku form",
    instructions="You are a weather agent. You will answer related to weather queries.",
    model= model,
    tools=[get_weather],
)

async def main():
    result = await Runner.run(weather,
                               """What is today's weather of karachi?
                               What is today's weather of quetta?
                               What is today's weather of islamabad?
                               What is today's weather of lahore?""", 
                              run_config=config
                              )
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())