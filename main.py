import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from agent_config import triage_runner

# 1. Cargar variables de entorno desde .env
load_dotenv()

# 2. Inicializar FastAPI
app = FastAPI(
    title="Research Assistant API",
    description="API para consultar a un agente inteligente de investigación y cálculo",
    version="1.0.0"
)

# 3. Modelo de entrada
class QueryRequest(BaseModel):
    question: str

# 4. Ruta raíz
@app.get("/")
async def root():
    return {"message": "¡Bienvenido al asistente de investigación!"}

# 5. Endpoint principal
@app.post("/ask")
async def ask_agent(request: QueryRequest):
    if not request.question:
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía.")
    try:
        # 👇 CORRECTO: runner.run es una función async
        response = await triage_runner.run(request.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error del agente: {str(e)}")

# 6. Ejecutar con uvicorn si se corre directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
