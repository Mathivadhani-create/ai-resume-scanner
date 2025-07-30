# AI Resume Scanner 🧠📄

An AI-powered resume scanner built using **Python** and **Streamlit**, designed to analyze uploaded resumes and suggest missing skills based on job roles.

## 🔍 Features

- 📄 Upload and scan resumes (PDF or DOCX)
- 🧠 AI-powered skill extraction
- 🚀 Smart suggestions based on job descriptions
- ⚙️ Built with Streamlit for easy UI
- 🔐 No API key required (local Gemini integration)

## 📦 Tech Stack

- Python
- Streamlit
- Google Gemini (Local integration)
- PDF parsing (PyPDF2 / pdfminer)
- Resume parsing (spaCy / custom logic)

## ⚙️ Installation

```bash
git clone https://github.com/Mathivadhani-create/ai-resume-scanner.git
cd ai-resume-scanner
pip install -r requirements.txt
streamlit run app.py
