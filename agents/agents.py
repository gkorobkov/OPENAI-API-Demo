import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from utils.prompts import system_prompt 

load_dotenv()  # Load variables from .env file

print("agent.py __name__")
print(__name__ )


from langchain_core.tools import Tool
from agents.tools import get_all_course_names, get_most_similar_course, register_for_course
tools = [get_most_similar_course]  

tools = [
    Tool(
        name="get_all_course_names",
        func=get_all_course_names,
        description="Get all course names."
    ),
    Tool(
        name="get_most_similar_course",
        func=get_most_similar_course,
        description="Get most similar course."
    )
]

model = GigaChat(
    # credentials=os.getenv("OPENAI_CREDENTIALS"),
    scope=os.getenv("OPENAI_SCOPE"),
    model=os.getenv("OPENAI_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    verify_ssl_certs=False,
    profanity_check=False,
    timeout=600,
    top_p=0.3,
    temperature=0.1,
    max_tokens=6000
)


agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=system_prompt,  
    checkpointer=MemorySaver()  
)






