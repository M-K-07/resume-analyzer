from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pdfplumber
import streamlit as st
import json

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return pdf.pages[0].extract_text() 

llm= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.1,
    google_api_key=GOOGLE_API_KEY)

prompt= PromptTemplate.from_template(
    """
    You are an expert HR assistant specializing in technical recruitment. Your task is to evaluate a candidate's resume against a given job description.

    Instructions:
    1. Analyze how well the candidate's resume aligns with the job description.
    2. Estimate a match percentage between 0 and 100 based on keyword overlap, relevant skills, and experience.
    3. Identify and return any important skills or keywords missing from the resume that are present in the job description.
    4. Provide suggestions for improving the resume to better match the job description.

    RESUME:
    {resume}

    JOB DESCRIPTION:
    {jd}

    Respond ONLY in the following JSON format without preamble:
    {{
    "match_percentage": <integer between 0 and 100>,
    "missing_keywords": [<list of missing skills/keywords as strings>],
    "improvement_suggestions": [<list of suggestions for improving the resume as strings>]
    }}
    """
)

    
def analyze_resume(pdf_path, jd):
    resume = extract_text_from_pdf(pdf_path)
    chain= prompt | llm 
    response = chain.invoke({"resume": resume, "jd": jd})
    return  json.loads(response.content.replace("```json", "").replace("```", "").strip())





    