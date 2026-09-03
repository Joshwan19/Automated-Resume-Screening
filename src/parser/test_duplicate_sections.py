from section_splitter import split_sections


def test_duplicate_sections():

    resume_text = """
    JOHN SMITH

    EDUCATION
    Bachelor of Engineering in Computer Science
    ABC Engineering College

    PROJECTS
    Student Management System
    Java-based application

    PROJECTS
    Online Career Guidance System
    Python-based application

    SKILLS
    Java
    Python
    SQL
    """

    sections = split_sections(resume_text)

    assert "education" in sections
    assert "projects" in sections
    assert "skills" in sections

    # Both project entries should be preserved
    assert "Student Management System" in sections["projects"]
    assert "Online Career Guidance System" in sections["projects"]

    print("Duplicate section test passed!")

    print("\nProjects section:")
    print(sections["projects"])


if __name__ == "__main__":

    test_duplicate_sections()

    print("\nAll duplicate section tests passed!")