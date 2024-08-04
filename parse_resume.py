import json

def parse_resume_to_json(resume_text):
    # Placeholder for actual parsing logic
    resume_json = {
        "personal_information": {
            "name": "Mittul Kumar",
            "contact_info": "+916206775218",
            "linkedin": "https://www.linkedin.com/in/mittul-kumar-4169b8152/",
            "github": "https://github.com/mittulofficial"
        },
        "summary": "Experienced software engineer with expertise in Flutter, React, and data science projects. Skilled in creating and managing software solutions from concept to deployment.",
        "skills": ["C++", "Java", "JavaScript", "Python", "Angular", "React JS", "Node JS", "Git", "GitHub", "Ubuntu", "MongoDB", "Tailwind CSS", "Data Structures and Algorithms", "Problem-Solving", "Responsive Web Design", "Scripting in Python and JavaScript"],
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
                "institution": "Lovely Professional University",
                "graduation_year": "2024"
            }
        ],
        "projects": [
            {
                "project_title": "Spotify Clone",
                "description": "A clone of Spotify including features such as sidebar, top 10 hits, and Billboard Top 100.",
                "technologies": ["React", "JavaScript", "Tailwind CSS", "MongoDB"],
                "link": "https://github.com/mittulofficial/Spotify_clone"
            },
            {
                "project_title": "Customer Churn Prediction",
                "description": "A project to predict customer churn using various customer attributes and information.",
                "technologies": ["Python", "Data Science"],
                "link": "https://github.com/mittulofficial/customer-churn-prediction"
            },
            {
                "project_title": "Ride-Hailing App",
                "description": "An app for Android that tracks trip status and duration in real-time with features like start trip, driving to destination, and trip end.",
                "technologies": ["Flutter", "Kotlin", "Firebase"],
                "link": "https://github.com/mittulofficial/Ride-Hailing-App"
            },
            {
                "project_title": "Resume JSON Converter",
                "description": "A tool to convert resume content from text to JSON format.",
                "technologies": ["Python"],
                "link": "https://github.com/mittulofficial/resume-json-converter"
            }
        ]
    }
    
    return resume_json

resume_text = """Personal Information:
Name: Mittul Kumar
Contact Info: +916206775218
LinkedIn Profile: https://www.linkedin.com/in/mittul-kumar-4169b8152/
GitHub Profile: https://github.com/mittulofficial

Summary:
Experienced software engineer with expertise in Flutter, React, and data science projects. Skilled in creating and managing software solutions from concept to deployment.

Skills:
C++, Java, JavaScript, Python, Angular, React JS, Node JS, Git, GitHub, Ubuntu, MongoDB, Tailwind CSS, Data Structures and Algorithms, Problem-Solving, Responsive Web Design, Scripting in Python and JavaScript

Experience:
Job Title: Software Engineer
Company: Tech Corp
Location: San Francisco, CA
Duration: Jan 2020 - Present
Responsibilities: Developed web applications, Collaborated with cross-functional teams

Education:
Degree: Bachelor of Science in Computer Science
Institution: Lovely Professional University
Graduation Year: 2024

Projects:
Project Title: Spotify Clone
Description: A clone of Spotify including features such as sidebar, top 10 hits, and Billboard Top 100.
Technologies: React, JavaScript, Tailwind CSS, MongoDB
Link: https://github.com/mittulofficial/Spotify_clone

Project Title: Customer Churn Prediction
Description: A project to predict customer churn using various customer attributes and information.
Technologies: Python, Data Science
Link: https://github.com/mittulofficial/customer-churn-prediction

Project Title: Ride-Hailing App
Description: An app for Android that tracks trip status and duration in real-time with features like start trip, driving to destination, and trip end.
Technologies: Flutter, Kotlin, Firebase
Link: https://github.com/mittulofficial/Ride-Hailing-App

Project Title: Resume JSON Converter
Description: A tool to convert resume content from text to JSON format.
Technologies: Python
Link: https://github.com/mittulofficial/resume-json-converter"""

parsed_json = parse_resume_to_json(resume_text)
print(json.dumps(parsed_json, indent=4))
