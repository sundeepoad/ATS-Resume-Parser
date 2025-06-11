# app.py
import streamlit as st
from resume_parser import extract_text_from_docx
from matcher import calculate_match_score

st.title("🔍 Job vs Resume Matcher")

# Upload resume
resume_file = st.file_uploader("Upload your resume (.docx)", type=["docx"])

# Paste job description
job_description = st.text_area("Paste the job description")

# On button click
if st.button("Match Job with Resume"):
    if resume_file and job_description.strip():
        resume_text = extract_text_from_docx(resume_file)

       
        result = calculate_match_score(resume_text, job_description)

        st.metric(label="📊 Match Score", value=f"{result['score']}%")
        st.subheader("✅ Matched Skills:")
        st.write(result["matched"])
        st.subheader("⚠️ Missing Skills:")
        st.write(result["missing"])
    else:
        st.warning("Please upload your resume and paste a job description.")
