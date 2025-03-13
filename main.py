# from crewai import Crew
# from agents import dataset_provider_agent
# from tasks import dataset_provider
# from crewai import Process

# crew=Crew(
#     agents=[dataset_provider_agent],
#     tasks=[dataset_provider],
#     process=Process.sequential,
# )
# result = crew.kickoff(inputs={'input': 'dog dataset in yolo format'})
# print(result)

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from crewai import Crew
# from agents import dataset_provider_agent
# from tasks import dataset_provider
# from crewai import Process

# # Initialize FastAPI app
# app = FastAPI()

# # Initialize CrewAI configuration
# crew = Crew(
#     agents=[dataset_provider_agent],
#     tasks=[dataset_provider],
#     process=Process.sequential,
# )

# # Pydantic model for input data validation
# class DatasetRequest(BaseModel):
#     input: str

# @app.post("/process_dataset/")
# def process_dataset(request: DatasetRequest):
#     try:
#         # Kick off the process with user input
#         result = crew.kickoff(inputs={'input': request.input})
#         return {"result": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # For testing purpose
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the CrewAI Dataset Processor"}

from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from crewai import Crew
from agents import dataset_provider_agent
from tasks import dataset_provider
from crewai import Process
import httpx
import asyncio
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://daminiai.pythonanywhere.com/index/","*"],  # Change * to allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Initialize CrewAI configuration
crew = Crew(
    agents=[dataset_provider_agent],
    tasks=[dataset_provider],
    process=Process.sequential,
)

# Pydantic model for input data validation
class DatasetRequest(BaseModel):
    input: str

@app.post("/process_dataset/")
def process_dataset(request: DatasetRequest):
    try:
        # Kick off the process with user input
        result = crew.kickoff(inputs={'input': request.input})
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the CrewAI Dataset Processor"}

# Function to keep API alive
async def keep_api_alive():
    url = "https://researcher-agent-df3x.onrender.com/"
    while True:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                print(f"Keep-alive ping: {response.status_code}")
        except Exception as e:
            print(f"Error pinging API: {e}")
        await asyncio.sleep(10)  # Ping every 10 seconds

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(keep_api_alive())  # Start keep-alive task

