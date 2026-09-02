# Split resume text into different sections
def split_sections(text):

    sections = {}

    current_section = None

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        heading = line.upper()

        if heading in [
            "EDUCATION",
            "SKILLS",
            "EXPERIENCE",
            "PROJECTS",
            "CERTIFICATIONS"
        ]:
            current_section = heading.lower()
            sections[current_section] = ""

        elif current_section:
            sections[current_section] += line + "\n"

    return sections