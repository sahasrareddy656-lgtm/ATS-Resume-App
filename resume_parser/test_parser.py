import os
from resume_parser.resume_parser import extract_text_from_pdf, extract_skills
from resume_parser.jd_parser import extract_jd_text
from scorer.ats_scorer import calculate_ats_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    resume_path = os.path.join(BASE_DIR, "data", "sample_resume.pdf")
    jd_path = os.path.join(BASE_DIR, "data", "sample_jd.txt")

    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_jd_text(jd_path)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    score, matched, missing = calculate_ats_score(resume_skills, jd_skills)

    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)
    print("Matched Skills:", matched)
    print("Missing Skills:", missing)
    print("ATS Score:", round(score, 2))

if __name__ == "__main__":
    main()
