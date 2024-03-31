from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import io
import os
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def gemini_response(input, pdf, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf[0], prompt])
    return response.text

def input_pdf(upload):
    if upload is not None:    
        images = pdf2image.convert_from_bytes(upload.read())
        first_page = images[0]
        
        img_arr_byte = io.BytesIO()
        first_page.save(img_arr_byte, format='JPEG')
        img_arr_byte = img_arr_byte.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_arr_byte).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded!")


st.title("TalenView")
st.header("Resume tracking System")
input_text = st.text_area("Job Description: ", key="input")
upload_file=st.file_uploader("Upload Resume: ", type=["pdf"])

if upload_file is not None:
    st.write("Resume uploaded successfully!")

button1 = st.button("Scan the Resume for detailed info")
button2 = st.button("Percentage Match")

prompt1 = """
As an experienced Technical HR professional or interviewer, your task is to thoroughly evaluate the provided resume in detail, 
providing a comprehensive review and analysis. Your evaluation should focus on the candidate's qualifications, experiences, 
skills, and overall suitability for the specified job role. Your review should be structured and detailed, covering both the 
positive aspects (strengths) and areas that may need improvement (weaknesses). Additionally, assess how well the resume aligns 
with the job description provided. Your analysis should be presented in a clear, organized, and visually appealing format, 
ensuring that all information is easily digestible for the reader.
Please ensure that your evaluation includes the following key points:
1. Candidate Overview:
    Begin by providing a brief summary of the candidate's background, including their education, work experience, and any 
    notable achievements or certifications.
2. Relevance to Job Description:
    Evaluate how well the candidate's skills, experiences, and qualifications align with the requirements outlined in the 
    job description. Highlight specific areas where the candidate demonstrates strong alignment and areas that may require 
    further development.
3. Strengths:
    Identify and discuss the candidate's key strengths, such as relevant work experience, technical skills, domain knowledge, 
    and any accomplishments or awards. Provide examples or evidence to support your assessment.
4. Weaknesses:
    Address any potential weaknesses or areas of improvement in the resume, such as gaps in employment, lack of specific 
    skills or experience, or inconsistencies in the presentation. Offer constructive feedback on how the candidate could 
    strengthen these areas.
5. Presentation and Formatting:
    Evaluate the overall presentation and formatting of the resume, including layout, clarity, and organization of information. 
    Assess whether the resume is easy to read and effectively highlights the candidate's qualifications.
6. Language and Communication:
    Assess the language used in the resume, including grammar, vocabulary, and tone. Evaluate whether the candidate effectively 
    communicates their achievements, responsibilities, and career objectives.
7. Additional Considerations:
    Consider any additional factors that may impact the candidate's suitability for the job, such as relevant hobbies or 
    extracurricular activities, industry-specific knowledge, or cultural fit.
8. Conclusion:
    Summarize your overall evaluation of the resume, highlighting the candidate's strengths and weaknesses, and providing 
    recommendations for improvement. Offer insights into whether you believe the candidate would be a suitable fit for the 
    specified job role based on their resume.    

Use bullet points, tables, or other visual elements to enhance readability and comprehension.
"""

prompt2 = """
You are tasked with simulating an advanced Applicant Tracking System (ATS) software designed to analyze resumes and job 
descriptions to determine the extent of alignment between the candidate's qualifications and the requirements of the job. 
Your goal is to provide a comprehensive percentage match between the content of the resume and the job description, while 
also offering insights into areas where the candidate's profile may fall short.
Please ensure that your analysis includes the following components:
1. Percentage Match Calculation:
    Utilize advanced algorithms to analyze the resume and job description, extracting relevant keywords, skills, experiences, 
    and qualifications. Calculate a percentage match score that reflects the degree of alignment between the two documents.
2. Explanation of Percentage Match:
    Provide a detailed breakdown of the factors contributing to the percentage match score. Explain which keywords, skills, 
    or qualifications were successfully matched between the resume and job description, and how they influenced the overall 
    score.
3. Identifying Missing Elements:
    Identify any key requirements or qualifications specified in the job description that are missing or inadequately 
    represented in the candidate's resume. Highlight specific areas where the candidate's profile may fall short and explain 
    how these deficiencies impact the overall percentage match.
4. Recommendations for Improvement:
    Offer constructive suggestions for the candidate on how they can enhance their resume to improve its alignment with the 
    job description. This may include adding relevant skills or experiences, providing more detailed descriptions of previous 
    roles, or highlighting achievements that demonstrate suitability for the position.
5. Contextual Analysis:
    Take into account the context of the job role and industry standards when assessing the suitability of the candidate's 
    profile. Consider factors such as industry-specific terminology, emerging trends, or specialized qualifications that may 
    impact the match score.
6. Quality Assurance:
    Ensure the accuracy and reliability of the analysis by cross-referencing the extracted information with reliable sources 
    and databases. Address any potential errors or discrepancies in the matching process and provide transparency on the 
    limitations of the ATS software.
7. Conclusion:
    Summarize the analysis by reaffirming the percentage match score and providing a final assessment of the candidate's 
    suitability for the job based on their resume. Offer insights into the strengths and weaknesses of the candidate's profile 
    and suggest next steps for further consideration.
"""

if button1:
    if upload_file is not None:
        pdf_content = input_pdf(upload_file)
        response = gemini_response(prompt1, pdf_content, input_text)
        st.subheader("Answer is: ")
        st.write(response)
    else:
        st.write("Something went wrong! Please re-upload resume")

elif button2:
    if upload_file is not None:
        pdf_content = input_pdf(upload_file)
        response = gemini_response(prompt2, pdf_content, input_text)
        st.subheader("Answer is: ")
        st.write(response)
    else:
        st.write("Something went wrong! Please re-upload resume")   
        