from fastapi import FastAPI, UploadFile, File, HTTPException
from orchestrator.orchestrator import process_query
import shutil
import os
import requests

app = FastAPI()

# Securely get Hugging Face API token from environment variable
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
if not HF_API_TOKEN:
    raise RuntimeError("Environment variable HF_API_TOKEN is not set")

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"  # Or any other model

@app.post("/ask")
async def ask(audio: UploadFile = File(...)):
    try:
        # Save uploaded audio to a temporary file
        with open("temp.wav", "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        # Step 1: Process audio to get text
        text = process_query("temp.wav")

        # Step 2: Send the text to Hugging Face for inference
        response = requests.post(HF_API_URL, headers=headers, json={"inputs": text})

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        hf_result = response.json()

        # Return both original and model output
        return {
            "original_text": text,
            "huggingface_response": hf_result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
