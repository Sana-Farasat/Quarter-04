import asyncio
from pydantic import BaseModel
import rich
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool

# CLASS FOR CONTEXT
class LibraryBook(BaseModel):
    book_id: str
    book_title: str
    author_name: str
    is_available: bool

# LIBRARY BOOK CONTEXT
library_book = LibraryBook(
    book_id="BOOK-123",
    book_title="Python Programming",
    author_name="John Smith",
    is_available=True
)

@function_tool
def Library_Info(wrapper : RunContextWrapper[LibraryBook]):
    
    book = wrapper.context
    return {
        "book_id": book.book_id,
        "book_title": book.book_title,
        "author_name": book.author_name,
        "is_available": book.is_available
    }

triage_agent = Agent(
    name= "Info Provider",
    instructions= "You are a triage agent. Use the Library_Info tool to answer any questions about books. Always use the tool. Respond to user questions naturally but with accurate info.",
    tools= [Library_Info]
)

async def main():

    prompt1= "Who is the author of the book Python Programming?"
    prompt2=  "Is book available right now?"
    result = await Runner.run(
        triage_agent, 
        prompt1,
        run_config=config,
        context = library_book #Local context
        )
    
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
