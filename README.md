# 🧠 Resume Analyzer (AI-Powered)

An AI-powered resume analyzer that compares a candidate’s resume PDF with a job description to return:
- ✅ A match percentage
- ❌ Missing keywords/skills
- 💡 Actionable improvement suggestions

Built using **Streamlit**, **LangChain**, **Google Gemini**, and **pdfplumber**.

---

## 🚀 Features

- 📄 Upload a resume in PDF format
- 📝 Paste any job description
- 🤖 Leverages Gemini via LangChain for intelligent comparison
- 🔍 Identifies missing keywords
- 📊 Calculates a match percentage
- 💡 Suggests ways to improve your resume

---

## 🧩 Tech Stack

- [Streamlit](https://streamlit.io/) – for building the UI
- [LangChain](https://www.langchain.com/) – for chaining LLM tasks
- [Google Gemini](https://ai.google.dev/) – LLM for resume analysis
- [pdfplumber](https://github.com/jsvine/pdfplumber) – for accurate text extraction from PDFs

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the app

```bash
streamlit run app.py
```
