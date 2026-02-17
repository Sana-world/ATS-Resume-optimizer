import streamlit as st
import requests

st.title("AI Resume Builder & ATS Optimizer")

job_desc = st.text_area("Paste Job Description")
resume = st.file_uploader("Upload Resume (PDF or DOCX)")

if st.button("Optimize Resume"):
    if resume and job_desc:
        response = requests.post(
            "http://127.0.0.1:8000/process/",
            files={"file": resume},
            data={"job_desc": job_desc}
        )

        data = response.json()
        st.success("Optimization Complete!")
        st.write("Original ATS Score:", data["original_score"])
        st.write("Enhanced ATS Score:", data["enhanced_score"])
