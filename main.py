from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from agent_config import triage_agent
from agents import Runner  

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="Research Assistant API",
    description="API to query an intelligent research and calculation agent",
    version="1.0.0"
)

# Input model
class QueryRequest(BaseModel):
    question: str

# Root path
@app.get("/")
async def root():
    return {"message": "Welcome to the research assistant!"}

# Main endpoint
@app.post("/ask")
async def ask_agent(request: QueryRequest):
    if not request.question:
        raise HTTPException(status_code=400, detail="The question cannot be empty.")
    try:
        result = await Runner.run(triage_agent, request.question)
        return {"response": result.final_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")

# Ejecutar localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
