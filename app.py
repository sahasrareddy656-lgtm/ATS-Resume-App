import streamlit as st
import os
from resume_parser.resume_parser import extract_text_from_pdf, extract_skills
from resume_parser.jd_parser import extract_jd_text
from scorer.ats_scorer import calculate_ats_score

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="ATS Resume Analyzer", layout="centered")

st.title("📄 ATS Resume Analyzer")
st.write("Upload your resume and paste the Job Description to get ATS score")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text_input = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if uploaded_resume and jd_text_input.strip():
        resume_path = os.path.join(BASE_DIR, "data", "temp_resume.pdf")

        with open(resume_path, "wb") as f:
            f.write(uploaded_resume.read())

        resume_text = extract_text_from_pdf(resume_path)
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text_input.lower())

        score, matched, missing = calculate_ats_score(resume_skills, jd_skills)

        st.subheader("📊 ATS Result")
        st.success(f"ATS Score: {round(score, 2)}%")

        st.write("✅ Matched Skills:", list(matched))
        st.write("❌ Missing Skills:", list(missing))
    else:
        st.error("Please upload resume and paste job description.")
