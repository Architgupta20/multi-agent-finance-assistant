import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def generate_market_brief(risk_data, earnings_data):
    prompt = (
        f"Summarize this for a finance executive:\n"
        f"Today, your {risk_data['region']} {risk_data['sector']} allocation is {risk_data['today']}% of AUM, "
        f"up from {risk_data['yesterday']}% yesterday. "
    )
    for company, surprise in earnings_data.items():
        prompt += f"{company} {'beat' if '+' in surprise else 'missed'} earnings by {surprise}. "
    prompt += "Overall sentiment is neutral with a cautionary tilt due to rising yields."

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
            headers={"Authorization": f"Bearer {HF_API_KEY}"},
            json={"inputs": prompt}
        )
        response.raise_for_status()  # Raise error if HTTP request failed

        result = response.json()

        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]
        elif isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return f"⚠️ Unexpected API response: {result}"

    except Exception as e:
        return f"❌ Error parsing Hugging Face response: {str(e)}\nRaw content: {response.text}"
