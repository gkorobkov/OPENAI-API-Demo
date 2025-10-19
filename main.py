from langchain_gigachat.chat_models import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from agents.agents import agent

print("Begin")


def chat(thread_id: str):
    """
    Main chat function.
    """
    config = {"configurable": {"thread_id": thread_id}}
    print("Welcome!")
    print("How can I help you? Type 'exit' to exit this chat.")
    
    while True:
        try:
            user_input = input("\n>>: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            response = agent.invoke({"messages": [("user", user_input.encode('utf-8', errors='replace').decode('utf-8'))]}, config=config)
            # response = agent.invoke({"messages": [("user", user_input)]}, {"configurable": {"thread_id": thread_id}})
            print("🤖 :", response["messages"][-1].content)
        
        except KeyboardInterrupt:
            print("\nExiting. Goodbye!")
            break
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    chat('AI_consultant')


print("End")
