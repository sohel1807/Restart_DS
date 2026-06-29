from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

st.header("LangChain Chat with HuggingFace Models")

# llm = ChatGroq(
#     model_name="llama-3.3-70b-versatile",
#     temperature=0.3,
#     max_completion_tokens=100,
# )

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(
    llm=llm
)
user_input = st.text_input("Enter your text here:")

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)
