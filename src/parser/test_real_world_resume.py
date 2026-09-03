from resume_parser import parse_resume


def test_real_world_resume():

    docx_path = r"..\..\data\resumes\real_world_resume.docx"

    resume_data = parse_resume(docx_path)

    # Check top-level structure
    assert "name" in resume_data
    assert "contact" in resume_data
    assert "sections" in resume_data

    # Check candidate name
    assert resume_data["name"] == "JANE DOE"

    # Check contact information
    assert resume_data["contact"]["email"] == "jane.doe@example.com"
    assert resume_data["contact"]["phone"] == "9876543210"

    # Get sections
    sections = resume_data["sections"]

    # Expected sections
    expected_sections = [
        "summary",
        "education",
        "skills",
        "experience",
        "projects",
        "certifications",
        "achievements",
        "interests",
    ]

    # Verify every expected section exists
    for section in expected_sections:

        assert section in sections, (
            f"Missing section: {section}"
        )

    print("Real-world resume test passed!")

    print("\nCandidate:")
    print(resume_data["name"])

    print("\nContact:")
    print(resume_data["contact"])

    print("\nDetected sections:")

    for section in sections:
        print("-", section)


if __name__ == "__main__":

    test_real_world_resume()

    print("\nAll real-world resume tests passed!")