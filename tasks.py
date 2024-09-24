from crewai import Task
from agents import dataset_provider_agent
from tools import tool

dataset_provider=Task(
# description="""
#     Your Task is to provide link of dataset of {input}
#     """,
#     expected_output="""
#     The expected output would be dataset links from google
#     """,
    description="""
    Your Task is to provide top 5 research paper and patent links based on provided {input}
    """,
    expected_output="""
    The expected output would be patents and research paper links of given idea
    """,
    tools=[tool],
    agent=dataset_provider_agent,
)
