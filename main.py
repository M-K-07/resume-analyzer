import streamlit as st
from analyzer import analyze_resume

st.secrets("GOOGLE_API_KEY")  
st.title("Resume Analyzer 📝")
st.write("This application analyzes the match between a candidate's resume and a job description.")

uploaded_file = st.file_uploader("Upload Resume PDF: ", type="pdf")
job_description = st.text_area("Job Description: ",height=200, placeholder="Enter the job description here...")

if st.button("Analyze", type="primary"):
    if uploaded_file and job_description:
        
        with st.spinner("Analyzing your resume against the job description..."):
            
            response = analyze_resume(uploaded_file, job_description)

        st.header("📊 Analysis Results")

        # Display match percentage with a progress bar
        match_percentage = int(response["match_percentage"])
        st.subheader(f"Overall Match: {match_percentage}%")
        st.progress(match_percentage)

        st.subheader("⚠️ Missing Keywords")
        for keyword in response["missing_keywords"]:
            st.markdown(f"- {keyword.capitalize()}")

        st.subheader("💡 Improvement Suggestions")
        with st.expander("Click to see suggestions", expanded=False):
            for suggestion in response["improvement_suggestions"]:
                    st.markdown(f"- {suggestion.capitalize()}")
    else:
        st.warning("Please upload a resume and provide a job description.")


