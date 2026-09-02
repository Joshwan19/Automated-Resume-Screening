# Import the PDF parser
from pdf_parser import extract_text_from_pdf

# Import the DOCX parser
from doc_parser import extract_text_from_docx

# Import the section splitter
from section_splitter import split_sections


# Parse a resume file
def parse_resume(file_path):

    # Check if the file is a PDF
    if file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)

    # Check if the file is a DOCX
    elif file_path.lower().endswith(".docx"):
        text = extract_text_from_docx(file_path)

    # If the file type is not supported
    else:
        raise ValueError("Only PDF and DOCX files are supported.")

    # Split the extracted text into sections
    sections = split_sections(text)

    # Return the structured resume data
    return sections