# Import the PDF parser
from pdf_parser import extract_text_from_pdf

# Import the section splitter
from section_splitter import split_sections


# Path to the sample resume
pdf_path = r"..\..\data\resumes\sample_resume.pdf"


# Extract text from the PDF
text = extract_text_from_pdf(pdf_path)


# Split the extracted text into sections
sections = split_sections(text)


# Display the sections
for section, content in sections.items():
    print("\n---", section.upper(), "---")
    print(content)