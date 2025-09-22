from agents import Agent, ModelSettings, Runner, StopAtTools, enable_verbose_stdout_logging, function_tool
from connection import config
from datetime import datetime
import rich

enable_verbose_stdout_logging()

@function_tool
def get_weather(city:str)->str:
    return f'the weather of {city} is rainy'

@function_tool
def get_date():
    _now= datetime.now()
    return _now.strftime("the date is %d-%m-%Y")

@function_tool()
def multiply(num1: int, num2: int) -> int:
    return num1 * num2

#____________________function_tool_settings_____________________
agent=Agent(
    name="assistant",
    instructions="you are a helpful assistant",
    tools=[get_date,get_weather, multiply],
    model_settings= ModelSettings(
        tool_choice= "auto",
        # tool_choice= "required"
        # tool_choice= "None"
        # tool_choice= "multiply"
        # parallel_tool_calls= True
    ),
    # tool_use_behavior="stop_on_first_tool"
    tool_use_behavior=StopAtTools(stop_at_tool_names="get_date")
)
                   
result = Runner.run_sync(
    agent,
    #"multiply number 5 into 10",
    #"who is the founder of pakistan?",
    #"what is today's weather in karachi?",
    "What is date today?",
    run_config=config
)
rich.print(result.new_items)
print(result.final_output)