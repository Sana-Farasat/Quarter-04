from agents import Agent, Runner, ModelSettings
from connection import config

agent = Agent(
    name="Customer Support Bot",
    instructions="You are a helpful assistant for an online shopping store.",
    model_settings=ModelSettings(
        temperature= 0.5,        # balanced creativity
        max_output_tokens= 300,  # avoid very long answers
        top_p= 0.9,              # balanced randomness
        top_k= 50,               # sirf top 50 words consider karega
        stop_sequences= ["User:"], # stop when next user input starts
        response_format= {"type": "text"}  # normal text (could also be JSON)
    )
)

result = Runner.run_sync(
    agent,
    "Where is my order #12345?",
    run_config=config
)

print(result.final_output)
