# AI Tool Usage Log

## Language Agent
- Tool: Hugging Face Inference API
- Model: google/flan-t5-base
- Prompt: Finance brief generation with context
- Output type: Structured summary

## Voice Agent
- Tool: OpenAI Whisper
- Task: Transcription from `.wav` audio
- Model: base
- Parameters: default

## Code Generation
- Used ChatGPT to design agent structure, FastAPI endpoints, and Streamlit UI
- Prompt examples: “Give me a language agent that summarizes risk data and earnings”

## Future Improvements
- Add streaming audio input
- Use GPU-hosted models for faster LLM response
