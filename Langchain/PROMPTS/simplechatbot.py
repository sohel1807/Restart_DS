from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

modal=ChatGroq(
    model_name="llama-3.3-70b-versatile")
 
chat_mesaages=[
    SystemMessage(content="You are Mental Wellness Assistant Adaptive Question asker . Always ask Questions in adaptive way to understand the user mental Health.Dont ask boaring questions and direct questions and ask simpler way . Just ask question Whats Problem and how his mental health with limited range of question sentences."), 
  ]

while True:
    user_input=input("You: ")
    chat_mesaages.append(HumanMessage(content=user_input))

    if user_input.lower()=="exit":
        print("Exiting the chat...",chat_mesaages)
        break
    else:
        result=modal.invoke(chat_mesaages)
        chat_mesaages.append(AIMessage(content=result.content))
        print("AI: ",result.content) 