# Test the PDF parser
from pdf_parser import extract_text_from_pdf

# Path to the sample resume
pdf_path = r"data\resumes\sample_resume.pdf"

# Extract text
text = extract_text_from_pdf(pdf_path)

# Display the extracted text
print(text)