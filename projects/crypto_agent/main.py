import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool
import requests

# ____________________Load environment variables_________________________

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# __________________________Configure Gemini_____________________________

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# _____________________Binance Symbol Format____________________________

"""
Here is Binance Symbol Format:
_ BTC to USD → BTCUSDT
_ ETH to USD → ETHUSDT
_ BTC to ETH → BTCETH
"""
# _________________Function Calling / Tool Calling__________________

@function_tool
def get_crypto_rates(symbol : str) -> str:

    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"

    response= requests.get(url)

    if response.status_code == 200:
        price = response.json()["price"]
        return f"The current rate of {symbol.upper()} is ${price}."
    else:
        "Invalid symbol or data fetched failed."

# _________________________Crypto Agent______________________________

crypto_agent = Agent(
    name='Crypto Agent',
    instructions="You are a crypto agent. Provide real time cryptocurrency rates by using the Binance API or URL",
    tools= [get_crypto_rates]
)

# ________________________Execute the Agent___________________________

response = Runner.run_sync(
    starting_agent= crypto_agent,
    input = """Whats the current rate of BTCUSDT?
               Whats the current rate of ETHUSDT?
               Whats the current rate of BTCETH?""",
    run_config = config
)

# _________________________ Final Output________________________________

print(response.final_output)

