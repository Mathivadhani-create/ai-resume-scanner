import streamlit as st
import fitz  # PyMuPDF
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Predefined list of job-relevant skills
job_skills = [
    "python", "data analysis", "machine learning", "deep learning",
    "sql", "excel", "statistics", "communication", "problem solving",
    "teamwork", "java", "c++", "javascript", "cloud computing", "aws",
    "azure", "tableau", "power bi", "nlp", "computer vision", "pandas",
    "numpy", "matplotlib", "seaborn", "tensorflow", "pytorch", "html",
    "css", "react", "git", "github"
]

# Extract text from uploaded resume (PDF)
def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

# Match skills using NLP
def match_skills(resume_text):
    doc = nlp(resume_text.lower())
    tokens = set([token.text for token in doc if not token.is_stop])
    matched = [skill for skill in job_skills if skill.lower() in tokens]
    score = int((len(matched) / len(job_skills)) * 100)
    return matched, score

# Streamlit UI
st.set_page_config(page_title="AI Resume Skill Matcher", page_icon="📄")
st.title("📄 Resume Scanner & Skill Matcher")
st.markdown("Upload your Resume (PDF format only)")

uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    matched_skills, score = match_skills(resume_text)

    st.subheader("📊 Resume Score")
    st.progress(score)
    st.success(f"Skill Match Score: {score}/100")

    st.subheader("✅ Matched Skills")
    st.write(matched_skills)

    if score < 60:
        st.warning("Consider adding more job-relevant skills.")
    else:
        st.success("Great! Your resume contains many important skills. 🎯")



