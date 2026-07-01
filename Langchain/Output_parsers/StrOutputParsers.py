from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile")

template1=PromptTemplate(template="Please detailed report on : {text}", input_variables=["text"])

template2=PromptTemplate(template="Please summarize the report in 3 to 4 small sentences : {report}", input_variables=["report"])

parser=StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result=chain.invoke({"text":"tell us about LangChain"})

print(result)
