import re


# Different headings commonly found in resumes
SECTION_ALIASES = {
    "summary": {
        "SUMMARY",
        "PROFESSIONAL SUMMARY",
        "CAREER SUMMARY",
        "PROFILE",
        "PROFESSIONAL PROFILE",
        "CAREER OBJECTIVE",
        "OBJECTIVE",
    },

    "education": {
        "EDUCATION",
        "EDUCATIONAL QUALIFICATION",
        "EDUCATIONAL QUALIFICATIONS",
        "ACADEMIC QUALIFICATION",
        "ACADEMIC QUALIFICATIONS",
        "EDUCATIONAL BACKGROUND",
        "ACADEMIC BACKGROUND",
    },

    "skills": {
        "SKILLS",
        "TECHNICAL SKILLS",
        "TECHNOLOGY SKILLS",
        "CORE SKILLS",
        "KEY SKILLS",
        "TECHNOLOGIES",
        "TECHNICAL EXPERTISE",
        "TECHNOLOGY STACK",
    },

    "experience": {
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "PROFESSIONAL EXPERIENCE",
        "WORK HISTORY",
        "EMPLOYMENT HISTORY",
        "EMPLOYMENT EXPERIENCE",
        "PROFESSIONAL HISTORY",
    },

    "projects": {
        "PROJECTS",
        "ACADEMIC PROJECTS",
        "PERSONAL PROJECTS",
        "PROFESSIONAL PROJECTS",
        "KEY PROJECTS",
    },

    "certifications": {
        "CERTIFICATIONS",
        "CERTIFICATES",
        "PROFESSIONAL CERTIFICATIONS",
    },

    "achievements": {
        "ACHIEVEMENTS",
        "AWARDS",
        "HONORS",
        "HONOURS",
    },

    "languages": {
        "LANGUAGES",
        "LANGUAGE SKILLS",
    },

    "interests": {
        "INTERESTS",
        "HOBBIES",
        "INTERESTS AND HOBBIES",
    },
}


def normalize_heading(line):
    """
    Normalize a possible resume heading.
    """

    # Remove leading/trailing whitespace
    heading = line.strip()

    # Remove common numbering/bullet formats
    heading = re.sub(
        r"^(?:\d+(?:\.\d+)*[\s.)-]+|[-•▪●]\s*)",
        "",
        heading
    )

    # Remove trailing colon
    heading = heading.rstrip(":")

    # Normalize multiple spaces
    heading = re.sub(r"\s+", " ", heading)

    # Convert to uppercase
    return heading.upper().strip()


def detect_section_heading(line):
    """
    Return the internal section name if the line
    is a recognized resume heading.
    """

    heading = normalize_heading(line)

    for section, aliases in SECTION_ALIASES.items():
        if heading in aliases:
            return section

    return None


def split_sections(text):
    """
    Split extracted resume text into structured sections.
    """

    sections = {}
    current_section = None

    for line in text.splitlines():

        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Check whether this line is a section heading
        detected_section = detect_section_heading(line)

        if detected_section:

            current_section = detected_section

            # Create section only once
            if current_section not in sections:
                sections[current_section] = ""

            continue

        # Add normal content to the current section
        if current_section:
            sections[current_section] += line + "\n"

    # Remove unnecessary trailing whitespace
    for section in sections:
        sections[section] = sections[section].strip()

    return sections