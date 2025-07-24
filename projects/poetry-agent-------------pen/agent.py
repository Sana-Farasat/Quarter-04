from agents import Agent , Runner , OpenAIChatCompletionsModel , set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
set_tracing_disabled(True)

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

# Lyrics Poetry
web_developer = Agent(
    name= "Web Developer Expert",
    instructions= "Build responsive and performant websites using modern frameworks.",
    model= model,
    handoff_description="handoff to web developer if the task related to the web development."
)

# App Developer
app_developer = Agent(
    name= "App Developer Expert",
    instructions= "Build mobile applications using modern frameworks.",
    model= model,
    handoff_description="handoff to app developer if the task related to the app development."
)

# Graphic Designer
graphic_designer = Agent(
    name= "Graphic Designer Expert",
    instructions= "Design visually appealing, responsive, and performant user interfaces using modern design tools and frameworks.",
    model= model,
    handoff_description= "Handoff to the graphic designer if the task involves visual design, UI/UX, or front-end aesthetics."
)

# Marketing Agent
marketing = Agent(
    name="Marketing Expert Agent",
    instructions="Create and execute marketing strategies for product launch.",
    model=model,
    handoff_description="Handoff to the marketing agent if the task related to the marketing."
)

async def my_agent(user_input):
    manager = Agent(
        name= "Manager",
        instructions= "You will chat with the user and delegate tasks to speciliazed agent based on their request.",
        model= model,
        handoffs= [web_developer, app_developer, graphic_designer, marketing]
    )

    response = await Runner.run(
        manager,
        input= user_input
    )

    return response.final_output
    