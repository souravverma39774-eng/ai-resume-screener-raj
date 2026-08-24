import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI Resume Screener - RAG")

st.title("📄 AI Resume Screener (RAG)")
st.write("Built by Sourav Verma - AI/ML Project")

job_desc = st.text_area("Paste Job Description here:")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file and job_desc:
    reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()
    
    st.subheader("Resume Preview:")
    st.write(resume_text[:1000])

    # Simple RAG logic (keyword matching)
    keywords = job_desc.lower().split()
    matched = [k for k in keywords if k in resume_text.lower()]
    
    score = len(matched) / len(keywords) * 100 if keywords else 0
    
    st.subheader(f"Match Score: {score:.2f}%")
    st.write(f"Matched keywords: {', '.join(matched[:20])}")
    
    if score > 60:
        st.success("✅ Good Match! Shortlist this resume.")
    else:
        st.warning("⚠️ Low Match")
