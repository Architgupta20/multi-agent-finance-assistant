# Streamlit frontend

import streamlit as st
import requests

st.title("Finance Assistant")

audio_file = st.file_uploader("Upload your voice (.wav)", type=["wav"])

if audio_file:
    st.audio(audio_file)
    if st.button("Ask"):
        files = {"audio": audio_file}
        response = requests.post("http://localhost:8000/ask", files=files)
        st.success("Response: " + response.json()["response"])
