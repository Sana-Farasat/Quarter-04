from agents import Agent, AgentHooks, RunHooks, Runner, trace, function_tool
from connection import config
import asyncio
from dotenv import load_dotenv
import logging
import rich 

#Saving logs into file
logging.basicConfig(filename='agent_logs.txt', level=logging.INFO) 

load_dotenv()

# ===================== HOOKS CLASS =====================

class MyAgentHooks(AgentHooks):

    async def on_start(self, ctx, agent):
        rich.print(f"\n[AGENT] {agent.name} started")

    async def on_end(self, ctx, agent, output):
        rich.print(f"\n[AGENT] {agent.name} ended with output: {output}")

    async def on_tool_start(self, ctx, agent, tool, input):
        rich.print(f"\n[AGENT] Tool {tool.name} started with this {input}")

    async def on_tool_end(self, ctx, agent, tool, result):
        rich.print(f"\n[AGENT] Tool {tool.name} ended with result: {result}")

    async def on_handoff(self, ctx, from_agent, to_agent):
        rich.print(f"\n[AGENT] Handoff from {from_agent.name} to {to_agent.name}")

class MyRunHooks(RunHooks):

    async def on_agent_start(self, ctx, agent):
        rich.print(f"\n[RUN] Agent {agent.name} started")

    async def on_agent_end(self, ctx, agent, output):
        rich.print(f"\n[RUN] Agent {agent.name} ended with output: {output}")

    async def on_tool_start(self, ctx, agent, tool):
        rich.print(f"\n[RUN] Agent {agent.name} started tool {tool.name}")

    async def on_tool_end(self, ctx, agent, tool, result):
        rich.print(f"\n[RUN] Agent {agent.name} finished tool {tool.name} with result: {result}")

    async def on_handoff(self, ctx, from_agent, to_agent):
        rich.print(f"\n[RUN] Handoff from {from_agent.name} to {to_agent.name}")

# ===================== Function Tools =====================

@function_tool
def check_pizza_price(pizza_name: str) -> str:
    """Check the price of a pizza."""
    pizza_menu = {
        "Margherita": 12,
        "Pepperoni": 15,
        "Vegetarian": 14
    }
    price = pizza_menu.get(pizza_name, None)
    if price:
        return f"The price of {pizza_name} pizza is ${price}."
    else:
        return "Sorry, we don't have that pizza on the menu."


@function_tool
def order_pizza(pizza_name: str, quantity: int) -> str:
    """Order a pizza and get confirmation with total bill."""
    pizza_menu = {
        "Margherita": 12,
        "Pepperoni": 15,
        "Vegetarian": 14
    }
    if pizza_name not in pizza_menu:
        return "Sorry, we don't have that pizza on the menu."
    
    total = pizza_menu[pizza_name] * quantity
    return f"Your order for {quantity} {pizza_name} pizza(s) has been placed. Total = ${total}."


# ===================== Agents =====================

waiter_agent = Agent(
    name="Waiter Agent",
    instructions="""
    You are a waiter agent and provide a list of pizzas to the customer.
        ## Your pizza list:
        1. Margherita - $12
        2. Pepperoni - $15  
        3. Vegetarian - $14

    You can also use tools to check pizza price and place an order.
    """,
    tools=[check_pizza_price, order_pizza]
)

welcome_Agent = Agent(
    name="Welcome Agent",
    instructions=f"""
        You are a Welcome agent in a Pizza Restaurant. Your task is to:
        1. Welcome user politely.
        2. Ask them to have a seat.
        3. Handoff to the waiter agent to show them the menu.
        """,
    handoffs= [waiter_agent],
    handoff_description="You need to handoff to waiter agent after welcome message appears",
    hooks= MyAgentHooks()
)


# ===================== Main Executer =====================

async def main():
    # while True:
    #     msg = input("\n Enter your message: ")

        with trace("Quiz Practice"):
            result = await Runner.run(welcome_Agent, 
                                      "i want peppori pizza", 
                                      run_config=config,
                                      hooks= MyRunHooks()
                                      )
            print("\n" + result.last_agent.name + "\n")
            print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
