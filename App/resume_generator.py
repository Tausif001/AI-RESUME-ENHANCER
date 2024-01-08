import streamlit as st
import pdfkit
import base64

# Specify the path to wkhtmltopdf executable
pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')


# Function to create the PDF resume
def create_pdf(name, profession, phone, email, skills, experience, education, awards):
    pdf_content = f'''
     <style>
body {{
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}}
.header {{
    text-align: center;
    padding: 20px;
    background-color: #f4f4f4;
}}
.contact-info {{
    float: right;
    margin-top: 10px;
}}
.education, .experience {{
    clear: both;
}}
.education .school, .experience .company {{
    margin-bottom: 10px;
}}

h1 {{
    font-size: 30px;
    font-weight: bold;
    text-decoration: underline;
    color: #333;
}}

h2 {{
    font-size: 26px;
    font-weight: bold;
    text-decoration: underline;
    color: #333;
}}

h3 {{
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
    color: #333;
}}

p {{
    font-size: 20px;
    margin-bottom: 10px;
    color: #333;
}}

ul {{
    list-style-type: disc;
    margin-left: 20px;
}}

li {{
    font-size: 20px;
    color: #333;
}}
</style>
    
    <h1>{name}</h1>
    <h2>{profession}</h2>
    <h3>Contact Information</h3>
    <p>Phone: {phone}</p>
    <p>Email: {email}</p>

     <h3>Education</h3>
    <p>{education}</p>


    <h3>Experience</h3>
    <p>{experience}</p>

     <h3>Skills</h3>
    <p>{skills}</p>

    <h3>Awards</h3>
    <p>{awards}</p>
    '''
    # Create the PDF file with the specified wkhtmltopdf path
    pdfkit.from_string(pdf_content, 'resume.pdf', configuration=pdfkit_config)

# Main function to run the Streamlit app
def resume_generator():
    st.title('Resume Generator')

    # Create the resume form
    name = st.text_input('Name')
    profession = st.text_input('Profession')
    phone = st.text_input('Phone')
    email = st.text_input('Email')
    skills = st.text_area('Skills')
    experience = st.text_area('Experience')
    education = st.text_area('Education')
    awards = st.text_area('Awards')
    submit = st.button('Generate Resume')

    # Generate the resume PDF
    if submit:
        create_pdf(name, profession, phone, email, education , experience, skills, awards)
        with open('resume.pdf', 'rb') as f:
            base64_data = base64.b64encode(f.read()).decode()
        pdf_download_link = f'<a href="data:application/pdf;base64,{base64_data}" download="resume.pdf">Download Resume</a>'
        st.markdown(pdf_download_link, unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    resume_generator()
