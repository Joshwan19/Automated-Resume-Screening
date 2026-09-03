from section_splitter import detect_section_heading


def test_numbered_headings():

    test_cases = {
        "1. EDUCATION": "education",
        "2. TECHNICAL SKILLS": "skills",
        "3. WORK EXPERIENCE": "experience",
        "4. PROJECTS": "projects",
        "5. CERTIFICATIONS": "certifications",
    }

    for heading, expected in test_cases.items():

        result = detect_section_heading(heading)

        assert result == expected, (
            f"Failed: {heading} "
            f"Expected={expected}, Got={result}"
        )

    print("Numbered heading tests passed!")


def test_bullet_headings():

    test_cases = {
        "• EDUCATION": "education",
        "• TECHNICAL SKILLS": "skills",
        "- WORK EXPERIENCE": "experience",
        "▪ PROJECTS": "projects",
        "● CERTIFICATIONS": "certifications",
    }

    for heading, expected in test_cases.items():

        result = detect_section_heading(heading)

        assert result == expected, (
            f"Failed: {heading} "
            f"Expected={expected}, Got={result}"
        )

    print("Bullet heading tests passed!")


def test_colon_headings():

    test_cases = {
        "EDUCATION:": "education",
        "TECHNICAL SKILLS:": "skills",
        "WORK EXPERIENCE:": "experience",
        "PROJECTS:": "projects",
        "CERTIFICATIONS:": "certifications",
    }

    for heading, expected in test_cases.items():

        result = detect_section_heading(heading)

        assert result == expected, (
            f"Failed: {heading} "
            f"Expected={expected}, Got={result}"
        )

    print("Colon heading tests passed!")


def test_mixed_case_headings():

    test_cases = {
        "Education": "education",
        "Technical Skills": "skills",
        "Work Experience": "experience",
        "Academic Projects": "projects",
        "Certificates": "certifications",
    }

    for heading, expected in test_cases.items():

        result = detect_section_heading(heading)

        assert result == expected, (
            f"Failed: {heading} "
            f"Expected={expected}, Got={result}"
        )

    print("Mixed-case heading tests passed!")


if __name__ == "__main__":

    test_numbered_headings()
    test_bullet_headings()
    test_colon_headings()
    test_mixed_case_headings()

    print("\nAll heading variation tests passed!")