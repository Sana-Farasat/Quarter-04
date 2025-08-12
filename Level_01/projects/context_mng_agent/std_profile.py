import asyncio
from pydantic import BaseModel
import rich
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool

# CLASS FOR CONTEXT
class StudentProfile(BaseModel):
    student_id: str
    student_name: str
    current_semester: int
    total_courses: int

# STUDENT PROFILE CONTEXT
student = StudentProfile(
    student_id="STU-456",
    student_name="Areesha",
    current_semester=4,
    total_courses=5
)

@function_tool
def Student_Info(wrapper : RunContextWrapper[StudentProfile]):
    
    student= wrapper.context
    return(
        f"Here is your bank account info:\n"
        f"Student ID: {student.student_id}\n"
        f"Student Name: {student.student_name}\n"
        f"Current Semester: {student.current_semester}\n"
        f"Total Courses: {student.total_courses}"
    )

orchestrating_agent = Agent(
    name= "Info Provider",
    instructions= "You are a triage agent. Your task is to provide student related details by using student info tool.Must use this tool and answer in a structured way.",
    tools= [Student_Info]
)

async def main():
    
    prompt1= "What is the name of student?"
    prompt2=  "Tell me my student ID."
    prompt3= "What's current semester of students?"
    prompt4= "Give me complete student details."
    result = await Runner.run(
        orchestrating_agent , 
        prompt4,
        run_config=config,
        context = student #Local context
        )
    
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
