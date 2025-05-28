# handles speech-to-text and text-to-speech

import whisper
import subprocess

model = whisper.load_model("base")

def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

def text_to_speech(text):
    subprocess.run(["say", text])
