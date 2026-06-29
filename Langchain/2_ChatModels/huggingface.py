from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(
    llm=llm
)
result=model.invoke("who is MSDhoni?")
print(result.content)

