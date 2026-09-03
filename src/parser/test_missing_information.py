from pathlib import Path

from docx import Document

from resume_parser import parse_resume


def create_test_resume(file_path, content):
    """
    Create a temporary DOCX resume for testing.
    """

    document = Document()

    for line in content.strip().splitlines():
        document.add_paragraph(line)

    document.save(file_path)


def test_missing_phone():

    file_path = Path("test_missing_phone.docx")

    content = """
    JOHN SMITH

    Email: john@example.com

    EDUCATION
    Bachelor of Engineering in Computer Science

    SKILLS
    Java
    Python
    SQL
    """

    try:

        create_test_resume(file_path, content)

        resume_data = parse_resume(str(file_path))

        assert resume_data["name"] == "JOHN SMITH"

        assert resume_data["contact"]["email"] == "john@example.com"

        assert resume_data["contact"]["phone"] is None

        print("Missing phone test passed!")

    finally:

        if file_path.exists():
            file_path.unlink()


def test_missing_email():

    file_path = Path("test_missing_email.docx")

    content = """
    JOHN SMITH

    Phone: 9876543210

    EDUCATION
    Bachelor of Engineering in Computer Science

    SKILLS
    Java
    Python
    SQL
    """

    try:

        create_test_resume(file_path, content)

        resume_data = parse_resume(str(file_path))

        assert resume_data["name"] == "JOHN SMITH"

        assert resume_data["contact"]["email"] is None

        assert resume_data["contact"]["phone"] == "9876543210"

        print("Missing email test passed!")

    finally:

        if file_path.exists():
            file_path.unlink()


def test_missing_optional_sections():

    file_path = Path("test_missing_sections.docx")

    content = """
    JOHN SMITH

    Email: john@example.com
    Phone: 9876543210

    EDUCATION
    Bachelor of Engineering in Computer Science

    SKILLS
    Java
    Python
    SQL
    """

    try:

        create_test_resume(file_path, content)

        resume_data = parse_resume(str(file_path))

        sections = resume_data["sections"]

        assert "education" in sections
        assert "skills" in sections

        assert "projects" not in sections
        assert "certifications" not in sections

        print("Missing optional sections test passed!")

    finally:

        if file_path.exists():
            file_path.unlink()


if __name__ == "__main__":

    test_missing_phone()
    test_missing_email()
    test_missing_optional_sections()

    print("\nAll missing information tests passed!")