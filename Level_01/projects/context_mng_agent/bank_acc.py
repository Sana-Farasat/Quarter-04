import asyncio
from pydantic import BaseModel
import rich
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool

# CLASS FOR CONTEXT
class BankAccount(BaseModel):
    account_number: str | int
    customer_name: str
    account_balance: float
    account_type: str

# ACC_HOLDER PROFILE CONTEXT
bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Sana",
    account_balance=75500.50,
    account_type="Current"
)

@function_tool
def Bank_Info(wrapper : RunContextWrapper[BankAccount]):
    account= wrapper.context
    return(
        f"Here is your bank account info:\n"
        f"Account Number: {account.account_number}\n"
        f"Customer Name: {account.customer_name}\n"
        f"Balance: {account.account_balance}\n"
        f"Account Type: {account.account_type}"
    )

triage_agent = Agent(
    name= "Info Provider",
    instructions= "You are a triage agent. Your task is to provide bank account info by using bank info tool.Must use this tool for answering user query.",
    tools= [Bank_Info]
)

async def main():

    prompt1= "Give me complete my bank account information."
    prompt2=  "Give me my bank account ID."
    result = await Runner.run(
        triage_agent, 
        prompt1,
        run_config=config,
        context = bank_account #Local context
        )
    
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
