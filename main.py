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

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Crew
from agents import dataset_provider_agent
from tasks import dataset_provider
from crewai import Process

# Initialize FastAPI app
app = FastAPI()

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

# For testing purpose
@app.get("/")
def read_root():
    return {"message": "Welcome to the CrewAI Dataset Processor"}
