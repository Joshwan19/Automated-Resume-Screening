# Import the resume parser
from resume_parser import parse_resume


# Ask the user for the resume file path
file_path = input("Enter the path of your resume: ")


try:
    # Parse the resume
    resume_data = parse_resume(file_path)

    # Display the structured resume data
    for section, content in resume_data.items():
        print("\n---", section.upper(), "---")
        print(content)

except Exception as error:
    print("Error:", error)