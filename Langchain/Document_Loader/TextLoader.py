from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnablePassthrough,RunnableLambda, chain

load_dotenv()
    
model = ChatGroq(model_name="llama-3.3-70b-versatile")

document_loader = TextLoader(file_path="cricket.txt", encoding="utf-8")
document = document_loader.load()
prompt = PromptTemplate(template="Please summarize the document in 3 to 4 small sentences : {document}", input_variables=["document"])
parser = StrOutputParser()


# runnable_chain = RunnableSequence(prompt, model, parser)

content=RunnableParallel({
    "Summary":RunnableSequence(prompt, model, parser),
    "metadata":RunnableLambda(lambda x:x[0].metadata)
})

content_result=content.invoke(document)

print(content_result)