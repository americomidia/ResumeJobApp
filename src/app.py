import streamlit as st
from textExtraction import extract_text_from_pdf
from chain import get_resume_review

st.set_page_config(page_title="AI Resume Reviewer", layout="centered")

st.title("📄 AI Resume vs Job Description Reviewer")
st.subheader("Upload your documents to get instant feedback")

# Sidebar for API Key (Better security)
with st.sidebar:
    api_key = st.text_input("OpenAI API Key", type="password")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

with col2:
    jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")

if st.button("Analyze Resume"):
    if not api_key:
        st.error("Please provide an OpenAI API Key in the sidebar.")
    elif resume_file and jd_file:
        with st.spinner("Analyzing... this takes a few seconds."):
            # 1. Extract
            resume_text = extract_text_from_pdf(resume_file)
            jd_text = extract_text_from_pdf(jd_file)
            
            # 2. Process
            result = get_resume_review(resume_text, jd_text, api_key)
            
            # 3. Display
            st.divider()
            st.markdown("### 🎯 Review Results")
            st.write(result)
    else:
        st.warning("Please upload both documents first!")