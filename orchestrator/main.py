from fastapi import FastAPI, UploadFile, File
from orchestrator.orchestrator import process_query
import shutil

app = FastAPI()

@app.post("/ask")
async def ask(audio: UploadFile = File(...)):
    with open("temp.wav", "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
    response = process_query("temp.wav")
    return {"response": response}
