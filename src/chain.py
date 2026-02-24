from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_resume_review(resume_text, jd_text, api_key):
    llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)
    
    # Your Hardcoded Prompt
    template = """
    You are an expert HR Recruiter. 
    Compare the following Resume against the Job Description (JD).
    
    JOB DESCRIPTION:
    {jd}
    
    RESUME:
    {resume}
    
    Provide a detailed review, missing keywords, and 3 specific suggestions to improve the resume.
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    
    return chain.invoke({"resume": resume_text, "jd": jd_text})