import streamlit as st
import requests

st.title("🎙️ Multi-Agent Finance Assistant")

audio_file = st.file_uploader("Upload your voice (.wav)", type=["wav"])
if audio_file:
    st.audio(audio_file)
    if st.button("Ask"):
        files = {"audio": audio_file}
        try:
            response = requests.post("https://finance-api-k065.onrender.com/ask", files=files, timeout=60)
            result = response.json()
            st.success("💬 Response: " + result["response"])
        except requests.exceptions.RequestException as e:
            st.error(f"🚨 Request failed: {str(e)}")
