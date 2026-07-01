# from langchain_core.output_parsers import JsonOutputParser,StructuredOutputParser,ResponseSchema
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile")
schema=[
    ResponseSchema(name="Fact1", description="Fact 1 Of the Topic"),
    ResponseSchema(name="Fact2", description="Fact 2 Of the Topic"),
    ResponseSchema(name="Fact3", description="Fact 3 Of the Topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template1=PromptTemplate(template="Tell me about {text}{format_instructions}", input_variables=["text"], partial_variables={"format_instructions": parser.get_format_instructions()})

chain = template1 | model | parser

result=chain.invoke({"text":"LangChain"})

print(result)