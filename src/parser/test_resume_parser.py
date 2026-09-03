from pathlib import Path

from resume_parser import parse_resume


def test_pdf_resume():

    pdf_path = r"..\..\data\resumes\sample_resume.pdf"

    resume_data = parse_resume(pdf_path)

    assert "name" in resume_data
    assert "contact" in resume_data
    assert "sections" in resume_data

    sections = resume_data["sections"]

    assert "education" in sections
    assert "skills" in sections
    assert "experience" in sections
    assert "projects" in sections
    assert "certifications" in sections

    print("PDF resume test passed!")


def test_docx_resume():

    docx_path = r"..\..\data\resumes\sample_resume.docx"

    resume_data = parse_resume(docx_path)

    assert "name" in resume_data
    assert "contact" in resume_data
    assert "sections" in resume_data

    sections = resume_data["sections"]

    assert "education" in sections
    assert "skills" in sections
    assert "experience" in sections
    assert "projects" in sections
    assert "certifications" in sections

    print("DOCX resume test passed!")


def test_invalid_file():

    try:

        parse_resume(
            r"..\..\data\resumes\does_not_exist.pdf"
        )

    except FileNotFoundError:

        print("Invalid file test passed!")


def test_unsupported_file():

    test_file = Path(
        r"..\..\data\resumes\resume.txt"
    )

    test_file.write_text("This is a test file.")

    try:

        parse_resume(str(test_file))

    except ValueError as error:

        assert (
            "Only PDF and DOCX files are supported."
            in str(error)
        )

        print("Unsupported file test passed!")

    finally:

        test_file.unlink()


if __name__ == "__main__":

    test_pdf_resume()
    test_docx_resume()
    test_invalid_file()
    test_unsupported_file()

    print("\nAll resume parser tests passed!")