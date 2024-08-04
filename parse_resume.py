import json

def parse_resume_to_json(resume_text):
    # Placeholder for actual parsing logic
    resume_json = {
        "personal_information": {
            "name": "John Doe",
            "contact_info": "john.doe@example.com",
            "linkedin": "https://linkedin.com/in/johndoe",
            "github": "https://github.com/johndoe"
        },
        "summary": "Experienced software engineer with a passion for developing innovative programs...",
        "skills": ["Python", "JavaScript", "React", "Node.js"],
        "experience": [
            {
                "job_title": "Software Engineer",
                "company": "Tech Corp",
                "location": "San Francisco, CA",
                "duration": "Jan 2020 - Present",
                "responsibilities": ["Developed web applications", "Collaborated with cross-functional teams"]
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science in Computer Science",
                "institution": "XYZ University",
                "graduation_year": "2019"
            }
        ],
        "projects": [
            {
                "project_title": "Portfolio Website",
                "description": "A personal website showcasing projects and skills.",
                "technologies": ["HTML", "CSS", "JavaScript"],
                "link": "https://github.com/johndoe/portfolio"
            }
        ]
    }
    
    return resume_json

resume_text = """Your resume text here"""
parsed_json = parse_resume_to_json(resume_text)
print(json.dumps(parsed_json, indent=4))
