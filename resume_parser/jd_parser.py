def extract_jd_text(jd_path):
    with open(jd_path, "r", encoding="utf-8") as f:
        return f.read().lower()
