from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile")

parser=JsonOutputParser()

template1=PromptTemplate(template="Give me the name , age and occupation of the person described in the following text: {text}{format_instructions}", input_variables=["text"], partial_variables={"format_instructions": parser.get_format_instructions()})

chain = template1 | model | parser
result=chain.invoke({"text":"John is a 30-year-old software engineer who loves hiking and playing the guitar."})
print(result)
