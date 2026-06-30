from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

chat_prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant."), 
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")])

model=ChatGroq(model_name="llama-3.3-70b-versatile")

chat_history=[]

with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

prompt=chat_prompt.invoke({"chat_history":chat_history,"query":"where is my refund"})
result=model.invoke(prompt)
print(result.content)