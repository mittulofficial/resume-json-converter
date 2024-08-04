# Resume JSON Converter

This repository contains a Python script designed to convert resume content from a plain text format into a structured JSON format. The purpose of this tool is to facilitate the extraction and organization of resume data for various applications, such as automated resume screening, data analysis, or integration with other systems.

## Overview

The script parses a resume provided in text format and converts it into a JSON object with the following structure:

1. **Personal Information**: Includes details like name, contact info, LinkedIn profile, and GitHub profile.
2. **Summary**: A brief overview of the candidate's qualifications and career goals.
3. **Skills**: A list of relevant skills.
4. **Experience**: Job roles, companies, locations, time periods, and key responsibilities.
5. **Education**: Degrees, institutions, and graduation years.
6. **Projects**: Titles, descriptions, technologies used, and links (if any).

## Features

- **Flexible Input**: The script can handle resumes formatted in plain text.
- **Structured Output**: Converts the resume into a well-organized JSON format.
- **Easy Integration**: The JSON output can be easily integrated into other systems or used for data analysis.

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/mittulofficial/resume-json-converter.git
2.**Navigate to the Project Directory

   ```bash
    cd resume-json-converter
    
 ```

3.**Install Dependencies
Ensure you have Python installed. The script does not require any external libraries beyond the Python standard library.


#Example
Here is an example of how the resume content should be formatted:
Personal Information:

Name: John Doe
Contact Info: john.doe@example.com
LinkedIn Profile: https://linkedin.com/in/johndoe
GitHub Profile: https://github.com/johndoe

Summary:
Experienced software engineer with a passion for developing innovative programs...

Skills:
Python, JavaScript, React, Node.js

Experience:
Job Title: Software Engineer
Company: Tech Corp
Location: San Francisco, CA
Duration: Jan 2020 - Present
Responsibilities: Developed web applications, Collaborated with cross-functional teams

Education:
Degree: Bachelor of Science in Computer Science
Institution: XYZ University
Graduation Year: 2019

Projects:
Project Title: Portfolio Website
Description: A personal website showcasing projects and skills.
Technologies: HTML, CSS, JavaScript
Link: https://github.com/johndoe/portfolio


