from agent import main_agent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="### 🎉 Welcome to the Poet Agent! 📝\nGet ready to explore the world of poetry!"
        ).send()

@cl.on_message
async def main(message : cl.Message):
    user_input = message.content
    response = asyncio.run(main_agent(user_input))
    await cl.Message(
        content=(response)
    ).send()
    

