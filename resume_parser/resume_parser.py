import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    return text.lower()

def extract_skills(text):
    SKILLS = [
        "python", "java", "sql", "machine learning", "deep learning",
        "streamlit", "fastapi", "flask", "nlp", "pandas", "numpy"
    ]
    found = []
    for skill in SKILLS:
        if re.search(rf"\b{skill}\b", text):
            found.append(skill)
    return list(set(found))
