from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

result=search.invoke("ind vs eng 4th T20I Scorecard")

print(result)