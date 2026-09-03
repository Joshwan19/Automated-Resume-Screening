from section_splitter import split_sections


def test_special_characters_in_resume():

    resume_text = """
    JOHN SMITH

    TECHNICAL SKILLS
    C++
    C#
    .NET
    Node.js
    React.js
    Machine Learning (ML)
    HTML/CSS
    REST API
    Git/GitHub

    PROJECTS
    C++ Banking Application
    .NET Web Application
    React.js Portfolio Website
    """

    sections = split_sections(resume_text)

    assert "skills" in sections
    assert "projects" in sections

    skills = sections["skills"]
    projects = sections["projects"]

    # Verify special-character technologies are preserved
    assert "C++" in skills
    assert "C#" in skills
    assert ".NET" in skills
    assert "Node.js" in skills
    assert "React.js" in skills
    assert "Machine Learning (ML)" in skills
    assert "HTML/CSS" in skills
    assert "REST API" in skills
    assert "Git/GitHub" in skills

    # Verify project names are preserved
    assert "C++ Banking Application" in projects
    assert ".NET Web Application" in projects
    assert "React.js Portfolio Website" in projects

    print("Special character test passed!")


if __name__ == "__main__":

    test_special_characters_in_resume()

    print("\nAll special character tests passed!")