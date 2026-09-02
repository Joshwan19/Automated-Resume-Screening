# Import the resume parser
from resume_parser import parse_resume


# Path to the sample DOCX resume
docx_path = r"..\..\data\resumes\sample_resume.docx"


# Parse the resume
resume_data = parse_resume(docx_path)


# Display the structured resume data
for section, content in resume_data.items():
    print("\n---", section.upper(), "---")
    print(content)