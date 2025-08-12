from agents import Agent , Runner , OpenAIChatCompletionsModel, trace
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
#set_tracing_disabled(True)

openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client= provider
)

# config = RunConfig(
#     model=model,
#     model_provider=provider,
#     tracing_disabled=True
# )

# Lyrics Poeter
lyrics_poeter = Agent(
    name= "Lyrics Poeter",
    instructions= "You are a lyrics poeter , you will analyze lyrical things or stanzas.",
    model= model,
    handoff_description="Handoff to lyrics poeter if the poem/stanzas/things related to the lyrics."
)

# Narrative Poeter
narrative_poeter = Agent(
    name= "Narrative Poeter",
    instructions= "You are a narrative poeter , you will analyze narrative things or stanzas.",
    model= model,
    handoff_description="Handoff to narrative poeter if the poem/stanzas/things related to the narrative."
)

# Dramatic Poeter
dramatic_poeter = Agent(
    name= "Dramatic Poeter",
    instructions= "You are a dramatic poeter , you will analyze dramatic things or stanzas.",
    model= model,
    handoff_description= "Handoff to dramatic poeter if the poem/stanzas/things related to the dramatic."
)

async def main_agent(user_input):
    with trace("Poet Agent"):
      orchestrator_agent = Agent(
        name= "Manager",
        instructions= "You will chat with the user and delegate tasks to speciliazed agent based on their request.",
        model= model,
        handoffs= [lyrics_poeter, narrative_poeter, dramatic_poeter]
    )

      response = await Runner.run(
        orchestrator_agent,
        input= user_input
    )

      return response.final_output
    