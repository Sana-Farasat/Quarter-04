import asyncio
from pydantic import BaseModel
import rich
from connection import config
from agents import Agent, RunContextWrapper, Runner

class User(BaseModel):
    user : str
    user_type : str 
    
patient = User(user= "Fariha", user_type= "Patient")
medical_student = User(user= "Aiman", user_type= "Medical Student")
doctor = User(user= "Rameen", user_type= "Doctor")

def my_dynamic_instructions(ctx: RunContextWrapper[User], agent: Agent)->str:

    if ctx.context.user_type == "Patient":
        return"""
    Use simple, non-technical language. Explain medical terms in everyday words. Be empathetic and reassuring.
    """
    elif ctx.context.user_type == "Medical Student":
        return"""
    Use moderate medical terminology with explanations. Include learning opportunities.
    """
    elif ctx.context.user_type == "Doctor":
        return"""
    Use full medical terminology, abbreviations, and clinical language. Be concise and professional.
    """

medical_consultation_agent = Agent(
    name= "Medical Consultation Agent",
    instructions= my_dynamic_instructions
)

async def main():

    prompt= "What is the low power medicine for headache?"
    result = await Runner.run(
        medical_consultation_agent , 
        prompt,
        run_config=config,
        context= medical_student
        )
    
    rich.print(f"\n[bold yellow]Agent Output: {result.final_output} [/bold yellow]")

if __name__ == "__main__":
    asyncio.run(main())
