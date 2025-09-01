from agents import Agent, ModelSettings

#____________________frequency_penalty_____________________
agent = Agent(
    name="Songwriter Bot",
    instructions="Write song lyrics.",
    model_settings=ModelSettings(
        temperature=1.0,
        frequency_penalty=1.5  # avoid repeating same words
    )
)

#____________________presence_penalty_____________________
agent = Agent(
    name="Brainstorm Bot",
    instructions="Give me startup ideas.",
    model_settings=ModelSettings(
        presence_penalty=1.2  # push model to bring NEW ideas
    )
)

#_______________________truncate_________________________
agent = Agent(
    name="Transcript Analyzer",
    instructions="Summarize large transcripts.",
    model_settings=ModelSettings(
        truncation="auto"   # automatically cut if input too long
    )
)