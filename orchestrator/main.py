from fastapi import FastAPI, UploadFile
from orchestrator.orchestrator import process_query

app = FastAPI()

@app.post("/ask")
async def ask(audio: UploadFile):
    return {"response": process_query(audio)}
