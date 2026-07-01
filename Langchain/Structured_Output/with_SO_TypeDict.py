from langchain_groq import ChatGroq
from typing import TypedDict,Annotated
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile")

class MyTypeDict(TypedDict):
    summary:Annotated[str, "A brief summary of the text"]
    sentiment:Annotated[str, "The sentiment of the text positive or negative or neutral"]
    sentiment_score:Annotated[float, "A score representing the intensity of the sentiment"]

structerd_model=model.with_structured_output(MyTypeDict)

result=structerd_model.invoke("""Please, don't stop this GenAI series or make any of the videos course-oriented or members-only content I request you. 
                              Let alone this Langchain playlist is so good and helpful. It is difficult to keep up and make content consistently but 
                              I request you to keep posting the videos with the same effort and quality. 
Your channel is a gem and you are making a huge difference already so you have all the support you need please continue and keep pushing.""")

print(result["summary"])
print(result["sentiment"])
print(result["sentiment_score"])