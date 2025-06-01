# pip install openai-agents 
# pip install python-dotenv 

import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Configure Gemini
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

# Translator Agent
translator = Agent(
    name='Translator Agent',
    instructions="You are a translator agent. Translate text from one language to another based on user input."
)

# Execute the Agent
response = Runner.run_sync(
    translator,
    input = "Aap kese hen? Translate it into english.",
    run_config = config
)

print(response.final_output)

