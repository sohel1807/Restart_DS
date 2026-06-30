from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(
    model_name="llama-3.3-70b-versatile")

messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Who won the world series in 2020?")]


result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)