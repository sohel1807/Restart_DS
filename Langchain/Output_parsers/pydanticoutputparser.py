from langchain_core.output_parsers import JsonOutputParser ,PydanticOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel ,Field

load_dotenv()

class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    occupation: str = Field(..., description="The occupation of the person")


parser = PydanticOutputParser(pydantic_object=Person)

template1=PromptTemplate(template="Give me the name , age and occupation of the person described in the following text: {text}{format_instructions}", input_variables=["text"], partial_variables={"format_instructions": parser.get_format_instructions()})

model = ChatGroq(model_name="llama-3.3-70b-versatile")

chain = template1 | model | parser

result=chain.invoke({"text":"John is a 15-year-old software engineer who loves hiking and playing the guitar."})
print(result)