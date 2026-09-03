from pathlib import Path

from docx import Document

from resume_parser import parse_resume


def create_test_resume(file_path, content):
    """
    Create a temporary DOCX resume for testing.
    """

    document = Document()

    for line in content.splitlines():
        document.add_paragraph(line)

    document.save(file_path)


def test_empty_resume():

    file_path = Path("test_empty_resume.docx")

    try:
        create_test_resume(file_path, "")

        try:
            parse_resume(str(file_path))
            assert False, "Expected ValueError for empty resume"

        except ValueError as error:
            assert "no readable text" in str(error).lower()

        print("Empty resume test passed!")

    finally:
        if file_path.exists():
            file_path.unlink()


def test_whitespace_resume():

    file_path = Path("test_whitespace_resume.docx")

    try:
        create_test_resume(
            file_path,
            "     \n\n      \n"
        )

        try:
            parse_resume(str(file_path))
            assert False, "Expected ValueError for whitespace resume"

        except ValueError as error:
            assert "no readable text" in str(error).lower()

        print("Whitespace resume test passed!")

    finally:
        if file_path.exists():
            file_path.unlink()


def test_resume_without_sections():

    file_path = Path("test_no_sections_resume.docx")

    content = """
    JOHN SMITH

    Email: john@example.com
    Phone: 9876543210

    Java
    Python
    SQL
    """

    try:
        create_test_resume(file_path, content)

        try:
            parse_resume(str(file_path))
            assert False, "Expected ValueError when no sections are found"

        except ValueError as error:
            assert "no recognizable resume sections" in str(error).lower()

        print("No-section resume test passed!")

    finally:
        if file_path.exists():
            file_path.unlink()


if __name__ == "__main__":

    test_empty_resume()
    test_whitespace_resume()
    test_resume_without_sections()

    print("\nAll invalid resume content tests passed!")