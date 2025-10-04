from langchain_gigachat.chat_models import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

# https://developers.sber.ru/docs/ru/gigachain/tutorials/llm-chain
print("Begin")

load_dotenv()  # Load variables from .env file

# exit()

model = GigaChat(
    #credentials=os.getenv('credentials'),
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    verify_ssl_certs=False,
)

messages = [
    #SystemMessage(content="Напиши сколько сейчас времени. Поздоровайся вежливо и коротко."),
    HumanMessage(content="Привет, какой посоветуешь курс?"),
]

result = model.invoke(messages)
print(result)

parser = StrOutputParser()
res = parser.invoke(result)
print(res)

#response = model.invoke([HumanMessage(content="Привет, какой посоветуешь курс?")])
#console = Console()
#console.print(response)


print("End")
