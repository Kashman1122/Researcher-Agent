# from crewai import Task
# from agents import dataset_provider_agent
# from tools import tool

# dataset_provider=Task(
# # description="""
# #     Your Task is to provide link of dataset of {input}
# #     """,
# #     expected_output="""
# #     The expected output would be dataset links from google
# #     """,
#     description="""
#     Your Task is to provide top 5 research paper and patent links based on provided {input}
#     """,
#     expected_output="""
#     The expected output would be patents and research paper links of given idea
#     """,
#     tools=[tool],
#     agent=dataset_provider_agent,
# )



from crewai import Task
from agents import dataset_provider_agent
from tools import tool

dataset_provider = Task(
    description="""
    Your Task is to provide the top 50 research paper and patent links based on the provided {input}.
    You should filter the results based on the following criteria:
    - **Title**: Match the user's input with the title of the patent or paper.
    - **Abstract**: Match the user's input with the abstract of the patent or paper.
    - **Claims**: Match the user's input with the claims of the patent or paper.

    The result should include only those patents or papers that match these filters.
    """,
    expected_output="""
    The expected output would be a list of top 5 relevant patents and research paper links that match the user's input
    in **title**, **abstract**, or **claims**.
    """,
    tools=[tool],
    agent=dataset_provider_agent,
)
