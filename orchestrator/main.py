# FastAPI backend

#from fastapi import FastAPI, UploadFile
from orchestrator.orchestrator import process_query

app = FastAPI()

@app.post("/ask")
async def ask(audio: UploadFile):
    file_path = "input.wav"
    with open(file_path, "wb") as f:
        f.write(await audio.read())
    result = process_query(file_path)
    return {"response": result}
