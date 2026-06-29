from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.3,
    max_completion_tokens=100,
)

result=llm.invoke("who is the president of the united states?")
print(result.content)
