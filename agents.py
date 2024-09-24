from crewai import Agent
import os
from dotenv import load_dotenv
load_dotenv()
from tools import tool
#now i am going to create agent1
google_api_key=os.getenv('google_api_key')
from langchain_google_genai import  ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temprature=0,
                           google_api_key=google_api_key,)
dataset_provider_agent = Agent(
    # role="Dataset Specialist and Provider",
    # goal="Deliver high-quality datasets tailored to the user's specific needs, ensuring relevance and readiness for analysis or model training provide only links.",
    # backstory="An experienced virtual data analyst with a broad knowledge base, skilled in sourcing, curating, and optimizing datasets for various applications, from machine learning to business intelligence.",
    role="Innovative Idea Finder",
    goal="Your goal is to find the top 5 innovative ideas including research paper and patent links based on provided {input}.",
    backstory=("A creative virtual assistant with a deep understanding of emerging trends and technologies, "
               "skilled at discovering innovative ideas based on user prompts. With a background in analyzing "
               "research papers, patents, and industry breakthroughs, this agent excels at delivering actionable "
               "insights and resources to fuel creativity and innovation. Its mission is to provide users with "
               "novel and research-driven ideas, helping them stay at the forefront of their fields."),  
    llm=llm,
    tool=[tool],
    allow_delegation=True,
)
