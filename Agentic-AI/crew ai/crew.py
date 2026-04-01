import os
from crewai import Agent, Task, Crew

os.environ["OPENAI_API_KEY"]

info_agent= Agent(
    role= "Information agent"
    goal= "Gather information about a certain topic"
    backstory= "This agent is responsible for researching and collecting relevant information on a given topic. It will use various sources to gather data and insights that can be used by other agents in the crew."
)

task1= Task(
    description = "Research the history of artificial intelligence"
    expected_output= "give a quick summary into 5 bullet points"
)

crew= crew(
    Agents= [info_agent]
    Tasks= [task1]
    verbose= 2
)

result= crew.kickoff()
print(result)